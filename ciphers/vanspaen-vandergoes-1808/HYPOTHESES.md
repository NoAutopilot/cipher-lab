# vanspaen-vandergoes-1808 -- hypothesis families (append-only)

Opened 3 Oct 2026 (GAPS48, account-4). One row per run, control and target side by side (rule 3).

| date | run | hypothesis | statistic | matched control (N 304, values 15-1339) | control result vs gate | target result | verdict |
|---|---|---|---|---|---|---|---|
| 3 Oct 2026 | GAPS48 `gaps48/crib_place.py` (prereg `gaps48/PREREG.md`, d0e47f7f) | one-part code: value order tracks alphabetical order; GAPS44 cribs (12, FR and NL forms) present in No 4 + No 6 | S1 = AUC of crib vs 300 decoys on distance from predicted value to nearest group | synthetic one-part code from the other half of fr1810 / nl18, 20 seeds; two-part (random order) control must sit near 0.5 | one-part S1 0.638 FR / 0.636 NL (K 89 / 72) vs gate 0.75: CONTROL BELOW GATE. Two-part 0.496 / 0.509 (G0 ok). Post-hoc K-matched (`--kmatch`, K 163 / 184): one-part 0.745 / 0.690, two-part 0.460 / 0.433, still below gate | S1 0.401 FR, 0.466 NL (S2 0.509 / 0.487), at or below the two-part null mean | NON-TEST: untestable by crib placement at N 304 (not a negative). The target number would not have passed even with the gate met (FR p95 null 0.575, NL 0.611) |
