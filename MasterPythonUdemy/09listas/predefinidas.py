cantantes = ["GnfR", "Metallica", "Def Leppard"]
numeros = [1, 5, 6, 854, 965, 7458445, 215485, 8, 649494]

#ORDENAR
numeros.sort()
print(numeros)

#AÑADIR elementos
cantantes.append("MOTORHEAD")
print(cantantes)
cantantes.insert(0, "QUEEN") #PERO SE TIENE QUE SELECCIONAR EN QUE POSICION

print(cantantes)

#ELIMINAR ELEMENTOS
cantantes.pop(4)
print(cantantes)
#para eliminar por nombre
cantantes.remove("GnfR")
print(cantantes)    

#podemos dar vuelta una lista
numeros.reverse()
print(numeros)

#buscar dentro de una lista
print("QUEEN" in cantantes) #te devuelve un true

#contar elementos
print(len(cantantes))

#cuantas veces aparece un elemento en una lista
print(numeros.count(8)) #TE DEVUELVE LA CANTIDAD DE VECES
numeros.append(8)
numeros.append(8)
print(numeros.count(8))

#conseguir indice
print(cantantes.index("QUEEN"))

#unir listas
cantantes.extend(numeros)
print(cantantes)