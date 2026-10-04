## NEAR3-C1TX-c188L (4 Oct 2026)

Account 2 worker for LANE-NEAR3. Brief `.claude/briefs/runs/2026-10-04-ytbiz-near3-wave2.md` (job NEAR3-C1TX-<LEAF>,
LEAF = c188L), pointing to the wave-1 job of the same name. Clock: claim 01:35 UTC, reconciliation finished 01:52 UTC
(box 60 min). Written here, not in NOTES.md, per the brief; the lane folds it in.

**Leaf.** c188L = IIIF f189, left leaf, native region 100,50,3150,4600 (ark btv1b90010063; NOTES.md "IMG-GALLICA1").
It holds **27 lines** of cipher, continuous from top to bottom. There is no heading. The only clear writing is one small
word at the end of L14 ("curou?", read M). Below L27 the leaf is blank apart from the library stamp.

**Route and crops.**
- The crop command, pasted before any subagent call:
  `python3 tools/iiif_lines.py --ark btv1b90010063 --canvas 189 --region 100,50,3150,4600 --out
  ciphers/clair1161-avis-flandre-1688/images --prefix c188L --bottom-margin 75 --debug`.
  - It found 28 bands, with spurious centres at y 81 and 4568, so the bands straddled two lines.
  - **Side effect on other leaves' files.** Because the folder was over 30 MB on disk, the tool shrank two committed
    reference images from other leaves (`src_..._f186_...`, `src_..._f187_...`) to 1600 px "_ref1600" copies, and
    rewrote their manifest rows. It also downscaled this job's own native file. I restored both files and their manifest
    rows from git before committing. **The lane should know the tool does this whenever several leaves crop into one
    folder.**
- I fetched the region a second time into the scratchpad (not committed; sha1 dd16bb37cd08eaf2c35b4d955dcc62de31fa9a80).
  I re-cut it with centres set by eye: `python3 tools/iiif_lines.py --image <native> --out <scratchpad>/crops --prefix
  c188L --centres 280,420,600,720,850,990,1140,1260,1390,1530,1660,1800,1920,2050,2190,2330,2460,2580,2710,2850,2980,3130,
  3270,3400,3540,3670,3800 --top-margin 15 --bottom-margin 75 --max-width 1700 --overlap 150 --debug`.
  That gives 27 lines x 2 segments. The two blind passes read these crops (q95, in the scratchpad).
- **Those level crops were still wrong.** The lines on this leaf rise about 0.05-0.08 px per px to the right, some
  110-170 px across the leaf. A level band therefore holds its own line on the left, and on the right the end of the
  line cut at the top plus the next line in full. Both passes reported this.
- For the reconciliation I cut **slope-following crops** with `tx/c188L_slopecrop.py`. It tracks each line strip by
  strip on the ink profile and cuts 3 segments per line (x 450-1500, 1350-2400, 2250-3150), 81 crops.
- These are the committed crops: `images/c188L_L01..L27_s1..s3.jpg` plus an overlay of the boxes,
  `images/c188L_lines_debug.jpg`. They are grayscale JPEG q30 at native size, **1.34 MB** in all, under the brief's
  1.5 MB.
- The first-cut crops pushed in ad631ae3 are removed in this commit, along with their manifest rows. They can be
  regenerated with the commands above.
- The script reproduces the committed boxes exactly from the native region. The committed folder is about 27.8 MiB.

**Requests.** gallica.bnf.fr: 2. The first was the iiif_lines fetch; the second was a refetch after the tool had
downscaled its own copy. Both used a descriptive UA, with no challenge.

**Subagent calls (Sonnet): 2.** Pass A and pass B, run in parallel. Each saw only `tx/labels_v2.md` and the 54
level crop paths, with the prompt in `tx/c188L_pass_prompt.md`. Pass B worked bottom-up. I did the reconciliation from
27 three-segment line composites plus 4 detail views. That is the third priced unit; no third pass was run.

**Numbers.**

| item | value |
|---|---|
| lines | 27 |
| pass A / pass B signs | 730 / 750 |
| reconciled `tx/c188L_rec.tsv` | **752 cipher signs** + 1 clear word (PLAIN:curou?), conf H 634, M 119 |
| err_2reader, raw (`reconcile_passes.py`, nw) | 156/758 = 0.206 |
| err_2reader after `tx/c188L_signmap.tsv` (ε->e, 0->o, NEW:v-bar->vdash, NEW:triangle->tri: spelling, not reading) | **137/758 = 0.181** |
| of which one uniform convention split (A tz / B z on the same shape, every time) | 35; the rest 102/758 = 0.135 |
| pass vs reconciled (same sign map) | A 119/760 = 0.157 (35 of them the tz/z convention), B 63/762 = 0.083 |
| err_true | not measurable: no benchmark item of this hand |

