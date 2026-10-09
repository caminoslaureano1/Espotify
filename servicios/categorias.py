from estructuras.arbol_general import ArbolGeneral

RAIZ = "Música"

# Familias de géneros → géneros (valores de `track_genre` del dataset de Kaggle).
# Cada uno de los 114 géneros del dataset aparece exactamente una vez.
JERARQUIA_GENEROS: dict[str, list[str]] = {
    "Rock": [
        "rock", "alt-rock", "alternative", "hard-rock", "psych-rock", "punk",
        "punk-rock", "grunge", "indie", "garage", "emo", "goth", "british",
        "j-rock", "rock-n-roll", "rockabilly",
    ],
    "Metal": [
        "metal", "heavy-metal", "black-metal", "death-metal", "metalcore",
        "grindcore", "hardcore", "industrial",
    ],
    "Pop": [
        "pop", "indie-pop", "power-pop", "synth-pop", "k-pop", "j-pop",
        "j-idol", "j-dance", "cantopop", "mandopop", "pop-film", "anime",
    ],
    "Electrónica": [
        "electronic", "edm", "electro", "house", "deep-house", "chicago-house",
        "progressive-house", "techno", "detroit-techno", "minimal-techno",
        "trance", "dubstep", "drum-and-bass", "breakbeat", "hardstyle", "idm",
        "trip-hop", "dance", "club", "disco",
    ],
    "Hip-Hop y R&B": ["hip-hop", "r-n-b"],
    "Jazz, Blues y Soul": ["jazz", "blues", "soul", "funk", "groove", "gospel"],
    "Latina": [
        "latin", "latino", "reggaeton", "salsa", "tango", "spanish", "brazil",
        "mpb", "samba", "pagode", "forro", "sertanejo",
    ],
    "Reggae y Caribe": ["reggae", "dancehall", "ska", "dub"],
    "Folk, Country y Acústica": [
        "folk", "country", "bluegrass", "honky-tonk", "acoustic",
        "singer-songwriter", "songwriter", "guitar",
    ],
    "Clásica e Instrumental": [
        "classical", "opera", "piano", "new-age", "ambient", "show-tunes",
    ],
    "Música del mundo": [
        "world-music", "afrobeat", "indian", "iranian", "turkish", "malay",
        "french", "german", "swedish",
    ],
    "Estados de ánimo": ["happy", "sad", "chill", "sleep", "study", "party", "romance"],
    "Infantil y Entretenimiento": ["children", "kids", "disney", "comedy"],
}


def construir_arbol_categorias(arbol: ArbolGeneral) -> ArbolGeneral:
    """Carga en `arbol` la jerarquía Música → familia → género."""
    raiz = arbol.insertar_raiz(RAIZ)
    for familia, generos in JERARQUIA_GENEROS.items():
        nodo_familia = arbol.agregar_hijo(raiz, familia)
        for genero in generos:
            arbol.agregar_hijo(nodo_familia, genero)
    return arbol
