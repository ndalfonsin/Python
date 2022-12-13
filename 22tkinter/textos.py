from tkinter import *

ventana = Tk()
ventana.geometry("650x650")

#como cargar texto:
texto = Label(ventana, text="bienvenido a mi programa")
texto.config(
            fg="white",
            bg="black",
            padx=50,
            pady=20,
            font=("Arial", 21))

texto.pack()

def pruebas(nombre, apellidos, pais):
    return f"Hola {nombre} {apellidos} veo que eres de {pais}"


texto = Label(ventana, text=pruebas("Nico", "Alfonsin", "Argentina"))
texto.config(
            fg="white",
            bg="red",
            padx=50,
            pady=20,
            font=("Arial", 21),
            cursor="spider")


            
           
           
#para mover el texto en el pack ingresar "anchor=W"

texto.pack(anchor=W)


#para darle tamaño al elemento, se colocan dentro de config del texto

height=10, #altura
width=400 #anchura

#poner un cursor
cursor="spider"



ventana.mainloop()