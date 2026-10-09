"""
arbol_general.py — Árbol General (N-ario)

Un árbol general donde cada nodo puede tener cualquier cantidad de hijos.
Se usa para representar jerarquías del dominio (en Espotify: géneros musicales).

Uso:
    from estructuras.arbol_general import NodoGeneral, ArbolGeneral

    arbol = ArbolGeneral()
    arbol.insertar_raiz("Música")
    nodo_rock = arbol.agregar_hijo(arbol.raiz, "Rock")   # padre como nodo
    arbol.agregar_hijo(nodo_rock, "alt-rock")
    arbol.agregar_hijo("Rock", "punk")                    # padre por su dato
"""

from collections import deque


class NodoGeneral:
    """Nodo de un árbol general: tiene un dato y una lista de hijos."""

    def __init__(self, dato):
        self.dato = dato
        self.hijos = []

    def es_hoja(self):
        return not self.hijos

    def __repr__(self):
        return f"Nodo({self.dato})"


class ArbolGeneral:
    """Árbol General (n-ario). Cada nodo puede tener 0 o más hijos.

    Se usa para representar jerarquías naturales del dominio, como:
    Música → Rock → alt-rock, hard-rock, punk
           → Electrónica → house, techno, trance
           → Latina → tango, salsa, reggaeton
    """

    def __init__(self):
        self.raiz = None

    # ==================== INSERCIÓN ====================

    def insertar_raiz(self, dato):
        """Crea el nodo raíz del árbol."""
        self.raiz = NodoGeneral(dato)
        return self.raiz

    def agregar_hijo(self, nodo_padre, dato):
        """Agrega un hijo al nodo padre y retorna el nuevo nodo creado.

        nodo_padre puede ser un NodoGeneral (O(1)) o el dato del padre,
        en cuyo caso primero se lo busca en el árbol (O(n)).
        """
        if self.raiz is None:
            raise ValueError("El árbol no tiene raíz. Use insertar_raiz primero.")
        if not isinstance(nodo_padre, NodoGeneral):
            valor_padre = nodo_padre
            nodo_padre = self.buscar(valor_padre)
            if nodo_padre is None:
                raise ValueError(f"No existe el nodo padre '{valor_padre}'.")

        nuevo_nodo = NodoGeneral(dato)
        nodo_padre.hijos.append(nuevo_nodo)
        return nuevo_nodo

    # ==================== BÚSQUEDA ====================

    def buscar(self, valor):
        """Busca un nodo cuyo dato == valor en todo el árbol (búsqueda en amplitud).

        Devuelve el nodo o None si no existe.
        """
        if self.raiz is None:
            return None

        cola = deque([self.raiz])
        while cola:
            actual = cola.popleft()
            if actual.dato == valor:
                return actual
            cola.extend(actual.hijos)
        return None

    def buscar_recursivo(self, valor, nodo=None):
        """Busca un nodo por profundidad (DFS). Devuelve el nodo o None."""
        if nodo is None:
            nodo = self.raiz
        if nodo is None:
            return None
        if nodo.dato == valor:
            return nodo
        for hijo in nodo.hijos:
            resultado = self.buscar_recursivo(valor, hijo)
            if resultado is not None:
                return resultado
        return None

    # ==================== RECORRIDOS ====================

    def amplitud(self):
        """Recorrido en amplitud (BFS): nivel por nivel, de arriba hacia abajo.

        Devuelve una lista con los datos en orden de nivel.
        """
        if self.raiz is None:
            return []

        resultado = []
        cola = deque([self.raiz])
        while cola:
            actual = cola.popleft()
            resultado.append(actual.dato)
            cola.extend(actual.hijos)
        return resultado

    def profundidad_preorder(self, nodo=None, resultado=None):
        """Recorrido en profundidad preorder (DFS): nodo → hijos de izquierda a derecha.

        Devuelve una lista con los datos en preorder.
        """
        if nodo is None:
            nodo = self.raiz
        if resultado is None:
            resultado = []
        if nodo is None:
            return resultado

        resultado.append(nodo.dato)
        for hijo in nodo.hijos:
            self.profundidad_preorder(hijo, resultado)
        return resultado

    def profundidad_postorder(self, nodo=None, resultado=None):
        """Recorrido en profundidad postorder (DFS): hijos → nodo.

        Devuelve una lista con los datos en postorder.
        """
        if nodo is None:
            nodo = self.raiz
        if resultado is None:
            resultado = []
        if nodo is None:
            return resultado

        for hijo in nodo.hijos:
            self.profundidad_postorder(hijo, resultado)
        resultado.append(nodo.dato)
        return resultado

    # ==================== INFORMACIÓN ====================

    def altura(self, nodo=None):
        """Altura máxima del árbol (o del subárbol dado)."""
        if nodo is None:
            nodo = self.raiz
        if nodo is None:
            return 0
        if not nodo.hijos:
            return 1
        return 1 + max(self.altura(hijo) for hijo in nodo.hijos)

    def cantidad_nodos(self, nodo=None):
        """Cantidad total de nodos en el árbol (o subárbol)."""
        if nodo is None:
            nodo = self.raiz
        if nodo is None:
            return 0
        return 1 + sum(self.cantidad_nodos(hijo) for hijo in nodo.hijos)

    def es_vacio(self):
        return self.raiz is None

    # ==================== UTILIDADES ====================

    def listar_hijos(self, nodo):
        """Retorna los datos de los hijos directos de un nodo."""
        return [hijo.dato for hijo in nodo.hijos]

    def obtener_niveles(self):
        """Retorna los datos organizados por nivel.

        Devuelve una lista de listas: [[raíz], [hijos_de_raíz], [nietos], ...]
        """
        if self.raiz is None:
            return []

        niveles = []
        nivel_actual = [self.raiz]
        while nivel_actual:
            niveles.append([n.dato for n in nivel_actual])
            siguiente = []
            for nodo in nivel_actual:
                siguiente.extend(nodo.hijos)
            nivel_actual = siguiente
        return niveles

    def dibujar(self, nodo=None, prefijo=""):
        """Devuelve las líneas del árbol con conectores (├──, └──), en preorder."""
        if nodo is None:
            nodo = self.raiz
        if nodo is None:
            return []
        lineas = [str(nodo.dato)] if not prefijo else []
        for i, hijo in enumerate(nodo.hijos):
            ultimo = i == len(nodo.hijos) - 1
            lineas.append(prefijo + ("└── " if ultimo else "├── ") + str(hijo.dato))
            lineas.extend(self.dibujar(hijo, prefijo + ("    " if ultimo else "│   ")))
        return lineas

    def __repr__(self):
        if self.raiz is None:
            return "Árbol General vacío"
        return f"Árbol General (raíz: {self.raiz.dato}, altura: {self.altura()})"


