from flask import Flask, render_template, request

app = Flask(__name__)

# Servimos el formulario inicial
@app.route("/")
def inicio():
    return render_template("index.html")

# Procesamos los datos enviados
@app.route("/envio")
def envio():
    # Extraemos los parámetros de la URL
    nombre = request.args.get("nombre")
    apellidos = request.args.get("apellidos")
    # Devolvemos una respuesta personalizada al navegador
    return "Nombre recibido: " + nombre + " - Apellidos recibidos: " + apellidos

if __name__ == "__main__":
    app.run(debug=True)
