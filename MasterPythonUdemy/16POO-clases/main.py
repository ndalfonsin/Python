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

    #metodos (acciones que hace el objeto (coche))

    def acelerar(self):
        self.velocidad += 1
    
    def frenar(self):
        self.velocidad -= 1
    
    def getVelocidad(self):
        return self.velocidad

#Fin definicion clase. 

#crear un objeto o instanciar la clase. 
coche = Coche()


print(coche)
print(coche.marca, coche.color)
print("Velocidad actual: ", coche.velocidad)

coche.acelerar()
coche.acelerar() 
coche.acelerar()

print("velocidad nueva!!: ", coche.velocidad)


  


