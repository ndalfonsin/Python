"""
Ejercicios con listas:
hacer un programa que tenga una lista de 8 numeros enteros y haga lo siguiente:
-Hacer funcion que recorra listas de numeros y devuelta el resultado en un string
-ordenarla y mostrarla
-mostrar su longitud
buscar algun elemento en la lista (que pida el usuario)

"""

numeros = [3, 65, 90, 13, 27, 33, 7, 68]

#Recorrer y mostrar la lista
def mostrar_lista(lista):
    resultado = ""
    print("***** Recorrer y mostrar desde una funcion ******")

    for elemento in lista:
        
        
        resultado += str(f"Elemento: {elemento}")
        resultado += "\n"
    
    return resultado

print(mostrar_lista(numeros))

#Ordenar y mostrar
print("***** Ordenar y mostrar ******")
numeros.sort()
print(mostrar_lista(numeros))

#Mostrar longitud
print(f"la lista tiene {len(numeros)} elementos")

#Busqueda en la lista
def busqueda(lista):
    busqueda = int(input("Introduce el numero que quieres buscar: "))

    comprobar = isinstance(busqueda, int)
    while not comprobar or busqueda <= 0:
        busqueda = int(input("Introduce el numero que quieres buscar: "))
    else:
        print(f"Has introducido el {busqueda}")

    search = lista.index(busqueda)

    print(f"EL numero esta en el indice: {search}")

print("BUSQUEDA DE UN NUMERO")
busqueda(numeros)
