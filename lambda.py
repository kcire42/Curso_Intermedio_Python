#Se conocen como funciones anonimas 
#Funciones que no tiene un identificador (nombre)
#Estructura lambda argumentos:expresion 
#Solo se puede tener una sola linea de codigo 
#palindromo = lambda string : string == string[::-1]
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
palindromo = lambda palabra : palabra == palabra[::-1]
print(palindromo('ana'))
#Funcion Filter












#Map
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