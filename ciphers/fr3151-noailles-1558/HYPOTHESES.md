# fr3151-noailles-1558 -- hypotheses, controls and data conflicts (append-only)

Opened 2 Oct 2026 (LIKELY-5, account-4). Rule 3: every target number sits beside its matched control; a control that
cannot separate a known answer from its own shuffle makes the target row a non-test, not a negative.

| date | job | hypothesis / family | instrument | target | control | positive control | verdict |
|---|---|---|---|---|---|---|---|
| 26 Sept 2026 | NX-3151G | the margin gloss is a letter-level decipherment alignable line-to-line to block 1 | tools/interlinear_align.py, leave-one-line-out, align/control_3151.py | 0.000 (33 qualifying) | shuffled-pairing 10 perms, all 0.000 | none run | tied with shuffle; CONTROL BELOW GATE, not the brief's leave-one-block-out design |
| 2 Oct 2026 | LIKELY-5 | the surviving margin gloss (all three blocks) aligns to its block by DP/hard-EM well enough to yield a key | tools/interlinear_align.py, one (gloss, block) pair per block, align/likely5_align.py | consistency b1 0.500 (n_cons 2), b2 0.435 (0), b3 0.455 / 0.583 (4 / 4, two gloss witnesses) | shuffled-gloss 200 perms p95 b1 0.655, b2 0.609, b3 0.625; shuffled-lines p95 0.538 / 0.500 / 0.574-0.578 | synthetic French, same sign counts, correct gloss cut to the real coverage: 0/5 (block-1 shape) and 0/5 (block-3 shape) clear their own shuffled-gloss p95 | **non-test**: untestable by this method at this gloss coverage (about 0.4 letters/sign) and N (83-158 signs); not refuted; needs new material (gutter-lost gloss text, or a person-settled sign alphabet) before a third attempt |

## Data conflicts

- Gloss 1 line 3, last word: "affaires" (Bourdeau, guiche1551/NOTES.md citation) vs "iustice" (NX-3151G subagent and
  worker, 26 Sept; this worker, 2 Oct, who also floats "duction"). Unresolved, grade M; the image on disk (Gallica scan)
  cannot settle it.
- Gloss 3, whole text: two M-grade witnesses of the same crop disagree on most words (NX-3151G subagent: "a mre a
  chiffre auec le Sr Chef a prou prest a me chascune chose ..."; LIKELY-5 worker: "Mais ie me doubte que le Sr Che a
  sur a prou fait ..."); agree on "le S..r Che" and "a prou". Both were run as separate rows above; neither is a text.
