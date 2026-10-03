# FT4x pre-registration (account-4, 3 Oct 2026, written 16:0x UTC by the clock, pushed before any run of align/ft4x_pool.py)

Step (FT4w's Verdict): a pooled pin run of f.252r with the passages sharing its codes (527/253/369/213 and any other f.252r code
that recurs), testing whether those shared codes are jointly consistent with the current key. The one-edit family is [retired]
for f.249 (FT4w, rule 3), so the instrument here is different: **exact match, zero edits** (no release, no drop).

Instrument (`align/ft4x_pool.py`, written before this file, not yet run): ft4s_seg's segment CP-SAT, edits forced to 0, on one
concatenated model -- blocks joined by a separator token pinned to '|', so a code that occurs in two blocks must carry one chunk
in both (the joint pin). Blocks: f.266r S1 (groups 0-74 / slip to 'le Bressan', FT4s GATE PASS, fits with no edit), f.266r S2
(groups 76-138, FT4u GATE PASS), f.252r (15 groups / primary expanded gloss, PREREG-FT4v). f.249 enters only as its FT4t segment
(groups 39-100) and only if stage 0 shows that segment fits exactly on its own; the whole f.249 pair is proved to have no exact
fit (FT4e), so it cannot enter an exact model. C pins: 22 de, 66 r, 581 au, every occurrence; 722 free (undecided); M values not
pinned. MAXLEN 12, 30 s per solve, unresolved = counted high.

Stage 0 (facts, not a score): each block alone, exact; the list of f.252r codes shared with each block.

Statistic: J = pooled exact fit / nofit (proved infeasible) / unresolved.
Controls, run FIRST, seed 3, n 40, only the f.252r block perturbed: (s) f.252r gloss words shuffled; (g) f.252r group order
shuffled. Share = (fit + unresolved)/40.
Power check before the real run (the brief's condition): if either control share > 0.05 (> 2 of 40), the gate cannot pass ->
**NON-INFORMATIVE (power)**, and J_real is then reported as a readout only, licensing nothing (and the exact-pooled instrument is
logged as not able to discriminate at this length).
Gate (only when both shares <= 2/40):
  - J_real fit -> **PASS**: f.252r's gloss is jointly consistent with the shared codes' chunks in f.266r under the C key, at a
    rate the controls do not reach. Then the uniqueness readout: for each shared code, every gloss substring (len <= 12) is tried
    as its pin; a code with exactly one feasible chunk is a **C candidate** (decisive outcome) -> key.tsv row (or note on an existing
    M row that it is now witnessed/disputed), grade C only if no existing C row conflicts, plus a VERIFY flag line in ROOM.md.
    Readout capped at 10 min wall clock; unfinished codes are not scored.
  - J_real nofit -> the f.252r gloss (as expanded) cannot be exactly consistent with f.266r S1/S2 under the C key: a rule-4
    conflict readout (misread, paraphrased gloss, or polyvalence), no key edit; the 'literal' and 'est' gloss texts then run as a
    secondary readout only.
  - J_real unresolved -> NOT SCORED.
Box 16:00-16:30 UTC, stop line 16:24. Cap USD 3. Script only, no vision, no subagents.
