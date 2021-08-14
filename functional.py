from functools import reduce
from random import choices,sample
import itertools
#lambda argumentos: expresion
data = [1, 2,3, 5]
print(list(map(lambda a: a*3, data)))
print(list(filter(lambda x: x%2 == 0, data)))
print(reduce(lambda a, b: a*b, data))
print(reduce(lambda x, y: x + (1 if y == 's' else 0), 'assntcs', 0))
print( list(map( len, [ [2, 3, 5, 7], [11,13,17,19], [23, 29], [31,37] ])) )
deseos=['amor','paz','trabajo','salud','felicidad','viajes']
print(choices(deseos,k=3))
print(sample(deseos,k=3))
print(choices(range(10,100)))

asignaturas = ['Matemáticas', 'Física', 'Química', 'Economía']
notas = [6.0, 3.5, 7.5, 8.0,4.4]
estado=['A','R','A','A',"R","R"]

a=list(zip(asignaturas,notas,estado))
print(a)
print(list(filter(lambda x: x[2]=="A",a)))

personas=[
 {'Nombre': 'Alicia', "Edad": 22, 'Sexo': 'F'},
    {'Nombre': 'Bob', "Edad": 25, 'Sexo': 'M'},
    {'Nombre': 'Charlie', "Edad": 33, 'Sexo': 'M'},
    {'Nombre': 'Diana', "Edad": 15, 'Sexo': 'F'},
    {'Nombre': 'Esteban', "Edad": 30, 'Sexo': 'M'},
    {'Nombre': 'Federico', "Edad": 44, 'Sexo': 'M'}
]

hombres = list(filter(lambda x: x['Sexo'] == 'M' and x["Edad"]>40, personas))
print(hombres)
suma_edades = reduce(lambda suma, p: suma + p["Edad"], hombres, 0)
print(suma_edades)

