nombre = "Jane Doe"

#funcion para imprimir por pantalla
print(nombre)

#funcion type para conocer el tipo de dato
print(type(nombre))

#funcion para detectar el tipado
comprobar = isinstance(nombre, str)
if comprobar: #si no pongo nada el if interpreta que la variable debe ser true
    print("Es un string")
else:
    print("No es una cadena de texto")

if not isinstance(nombre, float):
    print("la variable no es un numero con decimales")

# limpiar espacios de un string
frase = "    mi contenido     "

print(frase.strip()) #strip limpia los espacios agregados

#eliminar variables
year = 2022
del year
#print(year) #year no esta definido

#comprobar variables vacias
texto = "  ff  "

if len(texto) == 0:
    print("la variable esta vacia")
else: 
    print(f"la variable tiene contenido ", len(texto))

#Encontrar caracteres en una variable
frase = "la vida es bella"
print(frase.find("bella")) #A partir del caracter 11

#Reemplazar palabras en un string
nueva_frase = frase.replace("vida", "moto")
print(nueva_frase)

#mayusculas y minusculas
print(nombre.lower()) #todo minusculas
print(nombre.upper()) #todo mayusculas

