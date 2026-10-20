## Bar Bara - Bases de datos

Este proyecto consiste en el desarrollo de un sistema de gestión para un establecimiento de hostelería (Bar Bara), diseñado con una arquitectura que separa la lógica del servidor (Backend) de la interfaz de usuario (Frontend).

El objetivo es digitalizar el ciclo de servicio, desde que el cliente se registra hasta que solicita el pago en mesa.

---

Hemos diseñado una base de datos relacional compuesta por cuatro tablas principales que gestionan desde los usuarios hasta qué se ha pedido en la mesa.

Primero hay que crear la base de datos, usaremos un nombre descriptivo para que sea fácil de ubicar. Y nos metemos dentro de ella para empezar a crear las tablas.

```
CREATE DATABASE Bar_Bara;

USE Bar_Bara;
```

A continuación, vamos a explicar la estructura y el la funcionalidad de cada una de ellas:

1. Tabla: usuario

Aquí almacenaremos la información de los clientes registrados.

Será donde se gestionan las credenciales y datos personales para permitir el acceso al sistema.

Contiene el id como llave primaria, además de nombre_usuario, apellidos, correo y contraseña.

```
CREATE TABLE usuario (
  id INT NOT NULL,
  nombre_usuario VARCHAR(255),
  apellidos VARCHAR(255),
  correo VARCHAR(255),
  contrasena VARCHAR(255),
  PRIMARY KEY (id)
);
```

id INT NOT NULL: Es el identificador numérico. El atributo NOT NULL garantiza que ningún usuario se quede sin un número de identificación (no permite valores vacíos).

nombre_usuario, apellidos, correo y contrasena: Todos están definidos como VARCHAR(255). Esto significa que son cadenas de texto variables que pueden contener hasta 255 caracteres.

La línea PRIMARY KEY (id) es la más importante para la integridad de los datos, ya que segura que no existan dos usuarios con el mismo id.


2. Tabla: producto

Funciona como nuestra carta digital.

Así será mas fácil de llevar un registro actualizado de todos los alimentos y bebidas disponibles en el bar.

Además de su id, incluye el nombre_producto, precio, descripcion, categoria y la ruta de la imagen para la visualización en el frontend.

```
CREATE TABLE producto (
  id INT NOT NULL,
  nombre_producto VARCHAR(255),
  precio DECIMAL(4,2),
  descripcion VARCHAR(255),
  categoria VARCHAR(255),
  imagen VARCHAR(255),
  PRIMARY KEY (id)
);
```

id INT NOT NULL: Como con los usuarios, es el identificador único de cada producto.

nombre_producto VARCHAR(255): El nombre que aparecerá en la carta.

precio DECIMAL(4,2): Este es un punto clave. Usamos DECIMAL(4,2) en lugar de un número entero para permitir decimales.

descripcion VARCHAR(255): Un texto para poner los ingredientes.

categoria VARCHAR(255): Para organizar nuestra carta (ej: "Bebidas", "Tapas", "Cócteles").

imagen VARCHAR(255): Aquí ruta o URL de la imagen.


PRIMARY KEY (id): Garantiza que no tengamos productos duplicados con el mismo código.


3. Tabla: pedido

Esta tabla actúa como la cabecera o el resumen de cada compra realizada.

Aquí se registrará de forma general quién hizo el pedido, en qué mesa se encuentra y cuál es el estado de su cuenta.

```
CREATE TABLE pedido (
  id INT NOT NULL,
  usuario_id INT,
  numero_mesa INT,
  fecha VARCHAR(255),
  hora VARCHAR(255),
  productos VARCHAR(255),
  cantidad_producto INT,
  total DECIMAL(10,2),
  pedir_cuenta VARCHAR(255),
  PRIMARY KEY (id),
  CONSTRAINT fk_pedido_1 FOREIGN KEY (usuario_id) REFERENCES usuario(id)
);
```

