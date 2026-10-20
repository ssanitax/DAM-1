Flask se utiliza para construir aplicaciones donde la información no es estática, sino que depende de las acciones del usuario. La importancia de esta práctica reside en el uso del objeto `request`, que actúa como un receptor de los datos que viajan a través de la URL (parámetros GET).

Cuando un usuario rellena un formulario y pulsa "Enviar", el navegador construye una URL con una estructura específica (ej. `?nombre=ana&apellidos=sanchez`). Nosotros, en el servidor, debemos ser capaces de "cazar" esos valores para realizar acciones como guardarlos en una base de datos o simplemente mostrarlos de vuelta al usuario.

---

1. El Servidor Python (`004 - lanzamos los datos.py`)

utilizamos dos rutas: una para mostrar el formulario (`/`) y otra para procesar la llegada de la información (`/envio`).

```
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
```

2. El Formulario HTML (`templates/index.html`)

Definimos los campos de entrada. Es vital que el atributo `name` del `<input>` coincida exactamente con el texto que nosotros busquemos en el `request.args.get` de Python.

```
<!doctype html>
<html lang="es">
  <head>
    <title>Micro formulario</title>
    <meta charset="utf-8">
    <style>
      /* Aplicamos un diseño centrado y limpio */
      html, body { background: indigo; display: flex; justify-content: center; align-items: center; min-height: 100vh; font-family: sans-serif; }
      form { width: 350px; padding: 30px; background: white; border-radius: 10px; display: flex; flex-direction: column; gap: 15px; }
      input { padding: 12px; border: 1px solid #ccc; border-radius: 5px; }
      input[type="submit"] { background: indigo; color: white; cursor: pointer; border: none; font-weight: bold; }
    </style>
  </head>
  <body>
    <form action="/envio" method="GET">
      <input type="text" name="nombre" placeholder="Introduce tu nombre" required>
      <input type="text" name="apellidos" placeholder="Introduce tus apellidos" required>
      <input type="submit" value="Enviar Datos">
    </form>
  </body>
</html>
```

---

Flask permite gestionar el flujo de información de manera profesional y sencilla. Al dominar el uso de formularios y parámetros de URL, estamos capacitados para construir aplicaciones web donde el usuario es el protagonista, permitiendo desde simples registros hasta la búsqueda en catálogos complejos.

Esta estructura modular, donde el HTML reside en una carpeta de plantillas y Python gestiona la lógica, es el pilar de los proyectos escalables que nosotros desarrollaremos en el futuro.
