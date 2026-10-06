# PREREG R11-ZESCORP -- era/register-matched control + fill-free pattern-rarity crib score (zeschau-seebach-1841)

Written 6 Oct 2026 before any control or target placement was scored (clock read with date -u, 13:49 UTC). Worker
R11-ZESCORP, LANE LANE-RUN11-account-4. Script: `crib_rarity.py` (disk only). Only earlier outputs: the corpus build
(letter counts) and `crib_rarity.py cribs` (the crib list below, computed from the fr1840 TRAINING files only; the
held-out control text was not read for it).

Why: R10-ZESCRIB's control was a non-test -- its Napoleonic plaintext held no multi-unit crib, and its J ranking of a
mostly frequency-filled key could not rank a partial key. This job changes both (the folder's Verdict "cheapest next"):
(1) the control plaintext is 1840s diplomatic French (new `tools/data/fr1840`: Nesselrode Lettres et papiers VIII-IX,
Metternich Memoires VI, Guizot Memoires VI-VII; held-out file `lettresetpapiers08ness`, Nesselrode 1840-46, chosen
crib-blind as the volume whose dates bracket the target's 1841-43 most tightly); (2) the placement score uses no fill
and no objective: pattern rarity plus cross-crib agreement.

## Cribs (fixed here, 63)
R10-ZESCRIB's 25 formulae unchanged, plus the top 40 word n-grams (2-5 words, >= 12 folded letters, no crib a substring
of an earlier one) of the four fr1840 training files, minus duplicates: as printed by `crib_rarity.py cribs` at 13:49
UTC (list stored in the output json's `cribs`). Editorial n-grams in it (notedelediteur, lememeaumeme) are left in, not
hand-pruned.

## Procedure
- Control: build_control()'s design unchanged (N 2,666 pooled R5005-R5007 pair counts, K 98, units = letters +
  multi-letter pins + top bigrams/trigrams by the same rule, 7 pins, 1 pct digit error, de19 German, offsets 5000)
  with French plaintext and unit inventory from fr1840; three keys (rng seeds 209, 210, 211).
- Crib tokenisation: greedy longest match, first and last token dropped. Arm B (GATED): attacker unit list built by the
  same rule from fr1810 training + de19 -- a list that is NOT the generator's, as on the target. Arm A (diagnostic
  only): the generator's own list.
- Admission: a window is admitted if code<->unit is one-to-one both ways inside it and it agrees with the pins.
- Rarity qualification (fill-free): a crib qualifies only if, over 40 order-shuffles of the French code streams
  (shuffle seed 11000; shuffling keeps code frequencies, breaks position), it is admitted at most 1 time in total
  (E_null <= 0.025 per stream). Every admitted placement of a qualifying crib on the real stream is accepted.
- Cross-crib agreement: every accepted placement that contradicts any other on a shared code or unit is dropped (both);
  the union of the rest is the seed. No objective J, no frequency fill, anywhere.
- Truth: a seed code is correct if the generator's true unit for that code equals the assigned unit string.

## Gates (arm B, mean of the three keys; all three must pass before the target is run)
- G0 testability: letter-level occurrences of QUALIFYING cribs in the control's French plaintext >= 3. Fewer -> NON-TEST.
- G1 seed precision: correct / seed codes (non-pin) >= 0.90.
- G2 seed size: correct non-pin seed codes >= 10.
- The control can vary on both statistics (precision 0-1, correct codes 0-91), and the shuffle null is position-based,
  the axis the pattern statistic measures (CLAUDE.md rule 3 orthogonality paragraph).
- Control below any gate -> CONTROL BELOW GATE, non-test at this N for this crib list and score; target not run;
  logged in HYPOTHESES.md. Arm A's numbers are reported but license nothing.
- If all pass: the same procedure on the pooled R5005+R5006 French pairs (attacker list from fr1840 training + de19),
  the same 40-shuffle qualification; output admitted placements and seed with the shuffle E_null beside the real count;
  nothing graded above M; verifier flag in ROOM.
