# Función recursiva para convertir un número entero a binario
def convertir_a_binario(numero):
    if numero > 1:
        convertir_a_binario(numero // 2)
    print(numero % 2, end='')

# Función recursiva para contar la cantidad de dígitos en un número entero
def contar_digitos(numero):
    if numero == 0:
        return 0
    return 1 + contar_digitos(numero // 10)

# Función recursiva para calcular la raíz cuadrada entera
def calcular_raiz_cuadrada(numero, estimacion=0):
    if estimacion ** 2 == numero:
        return estimacion
    elif estimacion ** 2 > numero:
        return estimacion - 1
    else:
        return calcular_raiz_cuadrada(numero, estimacion + 1)

def raiz_cuadrada_entera(numero):
    return calcular_raiz_cuadrada(numero)

# Función recursiva para convertir un número romano a decimal
def convertir_a_decimal(romano):
    romanos = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if len(romano) == 1:
        return romanos[romano]
    else:
        if romanos[romano[0]] < romanos[romano[1]]:
            return -romanos[romano[0]] + convertir_a_decimal(romano[1:])
        else:
            return romanos[romano[0]] + convertir_a_decimal(romano[1:])

# Función recursiva para sumar números enteros
def suma_numeros_enteros(numero):
    if numero == 0:
        return 0
    return numero + suma_numeros_enteros(numero - 1)

# Función para mostrar el menú y procesar la opción seleccionada por el usuario CUI
def menu():
    print("Menú:")
    print("1. Convertir a Binario")
    print("2. Contar Dígitos")
    print("3. Raíz Cuadrada Entera")
    print("4. Convertir a Decimal desde Romano")
    print("5. Suma de Números Enteros")
    print("6. Salir")

    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        numero = int(input("Ingrese un número entero: "))
        print("El número en binario es:", end=' ')
        convertir_a_binario(numero)
        print()
    elif opcion == 2:
        numero = int(input("Ingrese un número entero: "))
        print("La cantidad de dígitos es:", contar_digitos(numero))
    elif opcion == 3:
        numero = int(input("Ingrese un número entero: "))
        print("La raíz cuadrada entera es:", raiz_cuadrada_entera(numero))
    elif opcion == 4:
        romano = input("Ingrese un número romano: ")
        print("El número en decimal es:", convertir_a_decimal(romano))
    elif opcion == 5:
        numero = int(input("Ingrese un número entero positivo: "))
        print("La suma de los números enteros hasta", numero, "es:", suma_numeros_enteros(numero))
    elif opcion == 6:
        print("Saliendo del programa...")
        return
    else:
        print("Opción inválida. Por favor seleccione una opción válida.")
    
    menu()  # Volver al menú después de procesar la opción seleccionada

# Llamar a la función de menú para iniciar el programa
menu()


