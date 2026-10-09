# PREREG-F19 (D1162-F19 worker, account 4, 9 Oct 2026, written before any crop or exemplar was looked at in this job)

Question: the month on p.2 l.6 (clear_text.tsv row 2/6, focus id F19, `27^o febr~? 1491`): February or September.

Instrument (the "key" is the hand's own letter forms, not a model read): slot 1 of the month word is compared, by
normalised cross-correlation on the binarised crops (`clear/enhance/out/`-style processing of `images/clear/` only), against
exemplar glyphs of **f** and of **long s** cut from words of the same main hand already settled in clear_text.tsv (no '?').
Nearest-class-mean NCC decides the slot.

Control (rule 3), run before the target is scored: leave-one-out over the exemplar set itself (each exemplar classified
against the class means of the others). Gate: >= 80% right, with >= 4 exemplars per class, and above the 95th percentile of
a 1000-draw label-shuffled null of the same statistic. If the control misses its gate, stop: no target score is used,
F19 stays `febr~?`, logged untested-by-this-tool.

Decision rule, fixed now:
- Control PASS and slot 1 = f with margin (target NCC to f mean minus NCC to s mean) > 0 and outside the null band of
  the shuffled-label margin: F19 reads `febr~` (grade S), the '?' is removed in clear_text.tsv.
- Control PASS and slot 1 = long s by the same margin rule: F19 is logged as "September supported by the glyph test",
  the text is NOT changed by this job alone (it would contradict the docket, the archive strip and DOC 3593; a reader
  decides), logged as a conflict.
- Anything else: no change, logged.
Dating evidence already in NOTES (docket '27 febb^o', archive strip '1491 év 02 hó 27 nap', DOC 3593 'fibr', 1491 +
25-March year = 1492 modern beside busta 2's 1492 run) is tabulated as context, not counted as an independent vote: the
docket, the strip and DOC 3593 are all readings of this same word or of the docket, not separate witnesses to the date.
