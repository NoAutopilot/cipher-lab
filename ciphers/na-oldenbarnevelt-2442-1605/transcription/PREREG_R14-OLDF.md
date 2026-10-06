# PREREG R14-OLDF (6 Oct 2026, written before the blind pass was read)

Job: NOTES section 17 Verdict step (f). LANE LANE-RUN14-account-2.

1. Units: the 14 M/I-graded B/C1 tokens of reading_tokens.tsv (B28 B29 B31 B37 B57 B64; C1 3 5 21 29 30 31 36 44).
   Per-token crops: `python3 scripts/token_crops_R14OLDF.py` -> images/crops_R14OLDF/ (cut from scans 002/006 on disk).
2. One blind Sonnet pass on those crops only (no key, no committed transcription, no decoded values; notation as OLD-PASS2:
   letters as letters, digit-shaped signs as digits, G-shaped ligature `l7`, superscript `^a`).
3. Change rule: a committed sign changes only if (a) the blind reader names a different sign at that position AND
   (b) the worker's reconciliation on the same crop judges the image to settle it (not a look-alike pair of the
   OLD-PASS2 list read under a different naming convention: 9/q, f/p long descender, v/r, l/t). A plausible-word
   argument alone never changes a sign. Disagreements that the image does not settle stay as committed.
4. If no sign changes: no re-judge (section 17). If any sign changes: re-run `scripts/segment_judge.py` unchanged
   under PREREG_R13-OLDSEG.md (same window cut, judge, corpus es1600, controls) and report each window beside its
   real_p05, held-out p05 and null_p99; the PASS/FAIL call is PREREG_R13-OLDSEG item 5's, unchanged.
5. Figure reported: per-sign agreement of the blind pass with the committed rows on these 14 tokens (agreement,
   not accuracy).
