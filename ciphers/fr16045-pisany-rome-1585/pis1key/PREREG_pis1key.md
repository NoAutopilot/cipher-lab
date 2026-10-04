# PREREG pis1key (LANE-PIS1 PIS1-KEY, 4 Oct 2026; written and pushed before any score of either part)

Brief: .claude/briefs/runs/2026-10-04-acct1-pis1-wave1.md "PIS1-KEY". Disk only, no network, no subagents. Scripts reused
UNCHANGED by import (kp86/kp86.py test/norm/dec/p99/load_key, kp86d/kp86d.py load_tokens/control); wrapper pis1key/pis1key.py.
Seeds as the originals (rnd 20261004 per arm/page, control seeds 500+s); nulls 1000/1000 on targets, 200/200 x 5 seeds in controls.

## (a) T31 shape relabel (HYPOTHESES.md "T31 image compare", images/t31_compare.jpg)
- f.244r: every T31 token in tx86/ciphertext_f244r.tsv, tx86/passA.tsv, tx86/passB.tsv -> T45 (the loop form's table cell).
- f.275r: every T31 token in tx86e/ciphertext_f275r.tsv, passA, passB -> T36 (the x+o cell).
  Descriptive variant only (not gating): on f.275r a T31 immediately followed by T30 becomes one T36 (the readers' cut).
- f.244v/f.245r (5 T31 tokens) and f.301v (5): no image evidence; not relabelled.
- Relabelled copies go to pis1key/tx_relabel/ ; the committed transcriptions are NOT changed.
- Runs: f.244r = kp86.py's test (the f.244r test of the 17 Sept family; kp86b tests f.244v/f.245r, which carry no relabel),
  --err 0.284 as RUN3-PISA; f.275r = kp86e arm A (kp86d.py arm-A loop, same file order and seeds), --err 0.215. Positive
  control re-run with the same key (unchanged key86) -- it does not depend on the relabel, reported for completeness.
- Report old vs new nw_score and both p99s for reconciled + both blind passes, and how many relabelled tokens would align
  identically to the copy (descriptive).
- Reading of the result: the relabel is a transcription hypothesis checked by eye on 4 of 11 (f.244r) and 2 of 13 (f.275r)
  tokens. It is SUPPORTED if, on both pages, the reconciled score rises and stays above both p99s. Even then key86.tsv
  is unchanged (T31 = m stays as published), the committed transcriptions are unchanged, and the T31 tokens stay M:
  a token-level relabel needs each token's own crop checked (the step named in Remaining gaps), not this aggregate.

## (b) Held-out remap T45/T47/T49/T57
- Fit pages ONLY (17 Sept 1586): tx86/ciphertext_f244r.tsv vs kp86/colbert_p49_50.txt; tx86c/ciphertext_f244v_f245r.tsv vs
  kp86b/colbert_p51_52.txt (reconciled, unrelabelled transcriptions; T31 stays key86 m).
- Fit: start at key86 (arm A). Candidates per cell: the 21 single letters key86 uses (a b c d e f g h i l m n o p q r s t u
  x y) plus the cell's own key86 value. Objective F = sum of nw_score over the two fit pages. Coordinate ascent in the order
  T45, T47, T49, T57, repeated until a full round changes nothing (max 5 rounds); ties keep the current value. A cell whose
  fitted value equals key86's is not part of the remap.
- Held-out pages: f.275r (tx86e/ciphertext_f275r.tsv vs kp86d/colbert_p121_123.txt) and f.301v (tx87/ciphertext_f301v.tsv vs
  kp87a/colbert_p338_339.txt). Arm A scores: 0.6471 and 0.6302 (committed results; recomputed here).
- GATE (all on both held-out pages, reconciled files):
  G1 remap score > arm A score;
  G2 remap score > key-shuffle p99 and > order p99 (1000/1000, nulls built with the remap key);
  G3 remap score > the DEGENERATE remap's score, where the degenerate remap sends every disputed cell (T45, T47, T49, T57)
     to e (the most frequent clear letter: it can gain on nw_score by frequency alone). If the fitted remap is itself
     all-e, or the degenerate remap also clears G1, the gain is not attributed to the cells' true values.
  G4 positive control (kp86d.control, unchanged) with the remap key at the page's measured err (0.215 / 0.192) passes >= 4/5.
- Per cell: a cell enters key86.tsv only if G1-G4 pass for the joint remap AND that cell alone changed from arm A scores
  > arm A on both held-out pages. Such a change is labelled in key86.tsv's note/source as a label-level value for these
  readers' transcription convention (RUN4-PIS1 cellcheck_a.md: the table cut is right; the readers put a page form on the
  wrong sheet cell), not a correction of Tomokiyo's table. Otherwise key86.tsv is unchanged and the numbers go to
  pis1key/key86_proposals.tsv.
- Descriptive (not gating): held-out score gain of the previously used arm B (RUN4-PIS1 REMAP_B without T31) and of 200
  random remaps of the same four cells (values uniform over the candidate set).
- If key86.tsv changes: regrade with kp86e/t31_grades.py --grade and kp87a/cgrades87.py, regenerate readings, --check each.
