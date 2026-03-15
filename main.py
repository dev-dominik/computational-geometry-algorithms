from core import Line, Point, Polygon
from file_io.parser import get_element_points
from render.renderer2D import draw_line, draw_points, draw_polygon, draw_elements

draw_elements([get_element_points(1), get_element_points(2), get_element_points(3)])

line = Line(Point(0, 0), Point(1, 5))
#draw_line(line)

point = Point(3, 8)
#draw_points([point])

polygon = Polygon([Point(1,1), Point(5, 0), Point(3,4), Point(1, 4)])
#draw_polygon(polygon)

