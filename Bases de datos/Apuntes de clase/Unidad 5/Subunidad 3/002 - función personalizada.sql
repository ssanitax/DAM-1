DELIMITER //

CREATE FUNCTION nombre_completo(
    p_nombre VARCHAR(255),
    p_apellidos VARCHAR(255)
)
RETURNS VARCHAR(500)
DETERMINISTIC
BEGIN
    RETURN CONCAT(p_nombre,' ',p_apellidos);
END //

DELIMITER ;

INSERT INTO clientes(
    nombre,
    apellidos,
    email,
    direccion
)
VALUES(
    nombre_completo('Ana','Sánchez Suárez'),
    'Sánchez Suárez',
    'info@anasanchez.com',
    'La calle de Ana'
);