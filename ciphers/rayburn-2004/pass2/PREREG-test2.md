# PREREG test 2 (R8-RAY2, 6 Oct 2026, written and pushed before the scored run)

Question (spec test 2, diagram hypothesis): Schmeh's reading is that each symbol is an object whose underline (U) or
strikethrough (S) records an action done to it. That mechanism predicts the mark is a per-object state, independent of
the label's typographic form. During reconciliation (before any count) the worker noticed that capitals look underlined
and lower-case letters look struck. If the mark is predicted by case, the mark carries little or no per-object
information and the "crossed out after an action" mechanism loses its main support (it does not exclude a diagram of
some other kind).

Data, fixed before this file: pass2/passB_raw.tsv, the blind Sonnet pass (R8-RAY2, 6 Oct 2026), whose transcriber was
told nothing about case or this hypothesis. Its own symbol case and its own mark column are used as written; no
worker edits.
Tokens scored: group main only; rows 1-10; mark in {U,S} (a '?' mark is excluded); first character of the symbol is an
ASCII letter (a composite like 'A+m(below)' scored by its first letter; an alternative 'u/v' scored by its first
alternative). Excluded as edge bleed from the margin columns (named before the run from the reconciliation, not from
marks): main r1 pos6, r4 pos8, r5 pos8, r6 pos6, r7 pos1 ('t/+' left fragment), r6 pos1 ('W/m' fragment) -- the last
two are real grid tokens (b, w) that pass B read only as fragments.
Statistic: agreement A = share of scored tokens where (upper and U) or (lower and S).
Control: 10,000 random permutations of the mark values across the same scored tokens (the control varies exactly the
pairing the statistic measures, so it can differ from the target). Report A, the control mean, its 95th percentile and
the one-sided p = share of permutations with A_perm >= A.
Secondary (reported, not gated): the same on letters whose case is not size-only (exclude c k o s u v w x y z).
Gate: case-mark coupling is "supported" if p < 0.01 and A >= 0.85; "not supported" if p >= 0.05; between is "unclear".
Script: pass2/test2_case_mark.py (seed 20261006).
