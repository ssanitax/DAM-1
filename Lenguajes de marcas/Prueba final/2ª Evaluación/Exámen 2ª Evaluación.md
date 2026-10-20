## Bar Bara - Lenguajes de marcas

Este proyecto consiste en el desarrollo de un sistema de gestión para un establecimiento de hostelería (Bar Bara), diseñado con una arquitectura que separa la lógica del servidor (Backend) de la interfaz de usuario (Frontend).

El objetivo es digitalizar el ciclo de servicio, desde que el cliente se registra hasta que solicita el pago en mesa.

---

## Estructura de los directorios

Directory structure:
└── ssanitax-bar_bara/
    ├── back/
    │   ├── index.php
    │   ├── listar_productos.php
    │   ├── peticion_login.php
    │   ├── peticion_pedido.php
    │   ├── controladores/
    │   │   ├── PedidoControlador.php
    │   │   ├── ProductoControlador.php
    │   │   └── UsuarioControlador.php
    │   ├── css/
    │   │   └── estilo.css
    │   └── inc/
    │       └── conexion_bd.php
    └── front/
        ├── carrito.php
        ├── catalogo.php
        ├── contacto.php
        ├── finalizacion.php
        ├── historial.php
        ├── index.php
        ├── login.php
        ├── logout.php
        ├── procesar_pedido.php
        ├── producto.php
        ├── registro.php
        ├── css/
        │   └── estilo.css
        ├── img
        └── inc/
            ├── cabecera.php
            └── piedepagina.php

---

## Explicación del código

**front/index.php**

- Pantalla de bienvenida.
- Desde aquí el usuario puede ir al catálogo, al carrito o a contacto.

```
<?php 
// Conecta con la base de datos
require_once '../back/inc/conexion_bd.php';

// Incluye la cabecera común del sitio
include 'inc/cabecera.php'; 
?>

<!-- Conectamos el archivo CSS externo -->
<link rel="stylesheet" href="css/estilo.css">

<!-- Representa el contenido principal de la página -->
<main class="hero-section">
    
    <!-- Mostramos el logo del bar -->
    <img src="img/logo_home.png" alt="Bar Bara Logo" class="hero-logo-img">

    <!-- Texto descriptivo del negocio -->
    <p class="hero-subtitle">
        Comida con Carácter & Tragos Rebeldes
    </p>

    <!-- Contenedor de los botones principales -->
    <div class="action-grid">
        
        <!-- Botón para ver la carta, redirige a catalogo.php -->
        <a href="catalogo.php" class="btn-hero btn-carta">
            <span class="icon">🍔</span>
            Ver La Carta
        </a>

        <!-- Botón que lleva al carrito de compra -->
        <a href="carrito.php" class="btn-hero btn-carrito-hero">
            <span class="icon">🛒</span>
            Mi Pedido
        </a>

        <!-- Botón de contacto y reservas -->
        <a href="contacto.php" class="btn-hero btn-contacto">
            <span class="icon">📍</span>
            Contacto / Reservas
        </a>

    </div>

</main>

<?php 
// Incluimos el pie de página
include 'inc/piedepagina.php'; 
?>
```

**front/login.php y front/registro.php**

- El usuario se identifica para que el sistema pueda asociar pedidos a una mesa/cliente.

