from tkinter import *
from tkinter import messagebox

ventana = Tk()
ventana.geometry("800x500")

encabezado = Label(ventana, text="Formularios avanzados")
encabezado.config(
    padx=30,
    pady=15,
    fg="white",
    bg="red",
    font=("Arial", 20)
)

encabezado.grid(row=0, column=0, columnspan=122, sticky=W)

def mostrarProfesion():
    texto = ""

    if web.get():
        texto += "Desarrollo web"
    
    if movil.get():
        if web.get():
            texto +=  " y desarrollo movil"
        else:
            texto += "Desarrollo movil"

    mostrar.config(
        text=texto
        
    )

#botones check
web = IntVar()
movil = IntVar()


Label(ventana, text="¿A que te dedicas?").grid(row=1, column=0)

Checkbutton(
    ventana, 
    text="desarrollo web",
    variable=web,
    onvalue=1,
    offvalue=0,
    command=mostrarProfesion
).grid(row=2, column=0)

Checkbutton(
    ventana, 
    text="desarrollo movil",
    variable=movil,
    onvalue=1,
    offvalue=0,
    command=mostrarProfesion
).grid(row=3, column=0)

mostrar = Label(ventana)
mostrar.grid(row=4, column=0)

#radio buttons
def marcar():
    marcado.config(text=opcion.get())

opcion = StringVar()
opcion.set("opcion 1")

Label(ventana, text="¿Cual es tu genero?").grid(row=5)

Radiobutton(
    ventana, 
    text="Masculino",
    value="Masculino",
    variable=opcion,
    command=marcar
).grid(row=6)

Radiobutton(
    ventana,
    text="Femenino",
    value="Femenino",
    variable=opcion,
    command=marcar
).grid(row=7)

Radiobutton(
    ventana,
    text="Otro",
    value="Otro",
    variable=opcion,
    command=marcar
).grid(row=8)
marcado = Label(ventana)
marcado.grid(row=9)

def Salir(nombre):
    resultado = messagebox.askquestion("Salir", "Desea salir?")
    if resultado != "no":
        messagebox.showinfo("Chao!!", f"Adios {nombre}")
        ventana.destroy()

Button(ventana, text="Salir", bg="red", fg="white", command=lambda: Salir("Nicolas Alfonsin")).grid(row=11)

#option menu
def seleccionar():
    seleccionado.config(text=opcion.get())

opcion = StringVar()
select = OptionMenu(ventana, opcion, "opcion 1", "opcion 2", "opcion 3")
select.grid(row=5, column=1)

Button(ventana, text="Ver", command=seleccionar).grid(row=6, column=1)

seleccionado = Label(ventana)
seleccionado.grid(row=7, column=1)
ventana.mainloop()
