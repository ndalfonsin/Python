#La herencia es la posibilidad de compartir artibutos y metodos entre clases

class persona:
    nombre = "Juan"
    apellidos = "Diaz"
    edad = 22
    altura = 1,65

    def getNombre(self):
        return self.nombre

    def getApellidos(self):
        return self.apellidos
    
    def getEdad(self):
        return self.edad
    
    def getAltura(self):
        return self.altura
    
    def setNombre(self, nombre):
        self.nombre = nombre
    
    def setApellidos(self, apellidos):
        self.apellidos = apellidos
    
    def setEdad(self, edad):
        self.edad = edad
    
    def setAltura(self, altura):
        self.altura = altura

    def hablar(self):
        return "estoy hablando"

    def caminar(self):
        return "Estoy caminando"

    def dormir(self):
        return "Estoy durmiendo"

class informatico(persona):
    """
    lenguajes
    experiencia

    """
    def __init__(self):
        self.lenguajes = "html, CSS, JavaScript, PHP"
        self.experiencia = 5

    def getLenguajes(self):
        return self.lenguajes
    
    def aprender(self, lenguajes):
        self.lenguajes = lenguajes
        return self.lenguajes

    def programar(self):
        return "ESTOY PROGRAMANDO"

    def repararPC(self):
        return "HE REPARADO TU ORDENADOR"
    

class mecanico(persona):
    def __init__(self):
        self.conocimientos = "MAQUINAS DE VAPOR, HELADERAS, MOTORES DE HASTA 5 TIEMPOS"
        self.experiencia = 3



