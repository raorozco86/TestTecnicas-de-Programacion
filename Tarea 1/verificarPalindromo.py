

def esPalindromo(comprobarPalindromo):
        numeroInvertido = invierteNumero(comprobarPalindromo)
        return comprobarPalindromo == numeroInvertido 

def invierteNumero(comprobarPalindromo):
    numeroInvertido = 0
    while comprobarPalindromo > 0:
        digito = comprobarPalindromo % 10
        numeroInvertido *= 10
        numeroInvertido += digito
        comprobarPalindromo //= 10
    return numeroInvertido



from calculadora import resultadoOperacion
comprobarPalindromo=int(resultadoOperacion)
comprobarPalindromo = abs(comprobarPalindromo)
if esPalindromo(comprobarPalindromo):
                print("El número es palíndromo")
else:
            print("El número no es palíndromo") 
            print(" ")
              


