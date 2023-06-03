from tkinter import *
from PIL import Image, ImageTk



ventana = Tk()
ventana.geometry("750x500")


Label(ventana, text="hola soy nico!!").pack(anchor=W)
#imagenes:
imagen = Image.open('./22tkinter/imagenes/lobo.jpg')
render = ImageTk.PhotoImage(imagen)
Label(ventana, image=render).pack(anchor=CENTER)


ventana.mainloop()
