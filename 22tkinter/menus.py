from tkinter import *

ventana = Tk()

ventana.geometry("600x600")


mi_menu = Menu(ventana)
ventana.config(menu=mi_menu)

archivo = Menu(mi_menu)
archivo.add_command(label="New file")
archivo.add_command(label="New window")
archivo.add_separator()
archivo.add_command(label="Open file")
archivo.add_command(label="Open folder")
archivo.add_separator()
archivo.add_command(label="Save")
archivo.add_command(label="Save as")
archivo.add_separator()
archivo.add_command(label="Close editor", command=ventana.quit)

mi_menu.add_cascade(label="Archivo", menu=archivo)
mi_menu.add_command(label="Editar")
mi_menu.add_command(label="Seleccion")


ventana.mainloop()