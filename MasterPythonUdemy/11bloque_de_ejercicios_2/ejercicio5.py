"""
EJERCICIO 5. representar una tabla con informacion dentro de una lista de diccionario.
crear una lista con el contenido de esta tabla: 
videojuegos: accion, aventura y deportes
accion: gtav cod pub 
aventura: crash, prince op
deportes: fifa 21, pes 21, moto gp 21
guardarlo dentro de un listado de diccionario y mostrar la informacion ordenada
primero accion, aventura y ultimo deporte.
"""

tabla = [
    {
        "Categoria" : "Accion",
        "juegos" : ["COD", "GTAV", "PUB"]
    },
    {
        "Categoria" : "Aventura",
        "juegos" : ["Crash", "Prince of Persia"]
    },
    {
        "Categoria" : "Deportes", 
        "juegos" : ["FIFA 21, PES 21, MOTO GP 21"]

    }

]


for games in tabla:
    print(f"El genero es: {games['Categoria']}")
    print(f"los juegos son: {games['juegos']}")
    print("\n")
    
    



