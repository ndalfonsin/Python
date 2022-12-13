nombre = "Nicolas Alfonsin"

#funciones generales
print(type(nombre))

#detectar el tipado
comprobar = isinstance(nombre, str)
if comprobar:
    print("esa variable es un str")
else: 
    print("no es una cadena")

if not isinstance(nombre, float):
    print("la variable no es un numero con decimales")

#limpiar espacios
frase = "   gjhehe    "
print(frase)
print(frase.strip()) 

#eliminar variables
year = 2021
print(year)
del year
#print(year)

#comprobar variables vacias
texto = "  ff  "

if len(texto) <= 0:
    print("la variable esta vacia")
else: 
    print("la variable tiene contenido: " ,len(texto))

#encontrar caracteres
frase = "La vida es bella"
print(frase.find("vida"))

#reemplaza palabras en un str
nueva_frase = frase.replace("vida", "moto")
print(nueva_frase)

#mayusculas y minusculas
print(nombre)
print(nombre.lower())
print(nombre.upper())
