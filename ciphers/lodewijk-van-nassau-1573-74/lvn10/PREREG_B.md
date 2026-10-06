# R13-LVN10B pre-registration addendum (6 Oct 2026, written and pushed before any blind read is opened)

Attempt 2 of the R12-LVN10 instrument on WVO 4610 p3 (a defect repair: pass B4 was truncated past crop 11).
Everything in lvn10/PREREG.md holds unchanged -- material, targets (lvn10/targets.tsv, 63 rows), alignment (one page
sequence, difflib, autojunk off, equal and equal-length replace blocks 1:1), control (the 230 H numeral rows of
p3_L12-L31), **gate each pass >= 0.90**, settle rule (non-H row to H only when the two passes agree exactly, no '?'
mark, both aligned; no insertions/deletions). Only the pass layout and the prompt change:

Material check (13:2x UTC): WVO PDF re-fetched once (HTTP 200, 3,689,372 bytes), p3 rendered
`pdftoppm -png -r 300 -f 3 -l 3 04610.pdf 04610` -> 04610-3.png 2481x3508, sha1 a41b5df838e49cefb71e30cdfbe0803f3947d591
(matches R12-LVN10). Crops re-cut with R12-LVN10's exact command:
`python3 tools/iiif_lines.py --image 04610-3.png --out crops --prefix 04610_p3 --region 120,1150,2350,1950 --distance 65
--prominence 20 --top-margin 12 --bottom-margin 12 --debug` -> 22 crops, centres (region y) 26 105 197 278 348 448 534 630
713 808 891 993 1072 1168 1261 1349 1427 1521 1604 1682 1766 1843 (scratchpad, not committed).

Pass layout: two blind passes, A5 and B5, each run as two separate Sonnet 5.5 calls of 11 crops (batch 1 = L01-L11,
batch 2 = L12-L22), so 4 calls in all. Each call sees only its 11 crop paths and the prompt below; never the
transcription, the key, the earlier passes A4/B4, or the other pass. A batch that returns fewer crops than it was
given is re-run once (same prompt) before scoring; that re-run is logged.

Prompt change (the only change of substance): the reader is told about the hand's confusable numerals --
a '1' written with a hooked or flagged top that looks like '2'; '5' vs '3'; '8' vs '3' -- and asked to look at
each such digit twice. The prompt does not say which reading is usually right.

Scoring: lvn10/score.py --round b (passA5.tsv/passB5.tsv -> aligned_b.tsv); apply: lvn10/apply.py --round b
(writes ciphertext_4610.tsv and apply_log_b.tsv only if the gate passes). If either pass is below 0.90, no row is
changed and, per rule 3's third-attempt clause, a third attempt needs a different instrument, not a third run of
this one.
