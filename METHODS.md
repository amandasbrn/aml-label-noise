# Methods notebook

Use this file to explain implementation decisions in your own words as you make
them. Do not wait until report writing.

## Matrix convention

TODO: Explain why rows are clean classes, columns are noisy labels, and why the
row-vector implementation uses `q = p @ T`.

## Forward correction

TODO: Write the equation, describe numerical protection, and identify which
parameters receive gradients.

## Anchor estimator

TODO: Explain the approximate-anchor assumption and why the estimate is not a
guaranteed recovery of the true matrix.

## Reweighted objective

TODO: Map every part of Equation (3) to a named intermediate quantity. Record
the confirmed gradient handling and any adaptation such as clipping.

## T-Revision

TODO: Explain initialization, the chosen constraint method, and how model and
matrix checkpoints stay matched.

## Validation and test separation

TODO: Explain why noisy validation uses `q`, while final clean testing uses `p`.

## Reproducibility and compute

TODO: Record seeds, versions, device, stopping rules, stage budgets, and known
sources of nondeterminism.
