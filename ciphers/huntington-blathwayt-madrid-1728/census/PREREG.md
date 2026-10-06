# PREREG -- R7B-HUNT descending-glyph census (6 Oct 2026, written 02:09 UTC by date -u, before any crop is viewed)

Question: is the descending z-shaped digit on BLA188 p4-p6 and BLA194 p1 the hand's 7 (passes read it 3, 5 or 9)?

Populations (from census/swapstats.py, leave-these-pages-out key, glosses normalised for apostrophes):
- T (test): every glossed column on the four pages whose read 3/5/9 becomes the key's value for its gloss when that one
  digit is 7 (23 columns: 17 x 5->7, 6 x 3->7, plus 935 9->7; 290 and 251, where 7 is one of several swaps, are reported
  but not counted).
- K (control, true non-7): glossed columns on the same pages read as-read (gloss = key value of the read group) whose
  group contains a 3, 5 or 9 -- that digit is confirmed genuine by the gloss.
- S (control, true 7): glossed as-read columns on the same pages whose group contains a 7.

Method: native IIIF line crops (hdl.huntington.org, >= 1.6 s apart), read by eye in this session, one priced unit. Each
inspected digit classed Z (descending z-form: top bar, diagonal, tail below the line), plain-3, plain-5, plain-9,
plain-7, or unclear. Not blind: the reader knows the gloss (stated in the result).

Gate (both must hold to settle Z = 7 and re-grade T columns from M/H-as-misread to the 7 reading):
1. >= 80% of the T digits that are not 'unclear' are Z;
2. <= 10% of the K digits (3/5/9 confirmed by gloss) are Z, and at least 8 K digits are classed.
If 1 holds and 2 fails, Z is ambiguous between 7 and the confirmed digit: no settlement, columns stay M.
If 1 fails, the misreads are not one glyph form: no settlement; log per-column readings only.
