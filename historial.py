import csv

ARCHIVO_PEDIDOS = "pedidos.csv"

def ver_historial():
    try:
        print("=" * 25)
        print("=" * 2 + " Historial de pedidos " + "=" * 2)
        print("=" * 25)
        with open(ARCHIVO_PEDIDOS, "r", newline="", encoding="utf-8") as archivo:
            lector = csv.reader(archivo)
            pedidos = list(lector)
            if pedidos:
                for i, pedido in enumerate(pedidos, start = 1):
                    nombre_cliente, bebida, cantidad, precio_unitario, total, fecha = pedido
                    print(str(i) + ". [" + fecha + "] " + nombre_cliente + " - " + cantidad + "x " + bebida + " - $" + total)
            else:
                print("No hay ningun pedido.")

    except FileNotFoundError:
        print("No existe historial de pedidos.")


def ver_historial_usuario(nombre_cliente):
    try:
        print("=" * 29)
        print("=" * 2 + " Tu historial de pedidos " + "=" * 2)
        print("=" * 29)
        with open(ARCHIVO_PEDIDOS, "r", newline="", encoding="utf-8") as archivo:
            lector = csv.reader(archivo)
            pedidos = [fila for fila in lector if fila and fila[0] == nombre_cliente]

            if pedidos:
                for i, pedido in enumerate(pedidos, start = 1):
                    _, bebida, cantidad, precio_unitario, total, fecha = pedido
                    print(str(i) + ". [" + fecha + "] " + cantidad + "x " + bebida + " - $" + total)
            else:
                print("Aun no tienes pedidos registrados.")

    except FileNotFoundError:
        print("No existe historial de pedidos.")
