import unittest
from modelos.cancion import Cancion
from estructuras.grafo_canciones import GrafoCanciones

class TestGrafoCanciones(unittest.TestCase):
    def test_orden_recomendaciones_por_costo(self):
        base = Cancion("Base", "Luna", "Rock", 5, track_id="A")
        solo_genero = Cancion("B", "Sol", "Rock", 10, track_id="B")
        solo_artista = Cancion("C", "Luna", "Pop", 9, track_id="C")
        ambos =  Cancion("D", "Luna", "Rock", 1, track_id="D")

        grafo = GrafoCanciones([base, solo_genero, solo_artista, ambos])
        recomendaciones = grafo.recomendaciones("A")

        self.assertEqual(
            [c.track_id for c in recomendaciones],
            ["D", "C", "B"],
        )

    def test_desempate_por_popularidad(self):
        base = Cancion("Base", "Luna", "Rock", 5, track_id="A")
        menos_popular = Cancion("B", "Luna", "Rock", 2, track_id="B")
        mas_popular = Cancion("C", "Luna", "Rock", 9, track_id="C")

        grafo = GrafoCanciones([base, menos_popular, mas_popular])
        recomendaciones = grafo.recomendaciones("A")

        self.assertEqual(
            [c.track_id for c in recomendaciones],
            ["C", "B"],
        )

    def test_id_inexistentes_devuelve_lista_vacio(self):
        grafo = GrafoCanciones([])
        self.assertEqual(grafo.recomendaciones("no-existe"), []) 

    def test_recomienda_por_artista_en_colaboracion(self):
        base = Cancion("Base", "Luna;Sol", "Rock", 5, track_id="A")
        comparte_artista = Cancion("OTra", "Sol;Nube", "Pop", 5, track_id="B")
        solo_genero = Cancion("Rock", "Rio","Rock", 5, track_id="C")
        
        grafo = GrafoCanciones([base, comparte_artista, solo_genero])
        recomendaciones = grafo.recomendaciones("A")

        self.assertEqual(
            [c.track_id for c in recomendaciones],
            ["B", "C"],
        )

    def test_recomienda_por_genero_secundario(self):
        base = Cancion(
            "Base", "Luna", "acoustic", 5,
            track_id="A", generos=["acoustic", "j-pop"]
        )
        relacionada = Cancion(
            "Otra", "Sol", "rock", 6,
            track_id="B", generos=["rock", "j-pop"]
        )

        grafo = GrafoCanciones([base, relacionada])
        recomendaciones = grafo.recomendaciones("A")

        self.assertEqual([c.track_id for c in recomendaciones], ["B"])
        