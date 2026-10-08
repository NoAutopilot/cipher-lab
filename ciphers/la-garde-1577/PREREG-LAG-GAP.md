# PREREG-LAG-GAP: score-gap gate for the homophonic/masc decode at N=229 (8 Oct 2026, account 2, LANE FAMILY-A2c)

Written and pushed before any score below is computed (the one score already on file, the target's -572.867 from LAG-HOM /
A2-LAG3, is the reason for the job and is re-derived, not chosen). CPU only. Script: `families/lag_gap.py` (rule 7 `--check`).

**Instrument.** The homophonic solver's own best score (`families.load("homophonic").solve`, restarts 8, the LAG-HOM call), on
texts of the same N=229, K=26 base-code layout (`families/basecode_cipher.txt`, 15 messages), corpora from
`specs/la-garde-1577.json`. Every text gets exactly one solve (restarts 8); no text gets extra solver seeds.

- **T** = the target, solver seed 1, train = full spec corpora (exactly the family_run.py target call).
- **(a) controls** = `make_control(seed s)` + `solve(seed s)` with `profile=target`, noise 0.055 and 0.084, s = 1..20 each
  (40 decodes, the family_run.py control call). Recovery is recorded beside each score.
- **(b) shuffled targets** = the target tokens permuted by `random.Random(k).shuffle` and redistributed into the original
  message lengths (the family_run.py `--shuffle-target k` convention), solver seed k, k = 1..40.
- p95 of a set of n scores = the ceil(0.95 n)-th smallest. p05 = the ceil(0.05 n)-th smallest.

**Gate (target).** PASS iff T > p95(b) AND T >= p05(a pooled, 40). (A T above the top of (a) still counts as "within the
range"; only the lower bound binds.) Otherwise FAIL.

**Power check (must pass before a FAIL is read as a negative).** Held-out controls, noise 0.055, seeds 101..110 (not in (a)).
For each, its own shuffled null: the control ciphertext permuted the same way, shuffle seeds 1..20, solver seed = shuffle seed.
A control passes if its score > p95(its own 20 shuffles) AND >= p05(a pooled). Power PASS iff at least 80% of the held-out
controls with recovery >= 0.60 pass (the recovery the family_run gate accepts). Held-out controls with recovery < 0.60 are
reported, not counted.

**Read-out, fixed now.**
- Power PASS, target PASS -> score-gap PASS for homophonic (and masc, which shares the decode byte-for-byte): to the lane for a
  separate verifier. It is a design-level signal, not a reading; grades stay 0 H/C/S until a decode is read.
- Power PASS, target FAIL -> control-backed negative for `homophonic` (and `masc`) at N=229 at the measured error 0.055/0.084
  (rule 3), logged so in HYPOTHESES.md.
- Power FAIL -> untestable by this statistic at this N ("untested-by-this-tool"), not a negative.

**Descriptive only (not gates):** false-positive rate of the gate on the shuffled targets (each (b) member against p95 of the
other 39); T's percentile in (a) and (b); per-noise (a) ranges.
