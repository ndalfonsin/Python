"""
Modulos: funcionalidades ya hechas para reutilizar
en python por defecto hay muchos modulos.

podemos conseguir modulos que ya vienen en el lenguaje, en internet y  crear nuestros modulos

hay que guardar en el modulo diferentes funciones para luego exportarlas

#from mimodulo import *
#import mimodulo
from mimodulo import calculadora
print(calculadora(3, 5, True))

#MODULO FECHAS
import datetime

print(datetime.date.today())

fecha_completa = datetime.datetime.now()
print(fecha_completa)
print(fecha_completa.year)
print(fecha_completa.month)
print(fecha_completa.day)


fecha_personalizada = fecha_completa.strftime("%d/%m/%Y, %H:%M:%S")

print(fecha_personalizada)

print(datetime.datetime.now().timestamp())
print(datetime.datetime.now().timestamp())

# Modulo de matematicas
import math

print("raiz cuadrada de 10:", math.sqrt(10))
print("numero pi:", float(math.pi))
print("redondear: ",math.ceil(6.2321345348435843))
print("redondear: ",math.floor(6.2321345348435843))

#numero aleatorio, random
import random
print("numero aleatorio entre 15 y 67:", random.randint(15, 67))


"""