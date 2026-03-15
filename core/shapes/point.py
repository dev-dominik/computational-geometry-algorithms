from __future__ import annotations

from dataclasses import dataclass

from core.shape import Shape


@dataclass
class Point(Shape):
    """2D point with Cartesian coordinates."""

    def get_points(self) -> list[Point]:
        pass

    x: float
    y: float


