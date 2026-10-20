## Bar Bara - Programación

Este proyecto consiste en el desarrollo de un sistema de gestión para un establecimiento de hostelería (Bar Bara), diseñado con una arquitectura que separa la lógica del servidor (Backend) de la interfaz de usuario (Frontend).

El objetivo es digitalizar el ciclo de servicio, desde que el cliente se registra hasta que solicita el pago en mesa.

---

**Arquitectura de la Web**

```
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
        ├── img/
        │   └── coctel.webp
        └── inc/
            ├── cabecera.php
            └── piedepagina.php
```

---

Voy a explicar la parte de programación del proyecto Bar Bara, y lo haré archivo por archivo, centrándome sobre todo en aquellos archivos que tienen lógica de programación.

No todos los archivos del proyecto tienen el mismo peso a nivel de programación. Hay algunos que solo contienen HTML o sirven para reutilizar código visual, por lo que los mencionaré de forma más breve. He decidido centrarme más en los archivos donde realmente se ve la lógica, ya que son los que mejor reflejan lo que he aprendido en la asignatura.

Cuando empecé el curso en septiembre no sabía prácticamente nada de programación, y ahora soy capaz de hacer una aplicación web que funciona con PHP y base de datos. Voy a explicar qué hace cada archivo, qué código he escrito y qué he aprendido en el proceso.

---

## BACKEND

### back/inc/conexion_bd.php

Este archivo sirve para conectarse a la base de datos. Es uno de los más importantes porque todos los demás lo usan.

```
<?php
$host = 'localhost';
$db   = 'Bar_Bara';
$user = 'admin_bara';
$pass = 'BarBara_2025$';
$charset = 'utf8mb4';

try {
     $pdo = new PDO("mysql:host=$host;dbname=$db;charset=$charset", $user, $pass, [
         PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
         PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC
     ]);
} catch (PDOException $e) {
     die("Error de conexión: " . $e->getMessage());
}

header("Access-Control-Allow-Origin: *");
```

Aquí he aprendido a crear una conexión con PDO, a usar excepciones y a no repetir código usando `require_once`.

---

### back/controladores/ProductoControlador.php

En este archivo tengo una clase que se encarga de los productos.

```
<?php

class ProductoControlador {
    private $db;

    public function __construct($conexion) {
        $this->db = $conexion;
    }

    public function listarTodo() {
        // Obtenemos todos los campos: nombre, precio, descripción, categoria e imagen
        $sql = "SELECT * FROM producto";
        $stmt = $this->db->query($sql);
        return $stmt->fetchAll();
    }

    public function obtenerPorId($id) {
        $sql = "SELECT * FROM producto WHERE id = ?";
        $stmt = $this->db->prepare($sql);
        $stmt->execute([$id]);
        return $stmt->fetch();
    }
}
```

Aquí he aprendido a usar clases, constructores y métodos, y a separar la lógica del resto del código.

---

### back/controladores/UsuarioControlador.php

Este archivo se usa para el login de usuarios.

```
<?php

class UsuarioControlador {
    private $db;

    public function __construct($conexion) {
        $this->db = $conexion;
    }

    public function registrar($datos) {
        $passwordSegura = password_hash($datos['contrasea'], PASSWORD_BCRYPT);
        
        $sql = "INSERT INTO usuario (nombre_usuario, apellidos, correo, contrasea) VALUES (?, ?, ?, ?)";
        $stmt = $this->db->prepare($sql);
        return $stmt->execute([
            $datos['nombre_usuario'], 
            $datos['apellidos'], 
            $datos['correo'], 
            $passwordSegura
        ]);
    }

    public function login($correo, $password) {
        $sql = "SELECT * FROM usuario WHERE correo = ?";
        $stmt = $this->db->prepare($sql);
        $stmt->execute([$correo]);
        $usuario = $stmt->fetch();

        if ($usuario && password_verify($password, $usuario['contrasea'])) {
            return $usuario; // Login exitoso
        }
        return false;
    }
}
```

He aprendido a comprobar contraseñas cifradas, a validar datos y a controlar el acceso de los usuarios.

