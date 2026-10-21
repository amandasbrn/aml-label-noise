"""Aggregate completed non-smoke runs into report-ready summaries."""

from typing import Any


def summarize_results(results_dir: Any) -> Any:
    """Compute per-run pairs and six dataset-method mean/sample-SD rows."""
    raise NotImplementedError("Complete Stage 15: result aggregation")


def main() -> None:
    """Load result files, validate completeness, and write tables/figures."""
    raise NotImplementedError("Complete Stage 15: summary CLI")


if __name__ == "__main__":
    main()
