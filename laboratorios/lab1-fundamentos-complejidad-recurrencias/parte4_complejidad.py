import time
import matplotlib.pyplot as plt
from algoritmos import insertion_sort, merge_sort
from datos import generar_aleatorio

tamanos = [100, 200, 400, 800, 1600, 3200, 6400]
tiempos_insertion = []
tiempos_merge = []

for n in tamanos:
    datos = generar_aleatorio(n)
    inicio = time.perf_counter()
    insertion_sort(datos)
    fin = time.perf_counter()
    tiempos_insertion.append(fin - inicio)

    inicio = time.perf_counter()
    merge_sort(datos)
    fin = time.perf_counter()
    tiempos_merge.append(fin - inicio)

print("Tamaños:", tamanos)
print("Tiempos insertion sort:", tiempos_insertion)
print("Tiempos merge sort:", tiempos_merge)

plt.plot(tamanos, tiempos_insertion, label="Insertion sort")
plt.plot(tamanos, tiempos_merge, label="Merge sort")
plt.title("Tiempo de ejecución: Insertion sort vs Merge sort")
plt.xlabel("Tamaño de entrada (n)")
plt.ylabel("Tiempo de ejecución (segundos)")
plt.legend()
plt.savefig("graficas/parte4_tiempo.png")
plt.show()