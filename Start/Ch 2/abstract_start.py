# Python Object Oriented Programming by Joe Marini course example
# Using Abstract Base Classes to enforce class constraints
"""
1. We don't want consumers of the base class to be able to create an instance of the base class itself.

2. Enfoce the constraint that methods in the base class has to be implemented in the subclasses.
    - In this example, we want to prevent GraphicShape to be instantiated.
"""

from abc import ABC, abstractmethod 

class GraphicShape(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod 
    def calcArea(self):
        pass


class Circle(GraphicShape):
    def __init__(self, radius):
        self.radius = radius
    
    def calcArea(self):
        return 3.14 * (self.radius ** 2) 


class Square(GraphicShape):
    def __init__(self, side):
        self.side = side

    def calcArea(self):
        return (self.side ** 2)

# g = GraphicShape()

c = Circle(10)
print(c.calcArea())
s = Square(12)
print(s.calcArea())
