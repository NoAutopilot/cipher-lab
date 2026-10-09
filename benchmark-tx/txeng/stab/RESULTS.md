# TXE-J: jitter stability as a per-position prior in the lattice (LANE TX-ENGINEER idea M11, 9 Oct 2026)

Brief `.claude/briefs/runs/2026-10-09-account4-txe-j.md`; PREREG `benchmark-tx/PREREG-txeng-2.md` (gate fixed > broken,
p < 0.01, Amendment). Worker TXE-J (account 4, Opus), 07:43-07:54 UTC by date -u. Read-free: **0 vision calls, 0 reader
calls, 0 network requests**.

**Verdict: FAIL.** Dev gate not met: vs L_dev_tune fixed 1, broken 4, p = 0.375. The permuted-stability control (seed 1)
gives fixed 1, broken 5, p = 0.22, so the real and the permuted prior do not differ. Vs the plain lam-4 lattice: fixed 5,
broken 4, p = 1.0. No eval look taken (0 of 1 used). Doubt prediction: stab < 0.6 flags 1 of L's 14 wrong positions
(recall 0.071) at 5.4% of positions flagged, about the chance rate. Stability does not predict where L is wrong.

## What was built (tests: tools/tests/test_glyph_atlas_jitter.py, test_key_decode_lattice.py::test_stability_prior)
- `glyph_atlas.py classify ... --jitter N [--jitter-px 2 --jitter-scale 0.05 --jitter-seed 1 --jitter-rel 0.78]`: each target
  box is re-cut N times from the binarised page (window shifted by an integer dx, dy in [-px, px] and scaled about the box
  centre by s in [1-scale, 1+scale]; only components touching the window's central half are kept), projected into the SAME
  fitted feature space (`feats(..., project=True)`, scalers and PCA fitted on the atlas only) and voted by the same kNN.
  New columns: `stab` (share of jitters whose top-1 = the unjittered top-1), `k1_j` (majority jittered top-1), `k1_0` (the
  top-1 of the unjittered re-cut, a fidelity check). The existing columns are unchanged (test asserts it).
  Offline test result: the 6 px blob scores stab 0.00 and the 60 px blob 1.00. The brief's example values were 0.4 vs 1.0;
  the test asserts <= 0.6 vs = 1.0.
- `key_decode_lattice.py from-passes ... --stability STAB.tsv [--box-pos BOX_POS.tsv] [--stab-floor 0.6] [--stab-gain 0.9]
  [--stab-shuffle SEED]`. Where stab >= floor, the top-1 candidate's p becomes p + (1-p) x gain and the others are scaled by
  (1-gain). Where stab < floor, or the position is unmapped, the candidates are left unchanged. A position covered by
  several boxes takes their minimum stab. `--stab-shuffle` is the rule-3 control. The gain 0.9 was fixed before any score
  (commit 1301d9096 carries the decodes and the code).

## Protocol
- Classify: `glyph_atlas.py classify --out ciphers/nevers-birago-fr3251-1572/atlas --labels atlas/labels.json --page f178v
  --topk 3 --holdout f178r_ --holdout f178v_ --holdout f179r_ --jitter 5` -> `stab_f178v.tsv`. The unjittered top-1
  reproduces TXE-A's `topk_no87_allheld.tsv` on 675 of 675 f178v boxes. The re-cut fidelity (`k1_0` = stored top-1) is
  666/675.
- Boxes -> positions: `benchmark-tx/txeng/compare/box_pos.tsv` (TXE-A's `tx_compare.py map`, label-blind width DP). Of the
  354 dev positions, 341 are mapped and 19 have stab < 0.6.
- Lattice and decode: `run_stab.py dev` imports TXE-E's `run_conf.py` (passes A/B of f178v, passC skeleton,
  confusion_1572, printed key, it16dip, beam 64, lam 4). It regenerates `passL_lattice_dev_tune_lam4.tsv` byte-identical to
  TXE-E's. The prior sharpens 251 positions; the controls (stab permuted over the mapped positions, seeds 1-5) sharpen
  247-249.

## Stability distribution (f178v, 675 boxes, jitter 5)
| stab | 0.0 | 0.2 | 0.4 | 0.6 | 0.8 | 1.0 |
|---|---|---|---|---|---|---|
| boxes | 8 | 10 | 13 | 21 | 33 | 590 |

Mean 0.943; 87.4% are fully stable; 4.6% are below 0.6. On 30 boxes the majority jittered top-1 differs from the top-1.

## Dev scores (tx_bench, `--paired`)
```
passR_stab_dev_tune.tsv        err_true 0.050 (17/343) 0.031-0.078 | wrong 17 deleted 0 inserted 0
paired passR_stab_dev_tune.tsv vs labels_dev_tune.tsv: 343 common; base wrong 14, output wrong 17; fixed 1, broken 4; p = 0.3750
paired passR_stab_dev_tune.tsv vs passL_lattice_dev_tune_lam4.tsv: base wrong 18, output wrong 17; fixed 5, broken 4; p = 1.0000
control passR_stabshuf1_dev_tune.tsv  err_true 0.052 (18/343); vs L fixed 1, broken 5, p = 0.2188; vs plain lattice fixed 3, broken 3, p = 1.0
controls seeds 2-5: each err_true 0.050 (17/343), vs L fixed 1, broken 4, p = 0.3750
baseline passL_lattice_dev_tune_lam4.tsv  err_true 0.055 (19/343); vs L fixed 3, broken 7, p = 0.3438
```
The control does not pass, as required. But the real prior does not differ from it either: 4 of 5 permutations score
exactly what the real stability scores. The prior's only effect comes from sharpening about 250 of 341 positions, whichever
positions those are. Sharpening pulls the decode back toward the readers' top-1 (17 errors against the plain lattice's 18),
but never past L.

