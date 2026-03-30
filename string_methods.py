def string_methods():
    """Demuestra el uso de métodos de string: strip, lstrip, rstrip, upper, lower,
    title, find, replace, count, operador in, slicing con paso, reverso,
    f-strings y strings multilínea.
    """
    nombre = "   Grace Hopper   "
    frase = "Python es un gran lenguaje de programacion"
    multilinea = """Linea 1
    Linea 2
    Linea 3"""
    print("Strip:",nombre.strip())
    print("Lstrip:",nombre.lstrip())
    print("Rstrip:",nombre.rstrip())
    print("Upper:", frase.upper())
    print("Lower:", frase.lower())
    print("Title:", frase.title())
    print("Find:",frase.find("gran"))
    print("Replace:",frase.replace("programacion", "desarrollo"))
    print("Count:", frase.count("a"))
    print("Contiene Python:","Python" in frase)
    print("Contiene Java:","java" in frase)
    print("Slice:",frase[0:6])
    python=(frase[0:6:2])
    print("Paso:",python)
    print("Reverso:", frase[0:6][::-1])
    print(f"Formato: {nombre.strip()} sabe Python")
    multilinea = """Linea 1
Linea 2
Linea 3"""
    print(multilinea)

