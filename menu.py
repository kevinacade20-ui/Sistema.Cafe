from nombre import pedir_nombre 

def mostrar_menu ():
    print("=" * 35)
    print("=" * 4 + " Binevenido al sistema " + "=" * 4)
    print("=" * 35)

    name = pedir_nombre()

    print("=" * 45)
    print(f"Bienvenido {nombre_cliente}, ¿Que gustas el dia de hoy?")
    print("=" * 45)

    print("1. Pedir un cafe")
    print("2. Pedir bebida caliente sin cafeina")
    print("3. Ver historial de pedidos")
    print("4. Salir del programa")

def mostrar_menu_usuario(nombre_cliente):
    mensaje = f"Bienvenido, {nombre_cliente}. Que gustas el dia de hoy?"
    print("=" * len(mensaje))
    print(mensaje)
    print("=" * len(mensaje))

    print("1. Pedir un cafe")
    print("2. Pedir bebida caliente sin cafeina")
    print("3. Ver mi historial de pedidos")
    print("4. Salir del programa")

def mostrar_menu_admin():
    print("=" * 34)
    print("=" * 5 +" Panel de Administrador " + "=" * 5)
    print("=" * 34)

    print("1. Ver historial completo de pedidos")
    print("2. Ver reporte diario de ventas")
    print("3. Salir del programa")
