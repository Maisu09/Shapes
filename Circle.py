from math import pi
from Shapes import Shapes

class Circle(Shapes):
    __radius = float(0)

    def __init__(self, radius:float):
        super().__init__(radius*radius*pi, 2*pi*radius)
        self.__radius = radius

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, radius):
        print("radius was set")
        self.__radius = radius
        self.__init__(self.__radius)
    
    def Display(self):
        return super().Display()
    