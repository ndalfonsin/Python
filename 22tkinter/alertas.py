from tkinter import *
from tkinter import messagebox as MessageBox


ventana = Tk()
ventana.config(bd=70)


def sacarAlerta():
    MessageBox.showerror("Alerta", "HOLIWHI")
Button(ventana, text="mostrar alertas", command=sacarAlerta).pack()

def Salir(nombre):
    resultado = MessageBox.askquestion("Salir", "Desea salir?")
    if resultado != "no":
        MessageBox.showinfo("Chao!!", f"Adios {nombre}")
        ventana.destroy()

Button(ventana, text="Salir", command=lambda: Salir("Nicolas Alfonsin")).pack()


ventana.mainloop()
