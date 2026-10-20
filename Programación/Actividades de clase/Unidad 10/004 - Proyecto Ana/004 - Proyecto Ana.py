from flask import Flask, render_template, request, jsonify
import subprocess
import threading
import queue
import uuid
import os
import tempfile

app = Flask(__name__)

sessions = {}

class PythonSession:
    def __init__(self, code: str):
        # Creamos archivo temporal para el código
        fd, path = tempfile.mkstemp(suffix=".py", prefix="compilador_")
        os.write(fd, code.encode("utf-8"))
        os.close(fd)
        self.path = path
        
        # Iniciamos el proceso con tuberías para stdin y stdout
        self.proc = subprocess.Popen(
            ["python3", self.path],
            stdin=subprocess.PIPE, stdout=subprocess.PIPE,
            stderr=subprocess.PIPE, text=True, bufsize=1
        )
        self.queue = queue.Queue()
        self.alive = True
        
        # Hilo para leer la salida sin bloquear el servidor
        self.thread = threading.Thread(target=self._reader_thread, daemon=True)
        self.thread.start()

    def _reader_thread(self):
        try:
            for line in self.proc.stdout:
                self.queue.put(line)
        finally:
            self.proc.wait()
            self.alive = False
            if os.path.exists(self.path): os.remove(self.path)

    def write(self, data: str):
        if self.alive:
            self.proc.stdin.write(data + "\n")
            self.proc.stdin.flush()

    def read_all(self) -> str:
        chunks = []
        while not self.queue.empty():
            chunks.append(self.queue.get_nowait())
        return "".join(chunks)

@app.route("/")
def inicio():
    return render_template("frentemasampliado.html")

@app.route("/api/start", methods=["POST"])
def api_start():
    data = request.get_json(force=True)
    session_id = str(uuid.uuid4())
    sessions[session_id] = PythonSession(data.get("code", ""))
    return jsonify({"session_id": session_id})

@app.route("/api/write", methods=["POST"])
def api_write():
    data = request.get_json(force=True)
    sess = sessions.get(data.get("session_id"))
    if sess:
        sess.write(data.get("line", ""))
        return jsonify({"ok": True})
    return jsonify({"error": "No hay sesión"}), 404

@app.route("/api/read", methods=["GET"])
def api_read():
    sess = sessions.get(request.args.get("session_id"))
    if sess:
        return jsonify({"output": sess.read_all(), "alive": sess.alive})
    return jsonify({"error": "No hay sesión"}), 404

if __name__ == "__main__":
    app.run(debug=True)
