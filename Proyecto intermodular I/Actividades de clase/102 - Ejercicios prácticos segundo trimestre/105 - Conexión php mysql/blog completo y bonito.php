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
