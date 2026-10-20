PHP sirve como motor de renderizado para "dibujar" contenido dinámico en el navegador a partir de una base de datos. La importancia de esta práctica reside en el uso de la extensión mysqli, que nos permite establecer una conexión segura con el servidor MySQL, ejecutar consultas y recorrer los resultados mediante bucles para generar etiquetas HTML de forma automática.

Para que podamos visualizar los datos, el servidor debe tener instalado el conector correspondiente. Si detectamos que el código no funciona en un entorno Linux, es probable que necesitemos instalarlo manualmente mediante el comando `sudo apt install php-mysqli`.

---

1. Preparación del Backend (`le damos forma.php`)

Debemos asegurar que la lógica de conexión sea sólida. El script se encarga de abrir el "túnel" hacia la base de datos blogphp y extraer cada fila de la tabla blog para convertirla en un artículo de texto.

```
<?php
  // Definimos las credenciales de acceso
  $host = "localhost";
  $user = "blogphp";
  $pass = "Blogphp123$";
  $db   = "blogphp";

  // Establecemos la conexión
  $conexion = new mysqli($host, $user, $pass, $db);

  // Pedimos todos los artículos al servidor SQL
  $sql = "SELECT * FROM blog";
  $resultado = $conexion->query($sql);

  // Recorremos los resultados y generamos la estructura HTML
  while ($fila = $resultado->fetch_assoc()) {
    echo '
    	<article>
      	<h3>'.$fila['titulo'].'</h3>
        <time>'.$fila['fecha'].'</time>
        <p><strong>Autor:</strong> '.$fila['autor'].'</p>
        <p>'.$fila['contenido'].'</p>
      </article>
    ';
  }

  $conexion->close();
?>
```

2. Aplicación de Estilo (`blog completo y bonito.php`)

Para que no "vomitemos" los datos sin formato, integramos el código PHP dentro de una estructura HTML profesional con estilos CSS.

```
<!doctype html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <style>
    /* Aplicamos un diseño centrado y limpio */
    body, html { font-family: 'Segoe UI', sans-serif; background-color: #f4f4f4; color: #333; }
    header, main, footer { width: 800px; margin: 20px auto; padding: 20px; background: white; border-radius: 8px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
    header, footer { text-align: center; background: PaleVioletRed; color: white; }
    h1 { margin: 0; }
    article { border-bottom: 1px solid #eee; padding: 15px 0; }
    article:last-child { border-bottom: none; }
    time { font-size: 0.85em; color: #666; font-style: italic; }
    p { text-align: justify; line-height: 1.6; }
  </style>
</head>
<body>
  <header>
    <h1>Ana Sánchez Suárez</h1>
    <h2>Blog de Tecnología</h2>
  </header>
  <main>
    <?php
      // Repetimos aquí la lógica de conexión y bucle while
      $conexion = new mysqli("localhost", "blogphp", "Blogphp123$", "blogphp");
      $resultado = $conexion->query("SELECT * FROM blog");

      while ($fila = $resultado->fetch_assoc()) {
        echo "
          <article>
            <h3>{$fila['titulo']}</h3>
            <time>{$fila['fecha']}</time>
            <p><strong>{$fila['autor']}</strong></p>
            <p>{$fila['contenido']}</p>
          </article>
        ";
      }
      $conexion->close();
    ?>
  </main>
  <footer>
    <p>&copy; 2025 Ana Sánchez Suárez. Todos los derechos reservados.</p>
  </footer>
</body>
</html>
```

---

**Gestión y revisión de errores**

Si intentamos ejecutar el archivo y recibimos un Error 500, significa que el servidor ha tenido un fallo crítico interno. En sistemas configurados para producción, el navegador no muestra detalles por seguridad.

Para saber qué ha pasado, debemos consultar el registro de errores del sistema:

- Ruta del log: /var/log/apache2/error.log.

- Procedimiento: Abrimos la terminal, vamos a la última línea del archivo y leemos la descripción del error para corregir nuestro código PHP.

---

Hemos comprobado que la potencia de PHP reside en su capacidad para mezclar lógica con diseño web de forma fluida. Al automatizar la lectura de la base de datos y envolverla en CSS, reducimos la carga de trabajo manual y aseguramos que la interfaz sea escalable: si añadimos 100 artículos más a MySQL, nuestra página los mostrará automáticamente con el mismo estilo.
