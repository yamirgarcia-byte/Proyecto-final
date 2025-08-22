#Definir una función que dado un listado de alumnos evalúe cuántos aprobaron y cuántos desaprobaron,
#teniendo en cuenta que se aprueba con 4. La nota será el promedio de las 3 notas para cada alumno.

def evaluar_alumnos(lista_alumnos):
    aprobados = 0
    desaprobados = 0

    for alumno in lista_alumnos:
        nombre = alumno['nombre']
        notas = alumno['notas']
        promedio = sum(notas) / len(notas)

        if promedio >= 4:
            aprobados += 1
        else:
            desaprobados += 1

    print(f"Aprobados: {aprobados}")
    print(f"Desaprobados: {desaprobados}")

# Definimos la lista de alumnos aquí
alumnos = [
    {'nombre': 'Mario', 'notas': [2, 6, 3]},
    {'nombre': 'Jose', 'notas': [2, 3, 4]},
    {'nombre': 'Jorge', 'notas': [3, 2, 3]},
    {'nombre': 'Mateo', 'notas': [6, 5, 4]},
]

# Llamamos a la función
evaluar_alumnos(alumnos)
