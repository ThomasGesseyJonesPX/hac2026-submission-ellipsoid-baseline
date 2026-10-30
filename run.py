"""HAC2026 baseline submission: bounding-cylinder ellipsoids.

Returns, for each asteroid, the ellipsoid that fills the published bounding cylinder:
rotation axis z, z-extent [-1, 1], radius R. No lightcurve information is used - this is
the trivial baseline the challenge scores against.

Usage:
    uv run python run.py                 # all 10 asteroids -> reconstructed/asteroid_NN.stl
"""

from __future__ import annotations

import argparse
import logging
from pathlib import Path

import trimesh

REPO_ROOT = Path(__file__).parent
OUTPUT_DIR = REPO_ROOT / "reconstructed"

# Published bounding-cylinder radius R per model (challenge website, "Cylinder Base Radius R by Model").
RADII = {
    1: 1.12,
    2: 1.42,
    3: 0.88,
    4: 1.475,
    5: 1.22,
    6: 0.925,
    7: 1.205,
    8: 1.24,
    9: 0.67,
    10: 3.95,
}

logger = logging.getLogger(__name__)


def ellipsoid_stl(radius: float, out_path: Path) -> None:
    """Write the z-normalised ellipsoid for one asteroid.

    Icosphere of radius R squashed in z by 1/R, so z spans [-1, 1] and the max cylindrical
    radius is exactly R.
    """
    sphere = trimesh.creation.icosphere(radius=radius, subdivisions=5)
    verts = sphere.vertices.copy()
    verts[:, 2] /= radius
    mesh = trimesh.Trimesh(vertices=verts, faces=sphere.faces, process=False)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    mesh.export(str(out_path), file_type="stl")
    logger.info("Asteroid R=%.3f: wrote %s", radius, out_path)


def main() -> None:
    """Parse arguments and write the ellipsoid STLs."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--asteroids", type=int, nargs="+", default=sorted(RADII))
    parser.add_argument("--output-dir", type=Path, default=OUTPUT_DIR)
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format="%(message)s")
    args.output_dir.mkdir(parents=True, exist_ok=True)
    for asteroid_id in args.asteroids:
        ellipsoid_stl(RADII[asteroid_id], args.output_dir / f"asteroid_{asteroid_id:02d}.stl")


if __name__ == "__main__":
    main()
