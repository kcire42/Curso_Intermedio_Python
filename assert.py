def main():
    numero = input("Ingrese el numero positivo: ")
    assert  numero.isnumeric(), "Solo puedo agregar numeros"
    
    if int(numero) < 0:
        assert numero > 0, "no se pueden colocar numeros negativos"
    else:
        print(f"el numero es correcto: {numero}")
            

    
        
       
                
    


if __name__ == '__main__':
    main()