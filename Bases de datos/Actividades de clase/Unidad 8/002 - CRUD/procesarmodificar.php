<?php
  // Verificamos primero si el ID ha llegado por el método POST
  if (!isset($_POST['id']) || empty($_POST['id'])) {
      die("Error: No he recibido un ID. Por favor, usa el formulario.");
  }

  $id = $_POST['id'];
  $conexion = new mysqli("localhost", "empleados", "Empleados123$", "empleados");
  
  // Lanzamos la consulta filtrando por el ID recibido
  $sql = "SELECT * FROM empleados WHERE id = $id;";
  $resultado = $conexion->query($sql);

  if ($resultado->num_rows > 0) {
      while ($fila = $resultado->fetch_assoc()) {
        // Pintamos el formulario de edición con los datos actuales
        echo '
          <form action="procesaractualizacion.php" method="POST">
            <input type="hidden" name="id" value="'.$id.'">
            Nombre: <input type="text" name="nombre" value="'.$fila['nombre'].'"><br>
            Puesto: <input type="text" name="puesto" value="'.$fila['puesto'].'"><br>
            Salario: <input type="text" name="salario" value="'.$fila['salario'].'"><br>
            <input type="submit" value="Actualizar Datos">
          </form>';
      }
  } else {
      echo "No he encontrado ningún empleado con el ID: " . $id;
  }
  
  $conexion->close();
?>
