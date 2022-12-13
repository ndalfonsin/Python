""" mostrar todos los numeros inpares entre dos que elija el usuario"""

print("Te mostrare todos los numeros inpares entre dos que elijas!!")
numero1 = int(input("cual es el primer numero?: "))
numero2 = int(input("cual es el segundo numero?: "))

if numero1 < numero2:
    for x in range((numero1), (numero2 + 1)):
        if x%2 == 0:
            print(f" {x} es PAR")
        else:
            print(f" {x} es IMPAR")

else:
    print("el numero 1 debe ser mas chico que el numero 2")