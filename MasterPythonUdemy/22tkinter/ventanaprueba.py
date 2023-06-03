from tkinter import *
import os.path
 
#Es un modulo para crear interfaces graficas de usuario

#crear la ventana raiz:
ventana = Tk()

#comprobar si existe un archivo
ruta_icono = os.path.abspath('./imagenes/logotipo.ico')
#mostrar texto en el programa
texto = Label(ventana, text=ruta_icono)
texto.pack()

if not os.path.isfile(ruta_icono):
    ruta_icono = os.path.abspath('./22tkinter/imagenes/logotipo.ico')
#poner un logotipo a la ventana
ventana.iconbitmap(ruta_icono)

#cambio en el tamaño de la ventana
ventana.geometry("750x450")

#bloquear el tamaño de la ventana
ventana.resizable(0,0)

#poner titulo: 
ventana.title("interfaz grafica con python y tkinter")

#arrancar y mostrar la ventana hasta que se cierre
ventana.mainloop()

