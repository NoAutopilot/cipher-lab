# PREREG-R10-ZESBASIN: basin width of the word-parse objective on its matched control (6 Oct 2026, account-4, LANE-RUN10-account-4)

Written and pushed 6 Oct 2026 (09:44 UTC by date -u) before any scored run. The only run before this file is one
`basin_width.py --time` call (k = 32, draw 0), which printed the number of accepted swaps and elapsed seconds only; no
return fraction or J value was printed.

## What this is and is not
Not a search for the target's key and not a third search attempt (R9-ZESCH2 retired the objective under local search,
rule 3 third-attempt clause). It measures the landscape of the unchanged objective (`wordseg_syllabary.WordLM.llr`, 20-token
chunks, injective key, 7 pins fixed) on the unchanged matched control (`wordseg_syllabary.build_control()`: 2,666 tokens,
K 98, 91 free codes, 1 pct digit error; true-key J 1181.7). No target run in this job.

## Procedure (`basin_width.py run`, seed 10100)
- For k = 1, 2, 4, 8, 16, 32, 50 draws each (300 total): start at the true control key, apply k random code-code swaps among
  the free codes (swaps may overlap; the actual number of wrong codes is reported).
- One greedy pass: every unordered pair of free codes (4,095), in a per-draw shuffled order, swapped when it raises J
  (first-improvement). "Returned" = every free code back on its true unit.
- Reported per k: mean wrong codes at start, mean/min/max J at start, share of starts with J below the true key, return
  fraction, mean wrong codes after the pass, share of passes ending ABOVE the true key's J (a nearby higher optimum).
- The control can vary on the statistic: return fraction can be anything from 0 to 1 at each k, and a different objective
  (GAPS202's 4-gram, where the annealer beat the true key) would return poorly; nothing fixes it by construction.

## Decision rule (pre-registered)
- Basin width w = the largest k with return fraction >= 0.50.
- w >= 8 (a start with about 16 wrong codes of 91 still returns): WIDE -- the objective is usable by a genuinely different,
  near-key instrument (a crib-seeded or partial-key-seeded start, or an exhaustive near-key enumeration) if such a seed can
  be got within about w swaps; the named next step is the source of that seed, not a further blind search.
- 1 <= w <= 4: NARROW -- the objective is usable only from an almost-exact key; with no such seed source in hand (7 grade-I
  pins only) it is retired as a key-rebuild objective at this N.
- w = 0 (even k = 1 does not return half the time): NO BASIN -- the objective is retired at this N.
- In addition, a share of passes ending above the true key's J >= 0.10 at any k <= 8 means the true key is not the local
  maximum of its own neighbourhood: logged as a defect of the objective whatever w is.
- Cap 3 USD, box 09:43-10:38 UTC (80% about 10:27); a run that cannot finish by 10:27 is not started.
