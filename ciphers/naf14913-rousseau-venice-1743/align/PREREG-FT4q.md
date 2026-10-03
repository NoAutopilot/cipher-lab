# PREREG-FT4q (account-4, 3 Oct 2026, written 11:47 UTC by the clock; pushed before any part-1 or part-2 run)

Target: naf14913-rousseau-venice-1743. Worker FT4q. Script `align/ft4q_poly.py` (this commit). Question (FT4p's P1 next
instrument): is 722 polyvalent -- ti in f.206 (C) but another value in f.213 -- and what do the other passages say?

Facts fixed before the run: 722 occurs twice in f.206 (C, ti), twice in f.213 (both in "90 689 24 722", slip "garanti..."),
once in f.249 ("347 722 476", the same context as f.206's "347 722 476" = con-ti-nue; the f.250 slip carries "continuera"),
and **0 times in f.216v**, so f.216v cannot vary on this question: a non-test by construction (rule 3), not run.

Part 1 (f.213): Scorer.consistent, MAXLEN 12, group 73 dropped (FT4m), pins 22 de / 501 et, 722 tied at both occurrences;
every slip chunk occurring >= 2 times that is feasible is tried at 20 s; FIT / NOFIT / TIMEOUT listed; 'ti' always listed.
Part 2 (f.249): the FT4l one-edit model (one_edit_seg.solve, decomposition, sublimit 10 s) with 722's single occurrence
pinned to X (not releasable, not droppable): E_X for X = ti and for every part-1 FIT value (at most 4, shortest first).
Control (seed 3): n 20 random same-length chunks of the f.250 slip (X excluded), same E; share s_X, unresolved counted 1.
Discriminating only if s_X <= 0.10 (else part 2 for that X is a non-test: the pin does not constrain the fit).

Outcomes:
- Q1: E_ti = 1 with s_ti <= 0.10 and every f.213 value V gives E_V = 0 (or fails its own control): f.249 is a second witness
  for 722 = ti; f.213 needs a value other than ti at 722 -> logged as a 722 conflict confined to f.213 (polyvalent use or an
  encipherer/slip-spelling variant there), 722 in f.213 at grade I; key.tsv unchanged (722 ti stays C).
- Q2: some V gives E_V = 1 (control met) and E_ti = 0: f.206's ti contested by f.249 -> conflict per rule 4, witnesses logged,
  key.tsv unchanged in this job.
- Q3: both E_ti = 1 and some E_V = 1 (controls met): f.249 cannot decide between them.
- Q4: part 1 FIT empty (and no timeouts): 722 tied at both f.213 occurrences fits no value -> the f.213 conflict is not 722's
  monovalent value; polyvalence within f.213 itself (two different values) is the only 722 reading left; report.
- Any X with s_X > 0.10 or unresolved real E: non-test for that X.
Nothing moves in key.tsv in this job.
