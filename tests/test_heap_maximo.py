from estructuras.heap_maximo import HeapMaximo
import unittest
from modelos.cancion import Cancion

class TestHeapMaximo(unittest.TestCase):
    def test_extrae_canciones_de_mayor_a_menor_popularidad(self):
        heap = HeapMaximo()
        canciones = [
            Cancion("Cuatro", "Artista", "Rock", 4, track_id="A"),
            Cancion("Nueve", "Artista", "Rock", 9, track_id="B"),
            Cancion("Seis", "Artista", "Rock", 6, track_id="C"),
        ]

        for cancion in canciones:
            heap.insertar(cancion)

        ids_extraidos = [
                heap.extraer_maximo().track_id,
                heap.extraer_maximo().track_id,
                heap.extraer_maximo().track_id,             
            ]

        self.assertEqual(ids_extraidos, ["B", "C", "A"])