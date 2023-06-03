"""
listas (arrays)
Son colecciones de datos/valores, bajo un unico nombre.
Para acceder a esos valores podemos usar um indice numerico.
 

pelicula = "BATMAN"
#COMO DEFINIR UNA LISTA
#asignandolo con ]
peliculas = ["BATMAN", "Spiderman", "Harry Potter"]
#print(peliculas)

#con el list y la tuppla (())
cantantes = list(("gnfr", "megadeth", "metallica"))
#print(cantantes)

years = list(range(2000,2021))
#print(years)

#En una lista se pueden poner los tipos de valores o datos que se quiera sea boolean, int, lo que sea!

#INDICES
print(peliculas[1])
print(peliculas[-2])
#sublistas
print(cantantes[1:3]) #para sacar mas de un elemento

#RECORDAR QUE LA LISTA ARRANCA EN 0 Y SON VALIDOS ELEMENTOS NEGATIVOS
#para reasignar se hace
peliculas[1] = "NO WAY HOME"
print(peliculas[1])

#como añadir elementos a una lista
cantantes.append("ice cube")
print(cantantes[3])

#recorrer una lista con el bucle for
print("###### lista de peliculas ########")
nueva_pelicula = ""
while nueva_pelicula != "stop":
    nueva_pelicula = input("introduce una nueva pelicula: ")
    
    if nueva_pelicula != "stop":
        peliculas.append(nueva_pelicula)

for pelicula in peliculas:
    print(f"{peliculas.index(pelicula)+1}. {pelicula}")
""" 
#listas multidimencionales
"""
TIENE VARIAS DIMENCIONESS
"""
print("\n #### LISTA DE CONTACTOS ###")
contactos = [
    ["Juan", "Juan#####"
    ],
    ["rocio", "shddfhds"
    ]
]

for contacto in contactos:
    for elemento in contacto:
        if contacto.index(elemento) == 0:
            print("User: " + elemento)
        else:
            print("Password: " + elemento)
        print("\n")




