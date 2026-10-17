# PREREG-VIV-KCELLS -- p/m/f key cells by whole-stream alignment on the deciphered sibling pairs

Written 17 Oct 2026 02:2x UTC (date -u), before any scored run. Worker VIV-KCELLS (account 4), brief
`.claude/briefs/runs/2026-10-17-acct4-research-director-4.md` JOB VIV-KCELLS. Disk only; no readers, no vision calls.

## Question
key.tsv has no H/C code for p, m, f (nor k, x, y; only M rows for b, h, z). ERR-SIM showed the key, not reader error, caps every
ink-63 clause. With a whole-stream alignment (not VIV-ANCHOR's word windows, retired), which reader labels carry p, m and f on the
deciphered sibling pairs, and at what share?

## Instrument (fixed now)
`tools/stream_align.py` (= `tools/interlinear_align.py stream`), its library functions `emissions` and `band_dp` (banded monotone DP,
one letter per cipher sign, cipher-side and clear-side gaps 1.5, alpha 0.5, band 150, growing window step 300), driven by
`tx/kcells/kcells.py`. One change from the tool's flat-start `learn` (which failed on ink 40, VIV-K arm A 2/30): the emission matrix
is seeded from key.tsv's **C rows only** (every C label -> its letter, 10 pseudo-counts); M rows (S, A, y, b, e) and all other labels
start neutral (emission 0 for every letter). Hard EM, 3 iterations per window: keyed rows keep their prior plus path counts; unkeyed
labels learn from path counts only. The start offset j0 per pair is located with the C key exactly as tx/vivk_test.py does (80
signs vs 120-letter windows, step 5, refine +-5). Tool is untested below N 200 (HEID-1623CAL); every pair here has N >= 500 signs.

## Pairs (brace nulls `{...}` dropped, tokens via tx/vivk_test.tokens, "o o" -> oo)
- P40: ink 40 f102r+f102v+f103r (_rec.tsv) vs tx/dec_norm.txt (clerk's ink 41, ff.105v-108v merged).
- P67: ink 67 f201r+f201v (_rec.tsv) vs tx/dec67_norm.txt + tx/dec67b_norm.txt.
- P70: ink 70 f211r+f211v (_rec.tsv) vs tx/dec70_norm.txt.
Each pair run separately; "pooled" = the per-position tallies summed over the three pairs (one alignment per pair).

## Known-answer control (run first; gates everything)
Leave-one-letter-out: for each of the 14 C letters X (a c d e g i l n o q r s t u), remove all of X's C rows from the seed (X's labels
start neutral like p/m/f do), align every pair, and tally the cipher labels at clear positions whose letter is X (matched pairs only).
X is **recovered** when, pooled, the top label at X positions is one of X's own C labels in key.tsv and X's C labels together carry
share >= 2/3 of those positions (homophones: a has s, P, z; the union is X's cell set). Gate: recovered >= 10 of 14.
Shuffled control: the same 14 leave-one-out runs with each decipherment cut into consecutive 60-letter "lines" (about one manuscript
line) and the lines permuted (20 shuffles, seeds 0-19). Gate: mean recovered < 4 of 14 (and reported as max too).
Gate fails (either) -> NON-TEST, stop, no cell proposed, log.

## Target (only after the gate passes)
Full C seed (no letter held out). For p, m, f, k, x, y, b, h, z: every label's count and share at that letter's aligned positions, per
pair and pooled, plus each label's purity (its own top letters over all its aligned positions, pooled).
Cell proposed only at: pooled share >= 2/3 and n >= 10 for that label at that letter, and share >= 1/2 on each pair with n >= 5 for the
letter. (b, h, z: M rows today; a label meeting the rule for them is reported, upgrade proposed in NOTES, not applied by this job.)

## Decision rule (pre-registered)
(a) p and/or m (or f) cells meet the rule: add them to key.tsv at grade C (source: this job, counts), re-decode with the committed
decode scripts (`--check`, rule 7), report grades before/after, ink 63's longest all-H run, and rerun tx/err_sim/err_sim.py on the
extended key. (b) the letter's positions scatter with no label above 1/2: T1 confirmed for that letter (labels merge the sign); write
tx/kcells/<letter>_positions.tsv (page, line, pos, label); no key edit. Between 1/2 and 2/3, or n < 10: report, no key edit, positions
written as in (b). (c) gate fail: non-test.

## Decision
Belief: the clerk pairs carry p/m/f at stable reader labels the key simply never named (VIV-ANCHOR's windows could not anchor them).
Would change it: LOO control recovered >= 10/14 with shuffle < 4/14, then p/m labels below 1/2 share (merged signs) -> T1, tile reader next.
Observed: LOO known-answer control 12/14 recovered (l and q missed: l top label y 170 of 373, own share 0.483; q own 0.567) vs chunk-shuffle mean 2.95/14 (max 5, 20 shuffles): gate PASS; target (p/m/f) not run -- the control ended at 03:03 UTC, past 80% of the 45-min box (02:21-03:06).
Decision: continue -- run `tx/kcells/kcells.py --target` (about 30 s, no new gate) in a fresh box and apply rule (a)/(b) as registered; no key edit by this job.
Lesson: a key-seeded whole-stream DP passes a leave-one-letter-out known-answer gate on these pairs where the flat-start stream tool failed (VIV-K 2/30); price the 21x14 control at about 40 min on 4 CPUs, not minutes, before the box.