Esta tabla es la que conecta a los clientes con sus consumiciones.

La línea CONSTRAINT fk_pedido_1 FOREIGN KEY (usuario_id) REFERENCES usuario(id) hace que cada pedido esté conectado con un usuario. No podemos crear un pedido para un usuario que no existe, así sabremos exactamente quien nos tiene que pagar y cuanto.

numero_mesa: Nos indica la ubicación del cliente en el bar.

fecha y hora: Aunque están como VARCHAR, registran el momento exacto de la transacción para el historial.

total DECIMAL(10,2): Aquí dejaremos números más altos que en los productos, permitiendo cifras de hasta 10 dígitos en total, ya que la cuenta final, se puede llegar a disparar bastante si son grupos grandes.

pedir_cuenta: Servirá para poder mandar la notificación a los trabajadores y cobren a los clientes.


4. Tabla: contenido_pedido

Es la tabla que conecta los pedidos con los productos específicos.

Se desglosará exactamente qué productos y en qué cantidad se han solicitado en un pedido concreto.
    
```
CREATE TABLE contenido_pedido (
  id INT NOT NULL,
  pedido_id INT,
  cantidad INT,
  subtotal DECIMAL(10,2),
  producto_id INT,
  PRIMARY KEY (id),
  CONSTRAINT fk_contenido_pedido_1 FOREIGN KEY (pedido_id) REFERENCES pedido(id),
  CONSTRAINT fk_contenido_pedido_2 FOREIGN KEY (producto_id) REFERENCES producto(id)
);
```

La función de esta tabla, es conectar las tres tablas anteriores, gracias a las claves foráneas.

- fk_contenido_pedido_1: Conecta con la tabla pedido. Nos dice a qué cuenta pertenece esta línea.

- fk_contenido_pedido_2: Conecta con la tabla producto. Nos dice qué producto se está consumiendo.

---

**Relaciones y Lógica del Sistema**

- Un usuario puede tener múltiples pedidos registrados a su nombre.

- Cada pedido puede contener varios productos, relación que gestionamos a través de la tabla intermedia contenido_pedido.

- Cuando un cliente pulsa en "Pedir Cuenta", nuestro sistema puede identificar exactamente qué productos consumió, en qué mesa está y quién es el usuario responsable.

---

**Crear usuario**

A continuación, para más adelante poder hacer las conexiones, vamos a crear un usuario, y darle permisos en esta base de datos.

```
CREATE USER 
'admin_bara'@'localhost' 
IDENTIFIED  BY 'BarBara_2025$';

GRANT USAGE ON *.* TO 'admin_bara'@'localhost';

ALTER USER 'admin_bara'@'localhost' 
REQUIRE NONE 
WITH MAX_QUERIES_PER_HOUR 0 
MAX_CONNECTIONS_PER_HOUR 0 
MAX_UPDATES_PER_HOUR 0 
MAX_USER_CONNECTIONS 0;

GRANT ALL PRIVILEGES ON Bar_Bara.* 
TO 'admin_bara'@'localhost';

FLUSH PRIVILEGES;
```

---

**Meter datos para comprobar el funcionamiento**

Ahora, para poder ver que la base de datos funciona correctamente, meteremos unos cuantos productos, que en este caso, por la cantidad que son, nos hemos ayudado un poco de la IA.

