# PREREG DA1-COLV (verifier, account 1, LANE DEFAULT-account-1-20261007-1440, 7 Oct 2026, written ~16:2x UTC before the check below is run)

Verifier check of the eight key_f23 codes moved to C today (DA1-COL: 16 se, 20 i, 67 leur, 81 me, 96 que; DA1-COL3: 30 s, 85 na;
46 ce already lowered to M by DA1-COL2). Demotion only: nothing is raised by this check.

Concern: every value tested today came from key_f23_anchor_r10.tsv, which R10-COL26B chose by span containment on 14 units; the
word-grain tests scored those codes on canvases that include the units the value was chosen from (DA1-COL3's PREREG caveat 7).

Script: siblings/verify_colv.py (pushed with this file, before it is run). It reuses word_da1.py's statistic, hit rule, Control W
(within-canvas permutation of gloss words over word spans, 10000 draws, seed 20261007 + 1440) and instrument check unchanged, on the
canvases already paired today (c3940, c47, c50 from DA1-COL's pass; c54, c55, c56, c62, c63 from DA1-COL3's pass), and splits each
code's occurrences into IN (canvases listed in that code's key_f23_anchor_r10 `units=`) and OUT (the others). Only canvases that clear
the instrument check are scored. DA1-COL2's second pass is reported beside DA1-COL's for c3940/c47/c50 (not pooled).

Decision rule per code (registered now):
(a) Conflict: if f.23's own interlinear gloss pairs the code with a different word or value (key_f23 note / interlinear/f23w_align.tsv),
    the code is a two-witness data conflict (rule 4) and goes to M whatever its sibling score -- the 31 = t precedent.
(b) Value independence: on OUT canvases only, H > p95 and P < 0.05/7 = 0.00714 (seven codes at C) keeps C. If OUT has fewer than
    3 occurrences, or fails, the code's C rests on in-sample canvases only: it goes to M with a NOTES line (lead, not refuted).
Also reported, not gated: per-canvas hits, and k = 1 spans where the code alone covers a word not containing its value.
