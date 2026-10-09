# PREREG WVO-1068-CONC -- does key_1068 share sign->letter values with key_1069 and with f.23's gloss key? (pushed before scoring)

WVO-1068-KEY worker, account 4, 9-10 Oct 2026 (written before the concordance call, by date -u). Same design as R9-WVOX
(../../../wvo-hessen-1564/PREREG-R9-WVOX.md), extended to a fourth inventory.
- D = 1068: `k1068_shapes.tsv` (64 classes, ids D01-D64 opaque; descriptions are the two BLIND passes' own words at the
  first occurrence, not written by this worker). Letter = key_1068.tsv value; classes with value '?' or a code word drop out.
  Labels: 'o' is a real letter in 1068 (no null mark was found), kept as 'o'.
- B = 1069 (`../../../wvo-hessen-1564/r9wvox/k1069_shapes.tsv`, letters from key_1069.tsv as score.py: 'o' -> NULL).
- A = f.23 (`../../../wvo-hessen-1564/r9wvox/f23_shapes.tsv`, letters where R9-WVOALIGN pass A and B keys agree, as score.py).
Concordance: one Sonnet subagent, text only, given ONLY the three letter-stripped files, lists every D-B and D-A pair it judges
the same written shape, confidence high/medium/low; output `concordance_1068.tsv` committed as returned.
Statistic S per key pair = high+medium pairs whose two letters are equal. Control = letters permuted within each key over its
labelled signs, 10000 draws, seed 1068; mean, p95, max reported; degenerate null (p95 = max = real) = non-test.
Gate: S_real > p95 -> PASS (shared values between the two keys; a test result, not an assumption). Reported side by side:
matched/total and p95. No key.tsv change in any folder on either outcome; HYPOTHESES.md row in willem-van-hessen-1567.
