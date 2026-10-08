# PREREG-MANT-0008 (8 Oct 2026, written before any score was computed; LANE FAMILY account 2)

Leaf: HStA Dresden 10026 Loc. 694/09, film frame 0008 (sha256 prefix 08e05a6b1ebc5a37, the same file MANT-0609X inventoried).
Question: does Krauske's table (key.tsv as committed at origin/main 224e2bf16) read this leaf's code runs the way the leaf's own
interlinear period gloss reads them? The gloss is the known answer (prior-work: text KNOWN from the gloss, N0 for this leaf).

Inputs fixed before scoring:
- codes: reconciliation of two blind Sonnet passes on 12 code-line crops (readers told to ignore interlinear words), settled from the
  image by this worker where they disagree -> f0008_09/ciphertext.tsv.
- spans: one row per gloss phrase -> f0008_09/gloss.tsv with the code tokens it sits over, set from the image by physical position
  (gloss pass + worker eye). Disclosure: this worker had seen key.tsv's values before setting spans; spans are set by where the ink
  sits, never by what a decode would need, and a span that cannot be placed by position is left out (listed as such), not guessed.

Statistic S (per code): for each glossed span, a dynamic-programming alignment of its codes to the gloss letters (lowercase, accents
stripped, letters only, "roy"->"roi"). A code whose key value (any "|" alternative; a name value compared letters-only) equals the
next gloss letters scores 1 and consumes them; a code may instead consume 1-3 gloss letters unmatched (0), or none (-0.25, a null);
a gloss letter may be skipped (-0.25). S = number of codes matched in the best alignment, summed over spans. Codes not in key.tsv
can never match. Also reported: N codes in spans, N keyed, distinct codes matched on every instance.

Control (rule 3): key.tsv's values permuted over its codes, 1000 draws, seed 8, same spans, same alignment. S depends on which value
sits on which code, which is exactly what the permutation changes, so the control can differ from the target. The permutation keeps the
key's letter frequencies (homophones), so a high-frequency-letter key does not get a free pass.

Gate: PASS if S > p99 of the 1000 control draws AND S >= 0.5 x (keyed codes in spans). Otherwise FAIL (no key.tsv change).

Key extension (only on PASS, per CLAUDE.md rule 3 per-unit gate): a code absent from key.tsv (above 401 or a gap in the table) whose
slot in the best alignment is bracketed by matched codes or a span edge and consumes 1-3 gloss letters (or a whole one-code span's
gloss) gets that value; entered into key.tsv grade C, source "694/09 0008", note "gloss of 694/09 0008, n=<instances>". A keyed code
whose slot in a span where every other code matched reads a different gloss value is a conflict: logged in HYPOTHESES.md with both
witnesses (rule 4), key.tsv unchanged.

Script: f0008_09/gloss_gate.py (writes gate.out; --check exits 1 if stale).