---

## back/controladores/PedidoControlador.php

Este es el archivo más importante del proyecto porque gestiona los pedidos.

```
<?php

class PedidoControlador {
    private $db;

    public function __construct($conexion) {
        $this->db = $conexion;
    }

    public function crearNuevoPedido($datos) {
        // El pedido nace con pedir_cuenta = 'NO' (Pendiente de servir)
        $sqlPedido = "INSERT INTO pedido (usuario_id, numero_mesa, fecha, hora, total, pedir_cuenta) 
                      VALUES (?, ?, CURDATE(), CURTIME(), ?, 'NO')";
        $stmt = $this->db->prepare($sqlPedido);
        $stmt->execute([
            $datos['usuario_id'], 
            $datos['numero_mesa'], 
            $datos['total']
        ]);
        $idPedido = $this->db->lastInsertId();

        foreach ($datos['productos'] as $item) {
            $sqlContenido = "INSERT INTO contenido_pedido (pedido_id, producto_id, cantidad, subtotal) 
                             VALUES (?, ?, ?, ?)";
            $stmtDetalle = $this->db->prepare($sqlContenido);
            $stmtDetalle->execute([
                $idPedido, 
                $item['producto_id'], 
                $item['cantidad'], 
                $item['subtotal']
            ]);
        }
        return $idPedido;
    }

    public function marcarComoEntregado($idPedido) {
        $sql = "UPDATE pedido 
            SET pedir_cuenta = CASE 
                WHEN pedir_cuenta = 'SI' THEN 'SI_ENTREGADO' 
                ELSE 'ENTREGADO' 
            END 
            WHERE id = ?";
    return $this->db->prepare($sql)->execute([$idPedido]);
    }

    public function solicitarCuenta($idPedido) {
        $sql = "UPDATE pedido SET pedir_cuenta = 'SI' WHERE id = ?";
        return $this->db->prepare($sql)->execute([$idPedido]);
    }

    public function marcarComoPagado($idPedido) {
        $sql = "UPDATE pedido SET pedir_cuenta = 'PAGADO' WHERE id = ?";
        return $this->db->prepare($sql)->execute([$idPedido]);
    }
}
```

Aquí he aprendido a trabajar con arrays, a insertar datos relacionados y a controlar estados de los pedidos.

---

### back/index.php

Este archivo es el panel de control del bar. Desde aquí se verán los pedidos que hay que entregar y cuando algún cliente pida la cuenta.

