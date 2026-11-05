# =====================================================================
# SISTEMA DE GESTIÓN BÁSICA DE PRODUCTOS (PRE-ENTREGA OBLIGATORIA)
# =====================================================================

# 1. Usar listas para almacenar y gestionar los datos.
# Iniciamos la lista principal con 3 sublistas de productos como ejemplos
productos = [
    ["Teclado", "Electronica", 5000],
    ["Mouse", "Electronica", 2500],
    ["Cuaderno", "Libreria", 1200]
]

# El programa continúa funcionando en un bucle continuo hasta elegir salir (Opción 7)
while True:
    # Presentar un menú que permita elegir entre las funcionalidades disponibles
    print("\n===========================================")
    print("  SISTEMA DE GESTIÓN BÁSICA DE PRODUCTOS   ")
    print("===========================================")
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto")
    print("4. Eliminar producto")
    print("5. Actualizar precio")
    print("6. Buscar por categoria y precio")
    print("7. Salir")
    print("===========================================")
    
    # Utilizar condicionales para gestionar las opciones del menú
    opcion = input("Seleccione una opción (1-5): ").strip()
    
    if opcion == "1":
        print("\n[1] --- Agregar Nuevo Producto ---")
        
        # Validar entrada del nombre (que no esté vacío)
        nombre = ""
        while not nombre:
            nombre = input("Ingrese el nombre del producto: ").strip()
            if not nombre:
                print("-> Error: El nombre no puede estar vacío.")
                
        # Validar entrada de la categoría (que no esté vacía)
        categoria = ""
        while not categoria:
            categoria = input("Ingrese la categoría: ").strip()
            if not categoria:
                print("-> Error: La categoría no puede estar vacía.")
                
        # Validar entrada del precio (entero, sin letras ni decimales)
        precio = None
        while precio is None:
            precio_input = input("Ingrese el precio (solo números enteros): ").strip()
            if precio_input.isdigit():  # Valida que sean solo dígitos
                precio = int(precio_input)
            else:
                print("-> Error: Precio inválido. Ingrese un número entero sin centavos.")
        
        # Almacenar el producto como una sublista de tres elementos [nombre, categoria, precio]
        productos.append([nombre, categoria, precio])
        print(f"\n¡Éxito! El producto '{nombre}' fue agregado correctamente.")
        
    elif opcion == "2":
        print("\n[2] --- Lista de Productos Registrados ---")
        if not productos:
            print("No hay productos registrados en el sistema.")
        else:
            # Uso de bucle for para mostrar los productos ordenados y numerados
            for i in range(len(productos)):
                prod = productos[i]  # prod[0] = Nombre, prod[1] = Categoría, prod[2] = Precio
                print(f"{i + 1}. Nombre: {prod[0]} | Categoría: {prod[1]} | Precio: ${prod[2]}")
                
    elif opcion == "3":
        print("\n[3] --- Búsqueda de Productos ---")
        busqueda = input("Ingrese el nombre del producto a buscar: ").strip().lower()
        encontrado = False
        
        print("\nResultados coincidentes:")
        # Uso de bucle for para recorrer las sublistas y buscar coincidencias
        for prod in productos:
            if busqueda in prod[0].lower():  # Compara en minúsculas (coincidencia parcial o exacta)
                print(f"-> Encontrado: Nombre: {prod[0]} | Categoría: {prod[1]} | Precio: ${prod[2]}")
                encontrado = True
                
        # Si no hay coincidencias, informa al usuario
        if not encontrado:
            print("No se encontraron resultados para la búsqueda.")
            
    elif opcion == "4":
        print("\n[4] --- Eliminación de Productos ---")
        if not productos:
            print("No hay productos disponibles para eliminar.")
        else:
            try:
                posicion = int(input("Ingrese el número (posición) del producto a eliminar: "))
                # Validar que la posición seleccionada exista dentro del rango de la lista
                if 1 <= posicion <= len(productos):
                    # Se resta 1 porque el índice real en Python va de 0 a N-1
                    eliminado = productos.pop(posicion - 1)
                    print(f"\n¡Éxito! El producto '{eliminado[0]}' fue eliminado correctamente.")
                else:
                    print("-> Error: El número ingresado no corresponde a ningún producto.")
            except ValueError:
                print("-> Error: Entrada inválida. Debe ingresar un número entero.")
                
    elif opcion == "5":
        print("\nSaliendo del sistema... ¡Muchas gracias por utilizarlo!")
        break
        
    else:
        print("-> Opción no válida. Por favor, elija un número del 1 al 5.")