#Programacion orientada a objetos.

#la clase es un molde

#definir una clase:(molde para crear mas objetos de ese tipo(coche) con caracteristicas similares)
print("######### COCHE 1 ##########")

class Coche:
    
    #ATRIBUTOS O PROPIEDADES
    #caracteristicas del coche
    color = "rojo"
    marca = "ferrari"
    modelo = "aventador"
    velocidad = 300
    caballaje = 500
    plazas = 2

    #metodos (acciones que hace el objeto (coche))
    def setColor(self, color):
        self.color = color
    
    def getColor (self):
        return self.color
    
    def setModelo(self, modelo):
        self.modelo = modelo
    
    def getModelo(self):
        return self.modelo

    def acelerar(self):
        self.velocidad += 1
    
    def frenar(self):
        self.velocidad -= 1
    
    def getVelocidad(self):
        return self.velocidad

#Fin definicion clase. 

#crear un objeto o instanciar la clase. 
coche = Coche()

coche.setColor("NEGRO como el del 10")
coche.setModelo("Murcielago")


print(coche)
print(coche.marca, coche.getModelo(), coche.getColor())

print("Velocidad actual: ", coche.getVelocidad())


coche.acelerar()
coche.acelerar()
coche.acelerar()

print("velocidad nueva!!: ", coche.getVelocidad())


#crear mas objetos
print("########## COCHE 2 ########")
coche2 = Coche()

coche2.setColor("VERDE")
coche2.setModelo("Gallardo")

print(coche2.getColor())
print(coche2.marca, coche2.getModelo(), coche2.getColor())

print(type(coche2))

