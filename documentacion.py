#Impresion por pantalla 
from unittest import TestCase, result

"""
print("Hola mundo") 

#Esto es un comentario

"""
"""
Esto tambien es un comentario
 pero puede ser mas largo

"""
"""
"""
#---VARIABLES Y TIPOS---
"""
Una variable es un contenedor de informacion que dentro guardara un dato,
se puede crear muchas variables y que cada una tenga un dato distinto. 
Al transcurrir el codigo puede que la variable tome o adopte otros valores. 

"""
"""
#variable de tipo string
texto = "Master en python"
print(texto)
print(type(texto)) #con type() sabemos que tipo de dato es

#variable de tipo entero (INT)
textonumerico = 1
texto = textonumerico

print(textonumerico)
print(type(textonumerico))
"""
""" 
una variable puede comenzar siendo de un tipo pero esto puede verse modificado ya que python es un lenguaje 
altamente tipado, entonces el mismo programa ya reconoce el tipo de variable
"""
"""
numero = 56 
print(numero)
print(type(numero))

#variable de tipo decimal
decimal = 6.8
print(decimal)
print(type(numero))

#booleano
bool = False
print(bool)

#listas, tuplas y diccionarios

lista = [10, 20, 30, 50]
listastring = ["ilorem", 40, "ipsum"]
print(f"{lista} {listastring}")
tuplanocambia = ("master", "en", "python")
diccionario = {
    "nombre":"jane",
    "apellido":"doe",
    "curso":"master en python"
}

print(tuplanocambia)
print(diccionario)

#rango

rango = range(9)
print(rango,type(rango))

#byte
dato_byte = b"probando"
print(dato_byte,type(dato_byte))

#---Concatenacion---

#variables
nombre = "jane"
apellido = "doe"
web = "janedoe.web"

#concatenacion sumando las variables
print(nombre + " "+apellido+" "+web)

#concatenacion con la letra f
print(f"{nombre} {apellido} {web}")

#la letra f sirve tambien para concatenar variables en otras variables
web= f"{nombre} {apellido} janedoe.web"
print(web)

#concatenacion con la funcion .format
print("hola me llamo {} {} y mi web es {}".format(nombre, apellido, web))

"""
"""
solo se puede concatenar variables del mismo tipo
en todo caso usar str(), int(), float(), bool()
"""
"""

#---OPERADORES---

#operadores aritmeticos

numero1 = 77
numero2 = 44

numerosuma = numero1 + numero2
numeroresta = numero1 - numero2
numerodiv = numero1 / numero2
numeromult = numero1*numero2
numerorest = numero1 % numero2

print(f"La suma es: {numerosuma}, la resta es: {numeroresta}, la division es: {numerodiv} y la multiplicacion es: {numeromult}")
print(f"EL resto de la division de {numero1} por {numero2} es: {numerorest}")

#incremento y decremento

edad = 55
edad += 5 #le sumo a la edad 5

print(edad)

edad -= 5 #le resto a la edad 5
edad /= 5 #divido la edad por 5
edad *= 2 #multiplico la edad por 2

print(edad)


#---ENTRADA Y SALIDA DE DATOS---

#entrada

nombre = input("¿Cual es tu nombre?: ")
edad = input("¿Cual es tu edad?: ")

#salida
print(f"me alegro de conocerte {nombre} y veo que tienes {edad} años")



#---ESTRUCTURAS CONDICIONALES Y BUCLES---

"""
"""
Es una estructura de control que permite controlar el flujo
del programa, es decir si un dato cumple una condicion se van a ejecutar un grupo 
de instrucciones, y si no se ejecutaran otro grupo de instrucciones 
"""
"""
#if-else

auto = "rojo"

if auto == "rojo":
    print("El auto es rojo")
else:
    print("EL auto no es rojo")


#operadores de comparacion 
"""
"""
== IGUAL
!= DIFERENTE
< MENOR QUE
> MAYOR QUE
<= MENOR O IGUAL QUE
>= MAYOR O IGUAL QUE

"""
"""
year = int(input("que año es?"))

if year <= 2024 or year == 2023:
    print("todavia no cumples la mayoria de edad")
else:
    print("ya eres mayor de edad")

#if´s anidados

"""
"""
Programa que comprueba si una persona es mayor de edad y si es mayor, se mostrara su nombre.
comprobar de que continente es esta persona
"""
"""
nombre = input("Cual es tu nombre?")
edad = int(input("Cual es su edad?"))
ciudad = input("Cual es tu ciudad actual de residencia?")
continente = input("En que continente reside?")
mayoria_edad = 18

if edad >= mayoria_edad:
    print(f"{nombre} es mayor de edad")
    if continente != "Europa":
        print(f"{nombre} no es ciudadano europeo")
    else:
        print(f"{nombre} es europeo y de {ciudad}")
else:
    print(f"{nombre} no es mayor de edad")

"""

"""
Crear un programa al que se le inserte un numero y en base a ese numero me imprima 
el dia de la semana que es.
1- lunes
2- martes
3- miercoles
4- jueves
5- viernes
6- sabado
7- domingo
"""
#numero_dia = int(input("inserte el numero de dia de la semana:"))

"""
if numero_dia == 1:
    print("Hoy es lunes!")
else:
    if numero_dia == 2:
        print("Hoy es martes")
    else:
        if numero_dia == 3:
            print("Hoy es miercoles")
        else:
            if numero_dia == 4:
                print("hoy es jueves")
            else:
                if numero_dia == 5:
                    print("hoy es viernes")
                else:
                    if numero_dia == 6:
                        print("hoy es sabado")
                    else: 
                        print("Hoy es domingo")



#como hacer lo mismo pero aun mas sencillo 

if numero_dia == 1:
    print("Es lunes")
elif numero_dia == 2:
    print("Es martes")
elif numero_dia == 3:
    print("Es miercoles")
elif numero_dia == 4:
    print("Es jueves")
elif numero_dia == 5:
    print("es viernes")
elif numero_dia == 6:
    print("es sabado")
elif numero_dia == 7:
    print("es domingo")
elif numero_dia< 1 or numero_dia > 7: #VEFICICACION DE LOS VALORES INGRESADOS POR EL USUARIO
    print("los valores ingresados son incorrectos")

"""
"""
Multiples condiciones
realizar un programa que compruebe si una persona esta en edad de trabajar
"""
#---BUCLES FOR--- 

"""
for variable in elemento_iterable (lista, rango, etc)
    BOQUE DE CONDICIONES
"""
"""
contador = 0
suma_tot = 0

for contador in range(0,5):
    print(f"Voy por el: {str(contador)}")
    suma_tot = suma_tot + contador
    #suma_tot += contador

print(f"EL resultado es: {suma_tot}")
"""
"""
EJEMPLO DE TABLA DE MULTIPLICAR
"""
"""

numero_usuario = int(input("ingrese el numero del cual desea conocer la tabla: "))
numero_tabla = 0

#Pequeña validacion que con un bucle while cumpliria a la perfeccion su propocito
if numero_usuario < 1 or numero_usuario>10:
    print("los valores ingresados no son validos")
    numero_usuario = int(input("ingrese el numero del cual desea conocer la tabla"))
else: 
    for numero_tabla in range(0,11):
        print(f"{numero_usuario} x {numero_tabla} = {numero_usuario*numero_tabla}")
    else:
        print("tabla finalizada")

"""

#---BUCLES WHILE---

print("hola mundo")



