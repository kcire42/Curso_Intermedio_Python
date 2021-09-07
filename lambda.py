#Se conocen como funciones anonimas 
#Funciones que no tiene un identificador (nombre)
#Estructura lambda argumentos:expresion 
#Solo se puede tener una sola linea de codigo 
#palindromo = lambda string : string == string[::-1]
#Nombre de la funcion lambda = lambda variable que se va a usar : condicion a aplicar en la variable 
#como resultado va a regresar un true o false



palindromo = lambda palabra : palabra == palabra[::-1]
print(palindromo('ana'))
suma = lambda  y,z : y+z
print(suma(2,3))

#ORDEN SUPERIOR
#Funcion de orden superior es una funcion que recive como parametro otra funcion y ejecuta una tarea 
#EJEMPLO FUNCION DE ORDEN SUPERIOR
def saludo(funcion):
    funcion()
def hola():
    print("Hola")
def adios():
    print("adios")
saludo(hola)
saludo(adios)
numeros = [1,2,3,4,5,6,7,8,9,10]
#FUNCION FILTER
#La funcion filter se usa para filtra una lista de codigo
pares = list(filter(lambda x: x%2 !=0,numeros))
print(pares) 
palindromo = lambda palabra : palabra == palabra[::-1]
print(palindromo('ana'))
#FUNCION MAP
#Hacer numeros elevados 
#Filtra numeros pares y multiplicarlos por dos con list comprehensions
numeros = [1,2,3,4,5,6,7,8,9,10]
pares = [i for i in numeros if i % 2 ==0]
pares_dobles = [i*2 for i in numeros if i % 2 ==0]
print(pares)
print(pares_dobles)
#filtrar numeros para y elevarlos y multiplicarlos por dos con for
dobles_for =[]
for i in numeros:
    if i % 2 ==0: 
        dobles_for.append(i*2)
print(dobles_for)
#doblar numeros en una lista con map
cuadrados = list(map(lambda x: x**2,numeros))
print(cuadrados)

#FUNCION REDUCE 
#SE UTILIZA CUNADO QUIERO REDUCIR LOS TERMINO DE UNA LISTA
from functools import reduce
dos = [2,2,2]
multiplicar = reduce(lambda a,b : a*b , dos)
print(multiplicar)

