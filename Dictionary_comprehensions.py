
def main():
    #pass
    # diccionario ={}
    # for i in range (1,101):
    #     if i%3 != 0:
    #         diccionario.setdefault(i,i**3)
    # print(diccionario)
    # diccionario = {i:i**3 for i in range(1,101) if i % 3 !=0}
    # print(diccionario)
    diccionario = {i:round(i**(1/2),2) for i in range(1,101) }
    print(diccionario)
    


if __name__ == "__main__":
    main()
