"""
Una funcion es un conjunto de instrucciones agrupadas bajo un nobre concreto que pueden reutilizarse
invocando la funcion cuantas veces sea necesario.

def nombredemifuncion(parametros):
    #bloque/conjunto de instrucciones

nombredemifuncion(mi_parametro)



#Ejemplo 1 
print("########### EJEMPLO 1 #########")

def muestra_nombres():
    print("Nicolas")
    print("Juan")
    print("Lu")
    print("Caro")
    print("Ro")
    print("Marco")
    print("\n")

#invocar funciones
muestra_nombres()   #ASI SE INVOCA UNA FUNCION
"""
"""###########PARAMETROS#############"""
#Ejemplo 2
"""
print("### EJEMPLO 2 ###")

def mostrartunombre(nombre, edad):
    print(f"tu nombre es: {nombre} ")

    if edad >= 18:
        print("eres mayor de edad")
    else:
        print("no eres mayor de edad, ve por tu mami!!")

nombre = input("dime tu nombre: ")
edad = int(input("¿Cual es tu edad?: "))
mostrartunombre(nombre, edad)


#Ejemplo 3 
print("### EJEMPLO 3 ###")
numero = int(input("dime el numero del que deseas conocer su tabla de multiplicar: "))
def tabla(numero):
    print(f"tabla de multiplicar del: {numero}")
   
    for contador in range(11):
        operacion = numero*contador
        print(f"{numero} x {contador} = {operacion}")
    
    print("\n")

tabla(numero)

#Ejemplo 4 
print("##### EJEMPLO 4 ######")

#parametros opcionales

def getempleado(nombre, ID = None):          #SI QUEREMOS QUE EL ID SEA OPCIONAL se le pone = false(o lo que sea)

    print("Empleado")
    print(f"Nombre: {nombre}")
    

    if ID != None:
        print(f"ID: {ID}")

        
getempleado("Nicolas Alfonsin")

"""
#SI SE DEFINE EL PARAMETRO SE VUELVE OPCIONAL

#EJEMPLO 5, parametros opcionales y return

#vamos a generar una pequeña calculadora
"""
def saludame(nombre):
    saludo = f"hola!, saludos {nombre}"
    
    return saludo

print(saludame("Nicolas Alfonsin"))

#EJEMPLO 6 CALCULADORA en str

def calculadora(numero1, numero2, basicas = False):

    suma = numero1 + numero2    
    resta = numero1 - numero2
    multi = numero1 * numero2
    div = numero1 / numero2

    cadena = ""

    if basicas != False:
        cadena += "suma: " + str(suma)
        cadena += "\n"
        cadena += "Resta: " + str(resta)
        cadena += "\n"
    else:
        cadena += "multiplicacion: " + str(multi)
        cadena += "\n"
        cadena += "division: " + str(div)

    return cadena
print(calculadora(5, 5, True))


"""
#EJEMPLO 7 
def getNombre(nombre):
    texto = f"El nombre es: {nombre}"
    return texto    

def getApellidos(apellidos):
    texto = f"Los apellidos son: {apellidos}"
    return texto 

def devuelvetodo(nombre , apellidos):
    texto = getNombre(nombre) + "\n" + getApellidos(apellidos)
    return texto

print(devuelvetodo("Nicolas" , "Alfonsin Churruca"))

#Ejemplo  8: FUNCIONES LAMBDA/ funcion anonima
print("##### EJEMPLO 8 ######")

dime_el_year = lambda year: f"El año es {year * 50}"

print(dime_el_year(2034))
