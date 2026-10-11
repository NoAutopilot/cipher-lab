# PREREG TXE3-3 CROSSHAND (account 3, session_01YB6j6UY3F3EFihTGvxULmf, 11 Oct 2026 05:5x UTC by date -u; pushed BEFORE any read or score)

One of ten TXE3 transcription experiments the account-3 parent launched on 11 Oct 2026. Question: the no.87 result (reconciled
two-pass line read err_true 0.051 as measured on 803 scored signs, one letter in one hand) -- does the same protocol read a
SECOND hand at the 5% target? Rules as PREREG-txeng2-5's preamble: readers blind (brief + crops + sheet only, no key, no
truth, no other pass); every reader output committed with its sha256 BEFORE any score; no *.truth.tsv touched; no result
file printed whole; frozen confirm items (vivonne1573-f103r-confirm2, -w, spinelli-c1519-confirm) never opened or scored.

## Item choice (made from BENCHMARK-TX.tsv metadata only, no truth opened)
Non-confirm, non-frozen items in a hand other than Birago no.87 with >= 200 scored signs: bir1591-f23r-gloss (eval, 203),
gunther8246-p2 (eval, 317), dint-f89-gloss-kp2 (dev, 249), vivonne1573-f102r-dev/-dev2 (dev, 1008/1234).
- bir1591-f23r-gloss and dint-f89-gloss-kp2 are `gloss_visible=yes`: fragments of the period plaintext gloss remain legible
  in the cipher crops, and TX-ENGINEER-2's F3 (PREREG-txeng2-0 Amendment 2) rules that read arms are never gated on such an
  item. A reader could read the value off the gloss, so a 5% figure there would not test shape reading. Ruled out as gate.
- vivonne f102r: same hand as a frozen confirm item, 605/1008 flagged, control margin thin (0.552 vs shuffled max 0.549),
  37 two-segment lines (about 3x the budget). Ruled out.
- **gunther8246-p2 chosen**: WVO 8246 MS p.2, Willem van Oranje's German secretary, 1561; a hand, office, language and key
  family no other item shares; cipher-only page (no gloss); eval; truth C (Japikse 1934 print aligned 0.900 vs shuffled max
  0.311); 15 build-time align-conflict flags. Its committed baseline (two blind OPUS passes + Sonnet adjudication, TX-POOL-LEAF
  9 Oct 2026) is 0.057 as measured / 0.017 flagged-excluded -- so this hand is already known to read near the target with
  Opus readers; the question here is whether the SONNET two-pass protocol of no.87 does so too, measured in one session
  beside a no.87 control.
