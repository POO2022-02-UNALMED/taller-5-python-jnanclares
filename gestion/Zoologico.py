

class Zoologico:
    _zonas = []
    # Atributos
    def __init__(self, nombre, ubicacion):
        self._nombre = nombre
        self._ubicacion = ubicacion
        
    # Get and Set
    def getNombre(self):
        return self._nombre
    
    def setNombre(self, nombre):
        self._nombre = nombre
        
    def getUbicacion(self):
        return self._ubicacion
    
    def setNombre(self, ubicacion):
        self._ubicacion = ubicacion
    
    def getZona():
        return Zoologico._zonas


    # Métodos
    
    def agregarZonas(self, zona):
        Zoologico._zonas.append(zona)

    def cantidadTotalAnimales(self):
        return self.zonas[0].cantidadAnimales() + self.zonas[1].cantidadAnimales()