# PREREG-GAPS195 (3 Oct 2026, ~18:50 UTC, account-4), written before any statistic is computed

Leaf: SHStA Dresden 10026 Loc. 694/08 ff.422v-423, film frame 0528 (sha256 0d6bfbd2...9eb0).
Material: two blind Opus passes per page half (crops from tools/iiif_lines.py --image), reconciled by the worker
against the crops. Units: a "glossed run" = a maximal run of code groups with a period interlinear gloss above it.

Pairs: one pair per glossed run (plain_raw = gloss as reconciled, cipher_raw = codes), aligned with
tools/interlinear_align.py align --floor 0 --max-chunk 8 --seg-bonus 1.0 --len-prior 0.5 (syllabic/word nomenclator;
no --prior, so no Krauske value seeds any code).

Statistic S (per leaf): among codes that occur in >= 2 glossed positions on this leaf, the share whose aligned chunks
are identical (folded) at every occurrence. Single-code glossed runs count as positions (their chunk is the whole gloss).
Control: the gloss strings permuted across the glossed runs (pairing shuffled, codes and gloss texts unchanged),
re-aligned with identical options, S recomputed; 200 draws, seed 195. This control varies the code/gloss pairing,
the axis S measures.
Gate (CLAUDE.md rule 3, Szembek paragraph): merge into key.tsv only if N_recurring >= 3 AND S_real > p95(S_shuffle)
strictly. A tie or a miss = the leaf is held: values go to a separate leaf file at grade M, nothing into key.tsv.

Grades if the gate passes: a code under a single-code gloss -> C; a code inside a multi-code run whose chunk agrees
at >= 2 occurrences -> C; any other code chunk from a multi-code run -> M (boundary inferred). A code whose gloss
contradicts an existing key.tsv value (Krauske 1893) is not overwritten: logged in HYPOTHESES.md as a data conflict
(rule 4), with both witnesses.
Also reported, not a gate: single-code glosses vs key.tsv where the code is in Krauske's table (agree / disagree).

## Addendum (3 Oct 2026, ~19:00 UTC), before any alignment or statistic was run
--max-chunk 8 cannot hold a name glossed over one code (Schonborn, Bartholdi, le Roy de Prusse: 9-13 letters), so it
would force a misalignment on every single-code gloss. Changed to --max-chunk 14 (the tool's own default); nothing else
changed. Also reported beside S (not a second gate): S restricted to codes occurring inside multi-code runs only, since
single-code name glosses repeat trivially (AX-NAMES per-class lesson, CLAUDE.md rule 3).
