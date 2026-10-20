-- Creamos la estructura base
CREATE TABLE cliente (
  id INT PRIMARY KEY,
  nombre VARCHAR(255),
  apellidos VARCHAR(255)
);

CREATE TABLE telefono (
  id INT PRIMARY KEY,
  id_cliente INT,
  tipo VARCHAR(255),
  numero VARCHAR(255),
  CONSTRAINT fk_telefono_1 FOREIGN KEY (id_cliente) REFERENCES cliente(id)
);

-- Insertamos datos para verificar la relación
INSERT INTO cliente VALUES (1, 'Ana', 'Sánchez Suárez');
INSERT INTO telefono VALUES (1, 1, 'Móvil', '+34 722 28 96 95');
INSERT INTO telefono VALUES (2, 1, 'Trabajo', '963445566');


-- Superclase con datos comunes
CREATE TABLE persona (
  id INT PRIMARY KEY,
  nombre VARCHAR(255),
  apellidos VARCHAR(255)
);

-- Subclases especializadas
CREATE TABLE alumno (
  id INT PRIMARY KEY,
  nie VARCHAR(255),
  CONSTRAINT fk_alumno_persona FOREIGN KEY (id) REFERENCES persona(id)
);

CREATE TABLE profesor (
    id INT PRIMARY KEY,
    asignaturas VARCHAR(255),
    CONSTRAINT fk_profesor_persona FOREIGN KEY (id) REFERENCES persona(id)
);

-- Probamos la integridad de la jerarquía
INSERT INTO persona VALUES (1, 'Jose Vicente', 'Carratalá');
INSERT INTO profesor VALUES (1, 'Bases de Datos, Programación');

INSERT INTO persona VALUES (2, 'Ana', 'Sánchez');
INSERT INTO alumno VALUES (2, 'NIE123456');
