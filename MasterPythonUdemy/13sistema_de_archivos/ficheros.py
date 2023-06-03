from io import open
import pathlib
import shutil
#abrir archivo
#archivo = open (pathlib.Path().absolute()"fichero_texto.txt", "a+")
ruta = str(pathlib.Path().absolute()) + "/fichero_texto.txt"
print(ruta)
archivo = open(ruta, "a+")

#podemos escribir dentro del archivo
archivo.write("\nlas papas fritas son ricas\n")

#cerrar archivo
archivo.close()

#archivo = open (pathlib.Path().absolute()"fichero_texto.txt", "a+")
ruta = str(pathlib.Path().absolute()) + "/fichero_texto.txt"
print(ruta)
archivo_lectura = open(ruta, "r")

#leer contenido:
#contenido = archivo_lectura.read()
#print(contenido)

#for elemento in contenido:
#    print(elemento)

#leer contenido y guardarlo en una lista
lista = archivo_lectura.readlines()
archivo_lectura.close()

for elemento in lista:
    print("- " + elemento)
    
#copiar un archivo:
"""
import shutil
ruta_original = str(pathlib.Path().absolute()) + "/fichero_texto.txt"
ruta_nueva= str(pathlib.Path().absolute()) + "/fichero_copiado.txt"
shutil.copyfile(ruta_original, ruta_nueva)

#mover
ruta_original = str(pathlib.Path().absolute()) + "/fichero_copiado.txt"
ruta_nueva = str(pathlib.Path().absolute()) + "/fichero_copiado_NEW.txt"

shutil.move(ruta_original, ruta_nueva)

#ELIMINAR ARCHIVOS
import os
ruta_nueva = str(pathlib.Path().absolute()) + "/fichero_copiado_NEW.txt"
os.remove(ruta_nueva)
"""
#comprobar si existe
import os.path
#print(os.path.abspath("/"))

ruta_comprobar = os.path.abspath("./") + "/fichero_texto.txt"
if os.path.isfile(ruta_comprobar):
    print("EL FICHERO EXISTE")
else:
    print("NO EXISTE")
  