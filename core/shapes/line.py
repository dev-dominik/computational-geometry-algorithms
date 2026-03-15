from __future__ import annotations

from dataclasses import dataclass

from core.shape import Shape
from core.shapes.point import Point


@dataclass
class Line(Shape):
    """Line segment defined by two endpoints."""
    start: Point
    end: Point

    def get_points(self) -> list[Point]:
        return [self.start, self.end]



