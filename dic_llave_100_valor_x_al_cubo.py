
'''Generar numeros de 1 al 1000 con listas y Diccionarios'''
def main():
    numeros = {}
    for i in range(100):
        numeros.setdefault(i, i**2)
    print(numeros)




if __name__ == '__main__':
    main()