continuar= "Presione ENTER para continuar"


def esPrimo(resultadoOperacion):
    if resultadoOperacion<1:
        return False
    elif resultadoOperacion==2:
        return True
    else:
        for comprobarPrimo in range(2, resultadoOperacion):
         if resultadoOperacion % comprobarPrimo == 0:
            print("Y ya que el ", resultadoOperacion, "tiene mas divisores")
            return False
    return True