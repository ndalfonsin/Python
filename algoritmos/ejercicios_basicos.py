"""
EJERCICIO 1
-crear 2 variables, "pais" y "continente"
-mostrar su valor por pantalla
-poner un comentario diciendo el tipo de dato
"""


pais = input("En que pais vives? ") #El tipo de dato es string
continente = input("En que contienente esta tu pais de residencia? ") #El tipo de dato es string

print(f"El usuario es de {pais} en el contienente {continente}")


"""
EJERCICIO 2
crear un script que te muestre todos los numeros positivos del 1 al 100
"""


contador = 1

for contador in range (0,101):
    if contador % 2 == 0:
        print(contador)


"""
EJERCICIO 3
crear un programa que imprima por pantalla los cuadrados de los primeros 60 numeros naturales
"""


contador = 0 

while contador <= 60:
    cuadrado = contador*contador
    print(f"El cuadrado de {contador} es = {cuadrado}")
    
    contador += 1

print("----------------------------------------------------------")

for contador in range (0,60):
    cuadrado = contador*contador
    print(f"El cuadrado de {contador} es = {cuadrado}")
    
    contador += 1


"""
Ejercicio 4
Pedir 2 numeros al usuario y realizar con ellos todas las operaciones basicas
"""


numero1 = int(input("Inserte el primer numero: "))
numero2 = int(input("Inserte el segundo numero: "))

suma = numero1 + numero2
print(f"SUMA: {numero1} + {numero2} = {suma}")

resta = numero1 - numero2
print(f"RESTA: {numero1} - {numero2} = {resta}")

mult = numero1 * numero2
print(f"MULTIPLICACION: {numero1} X {numero2} = {mult}")

#DIVISION ---> LA DIVISION POR 0 NO EXISTE, PRIMERO HAY QUE VALIDAR EL VALOR DE ENTRADA DE NUMERO 2 que sera el divisior

if numero2 != 0:
    div = numero1 / numero2
    print(f"DIVISION: {numero1} / {numero2} = {div}")
else:
    #cuando el divisor es = 0
    print(f"DIVISION: El divisor es {numero2}, no puede realizarse esta operacion")


"""
Ejercicio 5
realizar un programa que pida 2 numeros al usuario y que te muestre todos los numeros que hay entre este rango
"""


numeroU1 = int(input("Inserte el primer numero: "))
numeroU2 = int(input("inserte el segundo numero: "))

if numeroU1 > numeroU2:
    for contador in range((numeroU2 + 1),(numeroU1)):
        print(contador)
elif numeroU1 < numeroU2:
    for  contador in range((numeroU1 + 1), (numeroU2)):
        print(contador)
else:
    print(f"{numeroU1} = {numeroU2}")


