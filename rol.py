CLAVE_ADMIN = "admin123"

def pedir_rol():
    while True:
        print("=" * 34)
        print("=" * 6 + " Selecciona tu perfil " + "=" * 6)
        print("=" * 34)
        print("1. Usuario (pedir bebidas)")
        print("2. Administrador")

        opcion = input("Opcion: ")

        if opcion == "1":
            return "usuario"

        elif opcion == "2":
            clave = input("Ingrese la clave de administrador: ")
            if clave == CLAVE_ADMIN:
                return "admin"
            print("Clave incorrecta.\n")

        else:
            print("Opcion no valida, intente de nuevo.\n")
