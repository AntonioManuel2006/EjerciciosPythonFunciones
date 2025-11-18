"""añade al informe que se hace en el ejercicio PY0006 el código necesario para que muestre los dos elementos con más stock. (usa sorrted-lambda)"""

inventario_total = {'CUS001': 12, 'CUS002': 5, 'CUSOO3': 0}
ventas = ['CUS001', 'CUS002', 'CUS001', 'CUS004']
reposiciones = {'CUS002': 10, 'CUS004': 7}
# Crear una copia de trabajo del inventario
inventario = inventario_total.copy()
# Procesar las ventas
avisos = []
for codigo in ventas:
    if codigo not in inventario:
        inventario[codigo] = 0
        avisos.append(f'Aviso: El codigo {codigo} no existe en el inventario. Se ha añadido con stock 0.')
        inventario[codigo] -= 1
    else:
        inventario [codigo] -= 1
# Aplicar las reposiciones
for codigo in reposiciones:
    if codigo in inventario:
        inventario [codigo] += reposiciones[codigo]
    else:
        inventario [codigo] = reposiciones[codigo]
# Generar informe
num_referencias = len(inventario)
unidades_totales = sum(inventario_total.values())
print(f'Numero de referencias: {num_referencias}')
print(f'Unidades totales: {unidades_totales}')
# Eliminar productos con stock 0 o negativo
clases_borrar = [codigo for codigo, stock in inventario.items() if stock <= 0]
for codigo in clases_borrar:
    inventario.pop(codigo)
# Consulta de stock
codigo_consulta = input('Introduce el codigo a consultar: ').strip()
stock = inventario.get(codigo_consulta)
if stock is not None:
    print(f'El stock del codigo {codigo_consulta} es: {stock}')
else:
    print(f'No existe el codigo')
# Borrar el objeto diccionario inventari
del inventario
print("Inventario eliminado.")


# Mostrar los dos elementos con más stock
inventario_ordenado = sorted(inventario_total.items(), key=lambda item: item[1], reverse=True)
top_dos = inventario_ordenado[:2]
print("Los dos elementos con más stock son:")
for codigo, stock in top_dos:
    print(f'Código: {codigo}, Stock: {stock}')
