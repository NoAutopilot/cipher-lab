# PREREG-MANT0494 (9 Oct 2026, written before any score was computed; LANE FAMILY-A2i account 2)

Leaf: HStA Dresden 10026 Loc. 694/08, film frame 0494 (file 0494.jpg; card reads "Aufnahme Einheit 0495", the offset noted in MANT-INV08),
sha256 prefix 3a5e0b088808415c (= MANT-INV08C's), stamp 395, Manteuffel to Flemming, Breton / Queen of England matter.
Question: does Krauske's table (key.tsv at origin/main 976b7cf62) read this leaf's glossed code runs the way the leaf's own interlinear period
gloss reads them? A key test, not a reading: the gloss makes the glossed text KNOWN (N0 for those spans).

Inputs fixed before scoring:
- codes: two blind Sonnet passes over code-line crops (f0494_08/crops/c0494L_*, c0494R_*; readers told to skip interlinear words), half a
  page's code per call (4 calls); reconciled by this worker from the image where they disagree -> f0494_08/ciphertext.tsv. Reconciliation
  is done before any gloss is attached to codes and before any score; key.tsv values are not consulted to settle a digit.
- gloss: ONE blind Sonnet gloss pass per page (gloss_L.tsv, gloss_R.tsv; V-BRANDT rule). The gloss text of each note is used exactly as that
  pass wrote it (letters only; '?' letters and '[?]' marks dropped); this worker does NOT correct, complete or settle any gloss word.
  A note the pass marks 'none' or does not see is simply absent (no span).
- spans: f0494_08/gloss.tsv, one row per gloss note, with the code tokens it sits over, set by physical position (the pass's x extents /
  'sits_over' and this worker's eye on the image). Disclosure: this worker has seen key.tsv's values; spans are set by where the ink sits,
  never by what a decode would need; a note whose codes cannot be placed by position is left out and listed.

Statistic S: exactly f0008_09/gloss_gate.py's (PREREG-MANT-0008): per span, a DP alignment of codes to gloss letters (lowercase, accents
stripped, letters only, 'roy'->'roi'); a code whose key value (any '|' alternative, name values letters-only) equals the next gloss letters
scores 1; a code may consume 1-3 gloss letters unmatched (0) or none (-0.25); a gloss letter may be skipped (-0.25). S = matched codes.
Control (rule 3): key.tsv values permuted over its codes, 1000 draws, seed 494, same spans and alignment. S depends on value-to-code
assignment, which is exactly what the permutation changes, so the control can differ from the target.

Gate, computed separately per gloss pass (left page = gloss_L, right page = gloss_R) and pooled (reported): PASS if S > p99 of the control
AND S >= 0.5 x keyed codes in spans. A pass whose spans hold fewer than 10 keyed code tokens is reported "too short", neither PASS nor
FAIL. Grading: a span's codes are grade C (from the period gloss) only for a pass that PASSes.

Candidates (never key.tsv): a code absent from key.tsv (above 401, or a gap) whose slot in the best alignment of a PASSing pass is bracketed
by matched codes or a span edge and consumes gloss letters, or which is the only code under a whole note -> f0494_08/candidates.tsv with
its gloss slot, n instances, grade C (gloss) and "candidate, not keyed". A keyed code whose slot in a span where every other code matched
reads a different gloss value -> listed in candidates.tsv as a conflict (rule 4), key.tsv unchanged.

Unglossed long runs (>= 15 tokens with no gloss over them): decoded with key.tsv only if gate (b) passes at their N -- the fr18 permuted-key
test with power control exactly as f0177_08/judge_gate.py (52-letter blocks, power from the positive-control streams, power >= 0.80 needed);
otherwise "too short", no reading. Skipped altogether if the job has used 80% of its cap.

Script: f0494_08/gloss_gate.py (writes gate.out; --check exits 1 if stale).
