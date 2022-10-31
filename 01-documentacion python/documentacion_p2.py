"""
---FUNCIONES---
una funcion es un conjunto de instrucciones que se agrupan bajo un grupo concreto y que es reutilizable, puede llamarsela cuantas veces se desee

def nombre_de_funcion(parametros):
    #bloque/conjunto de instrucciones

nombre_de_funcion(mi_parametro)
nombre_de_funcion(mi_parametro)

"""
"""
#EJEMPLO 1: muestra nombre de personas

#Definir funcion
from unicodedata import decimal


def muestra_nombre():
    print("Tomas")
    print("Juan")
    print("Lorena")
    print("Ignacio")
    print("Maria")
    print("\n")

#Invocar funcion
muestra_nombre()


#PARAMETROS EN FUNCIONES

def muestra_nombre(nombre, edad):
    print(f"Tu nombre es: {nombre}")

    if edad >= 18:
        print(f"{nombre} es mayor de edad y tiene: {edad}")
    else:
        print(f"{nombre} es menor de edad.")

muestra_nombre("Jane doe", 40)

#Pero tambien puedo pedir al usuario que me pase el parametro

nombre = input("Dime tu nombre: ")
edad = int(input("Dime tu edad: "))
muestra_nombre(nombre, edad)

#Ejemplo 2:
""" 
"""
 Realizar una funcion que le pregunte al usuario la tabla de multiplicar de un numero en concreto y se lo muestre completo del 1 al 10
"""
"""
def tabla_multiplicar(numero):
    contador = 1
    print(f"*** Tabla del {numero} ***")

    while contador <= 10:
        mult = numero * contador
        print(f"{numero} X {contador} = {mult}")
        contador += 1

numero = int(input("La tabla de que numero desea conocer?: "))

tabla_multiplicar(numero)

"""
"""
Realizar la multiplicacion de dos numeros
"""
"""
def multiplicacion(numero, numero2):
    print(f"{numero} X {numero2} = {numero*numero2}")

print("MULTIPLICACION DE DOS NUMEROS")

numero = int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))

multiplicacion(numero,numero2)

"""

#