from Animal import Animal

class Pez (Animal):
    peces = 0
    salmones = 0
    bacalaos = 0
    _listado = []
    
    def __init__(self, nombre, edad, habitat, genero, colorEscamas, cantidadAletas):
        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas = colorEscamas
        self._cantidadAletas = cantidadAletas
        Pez.peces += 1
        Pez._listado.append(self)
        
    
    def getListado():
        return Pez._listado

        
    def getColorEscamas(self):
        return self._colorEscamas
    
    def setColorEscamas(self, colorEscamas):
        self._colorEscamas = colorEscamas
        
    def getCantidadAletas(self):
        return self._cantidadAletas
    
    def setCantidadAletas(self, cantidadAletas):
        self._cantidadAletas = cantidadAletas
        
    
    def cantidadPeces():
        return Pez.peces
    
    def movimiento():
        return "nadar"
    
    def crearSalmon(self, nombre, edad, genero):
        Pez.salmones += 1
        return Pez(nombre, edad, "oceano", genero, "rojo", 6)
    
    def crearBacalao(self, nombre, edad, genero):
        Pez.bacalaos += 1
        return Pez(nombre, edad, "oceano", genero, "gris", 6)

        
    