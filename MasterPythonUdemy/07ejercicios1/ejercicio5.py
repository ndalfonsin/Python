"""
tenemos que hacer un programa que muestre todos los numeros entre dos numeros que diga
el usuario
"""
print("Te mostrare todos los numeros entre dos que elijas!!")

numero_1 = int(input("Cual es el primer numero?: "))
numero_2 = int(input("Cual es el segundo numero?: "))

if numero_1 < numero_2:

    for contador in range(numero_1, numero_2):
        print(contador)
else:
    print("el numero 1 debe ser menor al numero 2")
