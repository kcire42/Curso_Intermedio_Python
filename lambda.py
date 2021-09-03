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