```
INSERT INTO producto (id, nombre_producto, precio, descripcion, categoria, imagen) VALUES
-- CERVEZAS
(1, 'Cerveza Lager', 2.50, 'Agua, malta de cebada, maíz, lúpulo', 'Cervezas', 'cerveza.jpg'),
(2, 'Cerveza IPA', 4.50, 'Agua, malta de cebada, lúpulo Citra, levadura Ale', 'Cervezas', 'cerveza.jpg'),
(3, 'Cerveza de Trigo', 4.00, 'Agua, malta de trigo, malta de cebada, lúpulo, levadura', 'Cervezas', 'cerveza.jpg'),
(4, 'Cerveza Negra', 4.20, 'Agua, cebada tostada, lúpulo, levadura', 'Cervezas', 'cerveza.jpg'),
(5, 'Cerveza Sin Alcohol', 3.00, 'Agua, malta de cebada, lúpulo, aromas naturales', 'Cervezas', 'cerveza.jpg'),
(6, 'Cerveza Radler', 2.80, 'Cerveza lager, zumo de limón natural, azúcar', 'Cervezas', 'cerveza.jpg'),
(7, 'Cerveza Artesana Roja', 5.00, 'Agua, maltas caramelizadas, lúpulo, levadura', 'Cervezas', 'cerveza.jpg'),
(8, 'Cerveza de Abadía', 6.00, 'Agua, malta de cebada, jarabe de glucosa, lúpulo', 'Cervezas', 'cerveza.jpg'),
(9, 'Cerveza Doble Malta', 4.50, 'Agua, exceso de malta de cebada, lúpulo', 'Cervezas', 'cerveza.jpg'),
(10, 'Cerveza Pilsen', 2.50, 'Agua, malta de cebada, lúpulo de Saaz', 'Cervezas', 'cerveza.jpg'),

-- VINOS Y VERMUT
(11, 'Vino Tinto Crianza', 3.50, 'Uva Tempranillo, sulfitos', 'Vinos', 'vinos.jpeg'),
(12, 'Vino Blanco Rueda', 3.00, 'Uva Verdejo, sulfitos', 'Vinos', 'vinos.jpeg'),
(13, 'Vino Rosado', 3.00, 'Uva Garnacha tinta, sulfitos', 'Vinos', 'vinos.jpeg'),
(14, 'Vino Albariño', 4.00, 'Uva Albariño 100%, sulfitos', 'Vinos', 'vinos.jpeg'),
(15, 'Copa de Cava', 4.50, 'Uva Macabeo, Parellada, Xarel·lo, sulfitos', 'Vinos', 'vinos.jpeg'),
(16, 'Vermut Rojo', 3.50, 'Vino blanco, ajenjo, canela, cáscara de naranja, hierbas', 'Vinos', 'vinos.jpeg'),
(17, 'Vermut Blanco', 3.50, 'Vino blanco, azúcar, extractos de hierbas aromáticas', 'Vinos', 'vinos.jpeg'),
(18, 'Tinto de Verano', 4.00, 'Vino tinto, agua carbonatada, ácido cítrico, azúcar', 'Vinos', 'vinos.jpeg'),
(19, 'Sangría Copa', 5.00, 'Vino tinto, zumo de naranja, limón, azúcar, canela', 'Vinos', 'vinos.jpeg'),
(20, 'Lambrusco', 3.50, 'Uva Lambrusco, gas carbónico natural, sulfitos', 'Vinos', 'vinos.jpeg'),

-- REFRESCOS
(21, 'Coca-Cola', 2.80, 'Agua carbonatada, azúcar, colorante E-150d, cafeína', 'Refrescos', 'refrescos.jpg'),
(22, 'Fanta Naranja', 2.80, 'Agua carbonatada, 8% zumo de naranja, azúcar', 'Refrescos', 'refrescos.jpg'),
(23, 'Nestea Limón', 2.90, 'Agua, azúcar, extracto de té negro, zumo de limón', 'Refrescos', 'refrescos.jpg'),
(24, 'Aquarius', 2.90, 'Agua, azúcar, sales minerales, aromas cítricos', 'Refrescos', 'refrescos.jpg'),
(25, 'Zumo Naranja Natural', 3.50, 'Naranjas de temporada recién exprimidas', 'Refrescos', 'refrescos.jpg'),
(26, 'Agua Mineral', 2.00, 'Agua mineral de manantial', 'Refrescos', 'refrescos.jpg'),
(27, 'Agua con Gas', 2.50, 'Agua mineral, anhídrido carbónico', 'Refrescos', 'refrescos.jpg'),
(28, 'Sprite', 2.80, 'Agua carbonatada, azúcar, aromas de lima y limón', 'Refrescos', 'refrescos.jpg'),
(29, 'Tónica Premium', 3.00, 'Agua, azúcar, anhídrido carbónico, quinina', 'Refrescos', 'refrescos.jpg'),
(30, 'Ginger Ale', 3.00, 'Agua carbonatada, azúcar, extracto de jengibre', 'Refrescos', 'refrescos.jpg'),

-- TAPAS Y ENTRANTES
(31, 'Patatas Bravas', 6.50, 'Patatas, aceite de oliva, tomate, guindilla, pimentón', 'Tapas', 'tapas.jpg'),
(32, 'Croquetas de Jamón', 8.00, 'Leche, harina, mantequilla, jamón ibérico, pan rallado', 'Tapas', 'tapas.jpg'),
(33, 'Calamares Romana', 9.50, 'Calamares, harina de trigo, huevo, levadura, sal', 'Tapas', 'tapas.jpg'),
(34, 'Aceitunas Aliñadas', 2.50, 'Aceitunas gordal, ajo, tomillo, romero, aceite', 'Tapas', 'tapas.jpg'),
(35, 'Tabla de Quesos', 12.00, 'Leche de oveja, cabra y vaca, cuajo, sal', 'Tapas', 'tapas.jpg'),
(36, 'Jamón Ibérico', 18.00, 'Jamón de cerdo ibérico, sal marina', 'Tapas', 'tapas.jpg'),
(37, 'Pimientos Padrón', 7.00, 'Pimientos de Padrón, aceite de oliva, sal gorda', 'Tapas', 'tapas.jpg'),
(38, 'Nachos Completos', 9.00, 'Maíz, queso fundido, jalapeños, nata agria, aguacate', 'Tapas', 'tapas.jpg'),
(39, 'Ensaladilla Rusa', 7.50, 'Patata, atún, huevo, zanahoria, mayonesa, guisantes', 'Tapas', 'tapas.jpg'),
(40, 'Alitas de Pollo', 8.50, 'Pollo, miel, mostaza, salsa de soja, especias', 'Tapas', 'tapas.jpg'),
(41, 'Gambas al Ajillo', 12.50, 'Gambas, ajo, aceite de oliva, guindilla, perejil', 'Tapas', 'tapas.jpg'),
(42, 'Tortilla de Patatas', 5.00, 'Patatas, huevos, cebolla, aceite de oliva, sal', 'Tapas', 'tapas.jpg'),
(43, 'Boquerones Vinagre', 8.00, 'Boquerones, vinagre de vino, ajo, perejil, aceite', 'Tapas', 'tapas.jpg'),
(44, 'Pan con Tomate', 3.00, 'Pan de hogaza, tomate maduro, aceite virgen, sal', 'Tapas', 'tapas.jpg'),
(45, 'Quesadilla Queso', 7.50, 'Tortilla de trigo, queso cheddar, mozzarella', 'Tapas', 'tapas.jpg'),

-- HAMBURGUESAS Y BOCADILLOS
(46, 'Burger Clásica', 10.50, 'Pan brioche, ternera, lechuga, tomate, cebolla', 'Comida', 'comida.jpg'),
(47, 'Burger Queso', 11.50, 'Ternera, queso cheddar, bacon, pepinillo, kétchup', 'Comida', 'comida.jpg'),
(48, 'Sandwich Mixto', 4.50, 'Pan de molde, jamón york, queso edam, mantequilla', 'Comida', 'comida.jpg'),
(49, 'Sandwich Club', 9.00, 'Pollo, bacon, huevo, lechuga, tomate, mayonesa', 'Comida', 'comida.jpg'),
(50, 'Bocadillo de Lomo', 6.50, 'Pan de barra, lomo de cerdo, queso, pimientos', 'Comida', 'comida.jpg'),
(51, 'Bocadillo Calamares', 7.50, 'Pan de barra, calamares fritos, mayonesa de limón', 'Comida', 'comida.jpg'),
(52, 'Hot Dog', 5.50, 'Pan de Frankfurt, salchicha de cerdo, cebolla frita', 'Comida', 'comida.jpg'),
(53, 'Burger Vegana', 12.00, 'Proteína de guisante, quinoa, espinacas, tofu', 'Comida', 'comida.jpg'),
(54, 'Pepito de Ternera', 8.50, 'Pan, solomillo de ternera, ajo, aceite de oliva', 'Comida', 'comida.jpg'),
(55, 'Bocadillo de Atún', 6.00, 'Pan, atún en aceite, pimientos rojos, aceitunas', 'Comida', 'comida.jpg'),

-- ENSALADAS Y PLATOS
(56, 'Ensalada César', 9.50, 'Lechuga romana, pollo, picatostes, parmesano, salsa', 'Platos', 'platos.jpg'),
(57, 'Pasta Boloñesa', 10.00, 'Espaguetis, carne picada, tomate, cebolla, orégano', 'Platos', 'platos.jpg'),
(58, 'Pizza Margarita', 9.50, 'Harina, tomate, mozzarella, albahaca fresca', 'Platos', 'platos.jpg'),
(59, 'Pechuga Plancha', 11.00, 'Pollo, sal, pimienta, guarnición de ensalada', 'Platos', 'platos.jpg'),
(60, 'Salmón Grill', 15.00, 'Salmón fresco, eneldo, limón, espárragos verdes', 'Platos', 'platos.jpg'),
(61, 'Entrecot Ternera', 19.00, 'Carne de vacuno, sal maldon, patatas fritas', 'Platos', 'platos.jpg'),
(62, 'Lasaña Carne', 11.50, 'Pasta, ternera, bechamel, queso rallado, tomate', 'Platos', 'platos.jpg'),
(63, 'Ensalada Burrata', 12.00, 'Queso burrata, tomate cherry, pesto, canónigos', 'Platos', 'platos.jpg'),
(64, 'Pizza Pepperoni', 11.00, 'Masa fina, tomate, mozzarella, salchichón picante', 'Platos', 'platos.jpg'),
(65, 'Risotto Setas', 13.00, 'Arroz carnaroli, setas variadas, parmesano, nata', 'Platos', 'platos.jpg'),

-- CÓCTELES (CATEGORÍA TOP)
(66, 'Mojito', 8.50, 'Ron blanco, azúcar moreno, lima, hierbabuena, soda', 'Cócteles', 'coctel.webp'),
(67, 'Caipirinha', 8.00, 'Cachaça, lima troceada, azúcar blanca, hielo', 'Cócteles', 'coctel.webp'),
(68, 'Piña Colada', 9.00, 'Ron, crema de coco, zumo de piña natural', 'Cócteles', 'coctel.webp'),
(69, 'Margarita', 8.50, 'Tequila, triple seco, zumo de lima, sal', 'Cócteles', 'coctel.webp'),
(70, 'Gin Tonic', 10.00, 'Ginebra, tónica, bayas de enebro, piel de limón', 'Cócteles', 'coctel.webp'),
(71, 'Negroni', 9.50, 'Ginebra, vermut rojo, Campari, naranja', 'Cócteles', 'coctel.webp'),
(72, 'Cosmopolitan', 9.00, 'Vodka, Cointreau, zumo de arándanos, lima', 'Cócteles', 'coctel.webp'),
(73, 'Daiquiri Fresa', 8.50, 'Ron blanco, fresas naturales, azúcar, limón', 'Cócteles', 'coctel.webp'),
(74, 'Sex on the Beach', 9.00, 'Vodka, licor melocotón, naranja, arándanos', 'Cócteles', 'coctel.webp'),
(75, 'Aperol Spritz', 7.50, 'Aperol, cava, soda, rodaja de naranja', 'Cócteles', 'coctel.webp'),
(76, 'Bloody Mary', 9.00, 'Vodka, zumo tomate, tabasco, apio, pimienta', 'Cócteles', 'coctel.webp'),
(77, 'Moscow Mule', 9.50, 'Vodka, cerveza de jengibre, lima, menta', 'Cócteles', 'coctel.webp'),
(78, 'Manhattan', 10.00, 'Whisky de centeno, vermut dulce, angostura', 'Cócteles', 'coctel.webp'),
(79, 'Tequila Sunrise', 8.50, 'Tequila, zumo de naranja, granadina', 'Cócteles', 'coctel.webp'),
(80, 'Espresso Martini', 9.50, 'Vodka, licor de café, café espresso, azúcar', 'Cócteles', 'coctel.webp'),

-- CAFÉ Y POSTRES
(81, 'Café Espresso', 1.50, 'Granos de café arábica molidos', 'Cafetería', 'cafe.jpg'),
(82, 'Capuccino', 2.50, 'Café, leche vaporizada, espuma, cacao', 'Cafetería', 'cafe.jpg'),
(83, 'Café con Leche', 1.80, 'Café espresso, leche entera caliente', 'Cafetería', 'cafe.jpg'),
(84, 'Té Verde', 2.00, 'Hojas de té verde, agua caliente', 'Cafetería', 'cafe.jpg'),
(85, 'Chocolate Caliente', 3.00, 'Cacao puro, leche, azúcar, canela', 'Cafetería', 'cafe.jpg'),
(86, 'Tarta de Queso', 5.50, 'Queso crema, galleta, mantequilla, mermelada', 'Postres', 'postres.jpg'),
(87, 'Brownie', 5.00, 'Chocolate negro, nueces, harina, huevo, azúcar', 'Postres', 'postres.jpg'),
(88, 'Tiramisú', 6.00, 'Bizcocho, café, mascarpone, huevo, cacao', 'Postres', 'postres.jpg'),
(89, 'Helado Vainilla', 4.00, 'Leche, nata, vainilla natural, azúcar', 'Postres', 'postres.jpg'),
(90, 'Fruta Temporada', 3.50, 'Fruta variada según estación', 'Postres', 'postres.jpg'),

-- COMBINADOS Y CHUPITOS
(91, 'Cuba Libre', 8.00, 'Ron añejo, Coca-Cola, lima', 'Copas', 'copas.jpeg'),
(92, 'Vodka Lemon', 8.00, 'Vodka, refresco de limón, hielo', 'Copas', 'copas.jpeg'),
(93, 'Whisky Cola', 8.50, 'Whisky escocés, Coca-Cola, hielo', 'Copas', 'copas.jpeg'),
(94, 'Chupito Tequila', 3.00, 'Tequila blanco, sal, limón', 'Copas', 'copas.jpeg'),
(95, 'Chupito Hierbas', 2.50, 'Licor de hierbas maceradas', 'Copas', 'copas.jpeg'),
(96, 'Jaggermeister', 3.50, '56 hierbas, raíces y frutas', 'Copas', 'copas.jpeg'),
(97, 'Gin con Limonada', 8.00, 'Ginebra, zumo de limón, azúcar, gas', 'Copas', 'copas.jpeg'),
(98, 'Ron con Naranja', 8.00, 'Ron blanco, zumo de naranja, hielo', 'Copas', 'copas.jpeg'),
(99, 'Chupito de Crema', 2.50, 'Licor de crema de orujo, leche', 'Copas', 'copas.jpeg'),
(100, 'Carajillo', 2.80, 'Café espresso, brandy, granos de café', 'Copas', 'copas.jpeg');
```

