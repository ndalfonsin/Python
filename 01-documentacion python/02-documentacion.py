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

# Parametros opcionales

"""
Se le puede asignar un valor al parametro opcional o tan solo poner valor None y ejecutar el print en un if
"""
def getEmpleado(nombre, dni = None):
    
    print("Empleado")
    print(f"NOMBRE: {nombre}")
    if dni != None:
        print(f"DNI: {dni}")

#sin parametro dni
getEmpleado("Jane doe")

getEmpleado("Jane doe", "78437938")

#Ejemplo 3: Parametros opcionales y return o devolver datos

"""
crear una funcion que tenga las operaciones matematicas basicas

//Que es un return? y para que sirve
dentro de una funcion un return sirve para hacer imprimir por pantalla una variable dentro de una funcion. 


def saludame(nombre):
    saludo = f"Hola saludos {nombre}"
    
    return saludo

#Imprimir un return por consola
print(saludame("Jane"))

"""
"""
def calculadora(numero, numero2, operacion):

    
    if operacion == "S" or "s":
        result = numero + numero2
    elif operacion == "R" or "r":
        result = numero - numero2
    elif operacion == "M" or "m":
        result = numero * numero2
    elif operacion == "D" or "d":
        if numero2 != 0:
            result = numero / numero2
        else:
            result = "ERROR, DIVISION POR 0"
    else:
        result = "ERROR"
    return result

numero = int(input("inserte el primer numero: "))
numero2 = int(input("inserte el segundo numero: "))
operacion = input("'S' suma ; 'R' resta ; 'M' multiplicacion ; 'D' division : ")

print(calculadora(numero, numero2, operacion))

"""

#Ejemplo 4: Funciones dentro de otras funciones

def getnombre(nombre):
    texto = f"El nombre es {nombre}"
    return texto

def getapellido(apellido):
    texto = f"El apellido es {apellido}"
    return texto

def devuelve_todo(nombre, apellido):
    texto = getnombre(nombre) + "\n" + getapellido(apellido)
    return texto

print(devuelve_todo("Jane","Doe"))

#Ejemplo 5: FUNCIONES LAMBDA
#Son funciones para realizar acciones simples 

dime_el_year = lambda year: f"El año es {year+2}"

print(dime_el_year(2022))

"""
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
     CONSULTAR EL ARCHIVO DE FUNCIONES PREDEFINIDAS DE PYTHON '03-predefinidas.py'
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""

