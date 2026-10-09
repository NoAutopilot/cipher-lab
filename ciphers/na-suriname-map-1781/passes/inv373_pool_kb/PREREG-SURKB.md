# PREREG SUR-KB (9 Oct 2026, 15:5x UTC by date -u; pushed in its own commit BEFORE any draw; kb.py pushed with it, unchanged after)
LANE FAMILY-A2j (account 2), job SUR-KB. Question (SUR-PARTIAL's and V-SUR0745's next): score.py (b)'s SPLIT statistic and its power curve
(SUR-POOLPC, SUR-PARTIAL) both carry the aligner's [y-fam]={m,n} steer. Does a key-blind statistic -- T without the [y-fam] row, so the DP
aligner earns nothing for putting a y-family sign on gloss m or n -- detect a second m sign at the pooled 65 lines, and what does the real
pooled key-blind S show? CPU only; no fetch, no vision, no transcription.

## Design (kb.py; imports poolpc.py unchanged, then removes '[y-fam]' from the shared T before any alignment it uses)
- Units: the same 65 pooled lines (0744 L, 0744 R, 0745 L), passes A and B, loaded by poolpc.py / 0745 L score.py load() unchanged.
- Statistic: S = n/(m+n) over y-family tokens that the KEY-BLIND DP aligns to gloss m|n (V-SUR0745's `--keyblind` S, pooled).
- Control (C1): deranged-gloss draws, the same derangement routine; K = 300 per synthetic unit, 10,000 for the real run.
- Verdict rule (poolpc.ctrl unchanged): LEANS n iff S > p99.5; LEANS m iff S < p0.5; non-test iff m+n < 10, < K/2 usable draws, or
  p0.5 == p99.5; else NO SPLIT SHOWN.
- Scaffolds rebuilt per pass from the KEY-BLIND alignment of the 65 real lines (facing distributions, deletion and insertion rates), so the
  synthetic generator does not carry the steer either. Planted arm: each gloss m drawn as [y-fam] is written 'Mx' with probability f.
  Under the key-blind T both 'Mx' and '[y-fam]' lie outside T, so a plant changes only which tokens are labelled y-family, never the
  alignment (the control can differ from H0 only through the statistic being measured -- rule 3's orthogonality check is met).
- Levels f = 0 (H0: false LEANS n rate), 0.25, 0.50, 0.75, 1.00; 100 units per level per pass scaffold at 65 lines; master seed 20261009.
  (100, not SUR-PARTIAL's 200, to fit the 60-minute box: SE of a detection near 0.8 is about 0.04.)
- `kb.py --selftest` (run before this file; it prints no real statistic and no verdict): key-blind matrix sums == stats() on 5 deranged
  draws; planted shares 0.269 / 0.524 / 0.760 / 1.000 on 20 draws.

## Gate (stated in advance)
- Power per f = LEANS n share among H1 units, per scaffold. A level is TESTED only if power >= 0.80 on BOTH scaffolds; a level below that is
  a non-test at that f. H0 false-LEANS-n must be <= 0.05 on both scaffolds, or the whole curve is void (the statistic leaks).
- Then, and only if at least one level is tested, `kb.py --real` scores the real pooled units (10,000 draws, seed 20261009).
  Unit verdict = both passes agree; else "not shown (passes disagree)".
- Read-out: a real NO SPLIT SHOWN excludes, at power >= 0.80, a second m sign used on a share >= f*_kb (smallest tested level); levels below
  f*_kb are not excluded. A real LEANS n on both passes is a signal for a second m sign (to a verifier, no key change). A real LEANS m on both
  is reported as such (a second n sign is not planted, so its power is unmeasured). Any between-level figure is labelled an interpolation.
- Compared descriptively with SUR-PARTIAL's steered curve (f* = 0.75): whether the key-blind statistic is sharper or blunter.

## Stated limits
300-draw p99.5 per synthetic unit (noisier than 10,000); only a second m sign is planted; the scaffold's facing distributions come from an
alignment that is itself noisy without the steer (y-family tokens then face other letters too) -- the generator and the statistic share it.

## Consequences
Whatever the result: no edit to key.tsv, key_period_*.tsv, conflicts.tsv, any transcription file, token grade, earlier .out file or N-class.
HYPOTHESES.md row with both numbers, NOTES section "SUR-KB (9 Oct 2026)", Remaining gaps / Escalation, gaps_check. Rule 10: report only;
to a verifier if the real statistic moves.
