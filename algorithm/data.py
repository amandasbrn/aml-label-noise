"""Dataset inspection, preprocessing, splitting, and loader construction.

Work on this file first. Keep clean test labels out of every training-facing
interface.
"""

from pathlib import Path
from typing import Any
import numpy as np


REQUIRED_KEYS = ("Xtr", "Str", "Xts", "Yts")


def inspect_npz(path: Path) -> dict[str, Any]:
    """Return a factual summary without changing the stored arrays.

    Stage 2 algorithm:
    1. Open the file.
    2. Check the four required keys.
    3. Record shape, dtype, minimum, and maximum for each array.
    4. Check that label values belong to {0, 1, 2}.
    5. Do not normalize or split anything here.
    """
    raise NotImplementedError("Complete Stage 2: dataset inspection")


def load_dataset(path: Path) -> tuple[Any, Any, Any, Any]:
    """Load Xtr, Str, Xts, and Yts after validating the file.

    Decide and document whether this function returns NumPy arrays or tensors.
    It must preserve the supplied noisy training labels.
    """
    raise NotImplementedError("Complete Stage 2: dataset loading")


def make_split_indices(
    sample_count: int,
    seed: int,
    train_fraction: float = 0.8,
) -> tuple[Any, Any]:
    """Return disjoint, reproducible training and validation indices.

    Stage 3 algorithm:
    1. Build indices from 0 to sample_count - 1.
    2. Shuffle them with a generator controlled by seed.
    3. Assign train_fraction to training and the rest to validation.
    4. Verify disjointness and full coverage.
    """
    raise NotImplementedError("Complete Stage 3: paired split indices")


def prepare_images(images: Any, *, is_color: bool) -> Any:
    """Convert images to the shape and numeric scale expected by the CNN.

    Inspect the pixel range before choosing any scaling. If statistics are
    learned, calculate them later from the training split only.
    """
    raise NotImplementedError("Complete Stage 3: image preparation")


def make_loaders(*args: Any, **kwargs: Any) -> Any:
    """Construct portable train and validation data loaders.

    Keep split indices explicit. Start with num_workers=0 and seeded shuffling.
    Design this only after inspection, splitting, and preprocessing work.
    """
    raise NotImplementedError("Complete Stage 3: data loaders")
