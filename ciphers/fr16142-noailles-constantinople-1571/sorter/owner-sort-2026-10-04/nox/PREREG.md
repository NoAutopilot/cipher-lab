# NOX-OWNERSORT pre-registration (account 3 worker, 4 Oct 2026, written ~07:40 UTC before any statistic is computed)

Input: `../settled_labels.tsv`, `../summary.json` (owner's quick pass: 18 pile merges, 36 moves, 4 bad cuts).
Readers: RUN2-NXTA passA/passB (c510, 37 lines) and RUN2-NXTB passA/passB (c516 18 lines, c515 L01-L20), each pass kept separate.

## Placement of reader signs on atlas tiles (fixed before looking at merges)
Line map (from sorter/build_inputs.py, N4-NXS): NXTA c510_Ln -> atlas c510 L(n+5); NXTB c515_Ln -> c515 Ln;
c516a_Ln -> c516 Ln; c516b_Ln -> c516 L(n+5) for n<=3, L(n+4) for n>=6; c516b L04/L05 (both on the blot line L09) dropped.
Two placements, both reported: P1 = the build's same-fraction rule (column/columns -> tile index); P2 = per-line
Needleman-Wunsch alignment of reader labels to atlas tiles, scored by log P(label|cluster) re-estimated by hard EM
over all lines (5 iterations, both passes pooled for estimation). P1 is the primary placement (label-blind).
Reader labels: trailing '?' stripped; '?{...}' descriptions kept as their own labels.

## Step 1 statistic, per merge (a -> b)
S(a,b) = sum_l pA(l) pB(l) over reader labels, where pA/pB are the label distributions of reader-placed tiles in piles
a and b, computed per pass and averaged over the two passes of each reader group.
Null (matched control): for pile a take the 8 original piles nearest a in tile count (excluding a, b), likewise for b;
all 64 cross pairs, same statistic. Corroborated: S above the null's 90th percentile AND both piles >= 8 placed reader
signs; not corroborated: both piles >= 8 placed signs and S at or below the null median... otherwise "weak" (between)
; readers silent: either pile < 8 placed signs. Decision on P1; P2 reported beside it.
Supplementary (not a gate): the same S from run2/nxatl/cluster_provisional_names.tsv (c262 tile-position labels).

## Step 2
err_true: not measurable unless BENCHMARK-TX.tsv has a fr16142 row (checked: 0 rows on 4 Oct 2026).
err_2reader (A vs B) is a property of the reader passes and is unchanged by a sort that relabels tiles; reported as is.
Measured instead: pile impurity against the readers' agreed signs (tiles where pass A and pass B give the same label,
placement P1): weighted impurity = 1 - sum_pile max_l n(pile,l) / N, before (atlas clusters) vs after (owner piles).
Control: 200 random sets of 18 merges between size-matched piles (same rule as step 1); the owner's delta is compared
with that distribution. Also conditional entropy H(label | pile) before/after.

## Step 3
Mixed piles: piles with >= 15 agreed placed signs whose top two agreed labels each hold >= 25% and decode to different
plaintext under key.tsv, ranked by n x (second share); plus kNN split share from sequences.tsv (share of tiles whose k1 is
not the own cluster). Tiles: in those piles plus the moved/merged piles, tiles where the readers agree on a label that
is not the pile's majority and decodes differently, ranked by (2 readers agree) x (letters differ) x (1 - own kNN share).
At most 3 piles + 40 tiles -> next_targets.tsv.
