# FT4ab pre-registration (account-4, 3 Oct 2026, written 17:3x UTC by the clock, pushed before any run of align/ft4ab_readout.py)

Step (FT4aa's next, ROOM 17:17 UTC): value readout on FT4aa's two decisive locators. With 121 = s pinned (C, VERIFY-ROU121),
release exactly {338} in F206 for pair A (F206 + F216V) and exactly {347, 534} in F206 for pair B (F206 + f.266r S1), and
enumerate every chunk each released code can take under exact fit.

Instrument: FT4x/FT4z/FT4aa's exact (0-edit) CP-SAT, unchanged except two read-only additions: (i) the target codes are always
modelled with a chunk variable even when they occur once (otherwise a single occurrence is an anonymous gap); (ii) a solution
loop: solve, read the target code's chunk, forbid it, re-solve, until INFEASIBLE (enumeration complete) or a solve is
unresolved (enumeration incomplete). Pins 22 de, 66 r, 581 au, 121 s, '#SEP' |; 722 free; MAXLEN 12; 30 s per solve.
Codes read out: pair A R338 (F206's 338) and 338 (F216V's, 2 occurrences); pair B R347, R534 (F206's) and 347, 534 (S1's),
each enumerated separately.

What counts as a unique readout: the enumeration for that code is complete (ends INFEASIBLE, no unresolved solve) AND it has
exactly one feasible chunk. Anything else is "not unique" (list the set) or "incomplete".
Witness consistency (only for a unique F206-side value v of code c): pin c = v in each other transcribed block containing c,
solved alone exactly (pair A: F216V; pair B 347: S1, S2, F249; 534: S1, S2) -> fit / nofit / unresolved; plus whether v equals
the current key.tsv value. Consistent = fit in every one of them.

Grading (stated now): FT4aa's controls were non-discriminating on two-release specificity (all 160 draws stopped at
release-all nofit), so the locator itself is not control-backed for specificity. Any readout therefore stays M unless it is
unique AND witness-consistent; even then no key or grade change by this worker -- a ROOM.md VERIFY flag line only, key change
only after a separate verifier. No status change. A non-unique or inconsistent readout: rule-4 note only.
No control is run in this step: the enumeration is a readout of an already-located site, not a gate (rule 3: no negative or
gain is claimed from it). Rule 3 count: the pooled-exact instrument's fourth use, first as a value enumeration.
Box 17:30-17:55 UTC, stop line 17:50. Cap USD 2. Script only, no vision, no subagents.
