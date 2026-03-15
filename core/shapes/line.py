from __future__ import annotations

from dataclasses import dataclass

from core.shapes import Point
from core.utils import almost_zero


@dataclass
class Line:
    a: int
    b: int
    c: int

    def print_equation(self):
        print(f'{self.a}x + {self.b}y + {self.c} = 0')

    @staticmethod
    def create(point1: Point, point2: Point) -> Line:
        x1, y1 = point1.x, point1.y
        x2, y2 = point2.x, point2.y

        if x1 == x2 and y1 == y2:
            raise ValueError("Cannot determine a line from two identical points.")

        a = y1 - y2
        b = x2 - x1
        c = x1 * y2 - x2 * y1

        return Line(a, b, c)

    def contains_point(self, point: Point) -> bool:
        return almost_zero(self.a * point.x + self.b * point.y + self.c)

    def point_position(self, point: Point) -> str:
        """
        Determine the position of a point relative to the line.
        """

        value = self.a * point.x + self.b * point.y + self.c

        if almost_zero(value):
            return "on"
        elif value > 0:
            return "left"
        else:
            return "right"

    def reflect_point(self, point: Point) -> Point:
        """
        Reflect a point across the line Ax + By + C = 0.
        """

        x0, y0 = point.x, point.y
        a, b, c = self.a, self.b, self.c

        d = (a * x0 + b * y0 + c) / (a * a + b * b)

        x_ref = x0 - 2 * a * d
        y_ref = y0 - 2 * b * d

        return Point(x_ref, y_ref)

