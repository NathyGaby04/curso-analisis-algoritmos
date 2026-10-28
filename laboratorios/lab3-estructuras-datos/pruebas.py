"""Pruebas para la lista enlazada y la tabla hash."""


import random

from estructuras import ListaEnlazada, TablaHash


# Prueba 1: busqueda exitosa e infructuosa en la lista enlazada.
lista = ListaEnlazada()
lista.insertar(1234567890, "en bodega")
lista.insertar(2345678901, "en reparto")

assert lista.buscar(1234567890) == "en bodega"
assert lista.buscar(2345678901) == "en reparto"
assert lista.buscar(9999999999) is None
assert lista.tamano == 2


# Prueba 2: busqueda exitosa e infructuosa en la tabla hash.
tabla = TablaHash(7)
tabla.insertar(1234567890, "en bodega")
tabla.insertar(2345678901, "en reparto")

assert tabla.buscar(1234567890) == "en bodega"
assert tabla.buscar(2345678901) == "en reparto"
assert tabla.buscar(9999999999) is None
assert tabla.tamano == 2


# Prueba 3: colisiones forzadas con m = 7.
tabla_colisiones = TablaHash(7)

tabla_colisiones.insertar(10, "en bodega")
tabla_colisiones.insertar(24, "en reparto")
tabla_colisiones.insertar(17, "entregado")

assert tabla_colisiones.hash(10) == 3
assert tabla_colisiones.hash(24) == 3
assert tabla_colisiones.hash(17) == 3

assert tabla_colisiones.buscar(10) == "en bodega"
assert tabla_colisiones.buscar(24) == "en reparto"
assert tabla_colisiones.buscar(17) == "entregado"

assert tabla_colisiones.casillas[3].tamano == 3
assert tabla_colisiones.tamano == 3
assert tabla_colisiones.factor_carga() == 3 / 7


# Prueba 4: comparar ambas estructuras con colecciones aleatorias.
azar = random.Random(7)
estados = ["en bodega", "en reparto", "entregado"]

for numero_prueba in range(20):
    lista = ListaEnlazada()
    tabla = TablaHash(101)

    cantidad = azar.randint(1, 50)
    guias = []

    while len(guias) < cantidad:
        guia = azar.randint(10**9, 10**10 - 1)

        if guia not in guias:
            guias.append(guia)

    for guia in guias:
        estado = azar.choice(estados)
        lista.insertar(guia, estado)
        tabla.insertar(guia, estado)

    # Todas las guias existentes deben dar el mismo resultado.
    for guia in guias:
        assert lista.buscar(guia) == tabla.buscar(guia)

    # Las guias inexistentes tambien deben dar el mismo resultado.
    for _ in range(10):
        guia = azar.randint(10**9, 10**10 - 1)

        while guia in guias:
            guia = azar.randint(10**9, 10**10 - 1)

        assert lista.buscar(guia) is None
        assert tabla.buscar(guia) is None


print("Todas las pruebas fueron superadas.")
