from tkinter import *
import os.path


class programa:

    def __init__(self):
        self.title = "Master en Python"
        self.icon = './imagenes/logotipo.ico'
        self.iconalt = './22tkinter/imagenes/logotipo.ico'
        self.size = "770x470"
        

    def cargar(self):
       
        ventana = Tk()
        self.ventana = ventana

        #comprobar si existe un archivo
        ruta_icono = os.path.abspath(self.icon)
        #mostrar texto en el programa
        texto = Label(ventana, text=ruta_icono)
        texto.pack()

        if not os.path.isfile(ruta_icono):
            ruta_icono = os.path.abspath(self.iconalt)
        #poner un logotipo a la ventana
        ventana.iconbitmap(ruta_icono)

        #cambio en el tamaño de la ventana
        ventana.geometry(self.size)

        #bloquear el tamaño de la ventana
        ventana.resizable(0, 0)

        #poner titulo: 
        ventana.title(self.title)

        #arrancar y mostrar la ventana hasta que se cierre
        #ventana.mainloop()
    
    def addtexto(self, dato):
        texto = Label(self.ventana, text=dato)
        texto.pack()

    def mostrar(self):
        self.ventana.mainloop()
#instanciar mi programa
Programa = programa()
Programa.cargar()
Programa.addtexto("Hola")
Programa.addtexto("Soy un texto")
Programa.addtexto("Bienvenido al master en python")
Programa.addtexto("soy Nico")
Programa.addtexto("Esto es una prueba")

Programa.mostrar()


