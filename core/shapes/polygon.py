from __future__ import annotations

from dataclasses import dataclass

from core.shape import Shape
from core.shapes.point import Point
from core.utils import almost_zero


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

    def area(self) -> float:
        """Return the area. Only implemented for triangles; raises NotImplementedError otherwise."""
        if len(self.vertices) != 3:
            raise NotImplementedError(
                f"area() is only implemented for triangles (3 vertices), "
                f"but this polygon has {len(self.vertices)} vertices."
            )
        a, b, c = self.vertices
        return 0.5 * abs(
            (b.x - a.x) * (c.y - a.y) - (c.x - a.x) * (b.y - a.y)
        )

    def contains_point(self, point: Point) -> bool:
        """Return True if the point lies inside or on the boundary of the polygon.

        For triangles uses the sign-of-cross-product method.
        For general polygons uses the ray-casting algorithm.
        """
        if len(self.vertices) == 3:
            return self._triangle_contains_point(point)
        return self._ray_casting_contains_point(point)

    def _triangle_contains_point(self, point: Point) -> bool:
        """Point-in-triangle via sign of cross products (handles boundary)."""
        a, b, c = self.vertices
        p = point

        def cross(p1: Point, p2: Point, p3: Point) -> float:
            return (p1.x - p3.x) * (p2.y - p3.y) - (p2.x - p3.x) * (p1.y - p3.y)

        d1 = cross(p, a, b)
        d2 = cross(p, b, c)
        d3 = cross(p, c, a)

        has_neg = (d1 < 0) or (d2 < 0) or (d3 < 0)
        has_pos = (d1 > 0) or (d2 > 0) or (d3 > 0)
        return not (has_neg and has_pos)

    def _ray_casting_contains_point(self, point: Point) -> bool:
        """Ray-casting algorithm for general simple polygons."""
        x, y = point.x, point.y
        n = len(self.vertices)
        inside = False
        j = n - 1
        for i in range(n):
            xi, yi = self.vertices[i].x, self.vertices[i].y
            xj, yj = self.vertices[j].x, self.vertices[j].y
            if (yi > y) != (yj > y):
                x_intersect = (xj - xi) * (y - yi) / (yj - yi) + xi
                if x < x_intersect:
                    inside = not inside
            j = i
        return inside

