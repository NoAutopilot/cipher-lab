# FT4z pre-registration (account-4, 3 Oct 2026, written 16:4x UTC by the clock, pushed before any run of align/ft4z_pool.py)

Step (FT4y's Verdict): a pooled exact pin run of the passages that each fit with no edit -- f.206 (ciphertext.txt / slip_f206r.txt),
f.216v (ciphertext_f216v.txt / slip_f217r.txt), f.266r S1 (FT4s segment, groups 0-74) -- on the disputed f.206 split values
121 ons, 188 lar, 834 kowitz, 344 mee, 24 in, 534 ches (FT4u S2 / FT4v f.252r disputes) and 253 (FT4x).

Instrument: FT4x's, unchanged (`align/ft4x_pool.py` solve_exact, imported by `align/ft4z_pool.py`): segment CP-SAT, zero edits,
blocks joined by '#SEP' pinned to '|', a code in two blocks carries one chunk in both. C pins 22 de, 66 r, 581 au; 722 free;
M values not pinned; MAXLEN 12; 30 s per solve; unresolved counts high.

Testability, fixed before any solve by occurrence counts only (code listing, no solver): a disputed code is testable here only
if it occurs in at least two of the three blocks. Counts (F206, F216V, S1): 121 (1, 5, 5); 534 (1, 0, 1); 188, 834, 344, 24
(1, 0, 0); 253 (0, 0, 1). **Only 121 and 534 are testable; 188, 834, 344, 24 and 253 are NOT TESTED by this pool** (each occurs
in one block, so no joint pin exists) -- that is a fact of the material, not a result.

Stage 0 (facts, not a score): each block alone exact; each pair exact. A block with no exact fit alone is dropped (FT4x
addendum rule: it would make J nofit for real and controls alike, a control that cannot differ).

Statistic: J = pooled exact fit / nofit (proved infeasible) / unresolved, on F206 + F216V + S1.
Controls, run FIRST, seed 3, n 40, only S1 perturbed (f.206 + f.216v stay real; FT4d already pooled those two):
(s) S1 slip words shuffled; (g) S1 group order shuffled. Share = (fit + unresolved)/40.
Power check before the real run: if either share > 2/40, **NON-INFORMATIVE (power)**; J_real reported as a readout only.
Gate (both shares <= 2/40):
  - J_real fit -> **PASS**. Readout for 121 and 534: every substring (len <= 12) present in every block that carries the code is
    tried as that code's pin; feasible set reported (10 min cap; unfinished = not scored).
      * feasible set = exactly one chunk v: decisive. v == key M value -> key.tsv row M -> C candidate; v != key value -> key.tsv
        row value change candidate. Either way a ROOM.md VERIFY flag line, and the key.tsv edit is made only with the note
        "FT4z PASS, pending VERIFY" (grade C only if no existing C row conflicts); never a status change.
      * key M value feasible among several -> not decisive; 'ons'/'ches' stays M, consistent with these three passages; the
        S2 / f.252r disputes logged as rule-4 conflicts with witnesses (f.206 slip split vs f.266r S2 / f.252r gloss).
      * key M value infeasible (others feasible) -> the M value is excluded by these three passages: key.tsv note "excluded
        by FT4z pooled exact (F206+F216V+S1)", grade stays M (no single replacement) unless the feasible set is one chunk.
  - J_real nofit -> rule-4 conflict readout (no key edit): the three no-edit passages cannot be jointly exact under the C pins;
    post hoc (not registered) which shared code releases restore a fit.
  - J_real unresolved -> NOT SCORED.
Rule 3 third-attempt note: the pooled-exact instrument's second use (FT4x first, f.252r question); on the 121/534 values it is
the first exact pooled test (FT4u used the one-edit S2 gate, FT4v the f.252r pair).
Box 16:37-17:07 UTC, stop line 17:01. Cap USD 3. Script only, no vision, no subagents.

## Addendum (16:4x UTC, after stage 0 only; no control or real J run yet)
Stage 0 (`align/ft4z_stage0.out`): F206, F216V, S1 each exact fit alone; **F206+F216V nofit, F206+S1 nofit**, F216V+S1 fit.
A pool containing F206 is therefore nofit for the real run and for every S1-perturbed control draw by construction (F206+F216V
already nofit, a control that cannot differ, rule 3), so by the FT4x addendum rule F206 is dropped. Pool: **F216V + S1**.
Testable disputed codes now: **121 only** (5 + 5 occurrences); 534 is NOT TESTED (S1 only once remaining). Controls, gate and
the 121 readout exactly as registered above, on F216V + S1 (carriers of 121: both blocks).
Secondary readout, registered here, no gate, licenses nothing on its own (pairs with no control): for F206+F216V and F206+S1,
each code shared with F206 renamed in F206 alone (one release at a time); list the single releases that restore an exact fit.
If 121 is among them for both pairs, that is reported as the f.206 split '121 ons' being the joint-inconsistency candidate
(rule-4 conflict, witnesses named), no key edit.
