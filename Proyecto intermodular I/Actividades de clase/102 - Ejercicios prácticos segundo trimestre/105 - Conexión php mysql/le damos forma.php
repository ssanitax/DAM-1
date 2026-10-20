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
