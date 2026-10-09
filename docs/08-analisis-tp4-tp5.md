# Análisis TP4 + TP5 — AVL y Árbol General (Espotify)

## 1. ¿Qué resolvimos?

En esta etapa incorporamos **dos estructuras de datos** que resuelven problemas distintos dentro del sistema:

| Estructura | Problema que resuelve | Dónde se usa |
|---|---|---|
| **AVL** | Que las búsquedas por título sean siempre rápidas (O(log n)) incluso cuando los datos se insertan en orden | Opción 1 "Buscar canción por título" del menú |
| **Árbol General** | Representar la jerarquía de géneros musicales del dominio (Música → familia → género) | Opción 2 "Explorar categorías" del menú |

El AVL reemplaza al BST del TP3 como índice de títulos del `Catalogo`. El BST (`estructuras/arbol_binario.py`) se conserva sin cambios porque se usa como punto de comparación.

---

## 2. TP4 — Árbol AVL

### 2.1 ¿Por qué AVL y no un BST común?

Un BST común se desbalancea cuando se insertan datos ordenados (por ejemplo, títulos en orden alfabético): cada elemento nuevo es mayor que todos los anteriores y se cuelga siempre a la derecha, por lo que el árbol degenera en una lista enlazada con búsqueda O(n). El AVL resuelve esto con **rotaciones automáticas** que mantienen la altura en O(log n) sin importar el orden de inserción.

En Espotify el problema no es teórico: si el catálogo se carga desde una fuente ya ordenada por título, el BST del TP3 no solo se vuelve lento, sino que **directamente falla** con `RecursionError` (ver sección 7).

### 2.2 Rotaciones implementadas

| Tipo | Caso | Cuándo se aplica | Método |
|---|---|---|---|
| Rotación simple derecha | Izquierda-Izquierda | Factor de balance > 1 y el nuevo dato quedó a la izquierda del hijo izquierdo | `_rotacion_derecha` |
| Rotación simple izquierda | Derecha-Derecha | Factor de balance < -1 y el nuevo dato quedó a la derecha del hijo derecho | `_rotacion_izquierda` |
| Rotación doble izquierda-derecha | Izquierda-Derecha | Factor de balance > 1 pero el nuevo dato quedó a la derecha del hijo izquierdo | `_rotacion_izquierda_derecha` |
| Rotación doble derecha-izquierda | Derecha-Izquierda | Factor de balance < -1 pero el nuevo dato quedó a la izquierda del hijo derecho | `_rotacion_derecha_izquierda` |

El factor de balance se calcula como `altura(izquierdo) - altura(derecho)`. Cada caso está cubierto por un test unitario que inserta tres valores y verifica la forma resultante (`tests/test_avl.py`): `[3, 2, 1]`, `[1, 2, 3]`, `[3, 1, 2]` y `[1, 3, 2]` terminan los cuatro con raíz `2`, hijo izquierdo `1` e hijo derecho `3`.

### 2.3 Casos de desbalance generados

Insertamos datos **en orden alfabético** (el escenario que rompe un BST común) y comprobamos que el AVL mantiene la altura controlada.

**Datos de prueba:**

```text
A, B, C, D, E, F, G, H, I, J (10 elementos en orden)
```

Resultado: el AVL queda con **altura 4** y raíz `D`. Su preorder (`D, B, A, C, H, F, E, G, I, J`) muestra que los elementos quedaron repartidos a ambos lados de la raíz:

```text
            D
         /     \
        B       H
       / \     / \
      A   C   F   I
             / \   \
            E   G   J
```

Además del ejemplo chico, repetimos el experimento con **10.000 títulos reales del dataset** ordenados alfabéticamente (sección 2.4).

### 2.4 Comparación BST vs AVL

Mediciones obtenidas con `python algoritmos/comparar_bst_avl.py` (salida completa en `docs/Capturas/tp4-comparar-bst-avl.txt`). Se toman los primeros 10.000 títulos distintos del dataset de Kaggle en orden alfabético y se insertan los mismos objetos `Cancion` en ambos árboles. Los tiempos de búsqueda son el **promedio de 1000 búsquedas** medidas con `time.perf_counter()`.

