# Espotify

> Sistema inteligente de recomendación y exploración de música basado en grafos, árboles y métricas de audio.

Sistema de recomendación de música desarrollado para la materia **Estructuras de Datos** de la **Universidad Nacional de Almirante Brown (UNaB)**. El proyecto aborda la problemática de la exploración eficiente dentro de catálogos musicales, permitiendo buscar canciones, filtrar por género, construir listas de reproducción personalizadas y descubrir relaciones entre pistas.

---

## 📋 Tabla de Contenidos

1. [Integrantes](#-integrantes)
2. [Requisitos Previos](#-requisitos-previos)
3. [Instalación y Ejecución](#-instalación-y-ejecución)
4. [Ejecución de Pruebas Unitarias](#-ejecución-de-pruebas-unitarias)
5. [Estructura del Repositorio](#-estructura-del-repositorio)
6. [Documentación del Proyecto](#-documentación-del-proyecto)
7. [Estado del Proyecto](#-estado-del-proyecto)

---

## 👥 Integrantes

* **Laureano Imanol Caminos Delgado** - **Comision 3**
* **Joaquin Lamaita** - **Comision 3**
* **Rodrigo Mendy Godoy** - **Comision 3** 

---

## 💻 Requisitos Previos

* **Python:** Versión 3.10 o superior.
* **Módulos requeridos:** Utiliza únicamente la biblioteca estándar de Python (`json`, `unittest`, `csv`, etc.) para el núcleo del sistema, garantizando máxima portabilidad sin dependencias externas obligatorias.

---

## 🚀 Instalación y Ejecución

### 1. Clonar el repositorio
```bash
git clone https://github.com/tu-usuario/tp-integrador-Espotify.git
cd tp-integrador-Espotify
```

### 2. Ejecutar la aplicación
```bash
python main.py
```

Al iniciar, el sistema cargará automáticamente el dataset inicial en `datos/canciones.json` e iniciará la interfaz de terminal interactiva.

---

## 🧪 Ejecución de Pruebas Unitarias

El proyecto incluye una suite de pruebas automatizadas escritas con `unittest` para verificar el correcto funcionamiento de la lógica de negocio y las operaciones del catálogo.

Para ejecutar todas las pruebas unitarias:

```bash
python -m unittest discover tests
```

---

## 📂 Estructura del Repositorio

La arquitectura del proyecto aplica el principio de separación de responsabilidades en capas delgadas:

```text
.
├── main.py                    # Punto de entrada principal
├── README.md                  # Portada y documentación general
├── .gitignore                 # Reglas de exclusión para Git
├── datos/
│   └── canciones.json         # Dataset de canciones en UTF-8
├── docs/
│   ├── 01-requerimientos.md   # Propuesta, alcance y requerimientos (RF/RNF)
│   ├── 02-casos-de-uso.md     # Casos de uso detallados
│   ├── 03-diagrama-clases.md  # Diagrama UML en formato Mermaid
│   ├── 04-diagrama-datos.md   # Modelo e integración de estructuras
│   ├── 05-gestion-proyecto.md # Tablero de trabajo y seguimiento
│   ├── 07-analisis-tp3.md     # Análisis del BST
│   ├── 08-analisis-tp4-tp5.md # Análisis del AVL y del árbol general
│   └── Capturas/              # Salidas de terminal usadas como evidencia
├── estructuras/
│   ├── arbol_binario.py       # BST (TP3)
│   ├── avl.py                 # Árbol AVL (TP4)
│   └── arbol_general.py       # Árbol general N-ario (TP5)
├── algoritmos/
│   ├── medir_tiempos.py       # Secuencial vs BST (TP3)
│   └── comparar_bst_avl.py    # BST vs AVL con datos ordenados (TP4)
├── modelos/
│   └── cancion.py             # Clase de dominio (Cancion) con encapsulamiento
├── servicios/
│   ├── catalogo.py            # Lógica de negocio (búsqueda con AVL, top, filtrado)
│   └── categorias.py          # Jerarquía de géneros para el árbol general
├── ui/
│   └── terminal.py            # Interfaz de línea de comandos (I/O)
└── tests/
    ├── test_catalogo.py       # Pruebas del catálogo
    ├── test_avl.py            # Pruebas del AVL y sus rotaciones
    └── test_arbol_general.py  # Pruebas del árbol general y la jerarquía
```

---

## 📄 Documentación del Proyecto

Toda la documentación técnica se encuentra formalizada en la carpeta `docs/`:

* [📄 01-requerimientos.md](docs/01-requerimientos.md) — Dominio, problema, usuario objetivo y requerimientos del sistema.
* [📄 02-casos-de-uso.md](docs/02-casos-de-uso.md) — Flujos principales y alternativos de interacción.
* [📄 03-diagrama-clases.md](docs/03-diagrama-clases.md) — Diagrama de clases Mermaid actualizado (v1).
* [📄 05-gestion-proyecto.md](docs/05-gestion-proyecto.md) — Planificación del proyecto y enlace al tablero Kanban.
* [📄 07-analisis-tp3.md](docs/07-analisis-tp3.md) — Análisis del árbol binario de búsqueda.
* [📄 08-analisis-tp4-tp5.md](docs/08-analisis-tp4-tp5.md) — Análisis del árbol AVL y del árbol general.

---

## 📌 Estado del Proyecto

* [x] **TP0 (Lanzamiento):** Propuesta de dominio, requerimientos iniciales, diagrama de clases e infraestructura Git.
* [x] **TP1 (Versión Funcional Mínima v1):** Modelado del dominio `Cancion`, catálogo `Catalogo`, menú interactivo de terminal y suite de tests.
* [ ] **TP2 (Análisis de Complejidad & Benchmarking):** Medición de tiempos de búsqueda.
* [x] **TP3 (Árbol Binario de Búsqueda):** Indexación por título con BST y medición de tiempos.
* [x] **TP4 (Árbol AVL):** Índice por título auto-balanceado, comparación BST vs AVL con 10.000 datos ordenados.
* [x] **TP5 (Árbol General):** Jerarquía Música → familia → género para la opción "Explorar categorías".
* [ ] **TP6 (Colas de Prioridad - Heap):** Ranking Top-N de canciones por popularidad.
* [ ] **TP7 (Grafos):** Recomendación por caminos de similitud entre pistas.