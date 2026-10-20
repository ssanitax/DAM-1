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
