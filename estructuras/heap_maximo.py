from modelos.cancion import Cancion

class HeapMaximo():
    def __init__(self):
        self._elementos:  list[Cancion] = []

    def insertar(self, cancion: Cancion) ->None:
        self._elementos.append(cancion)
        indice = len(self._elementos)  - 1

        while indice > 0:
            indice_padre = (indice - 1) // 2

            if self._elementos[indice_padre].popularidad >= self._elementos[indice].popularidad:
                break 

            self._elementos[indice_padre], self._elementos[indice] = (
                self._elementos[indice],
                self._elementos[indice_padre],
            )
            indice = indice_padre

    def extraer_maximo(self) -> Cancion:
        if not self._elementos:
            raise IndexError("No hay canciones en el heap")

        maximo = self._elementos[0]
        ultimo = self._elementos.pop()

        if self._elementos:
            self._elementos[0] = ultimo
            indice = 0

            while True:
                hijo_izquierdo = 2 * indice + 1
                hijo_derecho = 2* indice + 2
                indice_mayor = indice

                if (
                    hijo_izquierdo <len(self._elementos)
                    and self._elementos[hijo_izquierdo].popularidad
                    > self._elementos[indice_mayor].popularidad
                ):
                    indice_mayor = hijo_izquierdo

                if (
                    hijo_derecho < len (self._elementos)
                    and self._elementos[hijo_derecho].popularidad
                    > self._elementos[indice_mayor].popularidad
                ):
                    indice_mayor = hijo_derecho

                if indice_mayor == indice:
                    break

                self._elementos[indice], self._elementos[indice_mayor] = (
                    self._elementos[indice_mayor],
                    self._elementos[indice],
                )
                indice = indice_mayor

        return maximo