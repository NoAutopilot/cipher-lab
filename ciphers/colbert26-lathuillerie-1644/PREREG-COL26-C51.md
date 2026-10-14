# PREREG-COL26-C51 (account 2, LANE DEFAULT-A2-0911-14, 14 Oct 2026): pooled held-out word-grain test of 20 = i (c33 + c51 + c63)

Registered before stage 0 is run and before any pairing of canvas 51 exists. Script: `siblings/word_c51pool.py` (its docstring is the
full rule).

**Units.** Held out from every value choice for 20: c33 (COL26-C33, two blind passes, both cleared the instrument check), c51 (two blind
passes to be made; row 51L01 carries no gloss, so 2 of its 3 occurrences of 20 are pairable), c63 (DA1-COL3's single pass; cleared its
instrument check, 7/22 vs p95 6). **c62 is excluded**: its DA1-COL3 pairing failed its own instrument check (8/37 vs p95 8, P 0.052);
CLAUDE.md rule 3 (per-unit gate before a merge) keeps a unit that tied/failed its own control out of a pooled score. Its one 20-span is
reported as a sensitivity line only.

**Instrument.** word_c33.py's (word_col3.py's) statistic, hit rule, Control W (within-unit permutation of gloss words over that unit's
spans) and power rule, unchanged; positive control = C codes of siblings/key_f23_preDA1COL.tsv; TEST 20 -> i; alpha 0.05/6 = 0.00833.

**Stage 0 (gate on running any vision).** Pooled N = c33 20-spans + c51 glossed occurrences + c63 20-spans. Power at that N = share of
1000 size-N subsamples of the positive-control occurrences of the already-paired units (c33 pass 1 + c63; again with c33 pass 2) whose
Control W P < alpha (10000 draws, seed 20261014 + 1051). If power < 0.5 on either c33 pass: log "too-short at pooled N=<n>", stop, no
vision call, no pairing of c51.

**Stage 1 (only if stage 0 clears).** Crops of c51 with tools/iiif_lines.py (command pasted in NOTES.md); two blind Sonnet word-grain
passes (crops, settled groups with indices, gloss words; no key value, no other pass's spans); mechanical reconciliation as COL26-C33.
c51's instrument check is not separately gateable (too few C occurrences on one short leaf); the pooled instrument check (c33 pass x +
c51 pass x + c63) must clear H > p95 and P < 0.05 for each of the two pooled combinations (c33 p1 + c51 p1 + c63; c33 p2 + c51 p2 +
c63). 20 = i PASS iff on BOTH pooled combinations H > p95 and P < 0.00833 under Control W; else FAIL (FAIL-LOWPOWER if power at N < 0.5).
No key file edited; on PASS the worker runs `tools/decode_key.py ciphers/colbert26-lathuillerie-1644 --try 20=i` and reports it only.
