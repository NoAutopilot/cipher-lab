# PREREG VIV-MSORT (20 Oct 2026, 01:5x UTC, worker VIV-MSORT, account 4)

Brief: .claude/briefs/runs/2026-10-20-acct4-research-director-28.md "## JOB VIV-MSORT"; RESEARCH.md 6d instrument (2). Written and
pushed before any clustering or scoring run.

## Material
The 36 ink-40 tiles the owner's blind sorter shows (tx/ksplit/sorter/signs.tsv ids; images tx/ksplit/tiles/<id>.png). Trays as the
sorter shows them: tray A = label c (15 tiles), tray B = label 2 (21 tiles). Truth (tx/ksplit/truth.tsv clerk_letter) is read only by
the scoring step, after tx/ksplit/msort_frozen.tsv is written and committed.

## Features (image only; no labels, truth, key values or positions)
Per tile: grayscale, inverted; Otsu threshold (numpy); crop to the ink bounding box; paste centred, aspect kept, into a 32x32 canvas;
3x3 box blur; flatten; mean-centre and L2-normalise. Nothing else.

## Sort
Average-linkage agglomerative clustering on cosine distance (numpy, deterministic, ties broken by lower index), cut at k=2.
Run (A) within tray A (15 tiles) -- the primary; (B) within tray B (21 tiles); (P) over all 36 tiles ignoring trays.
Assignments frozen to tx/ksplit/msort_frozen.tsv and committed before the score step runs.

## Statistic and gate
Primary (A): adjusted Rand index (ARI) of the k=2 sort vs truth classes {p} vs {e, q}; purity reported beside it.
Nulls, 20 draws each, seeded 'VIV-MSORT-<null>-<i>': (n1) truth labels shuffled among the 15 tray-A tiles, scored against the frozen
sort; (n2) random Gaussian feature vectors of the same dimension through the same clustering, scored against real truth.
p95 = the 19th of 20 sorted draws. Gate: real ARI > p95 of n1 AND > p95 of n2.
Both nulls can differ from the target on this statistic (n1 moves the truth, n2 moves the clustering), so neither is a non-test by
construction.
(B): tray B is all m in truth -- one class, ARI undefined: reported "not machine-testable at this material" (as PREREG-VIV-KSPLIT).
(P) positive control: the 36-tile sort's ARI vs the tiles.tsv label (c vs 2; the machine's own label, not truth), same two nulls.
Power at the target's N (CLAUDE.md rule 3, ARM3-ADJ): 20 draws of 15 tiles from the 36 with the target's class shape (12 of one label,
3 of the other; draws both ways round), each clustered k=2 and gated as above; the share of draws passing is the power figure.

## Decision
- (P) fails its gate, or the subsampled power is under 50%: the tray-A result is a non-test at this N/feature set, logged
  "untestable by this instrument at N=15", whatever it reads; not a negative on the split.
- (P) passes, power >= 50%, (A) passes: label c splits by shape into p vs e/q -- a machine lead (grade M), to be compared with the
  owner's sort when it lands; no key edit.
- (P) passes, power >= 50%, (A) fails: no shape split of label c at this material by this instrument (a control-backed negative for
  this instrument only, conditional on these tiles and the 14.6%-class reader error).
Report only. Nothing is written to the sorter page, its labels, or any page the owner sorts on. No vision calls.
