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