| Métrica | BST común | AVL |
|---|---|---|
| Altura con 10 datos ordenados (A–J) | 10 | 4 |
| Altura con 10.000 datos ordenados | 10.000 | 14 |
| Búsqueda con 10.000 datos ordenados (último título, peor caso del BST) | 3,6705 ms | 0,0022 ms |
| Búsqueda con 10.000 datos ordenados (títulos aleatorios) | 1,8820 ms | 0,0027 ms |
| Búsqueda con 10.000 datos ordenados (título inexistente) | 3,6450 ms | 0,0023 ms |
| Construcción del árbol con 10.000 datos ordenados | 27.173,4 ms | 99,9 ms |
| Complejidad peor caso búsqueda | O(n) | O(log n) |
| Complejidad promedio inserción | O(log n) | O(log n) |
| Complejidad peor caso inserción | O(n) | O(log n) |

> **Justificación:** insertar 10 elementos ordenados genera un BST con altura 10 (una cadena), mientras que el AVL tiene altura 4, que es además el máximo posible para un AVL de 10 nodos. Con 10.000 datos la diferencia se amplifica: el BST tiene altura 10.000 y el AVL 14, que coincide con el mínimo teórico ⌈log₂(10.001)⌉ = 14. Por eso buscar el último título cuesta unas **1.700 veces más** en el BST (3,6705 ms contra 0,0022 ms), y construir el BST lleva 27 segundos porque cada inserción recorre toda la cadena (O(n²) en total).

**Contraste con datos no ordenados.** Con el dataset completo en el orden original del CSV (114.000 filas, 72.397 títulos distintos), que no está ordenado por título, el BST no degenera:

| Métrica | BST común | AVL |
|---|---|---|
| Altura | 46 | 19 |
| Construcción | 993,5 ms | 1.231,0 ms |
| Búsqueda de títulos aleatorios | 0,0054 ms | 0,0034 ms |

El AVL paga un costo de construcción un poco mayor (≈ 24 %) por recalcular alturas y rotar, pero a cambio la altura queda **garantizada**: en este caso 19, dentro de la cota teórica del AVL (≈ 1,44·log₂ n ≈ 23). El BST tiene "buena suerte" con este orden, pero no ofrece ninguna garantía.

### 2.5 Prueba del AVL

Salida completa de `python estructuras/avl.py` (también en `docs/Capturas/tp4-avl.txt`):

```text
=== AVL con datos ordenados ===
Altura del AVL: 4
Cantidad de nodos: 10
Raíz: Elemento(nombre='D', valor=4)

--- inorder ---
  Elemento(nombre='A', valor=1)
  Elemento(nombre='B', valor=2)
  Elemento(nombre='C', valor=3)
  Elemento(nombre='D', valor=4)
  Elemento(nombre='E', valor=5)
  Elemento(nombre='F', valor=6)
  Elemento(nombre='G', valor=7)
  Elemento(nombre='H', valor=8)
  Elemento(nombre='I', valor=9)
  Elemento(nombre='J', valor=10)

--- preorder (muestra el balance) ---
  Elemento(nombre='D', valor=4)
  Elemento(nombre='B', valor=2)
  Elemento(nombre='A', valor=1)
  Elemento(nombre='C', valor=3)
  Elemento(nombre='H', valor=8)
  Elemento(nombre='F', valor=6)
  Elemento(nombre='E', valor=5)
  Elemento(nombre='G', valor=7)
  Elemento(nombre='I', valor=9)
  Elemento(nombre='J', valor=10)

Buscar 'F': Elemento(nombre='F', valor=6)
Buscar 'Z': None

=== Comparación BST vs AVL ===
  Altura BST: 10
  Altura AVL: 4
  AVL más bajo que BST: True
  1000 búsquedas de 'J' en BST: 1.457 ms
  1000 búsquedas de 'J' en AVL: 0.496 ms
```

Resumen: **Altura del AVL: 4**, `Buscar 'F'` devuelve `Elemento(nombre='F', valor=6)` y `Buscar 'Z'` devuelve `None`.

### 2.6 Código del AVL

Archivo: `estructuras/avl.py`

