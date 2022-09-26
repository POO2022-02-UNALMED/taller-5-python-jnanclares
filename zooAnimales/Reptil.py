from Animal import Animal

class Reptil (Animal):
    reptiles = 0
    iguanas = 0
    serpientes = 0
    _listado = []
    
    def __init__(self, nombre, edad, habitat, genero, colorEscamas, largoCola):
        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas = colorEscamas
        self._largoCola = largoCola
        Reptil.reptiles += 1
        Reptil._listado.append(self)
        
    
    def getListado():
        return Reptil._listado

        
    def getColorEscamas(self):
        return self._colorEscamas
    
    def setColorEscamas(self, colorEscamas):
        self._colorEscamas = colorEscamas
        
    def getLargoCola(self):
        return self._largoCola
    
    def setLargoCola(self, largoCola):
        self._largoCola = largoCola
        
    
    def cantidadReptiles():
        return Reptil.reptiles
    
    def movimiento():
        return "reptar"
    
    def crearIguana(self, nombre, edad, genero):
        Reptil.iguanas += 1
        return Reptil(nombre, edad, "humedal", genero, "verde", 3)
    
    def crearSerpiente(self, nombre, edad, genero):
        Reptil.serpientes += 1
        return Reptil(nombre, edad, "jungla", genero, "blanco", 1)
        
        
    