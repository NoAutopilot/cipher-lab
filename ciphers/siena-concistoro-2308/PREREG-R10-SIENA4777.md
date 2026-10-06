# PREREG R10-SIENA4777 -- no. 15 against key R4777 through a shape concordance (6 Oct 2026, written 10:0x UTC by date -u, pushed before the R4777 image was fetched or viewed this session)

Question: is DECODE R4777 (letter alphabet + Doppie + Nulle; nomenclator Granvelle, Cobos, Don Pedro de Toledo, Card. Farnese,
Marchese del Vasto, Duca d'Amalfi, Principe d'Oria; R10-SIENA15 "partial overlap" 2 of 4) the key of no. 15 (R4803, Mario Bandini,
Dec 1546 / Jan 1547)?

Identical to PREREG-R9-SIENA15.md except the key sheet and the concordance file. Fixed now:
- Tokens: `transcripts/no15.tok` (232 sign tokens, clear text as "|").
- Concordance: `concordance_R4777_no15.tsv`, written from native crops of R4777's alphabet, Doppie and Nulle rows and the no. 15 legend
  (Bourdeau no15v.txt) BEFORE any scoring; set P = shape plainly the same sign, set V = P plus looser likenesses (V rows replace P rows
  for the same sign). Value `&` scored as "et"; doppie values as the doubled pair. Nomenclator cells are not used (no. 15's codes are
  not compared; letters only).
- Statistic S2, controls, gate and validity exactly as R9-SIENA15: S2 = mean it16 bigram log10 probability inside maximal valued
  stretches (nulls dropped; "|" and unvalued signs break); (a) 2000 value-shuffled keys, (b) 200 order-shuffled streams; PASS iff
  p_a <= 0.05 AND real S2 > p95(b). Positive control: 100 it16 passages enciphered under "R4777 is the key" at the target's own valued
  count (q tuned), null rate r = (target's null tokens under that variant)/(232 - that count); power < 0.8 means the variant's miss is a
  NON-TEST at this N, not a negative.
- Coverage floor (R10-SIENA15's own condition): a variant whose concordance values fewer than 100 of the 232 tokens is still scored and
  reported, but its outcome cannot be logged as a negative unless power >= 0.8 (the same rule; stated so it is not read as a new gate).
- If PASS (either variant, power >= 0.8): the decode under that variant is written at grade M only and sent to
  `tools/judge_plaintext.py` (it16); no key.tsv, no reading claim. If FAIL: no. 15 stays too-short / no-key-material.
Script: specs/cheap-tests/siena-concistoro-2308/run_test_no15_r4777.py (seeded, reuses run_test_no15.py's functions; `--check`).
