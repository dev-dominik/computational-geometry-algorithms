import matplotlib.pyplot as plt
import numpy as np

from core.shapes import Segment, Line, Point


class Drawer:

    def __init__(self):
        self._lines: list[Line] = []
        self._segments: list[Segment] = []
        self._points: list[Point] = []

    def line(self, line: Line) -> "Drawer":
        self._lines.append(line)
        return self

    def segment(self, segment: Segment) -> "Drawer":
        self._segments.append(segment)
        return self

    def point(self, point: Point) -> "Drawer":
        self._points.append(point)
        return self

    def points(self, points: list[Point]) -> "Drawer":
        self._points.extend(points)
        return self

    def draw(self, x_range=(-10, 10)):
        plt.figure()

        for line in self._lines:
            if line.b != 0:
                x = np.linspace(x_range[0], x_range[1], 400)
                y = (-line.a * x - line.c) / line.b
                plt.plot(x, y, label=f"{line.a}x + {line.b}y + {line.c} = 0")
            else:
                x_val = -line.c / line.a
                y = np.linspace(x_range[0], x_range[1], 400)
                x = np.full_like(y, x_val)
                plt.plot(x, y, label=f"x = {x_val}")

        for segment in self._segments:
            xs = [segment.start.x, segment.end.x]
            ys = [segment.start.y, segment.end.y]
            plt.plot(xs, ys, marker="o", label="segment")

        if self._points:
            xs = [p.x for p in self._points]
            ys = [p.y for p in self._points]

            plt.scatter(xs, ys)

            for p in self._points:
                plt.text(p.x, p.y, f"({p.x}, {p.y})")

        plt.xlabel("X")
        plt.ylabel("Y")
        plt.grid(True)
        plt.axis("equal")
        plt.legend()

        plt.show()