import csv
from collections import Counter
from datetime import date

ARCHIVO_PEDIDOS = "pedidos.csv"


def ver_reporte_diario():
    print("=" * 32)
    print("=" * 3 + " Reporte diario de ventas " + "=" * 3)
    print("=" * 32)

    hoy = date.today().strftime("%Y-%m-%d")

    try:
        with open(ARCHIVO_PEDIDOS, "r", newline="", encoding="utf-8") as archivo:
            lector = csv.reader(archivo)
            pedidos_hoy = [fila for fila in lector if fila and fila[5].startswith(hoy)]
    except FileNotFoundError:
        print("No existe historial de pedidos.")
        return

    if not pedidos_hoy:
        print("No hay pedidos registrados hoy (" + hoy + ").")
        return

    total_recaudado = 0
    total_bebidas = 0
    contador_bebidas = Counter()

    for nombre_cliente, bebida, cantidad, precio_unitario, total, fecha in pedidos_hoy:
        cantidad = int(cantidad)
        total = int(total)

        total_recaudado += total
        total_bebidas += cantidad
        contador_bebidas[bebida] += cantidad

    bebida_top, veces = contador_bebidas.most_common(1)[0]

    print("Fecha: " + hoy)
    print("Bebidas vendidas: " + str(total_bebidas))
    print("Total recaudado: $" + str(total_recaudado))
    print("Bebida mas pedida: " + bebida_top + " (" + str(veces) + " unidades)")
