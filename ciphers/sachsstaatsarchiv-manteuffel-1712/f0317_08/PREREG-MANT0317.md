# PREREG-MANT0317 (9 Oct 2026, 19:0x UTC by date -u, written before any reading pass was run and before any score; LANE FAMILY-A2k account 2)

Leaf: HStA Dresden 10026 Loc. 694/08, film frame **0317** (stamp 246, dated "Berl. ce 17 Sept. 1712"; fullsize 4333x3871, sha256 prefix
4ddbd09a8a6b877d = inv08f.tsv; film card "Aufnahme Einheit 0318"). One GET, 9 Oct 2026 19:0x UTC. Code on the right page only (left page
blank). Manteuffel to Flemming.
Premise (brief): does 0317 continue the 16 Sept pack (0309 covering dispatch + 0312/0314 Extrait)? Worker eye on the native image, before any
pass: **no** -- it is a separate dispatch of the next day, with its own date line and opening ("J'ai l'honneur de dire en peu de mots a V.E. que
je reviens en ce moment de Charlottenbourg ou [..] le bar. d'I. m'a dit que le C[zar] devoit notifier a cette cour qu'il feroit un voyage
pour voir les frontieres de la Pomeranie ..."), numbered paragraphs 1-4; none of 0309's names (Stanislas,
Arnhold, Jablonski, Razrozewski) is visible in clear or gloss at native scale. Prior work and print (checks 1-4) in NOTES.md MANT-0317
section; Acta Borussica BO I Nr. 72 prints Manteuffel reports of 4, 7 and 23 Oct 1712, none of 17 Sept. This is a key test, not a reading.
Question: does key.tsv (origin/main at this commit) read this leaf's code runs the way its own interlinear period gloss reads them?

Token count on the image before planning (worker eye): about **37 code tokens in 11 runs** (5 multi-code runs: R02 6, R03 8, R04 6, R05 4,
R11 7 = 31; 6 single-code runs: R01, R06, R07, R08, R09, R10). Run boxes: f0317_08/runs.tsv (set by eye from tick-labelled native windows).
Crops (committed, f0317_08/crops; f0317_08/make_crops.sh, tools/iiif_lines.py per run, unchanged from f0309_08: code strip
`--region x0-20,yc-30,x1-x0+40,64 --centres 32`, gloss strip `--region x0-120,yg-26,x1-x0+240,50 --centres 25`, `--debug`). Some code
strips carry a gloss word at their top edge (R03, R05, R06, R07) -- the gloss sits ~30-35 px above the code; the code passes are told to read
digits only. Strip sheets: f0317_08/sheet.py (code/gloss, run order and reverse).

Passes (blind Sonnet subagents; strips only, never the page; one stacked sheet per call):
- codes: pass A (sheet_c_fwd) and pass B (sheet_c_rev) -> passA.tsv, passB.tsv; reconciled by this worker from the image where they disagree ->
  ciphertext.tsv BEFORE any span is attached and before any score. Disclosure: this worker has seen key.tsv (values of the codes it expects
  here), MANT-0309/MANT-XTR results and the glosses at native scale while cutting crops; digits are settled from the image, never from key
  values; doubtful ones marked med/low.
- gloss: TWO blind gloss passes (V-BRANDT rule): G1 (sheet_g_fwd) and G2 (sheet_g_rev) -> gloss1.tsv, gloss2.tsv, used exactly as written
  (letters only; '?' dropped); this worker does not correct, complete or settle any gloss word. Deciding pass G1; a row PASSes for grading
  only if it PASSes under both passes.
- spans: one span per glossed run.

Statistic and gate: exactly f0309_08/gloss_gate.py (= f0314_08's, MANT-XTR) -- row (a) letter runs (>= 2 codes, 0474 alignment), row (n)
single-code name runs (abbreviation-prefix rule), row (a-all) continuity only; control: key values permuted over codes, 1000 draws,
**seed 317**. Gate per row: PASS if S > p99 AND S >= 0.5 x keyed tokens; < 10 keyed = too short (neither). This leaf alone (no pooling).
Expected: row (a) about 31 keyed (R02, R03, R04, R05, R11); row (n) 6 keyed (R01 and R10 177, R06 292, R07 150, R08 8, R09 170) -> too short
by construction, reported per span only. The control permutes the value-to-code assignment, which is exactly what S measures, so it can
differ from the target (rule 3).
Known limits stated now: 103 (le|la), 60 (r|re|ro), 51 (s|sa), 55 (b|[a]), 15 (c) are M in key.tsv; their row (a) matches are reported per
span but a C grade on this leaf does not upgrade their key grade (one leaf, no gate on the code alone). 8 is a letter code ('h'); a gloss name
over a single 8 is scored by row (n)'s prefix rule (h ~ H.) and reported as usage, not as a key test. 170 ('le', example word 'Roi'): whatever
its gloss reads is a cross-witness in candidates.tsv, not a key change.
Grades: a span's code tokens C only if matched under a row that PASSes for both gloss passes; everything else M. H 0.
Cross-witness (descriptive, no gate) -> f0317_08/candidates.tsv, never key.tsv: codes outside key.tsv; codes > 401; MANT-0494's held 231-715;
V-MANTH's held 321 191 254 199 42; 259; rule-4 conflicts at keyed codes; single-code glosses that disagree with the key value. key.tsv not
changed above M without a passed gate.
Gate (b) (unglossed run >= 15): none expected; not run if none.
