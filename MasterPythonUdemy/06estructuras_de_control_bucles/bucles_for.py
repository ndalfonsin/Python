"""
el bucle for es una estructura que se va a repetir x cantidad de veces.
#for
for variable in elemento_iterable(lista,rango o datos que almacene mas datos dentro)
    bloque de instrucciones

mientras  que queden elementos en el elemnto interable va a crear una variable hasta que el elemento_interable
se termine
"""
"""
contador = 0

for contador in range(0,5):
    print("voy por el: " + str(contador))


voy por el: 0
voy por el: 1
voy por el: 2
voy por el: 3
voy por el: 4
voy por el: 5
"""

contador = 0
resultado = 0
for contador in range(0,10):
    print("voy por el: " + str(contador))

    resultado += contador 
print(f"el resultado es: {resultado}")

"""
voy por el: 0   
voy por el: 1
voy por el: 2
voy por el: 3
voy por el: 4 
voy por el: 5 
voy por el: 6
voy por el: 7 
voy por el: 8 
voy por el: 9 
"El resultado es: 45"
"""

#Ejemplo 1 tabla de multiplicar
print("\n######### EJEMPLO##########")

numero_usuario = int(input("¿De que numero quieres conocer la tabla?: "))

if numero_usuario < 1:
    numero_usuario = 1

print(f"### TABLA DE MULTIPLICAR DEL NUMERO {numero_usuario} ####")

for numero_tabla in range(1, 11):
    if numero_usuario == 45:
        print("no se pueden mostrar numeros prohibidos")
        #para cortar un bucle podemos usar la funcion break
        break
    print(f"{numero_usuario} x {numero_tabla} = {numero_usuario*numero_tabla} ")
else:
    print("tabla finalizada")

