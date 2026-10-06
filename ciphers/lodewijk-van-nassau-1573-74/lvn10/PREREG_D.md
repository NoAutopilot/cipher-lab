# R14-LVN10D pre-registration addendum (6 Oct 2026, written and pushed before any blind read is opened)

Defect repair of the per-token-crop instrument (lvn10/PREREG_C.md, attempt 1, control FAIL 0.726/0.722). **Layout change
only.** Everything else in PREREG_C.md (and through it PREREG.md) holds unchanged: material (p3 at 300 dpi, sha1
a41b5df838e49cefb71e30cdfbe0803f3947d591, WVO PDF re-fetched once 15:3x UTC, HTTP 200, 3,689,372 bytes), targets
(lvn10/targets.tsv, 63 rows), alignment (score.py: numeral rows of ciphertext_4610_pre.tsv p3_L12-L31 as one page sequence,
'|' dropped, difflib autojunk off, equal and equal-length replace blocks 1:1), control (the 230 H numeral rows), **gate each
pass >= 0.90**, settle rule (non-H row to H only when A == B exactly, no '?', both aligned; no insertions/deletions), reader
prompt (verbatim from PREREG_C.md), A call returning < 90% of its tiles re-run once (logged).

What changed (`python3 lvn10/tokcrops.py 04610-3.png tokd --repair`; without --repair the script reproduces round c's
blobs.tsv byte for byte):
1. Speck filter (the defect R14-LVN10C named): a narrow blob (< 24 px, < 500 ink px) is dropped only if shorter than 20 px or
   its top sits > 9 px below the local x-height top (median top of wide blobs within 250 px); a hooked '1' or a narrow
   '8'/'9' is kept (seen dropped in round c: L11 '81', L12 '9' and '115', L1 '92').
2. Slope (a second defect found on this job's overlay, before any read): the written lines slope by up to about 90 px over the
   line, so round c's fixed horizontal bands cut the left part of each lower line from the line below (round c's band for
   physical line 11 held line 12's opening, its band 12 held line 13's): tiles carried wrong page order. Each line's centre is
   now tracked from the right margin leftwards in 120 px windows (+-25 px search, gain 0.7) and fitted by a quadratic; every
   column's band and every tile's vertical window follow that centre. Overlay checked by eye on all 22 lines.
3. Join: kept blobs <= 16 px apart with no dropped speck between are joined (any width); an over-joined tile shows two
   comma-separated numbers, read in order. Eye check 1 (10 random tiles, seed 20261006, after fixes 1-2): 8 whole, 2 split
   inside a number ('115' -> '11'|'5', '77' -> '7'|'7'); a 30 px join chained half-lines (161 blobs) and was rejected;
   16 px joins both. Eye check 2 (10 fresh random tiles, seed 1610, final cut): 10 of 10 carry their whole number(s)
   (2 are script words). Known residue seen on the overlay, not repaired: a few splits at wider gaps (L18 '298', L21 '142').
4. Sheets: 323 blobs, shuffled with seed 4611, 16 tiles per sheet in 2 columns of 1500 px -> 21 sheets (lvn10/blobs_d.tsv);
   1 tile truncated at the sheet width (LP, L13 clear-script run, last ~10 source px).

Reads: two blind passes A7 and B7, each two Sonnet 5.5 calls (batch 1 = sheets 01-11, batch 2 = sheets 12-21), 4 calls;
each call sees only its sheet paths and the PREREG_C prompt. Conversion: reads_A7.tsv / reads_B7.tsv ->
`lvn10/blobs2pass.py A7|B7 --blobs blobs_d.tsv` -> passA7/passB7.tsv -> `lvn10/score.py --round d` (aligned_d.tsv) ->
`lvn10/apply.py --round d` (applies only if both passes >= 0.90).
This is the one allowed defect repair of attempt 1 of per-token crops (rule 3): if the control FAILs again with the crops eyed
clean, nothing is applied and per-token crops are [retired] for 4610 p3.
