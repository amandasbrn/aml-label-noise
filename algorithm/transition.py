"""Transition-matrix validation, estimation, and revision.

Convention: T[i, j] = P(observed label j | true label i), so q = p @ T.
"""

from typing import Any


FASHION_03 = (
    (0.7, 0.3, 0.0),
    (0.0, 0.7, 0.3),
    (0.3, 0.0, 0.7),
)

FASHION_06 = (
    (0.4, 0.3, 0.3),
    (0.3, 0.4, 0.3),
    (0.3, 0.3, 0.4),
)


def validate_transition(transition: Any, tolerance: float = 1e-6) -> None:
    """Check shape [3, 3], finite nonnegative values, and row sums of one."""
    raise NotImplementedError("Complete Stage 1: matrix validation")


def estimate_anchor_transition(
    pilot_model: Any,
    training_loader: Any,
    device: Any,
) -> Any:
    """Estimate T0 using one approximate anchor per class.

    Stage 7 flow:
    1. Get the pilot's noisy-class probability vector for each training image.
    2. For each class i, find the image maximizing probability i.
    3. Copy that image's full probability vector into row i of T0.
    4. Validate and return T0.
    """
    raise NotImplementedError("Complete Stage 7: anchor estimator")


class TransitionRevision:
    """Placeholder for a learnable revision initialized exactly at T0.

    The student must choose and document a constraint method that keeps the
    effective matrix nonnegative with rows summing to one. Compare that choice
    with the reference implementation before coding it.
    """

    def __init__(self, initial_transition: Any) -> None:
        raise NotImplementedError("Complete Stage 9: revision parameters")

    def effective_transition(self) -> Any:
        """Return the currently constrained transition matrix."""
        raise NotImplementedError("Complete Stage 9: matrix constraint")
