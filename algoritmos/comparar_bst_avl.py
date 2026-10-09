import os
import random
import sys
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from estructuras.arbol_binario import ArbolBST
from estructuras.avl import AVL
from servicios.catalogo import Catalogo

RUTA_DATASET = "datos/canciones-kreagle.csv.csv"
N_ORDENADOS = 10_000
REPETICIONES = 1_000


def clave(c):
    return c.titulo.lower()


def construir(clase, canciones):
    arbol = clase()
    inicio = time.perf_counter()
    for c in canciones:
        arbol.insertar(c, clave=clave)
    return arbol, (time.perf_counter() - inicio) * 1000


def ms_por_busqueda(arbol, valores):
    """Tiempo promedio (ms) de una búsqueda, repitiendo la lista de valores."""
    inicio = time.perf_counter()
    for valor in valores:
        arbol.buscar(valor, clave=clave)
    return (time.perf_counter() - inicio) * 1000 / len(valores)


def fila(metrica, bst, avl):
    print(f"{metrica:<40}{bst:>14}{avl:>14}")


def medir():
    catalogo = Catalogo()
    catalogo.cargar_desde_csv(RUTA_DATASET)
    canciones = catalogo.listar(limite=len(catalogo))

    # 10.000 títulos distintos del dataset, en ORDEN ALFABÉTICO (peor caso del BST)
    por_titulo = {}
    for c in canciones:
        por_titulo.setdefault(clave(c), c)
    ordenadas = [por_titulo[t] for t in sorted(por_titulo)[:N_ORDENADOS]]

    # Con datos ordenados el BST recursivo llega a profundidad N:
    # con el límite por defecto (1000) lanza RecursionError.
    print(f"Límite de recursión por defecto: {sys.getrecursionlimit()}")
    try:
        construir(ArbolBST, ordenadas)
        print("BST con datos ordenados: construido sin error")
    except RecursionError:
        print("BST con datos ordenados: RecursionError (se sube el límite)")
    sys.setrecursionlimit(N_ORDENADOS * 3)

    bst, t_bst = construir(ArbolBST, ordenadas)
    avl, t_avl = construir(AVL, ordenadas)

    ultimo = [clave(ordenadas[-1])] * REPETICIONES
    random.seed(42)
    aleatorios = [clave(random.choice(ordenadas)) for _ in range(REPETICIONES)]
    inexistente = ["zzzz cancion inexistente"] * REPETICIONES

    print()
    print("=" * 68)
    print(f"BST vs AVL — {len(ordenadas)} títulos insertados en orden alfabético")
    print(f"Último título (hoja más profunda del BST): '{ordenadas[-1].titulo}'")
    print("=" * 68)
    fila("Métrica", "BST", "AVL")
    print("-" * 68)
    fila("Altura", bst.altura(), avl.altura())
    fila("Construcción (ms)", f"{t_bst:.1f}", f"{t_avl:.1f}")
    fila("Búsqueda del último título (ms)",
         f"{ms_por_busqueda(bst, ultimo):.4f}", f"{ms_por_busqueda(avl, ultimo):.4f}")
    fila("Búsqueda de títulos aleatorios (ms)",
         f"{ms_por_busqueda(bst, aleatorios):.4f}", f"{ms_por_busqueda(avl, aleatorios):.4f}")
    fila("Búsqueda de título inexistente (ms)",
         f"{ms_por_busqueda(bst, inexistente):.4f}", f"{ms_por_busqueda(avl, inexistente):.4f}")
    print(f"(promedio de {REPETICIONES} búsquedas por fila)")

    # Dataset completo en el orden original del CSV (no está ordenado por título)
    bst_real, t_bst_real = construir(ArbolBST, canciones)
    avl_real, t_avl_real = construir(AVL, canciones)
    print()
    print("=" * 68)
    print(f"Dataset completo en orden del CSV — {len(canciones)} filas, "
          f"{len(avl_real)} títulos distintos")
    print("=" * 68)
    fila("Métrica", "BST", "AVL")
    print("-" * 68)
    fila("Altura", bst_real.altura(), avl_real.altura())
    fila("Construcción (ms)", f"{t_bst_real:.1f}", f"{t_avl_real:.1f}")
    fila("Búsqueda de títulos aleatorios (ms)",
         f"{ms_por_busqueda(bst_real, aleatorios):.4f}",
         f"{ms_por_busqueda(avl_real, aleatorios):.4f}")


if __name__ == "__main__":
    medir()
