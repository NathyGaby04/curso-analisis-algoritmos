# Retroalimentación — Laboratorio 2: Dividir y vencer

**Estudiante:** Nathalie Gabriela Miranda Rejón · **Laboratorio:** Laboratorio evaluativo 02 — Dividir y vencer
**Fecha límite:** 2026-10-21 23:59 · **Versión revisada:** commit `23c799b`

Muy buen trabajo: el laboratorio está completo, ordenado y bien sustentado con sus propias mediciones.

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 18 / 20 |
| Calidad de la explicación teórica | 18 / 20 |
| Corrección de la implementación | 24 / 25 |
| Calidad del análisis de las gráficas | 25 / 25 |
| Documentación y organización del informe | 9 / 10 |
| **Total** | **94 / 100** |
| **Nota (0–5)** | **4.70** |

## 1. Corrección conceptual (18 / 20)
**Lo que hizo bien:**
- Identificó que divide y vencerás empieza a ganar entre n=10 y n=50 y explicó por qué (el costo de las llamadas recursivas pesa en entradas pequeñas).
- Comparó con el máximo de un arreglo: combinar cuesta tiempo constante, la recurrencia da `Θ(n)` y dividir no mejora nada.
- Recomendó divide y vencerás y estimó el tiempo para 1.000.000 de registros, declarándolo como estimación.

**Lo que puede mejorar:**
- En la pregunta 3 faltó acotar el punto de cruce con un par de tamaños intermedios (por ejemplo 20 o 30).
- En la pregunta 4 podría mencionar que dividir sí puede servir por otras razones (por ejemplo, repartir el trabajo entre procesadores), aunque no baje el orden.

## 2. Calidad de la explicación teórica (18 / 20)
**Lo que hizo bien:**
- Planteó `T(n) = 2T(n/2) + Θ(n)` y explicó de dónde sale cada término.
- Aplicó el método maestro y comprobó la condición del caso 2 (`f(n) = Θ(n^(log₂2))`).
- Justificó el `Θ(n²)` de la fuerza bruta contando los `n(n+1)/2` tramos.

**Lo que puede mejorar:**
- Explique con más detalle por qué el caso cruzado cuesta `Θ(n)` (dos barridos, uno por cada lado del punto medio).

## 3. Corrección de la implementación (24 / 25)
**Lo que hizo bien:**
- Las tres funciones dan la suma correcta en todos los casos pedidos y coinciden en listas aleatorias; no modifican la lista recibida.
- `subarreglo_maximo` resuelve los tres casos y no llama a la fuerza bruta.
- Tienen *type hints* y *docstrings* estilo Google.

**Lo que puede mejorar:**
- El archivo `requirements.txt` quedó guardado con una codificación distinta (UTF-16) que `pip` puede no leer bien en otros equipos; guárdelo en UTF-8.

## 4. Calidad del análisis de las gráficas (25 / 25)
**Lo que hizo bien:**
- La gráfica tiene título, ejes rotulados, leyenda y ambas curvas en los mismos ejes, con 7 tamaños.
- Calculó el factor al duplicar n de 4000 a 8000 (≈3,64 para fuerza bruta y ≈2 para divide y vencerás) y lo contrastó con 4 y 2,17.
- Los valores que cita para n=8000 (cerca de 1 s) coinciden con la gráfica publicada.

## 5. Documentación y organización del informe (9 / 10)
**Lo que hizo bien:**
- Carpeta en una ubicación válida (`laboratorios/lab2-divide-y-vencer/`), con todos los archivos pedidos.
- Instrucciones de reproducción, enlaces al código en cada parte, gráfica incrustada con ruta relativa y tres commits descriptivos.

**Lo que puede mejorar:**
- Los encabezados del informe no son uniformes (la Parte 3 usa un nivel distinto a las Partes 1 y 2) y no hay tabla de valores medidos.

## ¿El código funciona?
Sí. Las pruebas pasan, ambos algoritmos coinciden en listas aleatorias y la medición corre y genera la gráfica sin errores.

## Para el próximo laboratorio
- Incluya una tabla con los tiempos medidos para respaldar sus afirmaciones sobre los tamaños pequeños.
- Pruebe tamaños intermedios cuando quiera ubicar un punto de cruce.
- Guarde `requirements.txt` en UTF-8.
- Explique cada término de una recurrencia con un poco más de detalle.
