#capturar excepciones y manejar errores en codigo suceptibles a fallos/errores

#nombre = input("¿Cual es tu nombre?: ")
#if len(nombre) > 1:
    #nombre_usuario = "El nombre es: " + nombre

#print(nombre_usuario)

"""
Cuando creemos que nuestro codigo es suceptible a un fallo, como en este caso que si al ingresar el nombre
el usuario no rellena el campo y manda el campo vacio, esto genera que la variable "nombre_usuario" no este
definida, por ende el print de nombre usuario no se ejecutaria y mandaria un error, tambien dado a que el 
nombre que ingrese el ususario tiene que ser mayor que uno!!

Para esto la solucion mas factible es ingresar el condigo entre uin try y un except. Esto seria de la 
siguiente forma:


try:
    nombre = input("¿Cual es tu nombre?: ")
    
    if len(nombre) > 1:
        nombre_usuario = "El nombre es: " + nombre

    print(nombre_usuario)
except:
    print("Ha ocurrido un error, debes rellenar el caracter!")
else:
    print("El usuario es correcto")
finally:
    print("fin de la interaccion!!")



Utilizar el manejo de errores es muy importante al momento de escribir cualquier codigo, ya que 
si un intruso desease irrumpir o encontrar fallos en el codigo, generar errores de este tipo
que revelen informacion podria ser perjudicial, por eso es mejor que la consola te devuelva un 
manejo de errores en vez de informacion de cual es el error.
-Poner un else nos permite que si el codigo del try se ejecuta bien, poder comandarle una interaccion
u orden.
-poner un finally al final SIEMPRE SE VA A MOSTRAR, pero nos permite saber cuando el codigo ha finalizado
y si este lo ha hecho hasta se podiria sugerir ingresar a otro comando de codigos!

#MANEJO DE MULTIPLES EXCEPCIONES
try:
        
    numero = int(input("Numero para elevarlo al cuadrado: "))
    print("El cuadrado es: " +str(numero*numero))
except TypeError:
    print("DEBES CONVERTIR TUS CADENAS A ENTEROS")
#except ValueError:
#   print("introduce un numero correcto")
except Exception as e:
    print("ha ocurrido un error: ", type(e).__name__)

"""
#EXCEPCIONES PERSONALIZADAS O LANZAR EXCEPCION


#El comando RAISE sirve para llamar a un tipo de error sin recurrir al try y except
try:
    nombre = input("introduce el nombre: ")
    edad = int(input("introduce la edad: "))



    if edad < 5 or edad > 110:
        raise ValueError("LA EDAD INTRODUCIDA NO ES REAL")
    elif len(nombre) <= 1:
        raise ValueError("EL NOMBRE NO ESTA COMPLETO")
    else:
        print("bienvenido")
except ValueError:
    print("introduce los datos correctamente!")
except Exception as e:
    print("EXISTE UN ERROR: ", e)

