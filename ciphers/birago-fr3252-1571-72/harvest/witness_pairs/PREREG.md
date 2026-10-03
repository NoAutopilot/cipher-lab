# CEPPO-WITNESS-PAIRS pre-registration (3 Oct 2026, 01:05 UTC; account 2 for the account-3 orchestrator)

Written and pushed BEFORE any f.47r or f.87 pair tile was opened in this job. Brief:
`.claude/briefs/runs/2026-10-03-acct3-ceppo-witness-pairs.md`.

## Source of the rules
fr.3252 f.36v top block (`../../../ceppo-nevers-fr3251-1570s/harvest/witness_f36/c38_f36v_top.jpg`, native Gallica region,
HARVEST-D), cut at 2.5x (`T_*` regions, x 1000-3480, y 120-900) and 3x (`cut3.py`), autocontrast. Gloss letters read by this
worker's own eye, grade M (no second reader). Only glossed (or visibly unglossed) occurrences are used. Evidence crops kept:
`w36v_*.jpg` in this folder. f.36r and f.37r not scanned (cap).

## Witness tallies (sign shape -> gloss letter)
| family | shape on the witness | gloss read | n | sheet id / printed value |
|---|---|---|---|---|
| 8 | 8 with a horizontal bar through the waist running out past both sides | a | 6 (L2, L3, L3 x2, L4, L5) | S80 a |
| 8 | plain 8, no bar | an &-like mark (et), faint | 1 (L3, x~2290) | S65 et |
| hash | stem SLANTED (/) crossing two horizontals | t | 2 (L2 x~1100, L3 x~1080) | S88 t |
| hash | stem UPRIGHT (vertical) crossing two horizontals, often a dot above | o | 4 (L2, L3, L2b, L4) | S24 o |
| 6 | 6 whose top carries a flat crossbar across the stem (б) | no gloss letter above it | 2 (L1 x~2895, L5 x~1870) | S54 null |
| 6 | 6 with a teardrop/blob top, no crossbar | gloss not legible (under upper-line ink or faint), never blank | 4 | (S74 m by elimination) |
| curly-c+y (S76/S91), loop-tail (S31), S32 | -- | no legible gloss found in the area scanned | 0 | no rule |

## Pre-registered rules (applied to f.47r and f.87 tiles by eye, value-blind to the decode)
- R-8: bar through the 8 extending past both sides -> S80 (a); no bar -> S65 (et). Strongest rule (6 vs 1).
- R-hash: slanted stem -> S88 (t); upright stem -> S24 (o). (2 vs 4.)
- R-6: crossbar on top of the 6 -> S54 (null); blob/teardrop top without crossbar -> S74 (m). The null side rests on two
  UNGLOSSED instances (a null carries no gloss), the m side on elimination only (no "m" gloss read): weaker than R-8.
- S76/S91 and S31/S32/S76: NO rule; tiles of these pairs are left as they are and counted as untested.
- A tile whose deciding feature (bar / stem angle / crossbar) cannot be seen is scored UNDECIDED, not forced.

## Measurement
For each pair tile on f.47r (`la/f47_split_tiles.tsv` rows whose readers split inside one family) and f.87
(`../../ceppo-nevers-fr3251-1570s/sorter/focus.tsv`): rule label vs the current label (f.47 passD third-reader label;
f.87 adjudicated passC label). Control: the same comparison with the current labels shuffled among the pair tiles of that
family (1000 shuffles); agreement real vs shuffle mean / p95. A rule that agrees with the current labels no better than
shuffle means the current labels are not following this shape.
Gate for any regrade: a token moves to S only if (i) the rule settles it, (ii) the re-decode's key control at the letter's
TWO-READER error (f.47 0.33, f.87 its own) still ranks 1/201 with power >= 18/20, (iii) the judge does not get worse.
