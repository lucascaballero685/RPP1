from paquete_ventas.validaciones import es_entero_positivo, convertir_a_entero
from paquete_ventas.operaciones import sumar_vector, obtener_maximo

def cargar_ventas(nombres_regiones):
    ventas = []
    print("\n--- CARGA DE VENTAS ---")
    for i in range(len(nombres_regiones)):
        while True:
            entrada = input(f"ingrese la cantidad de ventas para la region {nombres_regiones[i]}: ")
            if es_entero_positivo(entrada):
                valor = convertir_a_entero(entrada)
                if valor > 0:
                    ventas.append(valor)
                    break
                else:
                    print("Error: no se permite el ingreso de ceros. intente nuevamente.")
            else:
                print("Error: Dato invalido (ingrese solo numeros enteros positivos). Reintete.")
    print("¡Ventas cargadas exitosamente!")
    return ventas

def mostrar_ventas(ventas, nombre_regiones):
    total_ventas = sumar_vector(ventas)
    print("\n--- LISTADO DE VENTAS POR REGION ---")
    for i in range(len(ventas)):
        porcentaje = (ventas[i] * 100) / total_ventas if total_ventas > 0 else 0
        print(f"[{i+1}] Region: {nombre_regiones[i]} | Ventas: {ventas[i]} | Porcentaje: {porcentaje:.2f}%")
    print(f"Cantidad total de productor vendidos en todas las regiones: {total_ventas}")

def regiones_menos_de_5(ventas, nombres_regiones):
    total_ventas = sumar_vector(ventas)
    encontrado = False
    acumulado_porcentaje = 0
    print("\n--- REGIONES CON MENOS DEL 5% DE VENTAS ---")
    for i in range(len(ventas)):
        porcentaje = (ventas[i]  * 100 / total_ventas if total_ventas > 0 else 0)
        if porcentaje < 5:
            print(f"Region: {nombres_regiones[i]} | Ventas: {ventas[i]} | Porcentaje: {porcentaje:.2f}%")
            acumulado_porcentaje += porcentaje
            encontrado = True
    if not encontrado:
        print("Error: Ninguna region cumple con esta caracteristica (menos del 5%).")
    else:
        print(f"Porcentaje acumulado de las regiones encontradas: {acumulado_porcentaje:.2f}%")

def regiones_menos_de_25(ventas, nombres_regiones):
    total_ventas = sumar_vector(ventas)
    encontrado = False
    acumulado_porcentaje = 0
    print("\n--- REGIONES CON MENOS DEL 25% DE VENTAS ---")
    for i in range(len(ventas)):
        porcentaje = (ventas[i] * 100) / total_ventas if total_ventas > 0 else 0
        if porcentaje < 25:
            print(f"Region: {nombres_regiones[i]} | Ventas: {ventas[i]} | Porcentaje: {porcentaje:.2f}%")
            acumulado_porcentaje += porcentaje
            encontrado = True
    if not encontrado:
        print("Error: Ninguna region cumple con esta caracteristica (menos del 25%).")
    else:
        print(f"Porcentaje acumulado de las regiones encontradas: {acumulado_porcentaje:.2f}%")

def regiones_mas_de_500(ventas, nombres_regiones):
    encontrado = False
    suma = 0 
    cantidad = 0