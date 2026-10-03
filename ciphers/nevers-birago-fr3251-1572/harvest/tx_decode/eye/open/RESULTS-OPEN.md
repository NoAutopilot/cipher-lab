# BIR-OPEN results (3 Oct 2026, account-3 worker)

Pre-registration `PREREG-OPEN.md` + `prereg_open.py`, `score_open.py`, `oposnull.py` pushed at e5076ee1 before any crop or score.

## Crops (scratchpad only; commands run before the first reader call, 13:0x UTC)
    S=<scratchpad>/crops
    python3 tools/iiif_lines.py --image ciphers/birago-fr3252-1571-72/images/f117/src_ark_12148_btv1b9060232m_f118_4380_1400_3150_1300.jpg --out $S/f117 --prefix f117 --centres 103,223,347,462,580,702,815,944,1062,1210 --max-width 1100 --overlap 60 --top-margin 15 --bottom-margin 45 --debug
    python3 tools/iiif_lines.py --image ciphers/nevers-birago-fr3251-1572/harvest/f168r/src_ark_12148_btv1b9060248g_f171_4600_2560_3500_480.jpg --out $S/f168r --prefix f168r --max-width 1250 --overlap 50 --debug
    python3 tools/iiif_lines.py --image ciphers/nevers-birago-fr3251-1572/harvest/f168v/src_ark_12148_btv1b9060248g_f172_1650_700_2750_650.jpg --out $S/f168v --prefix f168v --max-width 1250 --overlap 50 --debug
f117: 30 crops (10 lines x 3 segments); f168r 12 (4 x 3); f168v 9 (3 x 3). Passage R0n = f168r_L0n, V0n = f168v_L0n.

## Readers (3 vision calls, one fresh blind Opus subagent per part, 13:01-13:04 UTC; 0 reconciliation calls; 0 network requests)
Answers `oanswers_<part>.tsv`: f117a 80 rows (H 33 M 43 L 4, OTHER 1: a plain "8"), f117b 68 (H 36 M 24 L 8, OTHER 1: triangle on a crossed
stem, "T84 upside down"), f168 44 (H 30 M 13 L 1). The readers split T86/T60 by crossbar count (one = T86, two = T60) and T51/T95 by crossbar length.

## Gates (`score_open.py`, `oscore.json`; posnull `oposnull.json`, 51 s)
| leaf | H-decoy calibration (gate >= 0.80) | targets: same / other sheet sign / OTHER-U | lattice picks the reader's new sign (H/M) | posnull | new S candidates |
|---|---|---|---|---|---|
| f.117r | 70/74 = 0.946 PASS | 31 / 41 / 2 (change rate 0.55) | 25 (24) | PASS: rank 1/201, S -1.065 vs p95 -1.476, z 4.88 | **12** |
| f.168 | 22/22 = 1.00 PASS | 10 / 12 / 0 (0.55) | 7 (6) | PASS: rank 1/201, S -1.036 vs p95 -1.392, z 3.25 | **4** |
Per-sign calibration where the changes fall: H decoys at T60 read T60 9/10 (f.117r) and 2/2 (f.168), T65 5/5, T98 15/15. The 4 f.117r decoy
misses were T83->T81, T66->T76, T60->T86, T76->T66. Baseline lattice (same candidates without the reader's answer) already picks the reader's sign at 13 / 5 of the 41 / 12 changes.

**Deviation (post-hoc, logged before the decode was run):** the 'M' targets included every A1-BIR-VERIFY exception position (19 on f.117r, 5 on f.168).
decode_key.py demotes an exception to M when the transcription row's conf is M, so those positions still read M. `score_open.py` was patched so
they are not re-added. They are reported instead (`already_exception` in oscore.json) as independent open-choice replications of A1's A/B reads:
- f.117r: 11 of 19 the same sign (T86 x6, T95, T18, T90, T13, T83). 8 conflict: T95->T51 x5 (L04:6, L05:2, L07:21, L09:11, L09:30), T66->T76 (L05:27), X_NEW->T84 (L03:27), T13->T64 (L06:23, L).
- f.168: 2 of 5 the same (T17 x2). 3 conflict: T83->T24 (R03:4, V01:10), T51->T95 (V03:10).
A1's binary reads could not offer T51 where they chose between T65 and T95, so the **T65/T95/T51 three-way is unsettled**. The A1 exceptions are
left unchanged here. The conflicts go to the owner's sorter, not settled by majority.

## Kept (`exceptions_open_<leaf>.tsv` = A1's rows + these, reason "BIR-OPEN kept")
- f.117r 12 (5+5+1+1): T60->T86 x5 (L02:3, L03:11, L06:21, L09:17, L10:7), T65->T51 x5 (L03:10, L05:18, L06:13, L08:23, L09:20), T95->T51 (L02:1), T98->T18 (L05:16, H).
- f.168 4: T60->T86 (R02:34, V02:30 H), T56->T97 (R03:17 H), T19->T33 (V03:14 H).
6 of the 12 f.117r survivors are T65->T51 or T95->T51, the signs the conflicts above show unsettled: weigh them below the T60->T86 and H ones.

## Decode and judge
    $ python3 tools/decode_key.py ciphers/nevers-birago-fr3251-1572 --config ciphers/nevers-birago-fr3251-1572/harvest/tx_decode/eye/open/decode_open.json --check
    harvest/tx_decode/eye/verify/ciphertext_f117_top1.tsv: tokens 279: M 74, S 179, U 26
    harvest/tx_decode/eye/verify/ciphertext_f168_top1.tsv: tokens 122: M 22, S 90, U 10
    harvest/ciphertext_f144r.tsv: tokens 90: M 36, S 40, U 14
    reading up to date   (exit 0)
**Grades do not move.** The 16 new values, like A1's 24, sit on rows whose transcription conf is M, and decode_key.py grades an exception on such a row M.
The "applied at S" wording in A1-BIR-VERIFY's results is therefore a value change at S-candidate level, not an S grade in the tokens file. Flagged for the
orchestrator: an open-read survivor would need its ciphertext conf raised, or a grade override, for the tool to show S. That is not done here.
Judge (letters only, brackets and separators stripped; the same extraction for before and after):
    f.117r (specs/birago-fr3252-f117.json)  before (verify) FAIL language: score=-1.301, null_p99=-1.813, real_p05=-0.899, N=246
                                             after (open)    FAIL language: score=-1.224, null_p99=-1.813, real_p05=-0.899, real_median=-0.782, N=246
    f.168  (specs/nevers-birago-fr3251-1572.json) before FAIL language: score=-1.242, null_p99=-1.622, real_p05=-0.992, N=111
                                             after (open)    FAIL language: score=-1.15, null_p99=-1.622, real_p05=-0.992, real_median=-0.824, N=111
The gain is partly circular, because the lattice uses the same kind of LM. FAIL on both. No reading claimed, H 0 C 0, no novelty classed.
