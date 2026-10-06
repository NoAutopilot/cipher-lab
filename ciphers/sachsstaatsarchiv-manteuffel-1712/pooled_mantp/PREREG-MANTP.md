# PREREG-MANTP -- pooled single-code-gloss gate (R7-MANTP, 6 Oct 2026, LANE LANE-RUN7-account-2, account 2)

Written and pushed before any pooled score was computed (clock 01:2x UTC 6 Oct 2026 by date -u). The single-code glosses in
the four leaves have been read by earlier workers (their pairs.tsv files are on disk), so this is a pre-registration of the
statistic and the decision rule, not of blindness to the data.

Data (as committed, no edits): single-code runs (cipher_raw has exactly one token) from
f0500_0502/pairs_0502.tsv (leaf 0502), f0501/pairs.tsv (0501), f422v_0527/pairs.tsv (0527), f423_0528/pairs.tsv (0528).
Gloss normalisation: MANT5 exactly (f0500_0502/gloss_norm.tsv: r->roy, pr->prince, pol->pologne as whole tokens; lower case;
. , ; : ' " as token breaks). Articles and spelling variants are NOT normalised.

Statistic S: among codes with >= 2 single-code runs in the pool (N_rec), the fraction whose normalised glosses are all identical.
Control: the gloss strings permuted across all single-code runs of the pool (codes and run positions fixed), 1000 draws, seed 7101.
The control can vary on S (a permutation changes which glosses meet which code). Gate: PASS iff N_rec >= 3 AND S_real > shuffle p95
(strictly). Also reported, not gating: shuffle mean, and S_real vs a per-leaf shuffle (glosses permuted within each leaf only).

Per-unit rule (CLAUDE.md rule 3, per-unit merge paragraph). Each leaf's own control, same instrument: its own single-code runs, glosses
permuted within the leaf, 1000 draws, seed 7101 + leaf number; leaf cleared iff N_rec_leaf >= 3 and S_leaf > its p95. A leaf also counts as
cleared if its registered per-leaf gate already PASSed on file (0502: PREREG-MANT5 PASS; 0528: PREREG-GAPS195 PASS). 0501 (tied, MANT5) and
0527 (HELD, MANT27) are not cleared unless this instrument clears them.

Licensing (only on a pooled PASS): a code with >= 2 agreeing single-code glosses enters/changes in key.tsv at
- C if at least one occurrence is on a cleared leaf AND at least one occurrence's gloss_grade (the leaf's reconciled.tsv) is C;
- M otherwise (held: value attested only on uncleared leaves, or every gloss reading M).
Codes with disagreeing glosses are not licensed. An existing key.tsv entry is never downgraded by this job and a Krauske row is never
overwritten (rule 4: a gloss value differing from Krauske's is logged in HYPOTHESES.md as a conflict, not merged). Single-attested codes
(one gloss in the pool) are never licensed by this gate.

Known-answer: every recurring single-code code that has a key.tsv value at C whose source is NOT one of these four leaves' glosses
(i.e. Krauske) is checked for agreement with that value; codes whose key.tsv value came from these glosses are reported but are circular.

Effects reported: decode_key --check exit, C/M/U counts before/after, and the number of f.409v / f.410 U tokens that move.
Script: pooled_mantp/pooled_gate.py. Disk only, no requests, no subagents.
