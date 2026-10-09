# PREREG UNA-GRAM (9 Oct 2026, written 05:45 UTC by date -u (header first typed 05:5x, corrected to the commit clock; nothing else changed), before any box is cut or looked at)

Job: UNA-GRAM (`.claude/briefs/runs/2026-10-09-account4-orch-unassigned-jobs.md`). Question: are the 6 fr.3040 no.6 plain `z`
tokens that still align R after DA1-GRA's relabel (OFF in both earlier sorts, or the sorts disagree) the barred z (`zh`, R x39 /
gap x2 pooled) or the plain z (A on f.30, H)? This closes or keeps the plain-z A (f.30) vs R (fr.3040) entry in HYPOTHESES.md.

## Targets (X, 6 tokens, n8gra3/recon.tsv, all z = A under key.tsv, aligned R by n8gra3/score3.py's aligner)
f18vC_L02 29, f18vC_L07 8, f18vC_L10 30, f18vC_L13 26, f18vC_L14 8, f18vC_L14 18. (The 3 other z left as z align A x2, T x1 and
are not in this test.) L07 8 and L13 26 were sorted by R12D-GRAZB2 (C2, not C1); the other 4 were never boxed.

## Unchanged from PREREG-R12D-GRAZB2.md (the instrument, word for word)
- Crop: each token is cut as one tight sign box from the fr.3040 half-line image on disk (`images/fr3040_f18/`), from
  `r12zb2/seg.py` `align()` (ink-column runs, over-wide runs split, the half's n tokens assigned to runs by a dynamic programme
  on the line's mean sign width), padded 3 px, full line height, enlarged to a common height. Token lists per half from
  `r12zb2/halves.tsv`. `unagram/cut.py` is `r12zb2/cut.py` with only the paths changed.
- Eye check before the sort, by this worker (who is not the sorter): an overlay per target showing the box on +-3 signs with
  codes; where the box is plainly on a neighbour, the worker moves it and logs it in `unagram/fixes.tsv`. The worker judges only
  "box on the intended sign position", using the line position and the neighbours' codes, never which class a target "should"
  join. Reference and decoy tiles are re-cut with R12D-GRAZB2's own eye-checked fixes (`r12zb2/fixes.tsv`), unchanged.
- The sorter: ONE Sonnet blind shape-sort call, tile sheets only (numbered, shuffled ids, no source, line, code or value),
  max 8 classes, OFF allowed, the same prompt as R12D-GRAZB2.

## The other tiles (same sets, same boxes as R12D-GRAZB2; ids reshuffled)
- Decoys: fh 6 f.30 + 6 fr.3040, n6 6 f.30 + 6 fr.3040 (r12zb/occ.tsv sets fh, n6, all 24).
- P plain-z references: the 12 r12zb/occ.tsv P tiles (10 f.30 K1 + 2 fr.3040 K1).
- B barred-z references: 12 fr.3040 tiles that R12D-GRAZB2 sorted C1 (T2a/T2b), seeded sample random.Random(20261009).
- Total 6 + 24 + 12 + 12 = 54 tiles; new ids by random.Random(20261009) shuffle; answer sheet `unagram/occ.tsv` kept from the
  sorter.

## Gate (decided in order; all counts over on-target, non-OFF tiles)
- G0: OFF <= 20% of all 54 tiles (the brief's threshold), else UNDECIDED.
- G1 decoy control, word for word from PREREG-R12D-GRAZB.md: for fh and for n6 separately, the plurality class holds >= 75% of
  that decoy's tiles AND >= 60% of each source's (f.30, fr.3040) tiles of that decoy; fh's and n6's plurality classes differ from
  each other and from P's plurality class; each decoy's plurality class holds <= 20% of the z-family tiles (X + P + B).
  Fail -> NON-TEST, no conclusion.
- G2 reference separation (needed because the classes are named by the sorter, not by us): B's plurality class holds >= 60% of B,
  P's plurality class holds >= 60% of P, the two differ, and neither is a decoy plurality class. Fail -> NON-TEST.
- Per target (only if G0, G1, G2 pass): in B's plurality class -> **barred** (relabel `zh`); in P's plurality class -> **plain**
  (stays `z`; an R-aligned plain z, kept as a listed conflict); OFF or any other class -> **unclassed** (stays `z`, listed).

## Consequences
- key.tsv is unchanged under every outcome (it changes only by its own registered open-code rule; `zh` is not keyed).
- `relabel_zh.py`'s rule is extended by one clause, written into its docstring before any re-score: a fr.3040 `z` -> `zh` if
  UNA-GRAM's sort put it in B's plurality class. Then `relabel_zh.py --check`, and a re-score of n8gra3 with the registered
  `n8gra3/score3.py` (pasted beside 0.889 on 696) and the zh open-code listing.
- All 6 barred -> the plain-z A-vs-R entry is closed: no fr.3040 plain z placed by shape reads R. Any plain -> the entry stays
  open with those tokens named. Unclassed -> stays open, a person's sign-sorter look named as next.
- If G1 or G2 fails: logged NON-TEST; this is the third run of this sort instrument in this folder (R12D-GRAZB, -GRAZB2, UNA-GRAM),
  so a failure retires it for this question (rule 3) and names the owner's sign sorter as the next instrument.
