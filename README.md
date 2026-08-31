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
│   └── capturas/              # Evidencia visual de ejecución de terminal
├── modelos/
│   └── cancion.py             # Clase de dominio (Cancion) con encapsulamiento
├── servicios/
│   └── catalogo.py            # Lógica de negocio (búsqueda, listado, filtrado)
├── ui/
│   └── terminal.py            # Interfaz de línea de comandos (I/O)
└── tests/
    └── test_catalogo.py       # Pruebas unitarias automatizadas
```

---

## 📄 Documentación del Proyecto

Toda la documentación técnica se encuentra formalizada en la carpeta `docs/`:

* [📄 01-requerimientos.md](docs/01-requerimientos.md) — Dominio, problema, usuario objetivo y requerimientos del sistema.
* [📄 02-casos-de-uso.md](docs/02-casos-de-uso.md) — Flujos principales y alternativos de interacción.
* [📄 03-diagrama-clases.md](docs/03-diagrama-clases.md) — Diagrama de clases Mermaid actualizado (v1).
* [📄 05-gestion-proyecto.md](docs/05-gestion-proyecto.md) — Planificación del proyecto y enlace al tablero Kanban.

---

## 📌 Estado del Proyecto

* [x] **TP0 (Lanzamiento):** Propuesta de dominio, requerimientos iniciales, diagrama de clases e infraestructura Git.
* [x] **TP1 (Versión Funcional Mínima v1):** Modelado del dominio `Cancion`, catálogo `Catalogo`, menú interactivo de terminal y suite de tests.
* [ ] **TP2 (Análisis de Complejidad & Benchmarking):** Medición de tiempos de búsqueda.
* [ ] **TP3 (Estructuras Jerárquicas - Árboles BST/AVL):** Indexación eficiente por título.
* [ ] **TP6 (Colas de Prioridad - Heap):** Ranking Top-N de canciones por popularidad.
* [ ] **TP7 (Grafos):** Recomendación por caminos de similitud entre pistas.