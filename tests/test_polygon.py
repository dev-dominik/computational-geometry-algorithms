import math
import pytest

from core.shapes import Point, Polygon


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def tri(ax, ay, bx, by, cx, cy) -> Polygon:
    return Polygon([Point(ax, ay), Point(bx, by), Point(cx, cy)])


def quad(pts) -> Polygon:
    return Polygon([Point(x, y) for x, y in pts])


# ===========================================================================
# area()
# ===========================================================================

class TestTriangleArea:
    def test_right_triangle_345(self):
        # legs 3 and 4 → area = 6
        t = tri(0, 0, 3, 0, 0, 4)
        assert math.isclose(t.area(), 6.0)

    def test_unit_equilateral(self):
        # equilateral triangle with side 1
        h = math.sqrt(3) / 2
        t = tri(0, 0, 1, 0, 0.5, h)
        assert math.isclose(t.area(), math.sqrt(3) / 4, rel_tol=1e-9)

    def test_vertex_order_does_not_affect_area(self):
        # CW vs CCW should yield same area
        t_ccw = tri(0, 0, 4, 0, 0, 3)
        t_cw  = tri(0, 0, 0, 3, 4, 0)
        assert math.isclose(t_ccw.area(), t_cw.area())

    def test_degenerate_collinear_area_is_zero(self):
        # Three collinear points → zero area
        t = tri(0, 0, 1, 1, 2, 2)
        assert math.isclose(t.area(), 0.0, abs_tol=1e-12)

    def test_floating_point_coords(self):
        t = tri(0.5, 0.5, 2.5, 0.5, 0.5, 3.5)
        # base = 2, height = 3 → area = 3
        assert math.isclose(t.area(), 3.0, rel_tol=1e-9)

    def test_large_coords(self):
        t = tri(0, 0, 1e6, 0, 0, 1e6)
        assert math.isclose(t.area(), 0.5e12, rel_tol=1e-9)

    def test_negative_coords(self):
        t = tri(-3, -3, 3, -3, 0, 3)
        # base = 6, height = 6 → area = 18
        assert math.isclose(t.area(), 18.0)


class TestAreaNotImplementedForNonTriangle:
    def test_quadrilateral_raises(self):
        p = quad([(0, 0), (1, 0), (1, 1), (0, 1)])
        with pytest.raises(NotImplementedError):
            p.area()

    def test_pentagon_raises(self):
        pts = [(math.cos(2 * math.pi * i / 5), math.sin(2 * math.pi * i / 5)) for i in range(5)]
        p = quad(pts)
        with pytest.raises(NotImplementedError):
            p.area()

    def test_error_message_mentions_vertex_count(self):
        p = quad([(0, 0), (1, 0), (1, 1), (0, 1)])
        with pytest.raises(NotImplementedError, match="4"):
            p.area()


# ===========================================================================
# contains_point() — triangle
# ===========================================================================

class TestTriangleContainsPoint:
    @pytest.fixture
    def standard(self):
        # (0,0)–(4,0)–(0,4)
        return tri(0, 0, 4, 0, 0, 4)

    def test_centroid_inside(self, standard):
        centroid = Point(4 / 3, 4 / 3)
        assert standard.contains_point(centroid)

    def test_vertex_on_boundary(self, standard):
        assert standard.contains_point(Point(0, 0))
        assert standard.contains_point(Point(4, 0))
        assert standard.contains_point(Point(0, 4))

    def test_edge_midpoint_on_boundary(self, standard):
        # midpoint of hypotenuse
        assert standard.contains_point(Point(2, 2))
        # midpoint of bottom edge
        assert standard.contains_point(Point(2, 0))

    def test_outside_point(self, standard):
        assert not standard.contains_point(Point(5, 5))
        assert not standard.contains_point(Point(-1, -1))
        assert not standard.contains_point(Point(3, 3))  # beyond hypotenuse

    def test_just_outside_edge(self, standard):
        assert not standard.contains_point(Point(2.01, 2.01))

    def test_degenerate_triangle_collinear(self):
        # All three vertices on x-axis → area 0
        t = tri(0, 0, 2, 0, 4, 0)
        # A point on the same line between vertices
        # With sign-of-cross-product, all cross products are 0 → inside
        assert t.contains_point(Point(2, 0))

    def test_point_far_away(self, standard):
        assert not standard.contains_point(Point(1e9, 1e9))

    def test_cw_wound_triangle(self):
        # Same triangle but CW vertex order
        t = tri(0, 0, 0, 4, 4, 0)
        assert t.contains_point(Point(1, 1))
        assert not t.contains_point(Point(5, 5))

    def test_very_thin_triangle(self):
        # Nearly degenerate but has tiny area
        t = tri(0, 0, 100, 1e-6, 50, 0)
        # centroid
        cx, cy = 50, 1e-6 / 3
        assert t.contains_point(Point(cx, cy))
        # far outside
        assert not t.contains_point(Point(0, 1))

    def test_single_vertex_query_matches_vertex(self):
        t = tri(1, 1, 5, 1, 3, 4)
        assert t.contains_point(Point(1, 1))


# ===========================================================================
# contains_point() — general polygon (ray casting)
# ===========================================================================

class TestPolygonContainsPoint:
    @pytest.fixture
    def unit_square(self):
        return quad([(0, 0), (1, 0), (1, 1), (0, 1)])

    @pytest.fixture
    def l_shape(self):
        # L-shaped hexagon
        return quad([(0, 0), (2, 0), (2, 1), (1, 1), (1, 2), (0, 2)])

    def test_center_inside_square(self, unit_square):
        assert unit_square.contains_point(Point(0.5, 0.5))

    def test_outside_square(self, unit_square):
        assert not unit_square.contains_point(Point(2, 2))
        assert not unit_square.contains_point(Point(-0.1, 0.5))

    def test_corner_of_square(self, unit_square):
        # Ray casting may or may not count corners as inside — just verify no crash
        _ = unit_square.contains_point(Point(0, 0))

    def test_inside_l_shape(self, l_shape):
        assert l_shape.contains_point(Point(0.5, 0.5))
        assert l_shape.contains_point(Point(0.5, 1.5))

    def test_outside_l_shape_in_notch(self, l_shape):
        # The "missing" square at (1,1)–(2,2)
        assert not l_shape.contains_point(Point(1.5, 1.5))

    def test_outside_l_shape_far(self, l_shape):
        assert not l_shape.contains_point(Point(5, 5))

    def test_large_polygon_centroid(self):
        # Regular octagon centred at origin, radius 10
        n = 8
        pts = [(10 * math.cos(2 * math.pi * i / n), 10 * math.sin(2 * math.pi * i / n)) for i in range(n)]
        p = quad(pts)
        assert p.contains_point(Point(0, 0))
        assert not p.contains_point(Point(11, 0))

    def test_point_exactly_at_origin_inside_square(self, unit_square):
        # (0,0) is a vertex; ray-casting result is implementation-defined but must not crash
        result = unit_square.contains_point(Point(0, 0))
        assert isinstance(result, bool)


# ===========================================================================
# Polygon construction edge cases
# ===========================================================================

class TestPolygonConstruction:
    def test_too_few_vertices_raises(self):
        with pytest.raises(ValueError):
            Polygon([Point(0, 0), Point(1, 1)])

    def test_exactly_three_vertices_ok(self):
        p = Polygon([Point(0, 0), Point(1, 0), Point(0, 1)])
        assert len(p.vertices) == 3