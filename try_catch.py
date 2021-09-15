def main():
    try:
        numero = int(input("Ingrese el numero positivo"))
        #print(numero)
        try:
            if numero > 0:
                print(f"EL numero es positivo y es: {numero}")
        
            elif  numero < 0:
                raise ValueError("No se pueden colocar numero negativos")

        except ValueError as positivo:
            print(positivo)
    
    except ValueError:
        print("no acepto letras")
    
    
    


if __name__ == '__main__':
    main()