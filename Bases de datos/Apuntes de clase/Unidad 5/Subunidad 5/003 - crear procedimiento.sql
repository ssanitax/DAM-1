DELIMITER //

CREATE PROCEDURE productos_baratos(IN precio_max DECIMAL(10,2))
BEGIN
    SELECT * 
    FROM productos 
    WHERE precio < precio_max;
END //

DELIMITER;

CALL`prductos_baratos`(40);