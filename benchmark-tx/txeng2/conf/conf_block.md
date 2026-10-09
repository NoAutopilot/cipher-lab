## Additional block for this pass (calibrated confidence)

For EVERY sign row, also give your three most likely cells with probabilities that sum to 1. Use one extra column,
placed between `conf` and `note`:

    passage	pos	sign_id	alt	conf	top3	note

- `top3`: three candidates as `CELL:p` separated by commas, most likely first, e.g. `T50:0.70,T92:0.25,T18:0.05`.
  A candidate may be a cell `T##`, one of the off-sheet labels (`X_K`, `X_A`, `X_EQ`, `X_S`, `X_NEW`) or `?`.
  The three probabilities sum to 1 (they are your honest chances that each candidate is the right cell, given only the
  crop and the sheet; put a small value on the third rather than 0 unless you truly see no third candidate, in which case
  give it 0.00). The first candidate is always the same as `sign_id`.
- Be calibrated: a probability of 0.9 should be right about nine times in ten. Do not give every sign 0.98.

Everything else in the brief is unchanged.
