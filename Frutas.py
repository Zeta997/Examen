from abc import ABC, abstractmethod

class Fruta(ABC):
    def __init__(self, nombre, cantidad):
        self.nombre = nombre
        self.cantidad = cantidad

    @abstractmethod
    def descripcion(self):
        pass

class Manzana(Fruta):
    def __init__(self, nombre, cantidad, variedad):
        super().__init__(nombre, cantidad)
        self.variedad = variedad
    def descripcion(self):
        return f"{self.nombre} es una manzana de variedad {self.variedad} Tiene un sabor dulce y es ideal para comer fresca o para hacer zumo."
    
class Banana(Fruta):
    def __init__(self, nombre, cantidad, madurez):
        super().__init__(nombre, cantidad)
        self.madurez = madurez
    def descripcion(self):
        return f"Esta es una banana de madurez {self.madurez}"  

class Naranja(Fruta):
    def __init__(self, nombre, cantidad, dulzor):
        super().__init__(nombre, cantidad)
        self.dulzor = dulzor
    def descripcion(self):
        return f"Esta es una naranja de dulzor {self.dulzor}"     
