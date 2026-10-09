# PREREG-MANT0474 (9 Oct 2026, written before any score was computed; LANE FAMILY-A2i account 2)

Leaf: HStA Dresden 10026 Loc. 694/08, film frame 0474 (fullsize 0474.jpg, one GET 9 Oct 2026 ~14:08 UTC; the film card reads
"Aufnahme Einheit 0475"), 4345x3860, sha256 prefix ac2c36d87223be59 (= MANT-INV08's inventory_stride4.tsv row), stamp 379, Manteuffel
to Flemming, Breton / Queen of England matter (paras 3-5). Second witness for MANT-0494's 13 held right-page codes (231-715) and the
54-at-'et' conflict (f0494_08/candidates.tsv).
Question: does Krauske's table (key.tsv at origin/main 7ca4b4f58) read this leaf's glossed code runs the way the leaf's own interlinear
period gloss reads them? A key test, not a reading: the gloss makes the glossed text KNOWN (N0 for those spans).

Protocol = PREREG-MANT0494 exactly, with these inputs:
- codes: two blind Sonnet passes over code-line crops (f0474_08/crops/c0474L_*, c0474R_*; readers told to skip interlinear words), one call per
  page per pass (4 calls; pass B reads in reverse order); reconciled by this worker from the image where they disagree -> f0474_08/ciphertext.tsv.
  Reconciliation is done before any gloss is attached to codes and before any score; key.tsv values are not consulted to settle a digit.
- gloss: ONE blind Sonnet gloss pass per page (gloss_L.tsv, gloss_R.tsv; V-BRANDT rule). The gloss text of each note is used exactly as that
  pass wrote it (letters only; '?' letters and '[?]' marks dropped); this worker does NOT correct, complete or settle any gloss word. A note
  the pass marks 'none' or does not see is absent (no span).
- spans: f0474_08/gloss.tsv, one row per gloss note, with the code tokens it sits over, set by physical position (the pass's x extents /
  'sits_over' and this worker's eye on the image). Disclosure: this worker has seen key.tsv's values and MANT-0494's results; spans are set
  by where the ink sits, never by what a decode would need; a note whose codes cannot be placed by position is left out and listed.
  Expected shape (from a pre-pass look at the leaf, before any pass returned): the leaf's code is in the letter range (mostly <= 120) with
  a few higher codes (150, 246?, 303); left page one glossed run; right page ~8 runs, most glossed.

Statistic S: exactly f0494_08/gloss_gate.py's (= f0008_09's): per span, a DP alignment of codes to gloss letters (lowercase, accents
stripped, letters only, 'roy'->'roi'); a code whose key value (any '|' alternative, letters only) equals the next gloss letters scores 1;
a code may consume 1-3 gloss letters unmatched (0) or none (-0.25); a gloss letter may be skipped (-0.25). S = matched codes.
Control (rule 3): key.tsv values permuted over its codes, 1000 draws, seed 474, same spans and alignment. S depends on the value-to-code
assignment, which is exactly what the permutation changes, so the control can differ from the target.

Gate, per gloss pass (left page = gloss_L, right page = gloss_R) and pooled (reported only): PASS if S > p99 of the control AND
S >= 0.5 x keyed codes in spans. A pass whose spans hold fewer than 10 keyed code tokens is "too short", neither PASS nor FAIL. A span's
codes are grade C (from the period gloss) only under a pass that PASSes.

Cross-leaf table (the job's point; descriptive, no gate): for each of MANT-0494's held/conflict codes (715, 295, 340, 475, 410, 403, 431,
384, 499, 419, 375, 583, 548, 408, 231, 357, 581, 561, 540, 44-at-c, 34-at-Hyen, 54-at-et) list its occurrences on 0474 (settled
ciphertext) and the 0474 gloss slot under the best alignment: agree / disagree / absent. A code agrees only if its 0474 slot is
bracketed by matched codes or a span edge (or is the only code under a whole note) and reads the same letters as 0494's slot.
-> f0474_08/candidates.tsv; never key.tsv. Codes outside key.tsv on 0474 itself go to the same file under the 0494 candidate rule.

Unglossed long runs (>= 15 tokens, no gloss over them): gate (b) exactly as f0494_08/judge_gate.py (fr18 permuted-key, power control,
power >= 0.80) at their N; otherwise "too short", no reading; if they decode to continuations of gloss phrases, say so (known text).
Skipped if the job has used 80% of its cap.

Script: f0474_08/gloss_gate.py (writes gate.out; --check exits 1 if stale).
