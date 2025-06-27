# weprocurellc-estimator

This repository contains utilities for converting acreage to square feet and
computing area from civil engineering drawings (DXF). The core script is
`acreage_to_sqft.py` which exposes several helper functions:

- `convert_acreage_to_sqft(acres)` – multiply acreage by 43,560.
- `polygon_area(vertices)` – compute the area of a polygon using the shoelace formula.
- `area_from_dxf(path, units="foot")` – parse a DXF file to compute the area of
  closed polylines. Requires the optional `ezdxf` package.

The `tests/` directory contains unit tests for the acreage conversion and
polygon area calculations.
