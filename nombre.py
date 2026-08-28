def pedir_nombre():
    while True:
        name = input("Ingrese su nombre por favor: ").strip()
        if name != "" and all(caracter.isalpha() or caracter.isspace() for caracter in name):
            return name
        print("Nombre invalido, intente de nuevo.")