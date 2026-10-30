# HAC2026 baseline submission: bounding-cylinder ellipsoids

Reconstruction of 3D asteroid shapes from lightcurve data for the
[Helsinki Asteroid Challenge 2026](https://fips.fi/data-challenges/helsinki-asteroid-challenge-2026/).

## Overview

The simplest possible reconstruction consistent with the challenge's prior information:
for each asteroid, return the ellipsoid that fills the published bounding cylinder -
rotation axis z, z-extent exactly [-1, 1], max cylindrical radius equal to the published
radius R. No lightcurve information is used.

This is the trivial baseline that any lightcurve-informed algorithm should beat; it
establishes a floor score for the challenge's two evaluation measures.

## Setup and running

Requires Python >= 3.11 and [uv](https://docs.astral.sh/uv/). No GPU needed.

```bash
uv sync
uv run python run.py                  # all 10 asteroids -> reconstructed/asteroid_NN.stl
uv run python run.py --asteroids 4 9  # subset
```

The one optional input, the bounding-cylinder radius per model, is tabulated in `run.py`
(from the challenge website). Runs in seconds. `reconstructed/` already contains the
STLs for all 10 models.

## Output

`reconstructed/asteroid_NN.stl` - binary STL in the competition frame: rotation axis z,
top/bottom touching z=+1/-1, max cylindrical radius R, light source at (-inf, 0, 0).
