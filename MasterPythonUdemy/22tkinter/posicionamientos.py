from tkinter import *

ventana = Tk()
#ventana.geometry("650x650")

#como cargar texto y posicionarlo con el "SIDE":
texto = Label(ventana, text="bienvenido a mi programa")
texto.config(
            fg="white",
            bg="black",
            padx=50,
            pady=20,
            font=("Arial", 21))

texto.pack(side=TOP)




texto = Label(ventana, text="Soy Nicolas Alfonsin")
texto.config(
            fg="white",
            bg="red",
            padx=50,
            pady=20,
            font=("Arial", 21),
            cursor="spider")
texto.pack(side=TOP, fill=X, expand=YES)

texto = Label(ventana, text="Basico")
texto.config(
            fg="white",
            bg="green",
            padx=50,
            pady=20,
            font=("Arial", 21),
            cursor="spider")

texto.pack(side=LEFT, fill=X, expand=YES)

texto = Label(ventana, text="Basico")
texto.config(
            fg="black",
            bg="yellow",
            padx=50,
            pady=20,
            font=("Arial", 21),
            cursor="spider")

texto.pack(side=LEFT, fill=X, expand=YES)

ventana.mainloop()