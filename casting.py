from ctypes import cdll


def casting():
    """Lee precio, descuento y cantidad como texto y calcula el precio con descuento y el total."""

    precio=int(input("introduce el precio:"))
    descuento=float(input("introduce el descuento:"))
    cantidad=int(input("introduce la cantidad"))
    precio_real=(precio-descuento)
    precio_total=(cantidad*precio_real)
    print(f"Precio: {precio}")
    print(f"Descuento: {descuento}")
    print(f"Precio con descuento: {precio_real}")
    print(f"Total: {precio_total}")

