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
- ### Flujo Máximo
- ### Ruta Crítica
- ### Ruta más Corta

## Unidad 3
