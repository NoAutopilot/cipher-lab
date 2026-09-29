# L02 opening mark -- eye pack for the verifier (H313, 29 Sept 2026, runner 12)

One question: is the mark that opens f.61r line L02 (before PHI and the II-shaped OTHER) the LL cipher sign, as read_call_U pass 1 coded it, or a
clear handwritten 'Il', as pass 2 read it (the decode, `family/f61_decode_period_v4_frac0.1_sbs.tsv`, follows pass 2)?

`L02_mark_pack.jpg` (regenerate: `python3 family/h313_eye_pack.py SCRATCH`, needs the f.211r native in SCRATCH): row 1 the two targets (f.61's LL at
L05 16, and the L02 mark), row 2 f.61's clear 'Il' x2 and 'ella', row 3 two doubled l's from fr.3983 f.211r (a clear page from Mayenne's chancery).

What the runners' instruments said (all descriptive; none is a reading):
- H302, H304 (blind free sorts): both put the L02 mark alone with LL, apart from the clear 'Il', the single l's and PHI/C43 -- but both missed their
  own control gate (CONTROL FAIL).
- H309 (free sort): NON-TEST (every l, single or doubled, in one group); the free sort is retired for LL (HYPOTHESES.md, untested-by-this-tool).
- H310 (forced choice ONE/TWO/NEITHER, known answers 14/14): LL = TWO and the L02 mark = TWO -- which cannot tell ll from 'Il'.
- H311 (forced choice capital-I lead-in vs upright l, known answers 7/7 + 4/4): unclear on both.
If the verifier reads the mark as LL, the null band's LL row counts 2 (a recount for the verifier; `family/f61_null_band.tsv` note row `L02 0 LL?`).
