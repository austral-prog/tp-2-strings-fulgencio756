def rectangle():
    """Lee base y altura de un rectángulo, calcula e imprime
    el área y el perímetro.
    """

    base=int(input("ingrese base: "))
    altura=int(input("ingrese altura: "))
    area=base*altura
    perimetro=(2*(base+altura))
    print(f"Base: {base}")
    print(f"Altura: {altura}")
    print("Area:",area)
    print("Perimetro:",perimetro)