- `NodoAVL`: nodo con dato, hijos (`izquierdo`, `derecho`) y `altura` (una hoja tiene altura 1).
- `AVL`: árbol con inserción balanceada (`insertar`), búsqueda (`buscar`), recorridos (`inorder`, `preorder`, `postorder`), `altura()` y `__len__`.
- Rotaciones: `_rotacion_izquierda`, `_rotacion_derecha`, `_rotacion_izquierda_derecha`, `_rotacion_derecha_izquierda`.
- `comparar_bst_vs_avl(lista_datos, clave)`: inserta los mismos datos en el BST del TP3 y en el AVL y devuelve alturas y tiempos.

La inserción sigue cuatro pasos sobre el camino de vuelta de la recursión:

```python
def _insertar_recursivo(self, nodo, dato, clave):
    # Paso 1: inserción estándar como en un BST
    if nodo is None:
        return NodoAVL(dato)
    ...
    # Paso 2: actualizar la altura del nodo actual
    self._actualizar_altura(nodo)
    # Paso 3: obtener el factor de balance
    balance = self._factor_balance(nodo)
    # Paso 4: si está desbalanceado, aplicar la rotación correspondiente
    if balance > 1 and clave(dato) < clave(nodo.izquierdo.dato):
        return self._rotacion_derecha(nodo)
    ...
```

Igual que el BST del TP3, el AVL **ignora los duplicados** según la clave: si un título ya existe, el nodo no se reemplaza.

---

## 3. TP5 — Árbol General (N-ario)

### 3.1 ¿Qué es un árbol general?

A diferencia del árbol binario, donde cada nodo tiene como máximo 2 hijos, un **árbol general** permite que cada nodo tenga **cualquier cantidad de hijos**. Esto lo hace ideal para representar jerarquías naturales, donde la cantidad de subcategorías varía de un nodo a otro.

### 3.2 Jerarquía elegida del dominio

El dataset de Kaggle clasifica cada canción con uno de **114 géneros** (`track_genre`). Una lista plana de 114 géneros es difícil de recorrer para el usuario, así que los agrupamos en **13 familias**. El árbol queda con 3 niveles: raíz `Música` → familia → género (128 nodos en total). Entre paréntesis figura la cantidad de géneros de cada familia:

```text
Música
├── Rock (16)
│       rock, alt-rock, alternative, hard-rock, psych-rock, punk
│       punk-rock, grunge, indie, garage, emo, goth, british, j-rock
│       rock-n-roll, rockabilly
├── Metal (8)
│       metal, heavy-metal, black-metal, death-metal, metalcore
│       grindcore, hardcore, industrial
├── Pop (12)
│       pop, indie-pop, power-pop, synth-pop, k-pop, j-pop, j-idol
│       j-dance, cantopop, mandopop, pop-film, anime
├── Electrónica (20)
│       electronic, edm, electro, house, deep-house, chicago-house
│       progressive-house, techno, detroit-techno, minimal-techno
│       trance, dubstep, drum-and-bass, breakbeat, hardstyle, idm
│       trip-hop, dance, club, disco
├── Hip-Hop y R&B (2)
│       hip-hop, r-n-b
├── Jazz, Blues y Soul (6)
│       jazz, blues, soul, funk, groove, gospel
├── Latina (12)
│       latin, latino, reggaeton, salsa, tango, spanish, brazil, mpb
│       samba, pagode, forro, sertanejo
├── Reggae y Caribe (4)
│       reggae, dancehall, ska, dub
├── Folk, Country y Acústica (8)
│       folk, country, bluegrass, honky-tonk, acoustic
│       singer-songwriter, songwriter, guitar
├── Clásica e Instrumental (6)
│       classical, opera, piano, new-age, ambient, show-tunes
├── Música del mundo (9)
│       world-music, afrobeat, indian, iranian, turkish, malay
│       french, german, swedish
├── Estados de ánimo (7)
│       happy, sad, chill, sleep, study, party, romance
└── Infantil y Entretenimiento (4)
        children, kids, disney, comedy
```

La jerarquía se define en `servicios/categorias.py` (`JERARQUIA_GENEROS`). El test `test_jerarquia_cubre_todos_los_generos_del_dataset` verifica contra el CSV que cada uno de los 114 géneros aparezca **exactamente una vez**.

**¿Por qué esta jerarquía?**

