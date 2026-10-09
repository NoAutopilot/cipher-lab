# PREREG-MANTXTR (9 Oct 2026, 16:4x UTC by date -u, written before any pass was run and before any score; LANE FAMILY-A2j account 2)

Leaves: HStA Dresden 10026 Loc. 694/08, film frames **0314** (stamp 244, "Extrait de la resolution que [198] a donnee a [66.60.21.8.33.12.120]",
foot "a la lettre de Mantf. du 16 Septb. 1712"; fullsize 4339x3865, sha256 prefix 862a7a715dd6b2c7 = inv08f.tsv; film card "Aufnahme Einheit
0315") and **0312** (stamp 242, "Extrait de la relation de [66.60.21.16.12.120]", foot "a la lettre Mantf. du 16 7bre 1712"; 4339x3865,
7fd64420ed115686 = inv08f.tsv; card 0313). One GET each, 9 Oct 2026 16:3x UTC. Manteuffel to Flemming, enclosures of 16 Sept 1712.
Only the right page of each frame carries code (0312's left page is a clear note; 0314's left page is blank/bleed-through).
Premise (check 1): never worked in this folder (only MANT-CEN3's inventory rows). Checks 3-4 (print) in NOTES.md MANT-XTR section, run
before scoring; whatever they find, this is a key test, not a reading.
Question: does key.tsv (origin/main at this commit) read these two leaves' code runs the way their own interlinear period gloss reads them?

Token count on the image before planning (worker eye, 16:4x UTC): 0314 about 45 code tokens in 21 runs; 0312 about 46 in 25 runs; together
about 91 (< 150: both leaves done, 0314 first). Run positions: f0314_08/runs.tsv, f0312_08/runs.tsv (by eye on a gridded native view).
Crops (committed): one `tools/iiif_lines.py --image <frame>.jpg --region x0-20,yc-24,w,64 --centres 32` per run (code strip) and one
`--region x0-60,yg-28,x1-x0+300,54 --centres 27` (gloss strip). Code strips may carry gloss ink at the top edge; readers are told to skip it.

Passes (all blind Sonnet subagents, one leaf per call; the strips of one leaf stacked as one labelled sheet, strips only, never the page):
- codes: pass A (sheet in run order) and pass B (reverse order) per leaf -> f03NN_08/passA.tsv, passB.tsv. Reconciled by this worker from the
  image where they disagree -> f03NN_08/ciphertext.tsv, BEFORE any span is attached and before any score. Disclosure: this worker has seen
  key.tsv and the glosses at preview scale; digits are settled from the image, never from key values; doubtful ones marked low.
- gloss: TWO blind gloss passes per leaf (V-BRANDT rule): G1 run order, G2 reverse order -> gloss1.tsv, gloss2.tsv, used exactly as written
  (letters only; '?' letters dropped); this worker does not correct, complete or settle any gloss word. Every row below is scored once per
  gloss pass; the pass-G1 score is the deciding one, G2 is reported beside it (a row PASSes for grading only if it PASSes under BOTH passes).
- spans: one span per run that the gloss pass glosses (a run's notes joined in order); a run the pass marks NONE has no span.

Statistic S (row a): exactly f0474_08/gloss_gate.py's (copied, seed 312; alignment, scores and control unchanged).
Row split, fixed now by run type from runs.tsv before any score (lesson PX-BRODEC: the glosses abbreviate the name codes -- 'Stan' for 198
Stanislas, 'R. de Pr' for 257 Le roi de Prusse -- and S scores a whole-word key value only against the whole word, so pooling the single-code
name runs into row (a) would measure notation, not the key):
- **row (a) letter runs**: spans whose run has >= 2 code tokens; S as 0474. Per leaf and pooled; **pooled is the deciding row** for the
  tokens in those spans.
- **row (n) name runs**: spans whose run has exactly 1 code token. Match rule (stated now): gloss and key value are split into words
  (letters() per word, after 0474's normalisation incl. roy->roi); articles le/la/les/l dropped from both; the code matches if the gloss
  words are non-empty and each is a prefix of a distinct value word, in order, the first gloss word on the first value word (any '|'
  alternative). S_n = matched single codes. Same control (values permuted over codes, 1000 draws, seed 312). Per leaf and pooled;
  pooled is the deciding row for the single-code tokens.
- row (a-all): all spans with 0474's statistic, reported for continuity with 0474/0494/0136B, not deciding.
Gate for every row: PASS if S > p99 of the control AND S >= 0.5 x keyed code tokens in the row's spans; fewer than 10 keyed tokens = too
short (neither). The control permutes the value-to-code assignment, which is exactly what S measures, so it can differ from the target.
Grades: a span's code tokens are C only if matched under a row that PASSes for both gloss passes; everything else M. H 0.
Cross-witness (descriptive, no gate) -> f03NN_08/candidates.tsv, never key.tsv: codes outside key.tsv (expected 321 'Stockholm', 177's
gloss 'Czar' is keyed), codes > 401, MANT-0494's held 231-715, 191 (key 'Stenbock', M) against its gloss, and rule-4 conflicts at any keyed
code whose slot disagrees with its gloss. key.tsv is not changed above M without a passed gate.
Gate (b) (unglossed run >= 15 tokens): none expected (0312's title run 66.60.21.16.12.120 is 6 tokens); not run if none.
