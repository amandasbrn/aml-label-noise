"""Final clean-test evaluation kept separate from model selection."""

from typing import Any


def clean_test_accuracy(model: Any, test_loader: Any, device: Any) -> float:
    """Return top-1 accuracy from argmax(p) against clean Yts.

    This function must not train, tune, select checkpoints, or apply T to the
    predictions.
    """
    raise NotImplementedError("Complete Stage 11: clean-test evaluation")
