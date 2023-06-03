import notas.nota as modelo


class Acciones:
    def crear(self, usuario):
        print(f"\nOK {usuario[1]} !! Vamos a crear una nota...")
        titulo = input("\nIntroduce el titulo de tu nota: ")
        descripcion = input("\nIntroduce el contenido de tu nota: ")


        nota = modelo.nota(usuario[0], titulo, descripcion)
        guardar = nota.guardar()

        if guardar[0] >= 1:
            print(f"\n Perfecto has guardado la nota: {nota.titulo}")
        else:
            print(f"\nNo se ha guardado la nota, lo siento {usuario[1]}")


    def mostrar(self, usuario):
        print(f"\n{usuario[1]}!! aqui tienes tus notas: ")

        nota = modelo.nota(usuario[0])
        notas = nota.listar()

        for nota in notas:
            print("******************")
            print(nota[2])
            print(nota[3])
            print("\n******************")

    def borrar(self, usuario):
        print(f"\n OK {usuario[1]}!!! Vamos a borrar notas")

        titulo = input("introduce el titulo de la nota a borrar: ")

        nota = modelo.nota(usuario[0], titulo)
        eliminar = nota.eliminar()

        if eliminar[0] >= 1:
            print(f"Hemos borrado la nota: {nota.titulo}")
        else:
            print("Ha ocurrido un error")
