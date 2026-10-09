# PREREG-MANT-0063 (9 Oct 2026, written and committed with git at ~02:52 UTC by date -u, BEFORE any score; LANE FAMILY-A2e account 2)

Leaf: HStA Dresden 10026 Loc. 694/09, file 0063 (film label "0064"; frames.tsv URL .../c5158a8f-.../fullsize/0063.jpg; 4339x3866,
sha256 prefix b58656a6e157f2df), page "44.", Berlin ... Fevr 1713 (MANT-0609Y: "p.44, Berl. 15 ..."). Question: does Krauske's table
(key.tsv as committed at origin/main 551098f5e, last changed in aacd8b312; sha256 prefix d2723c55a394c603) read this leaf's code runs
the way the leaf's own interlinear period gloss reads them? The gloss is the known answer: nothing here deciphers unknown text.

Design copied unchanged from PREREG-MANT-0056 (f0056_09/PREREG-MANT-0056.md, itself PREREG-MANT-0008's); the script is
f0056_09/gloss_gate.py copied to f0063_09/gloss_gate.py with only the docstring and the frame name changed. Fixed before scoring:
- codes: reconciliation of two blind Sonnet passes on 7 code-line crops (tools/iiif_lines.py --image, regions 2130,1840,1240,150
  centres 65,120; 2130,1990,1240,150 centres 55,120; 2130,2480,1260,180 centres 50,105; 2130,1660,700,150 centre 90; each crop
  enlarged 2x for the readers), readers told to ignore interlinear words; disagreements settled by this worker from the image ->
  f0063_09/ciphertext.tsv.
- spans: one row per gloss phrase -> f0063_09/gloss.tsv, codes set by physical position under the gloss ink (one Sonnet gloss pass +
  worker eye). Disclosure: this worker can read key.tsv; spans are placed by where the ink sits, never by what a decode needs; a span
  that cannot be placed by position, or a gloss word that cannot be read, is left out and listed, not guessed. Before scoring, the
  worker saw (eye, 1x) that one gloss run (over the long run after "obligeants,") is German ("Was hat er ... Dich Dankbar zu
  bekennen"?); German spans are scored exactly like French ones (same letters() normalisation; umlauts stripped, no other mapping).
- Statistic S: per span, DP alignment of codes to gloss letters (lowercase, accents stripped, letters only, roy->roi); a code whose
  key value (any '|' alternative) equals the next gloss letters scores 1; a code may consume 1-3 letters unmatched (0) or none
  (-0.25); a letter may be skipped (-0.25). S = matched codes summed over spans. Codes absent from key.tsv cannot match.
- Control (rule 3): key.tsv values permuted over its codes, 1000 draws, seed 8, same spans and alignment. S depends on which value
  sits on which code, which is exactly what the permutation changes, so the control can differ from the target.
- Gate: PASS iff S > p99 of the control AND S >= 0.5 x keyed codes in spans. Otherwise FAIL.
- Secondary (reported, not a gate): S on French-only spans and on German-only spans, each against the same control computed on that
  subset (labelled exploratory).
- On PASS: glossed tokens matched are grade C for this leaf. Codes absent from key.tsv whose slot is bracketed by matched codes or a
  span edge and consumes 1-3 gloss letters (or a whole one-code span's gloss) are listed in f0063_09/key_add_0063.tsv as candidate
  additions graded C, with this leaf's own control result beside each; NOT merged into key.tsv by this job (rule 3 per-unit clause).
  A keyed code reading a different gloss value in a span where all other codes match is a rule-4 conflict, logged in HYPOTHESES.md.
- On FAIL: no candidate list; the leaf is logged as a FAIL with both numbers.
