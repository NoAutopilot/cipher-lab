# BIR-OPEN-144 results (3 Oct 2026, account-3 worker)

Pre-registration `PREREG-OPEN-144.md` + `prereg_open144.py`, `score_open144.py`, `oposnull144.py`, `decode_open144.json` pushed at 88df4b16
(13:45 UTC) before any crop was cut or any score computed.

## Crops (scratchpad only; command run before the reader call)
    python3 tools/iiif_lines.py --image ciphers/nevers-birago-fr3251-1572/harvest/f144r/src_ark_12148_btv1b9060248g_f146_4350_800_3650_760.jpg --out $S/f144r --prefix f144r --max-width 1250 --overlap 50 --only-lines 3,4,5,6 --debug
12 crops; the s1 crops are byte-identical to the committed `harvest/f144r/f144r_L0n_s1.jpg`.

## Reader (1 vision call: one fresh blind Opus subagent, 13:46-13:49 UTC; 0 reconciliation calls; 0 network requests)
`oanswers_f144r.tsv`, 72 rows: H 39, M 27, L 6; no OTHER, no U.

## Gates (`oscore_f144r.json`, `oposnull_f144r.json`)
| | result |
|---|---|
| H-decoy calibration (gate >= 0.80) | 35/36 = 0.972 **PASS** (only 6/36 decoys same-sign, as pre-registered). The one miss: L04.1:7 current T60 (conf H) read T86 (H). |
| targets | 27 same / 9 other sheet sign / 0 OTHER-U (change rate 0.25) |
| lattice picks the reader's new sign | 3 (all H/M); the baseline lattice without answers already picks 2 of them |
| posnull (200 shuffles) | **PASS**: real rank 1/201, real S -1.049 vs shuffled p95 -1.239 (max -1.165), z 2.86 vs shuffled z p95 1.31; 38 s |
| survivors | 3: L05:19 T95->T51 (M), L05:26 T95->T51 (M), L04.1:12 T78->T86 (M) |

Changes the lattice did not take (stay as transcribed, M): L04.1:11 T26->T76 (L), L05:7 T36->T76, L03:8 T42->T17, L05:20 T42->T17,
L06:1 T90->T97 (L), L04.2:8 T83->T81.

## Grade policy (brief: S only where the open read agrees with A1-BIR-EYE's blind pick)
A1-BIR-EYE asked 16 of the 36 targets. The open read gives the same sign as A1-BIR-EYE at 12 of them, and differs at 4 (L05:7, L03:8, L05:12, L06:1).
- **S (2)**: L06:7 T36 and L05:32 T83. These are A1-BIR-EYE "changed" positions where A1's reader picked the lam-4 key-implied sign. The committed
  transcription already carries that sign, and the open read gives it too. The value does not change. The exception row only carries the S grade
  (`exception_grade_overrides_conf`). A1-BIR-VERIFY's matched-decoy arm failed this leaf as a whole (5/8 vs 6/12). The orchestrator's policy is what licenses these two.
  This applies the policy to "lattice sign = transcription sign" positions. The pre-registration did not spell that case out; I am logging it here, after scoring.
- The other 10 agreements are positions where both readers kept the current sign at A1 *decoys* (no lattice correction). They are left at M,
  as on f.117r/f.168, where BIR-APPLY raised only corrections.
- **M (3)**: the 3 survivors. A1-BIR-EYE did not ask any of them, so each rests on one instrument.
- **Not applied, to the sorter**: L04.1:7. Both blind instruments read T86 (A1 M, open H, as an H decoy) against the conf-H transcription T60. The lattice
  pinned it, so no lattice test exists, and the pre-registration applies changes only at target positions. The token stays as committed (S, T60).

## Decode and judge
    $ python3 tools/decode_key.py ciphers/nevers-birago-fr3251-1572 --config ciphers/nevers-birago-fr3251-1572/harvest/tx_decode/eye/open/decode_open144.json --check
    harvest/ciphertext_f144r.tsv: tokens 90: M 34, S 42, U 14
    reading up to date   (exit 0)
**f.144r H 0, C 0, S 42, M 34, I 0, U 14** (was S 40, M 36). Three M values changed (T95->T51 x2 = l, T78->T86 = e).
Judge (`specs/nevers-birago-fr3251-1572.json`, it). Same extraction for both: letters after the `|`, headers dropped:
    before (verify) FAIL language: score=-1.454, null_p99=-1.6, real_p05=-0.955, real_median=-0.828, mode=both, N=94
    after (open)    FAIL language: score=-1.418, null_p99=-1.614, real_p05=-0.954, real_median=-0.817, mode=both, N=91
The gain is partly circular, because the lattice uses an Italian LM. FAIL. No reading claimed, H 0 C 0, no novelty classed.

## Sorter
8 rows appended to `sorter/focus.tsv`, all sorter tiles from `ciphers/nevers-birago-fr3251-1572/sorter/signs.tsv`. f.144r tile counts match the
transcription on every line, so no off-by-one. There are 5 conflicts (L05:7 T36/T26/T76, L03:8 T42/T17, L05:12 T81/off-sheet, L06:1 T90/T97, L04.1:7 T60/T86) and
3 open-only rows (L05:19, L05:26 T95/T51; L04.1:12 T78/T86). The T95/T51 rows add to the f.117r/f.168 three-way question already in the sorter.
The orchestrator republishes the page.