```
<?php include 'inc/cabecera.php'; ?>
<!-- Incluye la cabecera común del sitio (doctype, head, menú, etc.) -->

<link rel="stylesheet" href="css/estilo.css">
<!-- Carga la hoja de estilos principal -->

<!-- CONTENEDOR PRINCIPAL DEL FORMULARIO -->
<div class="container" style="max-width: 500px; margin: 50px auto; padding: 20px;">
    <!-- Limita el ancho, centra el contenido y añade espacio -->

    <!-- LOGO SUPERIOR -->
    <div style="text-align: center; margin-bottom: 20px;">
        <img src="img/logo_home.jpg" alt="Logo" style="width: 80px; border-radius: 50%;">
        <!-- Imagen del logo, redonda y centrada -->
    </div>

    <!-- TÍTULO DEL FORMULARIO -->
    <h2 style="text-align: center; color: var(--color-navy);">
        Únete a la Familia
    </h2>

    <!-- TEXTO DESCRIPTIVO -->
    <p style="text-align: center; color: #666;">
        Regístrate para confirmar tu pedido
    </p>

    <!-- MENSAJE DE ERROR (solo aparece si existe la variable $error) -->
    <?php if(isset($error)): ?>
        <div style="background: var(--color-red); color: white; padding: 10px; border-radius: 5px; margin-bottom: 15px; text-align: center;">
            ⚠️ <?= $error ?>
            <!-- Muestra el mensaje de error enviado desde PHP -->
        </div>
    <?php endif; ?>

    <!-- FORMULARIO DE REGISTRO -->
    <form method="POST" style="background: white; padding: 30px; border-radius: 12px; box-shadow: 0 4px 10px rgba(0,0,0,0.1);">
        <!-- method="POST" envía los datos de forma segura -->

        <!-- CAMPO NOMBRE -->
        <div style="margin-bottom: 15px;">
            <label style="font-weight: bold; color: var(--color-navy);">
                Nombre
            </label>
            <input 
                type="text" 
                name="nombre" 
                required 
                placeholder="Ej: Juan"
                style="width: 100%; padding: 10px; border: 1px solid #ccc; border-radius: 5px; box-sizing: border-box;">
            <!-- Campo obligatorio para el nombre -->
        </div>

        <!-- CAMPO APELLIDOS -->
        <div style="margin-bottom: 15px;">
            <label style="font-weight: bold; color: var(--color-navy);">
                Apellidos
            </label>
            <input 
                type="text" 
                name="apellidos" 
                required 
                placeholder="Ej: Pérez"
                style="width: 100%; padding: 10px; border: 1px solid #ccc; border-radius: 5px; box-sizing: border-box;">
        </div>

        <!-- CAMPO EMAIL -->
        <div style="margin-bottom: 15px;">
            <label style="font-weight: bold; color: var(--color-navy);">
                Correo Electrónico
            </label>
            <input 
                type="email" 
                name="correo" 
                required 
                placeholder="tu@email.com"
                style="width: 100%; padding: 10px; border: 1px solid #ccc; border-radius: 5px; box-sizing: border-box;">
            <!-- type="email" valida que tenga formato de correo -->
        </div>

        <!-- CAMPO CONTRASEÑA -->
        <div style="margin-bottom: 25px;">
            <label style="font-weight: bold; color: var(--color-navy);">
                Contraseña
            </label>
            <input 
                type="password" 
                name="pass" 
                required 
                placeholder="******"
                style="width: 100%; padding: 10px; border: 1px solid #ccc; border-radius: 5px; box-sizing: border-box;">
            <!-- El texto se oculta automáticamente -->
        </div>

        <!-- BOTÓN DE ENVÍO -->
        <button 
            type="submit" 
            class="btn-hero btn-carta" 
            style="width: 100%; border: none; cursor: pointer; font-size: 1.1rem;">
            Registrarse ➔
        </button>
        <!-- Envía el formulario -->
    </form>

    <!-- ENLACE A LOGIN -->
    <p style="text-align: center; margin-top: 20px;">
        ¿Ya tienes cuenta?
        <a href="login.php" style="color: var(--color-red); font-weight: bold;">
            Inicia sesión aquí
        </a>
    </p>
</div>

<?php include 'inc/piedepagina.php'; ?>
<!-- Incluye el pie de página común -->
```

```
<?php include 'inc/cabecera.php'; ?>
<!-- Incluye la cabecera común del sitio (doctype, head, menú, etc.) -->

<link rel="stylesheet" href="css/estilo.css">
<!-- Hoja de estilos principal -->

<!-- CONTENEDOR PRINCIPAL DEL LOGIN -->
<div class="container" style="max-width: 450px; margin: -200px auto; padding: 20px;">
    <!--
        max-width: limita el ancho del formulario
        margin: centra el contenedor (margen superior negativo para subirlo)
        padding: espacio interior
    -->

    <!-- LOGO Y TEXTO DE BIENVENIDA -->
    <div style="text-align: center; margin-bottom: 20px;">
        <!-- Logo del bar -->
        <img src="img/logo_home.png" alt="Logo" style="width: 180px;">

        <!-- Mensaje de bienvenida -->
        <h2 style="color: var(--color-navy); margin-top: 10px; font-size: 1.5rem;">
            Bienvenido de nuevo
        </h2>
    </div>

    <!-- MENSAJE DE ERROR (solo se muestra si $error no está vacío) -->
    <?php if(!empty($error)): ?>
        <div style="background: var(--color-red); color: white; padding: 10px; border-radius: 5px; margin-bottom: 15px; text-align: center;">
            ⚠️ <?= $error ?>
        </div>
    <?php endif; ?>

    <!-- FORMULARIO DE LOGIN -->
    <form method="POST" style="background: white; padding: 25px; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
        <!--
            method="POST" envía los datos de forma segura
            action no se especifica → se envía a la misma página
        -->

        <!-- CAMPO CORREO ELECTRÓNICO -->
        <div style="margin-bottom: 15px;">
            <label style="font-weight: bold; color: var(--color-navy); display: block; margin-bottom: 5px;">
                Correo Electrónico
            </label>

            <input 
                type="email" 
                name="correo" 
                required 
                placeholder="tu@email.com"
                style="width: 100%; padding: 12px; border: 1px solid #ccc; border-radius: 8px; box-sizing: border-box;">
            <!-- El navegador valida automáticamente el formato del email -->
        </div>

        <!-- CAMPO CONTRASEÑA -->
        <div style="margin-bottom: 25px;">
            <label style="font-weight: bold; color: var(--color-navy); display: block; margin-bottom: 5px;">
                Contraseña
            </label>

            <input 
                type="password" 
                name="pass" 
                required 
                placeholder="******"
                style="width: 100%; padding: 12px; border: 1px solid #ccc; border-radius: 8px; box-sizing: border-box;">
            <!-- El texto se oculta automáticamente -->
        </div>

        <!-- BOTÓN PARA ENVIAR EL FORMULARIO -->
        <button 
            type="submit" 
            class="btn-hero btn-contacto" 
            style="width: 100%; border: none; cursor: pointer; padding: 15px; font-size: 1.1rem;">
            Entrar al Bar 🍺
        </button>
    </form>

    <!-- SECCIÓN INFERIOR: ENLACE A REGISTRO -->
    <div style="text-align: center; margin-top: 20px; padding-top: 15px; border-top: 1px solid #ddd;">
        <p style="color: #666; margin-bottom: 10px;">
            ¿Es tu primera vez aquí?
        </p>

        <a href="registro.php" class="btn-hero btn-carta" style="display: inline-block; padding: 10px 20px; font-size: 1rem; text-decoration: none;">
            Crear Cuenta Gratis
        </a>
    </div>
</div>

<?php include 'inc/piedepagina.php'; ?>
<!-- Incluye el pie de página común -->
```

