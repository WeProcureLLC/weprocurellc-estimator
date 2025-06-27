import math
import pytest

from acreage_to_sqft import convert_acreage_to_sqft, polygon_area


def test_convert_acreage_to_sqft():
    assert convert_acreage_to_sqft(1) == pytest.approx(43560.0)
    assert convert_acreage_to_sqft(0.5) == pytest.approx(21780.0)


def test_polygon_area_square():
    square = [(0, 0), (0, 10), (10, 10), (10, 0)]
    assert polygon_area(square) == pytest.approx(100.0)


def test_polygon_area_triangle():
    triangle = [(0, 0), (5, 0), (0, 5)]
    assert polygon_area(triangle) == pytest.approx(12.5)
