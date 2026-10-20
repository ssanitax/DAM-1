La validación automática es útil para asegurar la integridad de los datos antes de procesarlos en nuestras aplicaciones. Mientras que en ejercicios anteriores validábamos de forma manual o con herramientas externas, el uso de un script en Python nos permite integrar esta validación dentro de flujos de trabajo profesionales, como la recepción de pedidos en una tienda online o el registro en un sistema escolar.

La biblioteca `lxml` es el estándar en Python para estas tareas, ya que permite cargar documentos XML y esquemas XSD de forma eficiente, transformándolos en objetos que el ordenador puede comparar lógicamente para emitir un veredicto de validez.

---

El código será así:

```
from lxml import etree

# 1. Cargamos los documentos desde el disco
xml_doc = etree.parse("001-documento de referencia.xml")
xsd_doc = etree.parse("002-esquema.xsd")

# 2. Creamos el objeto validador basado en el esquema XSD
schema = etree.XMLSchema(xsd_doc)

# 3. Validamos el XML y mostramos el resultado
# Imprimirá True si cumple las reglas o False si no lo hace.
resultado = schema.validate(xml_doc)
print(f"¿Es el documento válido?: {resultado}")

# Opcional: Podemos ver los errores si el resultado es False
if not resultado:
    print(schema.error_log)
```

---

La asociación y la validación de documetos es el último paso necesario para garantizar que nuestros lenguajes de marcas funcionen correctamente en un entorno real. Al usar Python para esta tarea, pasamos de crear documentos estáticos a gestionar datos dinámicos y seguros, sentando las bases para conectar XML con otros módulos como Bases de Datos o Programación en el lado del servidor.
