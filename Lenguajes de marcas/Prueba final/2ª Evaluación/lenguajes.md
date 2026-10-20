# Examen – Vistas del proyecto **Bar Bara**

---

## 1. Diagrama de flujo y navegación entre pantallas

### Flujo general del usuario

1. **Inicio (`index.php`)**

   * Pantalla de bienvenida.
   * Desde aquí el usuario puede ir al catálogo, al carrito o a contacto.

2. **Login (`login.php`) / Registro (`registro.php`)**

   * El usuario se identifica para que el sistema pueda asociar pedidos a una mesa/cliente.

3. **Catálogo (`catalogo.php`)**

   * Se muestran todos los productos organizados por categorías.
   * El usuario selecciona productos y cantidades.

4. **Carrito (`carrito.php`)**

   * Se revisa el pedido.
   * Se pueden modificar cantidades o eliminar productos.
   * Se introduce el número de mesa y se confirma el pedido.

5. **Finalización (`finalizacion.php`)**

   * Mensaje de confirmación.
   * El pedido pasa a cocina.

6. **Historial (`historial.php`)**

   * Resumen del pedido activo.
   * El usuario puede pedir la cuenta.

7. **Contacto (`contacto.php`)**

   * Formulario informativo independiente del pedido.

---

## 2. Explicación detallada de las pantallas (VISTAS)

---

## 2.1 Inicio – `front/index.php`

### HTML

* `main`: contenedor principal de la página.
* `img`: muestra el logo del bar.
* `a`: botones de navegación a otras vistas.

Sirve como punto de entrada a la aplicación.

### CSS

* Flexbox para centrar el contenido.
* Botones grandes tipo "hero" para mejorar la experiencia de usuario.

### Código completo

```php
<?php 
require_once '../back/inc/conexion_bd.php';
include 'inc/cabecera.php'; 
?>

<link rel="stylesheet" href="css/estilo.css">

<main class="hero-section">
    <img src="img/logo_home.png" alt="Bar Bara Logo" class="hero-logo-img">
    <p class="hero-subtitle">Comida con Carácter & Tragos Rebeldes</p>

    <div class="action-grid">
        <a href="catalogo.php" class="btn-hero btn-carta">🍔 Ver La Carta</a>
        <a href="carrito.php" class="btn-hero btn-carrito-hero">🛒 Mi Pedido</a>
        <a href="contacto.php" class="btn-hero btn-contacto">📍 Contacto</a>
    </div>
</main>

<?php include 'inc/piedepagina.php'; ?>
```

---

## 2.2 Catálogo – `front/catalogo.php`

### HTML

* `div`: contenedores de categorías y productos.
* `h2`: título de cada categoría.
* `img`: imagen del producto.
* `form`: envío de productos al carrito.

### CSS

* **Grid** para mostrar productos en columnas.
* **Flexbox** para controles de cantidad.
* `position: sticky` para el menú de categorías.

### JavaScript (opcional)

* Uso de `stepUp()` y `stepDown()` en botones `+` y `-`.

### Código completo (vista)

```php
<?php 
session_start();
require_once '../back/inc/conexion_bd.php';
include 'inc/cabecera.php';
$res_cat = $pdo->query("SELECT DISTINCT categoria FROM producto");
$categorias = $res_cat->fetchAll(PDO::FETCH_COLUMN);
$stmt = $pdo->query("SELECT * FROM producto ORDER BY categoria");
?>

<div class="categorias-nav">
<?php foreach ($categorias as $c): ?>
<a href="#<?= $c ?>" class="cat-link"><?= $c ?></a>
<?php endforeach; ?>
</div>

<div class="catalogo-grid">
<?php $cat=""; while($p=$stmt->fetch()): ?>
<?php if($cat!=$p['categoria']): $cat=$p['categoria']; ?>
<h2 id="<?= $cat ?>" class="categoria-titulo"><?= $cat ?></h2>
<?php endif; ?>

<div class="producto-card">
<img src="img/<?= $p['imagen'] ?>" class="producto-img">
<h3><?= $p['nombre_producto'] ?></h3>
<p><?= number_format($p['precio'],2) ?>€</p>
<form action="carrito.php" method="POST">
<input type="hidden" name="id" value="<?= $p['id'] ?>">
<input type="number" name="cantidad" value="1" min="1" readonly>
<button type="submit" name="add">Añadir</button>
</form>
</div>
<?php endwhile; ?>
</div>

<?php include 'inc/piedepagina.php'; ?>
```

---

## 2.3 Carrito – `front/carrito.php`

### HTML

* `table`: lista de productos.
* `form`: actualizar cantidades y eliminar productos.
* `input type="number"`: control de unidades.

### CSS

* Flexbox para el total y controles.
* Media queries para versión móvil.

### JavaScript

* Modificación visual de cantidades.

### Código (vista resumida)

```php
<h2>🛒 Nuestra Comanda</h2>
<table>
<?php foreach($_SESSION['carrito'] as $p): ?>
<tr>
<td><?= $p['nombre'] ?></td>
<td><?= $p['cantidad'] ?></td>
<td><?= $p['precio'] * $p['cantidad'] ?>€</td>
</tr>
<?php endforeach; ?>
</table>
```

---

## 2.4 Finalización – `front/finalizacion.php`

### HTML

* Mensaje de confirmación.
* Enlaces a seguir pidiendo o ver historial.

### CSS

* Flexbox centrado.

### Código

```php
<h1>¡Marchando!</h1>
<p>Tu pedido se está preparando.</p>
<a href="catalogo.php">Pedir otra ronda</a>
<a href="historial.php">Ver resumen</a>
```

---

## 2.5 Historial – `front/historial.php`

### HTML

* `table`: resumen del pedido.
* `form`: botón para pedir la cuenta.

### CSS

* Diseño tipo ticket.

### Código

```php
<h2>Resumen de la mesa</h2>
<table>
<tr><th>Producto</th><th>Cant.</th><th>Subtotal</th></tr>
<?php foreach($items as $i): ?>
<tr>
<td><?= $i['nombre_producto'] ?></td>
<td><?= $i['cantidad'] ?></td>
<td><?= $i['subtotal'] ?>€</td>
</tr>
<?php endforeach; ?>
</table>
<form method="POST">
<button name="pedir_cuenta_total">Pedir la cuenta</button>
</form>
```

---

## 2.6 Contacto – `front/contacto.php`

### HTML

* `form`, `input`, `textarea`, `label`.

### CSS

* Grid de dos columnas.
* Responsive.

### Código

```php
<form method="POST">
<input type="text" name="nombre" required>
<input type="email" name="email" required>
<textarea name="mensaje" required></textarea>
<button>Enviar</button>
</form>
```

---

## 3. Conclusión

El proyecto **Bar Bara** cumple el objetivo del examen mostrando claramente las **vistas de la aplicación**, con un uso correcto de **HTML para estructura**, **CSS (Flexbox y Grid) para maquetación** y **JavaScript mínimo** para mejorar la experiencia del usuario. PHP se utiliza únicamente como apoyo para la lógica.

Este documento explica cómo el usuario se mueve entre pantallas y detalla cada vista tal y como se pediría en un examen práctico.

