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

#filter
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
#La funcion filter se usa para filtra una lista de codigo
pares = list(filter(lambda x: x%2 !=0,numeros))
print(pares) 