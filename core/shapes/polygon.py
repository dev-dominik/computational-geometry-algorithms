from __future__ import annotations

from dataclasses import dataclass

from core.shape import Shape
from core.shapes.point import Point


@dataclass
class Polygon(Shape):
    """Polygon defined by an ordered list of vertices (at least 3)."""
    vertices: list[Point]

    def __post_init__(self) -> None:
        if len(self.vertices) < 3:
            raise ValueError(
                f"A polygon requires at least 3 vertices, got {len(self.vertices)}."
            )

    def get_points(self) -> list[Point]:
        return self.vertices

