import os
import sys
import time
import random

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from servicios.catalogo import Catalogo

def buscar_secuencial_en_lista(canciones, titulo):
    objetivo = titulo.strip().lower()
    for cancion in canciones:
        if cancion.titulo.lower() == objetivo:
            return cancion
    return None

def contar_comparaciones(canciones, titulo):
    objetivo = titulo.strip().lower()
    comparaciones = 0

    for cancion in canciones:
        comparaciones += 1
        if cancion.titulo.lower() == objetivo:
            break
    return comparaciones

def medir():
    catalogo = Catalogo()
    # Carga del dataset usado en el experimento.
    ruta = "datos/canciones-kreagle.csv.csv"
    catalogo.cargar_desde_csv(ruta)

    elementos = catalogo.listar(limite=len(catalogo))
    total = len(elementos)

    if total == 0:
        print("El catálogo está vacío.")
        return

    tamaños = sorted(set(n for n in (100, 1_000, 10_000, total) if n <= total))
    repeticiones = 1_000
    random.seed(42)
    print("Busqueda secuencial: promedio de titulos elegidos al azar")
    print(f"{'canciones':>12} {'busquedas':>14} {'promedio (ms)':>16}")
    for tamaño in tamaños:
        muestra = elementos[:tamaño]
        objetivos = list(dict.fromkeys(c.titulo.lower() for c in muestra))
        objetivos =random.sample(objetivos, min(repeticiones, len(objetivos)))

        inicio = time.perf_counter()
        for objetivo in objetivos:
            buscar_secuencial_en_lista(muestra, objetivo)
        fin = time.perf_counter()

        promedio_ms = (fin - inicio) * 1000 / len(objetivos)
        print(f"{tamaño:>12} | {len(objetivos):>14} | {promedio_ms:>16.6f}")

    print("\nComparaciones de la busqueda secuencial")
    print(
        f"{'Canciones':>12}  {'Mejor caso':>14} "
        f"{'Promedio':>14} {'Peor caso':>14}"
    )
    random.seed(42)
    for tamaño in tamaños:
        muestra = elementos[:tamaño]
        titulos_unicos = list(dict.fromkeys(c.titulo.lower() for c in muestra))
        objetivos = random.sample(
            titulos_unicos, min(repeticiones, len(titulos_unicos))
        )

        mejor_caso = contar_comparaciones(muestra, muestra[0].titulo)
        promedio  = sum(
            contar_comparaciones(muestra, objetivo) for objetivo in objetivos  
        ) / len(objetivos)

        peor_caso = contar_comparaciones(
            muestra, "__titulo_inexistente_para_tp2__"
        )

        print(
            f"{tamaño:>12} {mejor_caso:>14}"
            f"{promedio:>12.2f} {peor_caso:>14}"
        )
if __name__ == "__main__":
    medir()