**front/catalogo.php**

- Se muestran todos los productos organizados por categorías.
- El usuario selecciona productos y cantidades.

```
<?php 
session_start();
require_once '../back/inc/conexion_bd.php'; 
include 'inc/cabecera.php'; 

// Preparamos los datos antes de mostrar el HTML
$res_cat = $pdo->query("SELECT DISTINCT categoria FROM producto ORDER BY categoria");
$categorias = $res_cat->fetchAll(PDO::FETCH_COLUMN);

$stmt = $pdo->query("SELECT * FROM producto ORDER BY categoria, nombre_producto");
?>

<!-- ===========================
     ESTILOS DEL CATÁLOGO
     =========================== -->
<style>
    /* Barra de navegación de categorías */
    .categorias-nav {
        display: flex;
        justify-content: center;
        gap: 15px;
        flex-wrap: wrap;
        padding: 30px;
        background: #f4f4f4;
        border-bottom: 2px solid #ddd;
        margin-bottom: 30px;
        border-radius: 12px;
        margin-top: -70px;
        position: sticky;
        top: 0px;                
        z-index: 900;
    }

    /* Enlaces de categoría */
    .cat-link {
        background: #153e5c; 
        color: white;
        padding: 10px 20px;
        border-radius: 20px;
        text-decoration: none;
        font-weight: bold;
    }

    .cat-link:hover { background: #eaa833; }

    /* Grid principal del catálogo */
    .catalogo-grid { 
        display: grid; 
        grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); 
        gap: 25px; 
    }

    /* Tarjeta individual de producto */
    .producto-card { 
        border: 1px solid #ddd; 
        border-radius: 12px; 
        padding: 20px; 
        text-align: center; 
        background: #fff; 
        display: flex; 
        flex-direction: column; 
        justify-content: space-between; 
    }

    /* Imagen del producto */
    .producto-img { 
        width: 100%; 
        height: 200px; 
        object-fit: cover; 
        border-radius: 8px; 
    }

    /* Control de cantidad */
    .cantidad-control { 
        display: flex; 
        align-items: center; 
        justify-content: center; 
        gap: 10px; 
        margin-bottom: 15px; 
    }

    /* Botones + y - */
    .btn-qty { 
        background: #153e5c; 
        color: white; 
        border: none; 
        width: 32px; 
        height: 32px; 
        border-radius: 50%; 
        cursor: pointer; 
    }

    /* Input de cantidad */
    .input-qty { 
        width: 45px; 
        text-align: center; 
        border: 1px solid #ddd; 
        border-radius: 5px; 
        font-weight: bold; 
    }

    /* Botón añadir al carrito */
    .btn-add { 
        background: #27ae60; 
        color: white; 
        border: none; 
        padding: 12px; 
        border-radius: 5px; 
        cursor: pointer; 
        font-weight: bold; 
    }

    /* Título de cada categoría */
    .categoria-titulo { 
        grid-column: 1 / -1; 
        text-align: left; 
        margin-top: 50px; 
        border-bottom: 3px solid #eaa833; 
        color: #153e5c; 
    }
</style>

<!-- ===========================
     NAVEGACIÓN DE CATEGORÍAS
     =========================== -->
<div class="categorias-nav">
    <!-- Enlaces ancla a cada categoría -->
    <?php foreach ($categorias as $c): ?>
        <a href="#<?php echo urlencode($c); ?>" class="cat-link">
            <?php echo htmlspecialchars($c); ?>
        </a>
    <?php endforeach; ?>
</div>

<!-- ===========================
     GRID DE PRODUCTOS
     =========================== -->
<div class="catalogo-grid">
    <?php
    $actual_cat = "";

    // Recorremos todos los productos
    while ($row = $stmt->fetch(PDO::FETCH_ASSOC)):

        // Si cambia la categoría, mostramos su título
        if ($actual_cat != $row['categoria']):
            $actual_cat = $row['categoria']; ?>
            <h2 class="categoria-titulo" id="<?php echo urlencode($actual_cat); ?>">
                <?php echo htmlspecialchars($actual_cat); ?>
            </h2>
        <?php endif; ?>
        
        <!-- Tarjeta de producto -->
        <div class="producto-card">

            <!-- Parte superior: imagen y nombre -->
            <div>
                <img src="img/<?php echo $row['imagen']; ?>" class="producto-img">
                <h3 style="margin: 15px 0 5px 0;">
                    <?php echo htmlspecialchars($row['nombre_producto']); ?>
                </h3>
            </div>

            <!-- Parte inferior: precio y formulario -->
            <div style="margin-top: 20px;">

                <!-- Precio del producto -->
                <p style="font-size: 1.4em; color: #153e5c; margin-bottom: 15px;">
                    <strong><?php echo number_format($row['precio'], 2); ?>€</strong>
                </p>
                
                <!-- Formulario para añadir al carrito -->
                <form action="carrito.php" method="POST">

                    <!-- ID del producto oculto -->
                    <input type="hidden" name="id" value="<?php echo $row['id']; ?>">

                    <!-- Selector de cantidad -->
                    <div class="cantidad-control">
                        <button type="button" class="btn-qty" onclick="this.nextElementSibling.stepDown()">-</button>
                        <input type="number" name="cantidad" class="input-qty" value="1" min="1" readonly>
                        <button type="button" class="btn-qty" onclick="this.previousElementSibling.stepUp()">+</button>
                    </div>

                    <!-- Botón para añadir el producto -->
                    <button type="submit" name="add" class="btn-add">
                        Añadir al pedido
                    </button>
                </form>
            </div>
        </div>

    <?php endwhile; ?>
</div>

<?php include 'inc/piedepagina.php'; ?>
```

