"""Mide y grafica los tiempos de los algoritmos de subarreglo maximo."""

import random
import time
import matplotlib.pyplot as plt

from subarreglo import subarreglo_fuerza_bruta, subarreglo_maximo


def generar_datos(cantidad: int) -> list[int]:
    """Genera una lista de variaciones diarias.

    Args:
        cantidad: cantidad de valores que tendra la lista.

    Returns:
        Lista de enteros entre -100 y 100.
    """
    valores = []

    for _ in range(cantidad):
        valores.append(random.randint(-100, 100))

    return valores


def medir_tiempo_fuerza_bruta(valores: list[int]) -> float:
    """Mide el tiempo de ejecucion de fuerza bruta.

    Args:
        valores: lista de valores a procesar.

    Returns:
        Tiempo de ejecucion en segundos.
    """
    inicio = time.perf_counter()

    subarreglo_fuerza_bruta(valores)

    fin = time.perf_counter()

    return fin - inicio


def medir_tiempo_divide_venceras(valores: list[int]) -> float:
    """Mide el tiempo de ejecucion de divide y venceras.

    Args:
        valores: lista de valores a procesar.

    Returns:
        Tiempo de ejecucion en segundos.
    """
    inicio = time.perf_counter()

    subarreglo_maximo(
        valores, 0, len(valores) - 1
    )

    fin = time.perf_counter()

    return fin - inicio


random.seed(42)

tamaños = [10, 50, 100, 500, 1000, 4000, 8000]
repeticiones = 3

tiempos_fuerza = []
tiempos_divide = []

for n in tamaños:
    valores = generar_datos(n)

    suma_fuerza = subarreglo_fuerza_bruta(valores)[2]

    suma_divide = subarreglo_maximo(
        valores, 0, len(valores) - 1
    )[2]

    assert suma_fuerza == suma_divide

    total_fuerza = 0
    total_divide = 0

    for _ in range(repeticiones):
        total_fuerza += medir_tiempo_fuerza_bruta(valores)
        total_divide += medir_tiempo_divide_venceras(valores)

    tiempos_fuerza.append(total_fuerza / repeticiones)
    tiempos_divide.append(total_divide / repeticiones)


plt.plot(
    tamaños,
    tiempos_fuerza,
    marker="o",
    label="Fuerza bruta"
)

plt.plot(
    tamaños,
    tiempos_divide,
    marker="o",
    label="Divide y vencerás"
)

plt.title("Tiempo de ejecución según el tamaño de entrada")
plt.xlabel("Tamaño de entrada, n (elementos)")
plt.ylabel("Tiempo de ejecución (segundos)")
plt.legend()

plt.savefig("graficas/tiempo_vs_n.png")
plt.show()