# TXE3-10 PAIR -- RESCORE (11 Oct 2026, 17:5x UTC by date -u)

**Measurement correction: box-to-position map fixed (off by one), not a new gate look -- but see "Status of the eval figure" below:
the corrected measurement crosses the registered bar, and whether that counts is for the verifier and the lane, not this job.**

Job BOXMAP-RESCORE (others) for the account-3 parent (session_0198Cv8ypBfBVfRToKVWx33M). Script-only: no vision call, no reader, no
image viewed, no network beyond git. No truth file, BENCHMARK-TX.tsv row or confirm item touched. Nothing re-tuned: same patch,
features, pool rules, threshold rule and seeds.

`glyph_atlas_pair.patch` (`classify --pair ... --map`) builds its dev pool from dev_tune positions and applies the discriminator at
eval positions, both through `atlas/no87_box_token.tsv`, which is one token off on 10 of 26 lines (f178v L06, L07, L09, L11 on dev;
L13, L17, L21, f179r L01-L03 on eval; `ciphers/nevers-birago-fr3251-1572/atlas/RESCORE.md`). **Only `--map` changed** (to
`atlas/no87_box_token_labelaware.tsv`). The run arguments, which TXE3-10 never committed, are now a script beside the patch:

    bash benchmark-tx/txeng3/10/rescore_boxmapLA/run.sh MAP OUTDIR

It applies the patch to `tools/glyph_atlas.py` as of 1b50c66c in a temp copy and runs VERIFY.md's argument set. **With the old map all
41 committed instrument files come out byte-identical** (g1/g2/apply/touched reports, real and 10 control eval outputs, dev outputs,
T90/T53). Outputs with the label-aware map: `rescore_boxmapLA/` (same names; `passX30_topo_full.tsv` = L with the eval flips).

## T18/T98 (d/s)

- Pool and dev gates: pool 25/39 (22 groups) unchanged; **G1** 0.984 vs shuffled max 0.609, PASS (identical file); **G2** dev LOO
  (`g2`, `touched`, `passX30_topo_dev_tune.tsv` byte-identical): fixed 1 (L06.18), broken 0, L10.31 wrong -> wrong. PASS, unchanged.
- **Eval** (9 boxed T98 reads): the one miss, **f178v L13.20 (margin -0.982), was the wrong tile**. The old map put tile
  f178v_13_020 there; that tile belongs to L13.21. The label-aware map gives L13.20 tile f178v_13_019, and the discriminator flips it
  (margin +0.988, truth d). The other 8 positions are the same tiles with the same margins.

| output | considered | changed | fixed | broken | exact p | eval err as measured | flagged excluded |
|---|---|---|---|---|---|---|---|
| L (base) | | | | | | 0.040 (15/376) | 0.027 (10/371) |
| X30 real, before | 9 | 5 | 5 | 0 | 0.0625 | 0.027 (10/376) | 0.013 (5/371) |
| **X30 real, after** | 9 | **6** | **6** | **0** | **0.0312** | **0.024 (9/376), 0.013-0.045** | **0.011 (4/371), 0.004-0.027** |
| ctrl 1-5 (registered pipeline), after | 0 | 0 | 0 | 0 | 1.0 | = L | = L |
| ctrl 1f-5f (`--force-t 0`), after | 9 | 2-4 | 1-2 | 1-2 | 1.0 | 0.040-0.043 | 0.027-0.030 |

Whole item (L with the eval flips): as measured 34/803 -> **28/803 (0.035; was 29/803)**; flagged excluded 23/792 -> **17/792
(0.021)**; position McNemar fixed 6 / broken 0, p 0.031; lines improved 5, worsened 0 (line sign p 0.0625); paired line bootstrap of
the difference -0.015..-0.002.

## T90/T53 (p/t), control C2

C2's G2 failure was the map too. Both "broken" dev positions, L11.26 and L11.28, sit on the shifted line L11 (tiles f178v_11_024 and
_026 belong to L11.25 and L11.27), and the dev pool changes by one tile (24/67 -> 23/67).

| | before | after |
|---|---|---|
| G1 (LOGO vs 20 shuffled) | 0.978 vs max 0.681, PASS | 1.000 vs max 0.667, PASS (pool 23/67) |
| G2 (dev LOO) | fixed 0, broken 2: **FAIL**, not applied to eval | fixed 0, **broken 0: PASS** |
| eval (registered "if G1 and G2 pass, applied to eval's 1:1 T90/T53 positions") | not run | 25 considered, **0 changed**: fixed 0, broken 0 |

The C2 eval step is the registered pipeline's next step once both dev gates pass; it ran here once, as `passX30b_topo_T90T53_eval_heldout.tsv`.

## Status of the eval figure

The registered verdict rule is "helps iff net > 0 and p < 0.05 (6-0 or better at this N)". The corrected measurement is 6-0, p 0.031,
with every registered shuffled control at 0 changes and every forced-threshold control at net <= 0. So **the registered rule is met by
the corrected measurement**. It is not a clean first look: the eval file was scored once on 11 Oct with the old map (5-0), the map was
then fixed for an unrelated reason (TXE3-9's second check), and this is the same instrument scored again. Nothing in the instrument was
changed and the new map reads no truth; still, a verifier should rule on whether TXE3-10's logged "weak for this pair at this N" is
upgraded, and that ruling is not made here.

## Does the conclusion change?

- **T18/T98: yes, by the registered rule.** "Weak for this pair at this N ... one position short of its own gate" -> the one miss was a
  wrong tile; on the right tiles the discriminator fixes all 6 eval d-for-T98 errors and breaks none (p 0.031). Pending the verifier's
  ruling above.
- **C2: yes.** "the same features break two correct dev positions and fix none ... the instrument is pair-specific, not a general
  look-alike fixer": with the right tiles the T90/T53 model passes G1 and G2 and changes nothing on dev or eval. It neither breaks nor
  fixes; "not shown to fix p/t" is the honest reading, not "breaks p/t".
