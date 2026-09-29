# VERIFY-F61-V11 pre-registration (written 29 Sept 2026 ~17:35 UTC, before any bowl answer, letter table or gain was computed by this session)

Claim under audit: family/PROPOSAL_v8_4tri.md (runner 13, H356-H366): the readers' 4TRI is two signs told apart by a stem-foot bowl; no-bowl = a/n
(C43's cell), bowl = c/p/t (4TRI's v7 cell).

Pre-look finding (structure only, no counts by bowl seen): passes/f101r_align.tsv's `status` is relative to the alignment's own EM key, in which 4TRI = n.
Every non-conflict 4TRI row therefore carries letter n by construction (140 `agrees n`; all others `conflict n X`). The brief's literal restriction
("non-conflict rows") cannot vary on the c/p-vs-a/n axis for 4TRI (rule 3: a control that cannot differ). It is run and reported as degenerate;
the pre-registered substitute is NEIGHBOUR-ANCHORED rows: a 4TRI row whose nearest code rows on each side in the same cipher line (excluding
4TRI and C43 rows) both have status `agrees` -- local alignment reliability that does not depend on 4TRI's own key value.

## A. Cross-tab from the runner's bowl labels (script verify_v11/v11_crosstab.py, own code)
Labels: H362 + H365 replies as used by h365 (gate-passing chunks). Letter: period letter by the difflib join (h364's method re-implemented).
Statistic: agreement share = (yes&c/p/t + no&a/n) / (tokens with c/p/t or a/n letter). Null: 10,000 permutations of the bowl labels among the
answered 4TRI tokens of the leaf (within-leaf), p = share of perms >= real. Sets: all rows; literal non-conflict (degenerate); neighbour-anchored.
Read-out per set with n >= 30: "tracks" iff share >= 0.75 AND p < 0.01; "does not track" iff share < 0.6 OR p > 0.05; else "unclear".
Also reported: P(a/n | no) and P(a/n | yes) -- the proposal needs both no->a/n high and yes->c/p/t high.

## B. Fresh bowl reads (own tiles cut from the natives, own prompt; verify_v11/v11_bowl.py)
Question (from the proposal's definition, not the runner's prompt): at the foot of the marked sign's vertical stem, is there a small closed
loop / bowl / triangle (yes), or does the stem end plainly (no)? 'unclear' allowed.
Calls (Opus subagent, one call per sheet set): C1 = 20 f.101r targets; C2 = 20 more f.101r targets; C3 = 24 f.124r targets. Each call also
carries 10 f.176v anchors (Desportes's hand, fr.3984; groups CP / AN from h193_items.tsv's coordinates, tiles cut by me from the native via
cut_bands.py) and 6 repeats (targets shown twice under different ids). Items shuffled, random 3-letter ids.
Gates per call: anchors >= 8/10 in group direction (CP=yes, AN=no) else the call's answers are not used; repeat consistency >= 5/6 else the call
is flagged unreliable and its answers not used.
Read-outs: (i) f.101r, my labels x period letter (all rows, and neighbour-anchored), share + within-leaf permutation null as A;
"independent read tracks" iff share >= 0.75 AND p < 0.01 (n >= 20). (ii) my labels vs runner's labels on shared tokens: Cohen's kappa >= 0.6
= the runner's reads replicate; < 0.4 = they do not. (iii) f.124r, same as (i) against passes/f124r_align.tsv.
Per hand: f.176v (anchors: does the bowl separate CP from AN in Desportes's hand), f.101r's hand, f.124r's hand (de Diou) each reported separately;
two signs in a hand iff the bowl predicts the letter class in that hand at the (i) bar; one sign drawn two ways iff the bowl does not.

## C. Order gain (tools/partial_key_test.py --cells, --shuffle-target 3; verify_v11/v11_gain.py)
Cells = key v7 as loaded; drafts = recf101r and recf124r as transcribed, and the runner's split drafts. Control: 30 random splits of the same size
(same number of 4TRI tokens relabelled C43, drawn uniformly from the leaf's 4TRI tokens, seeds 1100-1129).
Read-out per leaf: "the bowl split beats random splits" iff its gain exceeds the 95th percentile of the 30 random splits AND the shuffled-target
control on the split draft is clean (0/3 signal); "any split does this" iff it sits at or below the random median; else "unclear".

## D. Verdict rule
Endorse iff A(neighbour-anchored or all) tracks AND B(i) tracks AND C beats random on both leaves. In part iff B(i) tracks but C does not beat
random on both (or vice versa). Reject iff B(i) does not track, or B(ii) kappa < 0.4 with B(i) not tracking. Otherwise "unclear at this N".
Meter: verify_v8/meter_v8.py bands with and without the split, whatever the verdict (descriptive).

## Addendum E (written ~17:3x UTC after B's first read-out, before these calls): letter-stratified supplementary read
B's random 40 f.101r tokens carried only 5 c/p/t-lettered tokens (31 lettered), so B(i) cannot test the yes->c/p/t direction. Supplementary calls
c4, c5 (same prompt, tile format, anchors, repeat design and gates as B): 40 f.101r agreed 4TRI tokens not in B, 20 with a c/p/t period letter and 20
with an a/n letter (neighbour-anchored rows first, then others; seed 1115), shuffled together; the reader sees no letter or stratum.
Read-out: B(i)'s test on the c4+c5 answers alone and pooled with B (n >= 20): "tracks" iff share >= 0.75 AND perm p < 0.01; "does not track" iff
share < 0.6 OR p > 0.05; else unclear. This addendum is supplementary; B's pre-registered read-out stands as reported.
