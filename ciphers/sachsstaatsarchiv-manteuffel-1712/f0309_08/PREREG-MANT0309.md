# PREREG-MANT0309 (9 Oct 2026, 18:3x UTC by date -u, written before any reading pass was run and before any score; LANE FAMILY-A2k account 2)

Leaf: HStA Dresden 10026 Loc. 694/08, film frame **0309** (stamp 240, dated "a Berlin ce 16 Sept. 1712"; fullsize 4339x3865, sha256 prefix
26becac5ec11d3e1 = inv08f.tsv; film card "Aufnahme Einheit 0310"). One GET, 9 Oct 2026 18:2x UTC. Code on the right page only (left page blank,
bleed-through). Manteuffel to Flemming.
Premise (brief): is 0309 the covering dispatch of the 0312/0314 Extrait pair (MANT-XTR)? Worker eye on the native image, before any pass: its
opening clear text reads "Je joins ici les extraits de la resolution de [198] et de la relation de [66.60.21.33.44.120]" and its foot "2.) V. E.
trouvera peutetre les susdits extraits un peu differents de ce que [9] m'avoit dit auparavant": yes, the covering letter of those two extracts;
same codes (198 Stanislas, 66.60.21 = 'Arnh:' title runs). Prior work and print (checks 1-4) in NOTES.md MANT-0309 section; this is a key
test, not a reading.
Question: does key.tsv (origin/main at this commit) read this leaf's code runs the way its own interlinear period gloss reads them?

Token count on the image before planning (worker eye): about 48 code tokens in 16 runs (R05 continues onto the next line as R05b; one span
R05+R05b, glossed once). Run boxes: f0309_08/runs.tsv. Crops (committed, f0309_08/crops; f0309_08/make_crops.sh, tools/iiif_lines.py per run:
code strip `--region x0-20,yc-30,x1-x0+40,64 --centres 32`, gloss strip `--region x0-120,yg-26,x1-x0+240,50 --centres 25`, `--debug`).
Strip sheets: f0309_08/sheet.py (code/gloss, run order and reverse).

Passes (blind Sonnet subagents; strips only, never the page; one stacked sheet per call):
- codes: pass A (sheet_c_fwd) and pass B (sheet_c_rev) -> passA.tsv, passB.tsv; reconciled by this worker from the image where they disagree ->
  ciphertext.tsv BEFORE any span is attached and before any score. Disclosure: this worker has seen key.tsv, MANT-XTR's results and the glosses
  at native scale while cutting crops; digits are settled from the image, never from key values; doubtful ones marked low.
- gloss: TWO blind gloss passes (V-BRANDT rule): G1 (sheet_g_fwd) and G2 (sheet_g_rev) -> gloss1.tsv, gloss2.tsv, used exactly as written
  (letters only; '?' dropped); this worker does not correct, complete or settle any gloss word. Deciding pass G1; a row PASSes for grading
  only if it PASSes under both passes.
- spans: one span per glossed run (R05b's codes appended to R05's span; R05b's own strip is expected unglossed).

Statistic and gate: exactly f0314_08/gloss_gate.py (MANT-XTR) -- row (a) letter runs (>= 2 codes, 0474 alignment), row (n) single-code name
runs (abbreviation-prefix rule), row (a-all) continuity only; control: key values permuted over codes, 1000 draws, **seed 309**. Gate per row:
PASS if S > p99 AND S >= 0.5 x keyed tokens; < 10 keyed = too short (neither). This leaf alone (no pooling with 0312/0314 -- not pre-registered).
Expected: row (a) has R02 (6), R05+R05b (9), R07, R11, R12, R14 (3 each), R08 (11) = about 35 keyed; row (n) has 198 x6, 9 x3 (if the
passes read them so), and R04 257.259 is a 2-code run, so row (a). The control permutes the value-to-code assignment, which is exactly what S
measures, so it can differ from the target (rule 3).
Known limits stated now: the 9 runs are a Krauske letter code ('i', note "Ilgen"); if the gloss reads a name over a single 9, row (n) scores
it 0 against value 'i' -- that is a notation/usage difference reported in candidates.tsv, not a key test. 257 'Le roi de Prusse' and 259
'Ilgen' (M) inside R04 are scored by row (a) letters; their gloss is a cross-witness reported descriptively.
Grades: a span's code tokens C only if matched under a row that PASSes for both gloss passes; everything else M. H 0.
Cross-witness (descriptive, no gate) -> f0309_08/candidates.tsv, never key.tsv: 9 (Krauske note Ilgen) against its gloss; 259 (Ilgen, M);
codes outside key.tsv; codes > 401; MANT-0494's held 231-715; V-MANTH's held 321 191 254 199 42; rule-4 conflicts at keyed codes. key.tsv
not changed above M without a passed gate.
Gate (b) (unglossed run >= 15): none expected; not run if none.
