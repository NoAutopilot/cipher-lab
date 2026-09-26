# dict/ -- ARM3-DICT, family G dictionary-code test (26 Sept 2026)

`dict_control.py` (offline, stdlib): builds a fresh en18-derived pocket-dictionary vocabulary (NOT WE028's real
words), sorted alphabetically, mapped linearly onto values 100..(100+K-1) with the particle block (1-99) kept
separate, at K=1600 and K=1800; runs 60 simulated 369-token en18 control letters per size; compares the target's
own `units_top1` (already computed by `../design/design_stats.py`, cited from `../design/stats_sim.tsv` for
`onepart`/`seq_pblock`/`hdec`/`twopart`) against this fresh control's distribution. Full numbers and verdict in
`../HYPOTHESES.md`'s "Family G, ARM3-DICT dictionary code" section. `dict_stats.tsv` is the script's own raw
output (rerunning `python3 dict_control.py` regenerates it deterministically, seed 1).

Verdict: design exclusion (target 12 sd outside the control on the pre-registered statistic). U2-U4 (fetching
Entick/Johnson/Perry/Sheridan-Walker OCR from archive.org) were not run, per the brief's own gate -- U1 already
rejects the design at far beyond p<0.05.
