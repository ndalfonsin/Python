from tkinter import *
from tkinter import ttk
"""
Crear un programa que tenga:
(hecho)-ventana, fija y no redimencionable.
(hecho)-menu.(inicio, añadir, info, salir)
(hecho)-diferentes pantallas.
(hecho)-formulario de guardar productos.
(hecho)-guardar datos temporalmente, en una variable.
-mostrar datos listados en la pantalla home.
(hecho)-opcion de salir
"""

#VENTANA:
ventana = Tk()
#ventana.geometry("500x500")
ventana.minsize(500, 500)
ventana.title("Proyecto TK, Master en python")
ventana.resizable(0, 0)



def home():
    #Montar pantalla:

    home_label.config(
        fg="White",
        bg="Black",
        font=("Arial", 20),
        padx=220,
        pady=20
    )
    home_label.grid(row=0, column=0)

    #products_box.grid(row=2, column=0)
    
    #listar productos
    for product in products:
        if len(product) == 2:
            product.append("added")
            products_box.insert('', 0, text=product[0], values=(product[1]))

    #ocultar pantallas:
    add_label.grid_remove()
    info_label.grid_remove()
    data_label.grid_remove()
 
    add_name_entry.grid_remove()
    add_name_label.grid_remove()
    add_price_entry.grid_remove()
    add_price_label.grid_remove()
    boton.grid_remove()
    
def add():
    #Encabezado:

    add_label.config(
        fg="White",
        bg="Black",
        font=("Arial", 20),
        padx=160,
        pady=20
    )
    add_label.grid(row=0, column=0)
    
    #campos de formulario
    add_name_label.grid(row=1, column=0, padx=5, pady=5)
    add_name_entry.grid(row=2,column=0, padx=5, pady=5)

    add_price_label.grid(row=3, column=0, padx=5, pady=5)
    add_price_entry.grid(row=4, column=0)

    add_separator.grid(row=5, column=0)
    boton.grid(row=6, column=0, sticky=S)
    boton.config(
        padx=15,
        pady=5,
        bg="Black",
        fg="White"
    )
    #ocultar pantallas:
    home_label.grid_remove()
    info_label.grid_remove()
    data_label.grid_remove()
    products_box.grid_remove()

def info():
    info_label.config(
        fg="White",
        bg="Black",
        font=("Arial", 20),
        padx=190,
        pady=20
    )
    info_label.grid(row=0, column=0)

    
    data_label.grid(row=1, column=0)
    
    #ocultar pantallas:
    add_label.grid_remove()
    home_label.grid_remove()

    add_name_entry.grid_remove()
    add_name_label.grid_remove()
    add_price_entry.grid_remove()
    add_price_label.grid_remove()
    boton.grid_remove()
    products_box.grid_remove()

def add_product():
    products.append([
        name_data.get(),
        price_data.get()

    ])
    name_data.set("")
    price_data.set("")

    products_box.grid_remove()
    
    home()

#Variables:
products = []
name_data = StringVar()
price_data = StringVar()

#diferentes pantallas en la ventana. 

#llevar las definiciones por fuera de la funcion para que no se vean detras
home_label = Label(ventana, text="Inicio")
products_box = Frame(ventana, width=250)



products_box = ttk.Treeview(height=12, columns=2)
products_box.grid(row=1, column=0, columnspan=2)
products_box.heading("#0", text='Producto:', anchor=W)
products_box.heading("#1", text='Precio:', anchor=W)
#listar productos
"""
for product in products:
    if len(product) == 2:
        Label(products_box, text=product[0]).grid()
        Label(products_box, text=product[1]).grid()
        Label(products_box, text="__________________________").grid()
"""




add_label = Label(ventana, text="Añadir producto")
info_label = Label(ventana, text="Informacion")
data_label = Label(ventana, text="Creado por Nicolas Alfonsin")


#campos del formulario
add_name_label = Label(ventana, text="Nombre del producto")
add_name_entry = Entry(ventana, textvariable=name_data)

add_price_label = Label(ventana, text="Precio del producto")
add_price_entry = Entry(ventana, textvariable=price_data)

add_separator = Label(ventana)

add_frame = Frame(ventana)

#boton de guardado
boton = Button(ventana, text="Guardar", command=add_product)




#cargar pantalla de inicio
home()

#creacion de menu superior
menu_superior = Menu(ventana)
menu_superior.add_command(label="Inicio", command=home)
menu_superior.add_command(label="Añadir", command=add)
menu_superior.add_command(label="Info...", command=info)
menu_superior.add_command(label="Salir", command=ventana.quit)


#cargar menu
ventana.config(menu=menu_superior)

#diferentes pantallas en la ventana. 

#listar productos


ventana.mainloop()