**front/carrito.php**

- Se revisa el pedido.
- Se pueden modificar cantidades o eliminar productos.
- Se introduce el número de mesa y se confirma el pedido.

```
<?php
session_start();

// Conexión a la base de datos
include '../back/inc/conexion_bd.php';

/* ===========================
   LÓGICA DEL CARRITO (PHP)
   =========================== */

if (isset($_POST['add'])) {
    $id_producto = $_POST['id'];
    $cantidad = isset($_POST['cantidad']) ? (int)$_POST['cantidad'] : 1;

    $stmt = $pdo->prepare("SELECT * FROM producto WHERE id = ?");
    $stmt->execute([$id_producto]);
    $producto_bd = $stmt->fetch(PDO::FETCH_ASSOC);

    if ($producto_bd) {
        if (!isset($_SESSION['carrito'])) {
            $_SESSION['carrito'] = [];
        }

        $ya_existe = false;
        foreach ($_SESSION['carrito'] as $indice => $item) {
            if ($item['id'] == $id_producto) {
                $_SESSION['carrito'][$indice]['cantidad'] += $cantidad;
                $ya_existe = true;
                break;
            }
        }

        if (!$ya_existe) {
            $_SESSION['carrito'][] = [
                'id'       => $producto_bd['id'],
                'nombre'   => $producto_bd['nombre_producto'],
                'precio'   => $producto_bd['precio'],
                'imagen'   => $producto_bd['imagen'],
                'cantidad' => $cantidad
            ];
        }
    }

    header("Location: catalogo.php");
    exit;
}

/* Actualizar cantidad */
if (isset($_POST['actualizar_cantidad'])) {
    $id_producto = $_POST['id'];
    $nueva_cantidad = (int)$_POST['cantidad'];

    if (isset($_SESSION['carrito']) && $nueva_cantidad > 0) {
        foreach ($_SESSION['carrito'] as $indice => $item) {
            if ($item['id'] == $id_producto) {
                $_SESSION['carrito'][$indice]['cantidad'] = $nueva_cantidad;
                break;
            }
        }
    }

    header("Location: carrito.php");
    exit;
}

/* Eliminar producto */
if (isset($_POST['btn_eliminar'])) {
    $id_a_borrar = $_POST['id_eliminar'];

    foreach ($_SESSION['carrito'] as $indice => $producto) {
        if ($producto['id'] == $id_a_borrar) {
            unset($_SESSION['carrito'][$indice]);
            $_SESSION['carrito'] = array_values($_SESSION['carrito']);
            break;
        }
    }

    header("Location: carrito.php");
    exit;
}

/* Calcular total */
$total = 0;
if (isset($_SESSION['carrito'])) {
    foreach ($_SESSION['carrito'] as $item) {
        $total += $item['precio'] * $item['cantidad'];
    }
}

// Cabecera
include 'inc/cabecera.php';
?>

<link rel="stylesheet" href="css/estilo.css">

<!-- ===========================
     CONTENIDO DEL CARRITO
     =========================== -->

<!-- Contenedor principal del carrito -->
<div class="comanda-container">

    <!-- Título principal -->
    <h2 style="color: #153e5c; text-align: center;">🛒 Nuestra Comanda</h2>

    <!-- Si el carrito tiene productos -->
    <?php if (!empty($_SESSION['carrito'])): ?>

        <!-- Tabla de productos -->
        <table class="tabla-bar-bara">
            <tbody>

                <?php foreach ($_SESSION['carrito'] as $p): ?>

                    <!-- Fila de un producto -->
                    <tr class="fila-producto">

                        <!-- Imagen del producto -->
                        <td width="100">
                            <img src="img/<?php echo $p['imagen']; ?>" class="img-carrito" alt="Foto">
                        </td>

                        <!-- Nombre y precio unitario -->
                        <td>
                            <strong style="font-size: 1.1rem;">
                                <?php echo htmlspecialchars($p['nombre']); ?>
                            </strong><br>
                            <span style="color: #666;">
                                <?php echo number_format($p['precio'], 2); ?>€
                            </span>
                        </td>

                        <!-- Selector de cantidad -->
                        <td align="center">
                            <form action="carrito.php" method="POST" class="selector-cantidad">
                                <input type="hidden" name="id" value="<?php echo $p['id']; ?>">
                                <button type="submit" name="actualizar_cantidad" class="btn-ajuste" onclick="this.nextElementSibling.stepDown()">-</button>
                                <input type="number" name="cantidad" value="<?php echo $p['cantidad']; ?>" min="1" readonly>
                                <button type="submit" name="actualizar_cantidad" class="btn-ajuste" onclick="this.previousElementSibling.stepUp()">+</button>
                            </form>
                        </td>

                        <!-- Subtotal del producto -->
                        <td>
                            <span style="font-weight: 800; font-size: 1.2rem; color: #c93b2b;">
                                <?php echo number_format($p['precio'] * $p['cantidad'], 2); ?>€
                            </span>
                        </td>

                        <!-- Botón eliminar -->
                        <td align="right">
                            <form action="carrito.php" method="POST">
                                <input type="hidden" name="id_eliminar" value="<?php echo $p['id']; ?>">
                                <button type="submit" name="btn_eliminar" style="background:none; border:none; cursor:pointer;">
                                    Eliminar 🗑️
                                </button>
                            </form>
                        </td>

                    </tr>

                <?php endforeach; ?>

            </tbody>
        </table>

        <!-- Total y confirmación -->
        <div class="total-card">
            <div>
                <span style="color: #666; font-size: 0.8rem;">Total Mesa</span>
                <h3 style="margin:0; font-size: 2.2rem;">
                    <?php echo number_format($total, 2); ?>€
                </h3>
            </div>

            <form action="procesar_pedido.php" method="POST">
                <label>Nº MESA</label>
                <input type="number" name="numero_mesa" required>
                <input type="hidden" name="total_pagar" value="<?php echo $total; ?>">
                <button type="submit" class="btn-hero btn-carrito-hero">
                    PEDIR AHORA 🚀
                </button>
            </form>
        </div>

    <?php else: ?>

        <!-- Carrito vacío -->
        <div class="empty-cart-container">
            <img src="img/logo_triste.png" style="width: 150px;">
            <h2>¡Vuestra mesa está vacía!</h2>
            <a href="catalogo.php" class="btn-carta-vacio">🍔 Ver la Carta</a>
        </div>

    <?php endif; ?>
</div>

<?php include 'inc/piedepagina.php'; ?>
```

