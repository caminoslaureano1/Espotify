import os
import sys

# Permitir importaciones relativas
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from estructuras.arbol_binario import ArbolBST
from modelos.cancion import Cancion


def main():
    arbol = ArbolBST()

    canciones_prueba = [
        Cancion("De Música Ligera", "Soda Stereo", "Rock", 9.8),
        Cancion("Crimen", "Gustavo Cerati", "Rock", 9.5),
        Cancion("Ji Ji Ji", "Patricio Rey", "Rock", 9.7),
        Cancion("Arrancacorazones", "A77AQUE", "Punk Rock", 8.9),
        Cancion("Flaca", "Andrés Calamaro", "Pop Rock", 9.4),
    ]

    for c in canciones_prueba:
        arbol.insertar(c, clave=lambda x: x.titulo.lower())

    print("Altura del árbol:", arbol.altura())

    print("\n--- inorder (ordenado alfabéticamente) ---")
    for c in arbol.inorder():
        print(" ", c)

    print("\n--- preorder ---")
    for c in arbol.preorder():
        print(" ", c.titulo)

    print("\n--- postorder ---")
    for c in arbol.postorder():
        print(" ", c.titulo)

    print("\n--- búsquedas ---")
    encontrada = arbol.buscar("crimen", clave=lambda x: x.titulo.lower())
    print("Buscar 'crimen':", encontrada)
    no_encontrada = arbol.buscar("zzz", clave=lambda x: x.titulo.lower())
    print("Buscar 'zzz':", no_encontrada)


if __name__ == "__main__":
    main()