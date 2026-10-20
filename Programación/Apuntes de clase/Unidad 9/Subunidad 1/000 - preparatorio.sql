sudo mysql -u root -p

CREATE DATABASE empresa2026;
USE empresa2026;

CREATE TABLE clientes(
	nombre VARCHAR(255),
	apellidos VARCHAR(255),
	email VARCHAR(255)
);

INSERT INTO clientes VALUES(
	"Ana",
	"Sánchez",
	"ssanitax@gmail.com"
);

SELECT * FROM clientes;
