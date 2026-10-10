# PREREG-OBRED187 (10 Oct 2026, written before any overlap number is computed)

Question: do the numeral values of the scan-187 postscript (NA 1.01.02 inv. 6016, leaf 143r, P. Brederode, Stettin, 17 Oct 1604)
share more values with no. 92's printed groups than chance allows, given each text's own range and value histogram?
Known before writing this: the lane orchestrator's by-eye look listed ten values seen in both (M, unmeasured). This gate is built
so that a coincidental overlap of that size can fail it.

Inputs (frozen):
- V187 = distinct numeral values in `ciphertext_187.tsv` (all grades; tokens in [brackets] are text, excluded). n187 = token count.
  Sensitivity row: H-read tokens only (reported, not gating).
- V92 = distinct values of the Arabic numeral groups in `ciphertext.txt` (p.110/p.111 body only, between "Edele, erntfesten" and
  "Uyt Heydelberg"); excluded: the clear money sums "30.000", "12 off 13.000", the Roman XLII, dates, page labels and the archival line.
- Statistic S = |V187 ∩ V92|.

Controls (10,000 draws each, numpy seed 187), each able to differ from the target on S:
- C1 uniform: n187 values iid uniform on 1..M, M = max(max V187, max V92); S of the distinct set against V92.
- C2 band-matched: each 187 token replaced by a uniform value in its own hundred band (1-99, 100-199, ...), preserving 187's
  histogram shape by hundreds; S against V92.
- p = (1 + #{S_null >= S_obs}) / (1 + 10,000).
- Negatives (unrelated three-digit code texts on disk): N1 = `ciphers/lodewijk-van-nassau-1573-74/ciphertext_7206.tsv` (sign column,
  1574), N2 = `ciphers/jan-van-nassau-1572-75/ciphertext_5551.tsv` numerals (1574); 10,000 subsamples of n187 tokens without
  replacement (with replacement if the text is shorter), S against V92; report mean and 95th percentile.

Decision rule: "overlap clears its control" iff p < 0.01 under BOTH C1 and C2 AND S_obs > the 95th percentile of BOTH negatives.
If it clears: "consistent with a shared code list between no. 92 and the 1604 postscript", grade M, never a reading.
If not: "no evidence of shared values beyond range and histogram at n187". Script: `obred187/overlap.py` (`--check` re-runs
and fails if `obred187/overlap.json` is stale). No decode, no key.
