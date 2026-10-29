"""Experimentos de rendimiento para la lista enlazada y la tabla hash."""

import os
import random
import time

import matplotlib.pyplot as plt

from estructuras import ListaEnlazada, TablaHash


def generar_guias_existentes(cantidad: int, semilla: int = 42) -> list[int]:
    """Genera guias unicas de diez digitos.

    Args:
        cantidad: numero de guias que se deben generar.
        semilla: semilla para reproducir los datos.

    Returns:
        Una lista con guias distintas.
    """
    azar = random.Random(semilla)
    guias: list[int] = []
    conjunto: set[int] = set()

    while len(guias) < cantidad:
        guia = azar.randint(10**9, 10**10 - 1)

        if guia not in conjunto:
            guias.append(guia)
            conjunto.add(guia)

    return guias


def generar_guias_inexistentes(
    existentes: set[int], cantidad: int, semilla: int = 7
) -> list[int]:
    """Genera guias de diez digitos que no estan en la coleccion.

    Args:
        existentes: guias almacenadas en las estructuras.
        cantidad: cuantas guias inexistentes generar.
        semilla: semilla del generador, para reproducir la medicion.

    Returns:
        Una lista con `cantidad` guias que no pertenecen a `existentes`.
    """
    azar = random.Random(semilla)
    inexistentes: list[int] = []
    generadas: set[int] = set()

    while len(inexistentes) < cantidad:
        guia = azar.randint(10**9, 10**10 - 1)

        if guia not in existentes and guia not in generadas:
            inexistentes.append(guia)
            generadas.add(guia)

    return inexistentes


def es_primo(numero: int) -> bool:
    """Indica si un numero es primo.

    Args:
        numero: numero que se va a comprobar.

    Returns:
        True si es primo; False en caso contrario.
    """
    if numero < 2:
        return False

    divisor = 2

    while divisor * divisor <= numero:
        if numero % divisor == 0:
            return False

        divisor += 1

    return True


def primo_cercano(numero: int) -> int:
    """Busca un numero primo cercano al numero indicado.

    Args:
        numero: valor alrededor del cual se busca el primo.

    Returns:
        El numero primo mas cercano, priorizando el inferior en empate.
    """
    objetivo = round(numero)
    distancia = 0

    while True:
        inferior = objetivo - distancia
        superior = objetivo + distancia

        if inferior >= 2 and es_primo(inferior):
            return inferior

        if distancia > 0 and es_primo(superior):
            return superior

        distancia += 1


def verificar_resultados(
    lista: ListaEnlazada,
    tabla: TablaHash,
    guias: list[int],
) -> None:
    """Comprueba que ambas estructuras devuelvan el mismo estado.

    Args:
        lista: lista enlazada con las guias.
        tabla: tabla hash con las mismas guias.
        guias: guias existentes que se van a comprobar.
    """
    for guia in guias[:20]:
        assert lista.buscar(guia) == tabla.buscar(guia)


def verificar_busquedas_fallidas(
    lista: ListaEnlazada,
    tabla: TablaHash,
    guias: list[int],
) -> None:
    """Comprueba que las guias inexistentes no se encuentren.

    Args:
        lista: lista enlazada con las guias existentes.
        tabla: tabla hash con las mismas guias.
        guias: guias que no pertenecen a las estructuras.
    """
    for guia in guias:
        assert lista.buscar(guia) is None
        assert tabla.buscar(guia) is None


def medir_busquedas(
    estructura: ListaEnlazada | TablaHash,
    guias: list[int],
) -> float:
    """Calcula el tiempo medio de busqueda en microsegundos.

    Realiza tres mediciones y devuelve el promedio del tiempo por busqueda.

    Args:
        estructura: lista enlazada o tabla hash.
        guias: guias que se van a buscar.

    Returns:
        Tiempo medio por busqueda, en microsegundos.
    """
    repeticiones = 3
    tiempos: list[float] = []

    for _ in range(repeticiones):
        inicio = time.perf_counter()

        for guia in guias:
            estructura.buscar(guia)

        fin = time.perf_counter()

        tiempo_medio = (fin - inicio) / len(guias)
        tiempos.append(tiempo_medio * 1_000_000)

    return sum(tiempos) / repeticiones


def crear_carpetas() -> str:
    """Crea la carpeta de graficas junto a este archivo.

    Returns:
        Ruta de la carpeta de graficas.
    """
    carpeta = os.path.dirname(os.path.abspath(__file__))
    carpeta_graficas = os.path.join(carpeta, "graficas")
    os.makedirs(carpeta_graficas, exist_ok=True)

    return carpeta_graficas


