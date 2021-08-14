from functools import reduce
from random import sample,shuffle
import itertools

estudiantes = [
{ "Nombre": "Alicia", "Ciudad": "Guayaquil", "Genero": "F", "Edad":18, "Universidad": "ESPOL"},
{"Nombre": "Renato", "Ciudad": "Quevedo", "Genero": "M", "Edad": 20, "Universidad": "Estatal de Quevedo"},
{"Nombre": "Fernando", "Ciudad": "Guaranda", "Genero": "M", "Edad": 24, "Universidad": "Estatal de Guaranda"},
{"Nombre": "Sofia", "Ciudad": "Guayaquil", "Genero": "F", "Edad": 22, "Universidad": "UG"},
{"Nombre": "Gregorio", "Ciudad": "Guayaquil", "Genero": "M", "Edad":20, "Universidad": "UEES"},
{"Nombre": "Carmen", "Ciudad": "Piñas", "Genero": "F", "Edad": 19, "Universidad": "ECOTEC"},
{"Nombre": "Arlette", "Ciudad": "Guayaquil", "Genero": "F", "Edad": 29, "Universidad": "ESPOL"},
{ "Nombre": "Pablo", "Ciudad": "Ambato", "Genero": "M", "Edad": 30, "Universidad": "ECOTEC"},
]

#Mostrar aquellos estudiantes que sean de la ECOTEC
print(list(filter(lambda x :x['Universidad']=="ECOTEC",estudiantes)))
#Mostrar aquellos estudiantes que sean de Guayaquil
print(list(filter(lambda x :x['Ciudad']=="Guayaquil",estudiantes)))
#Cuantos estudiantes son de ESPOL
print(reduce(lambda x, y: x + 1, list(filter(lambda x :x['Universidad']=="ESPOL",estudiantes)), 0))
#Contar cuantos estudiantes son de género femenino
print(reduce(lambda x, y: x + 1, list(filter(lambda x :x['Genero']=="F",estudiantes)), 0))
#Mostrar aquellos estudiantes mayores de 25 que sean de Guayaquil
print(list(filter(lambda x : x['Edad']>25 and x['Ciudad']=="Guayaquil",estudiantes)))
print("-"*135)
lista1=['Gabriel','Ana','Pedro','Diana','Liam','Iliana']
lista2=['Gladys','Fabian','Samantha','Luis','Pamela','Joel']
#Retornar lista1 con los elementos en mayúscula
print(list(map(lambda word: word.upper(), lista1)))
#Formar parejas con ambas listas y etornar dos parejas aleatorias
print(sample(list(zip(lista1,lista2)),k=2))
#Unir ambas listas y retornar una lista con todos los nombres dentro de ella
#Se usa chain para colocar el segundo argumento al final de la lista1
print(list(itertools.chain(lista1,lista2)))
#Mezclar los elementos de cada lista, unir ambas listas y retornar una lista con todos los nombres dentro de ella
shuffle(lista1)
shuffle(lista2)
print(list(zip(lista1,lista2)))


