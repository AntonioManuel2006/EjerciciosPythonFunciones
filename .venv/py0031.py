#añade al informe de PY0007 el Ranking de alumnos por nota media ordenador (descendente), en caso de empate se ordena nombre. (sorted-lambda)
# python
calificaciones = [
    {'alumno': 'Ana', 'modulo': 'Programación', 'nota': 7.5},
    {'alumno': 'Ana', 'modulo': 'Sistemas', 'nota': 8.0},
    {'alumno': 'Luis', 'modulo': 'Sistemas', 'nota': 6.0},
    {'alumno': 'Marta', 'modulo': 'Programación', 'nota': 9.0},
    {'alumno': 'Marta', 'modulo': 'Programación', 'nota': 10.0},
]

# Construir la estructura anidada
alumnos = {}
for registro in calificaciones:
    alumno = registro['alumno']
    modulo = registro['modulo']
    nota = registro['nota']
    alumnos.setdefault(alumno, {}).setdefault(modulo, []).append(nota)

print("Estructura anidada de alumnos y calificaciones:")
print(alumnos)

# Calcular la media aritmética de todos los módulos de un alumno (usando la nota máxima por módulo)
medias_alumnos = {}
for alumno, mods in alumnos.items():
    notas_maximas = [max(notas) for notas in mods.values()]
    medias_alumnos[alumno] = sum(notas_maximas) / len(notas_maximas) if notas_maximas else 0.0

print("Media aritmética de todos los módulos por alumno:")
print(medias_alumnos)

# Generar un diccionario con el módulo y los alumnos con su nota máxima en el módulo
modulo_notas = {}
for alumno, mods in alumnos.items():
    for modulo, notas in mods.items():
        nota_maxima = max(notas)
        modulo_notas.setdefault(modulo, {})[alumno] = nota_maxima

print("Diccionario de módulos y notas máximas por alumno:")
print(modulo_notas)

# Filtrar aprobados por módulo
aprobados_por_modulo = {
    modulo: {alumno: nota for alumno, nota in alumnos_modulo.items() if nota >= 5}
    for modulo, alumnos_modulo in modulo_notas.items()
}
print("Aprobados por módulo:")
print(aprobados_por_modulo)

# Simular correcciones para subir o bajar notas
import copy
correcciones = {'Ana': {'Programación': +0.75}, 'Luis': {'Sistemas': -1.0}}
alumnos_corregidos = copy.deepcopy(alumnos)
for alumno, modulos in correcciones.items():
    for modulo, ajuste in modulos.items():
        if alumno in alumnos_corregidos and modulo in alumnos_corregidos[alumno] and alumnos_corregidos[alumno][modulo]:
            alumnos_corregidos[alumno][modulo][-1] += ajuste

print("Alumnos con notas corregidas:")
print(alumnos_corregidos)

# Eliminar una matrícula concreta (sin definir una función)
nota_borrada = None
try:
    nota_borrada = alumnos['Marta']['Programación'].pop(0)
    # limpiar estructuras vacías
    if not alumnos['Marta']['Programación']:
        del alumnos['Marta']['Programación']
    if not alumnos['Marta']:
        del alumnos['Marta']
    print("Nota borrada:", nota_borrada)
except (KeyError, IndexError):
    print("No se pudo borrar la matrícula: no existe alumno/modulo/índice")

print("Estructura de alumnos tras eliminación:")
print(alumnos)

# Ranking de alumnos por nota media (descendente), en caso de empate se ordena por nombre
ranking_alumnos = sorted(medias_alumnos.items(), key=lambda x: (-x[1], x[0]))
print("Ranking de alumnos por nota media:")
for alumno, media in ranking_alumnos:
    print(f"{alumno}: {media:.2f}")

