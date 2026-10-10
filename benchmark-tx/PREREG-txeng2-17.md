# PREREG TX-ENGINEER-2 round 17 (lane incarnation 3, session_01P46fwsU5VTc1oJiV1sayg5, 10 Oct 2026 00:3x UTC by date -u; pushed BEFORE any run; Amendment 9 additions 4; the outside review research/SO-TX-TRANSCRIPTION-2026-10-10.md and the orchestrator's message of 00:3x)

Rules as PREREG-txeng2-5's preamble. `tools/tx_register.py --check benchmark-tx/PREREG-txeng2-17.md` output before the spawn: `OK benchmark-tx/PREREG-txeng2-17.md: names register rows and states a difference` (exit 0).

## TOOL-SCORER-FIX tools/tx_bench.py corrected, with offline tests, then a corrected audit of the frozen S2 and DV1b outputs (TXE2-SCORERFIX; Opus 5.5; cap 8; box 75 min; a tool job + a corrected audit, never a new look)
Nearest prior: TOOL-2RATE / TXE2-2RATE (the last tx_bench change, landed 00:18; build on it), REGFIX (tool fix with tests),
TX-TRUTH-VERIFY (--exclude-flagged's origin), S2 look (benchmark-tx/txeng2/s2score/), DV1b (txeng2/viv102base/). What is different:
the review's reproduced faults, each fixed with a test written from its own snippet (research/SO-TX-TRANSCRIPTION-2026-10-10.md
"Reproduction snippet"): (1) a truth line absent from the output counts every scored position of that line as deleted (a fixed
manifest), and an output line id not in the truth fails validation with a non-zero exit (a `--coverage-diagnostic` mode keeps the
old partial-coverage behaviour under its own name); (2) `paired()` is computed on the SAME truth rows as the rate (drop_flagged
applied under --exclude-flagged) and its endpoint is per-line edit totals (S+D+I, unit cost) paired by line -- lines improved /
worsened with a sign test, the sign-level McNemar on positions reported beside and no longer the headline; (3) therefore an
insertion repair counts; (4) the flag kinds split: --exclude-flagged means truth-verifier flags ONLY; reader abstention tokens
(UNKNOWN, NONE, a trailing ?) are wrong in the full-output measure and, separately, `accepted-token error` and `coverage` are
printed; (5) standard SER = (S+D+I)/N under unit-cost Levenshtein on complete reference lines is printed beside the existing
0.75-indel alignment's figure, with a one-line ranking-sensitivity note when the two orders differ for any pair of files; (6)
`--strict`: exact ref_sign match only (visual identity), reported beside the value-compatible truth-set score; (7) no Wilson
interval on a rate with insertions -- a line-level paired bootstrap (1,000 resamples, conditional on the item's lines) replaces
it when --ci is asked; (8) per-hand (per-item) reporting unchanged, a macro mean over items when several are scored; (9)
`--legacy` reproduces every figure on file to the digit (test: the S2 and DV1b score files). Tests in tools/tests/test_tx_bench.py
(the review's three asserts inverted to the fixed behaviour, plus one per item above); tool_shelf.tsv and SYSTEM.md rows;
system_map_check passes. THEN the corrected audit: the frozen outputs of the S2 look (passZ_S2b, passA_S2, passB_S2, passA,
passB, committed; sha256 as in s2score/SHA256SUMS.prescore) and of DV1b (passZ_dv1, passA_dv1, passB_dv1 against the
WITHDRAWN dev truth, labelled so; the dev2 truth if DV1d has landed, beside) re-scored ONCE each with the fixed scorer into
benchmark-tx/txeng2/scorerfix/, every old score file preserved, every number reported beside its original with the mask stated,
declared "corrected audit of a prior look" in RESULTS.md; no reader, no crop, no new look (eval looks stay 0, S2 looks stay 1).
Openings of eval truth: 1 (the corrected audit of confirm2; logged).

## ORACLE-LOCATION-1 CANDIDATE (not spawned; the review's section 4; runs only after TOOL-SCORER-FIX lands and the desk step LOCAL-QUEUE L74 is answered)
Nearest prior: X12 (a model-generated count constraint), X19 (count-anomaly flags), X13 (proposed cell names) -- all retired or
FAIL; P1 / TXE2-BOXES (machine-proposed per-sign boxes), the owner's sorter sessions (X20: 0/3), B1/B2/B3b (the baseline-side
sheet corrections). What is different: verified spatial information from a person -- boxes, reading order and count, with
identities hidden -- given to the same reader; not another guess from the same reader. Design, fixed here and completed in a
dated final registration before sampling: hands f.102r (by the independent visual route; the old 80/403 never reused), Birago
no.87 (ciphers/birago-fr3252-1571-72 units), and a third hand named with its full candidate-line list before sampling; f.103r
excluded; seed 20261010; 12 complete lines per hand (all if fewer, minimum 6), never selected by error; the line manifest
committed before any annotation or read. Reference: machine-proposed boxes (tools/glyph_atlas.py / iiif_lines component
proposals) verified by the owner in the sorter's blind mode (LOCAL-QUEUE L74; minutes per 100 signs measured on the first 100),
a second independent image pass flagging discrepancies, human adjudication; key values consulted only after the visual reference
is frozen, as a separate audit; a frozen atlas gives the visual equivalences and a shared value is never one. Arms: A = today's
pipeline (two blind passes + reconcile + packet adjudication) with the verified visual atlas; B = the same plus the numbered
boxes (one ID or UNKNOWN per box; the unmarked line beside the overlay); three fresh-context repetitions per arm in randomised
order, averaged. Scoring: the fixed scorer, unit-cost SER on every selected complete line, UNKNOWN wrong, missing lines deleted,
unexpected ids fail; scorer, manifest, reference, atlas, prompts and both arms' hashes frozen before one comparative reveal.
PASS = M_B <= 0.70 x M_A AND M_A - M_B >= 0.03 AND E_Bh < E_Ah for every hand; INCOMPLETE on a missing arm or reference;
NOT PASSED otherwise; no threshold moves after the result. A finite-set diagnostic and investment decision, never S1/S2.
Cost: workers about 25 (box proposals 3, second image pass 4, adjudication 3, six reads 12, scoring 3) + the owner's desk
time, reported separately; B is never called automated. Openings: 0 (a new reference).

Costs this round: 8 (TOOL-SCORER-FIX). Eval looks this round: 0. Openings: TOOL-SCORER-FIX 1 (corrected audit).
