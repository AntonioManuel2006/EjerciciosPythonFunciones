

def sumar(a, b):
    """Suma dos números"""
    return a + b

def restar(a, b):
    """Resta dos números"""
    return a - b

def multiplicar(a, b):
    """Multiplica dos números"""
    return a * b

def dividir(a, b):
    """Divide dos números"""
    if b == 0:
        return None
    return a / b

def obtener_numero(mensaje):
    """Solicita un número al usuario y valida la entrada"""
    while True:
        entrada = input(mensaje)
        if entrada.lower() == "salir":
            return None
        try:
            return float(entrada)
        except ValueError:
            print("Número inválido. Intenta de nuevo.")

def mostrar_menu():
    """Muestra el menú de opciones"""
    print("\nCALCULADORA")
    print("Sumar  Restar  Multiplicar  Dividir")

def ejecutar_operacion(opcion):
    """Ejecuta la operación seleccionada"""
    # Solicitar números
    n1 = obtener_numero("Primer número (o 'salir'): ")
    if n1 is None:
        return False

    n2 = obtener_numero("Segundo número (o 'salir'): ")
    if n2 is None:
        return False

    # Realizar operación
    if opcion == "sumar":
        resultado = sumar(n1, n2)
    elif opcion == "restar":
        resultado = restar(n1, n2)
    elif opcion == "multiplicar":
        resultado = multiplicar(n1, n2)
    elif opcion == "dividir":
        resultado = dividir(n1, n2)
        if resultado is None:
            print("Error: división por cero.")
            return True

    print(f"Resultado: {resultado}")
    return True

def calculadora():
    """Función principal de la calculadora"""
    mostrar_menu()

    while True:
        opcion = input("\nElige operación (o 'salir'): ").lower()

        if opcion == "salir":
            print("Saliendo...")
            break

        if opcion in ["sumar", "restar", "multiplicar", "dividir"]:
            continuar = ejecutar_operacion(opcion)
            if not continuar:
                print("Saliendo...")
                break
        else:
            print("Operación no válida.")

# Ejecutar la calculadora
if __name__ == "__main__":
    calculadora()