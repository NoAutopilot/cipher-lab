# R2-2 T-LOW result (DEB-SWARM2-R2-2, 29 Sept 2026)

**Stopped at the known-answer control, as pre-registered: the protocol reads the synthetic page at 15.6 pct error,
above the 5 pct kill line. With this reading protocol, the public images are the limit, and that is the result.**
Steps 5-6 (the real re-reads of the 156 disputed and 90 audit boxes) were not run. Nothing in this folder is a reading.

## Steps 1-3

- **Resolution.** No public copy larger than the Schmeh/Cipherbrain PNGs was found. Wikimedia Commons carries the same
  file (identical sha1 for cryptogram 1). The Cipher Foundation's six full-size PNGs are the same set under new names,
  at identical dimensions. The printed figures (Bauer 2017, Farnsworth 2010) and the museum's own web images are not
  reachable from here. Details are in LOG.md row 1.
- **Sign-or-mark rule** (RULE.md): DASH-V is the scan's page edge; BLOB and BAR-SOLID are dots; HOOK-L is a comma.
  All four fold with `_`. BAR-THIN and DASH-H count as signs when they stand free.
- **Folds declared:** PCT+PCT-SLASH, X+X-DOT, X+X-CURL.

## Known-answer control (PREREG.md)

The synthetic page has 96 targets (12 lines x 8), rendered from native box pixels of the public PNGs. Truth for each
target is a box that passes A and B agreed on and that is not an exemplar on the reference sheet. The ids are drawn
from the class mix of the disputed boxes (25 ids). Two fresh value-blind readers (R1 Sonnet, R2 Opus) read one line
at a time against the inventory tiles (`t_low.py`, `reader_prompt.txt`, `control/`).

| scoring | R1 errors | R2 errors | R1 != R2 (unsettled) | agreed but != truth | control error |
|---|---|---|---|---|---|
| unfolded | 13/96 | 9/96 | 13 | 4 | **17.7 pct** |
| folds only | 11 | 7 | 13 | 2 | **15.6 pct** |
| folds + rule | 11 | 7 | 13 | 2 | **15.6 pct** |

Robustness: the two "agreed but != truth" boxes (s03_1 CC-DASH read CC-DOT by both readers; s03_4 X read X-O by both)
may be errors in the truth labels. H51 bounds the hidden error inside A-B agreement at up to ~17 pct. Counting both as
correct still leaves 13 of 96 = **13.5 pct** from reader disagreement alone. The single-reader error is also over 5 pct
(R1 11.5, R2 7.3 pct, folded). The kill holds under every reading of the numbers.

Where the readers split: EIGHT/VENUS/THREE (3), C-BAR-X/ARCH-DASH (3), CIRC-O/BLOB (3, a small closed loop against a
dot), O-SLASH/PHI (2), II-DASH/CC-DASH, S-CURL/DOUBLE-LOOP. These are the same small curved and stroked classes that
DIGEST-1 section 2 names. At these pixel sizes (a sign is about 15-30 px) two strong readers cannot tell them apart
reliably, even on boxes whose truth is known.

## What it means for the swarm

- On public pixels, reading c1+c2 under 5 pct type noise is out of reach for this protocol. The control fails for
  two-reader agreement on the hard classes, before any real box is read. A third or fourth reader on the same pixels
  would add votes but not resolution.
- Ways forward that do not depend on this protocol: (a) the private session's sharper museum scans; the same control
  can be rebuilt on them, privately, and should come first there. (b) Designs that hold at 15-20 pct noise, or the
  folded classes: R2-1's order battery already passes at that noise. (c) Coarser class folds (EIGHT+VENUS+THREE,
  C-BAR-X+ARCH-DASH, CIRC-O+BLOB), declared as design assumptions and reported both ways. R2-6 (conditional on the
  rule) can use RULE.md as written.
- Cost: 8 reader subagents (4 Sonnet, 4 Opus), 3 lines each, 96 crops per reader. Session cost is the orchestrator's
  to read (get_session).
