"""Small CNN backbones shared fairly by the compared methods."""

from typing import Any


class SmallCNN:
    """Placeholder for a modest CNN with exactly three output logits.

    Stage 4 decisions for the student:
    - Accept one input channel for Fashion and three for CIFAR.
    - Keep the model manageable on CPU/MPS.
    - Return raw logits, not probabilities.
    - Use the same backbone for both methods within a dataset.

    Replace this placeholder with the framework-specific model base class when
    implementing the stage.
    """

    def __init__(self, input_channels: int, class_count: int = 3) -> None:
        raise NotImplementedError("Complete Stage 4: CNN construction")

    def forward(self, images: Any) -> Any:
        """Map a batch of images to shape [batch_size, 3]."""
        raise NotImplementedError("Complete Stage 4: CNN forward pass")
