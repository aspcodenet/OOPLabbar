import math

class Circle:
    def __init__(self,radius):
        self._radius = float(radius)

    def Area(self):
        return math.pi * self._radius ** 2

    def Circumference(self):
        return math.pi * self._radius * 2
