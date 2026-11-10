# Modelo del grafo

Cada nodo representa una cancion y se identifica mediante su track_id dos canciones se relacionan si comparten al menos un artista o un genero. La relacion es no orientada: si una cancion se relaciona con otra la relacion tambien vale en sentido inverso. El costo es 1 si comparten artista y genero, 2 si comparten solo artista y 3 si comparten solo genero.

# Representacion en el programa


Las relaciones no se guardan como una lista permanente de conexiones. Cuando se piden recomendaciones, el grafo consulta dos indices artista -> IDs de canciones y genero -> IDs de canciones. reune las canciones candidatas, calcula el costo de cada relacion y devuelve hasta 10 resultados. asi evita comparar las canciones elegida contra todo el catalogo.

# Orden de recomendaciones 

Las canciones se ordenan primero por costo de relacion ascendente (1, 2 ,3). Cuando varias tienen el mismo costo, se prioriza la de mayor popularidad. sI tambien empatan en popularidad, se usa el track_id para obtener un orden estable. Si no existen canciones relacionadas o el ID consultado no esta en el catalogo, se devuelve una lista vacia.