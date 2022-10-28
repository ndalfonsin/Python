"""
Ejercicio 6 
Mostrar todas las tablas de multiplicar de todos los numeros del 1 al 10
mostrando titulo de la tabla y luego las multiplicaciones del 1 al 10
"""


for cabecera in range(1,11):
    print(f"""
-----------------------
### Tabla del {cabecera} ###
-----------------------   
""")

    
    contador = 1

    while contador <= 10:
        mult = cabecera * contador
        print(f"{cabecera} X {contador} = {mult}")
        contador += 1



"""
Ejercicio 7 
hacer un programa que muestre todos los numeros impares entre 2 numeros que elija el usuario
"""

numeroU1 = int(input("Inserte el primer numero: "))
numeroU2 = int(input("inserte el segundo numero: "))

if numeroU1 > numeroU2:
    for contador in range((numeroU2 + 1),(numeroU1)):
        if contador % 2 !=0:
            print(contador)
elif numeroU1 < numeroU2:
    for  contador in range((numeroU1 + 1), (numeroU2)):
        if contador % 2 !=0:
            print(contador)
else:
    print(f"{numeroU1} = {numeroU2}")

