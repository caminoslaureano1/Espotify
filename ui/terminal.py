from estructuras.arbol_general import ArbolGeneral
from servicios.catalogo import Catalogo
from estructuras.grafo_canciones import GrafoCanciones


class Terminal:
    """Interfaz de usuario en línea de comandos."""

    def __init__(self, catalogo: Catalogo, arbol_categorias: ArbolGeneral, grafo: GrafoCanciones) -> None:
        self._catalogo = catalogo
        self._arbol_categorias = arbol_categorias
        self._grafo = grafo
    def iniciar(self) -> None:
        while True:
            self._mostrar_menu()
            opcion = input("Opción: ").strip()
            if opcion == "1":
                self._buscar()
            elif opcion == "2":
                self._explorar_categorias()
            elif opcion == "3":
                self._ver_top()
            elif opcion == "4":
                self._listar()
            elif opcion == "5":
                self._filtrar()
            elif opcion == "6":
                self._recomendar()
            elif opcion == "0":
                print("¡Gracias por usar Espotify!")
                break
            else:
                print("Opción inválida. Intente de nuevo.\n")

    def _mostrar_menu(self) -> None:
        print("=" * 40)
        print("         ESPOTIFY TERMINAL (v2)")
        print("=" * 40)
        print("1. Buscar canción por título (AVL)")
        print("2. Explorar categorías (Árbol General)")
        print("3. Ver Top 10")
        print("4. Listar canciones")
        print("5. Filtrar por género")
        print("6. Recomendar canciones")
        print("0. Salir")
        print("-" * 40)

    def _buscar(self) -> None:
        titulo = input("Título a buscar: ").strip()
        resultado = self._catalogo.buscar(titulo)
        if resultado:
            print(f"\nEncontrada: {resultado}\n")
        else:
            print(f"\nNo se encontró la canción '{titulo}'.\n")

    def _explorar_categorias(self) -> None:
        arbol = self._arbol_categorias
        print("\nCategorías por amplitud (familias de géneros):")
        for familia in arbol.listar_hijos(arbol.raiz):
            print(f"  - {familia}")

        nombre = input("\nCategoría a explorar (Enter para volver): ").strip()
        if not nombre:
            print()
            return
        nodo = self._buscar_categoria(nombre)
        if nodo is None:
            print(f"\nNo existe la categoría '{nombre}'.\n")
            return

        if nodo.es_hoja():
            print(f"\n--- Top 10 de {nodo.dato} ---")
            for cancion in self._catalogo.top(10, genero=nodo.dato):
                print(f"- {cancion}")
        else:
            print()
            print("\n".join(arbol.dibujar(nodo)))
        print()

    def _buscar_categoria(self, nombre: str):
        """Búsqueda en el árbol general sin distinguir mayúsculas: O(n)."""
        objetivo = nombre.lower()
        for dato in self._arbol_categorias.amplitud():
            if dato.lower() == objetivo:
                return self._arbol_categorias.buscar(dato)
        return None

    def _ver_top(self) -> None:
        print("\n--- Top 10 por popularidad ---")
        for i, cancion in enumerate(self._catalogo.top(10), start=1):
            print(f"{i:2}. {cancion}")
        print()

    def _listar(self) -> None:
        print("\n--- Lista de Canciones ---")
        for cancion in self._catalogo.listar():
            print(f"- {cancion}")
        print()

    def _filtrar(self) -> None:
        genero = input("Género a filtrar: ").strip()
        resultados = self._catalogo.filtrar(genero)
        if resultados:
            print(f"\n--- Canciones de {genero} ---")
            for cancion in resultados:
                print(f"- {cancion}")
            print()
        else:
            print(f"\nNo hay canciones para el género '{genero}'.\n")

    def _recomendar(self) -> None:
        titulo = input("titulo de la cancion: ").strip()
        cancion = self._catalogo.buscar(titulo)

        if cancion is None:
            print(f"\nNo se encuentra la cancion'{titulo}'.\n")
            return

        recomendaciones = self._grafo.recomendaciones(cancion.track_id)

        if not recomendaciones:
            print(f"\nNo hay recomendaciones para '{cancion.titulo}' \n")
            return

        print(f"\n--- Recomendaciones para {cancion.titulo} ---")
        for recomendacion in recomendaciones:
            print(f"- {recomendacion}")
        print()