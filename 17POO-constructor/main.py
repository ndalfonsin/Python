"""
from coche import Coche


auto = Coche("Amarillo", "Renault", "Clio", 150, 200, 4)
auto2 = Coche("verde", "chevrolet", "chevy", 300, 200, 4)
auto3 = Coche("azul", "Renault", "504", 150, 200, 4)

print(auto.getInfo())
print(auto2.getInfo())
print(auto3.getInfo())

#detectar tipado:
if type(auto3) == Coche:
    print("Es un objeto correcto")
else:
    print("algo ha ido mal")


#VISIBILIDAD de los atributos y metodos. publicos o privados.

print(auto.Soy_publico)
print(auto.getPrivado())


#para acceder hay que crear un metodo def getprivado


"""


