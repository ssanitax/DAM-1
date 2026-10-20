import sqlite3

def crear_tabla():
    conn = sqlite3.connect('clientes.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS clientes
                 (id INTEGER PRIMARY KEY, nombre TEXT, email TEXT, telefono TEXT)''')
    conn.commit()
    conn.close()

def crear_cliente(nombre, email, telefono):
    conn = sqlite3.connect('clientes.db')
    c = conn.cursor()
    c.execute("INSERT INTO clientes (nombre, email, telefono) VALUES (?, ?, ?)", (nombre, email, telefono))
    conn.commit()
    conn.close()

def listar_clientes():
    conn = sqlite3.connect('clientes.db')
    c = conn.cursor()
    c.execute("SELECT * FROM clientes")
    rows = c.fetchall()
    for row in rows:
        print(row)
    conn.close()

def actualizar_cliente(id, nombre, email, telefono):
    conn = sqlite3.connect('clientes.db')
    c = conn.cursor()
    c.execute("UPDATE clientes SET nombre=?, email=?, telefono=? WHERE id=?", (nombre, email, telefono, id))
    conn.commit()
    conn.close()

def borrar_cliente(id):
    conn = sqlite3.connect('clientes.db')
    c = conn.cursor()
    c.execute("DELETE FROM clientes WHERE id=?", (id,))
    conn.commit()
    conn.close()

def main():
    crear_tabla()
    while True:
        try:
            print("\n1. Crear cliente")
            print("2. Listar clientes")
            print("3. Actualizar cliente")
            print("4. Borrar cliente")
            print("5. Salir")
            opcion = input("Selecciona una opción: ")

            if opcion == '1':
                nombre = input("Nombre: ")
                email = input("Email: ")
                telefono = input("Teléfono: ")
                crear_cliente(nombre, email, telefono)
            elif opcion == '2':
                listar_clientes()
            elif opcion == '3':
                id = int(input("ID del cliente: "))
                nombre = input("Nuevo nombre: ")
                email = input("Nuevo email: ")
                telefono = input("Nuevo teléfono: ")
                actualizar_cliente(id, nombre, email, telefono)
            elif opcion == '4':
                id = int(input("ID del cliente: "))
                borrar_cliente(id)
            elif opcion == '5':
                break
            else:
                print("Opción no válida")
        except EOFError:
            break

if __name__ == "__main__":
    main()