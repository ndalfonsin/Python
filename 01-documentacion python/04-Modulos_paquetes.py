#Modulos y paquetes
"""
Son funcionalidades ya hechas para reutilizar, se pueden crear o instalar 

www.docs.python.org/3/py-modindex.html //// modulos de python que ya vienen en el lenguaje
"""

#crear modulos:
"""
se crea un archivo con el nombre del modulo en la carpeta en la que se este trabajando
"""
"""
#Importar un modulo dentro de la carpeta
import mimodulo 

#Imprimir por consola las funciones dentro del modulo
print(mimodulo.holamundo("Nico"))

print(mimodulo.calculadora(1,2,True))

#si quisiera importar una sola funcion 
from mimodulo import holamundo

print(holamundo("Nico"))

#Para importar todas sin tener que poner mimodulo antes
from mimodulo import * 

"""

######################################################################################################

#Modulo de fechas

import datetime

print(datetime.date.today())  #fecha de hoy

fechacompleta = datetime.datetime.now()

print(fechacompleta) #fecha completa + hora
print(fechacompleta.day) #dia   
print(fechacompleta.month) #mes
print(fechacompleta.year) #año
print(fechacompleta.hour) #hora

#Personalizar fecha

fecha_personalizada = fechacompleta.strftime("%d/%m/%Y, %H:%M ")
print(fecha_personalizada)

########################################################################################################

#modulo de matematicas
import math

#sacar la raiz cuadrada de un numero

print("La raiz cuadrada de 10: ", math.sqrt(10))

print("Numero pi: ", float(math.pi))

print("Redondear", math.ceil(math.pi)) #Redondeo para arriba
print("Redondear", math.floor(math.pi)) #Redondeo para abajo

#Sacar numero aleatorio

import random

print("Numero aleatorio entre 15 y 67: ", random.randint(12,67))

########################################################################################################

"""
PAQUETES: es un conjunto de modulos que podemos utilizar para un programa
"""

