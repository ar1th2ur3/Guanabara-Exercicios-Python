import math
import random

n = random.randint(1, 2000)

#math.sqrt = Calcular raiz quadrada.
raiz = math.sqrt(n)

#math.ceil = Arredondamento para cima.
print(f"A raiz de {n} é {math.ceil(raiz)}")