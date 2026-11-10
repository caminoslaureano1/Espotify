# Analisis TP2  — Complejidad y Benchmarking

## 1. Objetivo

Analizar la busqueda secuencial de canciones por titulo y observar como cambian el tiempo y la cantidad de comparaciones al aumentar el tamaño del catalogo.

## 2. Complejidad teorica

La busqueda secuencial recorre las canciones en orden y compara cada titulo con el buscado. Termina cuando encuentra una coincidencia o llega al final de la lista.

| Escenario | Comparaciones | Complejidad temporal |
| ---|---:|---:|
| Mejor caso: el primer titulo coincide | 1 | O(1) |
| Caso promedio: el titulo aparece en una posicion variable |  Proporcional a n | O(n) |
| Peor caso: el titulo no existe o esta al final | Hasta n | O(n) |

El espacio auxiliar de la busqueda es O(1) respecto de la cantidad: no guarda los elementos recorridos. La normalizacion del titulo usa espacio temporal segun su longitud, que se consedera acotada respecto del tamaño del catalogo.

## 3. Metodologia

se utilizo el archivo 'datos/canciones-kreagle.csv.csv', que produjo un catalogo de 89.741 canciones. Se probaron muestras de 100, 1.000, 10.000 y 89.741 canciones.

Se midieron el mejor caso, el peor caso y busquedas exitosas de titulos elegidos al azar. Para medio el tiempo se uso 'time.perf_counter()' y se calculo el promedio por busqueda. Tambien se conto la cantidad de comparaciones para estudiar el crecimiento del algoritmo con menos dependencia de la velocidad del equipo.

Los tiempos son orientativos y pueden variar segun el equipo y las condiciones. Los tiempos son orientativos y pueden variar segun el equipo y las condiciones ejecucion.

## 4. Resultados de tiempo

### Mejor caso: buscar el primer titulo



| Canciones | Tiempo promedio por busqueda (ms) | 
|---:|---:|
| 100 | 0,000166 |
| 1.000 | 0,000159 |
| 10.000 | 0,000160 |
| 89.741 | 0,000159 |

El tiempo se mantiene practicamente constante porque la coincidencia se encuentra en la primera comparacion.

### Titulo ubicado aproximadamente a mitad de cada muestra

| Canciones | Tiempo promedio por busqueda (ms) |
|---:|---:|
| 100 | 0,003719 |
| 1.000 | 0,041861 |
| 10.000 | 0,497047 |
| 89.741 | 5,245782 |

Esta prueba es  aproximada: el titulo elegido puede aparecer repetido antes de la posicion seleccionada.

### Peor caso: buscar un titulo inecistente

| Canciones | Tiempo promedio por busqueda (ms) |
|---:|---:|
| 100 | 0,007885 |
| 1.000 | 0,087667 |
| 10.000 | 1,011174 |
| 89.741 | 11,159514 |

Como el titulo no existe, la busqueda recorre toda la muestra-

### Titulos unicos elegidos al azar

| Canciones | Busquedas realizadas | Tiempo promedio por busqueda (ms) |
|---:|---:|---:|
| 100 | 72 |0,003969 |
| 1.000 | 906 | 0,045254 |
| 10.000 | 1.000 | 0,506906 |
| 89.741 | 1.000 | 5,246789 |

En las muestras pequeñas habia menos de 1.000 titulos distintos, por eso se realizaron menos busquedas.


## 5. Cantidad de comparaciones

| Canciones | Mejor caso | Promedio de comparaciones | Peor caso |

|---:|---:|---:|---:|
| 100 | 1 | 47,08 | 100 |
| 1.000 | 1 | 508,57 | 1.000 |
| 10.000 | 1 | 5.149,84 | 10.000 |
| 89.741 | 1 | 45.506,33 | 89.741 |

El promedio se calculo buscando titulos unicos elegidos al azar. En el catalogo completo fueron unas 45.506 comparaciones, cerca de la mitad de los  89.741 elemtos. No es exactamente n/2 porque, si un titulo esta repetido, la busqueda lo encuentra en su primera aparicion.


## 6. Conclusion

Las mediciones muestran que el mejor caso mantiene una sola comparacion aunque aumente el catalogo. En cambio, las comparaciones promedio y las del peor caso crecen en proporcion a la cantidad de canciones. Los tiempos presentan una tendencia similar, aunque dependen mas del equipo y del ruido de medicion.

Por lo tanto, la busqueda secuencial tiene complejidad temporal O(1) en el mejor caso y O(n) en el caso promedio y el peor caso. Su espacio auxiliar es O(1) respecto de la cantidad de canciones.

