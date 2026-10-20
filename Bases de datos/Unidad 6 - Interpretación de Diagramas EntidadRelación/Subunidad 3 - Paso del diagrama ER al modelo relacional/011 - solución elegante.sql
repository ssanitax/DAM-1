CREATE TABLE persona (
  id INT PRIMARY KEY,
  nombre VARCHAR(255),
  apellidos VARCHAR(255)
);

CREATE TABLE alumno (
  id INT PRIMARY KEY,
  nia VARCHAR(255),
  CONSTRAINT fk_alumno_1 FOREIGN KEY (id) REFERENCES persona(id)
);

CREATE TABLE profesor (
    id INT PRIMARY KEY,
    asignaturas VARCHAR(255),
    CONSTRAINT fk_profesor_1 FOREIGN KEY (id) REFERENCES persona(id)
);