- Los géneros son la clasificación natural del dominio musical y ya vienen en el dataset.
- La cantidad de hijos varía mucho (de 2 a 20 géneros por familia): un árbol binario no la representa naturalmente, uno general sí.
- Permite al usuario explorar de lo general a lo particular: familia → género → canciones más populares del género.
- Se conecta con el AVL: el AVL busca por **título**, el árbol general organiza por **categoría**.

### 3.3 Recorridos implementados

| Recorrido | Descripción | Complejidad | Método |
|---|---|---|---|
| **Amplitud (BFS)** | Nivel por nivel, de arriba hacia abajo | O(n) | `amplitud()` |
| **Profundidad preorder** | Nodo → hijos (izquierda a derecha) | O(n) | `profundidad_preorder()` |
| **Profundidad postorder** | Hijos → nodo | O(n) | `profundidad_postorder()` |

El BFS usa `collections.deque`: `popleft()` es O(1), por lo que el recorrido completo es O(n). Con una lista común y `pop(0)` cada extracción costaría O(n) y el recorrido, O(n²) (ver sección 7).

### 3.4 Prueba del árbol general

Salida completa de `python estructuras/arbol_general.py` (también en `docs/Capturas/tp5-arbol-general.txt`). El ejemplo usa un subconjunto de la jerarquía real:

```text
=== Árbol General de Categorías ===
Raíz: Música
Altura: 3
Cantidad de nodos: 11

Música
├── Rock
│   ├── alt-rock
│   ├── hard-rock
│   └── punk
├── Electrónica
│   ├── house
│   └── techno
└── Latina
    ├── tango
    └── salsa

--- Recorrido en amplitud ---
['Música', 'Rock', 'Electrónica', 'Latina', 'alt-rock', 'hard-rock', 'punk', 'house', 'techno', 'tango', 'salsa']

--- Recorrido en profundidad (preorder) ---
['Música', 'Rock', 'alt-rock', 'hard-rock', 'punk', 'Electrónica', 'house', 'techno', 'Latina', 'tango', 'salsa']

--- Recorrido en profundidad (postorder) ---
['alt-rock', 'hard-rock', 'punk', 'Rock', 'house', 'techno', 'Electrónica', 'tango', 'salsa', 'Latina', 'Música']

--- Niveles ---
  Nivel 0: ['Música']
  Nivel 1: ['Rock', 'Electrónica', 'Latina']
  Nivel 2: ['alt-rock', 'hard-rock', 'punk', 'house', 'techno', 'tango', 'salsa']

--- Hijos de 'Rock' ---
['alt-rock', 'hard-rock', 'punk']

--- Buscar 'tango' ---
Encontrado: Nodo(tango)
--- Buscar 'opera' ---
Encontrado: None
```

### 3.5 Código del árbol general

Archivo: `estructuras/arbol_general.py`

- `NodoGeneral`: nodo con `dato` y lista `hijos`; `es_hoja()` indica si no tiene hijos.
- `ArbolGeneral`: árbol con inserción, búsqueda y recorridos.
- Métodos principales: `insertar_raiz`, `agregar_hijo`, `buscar` (BFS), `buscar_recursivo` (DFS), `amplitud`, `profundidad_preorder`, `profundidad_postorder`.
- Métodos auxiliares: `altura`, `cantidad_nodos`, `listar_hijos`, `obtener_niveles` y `dibujar` (devuelve el árbol con conectores `├──`/`└──`, que es lo que muestra la opción "Explorar categorías").

`agregar_hijo(nodo_padre, dato)` acepta el padre como `NodoGeneral` (O(1)) o como su dato, en cuyo caso primero lo busca (O(n)). Si el árbol no tiene raíz o el padre no existe, lanza `ValueError`.

---

## 4. Integración con la aplicación

### 4.1 ¿Dónde queda cada estructura?

```text
┌───────────────────────────────────────────────────────────────────────────┐
│                     Interfaz de terminal (ui/terminal.py)                 │
├──────────────┬──────────────┬──────────────┬──────────────┬───────────────┤
│ Opción 1:    │ Opción 2:    │ Opción 3:    │ Opción 4:    │ Opción 5:     │
│ Buscar       │ Explorar     │ Ver Top 10   │ Listar       │ Filtrar por   │
│              │ categorías   │              │              │ género        │
│ usa: AVL     │ usa:         │ usa: sorted  │ usa: lista   │ usa: lista    │
│ (Catalogo)   │ Árbol Gen.   │ (heap: TP6)  │              │               │
└──────────────┴──────────────┴──────────────┴──────────────┴───────────────┘
```

