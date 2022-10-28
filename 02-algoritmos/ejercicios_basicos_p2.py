"""
Ejercicio 6 
Mostrar todas las tablas de multiplicar de todos los numeros del 1 al 10
mostrando titulo de la tabla y luego las multiplicaciones del 1 al 10
"""


for cabecera in range(1,11):
    print(f"""
-----------------------
### Tabla del {cabecera} ###
-----------------------   
""")

    
    contador = 1

    while contador <= 10:
        mult = cabecera * contador
        print(f"{cabecera} X {contador} = {mult}")
        contador += 1

