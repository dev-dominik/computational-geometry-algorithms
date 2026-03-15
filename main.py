from core.shapes import Segment, Point, Line
from render import Drawer

p1 = Point(1, 2)
p2 = Point(4, 5)

#1. Determine the line equation for a segment defined by two points.
line = Line.create(p1, p2)
Drawer().line(line).points([p1, p2]).draw()

#2. Check if a point belongs to the line
print("2: Belongs to line: ", line.contains_point(p1))
print("2: Does not belong to line: ", line.contains_point(Point(-1, 5)))

#3. Check if a point belongs to the segment (line bounded on both sides)
p3 = Point(3, -4)
p4 = Point(-2, 3)

segment = Segment(p3, p4)

Drawer().segment(segment).points([p3, p4]).draw()

print("3: Belongs to segment: ", segment.contains_point(p3))
print("3: Does not belong to segment: ", segment.contains_point(Point(-4, -4)))

#4. Determine the position of a point relative to the line (right/left)
p5 = Point(-5, 5)
print("Position of point relative to line (right/left): ", line.point_position(p3))
print("Position of point relative to line (right/left): ", line.point_position(p5))
Drawer().line(line).points([p3, p5]).draw()

#5. Translate the segment by a given vector
segment1 = Segment(Point(1, 2), Point(3, 4))
segment2 = segment1.translate(0, 2)

Drawer().segment(segment2).segment(segment1).draw()

#6. Reflect a point across the line
p6 = Point(0, 0)
p7 = Point(2, 2)

line = Line.create(p6, p7)

point = Point(3, 1)
reflected = line.reflect_point(point)

print("Point:", point)
print("Reflection:", reflected)

Drawer().line(line).points([point, reflected]).draw()
