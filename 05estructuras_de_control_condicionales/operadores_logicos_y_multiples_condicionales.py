#como se hacen varias condiciones dentro de un mismo if
#EJEMPLO 5
print("\n####################### EJEMPLO 5 #################")
"""
queremos saber si una persona esta en edad apta para trabajar, rango entre 18 y 65
"""
edad_minima = 18
edad_maxima = 65
#edad_oficial= int(input("que edad tienes?: "))
edad_oficial = 18

"""
if edad_oficial >= 18:
    print("esta en edad de trabajar!!!!")
else:
    print("no esta en edad de trabajar!!!")
"""

#para agregar una segunda condicion en el if se utiliza un operador logico (and)
#se ejecutan todas si todas son correctas, sino pega un salto

if edad_oficial >= 18 and edad_oficial <= 65:
    print("esta en edad de trabajar!!!!")
else:
    print("no esta en edad de trabajar!!!")  
    

"""
OPERADORES LOGICOS
and = y
or = o
! = negacion
not = no
"""

#EJEMPLO 6 
print("\n############ EJEMPLO 6 ##########")
"""
pais = "alemania"

if pais == "mexico" or pais == "españa" or pais == "colombia" or pais == "argentina" or pais == "chile":
    print(f"{pais} Es un pais de habla hispana")
else:
    print(f"{pais} no es un pais de habla hispana")

#formato:(x) o (x) o (x):
"""
#EJEMPLO 7
"""
print("\n############ EJEMPLO 7 ##########")

pais = "españa"

if not (pais == "mexico" or pais == "españa" or pais == "colombia" or pais == "argentina" or pais == "chile"):
    print(f"{pais} NO es un pais de habla hispana")
else:
    print(f"{pais} si es un pais de habla hispana")
    
#con el Not se dice que "SI NO"
"""
#EJEMPLO 8
print("\n############ EJEMPLO 8 ##########")

pais = "españa"

if pais != "mexico" and pais != "españa" and pais != "colombia" and pais != "argentina" and pais != "chile":
    print(f"{pais} NO es un pais de habla hispana")
else:
    print(f"{pais} si es un pais de habla hispana")

#El != significa negacion


