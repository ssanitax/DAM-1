Los esquemas XSD sirven para definir el "vocabulario" y la "gramática" de un documento XML. Mientras que el XML se encarga de transportar los datos de forma jerárquica, el XSD actúa como un contrato que especifica qué elementos son obligatorios, cuántas veces pueden aparecer y qué tipo de datos deben contener (texto, números, etc.).

En el desarrollo de software, la importancia de esta tecnología reside en la integridad de los datos: antes de que nosotros guardemos información en una base de datos o la procesemos en una aplicación, el esquema asegura que no falte ningún campo crítico, como el nombre o el teléfono de un contacto.

---

001 - documento de referencia.xml

```
<?xml version="1.0" encoding="UTF-8"?>
<persona>
  <nombre>Ana</nombre>
  <apellidos>Sánchez Suárez</apellidos>
  <telefonos>
    <telefono>504934345</telefono>
    <telefono>059685321</telefono>
  </telefonos>
</persona>
```

002 - esquema.xsd

```
<?xml version="1.0" encoding="UTF-8"?>
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema" elementFormDefault="qualified">

  <xs:element name="persona">
    <xs:complexType>
      <xs:sequence>
        <xs:element name="nombre" type="xs:string"/>
        <xs:element name="apellidos" type="xs:string"/>
        <xs:element name="telefonos">
          <xs:complexType>
            <xs:sequence>
              <xs:element name="telefono" type="xs:string" minOccurs="1" maxOccurs="unbounded"/>
            </xs:sequence>
          </xs:complexType>
        </xs:element>
      </xs:sequence>
    </xs:complexType>
  </xs:element>

</xs:schema>
```

---

El uso de esquemas XSD es fundamental para transformar el XML en un formato de intercambio de datos robusto y fiable. Al practicar la definición de cardinalidades (como el número de teléfonos), nosotros sentamos las bases para la creación de servicios web modernos donde la validación automática ahorra tiempo de depuración y evita errores en la lógica de negocio.
