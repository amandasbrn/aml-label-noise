"""Noise-aware objectives.

Keep probability inputs and logit inputs clearly distinguished.
"""

from typing import Any


def forward_correction_loss(
    logits: Any,
    noisy_targets: Any,
    transition: Any,
    epsilon: float,
) -> Any:
    """Compute forward-correction loss without changing transition.

    Stage 5 flow:
    logits -> clean probabilities p -> q = p @ T -> select q[b, s[b]]
    -> protected negative logarithm -> batch mean.
    """
    raise NotImplementedError("Complete Stage 5: forward correction")


def reweighted_loss(
    logits: Any,
    noisy_targets: Any,
    transition: Any,
    epsilon: float,
    *,
    detach_weights: bool,
) -> Any:
    """Compute the paper-specific reweighted objective.

    Stage 8 flow:
    logits -> p -> q = p @ T -> w = p[b, s[b]] / q[b, s[b]]
    -> per-example CE(logits, s) -> mean(w * CE).

    Confirm gradient handling against the paper/reference before deciding the
    detach_weights setting. Document any clipping as an adaptation.
    """
    raise NotImplementedError("Complete Stage 8: reweighted objective")
