from geometry.draw.base import DrawShape
from geometry.shapes.circle import Circle
from geometry.shapes.quadrilateral import Rectangle, Square
import turtle

    
class DrawCircle(DrawShape):

    def __init__(self, turtle: turtle.Turtle, circle: Circle) -> None:
        self.t = turtle
        self.c = circle
        self.draw()

    def draw(self):
        if turtle.isdown():
            turtle.pu()
        turtle.goto(self.c.get_pos())
        turtle.pd()
        turtle.circle(self.c.radius)


class DrawSqaure(DrawShape):

    def __init__(self, turtle: turtle.Turtle, square: Square) -> None:
        self.t = turtle
        self.sq = square
        self.draw()

    def draw(self):
        if turtle.isdown():
            turtle.pu()
        turtle.goto(self.sq.get_pos())
        turtle.pd()
        turtle.fd(self.sq.length)
        turtle.setheading(270)
        turtle.fd(self.sq.length)
        turtle.setheading(180)
        turtle.fd(self.sq.length)
        turtle.setheading(90)
        turtle.fd(self.sq.length)
        turtle.pu()


class DrawRectangle(DrawShape):

    def __init__(self, turtle: turtle.Turtle, rectangle: Rectangle) -> None:
        self.t = turtle
        self.rect = rectangle
        self.draw()

    def draw(self):
        if turtle.isdown():
            turtle.pu()
        turtle.goto(self.rect.get_pos())
        turtle.pd()
        turtle.fd(self.rect.width)
        turtle.setheading(270)
        turtle.fd(self.rect.height)
        turtle.setheading(180)
        turtle.fd(self.rect.width)
        turtle.setheading(90)
        turtle.fd(self.rect.height)
        turtle.pu()
