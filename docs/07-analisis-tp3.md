# Análisis TP3 Árbol Binario de Búsqueda (Espotify)

## 1. ¿Qué resolvimos?
Incorporamos un **árbol binario de búsqueda (BST)** para resolver la búsqueda de canciones por título de forma eficiente dentro de Espotify.

## 2. Clave de ordenamiento
Ordenamos por **título de la canción** en minúsculas (`lambda c: c.titulo.lower()`). Elegimos este atributo porque representa la forma principal en que el usuario final busca contenido dentro del catálogo musical.

## 3. Prueba del árbol
Salida al ejecutar `python algoritmos/probar_bst.py`: 
""
========================================
         ESPOTIFY TERMINAL (v1)
========================================
1. Buscar canción por título
2. Listar todas las canciones
3. Filtrar por género
0. Salir
----------------------------------------
Opción: 1
Título a buscar: material girl

Encontrada: 'Material Girl' - Kris Bowers (jazz) [Pop: 5.9]

========================================
         ESPOTIFY TERMINAL (v1)
========================================
1. Buscar canción por título
2. Listar todas las canciones
3. Filtrar por género
0. Salir
---------------------------------------- "" 
