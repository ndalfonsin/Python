"""
hacer un progrma que tenga una lista con 8 numeros enteros
1-recorrerla y mostrarla
2- ordenarla y mostrarla
3- mostrar su longitud
4. buscar un elemento en base a lo que el ususario quiera buscar
"""

numeros = [1, 2, 5, 4, 9, 568, 69, 89, 77]

print("\n")

print("NUMEROS:")
print(numeros)
print("\n")

print("MOSTRAR NUMEROS:")
for numero in numeros:
    print(f"El numero es: {numero}")
print("\n")

print("ORDENAR NUMEROS: ")
numeros.sort()
print(numeros)
print("\n")

print("¿Cuantos numeros hay?: ")
print(len(numeros))
print("\n")

print("Busca si tu numero se encuentra registrado... ")
try:

    numeroU = int(input("¿Que numero deseas buscar?: "))
    print(numeroU in numeros)
except:
    print("El numero no esta en la lista")
    