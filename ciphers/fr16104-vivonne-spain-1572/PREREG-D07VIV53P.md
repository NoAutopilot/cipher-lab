# PREREG-D07VIV53P (7 Oct 2026, D07-VIV53, account-1 worker for LANE DEFAULT-account-1-20261007-0042)

Committed and pushed before any judge call. Target: ink 53 (fr.16104 ff.170r-171v), reading R7A-VIV53 G (reading_piece53_G.tsv).
Question (AUDIT 4; D1-F16104K whole-label test negative): do individual positions of the U labels e (16) and o (33) carry the key image's
f, m or p signs (context suggests e merges an f and an m sign, o a p sign)? Instrument: DEF1-VIV54's hand-placed per-position crops.

## (i) Items and placement
Targets: all 49 e/o tokens of reading_piece53_G.tsv. Known-answer control: 3 H-graded positions each of the settled labels d, m, p, g
(seed "20261053P"; tx/lookalike53P/viv53P_items.tsv, 61 items). The worker marks each sign's strip x by eye on tx/viv53P_place.py sheets
(tx/lookalike53P/viv53P_xmarks.tsv); an item the worker cannot find is marked x=-1 and dropped (count reported). Crops: strip x +-110 px
native, 2x, red ticks at the mark, opaque ids, no label, no context, no decoded text.

## (ii) Reference cells (sources/cryptiana/web/henryiii_Vivonne1.png), shown under opaque letters, shuffled
f row 1, g row 1, m row 1, m row 2, m row 5, p row 1 (candidates and look-alike foils for e/o); o row 1, e row 1, n row 1, r row 1
(the control labels' cells: d -> o1, m -> e1, p -> n1, g -> r1, per key.tsv). m row 3 is not shown (its column is ambiguous on the image).

## (iii) Judge
Two independent blind Sonnet calls, same crops, different montage orders (seeds "20261053P-A", "20261053P-B"). Each answers per crop one
reference letter or NONE, conf H/M/L, and a stroke note. Reconciliation (this worker) is mechanical: the rules below; disagreements are
listed, not settled by eye.

## (iv) Control gate (run first; scored before any target answer is read)
Per pass: control correct cell at H/M >= 8 of 12 placed controls (0.67) and firm (H/M) wrong-cell answers <= 2. Both passes must pass.
The control can fail differently from the target: the judge can name any of the 10 cells or NONE for a control crop.
If either pass misses: NON-TEST, nothing applied, target answers not used.

## (v) Target rule
A target position is relabelled only when BOTH passes name the same reference cell at H/M, and that cell is f1, m1, m2, m5 or p1
(meanings f, m, m, m, p) -- or o1/e1/n1/r1 (an existing label's cell: d=o, m=e, p=n, g=r), applied the same way. g1 is a foil
with no key.tsv meaning: a g1 answer is reported, not applied. Applied positions go to an ink-53-only per-position overlay
(tx/lookalike53P/viv53P_overlay.tsv; key.tsv untouched), graded M (shape-judged on the manuscript, cell from the published key).

## (vi) Gates on the overlay
If any position is applied: the whole-piece gates of tx/viv53G_decode.py (b2 vs shuffled p99, and 200 wrong-key draws) re-run on the
overlaid stream (seed "20261053P"); the overlay is kept only if both still PASS. Reported beside them: the registered V_strict stretch
top-1 before (20) and after. A per-position relabel changes the counted reading: decode --check, grade counts, ROOM flag for a verifier.
No depth claim is made here.
