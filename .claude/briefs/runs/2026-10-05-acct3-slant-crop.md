# SLANT-CROP (account 3 worker) -- 5 Oct 2026. Opus 5.5. Cap $10, box 120 min. Owner: go; "if it works, systematize it".
Problem: tools/iiif_lines.py cuts axis-aligned line crops; on slanted lines they clip end marks and take in neighbour-line ink
(owner count page, armstrong-madison-1808: 5/27 boxes clipped a mark, several took in numerals from the next line; p1x was a numeral).
Readers get the same crops. Steps (stop at the first failed gate):
0. Per stretch, compare ciphers/armstrong-madison-1808/owner-counts/counts-2026-10-05.tsv with the two transcriptions' mark counts
   (owner = third reader, not truth). Write owner-counts/compare.tsv (stretch, A, B, owner, 2-of-3 or 3-way split). ~$1.
1. Add to tools/iiif_lines.py: --deskew (per-line angle from ink, rotate before cutting) and --mask-neighbours (white out ink
   whose connected component lies mostly outside the line band). Offline tests in tools/tests/. Default OFF until step 3 passes.
2. PREREG in armstrong NOTES before any read: same Sonnet reader prompt, same N Armstrong lines (the 15 disagreement stretches'
   lines), old crops vs new crops, 2 blind passes each; metric = two-reader agreement on mark segmentation (and agreement with the
   2-of-3 consensus from step 0 where it exists). Gate: new > old by >= 5 points on agreement AND no stretch loses a consensus mark.
   Price per pass (Usage 6): ~2 x 2 x N calls.
3. If PASS: systematize -- make --deskew --mask-neighbours the default in iiif_lines.py (flag to turn off), one line in
   TRANSCRIPTION.md and SYSTEM.md naming the change and the evidence, a WORK-QUEUE note listing targets whose crops predate it
   (re-cut candidates, not re-run now); also fix the owner count page generator (if any in tools/) to anchor instructions on the
   bounding numbers ("count between 740 and 67") and pad boxes. If FAIL: log in HYPOTHESES.md "untested-by-this-tool"/FAIL with
   both numbers; keep flags off.
Commit by path, push, ROOM lines, 5-line report.
