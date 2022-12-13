from tkinter import *

ventana = Tk()
ventana.geometry("700x400")
ventana.title("formularios")

#texto encabezado
encabezado = Label(ventana, text="Formularios con tkinter")
encabezado.config(
                fg="white",
                bg="darkgray",
                font=("Arial", 18),
                padx=10,
                pady=10
)
encabezado.grid(row=0, column=0, columnspan=12, sticky=W)

#label para el campo:
label = Label(ventana, text="Nombres")
label.grid(row=1, column=0, sticky=W, padx=5, pady=5)


#campos en formularios, campo de texto (NOMBRE):
campo_texto = Entry(ventana)
campo_texto.grid(row=1, column=1, sticky=W, padx=5, pady=5)
campo_texto.config(justify="right", state="normal")



#label para el campo:
label = Label(ventana, text="Apellidos")
label.grid(row=2, column=0, sticky=W, padx=5, pady=5)

#campos en formularios, campo de texto (apellidos):
campo_texto = Entry(ventana)
campo_texto.grid(row=2, column=1, sticky=W, padx=5, pady=5)
campo_texto.config(justify="right", state="normal")



#label para el campo:
label = Label(ventana, text="Email")
label.grid(row=3, column=0, sticky=W, padx=5, pady=5)

#campos en formularios, campo de texto (EMAIL):
campo_texto = Entry(ventana)
campo_texto.grid(row=3, column=1, sticky=W, padx=5, pady=5)
campo_texto.config(justify="right", state="normal")



#label para el campo:
label = Label(ventana, text="Nacionalidad")
label.grid(row=4, column=0, sticky=W, padx=5, pady=5)

#campos en formularios, campo de texto (Nacionalidad):
campo_texto = Entry(ventana)
campo_texto.grid(row=4, column=1, sticky=W, padx=5, pady=5)
campo_texto.config(justify="right", state="normal")

#label separador
Label(ventana).grid(row=5, column=1)

#boton
boton = Button(ventana, text="Enviar")
boton.grid(row=6, column=1, sticky=W, padx=5, pady=5)
boton.config(bg="green", fg="white")




ventana.mainloop()
