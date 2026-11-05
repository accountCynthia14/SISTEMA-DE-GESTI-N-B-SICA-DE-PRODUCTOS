# Import the connection manager from your database module
from database import conexion

# Import the functional logic from your products module
from productos import (
    agregar_producto,
    ver_productos,
    buscar_producto,
    eliminar_producto,
    actualizar_precio,
    buscar_categoria_y_precio,
)

def programa_principal():
    while True:
        # Your exact requested dashboard layout
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

        opcion = input("Elegir opcion: ").strip()

        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            ver_productos()
        elif opcion == "3":
            buscar_producto()
        elif opcion == "4":
            eliminar_producto()
        elif opcion == "5":
            actualizar_precio()
        elif opcion == "6":
            buscar_categoria_y_precio()
        elif opcion == "7":
            print("Fin del programa")
            # Safely close the SQLite connection before exiting
            conexion.close()
            break
        else:
            print("Opción inválida")

# Safe standard entry point for Python applications
if __name__ == "__main__":
    programa_principal()