DELIMITER //

CREATE PROCEDURE insertar()
BEGIN

    IF (SELECT COUNT(*) 
        FROM clientes 
        WHERE email='info@anasanchez.com') = 0
    THEN
        INSERT INTO clientes
        VALUES(
            NULL,
            'Ana',
            'Sánchez Suárez',
            'info@anasanchez.com',
            'La calle de Ana'
        );
    END IF;

END //

DELIMITER ;