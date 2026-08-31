# Casos de Uso (TP1)

## Caso de Uso 1: Buscar Canción por Título
- **Actor:** Usuario
- **Precondición:** El catálogo de datos está cargado correctamente.
- **Flujo Principal:**
  1. El usuario selecciona la opción "1" en el menú.
  2. El sistema solicita el título de la canción.
  3. El usuario ingresa el nombre (ej. "Crimen").
  4. El sistema realiza la búsqueda e imprime los detalles de la canción encontrada.
- **Flujo Alternativo:**
  - Si la canción no se encuentra, el sistema muestra un mensaje indicando que no hay coincidencias.

## Caso de Uso 2: Listar Canciones
- **Actor:** Usuario
- **Precondición:** El catálogo está cargado.
- **Flujo Principal:**
  1. El usuario selecciona la opción "2".
  2. El sistema recorre la lista interna y muestra todas las canciones registradas.

## Caso de Uso 3: Filtrar por Género
- **Actor:** Usuario
- **Precondición:** El catálogo está cargado.
- **Flujo Principal:**
  1. El usuario selecciona la opción "3".
  2. El sistema pide el género deseado (ej. "Rock").
  3. El sistema muestra la lista de canciones pertenecientes a ese género.