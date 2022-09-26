from gestion.Zona import Zona
from Animal import Mamifero
from Animal import Ave
from Animal import Reptil
from Animal import Pez
from Animal import Anfibio

class Animal:
    _zona = None
    _totalAnimales = 0
    
    def __init__(self, nombre, edad, habitat, genero):
        Animal._totalAnimales += 1
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        
    def getTotalAnimales(self):
        return Animal._totalAnimales
    
    
    def getNombre(self):
        return self._nombre
    
    def setNombre(self, nombre):
        self._nombre = nombre

    def getEdad(self):
        return self._edad
    
    def setEdad(self, edad):
        self._edad = edad
        
    def getHabitat(self):
        return self._nombre
    
    def setHabitat(self, habitat):
        self._habitat = habitat
    
    def getGenero(self):
        return self._genero
    
    def setGenero(self, genero):
        self._genero = genero
      
        
    def getZona():
        return Animal._zona
    
    @classmethod
    def setZona(cls, zona):
        cls._zona = zona
        
    
    def movimiento():
        return "desplazarse"
    
    
    def totalPorTipo():
        return f"Mamiferos: {Mamifero.cantidadMamiferos()}\nAve: {Ave.cantidadAve()}\nReptil: {Reptil.cantidadReptil()}\nPez: {Pez.cantidadPez()}\nAnfibio: {Anfibio.cantidadAnfibio()}" 
    
    def __str__(self):
        cadena = f"Mi nombre es {Animal.getNombre()}, tengo una edad de {Animal.getEdad()}, habito en {Animal.getHabitat()} y mi genero es {Animal.getGenero()}, la zona en la que me ubico es {Animal.getZona()}, en el {Animal.getZona().getZoologico()}"