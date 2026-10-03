# Pre-registration: key no.71 (BnF fr.3995 f.133r, Gallica btv1b525085665 canvas f256) known-answer gate
GAPS-fr4715-vieuville-pool-14 (account-4), written 3 Oct 2026 03:2x UTC, committed BEFORE any scoring.

Disclosure: before writing this gate the worker looked once at a quarter-size overview of the leaf (to find the
table's layout for the crop cut). At that size some names were legible. The gate below is fixed before the crop
transcription and before any score is computed; the scorer (scripts/key71_control.py) is written to this text.

## Known answer A (gating): our C-graded word-code glosses
| code | mark seen on our leaf | gloss (C) | source |
|---|---|---|---|
| 7 | bar | Roy | f.60r L23 (x2) |
| 71 | bar | montolon | f.60r L01 |
| 93 | two dots | Mr | f.60r L01 |
| 14 | bar | Card de bourbon | f.62r L14 |
| 22 | bar (A only) | Soissons | f.51r S01 |
Match rule: the key's entry for that number in the layer the key's own mark convention assigns to that mark matches
the gloss after normalization (case, accents, u/v, i/y, dropped h; an abbreviation matches its expansion: Mr =
Monsieur, Card/C = Cardinal; a place gloss matches a title naming that place, e.g. Soissons ~ Comte de Soissons).
If the key's mark convention cannot be read from the leaf, a code matches if ANY word-code layer's entry for that
number matches, and the number of layers searched is reported (this widens chance; the control below uses the same
rule, so it widens the control equally).

## Known answer B (gating): the letter alphabet
The key's letter row (header) against key_vieuville_nevers.tsv's 33 numeric letter rows (Tomokiyo, proven on no.58).
Statistic: share of those 33 (sign, letter) pairs that the key no.71 header reproduces.

## Controls (must be able to vary on the statistic's own axis)
- A: gloss-label permutation over the 5 codes (all 120 permutations, exact distribution) AND random-code draws
  (each gloss given a uniform random number 1-100, 10,000 draws, same match rule). Both change which value meets
  which gloss, so both can fail differently from the target.
- B: letter labels permuted among the key no.71 header's codes, 10,000 permutations.

## Gate (PASS only if all hold)
1. A REAL >= 4 of 5, and A REAL > p95 of both A controls (strictly).
2. B REAL >= 0.80, and B REAL > p95 of its control.
If the gate fails: stop. No no.44 slot is read from the key; log "key no.71 not confirmed by our known answer" in
HYPOTHESES.md. If it passes: read no.44's six open slots (.03 x2, .07, .49, .57, .6) from the key, grade H only where
the slot's mark selects one layer unambiguously and the key cell is read clearly by two reads (pass + reconciliation);
otherwise M. The M-graded pairs (13 Narre, 27 nauarre?/Neuers, 52 Normandie, 44 Roy, 99 bours, 49 Champagne held)
are reported as data beside the gate, never used to pass it; conflicts go to HYPOTHESES.md (rule 4), not settled by
majority.
