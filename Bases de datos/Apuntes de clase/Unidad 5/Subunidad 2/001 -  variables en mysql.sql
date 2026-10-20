SET @nombre = 'Ana';
SET @apellidos = 'Sánchez Suárez';
SET @email = 'info@anasanchez.com';
SET @direccion = 'La calle de Ana';

INSERT INTO clientes(
    nombre,
    apellidos,
    email,
    direccion
)
VALUES(
    @nombre,
    @apellidos,
    @email,
    @direccion
);