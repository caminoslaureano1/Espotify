# Diagrama de Clases (Boceto inicial TP0 / Actualizado TP1)

```mermaid
classDiagram
class Cancion {
    -titulo: str
    -artista: str
    -genero: str
    -popularidad: float
    +titulo() str
    +artista() str
    +genero() str
    +popularidad() float
    +repr() str
}

class Catalogo {
    -elementos: list[Cancion]
    +cargar_desde_json(ruta: str) None
    +buscar(titulo: str) Cancion
    +listar() list[Cancion]
    +filtrar(genero: str) list[Cancion]
}

class Terminal {
    -catalogo: Catalogo
    +iniciar() None
}

Terminal --> Catalogo: usa
Catalogo "1" o-- "*" Cancion: contiene