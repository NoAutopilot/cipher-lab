# N4-XM pre-registration (4 Oct 2026, written 04:2x UTC before any control statistic was computed)

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
