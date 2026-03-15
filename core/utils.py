import math

# Global tolerance for floating point comparisons
EPS = 1e-9


def almost_zero(value: float) -> bool:
    """Return True if value is close to zero."""
    return math.isclose(value, 0.0, abs_tol=EPS)