```
<?php
require_once 'inc/conexion_bd.php';
require_once 'controladores/PedidoControlador.php';
require_once 'controladores/ProductoControlador.php';

$pedidoCtrl = new PedidoControlador($pdo);
$productoCtrl = new ProductoControlador($pdo);

if (isset($_POST['entregar_id'])) {
    $pedidoCtrl->marcarComoEntregado($_POST['entregar_id']);
}

if (isset($_POST['cobrar_id'])) {
    $idPedido = $_POST['cobrar_id'];

    $sql = "UPDATE pedido SET pedir_cuenta = 'PAGADO' WHERE id = ?";
    $stmt = $pdo->prepare($sql);
    $stmt->execute([$idPedido]);
}

try {
    $totalProductos = count($productoCtrl->listarTodo());
    
    $pendientes = $pdo->query("SELECT * FROM pedido WHERE pedir_cuenta IN ('NO', 'SI') ORDER BY hora ASC")->fetchAll();    
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
    <link rel="stylesheet" href="css/estilo.css">
    <meta http-equiv="refresh" content="30">
    <style>
        .seccion { margin-bottom: 40px; }
        .titulo-seccion { padding: 10px; border-radius: 8px; margin-bottom: 20px; color: white; }
    </style>
</head>
<body>
    <nav>
        <div class="logo">🍴 BAR BARA - PANEL DE CONTROL</div>
        <div class="header-status">
            <code>PRODUCTOS: <?php echo $totalProductos; ?></code>
        </div>
    </nav>

    <div class="container">
        
        <div class="seccion">
            <h2 class="titulo-seccion" style="background: var(--error);">🔔 ALERTAS DE COBRO (<?php echo $conteoAlertas; ?>)</h2>
            <div class="grid-productos">
                <?php if (empty($alertas)): ?>
                    <div class="card"><h3>No hay mesas solicitando la cuenta.</h3></div>
                <?php else: ?>
                    <?php foreach($alertas as $a): ?>
                        <div class="card" style="border-left: 10px solid var(--error); text-align: left;"> 
                            <h2 style="margin:0">MESA <?php echo $a['numero_mesa']; ?></h2>
                            <p><strong>Total a cobrar: <?php echo $a['total']; ?>€</strong></p>
                            <p>Hora solicitud: <?php echo $a['hora']; ?></p>
                            
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

        <div class="seccion">
            <h2 class="titulo-seccion" style="background: var(--primario);">📥 COMANDAS POR SERVIR</h2>
            <div class="grid-productos">
                <?php if (empty($pendientes)): ?>
                    <div class="card"><h3>Cero comandas pendientes.</h3></div>
                <?php else: ?>
                   <?php foreach ($pendientes as $p): ?>
    <div class="card" style="border-left: 10px solid var(--primario); text-align: left;"> 
        
        <div style="display:flex; justify-content:space-between; align-items:center;">
            <h2 style="margin:0">MESA <?php echo $p['numero_mesa']; ?></h2>
            <span style="background:#eee; padding:5px 10px; border-radius:5px; font-weight:bold;">
                <?php echo date('H:i', strtotime($p['hora'])); ?>
            </span>
        </div>

        <hr style="margin: 10px 0; border: 0; border-top: 1px dashed #ccc;">

        <ul style="padding-left: 20px; margin: 10px 0;">
            <?php 
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
        <p style="text-align: right; color: #666; font-size: 0.9rem;">Total: <?php echo $p['total']; ?>€</p>
        
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

He aprendido a manejar formularios, condiciones y acciones desde el backend.

---

## FRONTEND

### front/catalogo.php

En este archivo se muestran los productos.

```
<?php 
session_start();
require_once '../back/inc/conexion_bd.php'; 
include 'inc/cabecera.php'; 

$res_cat = $pdo->query("SELECT DISTINCT categoria FROM producto ORDER BY categoria");
$categorias = $res_cat->fetchAll(PDO::FETCH_COLUMN);

$stmt = $pdo->query("SELECT * FROM producto ORDER BY categoria, nombre_producto");
?>

