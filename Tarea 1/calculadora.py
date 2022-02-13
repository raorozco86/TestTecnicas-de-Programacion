from verificarPalindromo import esPalindromo
from verificarPrimo import esPrimo


primerNumero = float(input("Introduce tu primer número: ") )
segundoNumero = float(input("Introduce tu segundo número: ") )
continuar= "Presione Enter para continuar"

opcion = 0
while True:
    print("""
    Dime, ¿qué quieres hacer?
    
    1) Sumar dos números
    2) Restar dos números
    3) Multiplicar dos números
    4) Dividir dos numero
    5) Valida si un Numero es Primo
    6) Consultar si un Numero es palindromo
    7) Cambiar los números elegidos
    8) Apagar calculadora
    """)
    opcion = int(input("Elige una opción: ") )  
   

    if opcion == 1:
        print(" ")
        resultadoOperacion= primerNumero+segundoNumero
        print("El resultado de sumar",primerNumero,"+",segundoNumero,"es igual a",resultadoOperacion)
         
        #Palindromo 
        comprobarPalindromo=int(resultadoOperacion)
        comprobarPalindromo = abs(comprobarPalindromo)
        if esPalindromo(comprobarPalindromo):
            print("El número es palíndromo")
        else:
            print("El número no es palíndromo") 
            print(" ")
             

        #Comprobar numero primo
        consultarPrimo= int(resultadoOperacion )
        consultarPrimo=abs(consultarPrimo)

        if esPrimo(consultarPrimo):
            print(" Ademas el numero es PRIMO")
            
        else:
           print("El numero NO es PRIMO")
        print("")

        
        input(continuar)


       

    elif opcion == 2:
        print(" ")
        resultadoOperacion= primerNumero-segundoNumero
        print("El resultado de restar",primerNumero,"-",segundoNumero,"es igual a",resultadoOperacion)
       
         #Comprobar palindromo
        comprobarPalindromo=int(resultadoOperacion)
        comprobarPalindromo = abs(comprobarPalindromo)
        if esPalindromo(comprobarPalindromo):
            print("El número es palíndromo")
        else:
            print("El número no es palíndromo") 
            print(" ")
            
         #Comprobar numero primo
        consultarPrimo= int(resultadoOperacion )
        consultarPrimo=abs(consultarPrimo)

        if esPrimo(consultarPrimo):
            print(" Ademas el numero es PRIMO")
            
        else:
           print("El numero NO es PRIMO")
        print("")
 
        input(continuar)

                
    elif opcion == 3:
        print(" ")
        resultadoOperacion = primerNumero*segundoNumero
        print("El producto de multiplicar",primerNumero,"x",segundoNumero,"es igual a",resultadoOperacion)
        
        #Palindromo
        comprobarPalindromo=int(resultadoOperacion)
        comprobarPalindromo = abs(comprobarPalindromo)
        if esPalindromo(comprobarPalindromo):
            print("El número es palíndromo")
        else:
            print("El número no es palíndromo") 
            print(" ")  
        
        #Comprobar numero primo
        consultarPrimo= int(resultadoOperacion )
        consultarPrimo=abs(consultarPrimo)

        if esPrimo(consultarPrimo):
            print(" Ademas el numero es PRIMO")
            input(" ")
        else:
           print("El numero NO es PRIMO")
        print("")
       
        input(continuar)

    elif opcion == 4:
            print(" ")
            try:
                resultadoOperacion= primerNumero/segundoNumero
            except ZeroDivisionError:
                    print("LA DIVISION DE CUALQUIER NUMERO ENTRE 0, NO SE PUEDE REALIZAR!!!!!!!!!!!") 
                    resultadoOperacion=0
                    
                                                            
            else:
                resultadoOperacion = primerNumero/segundoNumero
                print("El resultado de dividir",primerNumero,"÷",segundoNumero,"es igual a",resultadoOperacion)
                
            #Palindromo
            
            comprobarPalindromo=int (resultadoOperacion)
            comprobarPalindromo = abs(comprobarPalindromo)
            if esPalindromo(comprobarPalindromo):
               print("El número es palíndromo")
               
            else:
               print("El número no es palíndromo") 
               print(" ")
               input (continuar)  

             #Comprobar numero primo
            consultarPrimo= int(resultadoOperacion )
            consultarPrimo=abs(consultarPrimo)

            if esPrimo(consultarPrimo):
                print(" Ademas el numero es PRIMO")
                input(" ")
            else:
                print("El numero NO es PRIMO")
                print("")
       
            input(continuar)      
    
    elif opcion == 5:
        print("Indica si el valor es Primo")

        consultarPrimo= int(input("Digite numero a consultar:   ") )
        consultarPrimo=abs(consultarPrimo)

        if esPrimo(consultarPrimo):
            print("El numero es PRIMO")
        else:
           print("El numero no es PRIMO")
        print("")

        
        input(continuar)
    
    elif opcion == 6:
        print("Indica si el valor es un numero palindromo")

        consultarPalindromo= int(input("Digite numero a consultar:   ") )
        
        comprobarPalindromo = abs(consultarPalindromo)
        if esPalindromo(comprobarPalindromo):
               print("El número es palíndromo")
               input(" ")
        else:
               print("El número no es palíndromo") 
               print(" ")
               input ("presione una tecla para continual")
                    

    elif opcion == 7:
        primerNumero = float(input("Introduce tu primer número: ") )
        segundoNumero= float(input("Introduce tu segundo número: ") )
    
    elif opcion == 8:
        print("Hasta la proxima")
        break
        input(" ")
    else:
        print("Opción incorrecta")
        input(continuar)