Las opciones 1 a 3 siguen la distribución propuesta. Mantuvimos "Listar" y "Filtrar por género" del TP1 como opciones 4 y 5. El Top 10 se resuelve por ahora con `sorted()` (O(n log n)); en el TP6 se reemplazará por un heap.

### 4.2 Código de integración

**Diferencia con la propuesta de la plantilla:** la plantilla instancia el AVL directamente en `main.py`. En el proyecto el AVL quedó **encapsulado dentro de `Catalogo`**, que ya era dueño del índice por título desde el TP3. Así la interfaz no conoce la estructura interna, y para pasar de BST a AVL alcanzó con cambiar el índice dentro del catálogo. El árbol de categorías sí se crea en `main.py` y se le pasa a la terminal.

**Imports** (`main.py` y `servicios/catalogo.py`):

```python
# main.py
from estructuras.arbol_general import ArbolGeneral
from servicios.catalogo import Catalogo
from servicios.categorias import construir_arbol_categorias
from ui.terminal import Terminal

# servicios/catalogo.py
from estructuras.avl import AVL
```

**Inicialización** (`main.py`):

```python
# El catálogo indexa los títulos en un árbol AVL (opción "Buscar")
catalogo = Catalogo()
catalogo.cargar_desde_csv(ruta_dataset)

# Jerarquía Música → familia → género (opción "Explorar categorías")
arbol_categorias = ArbolGeneral()
construir_arbol_categorias(arbol_categorias)

terminal = Terminal(catalogo, arbol_categorias)
terminal.iniciar()
```

Dentro de `Catalogo`, el AVL se puebla al cargar los datos:

```python
def _indexar_arbol(self) -> None:
    """Pobla el árbol AVL ordenando por título en minúsculas."""
    self._arbol_titulos = AVL()
    for cancion in self._elementos:
        self._arbol_titulos.insertar(
            cancion, clave=lambda c: c.titulo.lower()
        )
```

**Opción "Buscar"** (`Catalogo.buscar_avl`, usado por `Terminal._buscar`):

```python
return self._arbol_titulos.buscar(
    titulo.strip().lower(), clave=lambda c: c.titulo.lower()
)
```

**Opción "Explorar categorías"** (`Terminal._explorar_categorias`, resumido):

```python
print("\nCategorías por amplitud (familias de géneros):")
for familia in arbol.listar_hijos(arbol.raiz):
    print(f"  - {familia}")

nombre = input("\nCategoría a explorar (Enter para volver): ").strip()
...
nodo = self._buscar_categoria(nombre)
...
if nodo.es_hoja():   # un género: mostrar sus canciones más populares
    for cancion in self._catalogo.top(10, genero=nodo.dato):
        print(f"- {cancion}")
else:                # una familia: dibujar su subárbol
    print("\n".join(arbol.dibujar(nodo)))
```

La plantilla imprime `arbol_categorias.amplitud()` completo; con 128 nodos esa lista resulta poco útil, así que el menú muestra el primer nivel del recorrido (las familias) y deja bajar a una familia o a un género. `_buscar_categoria` recorre el árbol por amplitud comparando sin distinguir mayúsculas (O(n)).

**Ejecución real** (extracto de `docs/Capturas/tp4-tp5-main.txt`, obtenida pasando las opciones por entrada estándar):

```text
Se cargaron exitosamente 114000 canciones desde 'datos/canciones-kreagle.csv.csv' (altura del índice AVL: 19).
...
Opción: Título a buscar:
Encontrada: 'Ghost - Acoustic' - Ben Woodward (acoustic) [Pop: 5.5]
...
Opción: Título a buscar:
No se encontró la canción 'Cancion que no existe'.
...
Categoría a explorar (Enter para volver):
Latina
├── latin
├── latino
├── reggaeton
...
└── sertanejo
...
--- Top 10 de tango ---
- 'Por Una Cabeza' - Carlos Gardel (tango) [Pop: 4.6]
- 'Scent of a Woman: Tango (Por Una Cabeza)' - Carlos Gardel;Itzhak Perlman;John Williams;Pittsburgh Symphony Orchestra (tango) [Pop: 4.4]
- 'Naranjo en Flor (En Directo)' - Roberto Goyeneche (tango) [Pop: 3.8]
...
```

