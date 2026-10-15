# PREREG-DEC1162RK (account-2 worker DEC1162-RK, LANE DEFAULT-A2-1410-15), committed 15 Oct 2026 14:2x UTC by date -u, before any split score

Brief: `.claude/briefs/runs/2026-10-15-ytbiz-default-1410-jobs.md` "### DEC1162-RK". Input: the owner's g/q sort (ASKS 144, 12 Oct 2026),
applied blind in `sorter/settled_labels.tsv`: 31 tiles, labels g/q split into six piles g, g-b, q, q-b, q-c, q-d. Scripts only, no vision.

## Labels (what changes)
- 1162 `ciphertext.tsv` and 1168 `ciphertext.tsv`: each sorted tile's sign (sid = line + 1-based pos) takes its pile name. Every g/q in
  both files is a sorted tile (10 + 21), so no g/q stays merged there.
- 1168 alignment pairs (the input of `align/run_align.py`): pass A pairs are the same 14 groups as 1168 `ciphertext.tsv`, so they take the
  same piles. Pass B pairs are mapped to the 1168 group of the same gloss and aligned to it sign by sign (difflib on labels); a B token
  that sits on a sorted tile AND is itself labelled g or q takes the tile's pile; any other B g/q token (B-only pairs "conclusioni",
  "laimperatrice", or unaligned positions) becomes `g.u` / `q.u` (unsorted, its own sign, never merged into a pile).
- No clear-text, gloss or other sign label changes.

## Re-key
Same procedure as A2-COS2: the run_align filter, `tools/interlinear_align.py align`, the 20-seed gloss-shuffle control per pass, and
the A2-COS2 combination rule (C = both passes' top value agree with >= 2 agreeing occurrences each; M otherwise; value from pass A, else
pass B). Reproducibility check first: the combination rule applied to the committed merged pass files must rebuild the committed
`key.tsv` exactly (sign, value, grade). If it does not, the job stops at that point and logs the difference; no split key is scored.

## Score (gating)
G of `score_g.py` (PREREG-MOD1162: sum LCS(decoded, gloss) / keyed signs over 1162's 'letters' groups) with the split 1162 labels and
the split key, and its band-shuffle control (values permuted within grade band C / M of the split key) at seeds 0..999 and 1000..1999.
Merged baseline on file: G 0.7288, control p99 0.5254 (both seed sets).

The split key REPLACES the merged one only if ALL of:
1. G_split >= 0.7288 (holds or rises);
2. G_split > the split control's p99 at seeds 0..999 AND at 1000..1999, and G_split >= 0.50;
3. each 1168 pass's realigned agreement beats its own 20-seed gloss-shuffle p95 (the A2-COS2 control).
Otherwise the split stays in `*_split.*` files only and the committed readings, key and scores are unchanged.

The control can differ from the target on G: G depends on which value each pile carries (not a coverage-only statistic).
Known effect, stated in advance: a pile with no 1168 occurrence (expected: g-b) has no key value, so its 1162 tokens leave G's
denominator (U). Coverage is reported before and after; it is descriptive, not a test.

## Reported, not gating
- Per pile: its 1168 values per pass (counts) and, at each 1162 tile, the 1162 gloss letter at the LCS-aligned position.
- J (it16dip) as score_g.py already prints it: descriptive.
- 1168's self-decode token grades before/after (fit set = test set; self-consistency, not a reading).

## Grades (rule 4)
As PREREG-MOD1162 through votes.tsv: C = C-key sign agreeing with 1162's gloss; S = key-transferred, gate passed; M = disagrees or
uncertain. A pile whose two passes split, or with one occurrence, is M. Conflicts between a pile's 1168 value and 1162's gloss go to
HYPOTHESES.md with both witnesses (letter, folio, date, direction).
