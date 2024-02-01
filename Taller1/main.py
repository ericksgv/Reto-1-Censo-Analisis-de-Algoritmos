import random
import string


# Función para generar un nombre aleatorio de 4 caracteres en mayúsculas
def generar_nombre():
    return ''.join(random.choices(string.ascii_uppercase, k=4))


# Función para crear un registro con II, Nombre, edad, impuesto
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


# Función para generar la lista de registros
def generar_registros():
    registros = [crear_registro(i) for i in range(500000)]
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
def buscar_nombre(registros, nombre_ingresado):
    nombre_mayusculas = nombre_ingresado.upper()
    for registro in registros:
        if registro['nombre'] == nombre_mayusculas:
            return registro
    return None


def main():
    # Generar lista de n registros
    registros = generar_registros()

    # Menú principal
    while True:
        print("1. Ingrese un ID menor a 500000")
        print("2. Ingrese un nombre de 4 caracteres")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            try:
                id_ingresado = int(input("Ingrese un ID menor a 500000: "))
                if id_ingresado < 500000:
                    resultado_busqueda = buscar_id(registros, id_ingresado)
                    if resultado_busqueda:
                        print("ID encontrado:", resultado_busqueda)
                    else:
                        print("ID no encontrado en la lista.")
                else:
                    print("El ID debe ser menor a 500000. Intenta de nuevo.")
            except ValueError:
                print("Por favor, ingrese un número válido.")

        elif opcion == '2':
            nombre_ingresado = input("Ingrese un nombre con 4 caracteres: ")
            resultado_busqueda = buscar_nombre(registros, nombre_ingresado)
            if resultado_busqueda:
                print("Nombre encontrado:", resultado_busqueda)
            else:
                print("Nombre no encontrado en la lista.")

        elif opcion == '3':
            print("Saliendo del programa. ¡Hasta luego!")
            break

        else:
            print("Opción no válida. Por favor, elija una opción válida")


main()
