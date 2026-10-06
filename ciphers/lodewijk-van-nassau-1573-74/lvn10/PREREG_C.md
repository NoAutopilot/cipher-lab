# R14-LVN10C pre-registration (6 Oct 2026, written and pushed before any blind read is opened)

Attempt 3 on WVO 4610 p3 with a **different instrument** (rule 3's third-attempt clause; the whole-line blind-pass instrument of
R12-LVN10 / R13-LVN10B is [retired]): per-token crops. Everything else in lvn10/PREREG.md holds unchanged -- material, targets
(lvn10/targets.tsv, 63 rows), alignment (the numeral rows of ciphertext_4610_pre.tsv p3_L12-L31 as one page sequence against each
pass's numeral tokens, '|' dropped, difflib, autojunk off, equal and equal-length replace blocks 1:1), control (the 230 H numeral
rows of p3_L12-L31), **gate each pass >= 0.90**, settle rule (non-H row to H only when the two passes agree exactly, no '?' mark,
both aligned; no insertions/deletions).

Material (15:2x UTC): WVO PDF re-fetched once (HTTP 200, 3,689,372 bytes), p3 rendered `pdftoppm -png -r 300 -f 3 -l 3` ->
sha1 a41b5df838e49cefb71e30cdfbe0803f3947d591 (matches R12-LVN10/R13-LVN10B). Line crops, R12-LVN10's exact command (pasted):
`python3 tools/iiif_lines.py --image 04610-3.png --out crops --prefix 04610_p3 --region 120,1150,2350,1950 --distance 65
--prominence 20 --top-margin 12 --bottom-margin 12 --debug` -> 22 crops, same centres; those centres fix the 22 line bands.

Instrument: `python3 lvn10/tokcrops.py 04610-3.png tok` cuts every token blob of the 22 bands from the image alone (no
transcription value is used to cut or order them): 358 blobs, each with its own vertical window, upscaled 1.5x, tiled in a fixed
shuffled order (seed 4610) into 12 contact sheets of 32 tiles under letters-only labels (blobs.tsv, committed, maps label ->
physical line, x, page order). The reader sees isolated tokens out of order, so no line context, sloping line or crop boundary
can carry a run of errors (the R13-LVN10B diagnosis), and controls and targets are indistinguishable.

Reads: two blind passes A6 and B6, each two Sonnet 5.5 calls (batch 1 = sheets 01-06, batch 2 = sheets 07-12), 4 calls; each
call sees only its six sheet paths and the prompt below, never the transcription, key, earlier passes or the other pass. A call
that returns fewer than 90% of its tiles is re-run once (logged). Prompt (same for all four calls):
"Each tile on these contact sheets is one cut-out word or number from a 16th-century French cipher letter written in numbers.
For every tile, write one line: the tile label, a TAB, then what the main line of writing in the tile says: each number in it,
left to right, separated by spaces; '|' for a word of ordinary script (one '|' per run of words); '-' if nothing legible.
Ignore commas and dots, and ignore fragments of other lines cut by the tile's top or bottom edge. Append '?' to a number you
are not sure of. The hand's numerals are easy to confuse: a '1' with a hooked or flagged top can look like '2'; '5' vs '3';
'8' vs '3' -- look at each such digit twice. Output only the lines, one per tile, every tile."

Conversion and scoring: reads_A6.tsv / reads_B6.tsv (verbatim reader output) -> `lvn10/blobs2pass.py A6|B6` (page order from
blobs.tsv) -> passA6.tsv / passB6.tsv -> `lvn10/score.py --round c` (aligned_c.tsv) -> `lvn10/apply.py --round c` (writes
ciphertext_4610.tsv and apply_log_c.tsv only if both passes >= 0.90). If either pass is below 0.90 no row changes; this
instrument then counts as attempt 1 of per-token crops, logged in NOTES.md and HYPOTHESES.md.
