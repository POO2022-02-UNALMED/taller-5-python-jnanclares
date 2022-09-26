

class Zoologico:
    _zonas = []
    # Atributos
    def __init__(self, nombre=None, ubicacion=None):
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
    
    def getZona(cls):
        return Zoologico._zonas


    # Métodos
    
    def agregarZonas(self, zona):
        Zoologico._zonas.append(zona)

    def cantidadTotalAnimales(self):
        return self._zonas[0].cantidadAnimales() + self._zonas[1].cantidadAnimales()