**finalizacion.php**

- Mensaje de confirmación.
- El pedido pasa a cocina.

```
<?php 
// Iniciamos la sesión
session_start();

// Incluimos la cabecera común del sitio
include 'inc/cabecera.php';
?>

<!-- ===========================
     CONTENIDO PRINCIPAL
     =========================== -->
<main class="container" style="text-align: center; padding: 40px 20px;">

    <!-- Tarjeta central de confirmación -->
    <div style="background: white; padding: 40px; border-radius: 15px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); max-width: 600px; margin: 0 auto;">

        <!-- Icono visual decorativo -->
        <div style="font-size: 4rem; margin-bottom: 20px;">
            👨‍🍳
        </div>

        <!-- Título principal -->
        <h1 style="color: #153e5c;">
            ¡Marchando!
        </h1>

        <!-- Mensaje informativo para el cliente -->
        <p style="font-size: 1.2rem; color: #555;">
            Tu comanda ha llegado a la cocina y se está preparando ahora mismo.
        </p>
        
        <!-- Contenedor de botones de acción -->
        <div style="margin-top: 30px; display: flex; flex-direction: column; gap: 15px;">

            <!-- Botón para volver al catálogo y pedir más -->
            <a href="catalogo.php" class="btn-hero btn-carta" style="text-decoration: none; padding: 15px;">
                Pedir otra ronda 🍻
            </a>

            <!-- Botón para ver el resumen de la mesa -->
            <a href="historial.php" class="btn-hero btn-contacto" style="text-decoration: none; padding: 15px; background: #153e5c; color: white;">
                Ver resumen de mi mesa 📝
            </a>

        </div>
    </div>
</main>

<?php 
// Incluimos el pie de página
include 'inc/piedepagina.php'; 
?>
```

**historial.php**

- Resumen del pedido activo.
- El usuario puede pedir la cuenta.
   
```
<?php 
// Iniciamos la sesión
session_start();

// Incluimos la cabecera común del sitio
include 'inc/cabecera.php';
?>

<!-- ===========================
     CONTENIDO PRINCIPAL
     =========================== -->
<main class="container" style="text-align: center; padding: 40px 20px;">

    <!-- Tarjeta central de confirmación -->
    <div style="background: white; padding: 40px; border-radius: 15px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); max-width: 600px; margin: 0 auto;">

        <!-- Icono visual decorativo -->
        <div style="font-size: 4rem; margin-bottom: 20px;">
            👨‍🍳
        </div>

        <!-- Título principal -->
        <h1 style="color: #153e5c;">
            ¡Marchando!
        </h1>

        <!-- Mensaje informativo para el cliente -->
        <p style="font-size: 1.2rem; color: #555;">
            Tu comanda ha llegado a la cocina y se está preparando ahora mismo.
        </p>
        
        <!-- Contenedor de botones de acción -->
        <div style="margin-top: 30px; display: flex; flex-direction: column; gap: 15px;">

            <!-- Botón para volver al catálogo y pedir más -->
            <a href="catalogo.php" class="btn-hero btn-carta" style="text-decoration: none; padding: 15px;">
                Pedir otra ronda 🍻
            </a>

            <!-- Botón para ver el resumen de la mesa -->
            <a href="historial.php" class="btn-hero btn-contacto" style="text-decoration: none; padding: 15px; background: #153e5c; color: white;">
                Ver resumen de mi mesa 📝
            </a>

        </div>
    </div>
</main>

<?php 
// Incluimos el pie de página
include 'inc/piedepagina.php'; 
?>
```

