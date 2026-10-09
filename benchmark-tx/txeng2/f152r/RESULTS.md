# TXP-152 results: birago1572-f152r built and read ONCE with today's pipeline (9 Oct 2026, 15:21-15:3x UTC by date -u)

LANE TX-ENGINEER-2 round 0b item 2 (PREREG `benchmark-tx/PREREG-txeng2-0.md`). Order kept: crops 6e9086b86, passA 013af694a,
passB 6890cf62c, reconcile + queue (next commit), adjudication + passZ d2587da40 (pushed c3720e963 at 15:28 UTC) -- all before the
slip, passC or any truth was opened; truth built and scored after.

## Headline (this leaf only)
```
birago1572-f152r [eval] err_true 0.082 (6/73) 95% 0.038-0.168 | wrong 5 deleted 0 inserted 1 | excluded 24 | lines missing 0
  as measured 0.082 (6/73) | flagged excluded 0.043 (3/70) 95% 0.015-0.119 [3 flagged]
  top confusions (truth value <- read): e<-T36 x1, d<-T98 x1, c<-T86 x1, a<-T52 x1, l<-T64 x1
paired passZ_pipeline.tsv vs committed.tsv: 73 common scored signs; base wrong 5, output wrong 5; fixed 0, broken 0; p = 1.0
```
| output | err_true (95%) | flagged excluded | paired vs committed (fixed/broken) |
|---|---|---|---|
| **passZ_pipeline (baseline)** | **0.082 (6/73) 0.038-0.168** | 0.043 (3/70) | 0 / 0 |
| passA (Opus) | 0.082 (6/73) 0.038-0.168 | 0.057 (4/70) | 1 / 1 |
| passB (Opus) | 0.082 (6/73) 0.038-0.168 | 0.043 (3/70) | 0 / 0 |
| committed (= passC, reference; home advantage) | 0.069 (5/73) 0.030-0.150 | 0.029 (2/70) | -- |

The 5 wrong positions are the same 5 in passZ and in the committed reference: today's pipeline reproduced the folder's settled
reading exactly on scored signs; the 6th error is one inserted sign (passZ 96 signs per 97 committed; the reader/adjudicator split
L02.14-15 into X_NEW + T85 where passC has one sign). Of the 5, two are flagged align-conflict next to slip artefacts (L03.32 beside
the slip's dot run, L04.18 beside its inserted superscript "l") and L04.16 (T52 -> a) sits in the same stretch: treat the three as
truth-doubtful (a verifier pass from the f.151v slip image would settle them). L03.8 (T98 s vs slip "d" of "di") and L02.18 (T36 vs
slip "e") are the plausible real reader errors.

## Counts
97 positions (passC), 73 scored, 24 excluded: slip dots 11, unaligned 5 (L01.1-2 before "che"; L04.24-26 after "onore"), off-sheet
X_NEW 5 (the t-shaped m sign, exceptions_f152r.tsv), T88 2, align-uncertain 1 (single-segment). Flag align-conflict on 3 scored.
Pair agreement A/B 90/96 = 93.8% (nw); 6 disagreements + 37 agreed-uncertain went to the adjudicator (43 rows, all viewed; 5 changed
from first candidate). NO87-LABELS relabels: none apply on f152r (exceptions_f152r.tsv carries no X_CE row; its 5 rows are value
overrides read off the slip, not relabels).
Alignment control (truth build): interlinear_align agrees 63/97 = 0.649; GAPS4 statistic real key 0.612 vs 200 value-shuffled keys
mean 0.047, max 0.121, rank 1 of 201.

## Pool after this unit (tools/tx_power.py, 1000 draws, seed 1)
```
| eval | 34 | 642 | 0.3 | 0.863 | 0.971 | 0.000 | 0.000 | 0.128 | 0.361 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| eval | 34 | 642 | 0.5 | 0.999 | 1.000 | 0.001 | 0.012 | 0.687 | 0.891 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
```
Eval pool = eval_heldout 15 + spinelli 14 + f152r 5 = 34 baseline errors (>= 32): a clean 30% fixer passes p < 0.01 in 0.863 of
draws (the PREREG's 80% bar met). The unit alone (E 5) has no power; it counts only in the pool.

## Crops (pasted)
Final command (the auto line-finder took the prose line above as L01; the old manifest's centres put the cipher run on L01-L04 to
match the slip):
`python3 tools/iiif_lines.py --image ciphers/nevers-birago-fr3251-1572/harvest/f152r/src_ark_12148_btv1b9060248g_f154_4350_3700_3800_580.jpg --out benchmark-tx/txeng2/f152r/crops --prefix f152r --max-width 1250 --overlap 425 --follow-slope 400 --band-extent 0.1 --mask-neighbours --overlap-note --debug --centres 179,290,381,510`
(4 bands x 5 segments, drift +35/+91/+42/-5 px; overlay checked.) crops_note.md:
> - f152r: segments of a line overlap by 612 native px (the images you read are at native resolution, so 612 px in each image), about 14 signs (median sign width 45 px, ink-run median); a sign at the right edge of s1 and the left edge of s2 is ONE sign: the last 612 px of s1 and the first 612 px of s2 show the same ink, read it once.

## Protocol notes (deviations stated)
- Reader brief `blind_pass_brief_f152r.md` = the folder's `blind_pass_brief_1572.md` with the segment-overlap bullet replaced by
  crops_note.md's AND its f.178v "this page carries no prose" sentence replaced by the f.152r fact (prose before L01's run and after
  L04's); nothing about values. Readers opened only the brief, the blind sheet and the 20 crops (B also made enlarged copies in its
  own scratchpad). Adjudicator: `adjud_task.txt` + `adjud_queue.tsv` (TXE-Q shape).
- Truth: the slip's four lines joined into one span (its line breaks are not the letter's); dots kept as unread positions with
  interlinear_align `--wildcard .`; conflicts scored as in build_birago87.py, flagged in the new `flag` column.

## Calls and cost
3 vision subagents: 2 Opus passes (about 115k and 133k tokens), 1 Sonnet adjudication (about 117k). Dollar figure: the orchestrator's
get_session reading.
