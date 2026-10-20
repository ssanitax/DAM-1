En este ejercicio, aplicamos conceptos avanzados de Programación Orientada a Objetos y gestión de sistemas operativos para crear un complilador web funcional. La arquitectura se basa en la Composición de clases mediante la creación de `PythonSession`, una clase que encapsula la ejecución de un proceso secundario independiente para cada usuario.

Utilizamos el método `subprocess` de Python para abrir tuberías de comunicación que conectan la entrada y la salida del proceso remoto con nuestra interfaz web. Esta técnica es fundamental en el desarrollo de herramientas de computación en la nube y entornos de aprendizaje, ya que permite que el servidor ejecute código de forma aislada y segura mientras mantiene una sesión viva y persistente para interactuar con funciones como `input()`.

---

Primero importamos las librerías necesarias. Importamos `Flask` para crear el servidor web y manejar las peticiones, y el resto de librerías para poder ejecutar código Python, manejar procesos, hilos y archivos temporales.

```
from flask import Flask, render_template, request, jsonify
import subprocess
import threading
import queue
import uuid
import os
import tempfile
```

Creamos la aplicación Flask y un diccionario llamado `sessions` donde se guardarán todas las ejecuciones activas.

```
app = Flask(__name__)
sessions = {}
```

Creamos la clase `PythonSession`. Esta clase representa una ejecución de un programa Python independiente.

```
class PythonSession:
```

En el constructor, guardamos el código en un archivo temporal. Cuando se crea una sesión, recibimos el código Python como texto y lo guardamos en un archivo `.py` temporal.

```
def __init__(self, code: str):
    fd, path = tempfile.mkstemp(suffix=".py", prefix="compilador_")
    os.write(fd, code.encode("utf-8"))
    os.close(fd)
    self.path = path
```

Después, lanzamos el archivo Python como un proceso externo y habilitamos la entrada y salida.

```
self.proc = subprocess.Popen(
    ["python3", self.path],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True,
    bufsize=1
)
```

Creamos una cola para guardar la salida del programa y una variable para saber si sigue en ejecución.

```
self.queue = queue.Queue()
self.alive = True
```

Usamos un hilo para leer la salida del programa en segundo plano.

```
self.thread = threading.Thread(
    target=self._reader_thread,
    daemon=True
)
self.thread.start()
```

Este método se ejecuta en el hilo y lee cada línea que imprime el programa.

```
def _reader_thread(self):
    try:
        for line in self.proc.stdout:
            self.queue.put(line)
```

Cuando el proceso acaba, marcamos la sesión como terminada y borramos el archivo temporal.

```
    finally:
        self.proc.wait()
        self.alive = False
        if os.path.exists(self.path):
            os.remove(self.path)
```

Método `write()` para enviar datos al programa. Este método envía texto al `input()` del programa que se está ejecutando.

```
def write(self, data: str):
    if self.alive:
        self.proc.stdin.write(data + "\n")
        self.proc.stdin.flush()
```

Método `read_all()` para leer toda la salida disponible. Este método lee toda la salida acumulada en la cola y la devuelve como texto.

```
def read_all(self) -> str:
    chunks = []
    while not self.queue.empty():
        chunks.append(self.queue.get_nowait())
    return "".join(chunks)
```

Ruta principal `/`. Esta ruta carga el archivo HTML que contiene la interfaz del compilador.

```
@app.route("/")
def inicio():
    return render_template("frentemasampliado.html")
```

Ruta `/api/start` para iniciar una sesión. Recibe el código Python desde el frontend, crea una nueva sesión y devuelve su ID.

```
@app.route("/api/start", methods=["POST"])
def api_start():
    data = request.get_json(force=True)
    session_id = str(uuid.uuid4())
    sessions[session_id] = PythonSession(data.get("code", ""))
    return jsonify({"session_id": session_id})
```

Ruta `/api/write` para enviar entrada al programa. Permite enviar texto al programa que está esperando un `input()`.

```
@app.route("/api/write", methods=["POST"])
def api_write():
    data = request.get_json(force=True)
    sess = sessions.get(data.get("session_id"))
    if sess:
        sess.write(data.get("line", ""))
        return jsonify({"ok": True})
```

Ruta `/api/read` para leer la salida del programa. Devuelve toda la salida nueva y el estado del proceso.

```
@app.route("/api/read", methods=["GET"])
def api_read():
    sess = sessions.get(request.args.get("session_id"))
    if sess:
        return jsonify({
            "output": sess.read_all(),
            "alive": sess.alive
        })
```

Arrancamos el servidor Flask. Por último, arrancamos el servidor en modo desarrollo.

```
if __name__ == "__main__":
    app.run(debug=True)
```

---

El código:

Python

```
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
```

HTML:

