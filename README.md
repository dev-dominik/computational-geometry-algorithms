# 2D Geometry Library

A Python library for 2D computational geometry with matplotlib-based visualization.

## Features

- **Point** — 2D Cartesian point
- **Line** — infinite line defined by equation `Ax + By + C = 0`
  - Create from two points
  - Check if a point lies on the line
  - Determine point position relative to the line (left/right)
  - Reflect a point across the line
- **Segment** — line segment defined by two endpoints
  - Check if a point lies on the segment
  - Translate by a vector
- **Polygon** — polygon defined by an ordered list of vertices
- **Drawer** — fluent 2D renderer (matplotlib) for lines, segments, and points
- **File I/O** — parse nodes and elements from text files

## Project Structure

```
core/
  shape.py          # Abstract base class
  shapes/
    point.py
    line.py
    segment.py
    polygon.py
  utils.py          # Floating-point helpers
file_io/
  parser.py         # Node/element file parsing
render/
  renderer2D.py     # Matplotlib-based Drawer
main.py             # Usage examples
```

## Requirements

- Python 3.10+
- `matplotlib`
- `numpy`

Install dependencies:

```bash
pip install matplotlib numpy
```

## Usage

```python
from core.shapes import Point, Line, Segment
from render import Drawer

p1, p2 = Point(1, 2), Point(4, 5)

# Create a line through two points
line = Line.create(p1, p2)

# Check point membership
line.contains_point(p1)          # True
line.point_position(Point(0, 0)) # "left" | "right" | "on"

# Reflect a point across the line
reflected = line.reflect_point(Point(3, 1))

# Segment operations
segment = Segment(Point(0, 0), Point(3, 4))
segment.contains_point(Point(1, 1))  # True/False
segment.translate(1, -1)             # returns new Segment

# Visualize
Drawer().line(line).points([p1, p2]).draw()
```

Run the bundled examples:

```bash
python main.py
```