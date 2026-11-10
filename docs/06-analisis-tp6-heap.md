# Analisis del heap maximo (TP6)

Sea 'n' la cantidad de canciones del catalogo, "m" la cantidad de canciones candidatas y 'k' la cantidad de resultados solicitados.

sea r = min(k, m) la cantidad de canciones que realmente se devuelve.

- Insertar una cancion en el heap cuesta 'O(log m)' en el peor caso.
- Construir el heap insertando las 'm' canciones cuesta 'O(m log m)' en el peor caso.
- Extraer una cancion de maximo popularidad cuesta 'O(log m)'.
- Extraer las r canciones del Top cuesta 'O(r log m)'.
- El heap necesita 'O(m)' espacio.

Por lo tanto, obtener el Top cuesta 'O(m log m + r log m)', ademas del filtrado opcional por genero, que recorre el catalogo y cuesta 'O(n)'. Sin filtro, 'm = n'; entonces el costo es 'O(n + m log m + r log m)'.

EL heap mantiene la cancion de mayor popularidad en la raiz. Cada insercion puede subir el elemento por la altura del arbol y cada extraccion puede bajarlo; como la altura de un heap binario es 'O(log m)', ambas operaciones tienen ese costo en el peor caso.