## Doubt prediction (read-free use: does stab < floor mark L's wrong positions? `doubt.py`, truth via tx_bench only)
```
scored 343, L wrong 14, mapped 331, L wrong & mapped 14
floor	flagged	share	L_wrong_flagged	recall	precision
0.4	9	0.027	0	0.000	0.000
0.6	18	0.054	1	0.071	0.056
0.8	27	0.082	1	0.071	0.037
1.0	46	0.139	3	0.214	0.065
L wrong positions: [('L02.12', 1.0), ('L02.8', 1.0), ('L05.1', 0.8), ('L05.4', 1.0), ('L05.9', 1.0), ('L06.18', 1.0), ('L06.27', 1.0), ('L09.4', 1.0), ('L10.1', 1.0), ('L10.31', 1.0), ('L10.4', 0.4), ('L11.17', 0.8), ('L11.29', 1.0), ('L11.5', 1.0)]
```
Base rate: 14/331 = 4.2%. At floor 0.6 the precision is 5.6% with recall 1/14, close to chance. 12 of L's 14 errors sit on
tiles with stab 1.0. These are the agreed-wrong class-1 confusions (TXE-E; TX-TAXONOMY C1): the atlas and the readers make
the same mistake every time, so jitter cannot reveal it. A doubt measure of the kind the sorter's focus needs has to come
from somewhere other than crop stability.

## Taxonomy (`tools/tx_taxonomy.py`, `taxonomy_dev.md` / `.tsv`, passes L, Lat4, R, Rshuf1)
R repeats 13 of L's 14 errors with the same wrong sign. R and Rshuf1 share 16 of 17 errors (same sign). Nothing moved in
any class because of stability as such.

## Calls and cost
0 vision calls; 0 subagents; no host. The lane reads the cost from get_session.

## Follow-up (one line, not done)
Gating the sharpening on atlas top-1 = reader top-1 would be a fresh dev attempt at this instrument (a second attempt);
the doubt table says the signal is not there to gate on, so I do not recommend it.
