import csv
import json
from estructuras.heap_maximo import HeapMaximo
from estructuras.avl import AVL
from modelos.cancion import Cancion


class Catalogo:

    def __init__(self) -> None:
        self._elementos: list[Cancion] = []
        self._arbol_titulos: AVL = AVL()

    def _indexar_arbol(self) -> None:
        """Pobla el árbol AVL ordenando por título en minúsculas."""
        self._arbol_titulos = AVL()
        for cancion in self._elementos:
            self._arbol_titulos.insertar(
                cancion, clave=lambda c: c.titulo.lower()
            )

    def cargar_desde_json(self, ruta: str) -> None:
        with open(ruta, encoding="utf-8") as archivo:
            datos = json.load(archivo)
            for item in datos:
                self._elementos.append(
                    Cancion(
                        titulo=item["titulo"],
                        artista=item["artista"],
                        genero=item["genero"],
                        popularidad=float(item["popularidad"]),
                    )
                )
        self._indexar_arbol()

    def cargar_desde_csv(self, ruta: str) -> None:
        with open(ruta, mode="r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            canciones_por_id = {}
            for fila in lector:
                track_id = fila.get("track_id", "").strip()
                duracion = int(fila.get("duration_ms") or 0)
                titulo = (
                    fila.get("track_name") or fila.get("titulo") or "Desconocido"
                )
                artista = (
                    fila.get("artists")
                    or fila.get("artist_name")
                    or fila.get("artista")
                    or "Desconocido"
                )
                genero = (
                    fila.get("track_genre")
                    or fila.get("genre")
                    or fila.get("genero")
                    or "Varios"
                )
                # Kaggle ('popularity') usa escala 0-100; 'popularidad' ya viene en 0-10
                if fila.get("popularity"):
                    popularidad = round(float(fila["popularity"]) / 10.0, 1)
                else:
                    popularidad = round(float(fila.get("popularidad") or 0), 1)

                if track_id not in canciones_por_id:
                    canciones_por_id[track_id] = {
                        "titulo": titulo,
                        "artista": artista,
                        "duracion": duracion,
                        "genero": set(),
                        "suma_popularidad": 0.0,
                        "cantidad_popularidades": 0,
                    }

                datos = canciones_por_id[track_id]
                datos["genero"].add(genero.strip())
                datos["suma_popularidad"] += popularidad
                datos["cantidad_popularidades"] += 1

        for track_id, datos in canciones_por_id.items():
            popularidad_promedio = round(datos["suma_popularidad"] / datos["cantidad_popularidades"], 1)
            self._elementos.append(
                Cancion(
                    titulo=datos["titulo"],
                    artista=datos["artista"],
                    genero=sorted(datos["genero"])[0],
                    popularidad=popularidad_promedio,
                    track_id=track_id,
                    duracion_ms=datos["duracion"],
                    generos=sorted(datos["genero"]),
                )
            )  
               
        self._indexar_arbol()

    def buscar_secuencial(self, titulo: str) -> Cancion | None:
        """Búsqueda lineal O(n)."""
        target = titulo.strip().lower()
        for c in self._elementos:
            if c.titulo.lower() == target:
                return c
        return None

    def buscar_avl(self, titulo: str) -> Cancion | None:
        """Búsqueda por árbol AVL: O(log n) garantizado."""
        return self._arbol_titulos.buscar(
            titulo.strip().lower(), clave=lambda c: c.titulo.lower()
        )

    # El método 'buscar' por defecto usa el árbol AVL
    def buscar(self, titulo: str) -> Cancion | None:
        return self.buscar_avl(titulo)

    def listar(self, limite: int = 20) -> list[Cancion]:
        return self._elementos[:limite]

    def altura_indice(self) -> int:
        """Altura del árbol AVL que indexa los títulos."""
        return self._arbol_titulos.altura()

    def top(self, cantidad: int = 10, genero: str | None = None) -> list[Cancion]:
        """Devuelve las canciones más populares, opcionalmente filtradas por género, 
            usando un heap máximo."""

       
        candidatas = self.filtrar(genero) if genero else self._elementos
        heap = HeapMaximo()
        for cancion in candidatas:
            heap.insertar(cancion)
        resultado = []
        cantidad_a_devolver = min(cantidad, len(candidatas))

        for _ in range(cantidad_a_devolver):
            resultado.append(heap.extraer_maximo())

        return resultado

    def filtrar(self, genero: str) -> list[Cancion]:
        target = genero.strip().lower()
        return [c for c in self._elementos if any(g.lower() == target for g in c.generos)]

    def __len__(self) -> int:
        return len(self._elementos)