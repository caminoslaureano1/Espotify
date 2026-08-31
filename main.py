from servicios.catalogo import Catalogo
from ui.terminal import Terminal


def main() -> None:
    catalogo = Catalogo()

    # Carga desde el dataset de Kaggle
    ruta_dataset = "datos/canciones-kreagle.csv.csv"
    catalogo.cargar_desde_csv(ruta_dataset)

    print(
        f"Se cargaron exitosamente {len(catalogo)} canciones desde '{ruta_dataset}'."
    )

    terminal = Terminal(catalogo)
    terminal.iniciar()


if __name__ == "__main__":
    main()