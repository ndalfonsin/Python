from tkinter import * 

ventana = Tk()
ventana.title("Marcos|Master en python")
ventana.geometry("700x400")

#como insertar marcos:
marco = Frame(ventana, width=250, height=250)
marco.config(bg="red",
            bd=5,
            relief="solid")
marco.pack(side=BOTTOM, anchor=CENTER)
marco.pack_propagate(False)

#se posiciona con bottom, rigth, left
#cargar texto
texto = Label(marco, text="Primer Marco")
texto.config(
    bg="red",
    fg="white",
    font=("Arial", 20),
    height=10,
    width=10,
    anchor=CENTER

)
texto.pack()

ventana.mainloop()

#se pueden poner cuantos querramos
