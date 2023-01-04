from abc import ABC, abstractmethod


class Shape(ABC):
    """"
    Abstract Base Class of shapes
    """

    @abstractmethod
    def area(self) -> float:
        pass

    @abstractmethod
    def get_pos(self) -> tuple[float, float]:
        pass