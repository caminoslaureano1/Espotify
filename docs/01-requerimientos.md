# Espotify - Propuesta (TP0)

Sistema de recomendación de música que permite buscar, filtrar y descubrir canciones afines a partir de una pista seleccionada.

## 1. Dominio elegido y justificación
Música. El dominio cuenta con datasets públicos (e.g., datos de Spotify en CSV/JSON con metadatos de artista, género, rating y BPM).
Encaja perfectamente con la cursada:
- **BST/AVL:** Búsqueda eficiente por título.
- **Heap:** Generación del Top-N por popularidad.
- **Grafos:** Modelado de relaciones de similitud entre canciones.

## 2. Problema que resuelve
"Termino de escuchar una canción que me encanta y no sé qué tema similar poner a continuación."

## 3. Usuario objetivo
Lucas, un estudiante de 23 años apasionado por descubrir música indie/rock que busca recomendaciones precisas dentro de un catálogo seleccionado.

## 4. Funcionalidades iniciales
| ID | Funcionalidad |
|---|---|
| F1 | Buscar canción por título |
| F2 | Listar canciones por género |
| F3 | Ver Top 10 canciones más escuchadas |
| F4 | Ver canciones relacionadas a una pista dada |
| F5 | Sugerir camino de reproducción a partir de una canción |

## 5. Ejemplo de uso (Interfaz simulada)
========================================
 ESPOTIFY TERMINAL (v1)
========================================
1. Buscar canción
2. Listar por género
3. Ver Top 10
4. Ver relacionadas
0. Salir
----------------------------------------
Opción: 1
Título a buscar: De Música Ligera
Encontrada: De Música Ligera - Soda Stereo (Rock) [Rating: 9.8]

## 6. Requerimientos
| ID | Requerimiento | Tipo |
|---|---|---|
| RF01 | El sistema debe permitir buscar una canción por título | Funcional |
| RF02 | El sistema debe filtrar canciones por género | Funcional |
| RF03 | El sistema debe mostrar el Top N de canciones | Funcional |
| RNF01| Las búsquedas deben resolverse con tiempos de respuesta aceptables con +1000 elementos | No funcional |

## 7. Fuera de alcance
- Autenticación de usuarios.
- Reproducción de audio real.