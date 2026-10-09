import csv
import unittest
from estructuras.arbol_general import ArbolGeneral
from servicios.categorias import JERARQUIA_GENEROS, construir_arbol_categorias


class TestArbolGeneral(unittest.TestCase):

    def setUp(self):
        self.arbol = ArbolGeneral()
        self.arbol.insertar_raiz("Música")
        rock = self.arbol.agregar_hijo(self.arbol.raiz, "Rock")
        self.arbol.agregar_hijo(self.arbol.raiz, "Latina")
        self.arbol.agregar_hijo(rock, "punk")
        self.arbol.agregar_hijo("Latina", "tango")

    def test_recorridos(self):
        self.assertEqual(self.arbol.amplitud(), ["Música", "Rock", "Latina", "punk", "tango"])
        self.assertEqual(self.arbol.profundidad_preorder(), ["Música", "Rock", "punk", "Latina", "tango"])
        self.assertEqual(self.arbol.profundidad_postorder(), ["punk", "Rock", "tango", "Latina", "Música"])

    def test_buscar(self):
        self.assertEqual(self.arbol.buscar("tango").dato, "tango")
        self.assertEqual(self.arbol.buscar_recursivo("punk").dato, "punk")
        self.assertIsNone(self.arbol.buscar("opera"))

    def test_agregar_hijo_errores(self):
        with self.assertRaises(ValueError):
            ArbolGeneral().agregar_hijo(None, "Rock")
        with self.assertRaises(ValueError):
            self.arbol.agregar_hijo("Jazz", "bebop")

    def test_altura_y_cantidad(self):
        self.assertEqual(self.arbol.altura(), 3)
        self.assertEqual(self.arbol.cantidad_nodos(), 5)


class TestCategorias(unittest.TestCase):

    def test_jerarquia_cubre_todos_los_generos_del_dataset(self):
        with open("datos/canciones-kreagle.csv.csv", encoding="utf-8") as archivo:
            generos_dataset = {fila["track_genre"] for fila in csv.DictReader(archivo)}
        generos_jerarquia = [g for generos in JERARQUIA_GENEROS.values() for g in generos]
        self.assertEqual(len(generos_jerarquia), len(set(generos_jerarquia)))
        self.assertEqual(set(generos_jerarquia), generos_dataset)

    def test_arbol_categorias(self):
        arbol = construir_arbol_categorias(ArbolGeneral())
        self.assertEqual(arbol.altura(), 3)
        self.assertEqual(arbol.cantidad_nodos(), 1 + 13 + 114)
        self.assertTrue(arbol.buscar("tango").es_hoja())


if __name__ == "__main__":
    unittest.main()
