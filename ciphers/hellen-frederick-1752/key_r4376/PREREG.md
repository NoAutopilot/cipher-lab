# N6-HEL76 pre-registration (4 Oct 2026, 10:2x UTC, written and pushed before the R4376 image is fetched or read)

Target: R1049 (7 Sept 1756), `ciphertext_R1049.txt` (DECODE's transcription, rule 2: a negative is conditional on it). 506 numeric
tokens: 178 at codes 1-500, 211 at 1-600, 230 above 800. R4369 (the 1751-52 Hellen key, 801-1796) does not read R1049 (LR100 uni p
0.665, bi order p 0.545, power 1.00), so R1049 is not assumed to be in the R4369 series. Candidate key: DECODE R4376 (BL Add MS 32276
f.56; P1 docket "1754", P2 a blank ruled form, P3 a filled French table of codes 1-500 with "zero" nulls, "la Haye", "pays bas", no
holder named; NEAR3-HEL3). R4370 and R4372 are not candidates (retired, LANE-NEAR5 refresh); R4372's secondary R1049 row is not used.
Method copied from `../key_r4372/PREREG.md` with R4376 P3 in place of R4372 P2/P3 and R1049 in place of R1953.

1. Transcription: P3 only (P2 is blank, P1 the docket). Column crops with `tools/iiif_lines.py --image` before any subagent call;
   two blind Sonnet passes; code-keyed diff (letters only); reconciliation of disagreements from crops/montages (my own reads).
   err_2reader reported. `key.tsv` = code, left, right, grade_left, grade_right, page; conventions as `../key_r4372/README.md`.
2. Attributions (k = 4, built as `../key_r4372/build_keys.py`): L, R0, R100, LR100. If P3 has no right entries, only L (k = 1).
   If the block size is not 100, R100 becomes R+block and is named so. No range restriction (the sheet carries what it carries).
3. Nulls: cells reading "zero" are nulls, not words. They are dropped from the gated keys (N4-HEL6: the word statistics score "zero"
   as a rare or out-of-vocabulary word, which biases both statistics); the same keys with "zero" kept are reported, not gated.
4. Gate B (coverage): if the best-covering attribution covers fewer than 54 R1049 tokens (30% of the 178 at 1-500), stop after
   transcription and record coverage -- a finding, not a negative.
5. Test: `sibling_michell/test_sibling.py --key <key> --out <file> --oov-floor` (seed 1). uni = mean fr18 word log-prob of covered
   tokens vs 200 value-shuffled keys; bi = mean junction PMI of adjacent covered pairs, with an out-of-vocabulary left word scored at
   the unseen floor (N5-HEL7's `oov_floor=True`; the option is added to `--key` mode before any run, default unchanged), vs 200 value
   shuffles and 200 token-order shuffles of R1049. Matched positive control (rule 3, last paragraph): windows of real fr18 prose
   encoded with this very key, subsampled to R1049's own covered count (uni) and own adjacent-pair count (bi), 200 draws; power =
   share reaching p <= 0.05. **Pass** for an attribution = uni value-shuffle p <= 0.0125 AND bi order-shuffle p <= 0.0125 (0.05/k,
   k = 4) AND power uni and bi >= 0.8, and the same at seed 2. If bi power < 0.8 (too few adjacent pairs), the attribution cannot
   pass and the row is "underpowered", not a negative. Other letters (R1953, R1045-R1048, R1060, R1061) reported, not gated.
6. On a pass: `decode.json` + `key_decode.tsv` and a partial reading of R1049 via `tools/decode_key.py --check` (exit 0) in
   `key_r4376/`, grades H for read cells (M for doubtful), judge pasted. On a fail: target and control numbers side by side.
Nothing here changes after the first look.
