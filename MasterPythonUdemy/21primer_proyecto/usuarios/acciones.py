import usuarios.usuario as modelo

import notas.accion_nota

class Acciones:

    def registro(self):
        print("\n OK!! VAMOS A REGISTRARTE EN EL SISTEMA!!")
        
        nombre = input("¿Cual es tu nombre??..:")
        apellidos = input("¿Cual es tu apellido?..:")
        email = input("¿Cual es tu email?..:")
        password = input("¿Cual es tu contraseña?..:") 


        usuario = modelo.usuario(nombre, apellidos, email, password)
        registro = usuario.registrar()

        if registro[0] >=1:
            print(f"Perfecto {registro[1].nombre} te has registrado con el email: {registro[1].email}")
        else:
            print("Eror 404")


    def login(self):
        print("OK!! Identificate en el sistema... ")
        
        try:
            email = input("¿Cual es tu email?..:")
            password = input("¿Cual es tu contraseña?..:")

            usuario = modelo.usuario('', '', email, password)
            login = usuario.identificar()

            if email == login[3]:
                print(f"Bienvenido {login[1]}, te has  registrado en el sistema el {login[5]}")
                self.proximasacciones(login)

        
        except Exception as e:
            print(type(e))
            print(type(e).__name__)
            print("Login incorrecto intentalo mas tarde!!!")
            



    def proximasacciones(self, usuario):
        print("""
        -Crear nota (crear)
        -Mostrar notas (mostrar)
        -Eliminar notas (eliminar)
        -Salir(salir)
        """)

        accion = input("¿Que quieres hacer?:")
        hazEl = notas.accion_nota.Acciones()

        if accion == "crear":
            hazEl.crear(usuario)
            self.proximasacciones(usuario)
        elif accion == "mostrar":
            hazEl.mostrar(usuario)
            self.proximasacciones(usuario)
        elif accion == "eliminar":
            hazEl.borrar(usuario)
            self.proximasacciones(usuario)
        elif accion == "salir":
            print(f"HASTA PRONTO {usuario[1]}!!!!!")
            exit()