```
<!doctype html>
<html lang="es">
  <head>
    <meta charset="utf-8" />
    <title>compilador.ssanitax.com</title>
    <style>
      :root {
        --bg: #f3f4f6;
        --panel: #ffffff;
        --border: #d4d4d8;
        --accent: #16a34a;
        --text: #111827;
        --terminal-bg: #111827;
        --terminal-text: #e5e7eb;
      }
      * { box-sizing: border-box; }
      body {
        margin: 0; min-height: 100vh;
        font-family: system-ui, -apple-system, sans-serif;
        background: radial-gradient(circle at top, #e5e7eb 0, #f9fafb 55%);
        display: flex; justify-content: center; align-items: center;
      }
      .app-shell {
        background: var(--panel); border-radius: 18px; border: 1px solid var(--border);
        box-shadow: 0 20px 50px rgba(15, 23, 42, 0.08); padding: 22px; width: 1000px;
      }
      .layout { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; }
      .panel { border: 1px solid #e4e4e7; border-radius: 14px; padding: 12px; display: flex; flex-direction: column; }
      #editor { 
        flex: 1; height: 350px; font-family: 'JetBrains Mono', monospace; 
        background: #f9fafb; padding: 10px; border-radius: 8px; border: 1px solid #ddd; outline: none; 
      }
      #terminal-log { 
        height: 315px; background: var(--terminal-bg); color: var(--terminal-text); 
        font-family: monospace; padding: 10px; border-radius: 8px; overflow-y: auto; white-space: pre-wrap; 
      }
      .btn-main { 
        margin-top: 10px; padding: 12px; background: var(--accent); color: white; 
        border: none; border-radius: 999px; cursor: pointer; width: 100%; font-weight: bold; 
      }
      #terminal-input { 
        margin-top: 10px; width: 100%; padding: 10px; border-radius: 8px; 
        border: 1px solid var(--border); font-family: monospace;
      }
      .status { font-size: 12px; margin-top: 5px; color: #6b7280; }
    </style>
  </head>
  <body>
    <div class="app-shell">
      <header style="margin-bottom: 20px;">
        <h1 style="font-size: 20px; margin: 0;">compilador.ssanitax.com</h1>
        <div class="status" id="status-text">Estado: <span>listo</span></div>
      </header>
      <div class="layout">
        <div class="panel">
          <textarea id="editor" spellcheck="false">
nombre = input("¿Cómo te llamas? ")
print("Hola", nombre)
edad = int(input("¿Qué edad tienes? "))
print("El año que viene tendrás", edad + 1)</textarea>
          <button id="run" class="btn-main">EJECUTAR PROGRAMA</button>
        </div>
        <div class="panel">
          <pre id="terminal-log">$ Consola lista...</pre>
          <input id="terminal-input" type="text" placeholder="Escribe aquí para input()..." />
          <div class="status">Pulsa Enter para enviar datos a <code>stdin</code></div>
        </div>
      </div>
    </div>

    <script>
      const editor = document.querySelector("#editor");
      const terminalLog = document.querySelector("#terminal-log");
      const terminalInput = document.querySelector("#terminal-input");
      const runButton = document.querySelector("#run");
      const statusText = document.querySelector("#status-text span");

      let sessionId = null;
      let readInterval = null;

      function stopSession() {
        if (readInterval) clearInterval(readInterval);
        readInterval = null;
        sessionId = null;
        statusText.textContent = "finalizado";
      }

      function startReadLoop() {
        readInterval = setInterval(() => {
          if (!sessionId) return;
          fetch("/api/read?session_id=" + encodeURIComponent(sessionId))
            .then(r => r.json())
            .then(data => {
              if (data.output) {
                terminalLog.textContent += data.output;
                terminalLog.scrollTop = terminalLog.scrollHeight; // Nosotros mantenemos el scroll abajo
              }
              if (!data.alive) {
                stopSession();
              }
            })
            .catch(err => stopSession());
        }, 300); // Nosotros consultamos cada 300ms
      }

      runButton.onclick = () => {
        stopSession();
        terminalLog.textContent = "$ python3 programa.py\n";
        statusText.textContent = "iniciando...";
        
        fetch("/api/start", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ code: editor.value })
        })
        .then(r => r.json())
        .then(data => {
          if (data.session_id) {
            sessionId = data.session_id;
            statusText.textContent = "ejecutando";
            startReadLoop();
          }
        });
      };

      terminalInput.onkeydown = (e) => {
        if (e.key === "Enter" && sessionId) {
          const line = terminalInput.value;
          terminalLog.textContent += "> " + line + "\n"; // Eco local
          
          fetch("/api/write", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ session_id: sessionId, line: line })
          });
          terminalInput.value = "";
        }
      };
    </script>
  </body>
</html>
```

---

Hemos comprobado que la integración de hilos en el servidor y bucles de consulta en el cliente permite transformar una página estática en una consola profesional interactiva. Al organizar el código con una lógica de sesiones persistentes, garantizamos que cada ejecución sea independiente, fluida y capaz de responder a las entradas del usuario en tiempo real.
