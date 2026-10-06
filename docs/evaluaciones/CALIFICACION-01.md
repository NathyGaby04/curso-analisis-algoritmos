# Retroalimentación — Laboratorio 01: Fundamentos, complejidad y recurrencias

**Estudiante:** Nathalie Gabriela Miranda Rejón · **Laboratorio:** Fundamentos, complejidad y recurrencias (Tamiza)
**Fecha límite:** 2026-10-06 23:59 · **Versión revisada:** commit `1748b2c`

Muy buen trabajo en general: el informe es completo y sus afirmaciones se apoyan en sus propias mediciones.

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 21 / 25 |
| Calidad de la explicación teórica | 23 / 25 |
| Corrección de la implementación | 17 / 20 |
| Calidad del análisis de las gráficas | 18 / 20 |
| Documentación y organización del informe | 10 / 10 |
| **Total** | **89 / 100** |
| **Nota (0–5)** | **4.45** |

## 1. Corrección conceptual (21 / 25)
**Lo que hizo bien:**
- Distingue entre que el algoritmo sea correcto y que sea viable, y nombra la restricción que se incumple: la ventana de 2:00 a 6:00 a. m. que ya falló tres veces.
- Explica que un servidor más rápido no cambia la forma en que crece el trabajo cuando crecen los datos.
- En la Parte 2 relaciona el tiempo de ejecución con el consumo de energía acumulado noche tras noche.
- Da dos perjuicios concretos (el paciente de riesgo alto llamado tarde y el operador con una lista incompleta) e indica quién asume el costo de cada uno.
- Discute bien la obligación de que el orden de la lista sea correcto, porque decide a quién se llama primero.

**Lo que puede mejorar:**
- El segundo ejemplo (el bot de Tigo) cuenta una experiencia interesante, pero no deja claro qué restricción concreta se incumple (por ejemplo, un tiempo máximo de respuesta) ni cuántos datos procesa el sistema.
- En la Parte 2, el costo para la Secretaría y el equipo de desarrollo se menciona de pasada; podría detallarse más.

## 2. Calidad de la explicación teórica (23 / 25)
**Lo que hizo bien:**
- Define peor, mejor y caso promedio indicando sobre qué se toma cada uno, justifica que usaría el peor caso por la ventana estricta y deja escrita la predicción antes de medir.
- Plantea la recurrencia de merge sort explicando cada término y la resuelve con el árbol de recursión: costo por nivel, número de niveles y costo total `Θ(n log n)`.
- Calcula insertion sort línea a línea y presenta la tabla de complejidades.

**Lo que puede mejorar:**
- El caso promedio de insertion sort se explica con una idea general ("la mitad de los elementos"); faltó mostrar la suma que lleva a `n²/4`.

## 3. Corrección de la implementación (17 / 20)
**Lo que hizo bien:**
- `insertion_sort` y `merge_sort` ordenan bien, no cambian la lista recibida, cuentan solo comparaciones entre elementos y no usan `sorted()` ni `sort()`. El mejor caso da exactamente `n - 1` comparaciones.
- Los tres generadores producen listas con valores distintos y del tamaño pedido, y los aleatorios usan semilla reproducible.
- Funciones con *type hints* y *docstrings*.

**Lo que puede mejorar:**
- Faltan líneas en blanco entre funciones y un salto de línea al final de varios archivos (PEP 8).
- `parte3_casos.py` y `parte4_complejidad.py` son código suelto sin funciones, y `parte4_complejidad.py` no tiene descripción al inicio.

## 4. Calidad del análisis de las gráficas (18 / 20)
**Lo que hizo bien:**
- Las tres gráficas existen y tienen título, ejes rotulados y leyenda; los escenarios y los dos algoritmos están en los mismos ejes.
- Identifica con evidencia el escenario C como peor caso, B como mejor y A como cercano al promedio, y lo contrasta con su predicción.
- En 4.3 recomienda merge sort, usa un dato medido (n = 6400) contra la compra del servidor, extrapola a 1.200.000 registros declarándolo como estimación y menciona la memoria adicional.

**Lo que puede mejorar:**
- Cada medición se hizo una sola vez; repetirla y promediar daría curvas más estables, y convendría decirlo en el informe.
- En 4.2 la explicación de lo que ocurre con tamaños pequeños es genérica; podía apoyarse en los valores medidos.
- La gráfica de la Parte 4 no tiene marcadores ni cuadrícula, y con insertion sort tan arriba casi no se distingue la curva de merge sort.

## 5. Documentación y organización del informe (10 / 10)
**Lo que hizo bien:**
- El laboratorio está en `laboratorios/lab1-fundamentos-complejidad-recurrencias/`, ubicación válida, con todos los archivos del entregable.
- El README tiene su nombre, instrucciones para reproducir, las partes en orden, enlaces al código y gráficas incrustadas que se ven.
- Hay cinco commits del laboratorio con mensajes descriptivos.

## ¿El código funciona?
Sí. Los dos scripts corren sin errores, ordenan bien y regeneran las gráficas, y los tiempos obtenidos coinciden con los de su informe.

## Para el próximo laboratorio
- Cuando dé un ejemplo propio, indique qué se procesa, cuántos datos hay y qué restricción concreta se incumple.
- Repita las mediciones varias veces y grafique el promedio, aclarándolo en el informe.
- Organice los scripts en funciones y corrija los detalles de PEP 8 (líneas en blanco, final de archivo).
- Cuando explique el caso promedio, muestre el cálculo y no solo la idea general.