Most of the split comes from the level crops, not from look-alike signs:
- L04 and L18 are 10 signs short in pass A, because the line's right half was cut off in its crop.
- Several splits are one sign that a pass read twice in the overlap.
- **One error was shared by both passes and so did not show up as a split.** Both gave L16's line end
  (`e wb S th w + a y th`) to L15 and left out L15's real end (`iii 7 7 th K w + S 9`). I fixed this from the slope crops
  (grade M, one reader).
- I checked every line end against the slope crops; the other 25 match the passes.

**Look-alike pass not run.** The brief asks for `tools/lookalike_pass.py` when err_2reader is over 0.10, but the tool
does not fit this leaf: it needs a blind sheet of sign tiles (glyph atlas) and a confusion table, and no atlas exists for
this hand. It also re-reads only tiles that look alike, while this split comes mostly from the line framing. I wrote the
residual questions as a sorter focus list instead (`tx/c188L_focus.tsv`, sid<TAB>question, 8 rows). No third full pass
was run.

**Settlements** (each is in `tx/c188L_reconcile.py` with its reason; 86 positional decisions, a tz/z rule and two
line-end corrections):
- **tz/z.** The shape is a barred z with a small raised loop on top. I settled all 35 as `z`, grade M, the label the
  earlier leaves use for this shape (c185R: z 48, tz 6; c187L: z 48, tz 1). Whether it differs from the plain barred z is
  focus row 1.
- **iii/iib.** Settled by stroke count where I looked. Barred three-stroke groups (iii) are the usual form
  (L02, L15, L16, L17, L22, L23), and a two-stroke `#` (iib) occurs too (L12 three times, L19). The two unviewed cases
  keep A (M). This is the same two-form question c186L raised.
- **The raised hook before q.** Pass A read f, pass B e or 7. I settled e (M where unclear), which is c187L's c/e
  convention.
- **`s z` pair** read as `s` (5-hook), as c186L and c187L did.
- **phi vs q** on the bowl with the stem through it: phi (M).
- **The e-looped K** at L07 and L17 is one sign, K (M).
- **A merged with B.** Pass B's `NEW:v-bar` (L25) = `vdash` and `NEW:triangle` (L25) = `tri`, the c187L conventions.
- **Signs dropped.** A's extra `a` before y at L02 and L05: the y glyph is drawn as a+y. Also overlap doubles at L05,
  L06, L08, L16, L20 and L23. The "ls" in L20 is L19's long-s descender.

**Shapes outside labels_v2** (provisional names; the c186L/c187L `NEW1` labels do not fit them):
- `NEW_c188L_1`: a closed D-loop under a long arched over-bar. 3 occurrences: L01 x2 (slope crop c188L_L01_s1/s2) and
  L19 (c188L_L19_s2).
- `NEW_c188L_2`: a small caret ^. 2 occurrences: L01 before `a` (c188L_L01_s3) and L17 before `S` (c188L_L17_s2).
  Pass B named it NEW:caret; pass A read `a`.
- `NEW_c188L_3`: a large open C enclosing a barred z. 4 occurrences: L05 (s2), L09 (s3), L11 (s3) and L24 (s1).
  - The passes read it as eloop, tz, or `eloop z`.
  - **L09 and L11 share the run `7 7 a sqc 3 7 NEW_c188L_3 y 4 q th`.**
  - In the information decode below it falls where a t would fit ("...rois" twice). In the current key, z = t. It may
    therefore be a form of z, but that is not settled.
- c186L's `NEW1` (v with long bar) is the `vdash` at L25 here. c187L's open-arc `NEW1` does not occur.

**Decode for information only** (`tx/c188L_decode_info.txt`). It is ungraded and not a reading: the leaf is decoded
under the current key.tsv, which was annealed on c185R+c186R only, and no control was run. decode_key's own count:
C 78, S 561, M 111, U 9 (the U are the NEW_c188L_* signs).
- Runs of French appear unprompted: "entreulx", "tous le", "conseil", "assisti", "pareile des", "plusieurs aultres",
  "persoune", "couuert", "eulx et", "croire".
- Much of the rest does not segment into words.
- A held-out judge score with a shuffled-key control would be the cheap check of the key on this leaf. It was not in
  this brief.

**Files:** `tx/c188L_passA.tsv`, `tx/c188L_passB.tsv`, `tx/c188L_signmap.tsv`, `tx/c188L_rec/` (reconcile_passes
output), `tx/c188L_rec.tsv` (wide), `tx/c188L_rec_long.tsv` (ids `c188L_Lnn`, line/pos/sign/conf/note),
`tx/c188L_reconcile.py` (regenerates both rec files), `tx/c188L_slopecrop.py`, `tx/c188L_focus.tsv`,
`tx/c188L_decode_info.txt`, `tx/c188L_pass_prompt.md`.

**Not done** (per the brief): no edit to ciphertext.tsv, key.tsv, tx/stream_all.txt, NOTES.md or NEAR.md; no judge
run; no third pass.

**Next step for the pooled job.** Before merging, re-read L15/L16 and the 119 M-graded signs against the slope crops,
or run two fresh blind passes on the slope crops (2 Sonnet calls at about the per-pass rate of this job), so that
err_2reader measures reading rather than framing.
