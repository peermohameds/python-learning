import math

from cartesian import Point

class Triangle:
    def __init__(self, vertice1, vertice2, vertice3):
        self.base = vertice1.distance_from_point(vertice2)
        self.perp = vertice1.distance_from_point(vertice3)
        self.hypote = math.hypot(self.base, self.perp)

    def perimeter(self):
        return self.base + self.perp + self.hypote


triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())
