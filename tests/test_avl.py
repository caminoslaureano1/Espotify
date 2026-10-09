import unittest
from estructuras.avl import AVL


def clave(x):
    return x


class TestAVL(unittest.TestCase):

    def construir(self, valores):
        arbol = AVL()
        for v in valores:
            arbol.insertar(v, clave=clave)
        return arbol

    def assert_balanceado(self, nodo):
        """Verifica factor de balance en [-1, 1] y alturas correctas en todo el árbol."""
        if nodo is None:
            return 0
        izq = self.assert_balanceado(nodo.izquierdo)
        der = self.assert_balanceado(nodo.derecho)
        self.assertLessEqual(abs(izq - der), 1)
        self.assertEqual(nodo.altura, 1 + max(izq, der))
        return nodo.altura

    def test_datos_ordenados_altura_4(self):
        arbol = self.construir("ABCDEFGHIJ")
        self.assertEqual(arbol.altura(), 4)
        self.assertEqual(arbol.raiz.dato, "D")
        self.assertEqual(arbol.inorder(), list("ABCDEFGHIJ"))
        self.assert_balanceado(arbol.raiz)

    def test_rotacion_izquierda_izquierda(self):
        self.assertEqual(self.construir([3, 2, 1]).preorder(), [2, 1, 3])

    def test_rotacion_derecha_derecha(self):
        self.assertEqual(self.construir([1, 2, 3]).preorder(), [2, 1, 3])

    def test_rotacion_izquierda_derecha(self):
        self.assertEqual(self.construir([3, 1, 2]).preorder(), [2, 1, 3])

    def test_rotacion_derecha_izquierda(self):
        self.assertEqual(self.construir([1, 3, 2]).preorder(), [2, 1, 3])

    def test_10000_ordenados_altura_logaritmica(self):
        arbol = self.construir(range(10_000))
        self.assertEqual(arbol.altura(), 14)
        self.assert_balanceado(arbol.raiz)

    def test_buscar(self):
        arbol = self.construir("ABCDEFGHIJ")
        self.assertEqual(arbol.buscar("F", clave=clave), "F")
        self.assertIsNone(arbol.buscar("Z", clave=clave))

    def test_duplicados_se_ignoran(self):
        arbol = self.construir([5, 5, 5])
        self.assertEqual(len(arbol), 1)


if __name__ == "__main__":
    unittest.main()
