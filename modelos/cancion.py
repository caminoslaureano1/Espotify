class Cancion:
    """Representa una canción dentro del catálogo."""

    def __init__(self, titulo: str, artista: str, genero: str, popularidad: float, track_id: str = "", duracion_ms: int = 0, generos: list[str] | None = None, artistas:list[str] | None = None ):
        self._titulo = titulo
        self._artista = artista
        self._genero = genero
        self._popularidad = popularidad
        self._track_id = track_id
        self._duracion_ms = duracion_ms
        self._generos = list(generos) if generos is not None else [genero]
        self._artistas = list(artistas) if artistas is not None else [nombre.strip() for nombre in artista.split(";")]

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

    @property
    def track_id(self) -> str:
        return self._track_id

    @property
    def duracion_ms(self) -> int:
        return self._duracion_ms
    
    @property
    def generos(self) -> list[str]:
        return list(self._generos)

    @property
    def artistas(self) -> list[str]:
        return list(self._artistas)

    def __repr__(self) -> str:
        return f"'{self._titulo}' - {self._artista} ({self._genero}) [Pop: {self._popularidad} | Duracion: {self._duracion_ms} | ID: {self._track_id}]"