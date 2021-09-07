
'''Lista comprehension'''
def main():
    cuadrado = []
    #for i in range(1,101):
        #lista_pequeña = [i,i**2]
        #cuadrado.append(lista_pequeña)
    #     lista_dos = [i,i**2]
    #     if i%3 == 0:
    #         cuadrado.append(lista_dos)
    # print(cuadrado)
    #list comprehensions
    lista = [ i for i in range (1,10000) if i % 4 == 0 and i % 6 == 0 and i % 9 == 0 ]
    print(lista)
    numeros = [1,2,3,4,5,6,7,8,9,10]
    pares = [i for i in numeros if i % 2 == 0 ]
    print(pares)
    elevados_doble = [i for i in pares]
    print(elevados_doble)



if __name__ == '__main__':
    main()