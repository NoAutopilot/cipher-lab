# PREREG-BAL-GHV (BAL167-GHV worker, LANE DEFAULT-A4-0935, account 4), written 13 Oct 2026 10:4x UTC by date -u,
# pushed in its own commit BEFORE any gloss read or tile read for this job

Target: Baluze 170 f.228r-v (Chavigny to d'Avaux, 25 Aug 1640), the shape classes BAL-WL could not test (HYPOTHESES.md): hook (7 tokens,
value s, M), v (2 tokens, value s, M), g+ (3 tokens, value n, M). Brief: .claude/briefs/runs/2026-10-13-acct4-default-0935-jobs.md
"BAL167-GHV". Method as BAL-WL (PREREG-BAL-WL.md): a label-VERIFICATION read, one proposed exemplar per tile, yes/no.

## g+ (no test)
Glossed leaves searched by eye for a g+ form (a g with a cross stroke): f.233r, f.239r, f.258r (native crops on disk, BAL-CROP);
f.301r (c314) and f.320v-321r (c334) (openapi.bnf.fr full at 3000 px, this job); c71 (f.64r) is a clear draft, no cipher.
No g+ form seen. g+ stays M, untested; no exemplar exists, so it is not tiled.

## Hook/v exemplar and labels
E-s2 (the new exemplar): f.258r row E hook (images/b170gloss/c270_f258r_cipher_native.jpg x 2200, y 1123): both BAL-CROP blind gloss
reads (balshape/glossA.tsv, glossB.tsv, f258r_S05_h2) give 'plus estroitement' over mm 44 p w HOOK u+ 68' ...; w=e, u+=t (S, BAL-WL),
68'=ro (H) leave s for the hook.
f.258r labels (same two existing blind reads): P+ 'lors' (row I x 2600: 43'=lo H, y-bar=r S, HOOK -> s); P- 'Luneboyrg' z-swash
(row I x 1085: 44' 51' 6 = lu ne bo, the swash is the u/y, value not s); P- h (row A x 2494, gloss-fixed n, A10).
f.239r labels (no blind gloss read exists yet): two fresh blind Sonnet gloss reads of balshape/ghv/strips/f239r_g{1,2,3}.jpg (pasted
crop commands in NOTES.md). A tile gets its label only if BOTH reads give the same gloss word over it and that word, aligned with the
key's H codes on either side, forces one letter. Expected (not yet read): g1 x 2700 'n'est pas' -> s (P+); g2 x 2735 'presser' -> s
(P+); g3 x 1990 'plus' -> s (P+); g3 x 2887 final z-swash 'longueur' -> u (P-); g3 x 2085 r-shape 'grande' -> g (P-). A tile whose
label is not confirmed by both reads is DROPPED before the tile read (logged); its arm shrinks.

## Arms (balshape/ghv/tiles_ghv.py, seed 20261013; same tile() geometry as BAL-SHAPE/BAL-WL)
Every tile is captioned "Xnn: E-s2?" (one proposed label for all arms, so the label cannot cue the answer).
T  (2): f.228 hook (v_b_L02 x 1035) and f.228 v (r_a_L02 x 1700), the BAL-SHAPE T tiles.
P+ (<= 4): gloss-fixed hook-form s tiles (f.258r lors; f.239r g1, g2, g3-plus).
P- (<= 4): within-key look-alikes with a gloss-fixed value other than s: the two z-swashes (u/y), the r-shape (g), the h (n).
Reader: one blind Sonnet subagent, shown the exemplar sheet (E-s2 plus the 12 BAL-WL exemplars, as reference for 'best') and the
shuffled tiles; per tile yes/no "same sign as E-s2 allowing for hand variation", high/low, best exemplar or NONE. Not told arms exist.

## Why P-'s number can differ from T's (rule 3, AX-5799)
Statistic: yes-rate on E-s2. The manipulation is the tile itself (a true hook-s vs a near look-alike of another value, the V-BAL167
lesson), which is exactly what the yes/no depends on; a reader that says yes to any curl gives a high P- rate (G2 FAIL).

## Gates (same read)
G1: P+ yes-rate >= 0.75. G2: P- yes-rate <= 0.25 AND <= P+ - 0.50. Arms are small (<= 4): one tile moves a rate by 0.25; reported.
If either fails on read 1: ONE second read (fresh subagent, seed 20261014) only within the 80% line; gates on read 2 alone. Still
failing: hook/v logged untested-by-this-tool, no grade change.

## Target and adoption
hook CONFIRMED if its tile is yes and not high-confidence no; same for v. A CONFIRMED class moves all its f.228 tokens M -> S
(hook 7, v 2; class-wide, the BAL-WL convention, one tile standing for the class -- a stated limit) through an exceptions file read
by tools/decode_key.py (balshape/ghv/regrade_ghv.py writes balshape/ghv/exceptions_b170f228.tsv = BAL-WL rows + these rows; decode.json
pointed at it). Values never change, so the fr17 judge is not re-run. A "no" is logged in HYPOTHESES.md as a conflict (stays M).
Then `python3 tools/decode_key.py ciphers/baluze167-davaux-1637 --check`.
Caps: USD 4, box 10:29-11:39 UTC (80% 11:25). Units: 2 gloss reads + 1 tile read (~0.8 each) + this session.
