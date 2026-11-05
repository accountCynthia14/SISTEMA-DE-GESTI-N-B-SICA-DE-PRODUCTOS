import sqlite3

try:
    # 1. Establish connection and cursor variables (imported by productos.py and main.py)
    conexion = sqlite3.connect("productos.db")
    cursor = conexion.cursor()
    print("ejecutando database...")

    def crear_tabla():
        """Creates the product data structure if it does not exist yet."""
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS productos(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            categoria TEXT NOT NULL,
            precio REAL NOT NULL
        )
        """)
        conexion.commit()

    def cerrar_conexion():
        """Safely closes the connection stream."""
        conexion.close()

    # 2. CRITICAL FIX: Run the table creation instantly when this module load starts
    crear_tabla()

except sqlite3.Error as e:
    print(f"\n[❌] Error crítico de Base de Datos: {e}")
