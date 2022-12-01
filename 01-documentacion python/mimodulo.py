"""
Se definen las funciones o clases para realizar el modulo
"""

def holamundo(nombre):
    return f"Hola que tal estas, {nombre}"

def calculadora(numero1, numero2, basicas=False):

    suma = numero1 + numero2
    resta = numero1 - numero2
    div = numero1/numero2
    mult = numero1*numero2

    cadena = ""

    if basicas != False:
        cadena += "Suma: " + str(suma)
        cadena += "\n"
        cadena += "Resta: " + str(resta)
        cadena += "\n"
    else: 
        cadena += "Multiplicacion: " + str(mult)
        cadena += "\n"
        cadena += "Division: "+ str(div)
    
    return cadena 