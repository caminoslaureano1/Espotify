import unittest
from servicios.catalogo import Catalogo


class TestCatalogo(unittest.TestCase):

    def setUp(self):
        self.catalogo = Catalogo()
        self.catalogo.cargar_desde_json("datos/canciones.json")

    def test_buscar_existente(self):
        cancion = self.catalogo.buscar("de música ligera")
        self.assertIsNotNone(cancion)
        self.assertEqual(cancion.artista, "Soda Stereo")

    def test_buscar_inexistente(self):
        self.assertIsNone(self.catalogo.buscar("cancion no existente"))

    def test_listar(self):
        canciones = self.catalogo.listar()
        self.assertGreaterEqual(len(canciones), 20)

    def test_filtrar_genero(self):
        rock_items = self.catalogo.filtrar("rock")
        self.assertTrue(all(c.genero.lower() == "rock" for c in rock_items))

    def test_top_ordenado_por_popularidad(self):
        canciones = self.catalogo.top(5)
        popularidad = [c.popularidad for c in canciones]

        self.assertEqual(len(canciones), 5)
        self.assertEqual(popularidad, sorted(popularidad, reverse=True))

    def test_top_ordenado_por_genero(self):
        canciones = self.catalogo.top(5, genero ="rock")

        self.assertEqual(len(canciones), 5)
        self.assertTrue(
            all("rock" in [g.lower() for g in c.generos] for c in canciones)
        )



if __name__ == "__main__":
    unittest.main()