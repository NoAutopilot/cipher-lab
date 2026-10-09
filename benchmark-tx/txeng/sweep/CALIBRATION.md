# TXE-I calibration (truth-blind; 9 Oct 2026, before any truth file was opened)

Defaults step 0.06 / min_area 6 flagged 54.4% of f178v's 675 boxes, far above the registered gate's 20% ceiling. Rule fixed
before the gate: over step_frac {0.06, 0.04, 0.03, 0.02} x min_area {12, 20, 30, 45, 60}, take the setting whose f178v
page flag share is <= 20% and closest to it. Shares (f178v, read-free, no truth):

| step \ min_area | 12 | 20 | 30 | 45 | 60 |
|---|---|---|---|---|---|
| 0.06 | 48.1 | 41.9 | 35.6 | 32.3 | 30.5 |
| 0.04 | 34.7 | 28.9 | 24.7 | 21.6 | 20.3 |
| 0.03 | 25.9 | **20.0** | 16.9 | 14.8 | 14.7 |
| 0.02 | 18.1 | 13.2 | 10.4 | 9.3 | 9.6 |

Chosen: step 0.03, min_area 20 (now the tool defaults). f178v 135/675 flagged (20.0%), f179r 33/144 (22.9%).
