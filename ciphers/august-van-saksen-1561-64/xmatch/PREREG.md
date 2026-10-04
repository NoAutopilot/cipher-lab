# N4-XM pre-registration (4 Oct 2026, written 04:18 UTC before any control statistic was computed)

Worker N4-XM (account 2, for LANE-NEAR4), brief `.claude/briefs/runs/2026-10-04-ytbiz-near4-wave1.md` section N4-XM.

## Question
The key_crossmatch nightly of 4 Oct 2026 02:53-02:54 UTC (ROOM.md) reported
`ciphers/fr3993-villeroy-1595/keys/key_f159_letters.tsv` reaching the calibrated gate
(`tools/data/key_crossmatch_gate.json`: stat >= 3.292, n >= 100, coverage >= 0.5) on three August van Saksen
ciphertexts: ciphertext_58_sample.tsv 8.66, ciphertext_74.tsv 7.22, ciphertext_57.tsv 6.48. Is that a property of
this particular key (a lead) or of any letter-alphabet key of the same size whose numeric codes overlap the AVS
notation (a generic letter-frequency artefact)?

## Matched control (fixed before computing)
Control keys: every key file the tool itself discovers (`find_key_files` + `load_key_meta`, same loader as the
nightly), excluding the fr3993-villeroy-1595 and august-van-saksen-1561-64 folders, such that
1. it is a letter alphabet: >= 80% of its rows carry a single-letter value (f159: 39 of 39);
2. its count of single-letter-valued rows is within 20-58 (f159: 39, +-50%);
3. its coverage (the tool's `coverage_of`) is >= 0.5 on all three AVS ciphertexts -- without this the tool cannot
   score the pair at all, so a control below it could not reach the gate by construction (CLAUDE.md rule 3,
   "a control that can differ on the statistic").
From the keys meeting 1-3, take the three closest to 39 in single-letter-row count (ties: path order). If fewer
than three qualify, take all that do and say so; if none qualifies, relax 3 to coverage >= 0.5 on at least one
of the three ciphertexts and report it as a relaxation.

Each control key is run through the same tool functions (`get_model` in the key's own tool-assigned language,
`pair_stats` with 20 class-shuffled keys, seed 0, `gate_verdict`) on the same three tokenised ciphertexts
(`tokenize_ciphertext`). f159 is re-run the same way in the same script (its own numbers must reproduce the
nightly's within rounding, else the script is wrong and nothing is concluded). Secondary, descriptive only: the
same controls scored under f159's own tool-assigned language model.

## Decision rule
- "generic letter-frequency artefact": at least one control key reaches stat >= 3.292 (with coverage >= 0.5,
  n >= 100) on at least one of the three ciphertexts that f159 reached.
- "survives the size-matched control": no control key reaches the gate on any of the three.
Either way the result is about the tool's statistic, not a reading. The by-eye read (30 tokens of ciphertext_74
under f159 and under AVS's own key_74.tsv, letter-for-letter agreement count) is reported beside it and does
not change the rule above.

## Amendment A (04:19 UTC, after the selection step, before any control statistic was computed)
The selection step ran (`xm_control.py`) and found 0 qualifying keys: of every letter-alphabet key of 20-58 letters
on disk outside the two folders, none reaches coverage 0.5 on even one of the three AVS ciphertexts (highest:
decode-1168-modena-costabili-1492/key.tsv 0.45/0.39/0.48; dupuy468-anhalt/key_from_gloss.tsv 0.42/0.41/0.43;
na-suriname-map-1781/key_period_codes.tsv 0.40/0.36/0.39). The pre-registered relaxation also selects nothing.
f159 itself covers 0.52-0.57, so it sits just over the tool's coverage floor, and the floor alone would stop every
size-matched control from being scored -- a non-test by construction. Amended control, fixed now: the three
real (not shuffled/scratch: no 'shuf' in the path), distinct-folder letter-alphabet keys of 20-58 letters with the
highest minimum coverage over the three ciphertexts are scored with the same `pair_stats` statistic, the
coverage floor bypassed for the control only (f159 is scored identically, floor or not). Decision rule unchanged
except "coverage >= 0.5" is dropped for the control side: a control reaching stat >= 3.292 on any of the three
ciphertexts at coverage >= 0.35 marks the lead "generic letter-frequency artefact". Coverage of every control
pair is reported beside its stat.