# ==================== EJEMPLO DE USO ====================

if __name__ == "__main__":
    # Subconjunto de la jerarquía de géneros de Espotify
    arbol = ArbolGeneral()
    arbol.insertar_raiz("Música")

    rock = arbol.agregar_hijo(arbol.raiz, "Rock")
    electronica = arbol.agregar_hijo(arbol.raiz, "Electrónica")
    latina = arbol.agregar_hijo(arbol.raiz, "Latina")

    arbol.agregar_hijo(rock, "alt-rock")
    arbol.agregar_hijo(rock, "hard-rock")
    arbol.agregar_hijo(rock, "punk")

    arbol.agregar_hijo(electronica, "house")
    arbol.agregar_hijo(electronica, "techno")

    arbol.agregar_hijo(latina, "tango")
    arbol.agregar_hijo("Latina", "salsa")  # padre indicado por su dato

    print("=== Árbol General de Categorías ===")
    print("Raíz:", arbol.raiz.dato)
    print("Altura:", arbol.altura())
    print("Cantidad de nodos:", arbol.cantidad_nodos())
    print()
    print("\n".join(arbol.dibujar()))
    print()

    print("--- Recorrido en amplitud ---")
    print(arbol.amplitud())
    print()

    print("--- Recorrido en profundidad (preorder) ---")
    print(arbol.profundidad_preorder())
    print()

    print("--- Recorrido en profundidad (postorder) ---")
    print(arbol.profundidad_postorder())
    print()

    print("--- Niveles ---")
    for i, nivel in enumerate(arbol.obtener_niveles()):
        print(f"  Nivel {i}: {nivel}")
    print()

    print("--- Hijos de 'Rock' ---")
    nodo_rock = arbol.buscar("Rock")
    if nodo_rock:
        print(arbol.listar_hijos(nodo_rock))

    print()
    print("--- Buscar 'tango' ---")
    print("Encontrado:", arbol.buscar("tango"))
    print("--- Buscar 'opera' ---")
    print("Encontrado:", arbol.buscar("opera"))
