from servicios.catalogo import Catalogo


class Terminal:
    """Interfaz de usuario en línea de comandos."""

    def __init__(self, catalogo: Catalogo) -> None:
        self._catalogo = catalogo

    def iniciar(self) -> None:
        while True:
            self._mostrar_menu()
            opcion = input("Opción: ").strip()
            if opcion == "1":
                self._buscar()
            elif opcion == "2":
                self._listar()
            elif opcion == "3":
                self._filtrar()
            elif opcion == "0":
                print("¡Gracias por usar Espotify!")
                break
            else:
                print("Opción inválida. Intente de nuevo.\n")

    def _mostrar_menu(self) -> None:
        print("=" * 40)
        print("         ESPOTIFY TERMINAL (v1)")
        print("=" * 40)
        print("1. Buscar canción por título")
        print("2. Listar todas las canciones")
        print("3. Filtrar por género")
        print("0. Salir")
        print("-" * 40)

    def _buscar(self) -> None:
        titulo = input("Título a buscar: ").strip()
        resultado = self._catalogo.buscar(titulo)
        if resultado:
            print(f"\nEncontrada: {resultado}\n")
        else:
            print(f"\nNo se encontró la canción '{titulo}'.\n")

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