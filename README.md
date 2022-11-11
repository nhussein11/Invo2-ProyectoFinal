# Proyecto Final - Investigación Operativa II


## Autores
- Alejo Torres: [@AlejoTorres2001](https://www.github.com/alejotorres2001)
- Nicolas Hussein: [@nhussein11](https://www.github.com/nhussein11)

## Unidad 1

- ### Eliminacion de dominadas
  Consiste en ir eliminando iterativamente todas las estrategias dominadas. Partiendo de la matriz de pagos, en el primer paso, se elimina una estrategia dominada, ya que ningún jugador racional jugaría nunca esa estrategia. Esto se traduce en un nuevo juego más pequeño. Algunas estrategias que en el primer paso no eran dominadas, pueden resultar dominadas en este nuevo juego más pequeño. 
  ![image](https://user-images.githubusercontent.com/80422357/200175409-54be9636-d519-44be-a493-1277b06af490.png)
  
  La eliminación de estrategias dominadas se utiliza comúnmente para simplificar el análisis de cualquier juego. La manera de proceder es eliminar para cada jugador cada estrategia que parece «irracional», lo que reducirá en gran medida el número de equilibrios. Este método es bastante fácil de usar cuando solo hay estrategias estrictamente dominadas, pero la eliminación de las estrategias débilmente dominadas puede ser problemática, lo que puede dar con un juego que no se parece al original desde un punto de vista estratégico.
- ### Equilibrio de Nash
   Un equilibrio de Nash es una situación en la cual todos los jugadores han puesto en práctica, y saben que lo han hecho, una estrategia que maximiza sus ganancias dadas las estrategias de los otros. Consecuentemente, ningún jugador tiene ningún incentivo para modificar individualmente su estrategia.

  Es importante tener presente que un equilibrio de Nash no implica que se logre el mejor resultado conjunto para los participantes, sino solo el mejor resultado para cada uno de ellos considerados individualmente. Es perfectamente posible que el resultado fuera mejor para todos si, de alguna manera, los jugadores coordinaran su acción.
  ![image](https://user-images.githubusercontent.com/80422357/200175545-0873623d-9808-4280-85aa-489f238703ba.png)

  En términos económicos, es un tipo de equilibrio de competencia imperfecta que describe la situación de varias empresas compitiendo por el mercado de un mismo bien y que pueden elegir cuánto producir para intentar maximizar su ganancia.
- ### Estrategias Mixtas
  En teoría de juegos una estrategia mixta, a veces también llamada estrategia mezclada (del nombre en inglés mixed strategy), es una generalización de las estrategias puras, usada para describir la selección aleatoria de entre varias posibles estrategias puras, lo que determina siempre una distribución de probabilidad sobre el vector de estrategias de cada jugador. Una estrategia totalmente mixta es aquella en la que el jugador asigna una probabilidad estrictamente positiva a cada estrategia pura. Las estrategias totalmente mixtas son importantes para el refinamiento del equilibrio.
  Las estrategias mixtas son analizadas en la teoría de juegos cuando hay muchos equilibrios posibles, lo cual es especialmente el caso en los juegos de coordinación. La guerra de los sexos es un ejemplo común de un juego de coordinación en el que hay dos equilibrios de Nash (subrayados en rojo abajo), lo que significa que ningún equilibrio real puede ser alcanzado.
  En la guerra de los sexos, una pareja discute sobre qué hacer el fin de semana. Ambos saben que quieren pasar el fin de semana juntos, pero no se ponen de acuerdo sobre qué hacer. El hombre prefiere ir a ver un combate de boxeo, mientras que la mujer quiere ir de compras. Por tanto, la matriz de juego es como sigue:
  
  ![image](https://user-images.githubusercontent.com/80422357/200175659-48b2bbd9-f11c-4d71-865b-156a71fe840d.png)

- ### MinMax
  En teoría de juegos, 'minimax' es un método de decisión para minimizar la pérdida máxima esperada en juegos con adversario y con información perfecta. Minimax es un algoritmo recursivo.
  Pasos del algoritmo minimax:
  1. Generación del árbol de juego. Se generarán todos los nodos hasta llegar a un estado terminal.
  2. Cálculo de los valores de la función de utilidad para cada nodo terminal.
  3. Calcular el valor de los nodos superiores a partir del valor de los inferiores. Según nivel si es MAX o MIN se elegirán los valores mínimos y máximos representando los movimientos del jugador y del oponente, de ahí el nombre de minimax.
  4. Elegir la jugada valorando los valores que han llegado al nivel superior.
  ![image](https://user-images.githubusercontent.com/80422357/200175737-c1d4c988-d8ac-4b26-8fbc-4d653f74bdb2.png)

  El funcionamiento de minimax puede resumirse en cómo elegir el mejor movimiento para ti mismo suponiendo que tu contrincante escogerá el peor para ti.
  
## Unidad 2

- ### Arbol de Mínima Expansion
  El árbol de expansión de peso mínimo es aquel que comienza desde un vértice y encuentra todos sus nodos accesibles y las relaciones en conjunto que permiten que se conecten dichos nodos con el menor peso posible
  Dado un grafo conexo, no dirigido y con pesos en las aristas, un árbol de expansión mínima es un árbol compuesto por todos los vértices y cuya suma de sus aristas es la de menor peso. Al ejemplo anterior le agregamos pesos a sus aristas y obtenemos los arboles de expansiones siguientes:
  De la imagen anterior el árbol de expansión mínima seria el primer árbol de expansión cuyo peso total es 6.

  El problema de hallar el Árbol de Expansión Mínima (MST) puede ser resuelto con varios algoritmos, los mas conocidos con Prim y Kruskal ambos usan técnicas voraces (greedy).
  ![image](https://user-images.githubusercontent.com/80422357/200202445-ff866b66-3998-4a28-8131-fafa84f49210.png)

- ### Flujo Máximo
  El problema del Flujo Máximo consiste:  Dado un grafo dirigido con pesos,  G = (V, A,W),  que representa las capacidades máximas de los canales, un nodo de inicio S  y otro de fin T  en V , se trata de encontrar la cantidad máxima de flujo que puede circular desde S  hasta T.
  Las aristas representan canales por los que puede circular cierta cosa: transmisión de datos, redes de corriente eléctrica, líneas de oleoductos,  agua, automóviles, etc.
  Los pesos de las aristas representan la capacidad máxima de un canal: velocidad de una conexión, cantidad máxima de tráfico, voltaje de una línea eléctrica, volumen máximo de agua, etc.
  
  ![image](https://user-images.githubusercontent.com/80422357/200202568-d14fc476-45d2-47a9-885f-ccf65d92cc50.png)

- ### Ruta Crítica
  El método de la ruta crítica (CPM, por sus siglas en inglés) es una técnica que te permite identificar las tareas que se necesitan para realizar un proyecto.
  La ruta crítica en la gestión de proyectos es la secuencia más larga de actividades que deben finalizarse a tiempo para completar la totalidad del proyecto.

  El método de la ruta crítica es una técnica que te permite identificar las tareas necesarias para finalizar un proyecto y determinar cierta flexibilidad en el cronograma. Una ruta crítica en la gestión de proyectos es la secuencia más larga de actividades que deben finalizarse a tiempo para completar todo el proyecto. Cualquier retraso en las tareas críticas provocará el retraso del resto del proyecto.

  El método de la ruta crítica tiene como fin identificar las tareas más importantes del cronograma del proyecto, detectar las dependencias de las tareas y calcular la duración de las tareas.

  El método de la ruta crítica fue desarrollado a fines de la década de 1950 como un método para dar solución al aumento de los costos producido por la planificación ineficiente. Desde entonces, se usa con frecuencia para planificar proyectos y priorizar tareas. Te ayuda a desglosar tareas complejas en tareas individuales y a tener una idea general de la flexibilidad de un proyecto
  ![image](https://user-images.githubusercontent.com/80422357/200202624-f295682c-fa9a-4766-944c-ee333dc912fe.png)

- ### Ruta más Corta
  Con el algoritmo de Dijkstra, puedes encontrar la ruta más corta o el camino más corto entre los nodos de un grafo. Específicamente, puedes encontrar el camino más corto desde un nodo (llamado el nodo de origen) a todos los otros nodos del grafo, generando un árbol del camino más corto.

  Este algoritmo es usado por los dispositivos GPS para encontrar el camino más corto entre la ubicación actual y el destino del usuario. Tiene amplias aplicaciones en la industria, especialmente en aquellas áreas que requieren modelar redes.
  Aspectos básicos del algoritmo de Dijkstra
  - El algoritmo de Dijkstra básicamente inicia en el nodo que escojas (el nodo de origen) y analiza el grafo para encontrar el camino más corto entre ese nodo y todos los otros nodos en el grafo.
  - El algoritmo mantiene un registro de la distancia conocida más corta desde el nodo de origen hasta cada nodo y actualiza el valor si encuentra un camino más corto.
  - Una vez que el algoritmo ha encontrado el camino más corto entre el nodo de origen y otro nodo, ese nodo se marca como "visitado" y se agrega al camino.
  - El proceso continúa hasta que todos los nodos en el grafo han sido añadidos al camino. De esta forma, tenemos un camino que conecta al nodo de origen con todos los otros nodos siguiendo el camino más corto posible para llegar a cada uno de ellos.

## Unidad 3

Los actores principales en una situación de colas son el liente y el servidor. Los clientes llegan a una nstalación (servicio) desde de una fuente. Al llegar, n cliente puede ser atendido de inmediato o esperar n una cola si la instalación está ocupada.
![image](https://user-images.githubusercontent.com/80418452/201412465-8c867d1b-eb55-49ac-948d-155be7946ba6.png)

### Propiedad de Falta de Memoria
La propiedad totalmente aleatoria de la exponencial se onoce como olvido o falta de memoria. Dado que f(t) es distribución exponencial del tiempo t, entre eventos ucesivos (llegadas), si S es el intervalo desde la ocurrencia el último evento
![image](https://user-images.githubusercontent.com/80418452/201412684-b69e339b-31fd-4e86-9495-a5e77f28fbbf.png)

![image](https://user-images.githubusercontent.com/80418452/201413345-9b7c17d8-6fd0-4f1a-a2af-de65f5ab7e76.png)

### rincipio de tasa de entrada igual la tasa de salida

![image](https://user-images.githubusercontent.com/80418452/201413551-cbb1fad8-ddb7-4548-a09e-19a52fa8e18a.png)


### robabilidades de Estado Estable

Cuando un modelo de líneas de espera se basa en el proceso de acimiento y muerte, de manera que el estado del sistema
n representa el numero de clientes en el sistema de colas, las medidas clave de desempeño del sistema (L, Lq, W y Wq) se pueden obtener de inmediato después de calcular las Pn mediante las formulas anteriores.

![image](https://user-images.githubusercontent.com/80418452/201413910-2f63e0fe-4909-469e-8702-650fc612ee6b.png)





