import csv
import json
from modelos.cancion import Cancion


class Catalogo:
    """Lógica de negocio: carga y gestión de operaciones sobre canciones."""

    def __init__(self) -> None:
        self._elementos: list[Cancion] = []

    def cargar_desde_json(self, ruta: str) -> None:
        """Carga canciones desde un archivo JSON."""
        with open(ruta, encoding="utf-8") as archivo:
            datos = json.load(archivo)
            for item in datos:
                cancion = Cancion(
                    titulo=item["titulo"],
                    artista=item["artista"],
                    genero=item["genero"],
                    popularidad=float(item["popularidad"]),
                )
                self._elementos.append(cancion)

    def cargar_desde_csv(self, ruta: str) -> None:
        """Carga canciones desde un dataset público en formato CSV."""
        with open(ruta, mode="r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                # Mapeo flexible según las columnas habituales de Kaggle
                titulo = fila.get("track_name") or fila.get("titulo") or "Desconocido"
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

                # Normalización del score de popularidad (de 0-100 a escala 0-10)
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

                cancion = Cancion(
                    titulo=titulo.strip(),
                    artista=artista.strip(),
                    genero=genero.strip(),
                    popularidad=popularidad,
                )
                self._elementos.append(cancion)

    def buscar(self, titulo: str) -> Cancion | None:
        """Búsqueda exacta por título (case-insensitive)."""
        titulo_normalizado = titulo.strip().lower()
        for cancion in self._elementos:
            if cancion.titulo.lower() == titulo_normalizado:
                return cancion
        return None

    def listar(self, limite: int = 20) -> list[Cancion]:
        """Devuelve una muestra de elementos para no saturar la terminal."""
        return self._elementos[:limite]

    def filtrar(self, genero: str) -> list[Cancion]:
        genero_normalizado = genero.strip().lower()
        return [c for c in self._elementos if c.genero.lower() == genero_normalizado]

    def __len__(self) -> int:
        return len(self._elementos)