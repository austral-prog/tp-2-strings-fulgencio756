from dataclasses import replace


def ficha():
    """Ejercicio integrador. Lee nombre, email y 3 notas, y genera una ficha
    de alumno aplicando: strip, title, lower, upper, int, len, find, slicing,
    reverse, replace, count, in, f-strings, strings multilínea y operaciones matemáticas.
    """
    # Ejercicio integrador: Generador de Ficha de Alumno
    #
    # Leer mediante input:
    #   1. Nombre completo (puede tener espacios extra y mayúsculas mezcladas)
    #   2. Email (puede tener mayúsculas)
    #   3. Tres notas (como texto, hay que convertirlas)
    #
    # Generar una ficha que incluya:
    #   - Encabezado decorativo usando un string multilínea con "="
    #   - Nombre limpio: sin espacios extra y con formato título
    #   - Email en minúsculas
    #   - Cantidad de caracteres del nombre
    #   - Iniciales: usar find para encontrar el espacio e indexar las letras
    #   - Usuario: apellido.nombre en minúsculas
    #   - Verificar si el email contiene @ 
    #   - Extraer el dominio del email
    #   - Nombre con guion bajo en vez de espacio
    #   - Contar las 'a' en el nombre
    #   - Código secreto: nombre invertido en mayúsculas
    #   - Las 3 notas, su suma, promedio y promedio entero
    #   - Cierre decorativo usando repetición de string ("=" * 24)
    nombre=input("ingrese su nombre:")
    nombre=nombre.lower()
    nombre=nombre.title()
    nombre=nombre.strip()
    mail=input("ingrese su mail:")
    mail=mail.lower()
    inicial1=nombre[0:1]
    espacio=nombre.find(" ")
    inicial2=nombre[espacio+1]
    apellido=nombre[espacio+1:]
    solonombre=nombre[:espacio]
    arroba=mail.find("@")
    dominio=mail[arroba+1:]
    nombre_en_mayusculsa=nombre.upper()

    nota1=input("nota 1:")
    nota2=input("nota 2:")
    nota3=input("nota 3:")
    nota1=int(nota1)
    nota2=int(nota2)
    nota3=int(nota3)
    suma=nota1+nota2+nota3
    promedio=suma/3
    print("""========================
    FICHA DEL ALUMNO
========================""")
    print("Nombre:",nombre)
    print("Email:",mail)
    print("Caracteres en nombre:", len(nombre))
    print("Iniciales:",inicial1+inicial2)
    print("Usuario:",apellido.lower()+"."+solonombre.lower())
    print("Email valido:","@" in mail)
    print("Dominio:",dominio)
    print("Nombre para archivo:",nombre.replace(" ","_"))
    print("Cantidad de a:",nombre.count("a"))
    print("Codigo secreto:",nombre_en_mayusculsa[::-1])
    print(f"""Nota 1: {nota1}
Nota 2: {nota2}
Nota 3: {nota3}""")
    print("Suma:",suma)
    print("Promedio:",promedio)
    print("Promedio entero:",int(promedio))
    print("========================")
