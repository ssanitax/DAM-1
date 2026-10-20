Hemos desarrollado esta práctica para entender cómo se monta la infraestructura de datos de un periódico digital. Lo más importante que hemos aprendido es que las bases de datos no son tablas sueltas, sino que tienen que estar conectadas para que todo tenga sentido. Por ejemplo, no sirve de nada tener una noticia si nosotros no sabemos quién la ha escrito.

Para solucionar esto, hemos usado SQL para crear una relación de "autoría", vinculando a los redactores con sus artículos mediante claves foráneas.

---

**Creación de la Base de Datos y Tablas**

Hemos diseñado dos tablas principales. La tabla `autores` guarda los datos de los periodistas, y la tabla `noticias` guarda los artículos. Hemos añadido `ON DELETE SET NULL` para que, si nosotros borramos a un autor, sus noticias no desaparezcan, sino que simplemente se queden sin autor asignado.

```
-- Creamos el contenedor principal
CREATE DATABASE periodico
  DEFAULT CHARACTER SET utf8mb4
  DEFAULT COLLATE utf8mb4_unicode_ci;

USE periodico;

-- Tabla para los redactores
CREATE TABLE autores (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE,
    bio TEXT,
    fecha_registro DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Tabla para los artículos
CREATE TABLE noticias (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(200) NOT NULL,
    contenido TEXT NOT NULL,
    fecha_publicacion DATETIME DEFAULT CURRENT_TIMESTAMP,
    autor_id INT NULL,
    CONSTRAINT fk_noticias_autores
        FOREIGN KEY (autor_id)
        REFERENCES autores(id)
        ON UPDATE CASCADE
        ON DELETE SET NULL
);
```

**Gestión de Usuarios y Permisos**

Queremos ser buenos programadores, no usamos el usuario "root" en la web. Hemos creado un usuario específico llamado `periodico` que solo puede tocar su propia base de datos.

```
CREATE USER 'periodico'@'localhost' IDENTIFIED BY 'Periodico123$';
GRANT ALL PRIVILEGES ON periodico.* TO 'periodico'@'localhost';
FLUSH PRIVILEGES;
```

**Inserción de Contenido de Prueba**

Hemos metido unos cuantos datos para comprobar que los `JOIN` y las consultas funcionan bien antes de pasar a la fase de PHP.

```
INSERT INTO autores (nombre, email, bio) VALUES
('María López', 'maria.lopez@example.com', 'Periodista de política.'),
('Carlos Fernández', 'carlos.fernandez@example.com', 'Redactor de tecnología.');

INSERT INTO noticias (titulo, contenido, autor_id) VALUES
('Medidas económicas', 'Resumen de las nuevas reformas...', 1),
('Dron autónomo', 'Una startup valenciana presenta su prototipo...', 2);
```

---

Hemos comprobado que diseñar bien las tablas al principio nos ahorra muchos problemas luego en el código. Al tener las noticias y los autores relacionados, nosotros podemos sacar listados automáticos muy fácilmente. Además, nosotros ya tenemos la base lista para crear un Panel de Control donde los autores puedan entrar con su usuario y subir noticias ellos mismos.
