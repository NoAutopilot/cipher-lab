# PREREG R9-FLOR (6 Oct 2026, written before any segment run of this job)

Question: can `tools/glyph_atlas.py segment` thresholds be tuned (script only, no vision) so its box count per
c.127 cipher line tracks the sign count closely enough for sorter tiles on L02-L18 (images/c127b2)?

Reference: passes/c127b1_recon.tsv (reconciled two-pass read of pilot crops images/c127/c127b1_L0x_sN), cipher
tokens per crop = tokens not starting with '=' (clear text). Clear-text tokens of the same crop are subtracted
from nothing: crops with >2 clear tokens (L02_s2, L04_s2) are reported but excluded from the gate.
Tuning set: L01_s1, L01_s2, L02_s1. Held-out set: L04_s1, L03_s2 (L03_s2 only 8 cipher tokens; reported).
Metric: per crop, box ratio = boxes / cipher tokens.
Gate (held-out, fixed parameter set chosen on the tuning set only): every held-out crop's ratio in [0.85, 1.15].
Control: the same tuned parameters on the default run of the same crops are reported side by side (default
parameters' ratio); and a ratio-only gate cannot see merge+split errors that cancel, so the share of boxes whose
width exceeds 1.8x the median box width (merge suspects) is reported too -- reported, not gated.
Outcome words: PASS -> "atlas boxes usable as sorter tile candidates for L02-L18, by count"; FAIL -> "not usable at
these settings", logged as a tuning attempt (rule 3 third-attempt clause counts it as attempt 2 after GAPS106).
