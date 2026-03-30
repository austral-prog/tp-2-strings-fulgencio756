def change():
    """Lee un gasto y el dinero recibido, calcula el vuelto
    y lo separa en pesos (parte entera) y centavos.
    """
    pass
    precio = float(input("Ingresar gasto: "))
    pago = int(input("Dinero recibido: "))

    vuelto = pago - precio

    pesos = int(vuelto)
    centavos = round((vuelto - pesos) * 100)

    print("\nVuelto\n")
    print("Pesos:")
    print(pesos)
    print("Centavos:")
    print(centavos)
