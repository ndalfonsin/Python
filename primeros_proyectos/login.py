try:
    usuario = input("¿Cual es tu user?: ")

    if len(usuario) > 1:
        print(f"El usuario es : {usuario}")
except:
    print("No ha ingresado un usuario")
else:
    
    password = int(input(f"{usuario} ingrese su codigo de 4 dijitos: "))

    if password == 1515:
        print("Acceso concedido")
    else:
        print("EL CAMPO INGRESADO NO ES VALIDO")
    
finally:
    ("fin de la interaccion")

        