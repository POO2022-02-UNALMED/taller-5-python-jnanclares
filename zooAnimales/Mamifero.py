from zooAnimales.animal import Animal

class Mamifero (Animal):
    mamiferos = 0
    caballos = 0
    leones = 0
    _listado = []
    
    def __init__(self, nombre=None, edad=None, habitat=None, genero=None, pelaje=None, patas=None):
        super().__init__(nombre, edad, habitat, genero)
        self._pelaje = pelaje
        self._patas = patas
        Mamifero.mamiferos += 1
        Mamifero._listado.append(self)
        
    
    def getListado():
        return Mamifero._listado

    def isPelaje(self):
        return self._pelaje
    
    def setPelaje(self, pelaje):
        self._pelaje = pelaje
        
    def getPatas(self):
        return self._patas
    
    def setPatas(self, patas):
        self._patas = patas
        
    
    def cantidadMamiferos():
        return Mamifero.mamiferos
    
    def crearCaballo(nombre, edad, genero):
        Mamifero.caballos += 1
        return Mamifero(nombre, edad, "pradera", genero, True, 4)
    
    def crearLeon(nombre, edad, genero):
        Mamifero.leones += 1
        return Mamifero(nombre, edad, "selva", genero, True, 4)
        
        
    