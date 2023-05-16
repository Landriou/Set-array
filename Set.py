from algo1 import *
#Funciones de Create_Set

def repetidos(array):
  repetido = 0
  for n in range(len(array)):
    for j in range(n+1, len(array)):
        if array[n] == array[j] and array[j]!= None:
          array[j] = None
          repetido = repetido + 1
        
  return repetido

def unicidad(array, arraysinrepetidos):
  i = 0
  for n in range(len(array)):
    if array[n] == None:
      print("Eliminando elemento repetido ")
    else:  
      arraysinrepetidos[i] = array[n] 
      i= i + 1
  return arraysinrepetidos


def Create_set(array):
  Arrayunico = Array(len(array) - repetidos(array), 0)
  array = unicidad( array , Arrayunico)
  return array

#Funcion union, toma 2 vectores y los transforma en 1(sin elementos repetidos)

def Union(vector1, vector2):
  k = 0
  vector1 = Create_set(vector1)
  vector2 = Create_set(vector2)
  lentotal = len(vector1) + len(vector2)    #Hago un vector que sea del tamaño de ambos vectores
  vectorunion = Array(lentotal,0)         
  for n in range(len(vector1)):       #Paso los elementos del primer vector al vector resultante
    vectorunion[n] = vector1[n]
  for i in range(len(vector1), lentotal): #Hago lo mismo pero a partir de donde se quedo
    vectorunion[i] = vector2[k]
    k = k + 1
  vectorunion = Create_set(vectorunion) #Elimino los repetidos
  return vectorunion

def Interseccion(vector1, vector2):
  vector1 = Create_set(vector1)
  vector2 = Create_set(vector2)
  lenmaximo = 0                 #Veo cual tiene mayor longitud
  lenminimo = 0
  if len(vector1) > len(vector2):
    lenmaximo = len(vector1)
    lenminimo = len(vector2)
  else:
    lenmaximo = len(vector1)
    lenminimo = len(vector2)

  if len(vector1) == len(vector2):
    lenmaximo = len(vector1)
    lenminimo = len(vector2)

  comunes = 0
  k = 0
  for n in range(len(vector1)):
    for j in range(len(vector2)):
      if vector1[n] == vector2[j]:  #Veo los comunes entre ambos vectores para crear un vector
        comunes = comunes + 1       #igual a los comunes
  resultante = Array(comunes, 0)

  for i in range(len(vector1)):   #Recorro los vectores y paso los comunes
    for u in range(len(vector2)):
      if vector1[i] == vector2[u]:
        resultante[k] = vector2[u]
        k = k + 1        
  resultante = Create_set(resultante)

  return resultante


def Difference(vector1, vector2):
  vectorunion = Union(vector1, vector2)
  vectorinter = Interseccion(vector1,vector2)
  lentotal = len(vectorunion) - len(vectorinter)
  valor = 0
  k = 0
  resultante = Array(lentotal, 0)

  for n in range(len(vectorunion)):
    for j in range(len(vectorinter)):
      if vectorunion[n] == vectorinter[j]:
        valor = None
        break                   #Si encontro un igual rompo el bucle
      else:
        valor = vectorunion[n]      
    if valor != None:
      resultante[k] = valor     #Si no ha encontrado ningun igual lo pongo el vector
      k = k + 1

  if len(vectorinter) == 0:
    resultante = vectorunion
  resultante = Create_set(resultante)
  return resultante