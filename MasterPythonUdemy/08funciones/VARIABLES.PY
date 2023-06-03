"""
UNA VARIABLE LOCAL SOLO ESTA DISPLONIBLE DE LA FUNCION, EN CAMBIO LA GLOBAL
ESTA DISPONIBLE PARA CUALQUIER FUNCION DESDE SER ASIGNADA
"""
moraleja = "EL QUE NO COJE SE DEJA SE DEJA"

print(moraleja)

def holamundo():
    moraleja = "holamundo!"
    print(moraleja)

holamundo()
 #para ejecutar una variable de una funcion de forma global hay que asignarla como: global variable
 