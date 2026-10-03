# READ2-HEL2 pre-registration (3 Oct 2026, 23:4x UTC, written and pushed before any look at the R4370 images)

Target: R1953 (4 Jan 1752) tokens at codes 1-800, the ones R4369 (codes 801-1796) cannot reach. By `ciphertext_R1953.txt`
(DECODE's transcription, rule 2) that is 349 numeric tokens on 201 distinct codes; the brief's 374 U also counts empty
key cells and non-numeric tokens. Candidate key: DECODE R4370 (BL Add MS 32276 f.46, 1751, no named holder).

1. Transcription: P2 and P3 (P1, P4 looked at, contact size, first; a page with no entries is skipped). Column crops with
   `tools/iiif_lines.py --image` before any subagent call; two blind Sonnet passes per page; code-keyed diff; reconciliation of
   disagreements from a strip montage only. err_2reader reported. `key.tsv` = code, left, right, grade_left, grade_right, page.
2. Attributions tested (k = 4), built by `build_keys.py` exactly as `key_r4369/build_keys.py`: L (left meanings), R0 (right
   entry -> its own row's code), R100 (right entry -> code + 100, the next block's same row), LR100 (L plus R100, R100 winning).
   If the sheet's layout has no right entries, only L is tested and k = 1. If its block size is not 100, R100 is replaced by
   R+block (the code on the same row of the next block) and named so; nothing else changes.
3. Gate A (range): report the code range carried and its overlap with R4369 (801-1796). Codes 801+ on R4370 that also appear on
   R4369 with different meanings make it a rival key, not a half: record, and test the full R4370 key on R1953 as a rival too
   (same statistics, both numbers), outside the k = 4 family.
4. Gate B (coverage): the main test key is each attribution restricted to codes 1-800. If L (or the best-covering attribution)
   covers fewer than 113 R1953 tokens (30% of 374), stop after transcription and record coverage -- a finding, not a negative.
5. Test: `sibling_michell/test_sibling.py --key <key> --out <file>` (seed 1), on R1953 (the other letters' rows reported, not
   gated). Statistics: uni (mean fr18 word log-prob of covered tokens) vs 200 value-shuffled keys; bi (mean fr18 junction PMI
   of adjacent covered pairs) vs 200 value shuffles and 200 token-order shuffles; positive-control power at the covered count.
   **Pass** for an attribution = uni value-shuffle p <= 0.05/k AND bi order-shuffle p <= 0.05/k (0.0125 at k = 4) AND power
   uni and bi >= 0.8. Seed 2 re-run of any passing attribution must also pass. Nothing here changes after the first look.
6. On a pass: merge (R4370 1-800 + R4369 LR100 801+) into `../key_hellen1751/`, whole-letter test, judge with calibration
   re-run. On a fail: target and control numbers side by side; R4369's result stands unchanged.