**contacto.php**

- Formulario informativo independiente del pedido.

```
<?php 
// Iniciamos la sesión
session_start();

// Incluimos la cabecera común del sitio
include 'inc/cabecera.php';
?>

<!-- ===========================
     CONTENIDO PRINCIPAL
     =========================== -->
<main class="container" style="text-align: center; padding: 40px 20px;">

    <!-- Tarjeta central de confirmación -->
    <div style="background: white; padding: 40px; border-radius: 15px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); max-width: 600px; margin: 0 auto;">

        <!-- Icono visual decorativo -->
        <div style="font-size: 4rem; margin-bottom: 20px;">
            👨‍🍳
        </div>

        <!-- Título principal -->
        <h1 style="color: #153e5c;">
            ¡Marchando!
        </h1>

        <!-- Mensaje informativo para el cliente -->
        <p style="font-size: 1.2rem; color: #555;">
            Tu comanda ha llegado a la cocina y se está preparando ahora mismo.
        </p>
        
        <!-- Contenedor de botones de acción -->
        <div style="margin-top: 30px; display: flex; flex-direction: column; gap: 15px;">

            <!-- Botón para volver al catálogo y pedir más -->
            <a href="catalogo.php" class="btn-hero btn-carta" style="text-decoration: none; padding: 15px;">
                Pedir otra ronda 🍻
            </a>

            <!-- Botón para ver el resumen de la mesa -->
            <a href="historial.php" class="btn-hero btn-contacto" style="text-decoration: none; padding: 15px; background: #153e5c; color: white;">
                Ver resumen de mi mesa 📝
            </a>

        </div>
    </div>
</main>

<?php 
// Incluimos el pie de página
include 'inc/piedepagina.php'; 
?>
```

**inc/front/cabecera.php**

```
<?php
// Iniciamos la sesión si no está activa
if (session_status() === PHP_SESSION_NONE) {
    session_start();
}

// Calculamos la cantidad total de productos en el carrito
$cantidad_total = 0;
if (isset($_SESSION['carrito'])) {
    foreach ($_SESSION['carrito'] as $producto) {
        $cantidad_total += $producto['cantidad'];
    }
}

// Comprobamos si el usuario está conectado
$usuario_conectado = isset($_SESSION['user_id']);
$nombre_usuario = isset($_SESSION['nombre']) ? $_SESSION['nombre'] : 'Cliente';
?>
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Bar Bara</title>
    <link rel="icon" type="image/png" href="img/logo_home.png">
    
    <!-- ===========================
         ESTILOS DEL HEADER
         =========================== -->
    <style>
        /* Estilos generales del body */
        body { 
            margin: 0; 
            font-family: sans-serif; 
            background-color: #f8f1e0; 
        }
        
        /* Header azul superior */
        .header-azul {
            background-color: #153e5c;
            height: 90px;
            color: white;
            display: flex;
            align-items: center;
            justify-content: flex-end; 
            padding: 0 5%;
            position: relative;
            z-index: 10;
            border-bottom: 4px solid #eaa833;
            box-shadow: 0 4px 10px rgba(0,0,0,0.3);
        }

        /* Logo superpuesto sobre el header */
        .logo-superpuesto {
            position: absolute;
            top: -30px; 
            left: 20px;
            z-index: 100; 
        }

        .logo-superpuesto img {
            height: 160px;
            width: auto;
            display: block;
            filter: drop-shadow(0 10px 15px rgba(0,0,0,0.5));
            transition: all 0.3s ease;
        }

        /* Lista del menú */
        .menu-lista {
            display: flex;
            list-style: none;
            gap: 20px;
            align-items: center;
            margin: 0; padding: 0;
        }

        /* Enlaces del menú */
        .menu-lista a {
            color: #f8f1e0;
            text-decoration: none;
            font-weight: bold;
            text-transform: uppercase;
            font-size: 0.85rem;
        }

        /* Botón del carrito/pedido */
        .btn-pedido {
            background-color: #c93b2b;
            padding: 8px 15px;
            border-radius: 8px;
            display: flex;
            align-items: center;
            gap: 8px;
            color: white !important;
            transition: transform 0.2s;
        }

        /* Badge que muestra la cantidad de productos */
        .badge {
            background: white;
            color: #c93b2b;
            padding: 2px 6px;
            border-radius: 50%;
            font-size: 0.85em;
            font-weight: bold;
        }

        /* Mensaje de bienvenida del usuario */
        .user-welcome { 
            color: #eaa833; 
            font-weight: bold; 
            margin-right: 5px; 
        }
        
        /* Responsive para móviles */
        @media (max-width: 768px) {
            .logo-superpuesto img { height: 110px; }
            .logo-superpuesto { top: -15px; left: 10px; }
            .menu-lista { gap: 12px; }
            .ocultar-movil { display: none; }
        }
    </style>
</head>
<body>

<!-- ===========================
     HEADER PRINCIPAL
     =========================== -->
<header class="header-azul">

    <!-- Logo superpuesto -->
    <div class="logo-superpuesto">
        <a href="index.php">
            <img src="img/ChatGPT_Image_11_ene_2026__17_05_50-removebg-preview.png" alt="Logo Bar Bara">
        </a>
    </div>

    <!-- Menú de navegación -->
    <ul class="menu-lista">
        <!-- Enlace a la carta -->
        <li><a href="catalogo.php">Carta</a></li>
        
        <!-- Si el usuario está conectado -->
        <?php if ($usuario_conectado): ?>
            <li><a href="historial.php">Historial</a></li>
            <li>
                <!-- Mensaje de bienvenida -->
                <span class="user-welcome ocultar-movil">
                    Hola, <?php echo htmlspecialchars($nombre_usuario); ?>
                </span>
            </li>
        <?php endif; ?>

        <!-- Botón del carrito con badge -->
        <li>
            <a href="carrito.php" class="btn-pedido">
                🛒 <span class="badge"><?php echo $cantidad_total; ?></span>
            </a>
        </li>

        <!-- Enlace de login/logout según estado -->
        <?php if ($usuario_conectado): ?>
            <li>
                <a href="logout.php" style="font-size: 0.75rem; border: 1px solid white; padding: 4px; border-radius: 5px;">
                    Salir
                </a>
            </li>
        <?php else: ?>
            <li><a href="login.php">👤 Entrar</a></li>
        <?php endif; ?>
    </ul>
</header>

<!-- ===========================
     ESPACIO DEL CONTENIDO
     =========================== -->
<div style="margin-top: 50px; padding: 20px; min-height: 80vh;">

```

