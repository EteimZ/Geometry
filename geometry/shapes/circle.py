from geometry.shapes.base import Shape
from math import pi

class Circle(Shape):

    def __init__(self, radius: float, x: float, y: float ):
        self._radius = radius
        self._x = x
        self._y = y
    
    @property
    def radius(self) -> float:
        return self._radius
    
    @radius.setter
    def radius(self, value: float):
        self._radius = value

    def circumference(self) -> float:
        return 2 * pi * self.radius
    
    def area(self) -> float:
        return pi * self.radius
    
    def get_pos(self) -> tuple[float, float]:
        return (self._x, self._y)

    