from Animal import Animal

class Ave (Animal):
    aves = 0
    halcones = 0
    aguilas = 0
    _listado = []
    
    def __init__(self, nombre, edad, habitat, genero, colorPlumas):
        super().__init__(nombre, edad, habitat, genero)
        self._colorPlumas = colorPlumas
        Ave.aves += 1
        Ave._listado.append(self)
        
    
    def getListado():
        return Ave._listado

        
    def getColorPlumas(self):
        return self._colorPlumas
    
    def setcolorPlumas(self, colorPlumas):
        self._colorPlumas = colorPlumas
        
    
    def cantidadAves():
        return Ave.aves
    
    def movimiento():
        return "volar"
    
    def crearHalcon(self, nombre, edad, genero):
        Ave.halcones += 1
        return Ave(nombre, edad, "montanas", genero, "cafe glorioso")
    
    def crearAguila(self, nombre, edad, genero):
        Ave.aguilas += 1
        return Ave(nombre, edad, "montanas", genero, "blanco y amarillo")
        
        
    