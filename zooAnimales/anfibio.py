from zooAnimales.animal import Animal

class Anfibio (Animal):
    anfibios = 0
    ranas = 0
    salamandras = 0
    _listado = []
    
    def __init__(self, nombre=None, edad=None, habitat=None, genero=None, colorPiel=None, venenoso=None):
        super().__init__(nombre, edad, habitat, genero)
        self._colorPiel = colorPiel
        self._venenoso = venenoso
        Anfibio.anfibios += 1
        Anfibio._listado.append(self)
        
    
    def getListado():
        return Anfibio._listado

        
    def getColorPiel(self):
        return self._colorPiel
    
    def setColorPiel(self, colorPiel):
        self._colorPiel = colorPiel
        
    def isVenenoso(self):
        return self._venenoso
    
    def setVenenoso(self, venenoso):
        self._venenoso = venenoso
        
    
    def cantidadAnfibios():
        return Anfibio.anfibios
    
    def movimiento():
        return "saltar"
    
    def crearRana(nombre, edad, genero):
        Anfibio.ranas += 1
        return Anfibio(nombre, edad, "selva", genero, "rojo", True)
    
    def crearSalamandra(nombre, edad, genero):
        Anfibio.salamandras += 1
        return Anfibio(nombre, edad, "selva", genero, "negro y amarillo", False)
        
    