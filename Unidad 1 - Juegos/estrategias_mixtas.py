from array import array
from copy import deepcopy
import numpy as np
import nashpy as nash
# Create the payoff matrix
A = np.array([[4, 0], [0, 2]])  # A is the row player
B = np.array([[2, 0], [0, 4]])  # B is the column player
game2 = nash.Game(A, B)
game2
# Find the Nash Equilibrium with Support Enumeration
def getEquilibrium(): return game2.support_enumeration()


print("3 lineas de salida")
# Jugador A tiene estrategias de arriba hacia abajo, Jugador B de izq a derecha
# los dos primeros son los equilbirios de nash pero proque sucede una tercera linea? Porque es un equilibrio de Nash con estrategia mixta
eq = getEquilibrium()
for item in eq:
    print(item)

# el resultado del equilibrio deberia ser el siguiente
# Jugador A 0.67*0.33*4 +0.33*0.67*0+0.33*0.67*0+0.33*0.67*2 =1.3266
# Jugador B 0.33*0.67*2 + 0.67*0.33*0 + 0.33*0.67*0+0.67*0.33*4 = 1.3266
eq = getEquilibrium()
sigma_r, sigma_c = [array for array in eq][-1]
pd = nash.Game(A, B)
pd[sigma_r, sigma_c]

print("punto de equilibrio con estrategias mixtas")
print(pd[sigma_r, sigma_c])
