Utilizamos el archivo `index.php` como el corazón de nuestra estructura modular. En el desarrollo de aplicaciones web, la importancia de este archivo reside en que aplica la lógica de unión de bloques. Al igual que en `contacto.php`, nosotros no escribimos el código del menú ni del pie de página aquí; simplemente los "llamamos" para que el servidor los ensamble antes de enviar el resultado al navegador.

---

index.php

```
<?php 
   include "bloques/cabecera.php"; 
?>

<p>Aqui solo pongo el contenido de la pagina principal</p>

<?php 
    include "bloques/pie.php"; 
?>
```

contacto.php

```
<?php 
    include "bloques/cabecera.php"; 
?>

<p>Aqui solo pongo el contenido de la pagina de contacto</p>

<?php 
    include "bloques/pie.php"; 
?>
```

cabecera.php

```
<?php 
    include "bloques/cabecera.php"; 
?>

<p>Aqui solo pongo el contenido de la pagina de contacto</p>

<?php 
    include "bloques/pie.php"; 
?>
```

pie.php

```
</main>
    <footer>
      (c) 2025 Ana Sánchez Suárez
    </footer>
  </body>
</html>
```

---

Hemos comprobado que, una vez creados los bloques de cabecera y pie, desarrollar la página principal es una tarea sumamente sencilla y rápida. Esta metodología de trabajo es la que nosotros seguiremos para cualquier otra página que queramos añadir, como sobremi.php, garantizando que si Jose Vicente decide cambiar su nombre o el año del copyright, nosotros solo tengamos que hacerlo en un lugar.

Al dominar esta estructura, estamos preparados para crear portales web escalables donde el diseño y el contenido están perfectamente separados.
