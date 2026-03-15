import matplotlib.pyplot as plt

from core import Point, Line, Polygon, Shape


def draw_points(points: list[Point]) -> None:
    xs = [p.x for p in points]
    ys = [p.y for p in points]

    plt.scatter(xs, ys)

    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Wykres punktów")

    plt.grid(True)
    plt.show()

def draw_line_between_nodes(points: list[Point]) -> None:
    xs = [p.x for p in points]
    ys = [p.y for p in points]

    plt.scatter(xs, ys)

    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Wykres połączonych punktów")

    plt.plot(xs, ys, marker="o")

    plt.grid(True)
    plt.show()

def draw_line(line: Line) -> None:
    xs = [line.start.x, line.end.x]
    ys = [line.start.y, line.end.y]

    plt.plot(xs, ys, marker="o")

    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Wykres odcinka")
    plt.grid(True)
    plt.show()

def draw_polygon(polygon: Polygon) -> None:
    x = []
    y = []

    for p in polygon.vertices:
        x.append(p.x)
        y.append(p.y)

    x.append(polygon.vertices[0].x)
    y.append(polygon.vertices[0].y)

    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Wykres wielokąta")

    plt.plot(x, y, marker="o")

    plt.grid(True)
    plt.show()

def draw_elements(elements: list[list[Point]]) -> None:
    plt.figure()

    for element_points in elements:
        if not element_points:
            continue

        xs = [p.x for p in element_points]
        ys = [p.y for p in element_points]

        xs.append(element_points[0].x)
        ys.append(element_points[0].y)

        # rysowanie punktów
        plt.scatter(xs, ys)

        # rysowanie połączeń tylko w obrębie jednej listy
        if len(element_points) > 1:
            plt.plot(xs, ys, marker="o")

    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Wykres elementów")
    plt.grid(True)
    plt.show()

def draw_shapes(shapes: list[Shape]) -> None:
    elements = []
    for shape in shapes:
        elements.append(shape.get_points())

    draw_elements(elements)