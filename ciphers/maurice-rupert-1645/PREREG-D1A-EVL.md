# PREREG-D1A-EVL (8 Oct 2026, written before any alignment score was computed)

Job: harvest every printed cipher-number / gloss pair on Bray's Evelyn Memoirs (1819) vol. II correspondence pages (IA
memoirsillustrat02eveluoft) into key rows of the 9119 family, then re-run keys/key_test.py.

Instrument: keys/evelyn_harvest.py (OCR word boxes -> gloss/cipher line pairs) then tools/interlinear_align.py align
--floor 101 (codes 1-100 take at most one letter: the 9119 form's letters sit in 1-100), no --prior (the 9119 rows are
the check, so they must not seed the alignment), --shuffle 200 (gloss lines dealt to the wrong cipher lines).

Gates, fixed now:
1. Alignment control: the real run's CONSISTENT count must exceed the shuffle control's p95 (rule 3; the shuffle moves
   which gloss sits over which numbers, so it can fail differently).
2. Agreement check against key9119.tsv: among codes that key9119 fills AND the harvest reads with count >= 2 and share
   >= 0.6, the harvest's value must equal key9119's (u/v and f/s folded) in >= 70% of codes. Below 70%, no harvested row
   enters a key; the harvest is logged as a failed instrument.
3. Pages: primary set pp.102-115 (Aug-Oct 1645, the pages the 9119 form cites and their neighbours). Pages 82-101 and 120
   enter only if their own agreement with key9119 (same rule as 2, computed on that set alone) is >= 70% with >= 5 codes
   compared; otherwise they are a different key or too thin and are excluded.
4. Rows added to keys/evelyn_pairs.tsv: only codes the 9119 form leaves blank, count >= 2 on >= 2 cipher lines with
   share >= 0.6 (grade C for a whole-word gloss, I where the value is a letter or syllable split out of a word), or a
   count-1 reading on a code the 7 July letter uses, graded M. Conflicts with key9119 are listed, not applied.
5. Then keys/key_test.py is re-run on key9119 + the added rows (as key9119e) with its existing all-slot, banded and power
   controls; report coverage before (42/93 with the R15-MREVL rows) and after. The power control decides whether the
   4-gram result is a test (power >= 40/50) or a non-test.
