#Programacion orientada a objetos.

#la clase es un molde

#definir una clase:(molde para crear mas objetos de ese tipo(coche) con caracteristicas similares)

class Coche:
    
    #ATRIBUTOS O PROPIEDADES
    #caracteristicas del coche
    color = "rojo"
    marca = "ferrari"
    modelo = "aventador"
    velocidad = 300
    caballaje = 500
    plazas = 2
    
    Soy_publico = "SOY UN ATRIBUTO PUBLICO"
    __Soy_privado = "SOY PRIVADO"


    #DEFINIR UN CONSTRUCTOR
    def __init__(self, color, marca, modelo, velocidad, caballaje, plazas):
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad
        self.caballaje = caballaje
        self.plazas = plazas
    #metodos (acciones que hace el objeto (coche))

    def getPrivado(self):
        return self.__Soy_privado

    def setColor(self, color):
        self.color = color
    
    def getColor (self):
        return self.color
    
    def setModelo(self, modelo):
        self.modelo = modelo
    
    def getModelo(self):
        return self.modelo

    def setMarca(self, marca):
        self.marca = marca

    def getMarca(self):
        return self.marca

    def acelerar(self):
        self.velocidad += 1
    
    def frenar(self):
        self.velocidad -= 1
    
    def getVelocidad(self):
        return self.velocidad
    
    def getInfo(self):

        info = "---- Informacion del coche ----"
        info += "\n Color: " + self.getColor()
        info += "\n Marca: " + self.getMarca()
        info += "\n Modelo: " + self.getModelo()
        info += "\n Velocidad: " + str(self.getVelocidad())


        return info

#Fin definicion clase. 
#constructor: es un metodo especial dentro de una clase y se utiliza para darle un valor a las propiedades
#del metodo. 