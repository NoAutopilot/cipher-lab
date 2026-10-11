# TXE2-PAIR X2 (and X2b) -- RESCORE (11 Oct 2026, 18:0x UTC by date -u)

**Measurement correction: box-to-position map fixed (off by one), not a new gate look.** Dev only, as the original runs; no eval file
written.

Job BOXMAP-RESCORE (others) for the account-3 parent (session_0198Cv8ypBfBVfRToKVWx33M). Script-only: no vision call, no reader, no
image viewed, no network beyond git. No truth file or BENCHMARK-TX.tsv row edited.

`tools/tx_pair_clf.py` applies (X2, X2b) and trains (X2b) at no.87 positions through `--map`, default `atlas/no87_box_token.tsv`, which
is one token off on 10 of 26 lines, 4 of them on dev_tune (f178v L06, L07, L09, L11; `ciphers/nevers-birago-fr3251-1572/atlas/RESCORE.md`).
**Only `--map` changed** (to `atlas/no87_box_token_labelaware.tsv`): `sh benchmark-tx/txeng2/pair/rescore_boxmapLA/run.sh` (outputs in
`rescore_boxmapLA/` here and in `../pair2/rescore_boxmapLA/`). With the old map the same commands reproduce all 30 committed files byte
for byte. Scored paired vs `units/labels_dev_tune.tsv`, as measured (flagged excluded gives the same fixed/broken here).

| output | before: considered, changed, fixed / broken, p | **after** |
|---|---|---|
| **X2 real** (secure-tile training) | 119, 13, **1 / 11**, 0.0063 (against) | 115, 9, **2 / 6**, 0.29 |
| X2 ctrl seeds 1-5 | 0-3 / 13-30, all p < 0.001 | 0-3 / 11-27, all p <= 0.006 |
| **X2b real** (dev_tune LOLO) | 71, 4, **3 / 0**, 0.25 | 70, 5, **3 / 1**, 0.63 |
| X2b ctrl seeds 1-5 | 2-4 / 26-31 | 1-4 / 17-29 |

X2: the before and after outputs differ at 8 positions, all on the shifted lines (f178v L09.14, L09.17, L09.21, L09.27, L11.16,
L11.26, L11.28, L11.29). X2b: the training tiles move with the map, so the per-fold thresholds move too (T76/T86 in one fold:
t 0.9 -> 0.4); the new break is f178v L10.14 T60 -> T86 on an untouched line, and L05.1 / L10.4 flip to the other e-homophone (still
fixes).

**Does the conclusion change?** No, for both gates. X2's dev gate (fixed > broken, p < 0.05) still FAILs; "of 13 disagreements with L,
L was right on 11" becomes 6 of 9 with the right tiles, and "the real classifier breaks fewer than every shuffled control (11 vs 13-30)"
holds (6 vs 11-27). X2b still FAILs (3 / 1); its reading "fixed 3 and broke none" becomes "fixed 3, broke 1"; "the labels carry the
signal" (permuted controls break 17-29) and "the gate is not reachable at this N" stand.
