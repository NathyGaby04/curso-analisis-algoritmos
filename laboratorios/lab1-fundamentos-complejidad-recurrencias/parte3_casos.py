"""Experimento de peor, mejor y caso promedio para insertion sort."""

import time
import matplotlib.pyplot as plt

from algoritmos import insertion_sort
from datos import generar_aleatorio, generar_casi_ordenado, generar_inverso


tamanos = [100, 200, 400, 800, 1600, 3200, 6400]

resultados = {
    "A": [],
    "B": [],
    "C": []
}

tiempos = {
    "A": [],
    "B": [],
    "C": []
}


for n in tamanos:
    datos_a = generar_aleatorio(n)
    datos_b = generar_casi_ordenado(n)
    datos_c = generar_inverso(n)

    inicio = time.perf_counter()
    _, comparaciones_a = insertion_sort(datos_a)
    fin = time.perf_counter()

    resultados["A"].append(comparaciones_a)
    tiempos["A"].append(fin - inicio)

    inicio = time.perf_counter()
    _, comparaciones_b = insertion_sort(datos_b)
    fin = time.perf_counter()

    resultados["B"].append(comparaciones_b)
    tiempos["B"].append(fin - inicio)

    inicio = time.perf_counter()
    _, comparaciones_c = insertion_sort(datos_c)
    fin = time.perf_counter()

    resultados["C"].append(comparaciones_c)
    tiempos["C"].append(fin - inicio)


print("Tamaños:", tamanos)
print("Comparaciones:")
print("A:", resultados["A"])
print("B:", resultados["B"])
print("C:", resultados["C"])

print("\nTiempos:")
print("A:", tiempos["A"])
print("B:", tiempos["B"])
print("C:", tiempos["C"])

plt.figure()
plt.plot(tamanos, resultados["A"], marker="o", label="Escenario A")
plt.plot(tamanos, resultados["B"], marker="o", label="Escenario B")
plt.plot(tamanos, resultados["C"], marker="o", label="Escenario C")

plt.xlabel("Tamaño de entrada (n)")
plt.ylabel("Número de comparaciones")
plt.title("Comparaciones de insertion sort")
plt.legend()
plt.grid(True)

plt.savefig("graficas/parte3_comparaciones.png")
plt.show()

plt.figure()
plt.plot(tamanos, tiempos["A"], marker="o", label="Escenario A")
plt.plot(tamanos, tiempos["B"], marker="o", label="Escenario B")
plt.plot(tamanos, tiempos["C"], marker="o", label="Escenario C")

plt.xlabel("Tamaño de entrada (n)")
plt.ylabel("Tiempo (segundos)")
plt.title("Tiempo de ejecución de insertion sort")
plt.legend()
plt.grid(True)

plt.savefig("graficas/parte3_tiempo.png")
plt.show()