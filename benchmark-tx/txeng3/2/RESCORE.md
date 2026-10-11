# TXE3-2 FLOOR -- RESCORE (11 Oct 2026, 17:5x UTC by date -u)

**Measurement correction: box-to-position map fixed (off by one), not a new gate look.** The blind classification (13 Sonnet calls) is
not re-run: this job makes no model call. What follows is what the map touched and what that does to the registered reading.

Job BOXMAP-RESCORE (others) for the account-3 parent (session_0198Cv8ypBfBVfRToKVWx33M). Script-only: no vision call, no reader, no
image viewed (tx_taxonomy's stroke/erosion columns are computed by script from the harvest page pixels, as in the original run), no
network beyond git. No truth file, flag file, BENCHMARK-TX.tsv row or confirm item touched.

`build_items.py` cut each floor/control tile at the atlas box `atlas/no87_box_token.tsv` gives its position, and `positions6.tsv`
(`tools/tx_taxonomy.py --box-token`) took each position's box geometry from the same map. That map is one token off on 10 of 26 lines
(`ciphers/nevers-birago-fr3251-1572/atlas/RESCORE.md`). **Only the map changed:**

    sh benchmark-tx/txeng3/2/rescore_boxmapLA/rescore.sh     # positions6.tsv, positions6_summary.md, items_tiles.tsv

With the old map the tx_taxonomy command reproduces the committed `positions6.tsv` and `positions6_summary.md` byte for byte.

## 1. The 18/803 floor

The floor (positions wrong in all six of L A B C E F) is defined by the reads and the truth, not by any box: **unchanged, the same 18
positions.** Box geometry changes on 153 of 803 rows (all on the 10 moved lines plus one `unsure` box on f178v L23), and on 2 floor
positions: f178v L13.7 (band near -> in, stroke mid -> heavy) and L21.21 (band in -> near, stroke thin -> heavy, err_class thin ->
other). The summary's op table gains `bad-cut` / `unsure` columns (0 errors in either); its band-edge and stroke tables shift by 1-4
errors per pass; "C and L carry 0 insertions and 0 deletions" and every I/D-vs-S figure are read-based and unchanged.

## 2. The blind classifier's material (`items_tiles.tsv`)

**5 of the 36 items were cut at the neighbouring token's box**, so the classifier was shown the wrong sign:

| item | kind | position | box shown | box at that position now | classifier's answer (floor.tsv) |
|---|---|---|---|---|---|
| f178v_L13 A | floor | L13.7 | f178v_13_007 | f178v_13_006 | whole, clean, top-1 T90; class iii-flagged |
| f178v_L13 B | control | L13.26 | f178v_13_026 | f178v_13_025 | **joined**, top-1 T13 (truth T37/T85); invented cause |
| f178v_L21 A | floor | L21.21 | f178v_21_021 | f178v_21_022 | whole, clean, top-1 T58; class v |
| f178v_L21 B | control | L21.27 | f178v_21_027 | none (no one-token box) | **joined**, top-1 T45 (truth T60/T76); invented cause |
| f179r_L02 A | control | f179r L02.28 | f179r_02_029 | f179r_02_028 | whole, clean, top-1 T19 (truth T27/T53/T65); invented cause |

All three wrong-tile controls are among the 7 controls with an "invented cause", and two of them are 2 of the 4 "joined" verdicts.

| statistic (PREREG step 6) | as run (36 items) | the 31 items cut at the right box | gate |
|---|---|---|---|
| control invented-cause rate | 7/18 = 0.389 | **4/15 = 0.267** | <= 0.25: still **FAIL** |
| control top-1 in the truth set | 12/18 | 12/15 | |
| control Q1 cut/joined | 4/18 | 2/15 | |
| floor with a cause other than (v) | 11/18 | 10/16 | |

## Does the conclusion change?

**The verdict does not change**: NON-TEST for the per-position classification; on the correctly cut items the control's
invented-cause rate is 0.267, still above the 0.25 gate, and the floor set is map-independent. **Two supporting sentences weaken**:
"the four 'joined' verdicts all fell on control signs the readers got right" -- two of the four were the wrong sign's tile; and the
control failure's main part, "the classifier's own sign identification against the PRINTED sheet missed the right sign on 6/18 right
signs", is 3/15 on the right tiles (3 of the 6 misses were the neighbouring sign). RESULTS' "Next step" condition ("worth running only
if the sign-ID half of the rule drops below 1/6 on controls"): 3/15 = 0.20, still above 1/6 -- but the measured rate was half map, so a
re-run on correctly cut tiles is the cleaner basis for that call (a model-call job, not done here).
