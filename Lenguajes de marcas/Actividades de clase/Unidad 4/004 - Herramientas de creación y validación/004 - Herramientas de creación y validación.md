XML se puede usar como un estándar de intercambio de datos porque nos permite crear etiquetas personalizadas que describen exactamente el contenido, como `<puesto>` o `<skill>`. Sin embargo, para que este documento sea útil en entornos profesionales, necesitamos un XSD.

El XSD actúa como un "contrato" o gramática que define qué elementos son obligatorios y cómo deben estar anidados. En el desarrollo de aplicaciones de recursos humanos o portales de empleo, usamos estos esquemas para asegurar que todos los curriculums recibidos tengan el mismo formato y no falten datos críticos como el email o el nombre.

---

1. Documento de Currículum (`curriculum.xml`)

He adaptado mis datos a la estructura jerárquica del temario:

```
<?xml version="1.0" encoding="UTF-8"?>
<curriculum xmlns="https://ejemplo.com/curriculum" version="1.0">
    <datosPersonales>
        <nombre>Ana</nombre>
        <apellidos>Sánchez Suárez</apellidos>
        <nacionalidad>Española</nacionalidad>
        <email>ssanitax@gmail.com</email>
        <telefono>+34 722 28 96 95</telefono>
        <direccion>
            <ciudad>Valencia</ciudad>
            <pais>España</pais>
        </direccion>
    </datosPersonales>

    <perfilProfesional>
        ESTUDIANTE EN DESARROLLO DE APLICACIONES MULTIPLATAFORMA. 
        Cuento con habilidades para la resolución de problemas y actitud positiva.
    </perfilProfesional>

    <experienciaProfesional>
        <puesto>
            <titulo>ESPECIALISTA EN POSICIONAMIENTO SEO</titulo>
            <empresa>Kangar</empresa>
            <fechaInicio>Junio 2023</fechaInicio>
            <fechaFin>Septiembre 2023</fechaFin>
            <descripcion>Gestión de blogs, SEMrush, SEO y WordPress.</descripcion>
        </puesto>
        <puesto>
            <titulo>TÉCNICO MARKETING Y PUBLICIDAD</titulo>
            <empresa>CitySem</empresa>
            <fechaInicio>Mayo 2023</fechaInicio>
            <fechaFin>Junio 2023</fechaFin>
            <descripcion>Copywriting digital, arquitectura web y diseño de logotipos.</descripcion>
        </puesto>
    </experienciaProfesional>

    <formacionAcademica>
        <estudio>
            <titulo>Marketing y publicidad</titulo>
            <centro>IES Ángel Ganivet</centro>
            <localizacion>Granada</localizacion>
            <fechaInicio>Septiembre 2021</fechaInicio>
            <fechaFin>Junio 2023</fechaFin>
        </estudio>
        <estudio>
            <titulo>Desarrollo de aplicaciones multiplataforma</titulo>
            <centro>CEAC</centro>
            <localizacion>Valencia</localizacion>
            <fechaInicio>Septiembre 2025</fechaInicio>
            <fechaFin>Actualidad</fechaFin>
        </estudio>
    </formacionAcademica>

    <otrosDatos>
        <dato>Dispongo de carné de conducir y vehículo propio.</dato>
        <dato>Titulación de monitora de campamentos.</dato>
    </otrosDatos>
</curriculum>
```

2. Esquema de Validación (`curriculum.xsd`)

Definimos las reglas para que el XMl anterior sea válido:

```
<?xml version="1.0" encoding="UTF-8"?>
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema" 
           targetNamespace="https://ejemplo.com/curriculum"
           xmlns="https://ejemplo.com/curriculum"
           elementFormDefault="qualified">

    <xs:element name="curriculum">
        <xs:complexType>
            <xs:sequence>
                <xs:element name="datosPersonales">
                    <xs:complexType>
                        <xs:sequence>
                            <xs:element name="nombre" type="xs:string"/>
                            <xs:element name="apellidos" type="xs:string"/>
                            <xs:element name="nacionalidad" type="xs:string"/>
                            <xs:element name="email" type="xs:string"/>
                            <xs:element name="telefono" type="xs:string"/>
                            <xs:element name="direccion">
                                <xs:complexType>
                                    <xs:sequence>
                                        <xs:element name="ciudad" type="xs:string"/>
                                        <xs:element name="pais" type="xs:string"/>
                                    </xs:sequence>
                                </xs:complexType>
                            </xs:element>
                        </xs:sequence>
                    </xs:complexType>
                </xs:element>
                <xs:element name="perfilProfesional" type="xs:string"/>
                <xs:element name="experienciaProfesional">
                    <xs:complexType>
                        <xs:sequence>
                            <xs:element name="puesto" maxOccurs="unbounded">
                                <xs:complexType>
                                    <xs:sequence>
                                        <xs:element name="titulo" type="xs:string"/>
                                        <xs:element name="empresa" type="xs:string"/>
                                        <xs:element name="fechaInicio" type="xs:string"/>
                                        <xs:element name="fechaFin" type="xs:string"/>
                                        <xs:element name="descripcion" type="xs:string"/>
                                    </xs:sequence>
                                </xs:complexType>
                            </xs:element>
                        </xs:sequence>
                    </xs:complexType>
                </xs:element>
                <xs:element name="formacionAcademica">
                    <xs:complexType>
                        <xs:sequence>
                            <xs:element name="estudio" maxOccurs="unbounded">
                                <xs:complexType>
                                    <xs:sequence>
                                        <xs:element name="titulo" type="xs:string"/>
                                        <xs:element name="centro" type="xs:string"/>
                                        <xs:element name="localizacion" type="xs:string"/>
                                        <xs:element name="fechaInicio" type="xs:string"/>
                                        <xs:element name="fechaFin" type="xs:string"/>
                                    </xs:sequence>
                                </xs:complexType>
                            </xs:element>
                        </xs:sequence>
                    </xs:complexType>
                </xs:element>
                <xs:element name="otrosDatos">
                    <xs:complexType>
                        <xs:sequence>
                            <xs:element name="dato" type="xs:string" maxOccurs="unbounded"/>
                        </xs:sequence>
                    </xs:complexType>
                </xs:element>
            </xs:sequence>
            <xs:attribute name="version" type="xs:string" use="required"/>
        </xs:complexType>
    </xs:element>
</xs:schema>
```

---

El uso de esquemas XSD es fundamental para transformar documentos XML en formatos de datos robustos y fiables. Al definir reglas de cardinalidad (como permitir múltiples etiquetas `<puesto>` o `<dato>`), nosotros garantizamos que el sistema pueda escalar y adaptarse a perfiles con diferente nivel de experiencia sin perder la validez estructural.

Este ejercicio nos permite entender la importancia de la validación automática, la cual ahorra tiempo de depuración y evita errores en la lógica de negocio al integrar estos datos con otros lenguajes de programación.
