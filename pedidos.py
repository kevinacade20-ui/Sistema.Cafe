import csv
from datetime import datetime

ARCHIVO_PEDIDOS = "pedidos.csv"
from nombre import pedir_nombre

def pedir_cafe(nombre_cliente):
    print("=" * 35)
    print("=" * 4 + " Elige el cafe que quieras " + "=" * 4)
    print("=" * 35)

    cafes = {
        "1": ("Americano", 4000),
        "2": ("Espresso", 3500),
        "3": ("Mocha", 5500),
        "4": ("Latte", 5000),
        "5": ("Capuccino", 5000),
        "6": ("Macchiato", 5200),
        "7": ("Amaretto", 5800)
    }

    for clave, (nombre_cafe, precio) in cafes.items():
        print(clave + ". " + nombre_cafe + " - $" + str(precio))
    print("0. Cancelar pedido")

    opcion = input("Opcion: ")

    if opcion == "0":
        print("Pedido cancelado.")
        return

    if opcion in cafes:
        cafe_elegido, precio_unitario = cafes[opcion]

        cantidad = input("Cuantas unidades deseas?: ")
        while not cantidad.isdigit() or int(cantidad) <= 0:
            cantidad = input("Cantidad invalida. Ingrese un numero mayor a 0: ")
        cantidad = int(cantidad)

        total = cantidad * precio_unitario

        confirmar = input("Confirmar " + str(cantidad) + "x " + cafe_elegido + " por $" + str(total) + "? (si/no): ").lower()
        if confirmar != "si":
            print("Pedido cancelado.")
            return

        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        print("Pediste " + str(cantidad) + "x " + cafe_elegido + ". Total: $" + str(total) + ". Preparando tu cafe!")

        with open(ARCHIVO_PEDIDOS, "a", newline="", encoding="utf-8") as archivo:
            escritor = csv.writer(archivo)
            escritor.writerow([nombre_cliente, cafe_elegido, cantidad, precio_unitario, total, fecha])

    else:
        print("Opcion no valida, intente de nuevo")

def bebida_sin_cafeina(nombre_cliente):
    print("=" * 35)
    print("=" * 4 + " Elige la bebida que quieras " + "=" * 4)
    print("=" * 35)

    sin_cafeina = {
        "1": ("Aromatica de frutas", 3000),
        "2": ("Aromatica de hierbabuena", 3000),
        "3": ("Agua de panela", 2500),
        "4": ("Te de manzanilla", 3200),
        "5": ("Infusion de frutos rojos", 3500),
        "6": ("Te de canela", 3200),
        "7": ("Chocolate sin leche", 4500),
        "8": ("Chocolate con leche deslactosada", 4800)
    }

    for clave, (nombre_bebida, precio) in sin_cafeina.items():
        print(clave + ". " + nombre_bebida + " - $" + str(precio))
    print("0. Cancelar pedido")

    opcion = input("Opcion: ")

    if opcion == "0":
        print("Pedido cancelado.")
        return

    if opcion in sin_cafeina:
        bebida_elegida, precio_unitario = sin_cafeina[opcion]

        cantidad = input("Cuantas unidades deseas?: ")
        while not cantidad.isdigit() or int(cantidad) <= 0:
            cantidad = input("Cantidad invalida. Ingrese un numero mayor a 0: ")
        cantidad = int(cantidad)

        total = cantidad * precio_unitario

        confirmar = input("Confirmar " + str(cantidad) + "x " + bebida_elegida + " por $" + str(total) + "? (si/no): ").lower()
        if confirmar != "si":
            print("Pedido cancelado.")
            return

        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        print("Pediste " + str(cantidad) + "x " + bebida_elegida + ". Total: $" + str(total) + ". Preparando tu bebida caliente!")

        with open(ARCHIVO_PEDIDOS, "a", newline="", encoding="utf-8") as archivo:
            escritor = csv.writer(archivo)
            escritor.writerow([nombre_cliente, bebida_elegida, cantidad, precio_unitario, total, fecha])

    else:
        print("Opcion no valida, intente de nuevo")

def continuar_pedido(nombre_cliente):
    continuar = True
    while continuar:
        respuesta = input("¿Gustas ordenar algo mas?: ").lower()
        while respuesta != "si" and respuesta != "no":
                print("Respuesta invalida. Ingrese nuevamente su opcion. (si/no).")
                respuesta = input("¿Gustas ordenar algo mas?: ").lower()
        
        if respuesta == "no":
                continuar = False
                print("Gracias por su pedido, lo esperamos pronto ")
                break
                    
        print("=" * 35)
        print("=" * 7 + " TIPO DE BEBIDA " + "=" * 7)
        print("=" * 35)

        print("1. Bebida con cafeina")
        print("2. Bebida sin cafeina")

        eleccion = input("Opcion: ")

        if eleccion == "1":
            pedir_cafe(nombre_cliente)
        elif eleccion == "2":
            bebida_sin_cafeina(nombre_cliente)
        else:
            print("Opcion invalida, intente de nuevo.")
