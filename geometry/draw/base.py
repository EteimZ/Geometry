from abc import ABC, abstractmethod


class DrawShape(ABC):
    """"
    Abstract Base Class to draw shapes
    """

    @abstractmethod
    def draw(self) -> None:
        pass

