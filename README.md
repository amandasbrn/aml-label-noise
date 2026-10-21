# AML label-noise assignment

This repository is being built in small learning stages. The files contain
interfaces and TODOs, but the assignment algorithms are intentionally left for
the student to implement.

## Learning order

1. Inspect and load the three supplied `.npz` datasets.
2. Create reproducible paired train/validation splits.
3. Build a small three-output CNN.
4. Validate the transition-matrix convention.
5. Implement and test forward correction.
6. Train a noisy-label pilot and estimate `T0`.
7. Implement and test the reweighted objective.
8. Add the CIFAR transition-revision stage.
9. Add checkpointing and clean-test evaluation.
10. Run smoke experiments, then the paired ten-split experiment.
11. Summarize real results and prepare report material.

## Intended commands

These commands describe the final interface. They will not work until the
corresponding TODOs have been completed.

```bash
python -m algorithm.run_experiments --data-dir data --method forward --runs 1 --smoke --device auto
python -m algorithm.run_experiments --data-dir data --method reweight --runs 1 --smoke --device auto
python -m algorithm.run_experiments --data-dir data --method both --runs 10 --device auto
python -m algorithm.summarize --results-dir results
```

Do not commit assignment datasets or generated experiment outputs.
