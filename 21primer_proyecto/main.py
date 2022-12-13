"""
PROYECTO PYTHON_MYSQL
-abrir asistente
-login o registro
-si elegimos registro, creara un usuario en la bbdd
-si elegimos login, identifica al usuario y nos preguntara
-crear nota, mostrar notas, borrarlas.

"""

from usuarios import acciones



print("""
    BIENVENIDO!!!
Acciones disponibles:
    -registro
    -login
""")

hazEL = acciones.Acciones()


accion = input("Dime..¿Que quieres hacer?:")

if accion == "registro":
    hazEL.registro()


elif accion == "login":
    hazEL.login()

    