<style>
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

    .cat-link {
        background: #153e5c; 
        color: white;
        padding: 10px 20px;
        border-radius: 20px;
        text-decoration: none;
        font-weight: bold;
    }

    .cat-link:hover { background: #eaa833; }

    .catalogo-grid { 
        display: grid; 
        grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); 
        gap: 25px; 
    }

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

    .producto-img { width: 100%; height: 200px; object-fit: cover; border-radius: 8px; }

    .cantidad-control { display: flex; align-items: center; justify-content: center; gap: 10px; margin-bottom: 15px; }

    .btn-qty { background: #153e5c; color: white; border: none; width: 32px; height: 32px; border-radius: 50%; cursor: pointer; }

    .input-qty { width: 45px; text-align: center; border: 1px solid #ddd; border-radius: 5px; font-weight: bold; }

    .btn-add { background: #27ae60; color: white; border: none; padding: 12px; border-radius: 5px; cursor: pointer; font-weight: bold; }

    .categoria-titulo { grid-column: 1 / -1; text-align: left; margin-top: 50px; border-bottom: 3px solid #eaa833; color: #153e5c; }
</style>

<div class="categorias-nav">
    <?php foreach ($categorias as $c): ?>
        <a href="#<?php echo urlencode($c); ?>" class="cat-link"><?php echo htmlspecialchars($c); ?></a>
    <?php endforeach; ?>
</div>

<div class="catalogo-grid">
    <?php
    $actual_cat = "";
    while ($row = $stmt->fetch(PDO::FETCH_ASSOC)):
        if ($actual_cat != $row['categoria']):
            $actual_cat = $row['categoria']; ?>
            <h2 class="categoria-titulo" id="<?php echo urlencode($actual_cat); ?>"><?php echo htmlspecialchars($actual_cat); ?></h2>
        <?php endif; ?>
        
        <div class="producto-card">
            <div>
                <img src="img/<?php echo $row['imagen']; ?>" class="producto-img">
                <h3 style="margin: 15px 0 5px 0;"><?php echo htmlspecialchars($row['nombre_producto']); ?></h3>
            </div>

            <div style="margin-top: 20px;">
                <p style="font-size: 1.4em; color: #153e5c; margin-bottom: 15px;"><strong><?php echo number_format($row['precio'], 2); ?>€</strong></p>
                
                <form action="carrito.php" method="POST">
                    <input type="hidden" name="id" value="<?php echo $row['id']; ?>">
                    <div class="cantidad-control">
                        <button type="button" class="btn-qty" onclick="this.nextElementSibling.stepDown()">-</button>
                        <input type="number" name="cantidad" class="input-qty" value="1" min="1" readonly>
                        <button type="button" class="btn-qty" onclick="this.previousElementSibling.stepUp()">+</button>
                    </div>
                    <button type="submit" name="add" class="btn-add">Añadir al pedido</button>
                </form>
            </div>
        </div>
    <?php endwhile; ?>
</div>

<?php include 'inc/piedepagina.php'; ?>
```

Aquí he aprendido a recorrer resultados y a mostrar datos usando PHP.

---

## front/carrito.php

Este archivo gestiona el carrito usando sesiones.

```
<?php
session_start();
include '../back/inc/conexion_bd.php';

if (isset($_POST['add'])) {
    $id_producto = $_POST['id'];
    $cantidad = isset($_POST['cantidad']) ? (int)$_POST['cantidad'] : 1;
    $stmt = $pdo->prepare("SELECT * FROM producto WHERE id = ?");
    $stmt->execute(array($id_producto));
    $producto_bd = $stmt->fetch(PDO::FETCH_ASSOC);

    if ($producto_bd) {
        if (!isset($_SESSION['carrito'])) { $_SESSION['carrito'] = array(); }
        $ya_existe = false;
        foreach ($_SESSION['carrito'] as $indice => $item) {
            if ($item['id'] == $id_producto) {
                $_SESSION['carrito'][$indice]['cantidad'] = $_SESSION['carrito'][$indice]['cantidad'] + $cantidad;
                $ya_existe = true; break;
            }
        }
        if (!$ya_existe) {
            $_SESSION['carrito'][] = array(
                'id' => $producto_bd['id'],
                'nombre' => $producto_bd['nombre_producto'],
                'precio' => $producto_bd['precio'],
                'imagen' => $producto_bd['imagen'], // Aseguramos que se guarde la imagen 
                'cantidad' => $cantidad
            );
        }
    }
    header("Location: catalogo.php");
    exit;
}

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

$total = 0;
if (isset($_SESSION['carrito'])) {
    foreach ($_SESSION['carrito'] as $item) {
        $total = $total + ($item['precio'] * $item['cantidad']);
    }
}

include 'inc/cabecera.php';
?>

<link rel="stylesheet" href="css/estilo.css">
<style>
    .comanda-container { max-width: 900px; margin: 0 auto; padding: 20px; }
    .tabla-bar-bara { width: 100%; border-collapse: separate; border-spacing: 0 15px; }
    .fila-producto { background: white; box-shadow: 0 4px 12px rgba(0,0,0,0.1); border-radius: 15px; overflow: hidden; }
    .fila-producto td { padding: 15px; vertical-align: middle; }
    
    .img-carrito { width: 80px; height: 80px; object-fit: cover; border-radius: 10px; border: 2px solid #eee; } /*  */

    .selector-cantidad { display: flex; align-items: center; background: #f1f1f1; padding: 5px; border-radius: 30px; width: fit-content; }
    .btn-ajuste { background: #153e5c; color: white; border: none; width: 30px; height: 30px; border-radius: 50%; cursor: pointer; font-weight: bold; }
    
    .total-card { background: #ffffff; padding: 25px; border-radius: 15px; border: 3px solid #eaa833; display: flex; justify-content: space-between; align-items: center; margin-top: 20px; }

    @media (max-width: 600px) {
        .tabla-bar-bara, .tabla-bar-bara tbody, .tabla-bar-bara tr, .tabla-bar-bara td { display: block; width: 100%; }
        .fila-producto { margin-bottom: 20px; text-align: center; }
        .fila-producto td { padding: 10px; }
        .selector-cantidad { margin: 10px auto; }
        .total-card { flex-direction: column; text-align: center; gap: 20px; }
        .total-card form { flex-direction: column; align-items: center; width: 100%; }
    }
</style>

<div class="comanda-container">
    <h2 style="color: #153e5c; text-align: center;">🛒 Nuestra Comanda</h2>

    <?php if (!empty($_SESSION['carrito'])): ?>
        <table class="tabla-bar-bara">
            <tbody>
                <?php foreach ($_SESSION['carrito'] as $p): ?>
                    <tr class="fila-producto">
                        <td width="100">
                            <img src="img/<?php echo $p['imagen']; ?>" class="img-carrito" alt="Foto">
                        </td>
                        <td>
                            <strong style="font-size: 1.1rem;"><?php echo htmlspecialchars($p['nombre']); ?></strong><br>
                            <span style="color: #666;"><?php echo number_format($p['precio'], 2); ?>€</span>
                        </td>
                        <td align="center">
                            <form action="carrito.php" method="POST" class="selector-cantidad">
                                <input type="hidden" name="id" value="<?php echo $p['id']; ?>">
                                <button type="submit" name="actualizar_cantidad" class="btn-ajuste" onclick="this.nextElementSibling.stepDown()">-</button>
                                <input type="number" name="cantidad" value="<?php echo $p['cantidad']; ?>" min="1" readonly style="width: 35px; text-align: center; border: none; background: transparent; font-weight: bold;">
                                <button type="submit" name="actualizar_cantidad" class="btn-ajuste" onclick="this.previousElementSibling.stepUp()">+</button>
                            </form>
                        </td>
                        <td>
                            <span style="font-weight: 800; font-size: 1.2rem; color: #c93b2b;">
                                <?php echo number_format($p['precio'] * $p['cantidad'], 2); ?>€
                            </span>
                        </td>
                        <td align="right">
                            <form action="carrito.php" method="POST" style="margin:0;">
                                <input type="hidden" name="id_eliminar" value="<?php echo $p['id']; ?>">
                                <button type="submit" name="btn_eliminar" style="background:none; border:none; cursor:pointer; font-size: 1.3rem;" title="Eliminar">Eliminar 🗑️</button>
                            </form>
                        </td>
                    </tr>
                <?php endforeach; ?>
            </tbody>
        </table>

        <div class="total-card">
            <div>
                <span style="color: #666; font-size: 0.8rem; text-transform: uppercase;">Total Mesa</span>
                <h3 style="margin:0; font-size: 2.2rem; color: #153e5c;"><?php echo number_format($total, 2); ?>€</h3>
            </div>
            
            <form action="procesar_pedido.php" method="POST" style="display: flex; gap: 15px; align-items: flex-end;">
                <div>
                    <label style="display:block; font-weight: bold; margin-bottom: 5px; color: #153e5c;">Nº MESA</label>
                    <input type="number" name="numero_mesa" required placeholder="Ex: 5" style="padding: 12px; border: 1px solid #ccc; border-radius: 8px; width: 80px;">
                </div>
                <input type="hidden" name="total_pagar" value="<?php echo $total; ?>">
                <button type="submit" name="confirmar_pedido" class="btn-hero btn-carrito-hero" style="border:none; cursor:pointer; padding: 15px 25px;">
                    PEDIR AHORA 🚀
                </button>
            </form>
        </div>

    <?php else: ?>
        <div class="empty-cart-container">
            <img src="img/logo_triste.png" style="width: 150px; margin-bottom: 20px;">
            <h2 class="empty-title">¡Vuestra mesa está vacía!</h2>
            <a href="catalogo.php" class="btn-carta-vacio">🍔 Ver la Carta</a>
        </div>
    <?php endif; ?>
</div>

<?php include 'inc/piedepagina.php'; ?>
```

He aprendido qué son las sesiones, cómo guardar datos temporales y cómo calcular totales.

---

### front/procesar_pedido.php

Este archivo recoge los datos del pedido y los envía al backend.

He aprendido a usar `$_POST`, a comprobar datos y a vaciar el carrito.

```
<?php
session_start();
require_once '../back/inc/conexion_bd.php';
require_once '../back/controladores/PedidoControlador.php';

if (!isset($_SESSION['user_id'])) {
    header("Location: registro.php");
    exit;
}

if (isset($_POST['confirmar_pedido']) && !empty($_SESSION['carrito'])) {
    $pedidoCtrl = new PedidoControlador($pdo);

    $datosPedido = [
        'usuario_id'  => $_SESSION['user_id'],
        'numero_mesa' => $_POST['numero_mesa'],
        'total'       => $_POST['total_pagar'],
        'productos'   => []
    ];

    foreach ($_SESSION['carrito'] as $item) {
        $datosPedido['productos'][] = [
            'producto_id' => $item['id'],
            'cantidad'    => $item['cantidad'],
            'subtotal'    => $item['precio'] * $item['cantidad']
        ];
    }

    try {
        $idPedido = $pedidoCtrl->crearNuevoPedido($datosPedido);
        unset($_SESSION['carrito']);
        header("Location: finalizacion.php?finalizado=" . $idPedido);
        exit;
    } catch (Exception $e) {
        die("Error al guardar el pedido: " . $e->getMessage());
    }
} else {
    header("Location: catalogo.php");
    exit;
}
```

---

### front/historial.php

Aquí el usuario puede ver sus pedidos y pedir la cuenta.

```
<?php 
session_start();
require_once '../back/inc/conexion_bd.php';
include 'inc/cabecera.php';

if (!isset($_SESSION['user_id'])) {
    header("Location: login.php");
    exit;
}

$user_id = $_SESSION['user_id'];
$mensaje = "";

if (isset($_POST['pedir_cuenta_total'])) {
    $sql = "UPDATE pedido 
            SET pedir_cuenta = CASE 
                WHEN pedir_cuenta = 'ENTREGADO' THEN 'SI_ENTREGADO' 
                ELSE 'SI' 
            END 
            WHERE usuario_id = ? AND pedir_cuenta != 'PAGADO'";
            
    $stmt = $pdo->prepare($sql);
    $stmt->execute(array($user_id));
    
    $mensaje = "🔔 ¡Aviso enviado! El camarero traerá la cuenta en breve.";
}

$query = "SELECT p.id as pedido_id, pr.nombre_producto, cp.cantidad, cp.subtotal, p.pedir_cuenta
          FROM pedido p
          JOIN contenido_pedido cp ON p.id = cp.pedido_id
          JOIN producto pr ON cp.producto_id = pr.id
          WHERE p.usuario_id = ? AND p.pedir_cuenta != 'PAGADO'
          ORDER BY p.id DESC";
$stmt = $pdo->prepare($query);
$stmt->execute(array($user_id));
$items = $stmt->fetchAll();

$total_mesa = 0;
?>

<div class="container" style="max-width: 800px; margin: 0 auto; padding: 20px;">
    <h2 style="color: #153e5c; text-align: center; margin-bottom: 30px;">Resumen de vuestra mesa 📝</h2>

    <?php if ($mensaje): ?>
        <div style="background: #27ae60; color: white; padding: 15px; border-radius: 8px; margin-bottom: 20px; text-align: center;">
            <?php echo $mensaje; ?>
        </div>
    <?php endif; ?>

    <?php if (empty($items)): ?>
        <div style="background: white; padding: 60px 20px; border-radius: 20px; box-shadow: 0 10px 25px rgba(0,0,0,0.1); text-align: center; border: 2px dashed #ccc;">
            <div style="font-size: 5rem; margin-bottom: 20px;">🍽️</div>
            <h3 style="color: #153e5c; font-size: 1.8rem; margin-bottom: 10px;">¡Vuestra mesa está lista!</h3>
            <p style="color: #666; font-size: 1.1rem; margin-bottom: 30px;">Todavía no habéis marchado ningún plato. ¿Empezamos con unas rondas?</p>
            
            <a href="catalogo.php" class="btn-hero btn-carta" style="display: inline-block; text-decoration: none; padding: 15px 40px; font-size: 1.2rem;">
                📖 Ver la Carta
            </a>
        </div>
    <?php else: ?>
        <div style="background: white; padding: 25px; border-radius: 15px; box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
            <table style="width: 100%; border-collapse: collapse;">
                <thead>
                    <tr style="border-bottom: 2px solid #eee;">
                        <th style="text-align: left; padding: 10px; color: #153e5c;">Producto</th>
                        <th style="text-align: center; padding: 10px; color: #153e5c;">Cant.</th>
                        <th style="text-align: right; padding: 10px; color: #153e5c;">Subtotal</th>
                    </tr>
                </thead>
                <tbody>
                    <?php foreach ($items as $item): 
                        $total_mesa = $total_mesa + $item['subtotal'];
                    ?>
                        <tr style="border-bottom: 1px solid #f9f9f9;">
                            <td style="padding: 15px;"><?php echo htmlspecialchars($item['nombre_producto']); ?></td>
                            <td style="text-align: center; padding: 15px; font-weight: bold;"><?php echo $item['cantidad']; ?></td>
                            <td style="text-align: right; padding: 15px;"><?php echo number_format($item['subtotal'], 2); ?>€</td>
                        </tr>
                    <?php endforeach; ?>
                </tbody>
                <tfoot>
                    <tr style="font-size: 1.6rem; font-weight: bold; color: #c93b2b;">
                        <td colspan="2" style="padding: 25px 10px;">TOTAL ACUMULADO:</td>
                        <td style="text-align: right; padding: 25px 10px;"><?php echo number_format($total_mesa, 2); ?>€</td>
                    </tr>
                </tfoot>
            </table>

            <form method="POST" style="margin-top: 20px;">
                <button type="submit" name="pedir_cuenta_total" 
                        class="btn-hero btn-carrito-hero" 
                        style="width: 100%; border: none; cursor: pointer; padding: 20px; font-size: 1.2rem;">
                    🔔 PEDIR LA CUENTA FINAL
                </button>
            </form>
        </div>
        
        <div style="text-align: center; margin-top: 30px;">
            <a href="catalogo.php" style="color: #153e5c; font-weight: bold; text-decoration: underline;">¿Algo más? Seguir pidiendo</a>
        </div>
    <?php endif; ?>
</div>

<?php include 'inc/piedepagina.php'; ?>
```

He aprendido a actualizar datos y a usar estados para controlar el flujo del pedido.

---

## Conclusión

Este proyecto me ha servido para poner en práctica todo lo que he aprendido en programación durante el curso, viéndolo aplicado en un proyecto real y completo se ve  todo mucho más claro, ya que a veces en clase, viendo la teoría explicada, te puedes llegar a preguntar para qué se podría usar x cosa, y en este proyecto, he visto que realmente sí que es todo importante. También me ha gustado descubrir cómo un problema se puede solucionar de distintas formas, ya que trabajar en equipo, hace que veas que la gente tiene formas de pensar diferentes y válidas, llegando los dos juntos a una solución que no se hubiese llegado por separado.

Mi compañero de trabajo y yo decidimos hacer el proyecto en PHP porque, aunque en clase habíamos trabajado bastante con Python, queríamos aprender a manejar PHP a un nivel parecido. Pensamos que era una buena oportunidad para ampliar nuestros conocimientos y no quedarnos solo en un lenguaje de programación.

Gracias a este proyecto ahora entiendo mejor cómo funciona una aplicación web por dentro, cómo se organiza el código y cómo la programación conecta la base de datos con lo que ve el usuario. Aún me queda mucho por aprender, pero este trabajo refleja bastante la evolución que he tenido desde que empecé el curso.
