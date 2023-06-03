"""
Calculadora: 
-dos campos de texto
_4 botones para las operaciones
_Mostrar el resultado en una alerta
"""


from tkinter import *
from tkinter import messagebox  

ventana = Tk()
ventana.title("Calculadora con python y tkinter")
ventana.config(bd=25)
ventana.geometry("400x400")

def sumar():
    resultado.set(float(numero1.get()) + float(numero2.get()))
    mostrarResultado()

def restar():
    resultado.set(float(numero1.get()) - float(numero2.get()))
    mostrarResultado()

def dividir():
    resultado.set(float(numero1.get()) / float(numero2.get()))
    mostrarResultado()

def multiplicar():
    resultado.set(float(numero1.get()) * float(numero2.get()))
    mostrarResultado()


def mostrarResultado():
    messagebox.showinfo("Resultado", f"El resultado de la operacion es: {resultado.get}")
    numero1.set("")
    numero2.set("")

numero1 = StringVar()
numero2 = StringVar()
resultado = StringVar()

marco = Frame(ventana, width=300, height=300)
marco.config(
    padx=15,
    pady=30,
    bd=15,
    relief=SOLID,

)
marco.pack(side=TOP, anchor=CENTER)
marco.pack_propagate(False)


Label(marco, text="Primer numero: ").pack()
Entry(marco, textvariable=numero1, justify="center").pack()

Label(marco, text="Segundo numero: ").pack()
Entry(marco, textvariable=numero2, justify="center").pack()

Label(marco, text="").pack()


Button(marco, text="Sumar", command=sumar).pack(side="left", fill=X, expand=YES)
Button(marco, text="Restar", command=restar).pack(side="left", fill=X, expand=YES)
Button(marco, text="Dividir", command=dividir).pack(side="left", fill=X, expand=YES)
Button(marco, text="Multiplicar", command=multiplicar).pack(side="left", fill=X, expand=YES)


def Salir(nombre):
    resultado = messagebox.askquestion("Salir", "Desea salir?")
    if resultado != "no":
        messagebox.showinfo("Chao!!", f"Adios {nombre}")
        ventana.destroy()

Button(marco, text="Salir", bg="red", fg="white", command=lambda: Salir("Nicolas Alfonsin")).pack(side=BOTTOM, fill=X, expand=YES)




ventana.mainloop()