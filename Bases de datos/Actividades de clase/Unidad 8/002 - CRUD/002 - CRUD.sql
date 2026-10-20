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