Budget forces a declared line subset (cap USD 15 for the whole session including this orchestrator's own tokens):
- target lines: **p2_L01-L17** (first 17 cipher lines, top of page; 251 reference positions; about 215 scored expected at
  the item's 317/372 scored share). Scored with `--coverage-diagnostic` (lines L18-L25 listed as missing, not scored) and
  `--line-prefix p2`. Pre-declared; not changed after any number is seen.
- control lines: **no.87 f178v_L01-L09** (258 truth positions, the contiguous run from the top of f.178v whose count is nearest
  251; L01-L08 = 229, L01-L09 = 258). Each line is three overlapping segment crops s1-s3 (harvest/f178v/). Same scorer flags.

## Hypothesis, endpoint, gate
H1: the reconciled Sonnet two-pass line read of the second hand (gunther L01-L17) has err_true <= 0.05 as measured.
H0 (null, a result): it does not; the 5% figure is specific to the Birago no.87 hand or to its session.
Primary endpoint: err_true of the reconciled output (passC = reconcile_passes.py + one blind Sonnet adjudication of the
disagreements from the crops, the no.87 passC recipe) on gunther L01-L17, as measured AND flagged-excluded, Wilson 95%.
Gate: as-measured err_true <= 0.050 (the brief's gate; the flagged-excluded figure is reported beside, never alone).
Secondary endpoints (reported, not gated): pass A, pass B err_true; ratio r = reconciled / better single pass on each item,
against no.87's committed r = 0.051/0.066 = 0.77 ("about 0.75"); the same ratio against the mean of A and B (no.87 0.63).
Tertiary: lookalike_pass.py windows re-read of the split tiles folded in by its fixed 2-of-3 rule (passD), paired fixed/broken
vs passC, run only if budget remains after the primary endpoint (units 7-8 below).

## Matched control (CLAUDE.md rule 3) and proof it can vary on the statistic
Control = the identical pipeline (same reader model, same brief form, same session, same reconcile + adjudication recipe)
on no.87 f178v_L01-L09 (258 positions), the hand on which the 0.051 was measured. The manipulation between target and control
is the HAND (and with it the sign inventory: a 70-label letter-like list vs the 51-cell T## sheet); session, model and protocol
are held fixed. The statistic (err_true on the control lines) is free to take any value: the committed no.87 passes read these
same lines at per-leaf 0.055 (f178v) with single passes 0.066-0.097, and nothing in the control's construction ties its
figure to the target's -- the two chunks are read by separate calls on different images. So the control can fail
differently from the target: (a) control near its committed figure, target above gate -> a hand effect; (b) both well above
the committed figures -> session/model drift, the target figure is uninterpretable as a hand result (non-test, logged as
such); (c) both at or under gate -> the protocol holds on the second hand in this session.
Control validity gate, declared: the control's reconciled err_true (as measured, these 9 lines) is <= the committed passC's
err_true on the SAME lines (tx_bench on benchmark-tx/outputs/birago1572-no87/passC.tsv restricted by --coverage-diagnostic
to f178v_L01-L09) + 0.030. Above that, outcome (b) is declared and the target gate is reported as non-test for this session.

## Units, order, cost and stop rule
Readers: Sonnet subagents (the Agent tool's `sonnet`), one call per (pass, chunk) exactly as the no.87 passes were run
("Vision calls 3: two blind passes, one adjudication" per f178v chunk, NOTES.md); each call reads its chunk ONE LINE CROP AT
A TIME (the crop files, never a page image), enlarging into the scratchpad only, and writes one TSV (passage pos sign_id
alt conf note) into benchmark-tx/txeng3/3/. Pass A and pass B of a chunk are two calls with the same brief, neither told of
the other, neither allowed to open any other pass file.
1-4. readers: gunther A, gunther B (brief benchmark-tx/txpool/gunther8246-p2/blind_pass_brief_p2.md + sheet/), no.87 A,
     no.87 B (brief ciphers/nevers-birago-fr3251-1572/harvest/blind_pass_brief_1572.md + sign_sheet_blind_1572.png).
5-6. reconcile_passes.py per item, then one blind Sonnet adjudication per item of the disagreements (candidates = the two
     readers' labels, context = agreed neighbours, from the crops) -> passC.
7-8. lookalike_pass.py confusion -> windows (split tiles) -> one Sonnet re-read per item -> reconcile --tiles -> passD.
9.   score (tx_bench, --coverage-diagnostic --line-prefix, --exclude-flagged, --paired), RESULTS.md, LEDGER row, ROOM done.
Per-unit estimate: a reader call about USD 0.8-1.5 (about 250 signs, 17-27 crops); adjudication about 0.5; re-read about 0.5;
this orchestrator's own turns about 4-5 in total. Cap USD 15 / box 2 h (05:47-07:47 UTC; 80% lines USD 12 / 07:23 UTC):
stop before starting any unit that would cross either; units 7-8 are the first dropped. A reader call still running at the
80% line is allowed to finish (a unit is never cut mid-way), nothing new starts.

## What is NOT done
No truth file opened by this session before the outputs are committed (tx_bench reads it). No change to BENCHMARK-TX.tsv or
any truth. No tuning: nothing is adjusted after a score. No eval item other than the two named is scored. Nothing published,
the owner not contacted, the oracle pages (benchmark-tx/txeng2/oracle1/) untouched.