**Visualización de la base de datos en terminal**

```
mysql> SHOW TABLES;
+--------------------+
| Tables_in_Bar_Bara |
+--------------------+
| contenido_pedido   |
| pedido             |
| producto           |
| usuario            |
+--------------------+
4 rows in set (0,00 sec)
```

```
mysql> SELECT * FROM contenido_pedido;
+----+-----------+----------+----------+-------------+
| id | pedido_id | cantidad | subtotal | producto_id |
+----+-----------+----------+----------+-------------+
|  1 |         1 |        3 |     7.50 |          82 |
|  2 |         1 |        2 |    13.00 |          50 |
|  3 |         1 |        2 |    17.00 |          40 |
|  4 |         2 |        1 |     2.50 |          82 |
|  5 |         3 |        1 |     2.50 |          82 |
|  6 |         4 |        1 |     2.00 |          84 |
|  7 |         4 |        1 |     4.00 |           3 |
|  8 |         4 |        1 |     3.00 |           5 |
|  9 |         5 |        1 |     2.50 |          82 |
| 10 |         6 |        1 |     2.50 |          82 |
| 11 |         7 |        2 |    16.00 |          43 |
| 12 |         8 |        1 |     2.50 |          95 |
+----+-----------+----------+----------+-------------+
12 rows in set (0,00 sec)
```

