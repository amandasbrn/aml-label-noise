# Test checklist

Add one small test at a time while implementing each stage.

## Data

- Missing `.npz` keys produce a clear error.
- Labels outside `{0, 1, 2}` are rejected.
- Same seed gives the same split.
- Different run seeds give distinct splits.
- Training and validation indices are disjoint and cover all examples.

## Transition matrix

- Shape is exactly 3 by 3.
- Entries are finite and nonnegative.
- Every row sums to one.
- `[1, 0, 0] @ T` equals row zero of `T`.

## Losses

- Forward correction with identity `T` matches ordinary cross-entropy.
- Reweighting with identity `T` matches ordinary cross-entropy.
- Losses remain finite when `T` contains zeros.
- Known matrices do not receive updates.

## Revision

- The effective matrix begins at `T0`.
- It remains a valid probability matrix after an optimizer step.
- Revision parameters receive finite gradients.

## Checkpoints and leakage

- Reloading a checkpoint reproduces predictions.
- The model and matrix come from the same epoch.
- Training and estimator interfaces never receive `Yts`.
- Smoke outputs are excluded from final aggregates.
