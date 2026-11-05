def validar_precio(texto):
    """Valida que el texto ingresado sea un número flotante positivo."""
    try:
        precio = float(texto)
    except ValueError:
        raise ValueError("El precio debe contener solo números")

    if precio < 0:
        raise ValueError("El precio no puede ser negativo")

    return precio


def mostrar_producto(producto):
    """Muestra de manera ordenada los datos de una tupla de producto de la BD."""
    print(
        f"ID:{producto[0]} | "
        f"{producto[1]} | "
        f"{producto[2]} | "
        f"${producto[3]:.2f}"  # Agregado :.2f para mostrar siempre dos decimales limpios
    )
