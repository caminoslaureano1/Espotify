# Análisis TP3 Árbol Binario de Búsqueda (Espotify)

## 1. ¿Qué resolvimos?
Incorporamos un **árbol binario de búsqueda (BST)** para resolver la búsqueda de canciones por título de forma eficiente dentro de Espotify.

## 2. Clave de ordenamiento
Ordenamos por **título de la canción** en minúsculas (`lambda c: c.titulo.lower()`). Elegimos este atributo porque representa la forma principal en que el usuario final busca contenido dentro del catálogo musical.

## 3. Prueba del árbol
Salida al ejecutar `python algoritmos/probar_bst.py`: 
```text
Altura del árbol: 4

--- inorder (ordenado alfabéticamente) ---
 'Arrancacorazones' - A77AQUE (Punk Rock) [Pop: 8.9]
 'Crimen' - Gustavo Cerati (Rock) [Pop: 9.5]
 'De Música Ligera' - Soda Stereo (Rock) [Pop: 9.8]
 'Flaca' - Andrés Calamaro (Pop Rock) [Pop: 9.4]
 'Ji Ji Ji' - Patricio Rey (Rock) [Pop: 9.7]

--- preorder ---
 De Música Ligera
 Crimen
 Arrancacorazones
 Ji Ji Ji
 Flaca

--- postorder ---
 Arrancacorazones
 Crimen
 Flaca
 Ji Ji Ji
 De Música Ligera

--- búsquedas ---
Buscar 'crimen': 'Crimen' - Gustavo Cerati (Rock) [Pop: 9.5]
Buscar 'zzz': None 

test de medicion de tiempos
| N elementos | Secuencial (ms) | Árbol BST (ms) |
|---|---|---|
| 20 | 0.32990 | 0.00750 |