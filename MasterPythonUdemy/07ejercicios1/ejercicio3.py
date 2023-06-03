""" 
Ejercicio 3
escribir un programa que muestre los cuadrados (un numero multiplicado por si mismo) de los primeros 
60 numeros naturales. Resolver con for y while"

# WHILE
"""

contador = 1

while contador <=60:
    
    cuadrado = contador*contador
    print(f"El cuadrado de {contador} es {cuadrado}")

    contador += 1

#for

contador = 1 


for contador in range(1, 61):
    cuadrado = contador*contador
    print(f"El cuadrado de {contador} es {cuadrado}")



