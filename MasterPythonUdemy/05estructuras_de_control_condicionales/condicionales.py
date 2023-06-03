#Estructura de control condicionales
#si un dato cumple con una condicion  se van a ejecutar ciertas condiciones, en caso que no se cumpla
#la ejecucion va a ser otro

"""
Si_se_cumple_esta_condicion:
    ejecutar grupo de instrucciones
SI NO:
    se ejecutan otros grupos de instrucciones
    """
"""
if condicion:
    instrucciones
else:
    otras instrucciones
    """

#ejemplo 1
print("\n############### Ejemplo1 ###########")
#== es una comparacion
color = "rojo" 

if color == "rojo":
    print("el color es ROJO")
else:
    print("el color no es rojo")

#ejemplo 1.1
numero = input("adivina mi numero favorito: ")

if numero == "3":
    print("enhorabuena!!")
    print("ese es mi numero favorito")
else:
    print("ese no es mi numero favorito")

#no solo se puede comparar con ==, sino tambien con otros operadores de comparacion
"""
== igual
!= diferente
> mayor que ALT+62
< menor que ALT+60
>= mayor o igual que
<= menor o igual que
"""
"""
OPERADORES LOGICOS
and = y
or = o
! = negacion
not = no
"""

#Ejemplo 2
print("\n***********************EJEMPLO2***************")

year = 2020
#year = int(input("¿En que año estamos?"))           #es para agregar el año, va sin el print
if year >= 2021:
    print("es el final del mundo")
else:
    print("es el comienzo del fin")

#IFs anidados EJEMPLO 3
print("\n############### EJEMPLO 3 ###########")

nombre = "Nicolas Alfonsin"
ciudad = "Mar del plata"
continente = "Americano"
edad = 22
mayoria_edad = 18

if edad >= mayoria_edad:
    print(f"{nombre} es mayor de edad !!")
    if continente != "europa":
        print("el usuario no es europeo")
        print(f"Es del continente {continente} y de la ciudad de {ciudad}")
    else:
        print(f"es europeo")

else: 
    print(f"{nombre} NO es mayor de edad")

#EJEMPLO 4
print("********************** EJEMPLO 4 *******************") 

dia = int(input("que dia de la semana es?: "))

"""
if dia == 1:
    print ("es lunes")
else:
    if dia == 2:
        print("es martes")
    else:
        if dia == 3:
            print("es miercoles")
        else:
            if dia == 4:
                print("es jueves")
            else:
                if dia == 5:
                    print("es viernes")
                else:
                    print("es fin de semana")
                    """

#estructura de control ELIF

if dia == 1:
    print("es lunes")
elif dia == 2:
    print("es martes")
elif dia == 3:
    print("es miercoles")
elif dia == 4:
    print("es jueves")
elif dia == 5:
    print("es viernes")
else:
    print("es fin de semana")
