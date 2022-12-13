print("Bienvenido, Programa el analisis.")

numero_1 = int(input("A: (1<1000: "))
numero_2 = int(input("B: (150000<10000000) "))

if numero_1 < numero_2:

    for contador in range(numero_1, numero_2):
        print(contador)
else:
    print("el numero 1 debe ser menor al numero 2")
