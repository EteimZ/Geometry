from abc import abstractmethod
from geometry.shapes.base import Shape


class Quad(Shape):

    """"
    Abstract Base Class of Quadrilaterals
    """

    @abstractmethod
    def perimeter(self) -> float:
        pass

class Rectangle(Quad):
    
    def __init__(self, width: float, height: float, x: float, y:float ) -> None:
        self._width = width
        self._height = height
        self._x = x
        self._y = y
    
    @property
    def width(self) -> float:
        return self._width
    
    @width.setter
    def width(self, value: float):
        self._width = value

    @property
    def height(self) -> float:
        return self._height
    
    @height.setter
    def height(self, value: float):
        self._height = value

    def area(self) -> float:
        return self.width * self.height
    
    def get_pos(self) -> tuple[float, float]:
        return (self._x, self._y)
    
    def perimeter(self) -> float:
        return 2 * (self.width + self.height)


class Square(Quad):
    
    def __init__(self, length: float, x: float, y:float ) -> None:
        self._length = length
        self._x = x
        self._y = y
    
    @property
    def length(self) -> float:
        return self._length
    
    @length.setter
    def length(self, value: float):
        self._length = value

    def area(self) -> float:
        return self._length * self._length
    
    def get_pos(self) -> tuple[float, float]:
        return (self._x, self._y)
    
    def perimeter(self) -> float:
        return 4 * self._length

    