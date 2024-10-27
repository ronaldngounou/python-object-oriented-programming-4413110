# Python Object Oriented Programming by Joe Marini course example
# Using Abstract Base Classes to implement interfaces
# By implementing an interface, a particular class makes a contract to provide a certain kind of behavior or capabilities 

# If we would like the class to provide a json object

from abc import ABC, abstractmethod


class GraphicShape(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def calcArea(self):
        pass

class JSONify(ABC):
    @abstractmethod 
    def toJSON(self):
        pass

# we can apply this new class wherever we want. Python implements interfaces with abstract base classes (ABC) 
# and multiple inheritances.

class Circle(GraphicShape, JSONify): # this has the effect of the Circle class that has to implement the toJSON method
    def __init__(self, radius):
        self.radius = radius

    def calcArea(self):
        return 3.14 * (self.radius ** 2)

    def toJSON(self):
        return f"{{'Circle': {str(self.calcArea())}}} " 
    
c = Circle(10)
print(c.calcArea())
print(c.toJSON())
