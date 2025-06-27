"""Utilities to convert acreage to square feet and compute area from DXF drawings."""

from __future__ import annotations

import math
from typing import Iterable, Tuple

try:
    import ezdxf  # type: ignore
except ImportError:  # pragma: no cover - ezdxf may not be installed
    ezdxf = None

SQFT_PER_ACRE = 43560.0


def convert_acreage_to_sqft(acres: float) -> float:
    """Convert an area in acres to square feet."""
    return acres * SQFT_PER_ACRE


def polygon_area(vertices: Iterable[Tuple[float, float]]) -> float:
    """Return the area of a polygon given its vertices using the shoelace formula."""
    points = list(vertices)
    if len(points) < 3:
        raise ValueError("A polygon requires at least three vertices")
    area = 0.0
    for (x1, y1), (x2, y2) in zip(points, points[1:] + points[:1]):
        area += x1 * y2 - x2 * y1
    return abs(area) / 2.0


def area_from_dxf(path: str, units: str = "foot") -> float:
    """Parse a DXF drawing and compute the total area of closed polylines in square feet.

    Parameters
    ----------
    path: str
        Path to the DXF file.
    units: str, optional
        Drawing units ("foot" or "meter"). Defaults to "foot".
    """
    if ezdxf is None:
        raise ImportError(
            "ezdxf is required for reading DXF files. Install with `pip install ezdxf`."
        )

    doc = ezdxf.readfile(path)
    msp = doc.modelspace()
    area = 0.0
    for entity in msp.query("LWPOLYLINE"):
        if entity.closed:
            points = [(v[0], v[1]) for v in entity.get_points()]
            area += polygon_area(points)

    if units.lower().startswith("meter"):
        area *= 10.76391041671  # square meters to square feet

    return area


def sqft_from_dxf(path: str, units: str = "foot") -> float:
    """High-level helper to compute square footage from a DXF drawing."""
    return area_from_dxf(path, units=units)
