# PREREG-VIV52O (13 Oct 2026, VIV52-O worker for LANE DEFAULT-A1-0640, owner account)

Written and pushed BEFORE the blind passes of fr.16104 ff.164r-164v (ink 52, Vivonne to the Queen, 5 Sept 1572) have returned and before any
decode of this letter exists. No interlinear words were seen on c178-c183 at 1200 px nor on the native regions of f.164r/f.164v (debug overlays),
so the gloss check does not apply: the order gate b2 and the wrong-key gate, as N6-VIV63 / VIV-ANCHOR ran them.

Inputs, frozen when the passes land: tx/f164r|f164v_pass{A,B}.tsv (two blind Sonnet passes per page, crop paths only, prompt = SIGNS.md as
N6-VIV63), tx/viv63_clean.py (unchanged), tools/reconcile_passes.py, then tx/viv52_decode.py = tx/viv63_decode.py's code path with the inherited
label rules only (reconcile_vivk RULES + RULES54 + RULES63; no rule added after seeing a decode -- any eye-settled split rule is written into
viv52_decode.py and committed before its first decode run). key.tsv as on main (Tomokiyo's published values + VIV-ANCHOR's V -> n, grade C).
Scorer = tools/judge_plaintext.py NgramModel on the fr16 corpus (tx/viv63_test.FR16), used RELATIVE to nulls of the same decode.
Seed '20261013VIV52O' for every null; 200 draws; 200 wrong keys.

Statistics (tx/viv52_test.py):
- b2, order beyond frequency: s = mean log10 4-gram prob per letter of the key.tsv decode of f.164r+f.164v; null = 200 letter-order shuffles of
  the same decode. PASS iff s > null p99. Gate only if both positive controls (C1 f.103r = tx/f103r_rec.tsv, C2 ink 54 = f173r+f173v) pass b2
  against their own nulls with headroom (s - p99 > 0.01 and null median < s); otherwise "not a gate".
- c, wrong-key specificity: 200 value-shuffled keys, each run through b2 as the target; real margin (s - b2 p99) must exceed the p99 of the
  200 wrong-key margins. The wrong keys change the letters, so this null can differ from the target on the statistic (rule 3).
- Descriptive, no gate: b1 (shuffled-key null), per-page b2, the same decode under key_tomokiyo.tsv (no V row), the fr16 judge
  (tools/judge_plaintext.py) pasted, longest H run, H/M/U counts.
Expected depth stated before reading: D1 (inks 53, 54 and 63 under the same pipeline and key all hold D1 in AUDIT.md; nothing settles the f/m/p and
qu key questions first). "Ready for audit 1" is licensed only if b2 is a gate and passes AND c passes.
