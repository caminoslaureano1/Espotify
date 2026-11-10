from modelos.cancion import Cancion

class GrafoCanciones:
    def __init__(self, canciones: list[Cancion]) -> None:
        self._canciones_por_id: dict[str, Cancion] = {}
        self._ids_por_artista: dict[str, set[str]] = {}
        self._ids_por_genero: dict[str, set[str]] = {}

        for cancion in canciones:
            self._canciones_por_id[cancion.track_id] = cancion

            for artista in cancion.artistas:
                if artista not in self._ids_por_artista:
                    self._ids_por_artista[artista] = set()
                self._ids_por_artista[artista].add(cancion.track_id)

            for genero in cancion.generos:
                if genero not in self._ids_por_genero:
                    self._ids_por_genero[genero] = set()
                self._ids_por_genero[genero].add(cancion.track_id)

    def recomendaciones(self, track_id:str) -> list[Cancion]:
        cancion_base = self._canciones_por_id.get(track_id)
        if cancion_base is None:
            return []

        candidatos: set[str] = set()

        for artista in cancion_base.artistas:
            candidatos.update(self._ids_por_artista.get(artista, set()))
        for genero in cancion_base.generos:
            candidatos.update(self._ids_por_genero.get(genero, set()))

        candidatos.discard(track_id)

        resultados = []
        for id_candidatos in candidatos:
            candidata = self._canciones_por_id[id_candidatos]
            artistas_compartidos = set(cancion_base.artistas) & set(candidata.artistas)
            generos_compartidos = set(cancion_base.generos) & set(candidata.generos) 
            comparte_artista = bool(artistas_compartidos)
            comparte_genero = bool(generos_compartidos)

            if comparte_artista and comparte_genero:
                costo = 1
            elif comparte_artista:
                costo = 2
            else:
                costo = 3
            resultados.append((costo, -candidata.popularidad, candidata.track_id, candidata))
        resultados.sort()
        return [resultado[3] for resultado in resultados[:10]]