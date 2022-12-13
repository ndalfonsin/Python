def holaMundo(nombre):
    return f"hola que tal estas, {nombre}"

def calculadora(numero1, numero2, basicas = False):

    suma = numero1 + numero2    
    resta = numero1 - numero2
    multi = numero1 * numero2
    div = numero1 / numero2

    cadena = ""

    if basicas != False:
        cadena += "suma: " + str(suma)
        cadena += "\n"
        cadena += "Resta: " + str(resta)
        cadena += "\n"
    else:
        cadena += "multiplicacion: " + str(multi)
        cadena += "\n"
        cadena += "division: " + str(div)

    return cadena

