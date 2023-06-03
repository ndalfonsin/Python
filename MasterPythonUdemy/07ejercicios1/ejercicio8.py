"""crear un programa que nos permita sacat el x % de un numero ingresado por el usuario"""

numero = int(input("introduce el numero del que deseas saber el porcentaje: "))
porcentaje = int(input("introduce el porcentaje que deseas (solo numeros sin signos): "))

operacion = (numero * (porcentaje/100))

print(f"El {porcentaje}% de {numero} es: {operacion}")
