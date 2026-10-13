# PREREG-BAL-GPLUS (BAL167-GVER worker, LANE DEFAULT-A2-2013, account 2), written 13 Oct 2026 21:0x UTC by date -u,
# pushed in its own commit BEFORE any gloss read or tile read for this job

Target: Baluze 170 f.228v, the g+ ("gt") class: 3 tokens (b167228/sig_tiles.py TARGET g+ v_b_L01 x 2410, v_b_L03 x 385,
v_b_L05 x 1426), value n (Tomokiyo channel), grade M. Exemplars: the glossed "gt" on Baluze 170 f.124r (canvas 131, 2 tokens) and
f.124v (canvas 132, 1 token) found by BAL167-GPLUS, strips images/gplus/b170_c131_pct_73_52_5_27_5.jpg (2106x292) and
b170_c132_pct_15_32_5_20_5.jpg (1440x293). Brief: .claude/briefs/runs/2026-10-13-ytbiz-default-2013-jobs.md "BAL167-GVER".
Method: BAL167-GHV (PREREG-BAL-GHV.md), a label-VERIFICATION read, one proposed exemplar for every tile, yes/no.

## (a) Gloss letter(s) over "gt" -- two blind reads, settle or stop
Two fresh blind Sonnet subagents, each given only the two strips (one call each, both strips) and told: "read the clear words written
above the cipher, letter by letter, with their x positions" (plus: give each cipher sign's x span too, so letters can be placed over
signs). Not told the f.228 value, Tomokiyo's value, the gloss BAL167-GPLUS saw, or what the job is about. Output balshape/gplus/glossA.tsv,
glossB.tsv. Located by this worker (location only, after the reads, from the image): the x span of each "gt" token and of its two
neighbours. Settling rule, per gt token: list the gloss letters each read places over the gt's x span (+-20 px), after the letters both
reads place over the neighbouring signs whose key value is H (key.tsv) are assigned to those signs. The value is SETTLED for the class
only if (i) both reads give the same letter string over at least two of the three gt tokens, (ii) no token has the two reads disagreeing
on a letter, and (iii) that string is the same on every token where both reads give one. Otherwise NOT SETTLED: stop, g+ stays M, logged
in HYPOTHESES.md; no tile read. This worker does not substitute its own reading of the gloss for either read.

## (b) Tile test, only if (a) settles
Tiles cut with b167228/sig_tiles.py tile() (150x210, x +-75, y -90/+120) from images on disk; script balshape/gplus/tiles_gplus.py
[seed], every tile captioned "Xnn: E-g+?" so the label cannot cue the answer.
Exemplar E-g+: f.124r first gt (after 76).
T (3): the three f.228 g+ tiles above.
P+ (2): the other two f.124 gt tokens (f.124r line-final, f.124v after K).
P- (<= 4, within-key look-alikes, fixed value != the settled gt value): crossed y on f.229 (sig_tiles EXEMPLAR y+ L4 x 1444, value r,
the f.229 letter's alignment) and on f.228 (DECOY:y+=r, VB x 1713); the glossed r-shape = g on f.239r (balshape/ghv/labels.tsv N3,
both GHV reads 'grande'); a bare g ("y"-like) on the f.124 strips only if both reads of (a) force its letter by the same rule; else
the arm runs with 3. If the settled gt value equals one of these values (r or g) that tile is dropped from P- (logged).
Reader: one blind Sonnet subagent, shown exemplar sheet (E-g+) and the shuffled tile sheet; per tile yes/no "same sign as E-g+
allowing for hand variation", high/low. Not told arms exist.

## Why P-'s number can differ from T's (rule 3, AX-5799)
Statistic: yes-rate on E-g+. The manipulation is the tile itself (a true gt vs a crossed/looped look-alike of another value); a reader
that says yes to any descender-with-stroke gives a high P- rate (G2 FAIL).

## Gates (same read; same as GHV)
G1: P+ yes-rate >= 0.75 (with 2 tiles: both yes). G2: P- yes-rate <= 0.25 AND <= P+ - 0.50. If either fails on read 1: ONE second read
(fresh subagent, seed 20261014) only within the 80% line; gates on read 2 alone. Still failing: g+ logged untested-by-this-tool,
no grade change.

## Target and adoption
Each f.228 g+ tile CONFIRMED if yes and not high-confidence no. The class is adopted only if all three T tiles are confirmed AND the
settled gloss value is n: then the 3 f.228 g+ tokens move M -> S through balshape/ghv/exceptions_b170f228.tsv (rows appended), and
`python3 tools/decode_key.py ciphers/baluze167-davaux-1637 --check`. If the settled gloss value is not n, nothing is regraded: a value
conflict is logged in HYPOTHESES.md (stays M; the value change is a later job with a judge re-run). AUDIT.md not touched.
Caps: USD 4.5, box 20:54-22:09 UTC (80% 21:54). Units: 2 gloss reads + reconciliation + 1 tile read (+1 if G fails), ~0.7 each.
