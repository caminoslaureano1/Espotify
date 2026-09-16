import csv
import json
from estructuras.arbol_binario import ArbolBST
from modelos.cancion import Cancion


class Catalogo:

    def __init__(self) -> None:
        self._elementos: list[Cancion] = []
        self._arbol_titulos: ArbolBST = ArbolBST()

    def _indexar_arbol(self) -> None:
        """Pobla el árbol BST ordenando por título en minúsculas."""
        self._arbol_titulos = ArbolBST()
        for cancion in self._elementos:
            self._arbol_titulos.insertar(
                cancion, clave=lambda c: c.titulo.lower()
            )

    def cargar_desde_json(self, ruta: str) -> None:
        with open(ruta, encoding="utf-8") as archivo:
            datos = json.load(archivo)
            for item in datos:
                self._elementos.append(
                    Cancion(
                        titulo=item["titulo"],
                        artista=item["artista"],
                        genero=item["genero"],
                        popularidad=float(item["popularidad"]),
                    )
                )
        self._indexar_arbol()

    def cargar_desde_csv(self, ruta: str) -> None:
        with open(ruta, mode="r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                titulo = (
                    fila.get("track_name") or fila.get("titulo") or "Desconocido"
                )
                artista = (
                    fila.get("artists")
                    or fila.get("artist_name")
                    or fila.get("artista")
                    or "Desconocido"
                )
                genero = (
                    fila.get("track_genre")
                    or fila.get("genre")
                    or fila.get("genero")
                    or "Varios"
                )
                popularidad_raw = float(
                    fila.get("popularity") or fila.get("popularidad") or 0
                )
                popularidad = round(
                    (
                        popularidad_raw / 10.0
                        if popularidad_raw > 10
                        else popularidad_raw
                    ),
                    1,
                )

                self._elementos.append(
                    Cancion(
                        titulo=titulo.strip(),
                        artista=artista.strip(),
                        genero=genero.strip(),
                        popularidad=popularidad,
                    )
                )
        self._indexar_arbol()

    def buscar_secuencial(self, titulo: str) -> Cancion | None:
        """Búsqueda lineal O(n)."""
        target = titulo.strip().lower()
        for c in self._elementos:
            if c.titulo.lower() == target:
                return c
        return None

    def buscar_arbol(self, titulo: str) -> Cancion | None:
        """Búsqueda optimizada por árbol BST O(log n)."""
        return self._arbol_titulos.buscar(
            titulo.strip().lower(), clave=lambda c: c.titulo.lower()
        )

    # Mantener el método 'buscar' por defecto usando el árbol BST
    def buscar(self, titulo: str) -> Cancion | None:
        return self.buscar_arbol(titulo)

    def listar(self, limite: int = 20) -> list[Cancion]:
        return self._elementos[:limite]

    def filtrar(self, genero: str) -> list[Cancion]:
        target = genero.strip().lower()
        return [c for c in self._elementos if c.genero.lower() == target]

    def __len__(self) -> int:
        return len(self._elementos)