Utilizamos XML para representar información plana de manera jerárquica. La importancia de este lenguaje reside ne su capacidad para ser leído tanto por personas como por máquinas, basándose en reglas estrictas de notación y normativa.

Para que podamos considerar un documento XML como bien hecho, debemos respetar 3 reglas:

- Etiqueta raíz: Todo documento debe tener un único elemento que envuelva al resto del contenido.
- Sensibilidad a Mayúsculas (Case-sensitive): Debemos escribir las etiquetas de apertura y cierre de forma idéntica. Cuidado con las mayúsculas y minúsculas.

- Estructura jerárquica: Las etiquetas deben estar correctamente anidadas, creando una relacion de padres e hijos.

---

varios-teléfonos.xml

```
<?xml version="1.0" encoding="UTF-8"?>
<persona>
  <nombre>Ana</nombre>
  <apellidos>Sánchez Suárez</apellidos>
  <telefonos>
    <telefono>123456789</telefono>
    <telefono>234567891</telefono>
    <telefono>345678912</telefono>
  </telefonos>
</persona>
```

debe-haber-una-etiqueta-raiz.xml

```
<?xml version="1.0" encoding="UTF-8"?>
<persona>
  <nombre>Ana</nombre>
  <apellidos>Sánchez Suárez</apellidos>
</persona>
```

---

Hemos comprobado que dominar la sintaxis de XML es el primer paso para trabajar con formatos de datos intercambiables. Al practicar con etiquetas personalizadas y estructuras jerárquicas, sentamos las bases para la definición de esquemas más complejos que se utilizan ampliamente en sistemas empresariales y servicios web modernos.