---

## 5. Análisis de complejidad

| Operación | AVL | Árbol General |
|---|---|---|
| Inserción | O(log n) | O(1) al agregar un hijo a un nodo conocido; O(n) si el padre se indica por su dato (hay que buscarlo) |
| Búsqueda | O(log n) | O(n) (recorrido completo) |
| Recorrido inorder | O(n) | No aplica: el inorder no está definido para nodos con más de 2 hijos; se usan preorder y postorder, ambos O(n) |
| Recorrido amplitud | O(n) (no implementado en el AVL: no lo necesitamos) | O(n) |
| Altura (peor caso) | O(log n) | O(n) (árbol degenerado) |

Detalles de la implementación:

- En el AVL, `altura()` es O(1) porque cada nodo guarda su altura; el valor obtenido es O(log n). En cambio `len(avl)` recorre todos los nodos: O(n).
- En el árbol general, `altura()` y `cantidad_nodos()` recorren el árbol completo: O(n).

**¿Por qué el AVL es O(log n)?**

El AVL mantiene el factor de balance entre -1 y +1 en cada nodo. Eso garantiza que la altura sea siempre proporcional a log₂(n): como máximo ≈ 1,44·log₂(n). Un árbol con 1000 nodos tiene altura de entre 10 y 14, contra 1000 en un BST degenerado. Las mediciones lo confirman: con 10.000 títulos ordenados el AVL tiene altura 14 y el BST 10.000; con los 72.397 títulos del dataset, el AVL tiene altura 19.

**¿Por qué el árbol general no se auto-balancea?**

El árbol general no necesita balanceo porque no tiene un criterio de ordenamiento. Su estructura refleja una jerarquía natural (Música → familia → género), no un orden numérico o alfabético; "balancearlo" rompería el significado de la jerarquía. El costo de búsqueda O(n) es aceptable porque la cantidad de categorías es chica: 128 nodos en total, contra 114.000 canciones.

---

## 6. Conclusión

- **El AVL** garantiza búsquedas eficientes sin importar el orden de inserción y resuelve el problema principal del BST: con 10.000 títulos ordenados la altura baja de 10.000 a 14 y la búsqueda del peor caso pasa de 3,67 ms a 0,0022 ms.
- **El árbol general** organiza los 114 géneros del dataset en 13 familias y permite navegar de lo general (familia) a lo particular (género y sus canciones más populares).
- **Ambas estructuras se complementan:** el AVL resuelve la búsqueda eficiente por clave (título) y el árbol general organiza la navegación jerárquica por categorías. Las dos se conectan en la opción "Explorar categorías", donde un género (hoja del árbol general) muestra canciones del catálogo.
- Ninguna de las dos se usó "por cumplir": el AVL resuelve un problema real (el desbalance, que en el BST del TP3 llega a provocar un `RecursionError`) y el árbol general resuelve otro (jerarquizar un dominio que en el dataset viene como lista plana).

---

## 7. Errores o dudas que tuvimos

