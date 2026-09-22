"""Generadores de lotes de registros para los escenarios de Tamiza."""
import random

def generar_aleatorio(n: int, semilla: int = 42) -> list[int]:
    """Genera un lote de n registros en orden aleatorio (escenario A).

    Args:
        n: cantidad de registros del lote.
        semilla: semilla del generador aleatorio, para que el
            experimento sea reproducible.

    Returns:
        Lista de n indices de riesgo enteros distintos, desordenada.
    """
    rng = random.Random(semilla)
    lista = list(range(n))
    rng.shuffle(lista)
    return lista

def generar_casi_ordenado(n: int, semilla: int = 42) -> list[int]:
    """Genera un lote casi ordenado: 98% ordenado y 2% al final (escenario B).

    Args:
        n: cantidad de registros del lote.
        semilla: semilla del generador aleatorio.

    Returns:
        Lista de n indices de riesgo enteros distintos, con el primer
        98% en el orden que el algoritmo produce y el 2% restante
        desordenado al final.
    """
    rng = random.Random(semilla)
    lista = list(range(n))
    cantidad_desordenada = max(1, int(n * 0.02))
    indices_desordenados = rng.sample(lista, cantidad_desordenada)
    parte_ordenada = [valor for valor in lista if valor not in indices_desordenados]
    rng.shuffle(indices_desordenados)
    return parte_ordenada + indices_desordenados

def generar_inverso(n: int) -> list[int]:
    """Genera un lote en el orden exactamente contrario (escenario C).

    Args:
        n: cantidad de registros del lote.

    Returns:
        Lista de n indices de riesgo enteros distintos, en el orden
        inverso al que el algoritmo debe producir.
    """
    lista = list(range(n))
    lista.reverse()
    return lista
