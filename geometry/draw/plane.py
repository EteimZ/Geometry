from abc import ABC, abstractmethod
import turtle

class Plane(ABC):
    """
    Abstract base class that represents a plane for 
    which shapes are to be drawn on.    
    """
    def __init__(self) -> None:
        self.process()

    @abstractmethod
    def construct(self):
        """
        Abstract method for user to place their logic.
        """
        pass

    def process(self):
        self.t = turtle.getturtle()
        self.t.ht()
        self.s = self.t.getscreen()
        self.construct()
        self.s.exitonclick() # type: ignore for pylance
