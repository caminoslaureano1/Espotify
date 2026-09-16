import os
import sys
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from estructuras.arbol_binario import ArbolBST
from servicios.catalogo import Catalogo


def medir():
    catalogo = Catalogo()
    # Cambiar por la ruta real que utilices (canciones.json o canciones_kaggle.csv)
    ruta = "datos/canciones.json"

    if os.path.exists("datos/canciones_kaggle.csv"):
        ruta = "datos/canciones_kaggle.csv"
        catalogo.cargar_desde_csv(ruta)
    else:
        catalogo.cargar_desde_json(ruta)

    elementos = catalogo.listar(limite=len(catalogo))
    total = len(elementos)

    if total == 0:
        print("El catálogo está vacío.")
        return

    # Construcción previa del árbol (NO se mide dentro del cronómetro de búsqueda)
    arbol = ArbolBST()
    for c in elementos:
        arbol.insertar(c, clave=lambda x: x.titulo.lower())

    # Canción a buscar (tomamos el último elemento para probar el peor caso secuencial)
    cancion_objetivo = elementos[-1].titulo.lower()

    # 1. Medir Búsqueda Secuencial
    inicio = time.perf_counter()
    catalogo.buscar_secuencial(cancion_objetivo)
    fin = time.perf_counter()
    tiempo_secuencial = (fin - inicio) * 1000  # ms

    # 2. Medir Búsqueda en Árbol BST
    inicio = time.perf_counter()
    arbol.buscar(cancion_objetivo, clave=lambda x: x.titulo.lower())
    fin = time.perf_counter()
    tiempo_arbol = (fin - inicio) * 1000  # ms

    print("=" * 60)
    print(f"BENCHMARK ESPOTIFY (Dataset: {total} elementos)")
    print("=" * 60)
    print(f"Objetivo buscado: '{cancion_objetivo}'")
    print("-" * 60)
    print(f"Secuencial : {tiempo_secuencial:.5f} ms")
    print(f"Árbol BST  : {tiempo_arbol:.5f} ms")
    print("=" * 60)


if __name__ == "__main__":
    medir()