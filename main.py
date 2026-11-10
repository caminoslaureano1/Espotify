from estructuras.arbol_general import ArbolGeneral
from servicios.catalogo import Catalogo
from servicios.categorias import construir_arbol_categorias
from ui.terminal import Terminal
from estructuras.grafo_canciones import GrafoCanciones


def main() -> None:
    # El catálogo indexa los títulos en un árbol AVL (opción "Buscar")
    catalogo = Catalogo()

    # Carga desde el dataset de Kaggle
    ruta_dataset = "datos/canciones-kreagle.csv.csv"
    catalogo.cargar_desde_csv(ruta_dataset)

    print(
        f"Se cargaron exitosamente {len(catalogo)} canciones desde '{ruta_dataset}' "
        f"(altura del índice AVL: {catalogo.altura_indice()})."
    )

    # Jerarquía Música → familia → género (opción "Explorar categorías")
    arbol_categorias = ArbolGeneral()
    construir_arbol_categorias(arbol_categorias)
    grafo = GrafoCanciones(catalogo.listar(limite=len(catalogo)))

    terminal = Terminal(catalogo, arbol_categorias, grafo)
    terminal.iniciar()

if __name__ == "__main__":
    main()
