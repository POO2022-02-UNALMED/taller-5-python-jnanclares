class Zona:
    # Atributos
    def __init__(self, nombre=None, zoologico=None):
        self._nombre = nombre
        self._zoologico = zoologico
        self._animales = []
        
    # Get and Set
    def getNombre(self):
        return self._nombre
    
    def setNombre(self, nombre):
        self._nombre = nombre
        
    def getZoo(self):
        return self._zoologico
    
    def setNombre(self, zoologico):
        self._zoologico = zoologico
    
    def getAnimales(self):
        return self._animales


    # Métodos
    def agregarAnimales(self, animal):
        self._animales.append(animal)
        
    def cantidadAnimales(self):
        return len(self._animales)