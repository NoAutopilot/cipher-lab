# PREREG-MANT-0056 (9 Oct 2026, written to disk by 02:20 UTC before any score was computed; committed only with the results, see NOTES "MANT-0056"; LANE FAMILY-A2e account 2)

Leaf: HStA Dresden 10026 Loc. 694/09, file 0056 (film label "0057"; frames.tsv URL .../c5158a8f-.../fullsize/0056.jpg; 4345x3860,
sha256 prefix 4501d307142ab24d), Berlin 18 Feb 1713 ("p.42" per MANT-0609Y). Question: does Krauske's table (key.tsv as committed at
origin/main c1d700cba, last changed in 1ecc331f7; sha256 prefix d2723c55a394c603) read this leaf's code runs the way the leaf's own interlinear period gloss reads them? The gloss is the known
answer: nothing here is a decipherment of unknown text.

Design copied unchanged from PREREG-MANT-0008 (f0008_09/PREREG-MANT-0008.md); the script is f0008_09/gloss_gate.py copied to
f0056_09/gloss_gate.py with only the docstring and the frame name changed. Fixed before scoring:
- codes: reconciliation of two blind Sonnet passes on 6 code-line crops (tools/iiif_lines.py --image, region 2150,1120,1230,760,
  centres 75,130,182,240,425,487, --top-margin 45 --bottom-margin 20; each cut in two overlapping 2x halves), readers told to ignore
  interlinear words; disagreements settled by this worker from the image -> f0056_09/ciphertext.tsv.
- spans: one row per gloss phrase -> f0056_09/gloss.tsv, codes set by physical position under the gloss ink (one Sonnet gloss pass +
  worker eye). Disclosure: this worker can read key.tsv; spans are placed by where the ink sits, never by what a decode needs; a span
  that cannot be placed by position, or a gloss word that cannot be read, is left out and listed, not guessed.
- Statistic S: per span, DP alignment of codes to gloss letters (lowercase, accents stripped, letters only, roy->roi); a code whose
  key value (any '|' alternative) equals the next gloss letters scores 1; a code may consume 1-3 letters unmatched (0) or none
  (-0.25); a letter may be skipped (-0.25). S = matched codes summed over spans. Codes absent from key.tsv cannot match.
- Control (rule 3): key.tsv values permuted over its codes, 1000 draws, seed 8, same spans and alignment. S depends on which value
  sits on which code, which is exactly what the permutation changes, so the control can differ from the target.
- Gate: PASS iff S > p99 of the control AND S >= 0.5 x keyed codes in spans. Otherwise FAIL.
- On PASS: glossed tokens matched are grade C for this leaf. Codes absent from key.tsv whose slot is bracketed by matched codes or a
  span edge and consumes 1-3 gloss letters (or a whole one-code span's gloss) are listed in f0056_09/key_add_0056.tsv as candidate
  additions graded C, with this leaf's own control result beside each; NOT merged into key.tsv by this job (rule 3 per-unit clause).
  A keyed code reading a different gloss value in a span where all other codes match is a rule-4 conflict, logged in HYPOTHESES.md.
- On FAIL: no candidate list; the leaf is logged as a FAIL with both numbers.
