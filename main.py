from geometry.draw.plane import Plane
from geometry.draw.shape import DrawCircle
from geometry.shapes.circle import Circle

class Board(Plane):
    def construct(self):
        DrawCircle(self.t, Circle(10, 0,0))


Board()




