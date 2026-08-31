class Cancion:
    """Representa una canción dentro del catálogo."""

    def __init__(self, titulo: str, artista: str, genero: str, popularidad: float):
        self._titulo = titulo
        self._artista = artista
        self._genero = genero
        self._popularidad = popularidad

    @property
    def titulo(self) -> str:
        return self._titulo

    @property
    def artista(self) -> str:
        return self._artista

    @property
    def genero(self) -> str:
        return self._genero

    @property
    def popularidad(self) -> float:
        return self._popularidad

    def __repr__(self) -> str:
        return f"'{self._titulo}' - {self._artista} ({self._genero}) [Pop: {self._popularidad}]"