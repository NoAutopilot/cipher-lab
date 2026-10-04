# NEAR3-HEL4 pre-registration (4 Oct 2026, 01:4x UTC, written and pushed before the R4372 images are fetched or read)

Target: R1953 (4 Jan 1752) tokens at codes 1-800, the ones R4369 (codes 801-1796) cannot reach: 349 numeric tokens by
`ciphertext_R1953.txt` (DECODE's transcription, rule 2). Candidate key: DECODE R4372 (BL Add MS 32276 f.48, undated, no named
holder; same printed form, layout and apparent hand as R4369 by NEAR3-HEL3's strip look). Identical to READ2-HEL2's
`key_r4370/PREREG.md` except for the record, and for item 6 (the combined test), which is new.

1. Transcription: P2 and P3 (P1 is blank per NEAR3-HEL3). Column crops with `tools/iiif_lines.py --image` before any subagent call;
   two blind Sonnet passes per page; code-keyed diff; reconciliation of disagreements from strip montages only. err_2reader
   reported per page. `key.tsv` = code, left, right, grade_left, grade_right, page. Conventions as `key_r4369/README.md`
   (`~` = crossed out, not used; `?` = doubtful, graded M).
2. Attributions tested (k = 4), built by `build_keys.py` exactly as `key_r4370/build_keys.py`: L (left meanings), R0 (right
   entry -> its own row's code), R100 (right entry -> code + 100), LR100 (L plus R100, R100 winning). If the sheet has no right
   entries, only L is tested and k = 1. If the block size is not 100, R100 becomes R+block and is named so.
3. Gate A (range): report the range carried and its overlap with R4369 (801-1796). Shared codes 801+ with different meanings make
   it a rival key: then the full key is also tested as a rival (outside k).
4. Gate B (coverage): each attribution restricted to codes 1-800. If the best-covering attribution covers fewer than 113 R1953
   tokens (30% of 374), stop after transcription and record coverage -- a finding, not a negative.
5. Test: `sibling_michell/test_sibling.py --key <key> --out <file>` (seed 1) on R1953 (other letters reported, not gated).
   uni (mean fr18 word log-prob of covered tokens) vs 200 value-shuffled keys; bi (mean fr18 junction PMI of adjacent covered
   pairs) vs 200 value shuffles and 200 token-order shuffles; positive-control power at the covered count.
   **Pass** for an attribution = uni value-shuffle p <= 0.0125 AND bi order-shuffle p <= 0.0125 (0.05/k, k = 4) AND power uni
   and bi >= 0.8. A passing attribution must also pass at seed 2. Nothing here changes after the first look.
6. Combined test (new): R4372 <attribution> (1-800) + R4369 LR100 (801+, `key_r4369/key_LR100.tsv`) on all of R1953, same
   statistics and controls, for each R4372 attribution. **This row is reported, not gated**: R4369 LR100 alone already passes on
   R1953 (uni p 0.000, bi order p 0.000), so a combined key passes whatever the 1-800 half holds -- its control cannot fail
   differently from the target (CLAUDE.md rule 3). It is read only alongside the 1-800 row: the gate is item 5. Reported with it,
   for scale: the combined uni real minus R4369-only uni real (a drop means the 1-800 half reads worse than the 801+ half).
7. On a pass: `../key_combined/` = R4372 passing attribution (1-800) + R4369 LR100 (801+), decode.json + key.tsv + reading via
   `tools/decode_key.py --check` (exit 0), judge pasted. On a fail: target and control numbers side by side; R4369's reading stands.