```
mysql> SELECT * FROM pedido;
+----+------------+-------------+------------+----------+-----------+-------------------+-------+--------------+
| id | usuario_id | numero_mesa | fecha      | hora     | productos | cantidad_producto | total | pedir_cuenta |
+----+------------+-------------+------------+----------+-----------+-------------------+-------+--------------+
|  1 |          1 |          33 | 2026-01-12 | 08:37:39 | NULL      |              NULL | 37.50 | PAGADO       |
|  2 |          1 |           5 | 2026-01-12 | 08:42:38 | NULL      |              NULL |  2.50 | PAGADO       |
|  3 |          1 |           4 | 2026-01-12 | 09:09:49 | NULL      |              NULL |  2.50 | PAGADO       |
|  4 |          1 |           3 | 2026-01-13 | 09:25:29 | NULL      |              NULL |  9.00 | PAGADO       |
|  5 |          1 |           1 | 2026-01-13 | 09:37:27 | NULL      |              NULL |  2.50 | PAGADO       |
|  6 |          1 |           1 | 2026-01-13 | 11:03:52 | NULL      |              NULL |  2.50 | PAGADO       |
|  7 |          1 |           4 | 2026-01-13 | 11:22:32 | NULL      |              NULL | 16.00 | PAGADO       |
|  8 |          1 |           1 | 2026-01-13 | 21:41:03 | NULL      |              NULL |  2.50 | PAGADO       |
+----+------------+-------------+------------+----------+-----------+-------------------+-------+--------------+
8 rows in set (0,00 sec)
```

```
mysql> SELECT * FROM usuario;
+----+----------------+------------------+--------------------+--------------------------------------------------------------+
| id | nombre_usuario | apellidos        | correo             | contrasena                                                   |
+----+----------------+------------------+--------------------+--------------------------------------------------------------+
|  1 | Ana            | Sánchez Suárez   | ssanitax@gmail.com | $2y$10$uDBCmM7uW/9efiaBWpfsLuzHVO0c8jewO4AoXo1bEGPbVnw9x5jje |
+----+----------------+------------------+--------------------+--------------------------------------------------------------+
1 row in set (0,00 sec)
```

---

Hemos logrado crear una base de datos organizada y segura para el Bar Bara. Gracias a la unión de las cuatro tablas, el sistema es capaz de recordar quién es cada cliente, qué productos ofrece la carta y qué se ha servido en cada mesa sin errores. Al tenerlo todo conectado, el bar puede funcionar de forma mucho más rápida, desde que el cliente entra y se registra hasta que pide la cuenta, todo queda guardado automáticamente. Es una base sólida, fácil de usar y preparada para que el bar crezca y gestione sus ventas de forma moderna y profesional.
