# PREREG-MANT0490 (9 Oct 2026, 18:3x UTC by date -u, written while the three blind passes were still running: before any pass result was read and before any score; LANE FAMILY-A2k account 2)

Leaf: HStA Dresden 10026 Loc. 694/08, film frame 0490 (fullsize 0490.jpg, one GET 9 Oct 2026 18:27 UTC; the film card reads "Aufnahme
Einheit 0491", "beschaedigt" tag), 4339x3865, sha256 prefix c60a2ad6ca891c02 (= mant0608/inv08g.tsv row), page no. 392 (right page),
Manteuffel to Flemming; between 0489 (stamp 391, Berl. 15 Nov 1712) and 0496 (page 397, 20 Nov 1712), so mid-November 1712.
Premise (before this file): Acta Borussica, Behoerdenorganisation I (1894), IA diebehrdenorgan01posngoog _djvu.txt (1 GET, 9 Oct 2026):
the only Manteuffel report printed for November 1712 is Nr. 82, "Berlin 23. November 1712" (p.285; Dhona, the Prince Royal, Ilgen); no
15-20 Nov report is printed or paraphrased (Nr. 72 = 9 Sept/7 and 23 Oct, Nr. 83 = 3 and 9 Dec). So the leaf's only known answer is its
own interlinear gloss. A key test, not a reading.
Question: does key.tsv (origin/main dfd0701d2) read this leaf's glossed code runs the way the leaf's own interlinear period gloss reads them?

Token count on the image before planning (worker eye, 18:28 UTC): right page about 147 code tokens in 17 code lines; left page about 60-90
more plus a vertical run in the gutter margin. Over ~120 for the leaf, so per the brief ONE page only is read: the right page (more tokens,
denser gloss). The left page and the gutter run are not read in this job (named as next).

Protocol = PREREG-MANT0474 / PREREG-MANT0136B exactly, with these inputs:
- codes: two blind Sonnet passes over the 17 right-page code-line crops f0490_08/crops/c0490R01..R17_L01.jpg (one call per pass, one page;
  pass B in reverse order) -> passA.tsv, passB.tsv; reconciled by this worker from the image where they disagree -> f0490_08/ciphertext.tsv,
  before any gloss is attached to codes and before any score. Disclosure: this worker has seen key.tsv's values, MANT-0494/0474/0136B's
  results and the leaf's glosses at sight scale; digits are settled from the image, never from key values; doubtful ones marked low.
- gloss: ONE blind Sonnet gloss pass (gloss.tsv; V-BRANDT rule), over g0490R01..R17 strips plus the code crops' top edges, used exactly as
  that pass wrote it (letters only; '?' letters dropped); this worker does not correct, complete or settle any gloss word. A crop the pass
  marks NONE has no gloss span.
- spans: f0490_08/gloss_spans.tsv, one row per gloss note, with the code tokens it sits over, set by physical position (the pass's x extents
  and this worker's eye on the image), never by what a decode would need; a note whose codes cannot be placed is left out and listed.
  Where one note sits over a whole run, the span is the whole run.
- The R01 line: the strip above the first code line carries a full line of writing ('la paix ...' at sight) in a hand near main-text size.
  Whether it is a gloss of R01+R02 or main text is not settled here. It is EXCLUDED from the deciding row; a second row including it as one
  span over the R01+R02 code (if the gloss pass reports it as sitting over the numbers) is reported only.

Statistic S: exactly f0136_08/gloss_gate.py's (= f0474_08's), copied as f0490_08/gloss_gate.py, seed 490. Name codes whose key value is a
whole word or name (160 Manteuffel, 257 Le roi de Prusse, 288 Mecklenbourg, 120 d, ...) match only when the gloss spells that whole value;
an abbreviated gloss ('mant', 'Roy de Prusse' vs 'Le roi de Prusse') scores a miss: S is a lower bound.
Control (rule 3): key.tsv values permuted over its codes, 1000 draws, seed 490, same spans and alignment (the permutation changes the
value-to-code assignment, which is what S measures: the control can differ from the target).
Gate: deciding row = right page, R01 line excluded. PASS if S > p99 AND S >= 0.5 x keyed code tokens in spans; fewer than 10 keyed tokens
= too short (neither). A span's codes are grade C only if the deciding row PASSes; everything else M (or S under gate (b)).
Cross-witness (descriptive, no gate) -> f0490_08/candidates.tsv, never key.tsv: codes outside key.tsv; codes > 401; the held codes 321, 191,
254, 199, 42 and MANT-0494's 231-715 if present; rule-4 conflicts at any keyed code whose slot disagrees with its gloss letters.
Gate (b) (unglossed run >= 15 tokens, e.g. R01+R02 if the R01 line is not a gloss): exactly f0474_08/judge_gate.py (fr18, permuted-key,
power >= 0.80) at its N, copied with seed 490; run only if under 80% of the cap after gate (a); if it decodes to a gloss phrase, say so.
Script: f0490_08/gloss_gate.py (writes gate.out; --check exits 1 if stale).
