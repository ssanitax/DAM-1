Utilizamos las clases como "plantillas" o planos que definen cómo debe ser un objeto. En este ejercicio, la clase `Cena` nos permite agrupar tanto las características de la reunión (sus propiedades) como las acciones que podemos realizar en ella (sus métodos).

La importancia de este enfoque reside en la encapsulación: nosotros guardamos toda la lógica relacionada con la cena en un solo lugar, lo que hace que nuestro código sea mucho más organizado, fácil de leer y reutilizable en el futuro.

---

```
# definimos la clase siguiendo la estructura de POO
class Cena:
    # El constructor inicializa las propiedades de nuestra cena
    def __init__(self, nuevos_amigos, nueva_comida, nuevo_lugar):
        self.amigos_invitados = nuevos_amigos
        self.tipo_comida = nueva_comida
        self.lugar = nuevo_lugar

    # Método para simular el proceso de organización
    def organizar_cena(self):
        print(f"--- ORGANIZANDO LA CENA EN {self.lugar.upper()} ---")
        print(f"1. Enviando invitaciones a: {self.amigos_invitados}")
        print(f"2. El menú elegido para hoy es: {self.tipo_comida}")
        print(f"3. Preparando la mesa en {self.lugar}...")
        print("¡Todo listo! Que disfrutéis de la cena.")

# --- EJEMPLO DE USO ---

# instanciamos el objeto (creamos una cena concreta)
mi_cena = Cena("Ana, Jose y Carlos", "Pizza artesana", "la terraza")

# llamamos al método para ver el proceso en pantalla
mi_cena.organizar_cena()
```

---

Al ejecutar este código, podemos ver cómo los datos que hemos guardado en el objeto "cobran vida" a través del método. Si quisiéramos organizar una cena diferente (por ejemplo, de Sushi en el salón), no tendríamos que volver a escribir toda la lógica, simplemente crearíamos un nuevo objeto de la clase `Cena` con otros parámetros.
