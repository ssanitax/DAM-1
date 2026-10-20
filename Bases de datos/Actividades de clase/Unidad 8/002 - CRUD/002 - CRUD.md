Utilizamos un sistema CRUD para administrar el ciclo de vida de la información en una base de datos relacional. En este proyecto, la arquitectura se divide en tres capas:

- SQL: Donde nosotros definimos la estructura de las tablas y los permisos de seguridad.

- PHP: El motor que procesa la lógica, captura los datos de los formularios y ejecuta las sentencias SQL.

- HTML: La interfaz que permite al usuario interactuar con el sistema de forma intuitiva.

---

1. Empezamos creando la base de datos.

```
-- 1. Creamos la base de datos
CREATE DATABASE IF NOT EXISTS empleados DEFAULT CHARACTER SET utf8mb4;
USE empleados;

-- 2. Definimos la tabla de personal
CREATE TABLE empleados (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    puesto VARCHAR(100) NOT NULL,
    salario DECIMAL(10,2) NOT NULL,
    fecha_contratacion DATE NOT NULL,
    departamento VARCHAR(100)
);

-- 3. Creamos el usuario con permisos específicos
CREATE USER 'empleados'@'localhost' IDENTIFIED BY 'Empleados123$';
GRANT ALL PRIVILEGES ON empleados.* TO 'empleados'@'localhost';
FLUSH PRIVILEGES;
```

2. Ahora crearemos un formulario simple que recoja el identificador del empleado. Para poder hacer una actualización.

```
<form action="procesarmodificar.php" method="POST">
  <p>Introduce el ID del empleado que quieres modificar:</p>
  <input type="number" name="id" placeholder="ID del empleado" required>
  <input type="submit" value="Cargar Datos">
</form>
```

3. Por último haremos un segundo formulario con los datos actuales ya rellenos, para poder hacer la edición de forma más cómoda.

```
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
```

---

Un sistema CRUD bien estructurado garantiza la integridad de la información y facilita la administración empresarial. Al separar el proceso en varios archivos (uno para pedir el ID, otro para mostrar los datos y un tercero para ejecutar el UPDATE), nosotros logramos un código modular y fácil de mantener.