1. **El BST del TP3 falla con datos ordenados (`RecursionError`).** Al insertar títulos ordenados en `ArbolBST`, la recursión de `_insertar_recursivo` alcanza el límite de recursión de Python (1000) e interrumpe la carga en el elemento 997. Para poder medirlo, `algoritmos/comparar_bst_avl.py` sube el límite con `sys.setrecursionlimit` y deja registrado el error en su salida. El AVL no tiene este problema: su recursión llega como máximo a la altura del árbol (14 con 10.000 datos).
2. **Import inexistente en la comparación.** `comparar_bst_vs_avl` importaba `arboles` / `estructuras.arboles`, pero en el proyecto el BST está en `estructuras/arbol_binario.py`: la comparación siempre devolvía "No se encontró arboles.py". Corregimos el import (`estructuras.arbol_binario` y, como alternativa, `arbol_binario` para cuando se ejecuta `python estructuras/avl.py`).
3. **La comparación medía el mejor caso del BST.** La función buscaba `lista_datos[0]`, que con datos ordenados es la **raíz** del BST (O(1)), por lo que no mostraba el desbalance. Ahora busca el último elemento, que es la hoja más profunda, y mide con `time.perf_counter()` en lugar de `time.time()`, que tiene mejor resolución.
4. **Salida del ejemplo distinta a la esperada.** El `__repr__` de `Elemento` imprimía `F(6)`; lo cambiamos para que la salida sea `Elemento(nombre='F', valor=6)`. También corregimos los diagramas ASCII de los docstrings de las rotaciones, que estaban desalineados (el de la rotación derecha mostraba `/ /` en lugar de `/ \`).
5. **`agregar_hijo` con el padre como texto.** El docstring del módulo mostraba `arbol.agregar_hijo("Películas", ...)`, pero el método esperaba un `NodoGeneral` y fallaba con `AttributeError: 'str' object has no attribute 'hijos'`. Además, la validación `nodo_padre is None and self.raiz is None` dejaba pasar `nodo_padre=None` cuando ya había raíz. Ahora el método acepta un nodo o el dato del padre (y lo busca), y lanza `ValueError` si el árbol no tiene raíz o el padre no existe.
6. **BFS con `list.pop(0)`.** `pop(0)` desplaza toda la lista (O(n) por extracción), así que el recorrido en amplitud era O(n²) aunque la tabla dijera O(n). Lo reemplazamos por `collections.deque.popleft()` (O(1)).
7. **Bug de popularidad heredado del TP1 (detectado al probar "Ver Top 10").** `cargar_desde_csv` dividía la popularidad por 10 solo si era mayor que 10, así que una canción con popularidad 10/100 en Kaggle quedaba como 10.0/10, el máximo. Afectaba a 7.442 filas: el Top 10 mostraba temas de nicho con "Pop: 10.0". Ahora la columna `popularity` de Kaggle (escala 0–100) siempre se divide por 10 y la columna `popularidad` (ya en 0–10) se usa tal cual.
8. **Títulos repetidos en el dataset (duda pendiente).** El CSV tiene 114.000 filas pero solo 72.397 títulos distintos: la misma canción aparece una vez por cada género en que está clasificada, y también hay canciones distintas con el mismo título. Como el AVL ignora los duplicados por clave, "Buscar" devuelve la primera aparición del título. Por el mismo motivo, el Top 10 general muestra la misma canción varias veces ("La Bachata" aparece en latin, latino, reggae y reggaeton). Lo dejamos para el TP6, donde el ranking pasará a un heap y podremos deduplicar.
9. **Dominio de la plantilla.** El ejemplo de la consigna usa una jerarquía de películas; la adaptamos a géneros musicales, que es el dominio de Espotify.

---

## 8. Datos y evidencia

- **Script de prueba del AVL:** `estructuras/avl.py` (bloque `__main__`) → salida en `docs/Capturas/tp4-avl.txt`.
- **Script de comparación BST vs AVL (10.000 datos ordenados y dataset completo):** `algoritmos/comparar_bst_avl.py` → salida en `docs/Capturas/tp4-comparar-bst-avl.txt`.
- **Script de prueba del árbol general:** `estructuras/arbol_general.py` (bloque `__main__`) → salida en `docs/Capturas/tp5-arbol-general.txt`.
- **Tests unitarios:** `tests/test_avl.py` (altura con A–J, las 4 rotaciones, invariante de balance con 10.000 datos, búsqueda y duplicados) y `tests/test_arbol_general.py` (recorridos, búsqueda, errores de `agregar_hijo` y cobertura de los 114 géneros). Ejecución con `python -m unittest discover tests`: 18 tests, todos OK → `docs/Capturas/tp4-tp5-tests.txt`.
- **Ejecución de la aplicación integrada:** `docs/Capturas/tp4-tp5-main.txt` (Buscar existente e inexistente, Explorar "Latina" y "tango", Ver Top 10).
- **Capturas de la terminal:** la carpeta del repositorio es `docs/Capturas/` (con mayúscula, a diferencia de `docs/capturas/` de la plantilla). Contiene las salidas de texto listadas arriba, generadas al ejecutar los scripts. **Todavía no hay capturas de pantalla en imagen.**

Los tiempos dependen de la máquina y varían entre ejecuciones. Las alturas son deterministas: para un mismo orden de inserción, siempre dan el mismo resultado.
