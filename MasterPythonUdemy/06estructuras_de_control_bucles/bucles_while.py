"""
estructura de control que itera o repite la ejecucion de una serie de instrucciones
tantas veces como sea necesario hasta que deje de cumplise la condicion

while condicion: 
    bloque de instrucciones
    actualizador de contador
"""
#vamos a mostrar todos los numeros hasta el 100

from typing import Container


contador = 1

while contador <= 100:
    print(f"estoy en el nuemro {contador}")
    contador = contador + 1

print("_____________________________________")
contador = 1
muestrame = str(0)

while contador <= 100: 
    muestrame = muestrame + ", " + str(contador)
    contador = contador + 1

print(muestrame)


#EJEMPLO 1

print("###### EJEMPLO ########")

numero_usuario = int(input("¿de que numero quieres la tabla?: "))

if numero_usuario < 1:

    numero_usuario = 1

print(f"### TABLA DEL {numero_usuario} ###")

contador = 1
while contador <= 10:
    print(f"{numero_usuario} x {contador} = {numero_usuario*contador} ")
    contador += 1
else: 
    print("tabla terminada")
    