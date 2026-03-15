from __future__ import annotations

from dataclasses import dataclass

from core.shape import Shape
from core.shapes.point import Point
from core.utils import almost_zero


@dataclass
class Segment(Shape):
    """Line segment defined by two endpoints."""

    start: Point
    end: Point

    def get_points(self) -> list[Point]:
        return [self.start, self.end]

    def contains_point(self, point: Point, eps: float = 1e-9) -> bool:
        x1, y1 = self.start.x, self.start.y
        x2, y2 = self.end.x, self.end.y
        x, y = point.x, point.y

        cross = (x2 - x1) * (y - y1) - (y2 - y1) * (x - x1)
        if almost_zero(cross):
            return True

        if (
                min(x1, x2) - eps <= x <= max(x1, x2) + eps and
                min(y1, y2) - eps <= y <= max(y1, y2) + eps
        ):
            return True

        return False

    def translate(self, dx: float, dy: float) -> "Segment":
        new_start = Point(self.start.x + dx, self.start.y + dy)
        new_end = Point(self.end.x + dx, self.end.y + dy)

        return Segment(new_start, new_end)