**inc/front/piedepagina.php**

```
</div> <!-- Cierre del contenedor principal del contenido -->

<!-- ===========================
     FOOTER PRINCIPAL
     =========================== -->
<footer style="background: #2c3e50; color: white; text-align: center; padding: 20px; margin-top: auto; width: 100%;">

    <!-- Texto de copyright -->
    <p>&copy; 2026 Bar Bara - Todos los derechos reservados.</p>
    
    <!-- Dirección física de la empresa -->
    <p style="font-size: 0.8em; color: #bdc3c7; margin-top: 10px;">
        Calle Pedro Antonio de Alarcón, 17 - Granada, 18001
    </p>

</footer>

</body>
</html>
```

**back/index.php**

```
<?php
// index.php en la raíz del back

// Incluimos conexión a la base de datos
require_once 'inc/conexion_bd.php';

// Incluimos los controladores de Pedido y Producto
require_once 'controladores/PedidoControlador.php';
require_once 'controladores/ProductoControlador.php';

// Instanciamos los controladores con la conexión PDO
$pedidoCtrl = new PedidoControlador($pdo);
$productoCtrl = new ProductoControlador($pdo);

// --- LÓGICA DE ACCIONES ---

// 1. Marcar pedido como entregado (Cocina)
if (isset($_POST['entregar_id'])) {
    $pedidoCtrl->marcarComoEntregado($_POST['entregar_id']);
}

// 2. Marcar pedido como pagado (Barra) y actualizar estado en la base
if (isset($_POST['cobrar_id'])) {
    $idPedido = $_POST['cobrar_id'];
    $sql = "UPDATE pedido SET pedir_cuenta = 'PAGADO' WHERE id = ?";
    $stmt = $pdo->prepare($sql);
    $stmt->execute([$idPedido]);
}

// Obtenemos los totales y pedidos desde la base
try {
    $totalProductos = count($productoCtrl->listarTodo());
    
    // COMANDAS POR SERVIR: solo las que NO están entregadas
    $pendientes = $pdo->query("SELECT * FROM pedido WHERE pedir_cuenta IN ('NO', 'SI') ORDER BY hora ASC")->fetchAll();    

    // ALERTAS DE COBRO: solo las que solicitan la cuenta
    $alertas = $pdo->query("SELECT * FROM pedido WHERE pedir_cuenta IN ('SI', 'SI_ENTREGADO') ORDER BY hora ASC")->fetchAll();
    
    $conteoAlertas = count($alertas);
} catch (Exception $e) {
    die("Error en la base de datos: " . $e->getMessage());
}
?>
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Bar Bara - Panel Unificado</title>

    <!-- Enlace al CSS externo -->
    <link rel="stylesheet" href="css/estilo.css">

    <!-- Auto-refresh cada 30 segundos -->
    <meta http-equiv="refresh" content="30">

    <!-- Estilos internos rápidos -->
    <style>
        .seccion { margin-bottom: 40px; }
        .titulo-seccion { padding: 10px; border-radius: 8px; margin-bottom: 20px; color: white; }
    </style>
</head>
<body>

<!-- ===========================
     NAV / HEADER DEL PANEL
     =========================== -->
<nav>
    <!-- Logo y título -->
    <div class="logo">🍴 BAR BARA - PANEL DE CONTROL</div>

    <!-- Estado rápido de productos totales -->
    <div class="header-status">
        <code>PRODUCTOS: <?php echo $totalProductos; ?></code>
    </div>
</nav>

<!-- ===========================
     CONTENIDO PRINCIPAL
     =========================== -->
<div class="container">
    
    <!-- ===========================
         ALERTAS DE COBRO
         =========================== -->
    <div class="seccion">
        <h2 class="titulo-seccion" style="background: var(--error);">
            🔔 ALERTAS DE COBRO (<?php echo $conteoAlertas; ?>)
        </h2>

        <div class="grid-productos">
            <?php if (empty($alertas)): ?>
                <!-- Mensaje si no hay alertas -->
                <div class="card"><h3>No hay mesas solicitando la cuenta.</h3></div>
            <?php else: ?>
                <!-- Iteramos sobre las alertas -->
                <?php foreach($alertas as $a): ?>
                    <div class="card" style="border-left: 10px solid var(--error); text-align: left;"> 
                        <!-- Número de mesa y total -->
                        <h2 style="margin:0">MESA <?php echo $a['numero_mesa']; ?></h2>
                        <p><strong>Total a cobrar: <?php echo $a['total']; ?>€</strong></p>
                        <p>Hora solicitud: <?php echo $a['hora']; ?></p>
                        
                        <!-- Formulario para marcar como cobrado -->
                        <form method="POST">
                            <input type="hidden" name="cobrar_id" value="<?php echo $a['id']; ?>">
                            <button type="submit" class="button" style="background: var(--exito); width:100%; border:none; cursor:pointer; margin-top:10px;">
                                💰 MARCAR COMO COBRADO
                            </button>
                        </form>
                    </div>
                <?php endforeach; ?>
            <?php endif; ?>
        </div>
    </div>

    <hr>

    <!-- ===========================
         COMANDAS POR SERVIR
         =========================== -->
    <div class="seccion">
        <h2 class="titulo-seccion" style="background: var(--primario);">📥 COMANDAS POR SERVIR</h2>

        <div class="grid-productos">
            <?php if (empty($pendientes)): ?>
                <!-- Mensaje si no hay comandas pendientes -->
                <div class="card"><h3>Cero comandas pendientes.</h3></div>
            <?php else: ?>
                <!-- Iteramos sobre las comandas pendientes -->
                <?php foreach ($pendientes as $p): ?>
                    <div class="card" style="border-left: 10px solid var(--primario); text-align: left;"> 
                        
                        <!-- Número de mesa y hora -->
                        <div style="display:flex; justify-content:space-between; align-items:center;">
                            <h2 style="margin:0">MESA <?php echo $p['numero_mesa']; ?></h2>
                            <span style="background:#eee; padding:5px 10px; border-radius:5px; font-weight:bold;">
                                <?php echo date('H:i', strtotime($p['hora'])); ?>
                            </span>
                        </div>

                        <hr style="margin: 10px 0; border: 0; border-top: 1px dashed #ccc;">

                        <!-- Lista de productos en la comanda -->
                        <ul style="padding-left: 20px; margin: 10px 0;">
                            <?php 
                            // Obtenemos productos y cantidades de este pedido
                            $sqlDetalles = "SELECT cp.cantidad, prod.nombre_producto 
                                            FROM contenido_pedido cp 
                                            JOIN producto prod ON cp.producto_id = prod.id 
                                            WHERE cp.pedido_id = ?";
                            $stmtDetalles = $pdo->prepare($sqlDetalles);
                            $stmtDetalles->execute([$p['id']]);
                            $detalles = $stmtDetalles->fetchAll();

                            foreach($detalles as $d): ?>
                                <li style="font-size: 1.1rem; margin-bottom: 5px;">
                                    <strong><?php echo $d['cantidad']; ?>x</strong> 
                                    <?php echo htmlspecialchars($d['nombre_producto']); ?>
                                </li>
                            <?php endforeach; ?>
                        </ul>

                        <!-- Total de la mesa -->
                        <p style="text-align: right; color: #666; font-size: 0.9rem;">
                            Total: <?php echo $p['total']; ?>€
                        </p>
                        
                        <!-- Formulario para marcar como entregado -->
                        <form method="POST">
                            <input type="hidden" name="entregar_id" value="<?php echo $p['id']; ?>">
                            <button type="submit" class="button" style="background: var(--exito); width:100%; border:none; cursor:pointer;">
                                ✅ MARCAR ENTREGADO
                            </button>
                        </form>
                    </div>
                <?php endforeach; ?>
            <?php endif; ?>
        </div>
    </div>
</div>

</body>
</html>
```

---

En este proyecto usamos HTML y CSS, que son lenguajes de marcas. El HTML es el que estructura toda la página: define los títulos, párrafos, imágenes, formularios, botones… básicamente todo lo que se ve en la web. Por ejemplo, cada página del bar, como el catálogo o el carrito, está hecha con HTML, y dentro ponemos etiquetas como `<h1>`, `<p>`, `<div>`, `<form>`… para organizar la información.

El CSS es el que da estilo a todo eso: colores, tamaños, posiciones, bordes, sombras… gracias al CSS las páginas se ven bonitas y responsivas, y los botones y tarjetas de los productos no se ven planos ni aburridos. Por ejemplo, el logo del bar, los botones de “Añadir al pedido” o las alertas de cobro en el panel están todos estilizados con CSS.

Entonces, los lenguajes de marcas se usan para estructurar y presentar la información al usuario, mientras que PHP se encarga de la lógica del servidor. Básicamente, HTML y CSS son el “cuerpo y la ropa” (como diría Alfonso) de la web, y PHP es el cerebro que hace que todo funcione.
