from algo1 import *
from Set import *
import random
cantidad = random.randint(1,5)
vector1 = Array(cantidad,0)
cantidad2 = random.randint(1,5)
vector2 = Array(cantidad2,0)

for n in range(len(vector1)):
    vector1[n] = random.randint(1,10)
    
for j in range(len(vector2)):
    vector2[j] = random.randint(1,10)

print("Los vectores iniciales son")
print(vector1)
print(vector2)

print("Creando un set....")
vector1 = Create_set(vector1)
vector2 = Create_set(vector2)
print(vector1)
print(vector2)

print("Uniendo vectores...")
print(Union(vector1,vector2))

print("Intersectando vectores...")
print(Interseccion(vector1,vector2))

print("Diferenciando vectores...")
print(Difference(vector1,vector2))
