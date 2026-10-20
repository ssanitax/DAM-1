Crear un sistema de Login sirve para proteger la privacidad y la integridad de los datos en una aplicación. La arquitectura se basa en el intercambio de informacíon entre el clienre y el servidor. El navegador envía las credenciales mediante el método POST y el servidor realiza una consulta `SELECT` filtrada para verificar si existe una coincidencia exacta en la base de datos.

La importancia de estre ejercicio está en usar `session_start`. Que la usaremos para que el servidor recuerde que un usuario ya se ha identificado con éxito, permitiéndole navegar por páginas protegidas sin tener que reintroducir su contraseña constantemente.

---

Creamos la base de datos:

```
CREATE DATABASE IF NOT EXISTS superaplicacion;
USE superaplicacion;

CREATE TABLE IF NOT EXISTS usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario VARCHAR(50) NOT NULL UNIQUE,
    contrasena VARCHAR(255) NOT NULL,
    nombrecompleto VARCHAR(150) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE
);
```

Creamos el procesamiento del Login.

```
<?php
  session_start();
  $conexion = new mysqli("localhost", "superaplicacion", "Superaplicacion123$", "superaplicacion");
  
  // Nosotros buscamos al usuario con la contraseña proporcionada
  $sql = "SELECT * FROM usuarios WHERE usuario = '".$_POST['usuario']."' AND contrasena = '".$_POST['contrasena']."';";
  $resultado = $conexion->query($sql);

  if ($fila = $resultado->fetch_assoc()) {
    $_SESSION['usuario'] = 'si'; // Nosotros autorizamos la sesión
    header("Location: exito.php");
  } else {
    header("Location: login.html"); // Nosotros denegamos el acceso
  }
  $conexion->close();
?>
```

Realizamos la estructura del diagrama en json, con la aplicación de diagramas de Jocarsa.

```
{
  "formas": [
    {
      "id": "forma-1",
      "tipo": "rectangle",
      "left": "145.417px",
      "top": "158.715px",
      "width": "",
      "height": "",
      "texto": "Login"
    },
    {
      "id": "forma-2",
      "tipo": "rectangle",
      "left": "314.305px",
      "top": "158.198px",
      "width": "",
      "height": "",
      "texto": "Comprobación"
    },
    {
      "id": "forma-3",
      "tipo": "pill",
      "left": "469.554px",
      "top": "110.588px",
      "width": "",
      "height": "",
      "texto": "exito"
    },
    {
      "id": "forma-4",
      "tipo": "rectangle",
      "left": "609.558px",
      "top": "55.8232px",
      "width": "",
      "height": "",
      "texto": "Panel"
    },
    {
      "id": "forma-5",
      "tipo": "pill",
      "left": "447.632px",
      "top": "246.76px",
      "width": "",
      "height": "",
      "texto": "no exito"
    }
  ],
  "flechas": [
    {
      "desde": {
        "shapeId": "forma-1",
        "propId": null,
        "side": null
      },
      "hasta": {
        "shapeId": "forma-2",
        "propId": null,
        "side": null
      },
      "tipo": "simple",
      "estilo": "straight"
    },
    {
      "desde": {
        "shapeId": "forma-2",
        "propId": null,
        "side": null
      },
      "hasta": {
        "shapeId": "forma-3",
        "propId": null,
        "side": null
      },
      "tipo": "simple",
      "estilo": "straight"
    },
    {
      "desde": {
        "shapeId": "forma-2",
        "propId": null,
        "side": null
      },
      "hasta": {
        "shapeId": "forma-5",
        "propId": null,
        "side": null
      },
      "tipo": "simple",
      "estilo": "straight"
    },
    {
      "desde": {
        "shapeId": "forma-3",
        "propId": null,
        "side": null
      },
      "hasta": {
        "shapeId": "forma-4",
        "propId": null,
        "side": null
      },
      "tipo": "simple",
      "estilo": "straight"
    },
    {
      "desde": {
        "shapeId": "forma-5",
        "propId": null,
        "side": null
      },
      "hasta": {
        "shapeId": "forma-1",
        "propId": null,
        "side": null
      },
      "tipo": "simple",
      "estilo": "straight"
    }
  ]
}
```

---

Un sistema de login es el resultado de la coordinación perfecta entre el diseño de bases de datos, la programación del servidor y la interfaz de usuario. El uso de sesiones es el componente clave que permite crear una experiencia de usuario fluida y segura.

Dominar este flujo nos permite sentar las bases para proyectos más complejos, como paneles de administración o redes sociales, donde nosotros debemos gestionar múltiples perfiles y niveles de acceso de forma profesional.
