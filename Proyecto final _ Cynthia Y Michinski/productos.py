# Importamos variables que contienen referencias a objetos
from database import cursor, conexion
from utils import validar_precio, mostrar_producto

def verificar_base_de_datos() -> bool:
    """Verifica si las variables de la base de datos se cargaron correctamente."""
    if cursor is None or conexion is None:
        print("[❌] Error: La base de datos no está disponible.")
        return False
    return True

def agregar_producto():
    if not verificar_base_de_datos(): return

    nombre = input("Nombre: ").strip()
    categoria = input("Categoria: ").strip()
    precio_texto = input("Precio: ").strip()

    if not nombre:
        print("Nombre inválido")
        return

    if not categoria:
        print("Categoría inválida")
        return

    try:
        precio = validar_precio(precio_texto)
    except ValueError as error:
        print(error)
        return

    cursor.execute(
        """
        INSERT INTO productos(nombre, categoria, precio)
        VALUES(?, ?, ?)
        """,
        (nombre, categoria, precio)
    )
    conexion.commit()
    print("Producto agregado")

def ver_productos():
    if not verificar_base_de_datos(): return

    cursor.execute("SELECT * FROM productos")
    productos = cursor.fetchall()

    if len(productos) == 0:
        print("No hay productos")
        return
        
    # Recordemos que el enumerate devuelve una tupla siendo (indice/enumeracion, objeto)
    for i, producto in enumerate(productos, start=1):
        # Recordemos que el end, elimina el \n propio del print
        print(f"{i}. ", end="")
        mostrar_producto(producto)

def buscar_producto():
    if not verificar_base_de_datos(): return

    buscado = input("Buscar por nombre: ").strip()

    if not buscado:
        print("Debe ingresar un nombre")
        return

    cursor.execute(
        """
        SELECT *
        FROM productos
        WHERE nombre LIKE ?
        """,
        ("%" + buscado + "%",)
    )
    # Recordemos que el like nos permite ingresar patrones de busqueda
    # En este caso se ingresa el % (comodin) para buscar variaciones que incluyan la palabra buscada

    resultados = cursor.fetchall()

    if len(resultados) == 0:
        print("No se encontraron resultados")
        return

    for producto in resultados:
        mostrar_producto(producto)

def eliminar_producto():
    if not verificar_base_de_datos(): return

    cursor.execute("SELECT * FROM productos")
    productos = cursor.fetchall()

    if len(productos) == 0:
        print("No hay productos para eliminar")
        return

    print("\nPRODUCTOS DISPONIBLES:")
    for producto in productos:
        mostrar_producto(producto)

    try:
        id_borrar = int(input("\nID del producto a eliminar: "))
    except ValueError:
        print("Debe ingresar un número")
        return

    cursor.execute(
        """
        DELETE FROM productos
        WHERE id = ?
        """,
        (id_borrar,)
    )
    conexion.commit()
    print("Producto eliminado")

def actualizar_precio():
    if not verificar_base_de_datos(): return

    cursor.execute("SELECT * FROM productos")
    productos = cursor.fetchall()

    if len(productos) == 0:
        print("No hay productos")
        return

    print("\nPRODUCTOS DISPONIBLES:")
    for producto in productos:
        mostrar_producto(producto)

    try:
        id_producto = int(input("\nID del producto: "))
        nuevo_precio = validar_precio(input("Nuevo precio: "))
    except ValueError as error:
        print(error)
        return

    cursor.execute(
        """
        UPDATE productos
        SET precio = ?
        WHERE id = ?
        """,
        (nuevo_precio, id_producto)
    )
    conexion.commit()
    print("Precio actualizado")

def buscar_categoria_y_precio():
    if not verificar_base_de_datos(): return

    categoria = input("Categoria: ").strip()

    try:
        precio_maximo = float(input("Precio máximo: ")) # Cambiado a float para soportar decimales como precios reales
    except ValueError:
        print("Debe ingresar un número")
        return

    cursor.execute(
        """
        SELECT *
        FROM productos
        WHERE categoria = ?
        AND precio <= ?
        """,
        (categoria, precio_maximo)
    )

    resultados = cursor.fetchall()

    if len(resultados) == 0:
        print("No se encontraron productos")
        return

    for producto in resultados:
        mostrar_producto(producto)
