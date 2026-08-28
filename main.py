from nombre import pedir_nombre
from rol import pedir_rol
from menu import mostrar_menu_usuario, mostrar_menu_admin
from pedidos import pedir_cafe, bebida_sin_cafeina, continuar_pedido
from historial import ver_historial, ver_historial_usuario
from reporte import ver_reporte_diario


def flujo_usuario():
    nombre_cliente = pedir_nombre()

    while True:
        mostrar_menu_usuario(nombre_cliente)
        opcion = input("Selecciona una opcion: ")

        if opcion == "1":
            pedir_cafe(nombre_cliente)
            continuar_pedido(nombre_cliente)

        elif opcion == "2":
            bebida_sin_cafeina(nombre_cliente)
            continuar_pedido(nombre_cliente)

        elif opcion == "3":
            ver_historial_usuario(nombre_cliente)

        elif opcion == "4":
            print("Muchas gracias por preferir este maravilloso lugar")
            break

        else:
            print("Opcion no valida, ingrese nuevamente")


def flujo_admin():
    while True:
        mostrar_menu_admin()
        opcion = input("Selecciona una opcion: ")

        if opcion == "1":
            ver_historial()

        elif opcion == "2":
            ver_reporte_diario()

        elif opcion == "3":
            print("Sesion de administrador finalizada")
            break

        else:
            print("Opcion no valida, ingrese nuevamente")


def main():
    print("=" * 39)
    print("=" * 5 + " Bienvenido al sistema Nikev " + "=" * 5)
    print("=" * 39)

    rol = pedir_rol()

    if rol == "usuario":
        flujo_usuario()
    elif rol == "admin":
        flujo_admin()


if __name__ == "__main__":
    main()
