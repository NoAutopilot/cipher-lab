# H27 pre-registration (campaign runner armstrong-madison-1808, owner account, session_01NuaRiPghx6VRXA6GuJE8ne)

Written 28 Sept 2026 01:50 UTC, before any synthetic letter was built or any solver run.

**Question.** Does ARM3-LOOP's model-in-the-loop crib loop have the power to recover the ROOTS of a two-level
decade/slot nomenclator (ARM-DESIGN family C) at the target's length, when the solver is given the slot grammar
(slot 0 = root, slot 1 = plural/past, the other slots fixed suffix classes for the whole book)?

**Design simulated** (`tools/families/nomenclator.py --param slot_grammar=1`, added this step): en18 held-out text
(Jefferson Vol IX, holdout 5, never in the LM), 369 coded tokens (the target's own count on ciphertext.txt), the
target's wildcard-run shape; particle block = 99 values at 1-99 (cold, as ARM-C1/ARM3-LOOP); book = 180 decades,
one root lemma per decade, its inflected forms at fixed slots: 0 root, 1 plural or past (whichever form of that root
is the commoner in the register), and the eight remaining suffix classes (ing, er, ly, ion, ment, ness, est, able)
at slots 2-9 in a per-book random order. The solver is TOLD the slot map (the most favourable case): its unknowns are
99 particle words and one root per occupied decade.

**Metric.** Root recovery = share of decades occurring in the letter whose solved root equals the true root
(hidden.json `roots`, never opened by the reader). Also reported: blended / particle / book token accuracy as in
ARM3-LOOP, and the blind seed-to-seed spread.

**Gate (the row's, fixed here).** Mean root recovery over 3 seeds >= 30 percent on the loop's best round (blind or
any crib round) licenses one target run; below it, the power result is logged and the target is not run. ARM3-LOOP's
own gate stands for the crib gain: a gain over blind counts only if it is >= 10 points blended AND above the blind
spread. Headroom check (rule 3): the blind root recovery must be reported and be under 95 percent for a crib gain to
mean anything; if blind root recovery is already >= 30 percent, the loop is not needed and the target run is licensed
on the blind solver alone (the row's condition is on "the loop", read as blind + rounds).

**Reader protocol.** The reader is this session, seeing only `crib_rounds.py --view` output (decode, value ids,
confidence digit, three contexts) and the score verb's numbers; at most 12 cribs a round, at most 2 crib rounds per
seed (box 60 min, cap 5 USD). Seeds 2, 3, 4 (seed 1 reserved as in ARM3-LOOP).

**Known caveat, stated before running.** ARM-DESIGN Q3 found the target's decades used more evenly than root plus
en18 inflections (a 180-root book covers about 45 percent of content tokens); the simulated design therefore has
more wildcards and a more concentrated units-digit distribution than the target. This is the solver-FAVOURABLE
direction (fewer unknowns, a known grammar): a FAIL here is conservative for a stop decision, a PASS would still have
to survive the target's less structured book.
