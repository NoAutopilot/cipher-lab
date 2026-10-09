# PREREG-MANT0089 (9 Oct 2026, ~15:35 UTC by date -u, written before any score was computed; LANE FAMILY-A2j account 2)

Leaf: HStA Dresden 10026 Loc. 694/08, frame 0089 (fullsize 0089.jpg, one GET 9 Oct 2026 15:22 UTC; film card "Aufnahme Einheit 0090"),
4351x3855, sha256 prefix 09c68185e455bd65 (= MANT-CENSUS inv08d.tsv row), stamp 66, Manteuffel to Flemming. By position the continuation of
0088 (stamp 65, No. 35, "Berl. ce 31 May 1712"). The leaf is mostly clear text; code: 27 tokens in 11 short runs (not the inventory's
100-140), glosses over 5 runs read by the blind gloss pass.
Question: does key.tsv (origin/main 0dfc9a23c) read the glossed runs the way the leaf's own interlinear gloss reads them?

Protocol = PREREG-MANT0474 exactly, with these inputs:
- codes: two blind Sonnet passes (passA.tsv, passB.tsv in reverse order) over 12 run crops c0089*_L01.jpg; reconciled by this worker ->
  ciphertext.tsv (27 tokens). Disclosure: this worker had seen key.tsv and the leaf's glosses before reconciling; digits were settled from
  the image, not from key values; joined groups 1366 and 271 are kept as written (no split), 84 and 59 low.
- gloss: ONE blind Sonnet gloss pass (gloss.tsv), used exactly as written ('?' dropped). Spans gloss_spans.tsv (5 spans) set by position.
- statistic S and control exactly gloss_gate.py of f0474_08 (copied, seed 89).
Gate: per page (L, R): PASS if S > p99 and S >= 0.5 x keyed; < 10 keyed code tokens = too short. Expected before scoring: L has 5 keyed tokens,
R has 9 -> both too short by construction. Pre-registered for this leaf only: the pooled row (14 keyed) is the deciding gate, same rule;
a span's codes are grade C only if the pooled gate PASSes. If pooled is also < 10 or FAILs, every token stays M.
Cross-witness (descriptive): codes 0, 271, 1366, 84-at-gloss, 59 (key t), 85 (key st; Acta Borussica BO I p.208 paraphrases the 31 May
dispatch naming Blaspil, Creutz, Krautt) listed in candidates.tsv; never key.tsv.
