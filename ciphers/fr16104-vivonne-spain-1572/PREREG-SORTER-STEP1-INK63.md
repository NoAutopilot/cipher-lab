# PREREG-SORTER-STEP1-INK63 (15 Oct 2026, 06:4x UTC by date -u; account-1 worker SORTER-STEP1-INK63 for LANE VIV-KEYSTONE, account 4)

Written and pushed BEFORE the step-1 page is built and before any owner answer exists. Brief: .claude/briefs/runs/2026-10-15-acct4-for-acct1-jobs.md
"JOB SORTER-STEP1-INK63". Nothing here is a reading; no key.tsv, reading, rec.tsv or status.json edit.

## 1. Material (fixed now)
- Pool: `tx/sorter_step1/pool.py` (committed with this file; `--check` reproduces it): certain-answer tiles = single pen-unit boxes mapped 1:1
  to a scored, unflagged truth position whose reader label is one of that position's truth letters and whose key meaning is the clerk's letter
  (build_inputs.py packet3's rule, uncapped). Leaves f.102r (dev2), f.103r (confirm2), f.201r (dev): 628 tiles, 24 key codes. f.201v, f.202r,
  f.211r, f.211v: no box map exists (VIV-67C/70C2 line crops were scratchpad-only) -- not available, not regenerated in this job.
- Sample `tx/sorter_step1/sample.tsv`: per code min(n, 22), total 297 (seed 20261015). Codes under 6 exemplars: 4:2, P:2, f:1, h:5, k:2, to:3
  (all they have); key codes with no certain tile: A, S, V, Zu, b, e, oo, y.
- Box check (R14 gate, >= 90%): this worker's eye on contact sheets of all 297 tiles before the page is built, one verdict per tile
  (whole / not), written to `tx/sorter_step1/box_check.tsv`. If under 90% pass, the page is not built; failing tiles are dropped either way
  and the pass rate is reported before the drop.

## 2. Seed piles (fixed now)
`tools/glyph_atlas.py cluster --k 40` (HOG + log size, PCA 40, k-means seed fixed in the tool) on 48x48 binarised bitmaps of the passing tiles;
one pile per cluster, named by a neutral shape id ("shape 01".."shape 40", order seeded), no key value, letter or reader label on the page
(blind: `--seed-shape`). The owner's step 1 only: merge, split, set aside. No question tray, no --focus.

## 3. Consuming test (run when the owner's settled piles land; `sign_sorter_apply.py` export of this page)
(a) Relabel and score. Pile label L(p) = plurality key code of p's sample tiles (tie: alphabetical first, ties listed). A pile set aside has no
label. For each leaf X in {f.102r, f.103r, f.201r}, leave-one-leaf-out: only piles' tiles from the OTHER two leaves set L(p) and serve as
neighbours. Every 1:1-mapped pen-unit tile of X (tx/vivcls maps) is placed by kNN (k = 3) in the glyph_atlas cluster feature space fitted on
the page's tiles; pass A's token at that position takes L(p) only when all 3 neighbours sit in one labelled pile, else it keeps its label.
Score `tools/tx_bench.py --item <item>` on pass A before and after.
Before (pass A as committed, measured 15 Oct 2026 06:4x UTC): f102r-dev2 err_true 0.194 (239/1234); f103r-confirm2 0.232 (248/1068);
f201r-dev 0.185 (165/894).
**Gate:** err_true must not rise on any of the three items and must fall on >= 2.
**Controls (rule 3), same procedure:** (i) the seed piles as built (no owner change) -- the owner's sort must beat it on >= 2 items for the
gain to be attributed to the sort; (ii) shuffled piles (the owner's pile sizes kept, memberships permuted, 20 seeds): if the shuffled
median passes the gate, the test is a non-test at this N and is logged so, not as a pass. The controls can differ from the target
(labels change with membership), so they are not orthogonal to the statistic.
(b) The settled one-shape piles become the exemplars of the next f.191r question packet (PREREG-VIVPACKET4, one-shape piles by construction),
built with `tools/sign_sorter.py --piles-from <this page's settled.tsv> --answered-only`.

## 4. Not done here
No publishing (the account-4 parent decides), no owner question, no scoring.