def experimento_a(carpeta_graficas: str) -> None:
    """Compara el tiempo de busqueda de la lista y la tabla hash."""
    tamanos = [100, 500, 1000, 5000, 20000, 50000]
    tiempos_lista: list[float] = []
    tiempos_tabla: list[float] = []
    estados = ["en bodega", "en reparto", "entregado"]

    print("\nEXPERIMENTO A: LISTA FRENTE A TABLA HASH")
    print(
        f"{'n':>8} {'m':>8} {'alfa':>8} "
        f"{'Lista (us)':>14} {'Tabla (us)':>14}"
    )

    for n in tamanos:
        guias = generar_guias_existentes(n, semilla=100 + n)
        existentes = set(guias)

        lista = ListaEnlazada()

        for indice, guia in enumerate(guias):
            estado = estados[indice % len(estados)]
            lista.insertar(guia, estado)

        m = primo_cercano(round(n / 2))
        tabla = TablaHash(m)

        for indice, guia in enumerate(guias):
            estado = estados[indice % len(estados)]
            tabla.insertar(guia, estado)

        # Se verifican los resultados antes de iniciar el cronometro.
        verificar_resultados(lista, tabla, guias)

        inexistentes = generar_guias_inexistentes(
            existentes, 200, semilla=7
        )
        verificar_busquedas_fallidas(lista, tabla, inexistentes)

        # Las mismas 200 guias se usan en ambas estructuras.
        tiempo_lista = medir_busquedas(lista, inexistentes)
        tiempo_tabla = medir_busquedas(tabla, inexistentes)

        tiempos_lista.append(tiempo_lista)
        tiempos_tabla.append(tiempo_tabla)

        print(
            f"{n:8d} {m:8d} {tabla.factor_carga():8.3f} "
            f"{tiempo_lista:14.4f} {tiempo_tabla:14.4f}"
        )

    plt.figure()
    plt.plot(
        tamanos, tiempos_lista, marker="o", label="Lista enlazada"
    )
    plt.plot(
        tamanos, tiempos_tabla, marker="o", label="Tabla hash"
    )
    plt.title("Tiempo de busqueda: lista enlazada frente a tabla hash")
    plt.xlabel("Numero de guias (n)")
    plt.ylabel("Tiempo medio por busqueda (microsegundos)")
    plt.legend()
    plt.grid(True)

    ruta = os.path.join(carpeta_graficas, "lista_vs_tabla.png")
    plt.savefig(ruta, dpi=150, bbox_inches="tight")
    plt.close()

    print(f"\nGrafica guardada en: {ruta}")


def experimento_b(carpeta_graficas: str) -> None:
    """Mide el efecto del factor de carga en la tabla hash."""
    n = 20000
    factores_objetivo = [0.5, 1, 4, 10]
    estados = ["en bodega", "en reparto", "entregado"]

    guias = generar_guias_existentes(n, semilla=2026)
    existentes = set(guias)

    lista = ListaEnlazada()

    for indice, guia in enumerate(guias):
        estado = estados[indice % len(estados)]
        lista.insertar(guia, estado)

    inexistentes = generar_guias_inexistentes(
        existentes, 200, semilla=7
    )

    alfas_reales: list[float] = []
    tiempos: list[float] = []

    print("\nEXPERIMENTO B: EFECTO DEL FACTOR DE CARGA")
    print(
        f"{'n':>8} {'m':>8} {'alfa real':>12} "
        f"{'Tiempo (us)':>14}"
    )

    for factor_objetivo in factores_objetivo:
        m = primo_cercano(round(n / factor_objetivo))
        tabla = TablaHash(m)

        for indice, guia in enumerate(guias):
            estado = estados[indice % len(estados)]
            tabla.insertar(guia, estado)

        verificar_resultados(lista, tabla, guias)
        verificar_busquedas_fallidas(lista, tabla, inexistentes)

        alfa_real = tabla.factor_carga()
        tiempo = medir_busquedas(tabla, inexistentes)

        alfas_reales.append(alfa_real)
        tiempos.append(tiempo)

        print(f"{n:8d} {m:8d} {alfa_real:12.4f} {tiempo:14.4f}")

    plt.figure()
    plt.plot(alfas_reales, tiempos, marker="o", label="Tabla hash")
    plt.title("Tiempo de busqueda segun el factor de carga")
    plt.xlabel("Factor de carga (alfa = n / m)")
    plt.ylabel("Tiempo medio por busqueda (microsegundos)")
    plt.legend()
    plt.grid(True)

    ruta = os.path.join(carpeta_graficas, "tiempo_vs_alfa.png")
    plt.savefig(ruta, dpi=150, bbox_inches="tight")
    plt.close()

    print(f"\nGrafica guardada en: {ruta}")


carpeta_graficas = crear_carpetas()

experimento_a(carpeta_graficas)
experimento_b(carpeta_graficas)
