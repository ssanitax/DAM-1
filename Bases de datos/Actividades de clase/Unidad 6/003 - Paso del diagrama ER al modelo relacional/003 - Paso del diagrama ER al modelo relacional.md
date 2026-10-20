1. Relación 1 a n

Representamos esta relación donde un cliente puede poseer varios teléfonos, pero cada teléfono pertenece exclusivamente a un cliente. Para implementar esto en el modelo relacional, debemos añadir una clave foránea en la tabla hija que apunte a la madre.

**Representación en tablas**

```
| Cliente |
|---------|---------|----------|
| id (pk) | nombre  | apellidos|

| Teléfono |
|----------|------------|----------|--------|
| id (pk)  | id_cliente | tipo     | numero |
```

**Implementación SQL en Datos de Prueba**

```
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
```

2. Generalización/Especialización

Aquí aplicaremos el concepto herencia. La tabla `persona` actúa como superclase, mientras que `alumno` y `profesor` son subclases que se especializan compartiendo el mismo identificador que la tabla madre.

**Representación en tablas**

```
| Persona |
|---------|---------|----------|
| id (pk) | nombre  | apellidos|

| Alumno    |
|-----------|------|
| id (pk/fk)| nie  |

| Profesor  |
|-----------|-------------|
| id (pk/fk)| asignatura  |
```

**Implementación SQL y Datos de Prueba**

```
-- Superclase con datos comunes
CREATE TABLE persona (
  id INT PRIMARY KEY,
  nombre VARCHAR(255),
  apellidos VARCHAR(255)
);

-- Subclases especializadas
CREATE TABLE alumno (
  id INT PRIMARY KEY,
  nia VARCHAR(255),
  CONSTRAINT fk_alumno_persona FOREIGN KEY (id) REFERENCES persona(id)
);

CREATE TABLE profesor (
    id INT PRIMARY KEY,
    asignaturas VARCHAR(255),
    CONSTRAINT fk_profesor_persona FOREIGN KEY (id) REFERENCES persona(id)
);

-- Nosotros probamos la integridad de la jerarquía
INSERT INTO persona VALUES (1, 'Jose Vicente', 'Carratalá');
INSERT INTO profesor VALUES (1, 'Bases de Datos, Programación');

INSERT INTO persona VALUES (2, 'Ana', 'Sánchez');
INSERT INTO alumno VALUES (2, 'NIA123456');
```

---

En este ejercicio hemos visto que al traducir un diagrama ER al modelo relacional, se requieren decisiones de diseño precisas, mientras que las relaciones 1 a N se resuelve con columnas de enlace, las especializaciones requieren una coincidencia de claves primarias entre tablas jerárquicas. Este procedimiento garantiza que la base de datos no sea un simple almacén, sino una representación lógica y segura de la realidad del negocio.
