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


if __name__ == "__main__":
    unittest.main()