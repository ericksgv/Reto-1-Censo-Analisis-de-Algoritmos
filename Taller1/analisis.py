import random
import string
import time
import matplotlib.pyplot as plt

# Función para generar un nombre aleatorio de 4 caracteres en mayúsculas
def generar_nombre():
    return ''.join(random.choices(string.ascii_uppercase, k=4))


# Función para crear un registro con las características especificadas
def crear_registro(id_ordenado):
    nombre = generar_nombre()
    edad = random.randint(18, 99)
    impuesto = random.choice([True, False])

    return {
        'id_ordenado': id_ordenado,
        'nombre': nombre,
        'edad': edad,
        'impuesto': impuesto
    }


def imprimir_registro(registro):
    print("\n--Inicio de registro--")
    for key, value in registro.items():
        print(f"{key}: {value}")
    print("--Fin de registro--")


# Función para generar la lista de registros
def generar_registros(n):
    registros = [crear_registro(i + 1) for i in range(n)]
    return registros


# Función para Buscar de forma binaria los id
def buscar_id(registros, id_ingresado):
    inicio = 0
    fin = len(registros) - 1

    while inicio <= fin:
        medio = (inicio + fin) // 2
        id_medio = registros[medio]['id_ordenado']

        if id_medio == id_ingresado:
            return registros[medio]
        elif id_medio < id_ingresado:
            inicio = medio + 1
        else:
            fin = medio - 1

    return None


# Función para Buscar de forma secuencial los nombres
def buscar_nombre(registros, nombre_ingresado, id_usuario):
    nombre_mayusculas = nombre_ingresado.upper()
    for registro in registros:
        # Para hacer una comparación justa
        # Dado que muchos registros pueden compartir el mismo nombre
        # Se asegura que se encuentra el nombre del registro que tiene
        # el id recibido por la función de modo que sea ese registro y no
        # otro registro con el mismo nombre pero diferente id y así ver
        # la comparación un poco más adecuada
        if registro['nombre'] == nombre_mayusculas and registro["id_ordenado"] == id_usuario:
            return registro
    return None


def main():
    # Diccionario con los arreglos de tiempos de búsqueda lineal y búsqueda binaria

    tiempos_busquedas = {"lineal": [], "binaria": []}

    # Arreglo de tamaños de los registros.
    valores_n = []

    iteraciones = 10

    # Número de registros inicial
    num_registros = 100000

    multiplo = 1

    for i in range(iteraciones):

        # Cantidad de registros
        cantidad = num_registros*multiplo

        # Agregar num_registro al arreglo de valores_n:
        valores_n.append(cantidad)

        # Generar la lista con el valor actual de num_registros
        registros = generar_registros(cantidad)

        print(f"Hay {len(registros)} ")

        # Imprimir datos del último registro en el arreglo
        imprimir_registro(registros[-1])

        # Calcular tiempo de ejecución de función de búsqueda lineal
        nombre = registros[-1]["nombre"]
        id = registros[-1]["id_ordenado"]

        # Empezar conteo
        inicio = time.perf_counter()

        # Encontrar último elemento del arreglo de registros por nombre (Busqueda lineal)
        registro = buscar_nombre(registros, nombre, id)

        # Fin del conteo
        fin = time.perf_counter()

        if registro:
            print("\nRegistro encontrado")
            imprimir_registro(registro)
            print("\nRegistro encontrado")

        # Tiempo total para ejecutar busqueda lineal
        tiempos_busquedas["lineal"].append(fin - inicio)

        # Calcular tiempo de ejecución de función de búsqueda binario
        id = registros[-1]["id_ordenado"]

        # Empezar conteo
        inicio = time.perf_counter()

        # Encontrar el último elemento del arreglo de registros por ID (Búsqueda binaria)
        buscar_id(registros, id)

        # Terminar conteo
        fin = time.perf_counter()

        # Tiempo total para ejecutar la función de búsqueda binaria:
        tiempos_busquedas["binaria"].append(fin - inicio)

        # Aumentar multiplo
        multiplo += 1

        # Limpiar la lista
        registros.clear()

    # Imprimir los tiempos de busqueda lineal
    for busqueda in tiempos_busquedas:
        print(f"\nTiempos para busqueda {busqueda}")
        for i, t in zip(valores_n, tiempos_busquedas[busqueda]):
            print(f"Valor de n: {i} ->  {t} segundos")

    # Graficar resultados
    plt.plot(valores_n, tiempos_busquedas["lineal"], label="Búsqueda Lineal", marker='o', color="green")
    plt.plot(valores_n, tiempos_busquedas["binaria"], label="Búsqueda Binaria", marker='o', color="purple")
    plt.xlabel("Tamaño de la lista de registros")
    plt.ylabel("Tiempo de ejecución (s)")
    plt.title("Búsqueda Lineal VS Búsqueda Binaria")
    plt.legend()
    plt.grid(True)
    plt.show()
main()
