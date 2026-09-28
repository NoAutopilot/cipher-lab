# Candidate edits for a key v5 -- from campaign steps H119-H148 (runner 5, 28 Sept 2026)

For the family worker. The campaign does not edit KEY.md or key_period_v4.tsv; these are proposals with their evidence.
All evidence is model-free (fr16 4-gram beam) and uses the **sequence gain** statistic (real sign order minus 20 within-line
shuffles, compared across maps), which is null on shuffled text (H128, 1 of 25 shuffles in the top 10) and cannot be produced
by letter frequency alone (the plain rank can: H124). "Pool" = the reconciled drafts of fr.3982 f.97r, f.101r, fr.3984 f.188r,
fr.3982 f.124r (9,611 signs) with KEY.md's own equivalences (LOOPS = h/u, H24 = i/x, ZBAR = f/s). Bootstrap = 30 resamples
of the pool's lines. None of this is a period attestation (grade C); it is a text-fit check of cells the period counts propose.

| class | key v4 | proposal | evidence (file) |
|---|---|---|---|
| VBAR_A | t/s | **g/t** | pool: g/t beats t/s in 29/30 and 30/30 resamples; also higher on f.108v and on f.61's known lines (`scripts/f61vbar_cells_result.txt`, H146). v4's s 93 probably VBAR_B signs coded VBAR_A. |
| VBAR_B | s | **s** (f rarely right) | pool: s alone beats f/s 30/30; f.108v cannot tell (H146). Does not settle VBAR_B's second letter. |
| SBS | o/b/e (frac 0.1) | **b/o** | the added e is rejected, 0/30 (`scripts/f61v4_widen_result.txt`, H148) |
| 4PI | d/q/a/n | **d/q** | a/n rejected, 1/30 (H148) |
| HASH4 (4-over-hash) | d/q/i | **d/q** | i rejected, 0/30 (H148); on f.108r, where the passes do not separate the bare hash, HASH4 = i/x fits best (H118/H119) -- a coding question for that leaf, not the cell |
| 4TRI | c/p/t | c/p (t open) | t 6/30 (H148, open) |
| 4STEM | a/n/c/e | a/n (c/e open) | 7/30 (H148, open) |

Also for the family worker: f.61's 14-cell map puts all six family leaves "in f.61's cells" by sequence gain (f.97r, f.101r,
f.188r rank 1 of 201; f.124r, f.106r, f.274 at the edge; `scripts/f61seqgain_family_result.txt`, H129), and on the pool 128
of its 129 one-swaps lose (H132), though only the swaps with clear margins survive a bootstrap (H142: 13 of the 15 closest
are open). Refining f.61's own map with these cells did not improve the known-answer scores on f.61 (H147: 110 vs 111 of
125), so they are family-key candidates, not changes to f.61's map.
