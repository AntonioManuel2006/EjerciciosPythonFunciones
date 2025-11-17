import math
def calcular_area_circunferencia():
    radio = float(input("Introduce el radio de la circunferencia: "))
    area_circunferencia = lambda r: math.pi * r**2
    area = area_circunferencia(radio)
    print(f"El área de la circunferencia es: {area:.2f}")
calcular_area_circunferencia()

