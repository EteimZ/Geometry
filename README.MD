# Geometry

This repo implements various concepts from [Euclidean geometry](https://en.wikipedia.org/wiki/Euclidean_geometry) using [OOP](https://en.wikipedia.org/wiki/Object-oriented_programming).

## Usage

```python
from geometry.draw.plane import Plane
from geometry.draw.shape import DrawCircle
from geometry.shapes.circle import Circle

class Board(Plane):
    def construct(self):
        DrawCircle(self.t, Circle(10, 0,0))


Board()
```

The repo contains Shapes and they can be drawn on a plane.
In the example above **Circle** class is a shape which is drawn by
the **DrawCircle** on a **Board** which is a subclass of the **Plane** abstract base class.

## Todo

- [ ] Add more shapes and their equivalent drawers.
- [ ] Read up on Euclidean Geometry  
