
"""
VA a contener datos pero el indice va a ser alfanumerico
ES PARECIDO A UN ARRAY
"""
persona = {
    "Nombre": "Nicolas",
    "Apellidos": "Alfonsin",
    "Instagram": "AALFONZZZ"

}

print(persona["Apellidos"])

#DICCIONARIO MULTIDIMENCIONAL

#lista con diccionarios
contactos = [
    {
        "nombre": "Nicolas",
        "Email": "Nicolasdalfonsin@gmail.com"

    },
    {
        "nombre": "Juan",
        "Email": "juancruzzerillo@gmail.com"
    
    },

]

contactos[0]["nombre"] = "Nicolas Diego"
print(contactos[1]['nombre'])

print(contactos[0]['nombre'])

print(contactos[0]['Email'])

print("\ncontactos: ")
for contacto in contactos:
    print(f"Nombre del contacto: {contacto['nombre']}")
    print(f"El Email es: {contacto['Email']}")
    print("\n")
    