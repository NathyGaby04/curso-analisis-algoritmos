import random

from subarreglo import subarreglo_fuerza_bruta, subarreglo_maximo


# Un solo elemento
serie = [7]

assert subarreglo_fuerza_bruta(serie)[2] == 7
assert subarreglo_maximo(serie, 0, len(serie) - 1)[2] == 7


# Todos los valores negativos
serie = [-8, -3, -10]

assert subarreglo_fuerza_bruta(serie)[2] == -3
assert subarreglo_maximo(serie, 0, len(serie) - 1)[2] == -3


# Todos los valores positivos
serie = [2, 4, 1, 3]

assert subarreglo_fuerza_bruta(serie)[2] == 10
assert subarreglo_maximo(serie, 0, len(serie) - 1)[2] == 10


# Ejemplo del laboratorio
serie = [-3, 5, -2, 8, -6, 3, 9, -4]

assert subarreglo_fuerza_bruta(serie)[2] == 17
assert subarreglo_maximo(serie, 0, len(serie) - 1)[2] == 17


# Caso donde la mejor solucion cruza el punto medio
serie = [-2, 4, 5, -1, 6, -3]

assert subarreglo_fuerza_bruta(serie)[2] == 14
assert subarreglo_maximo(serie, 0, len(serie) - 1)[2] == 14


# 20 casos aleatorios
random.seed(42)

for _ in range(20):
    cantidad = random.randint(1, 20)
    serie = []

    for _ in range(cantidad):
        serie.append(random.randint(-10, 10))

    assert (
        subarreglo_fuerza_bruta(serie)[2]
        == subarreglo_maximo(serie, 0, len(serie) - 1)[2]
    )


print("Todas las pruebas pasaron correctamente.")