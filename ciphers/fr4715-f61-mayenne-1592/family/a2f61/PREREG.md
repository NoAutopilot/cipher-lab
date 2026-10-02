# A2-F61 pre-registration (2 Oct 2026, written before the reader call)

Worker A2-F61 (account 2, LANE-A2PUSH). One step: the L02-opening LL foil read that VERIFY-F61-V13 named (AUDIT.md, V13 "L02 opening"):
"a clear 'll' inside a word in this hand, read as O -- together with the target still at LL would settle it". No reading claim, no letter
graded, no novelty class, no key file edited; the corrections file is merged by the orchestrator/verifier, not here.

## Materials
- Tiles cut by `verify_v13/cut.py`'s own `tile()` (same windows W1/W2/W3, grey + autocontrast, height 180) from the same f.61 native region.
  Every centre except the foil is a V13 row of `verify_v13/v13_positions.tsv`, reused unchanged (target T_L02_0 = V13's eye placement).
- The foil, placed by this worker by eye on a gridded crop (disclosed look): `F_LL_DELLA`, f.61 L07, the clear 'll' inside the word read
  "...della" (in "Cependant on n'ose envoyer de par della pour ..."), centre x 1398, y 835 (native region px). It is plain handwriting in
  f.61's own hand, in-word (flanked by 'e' and 'a'), and the same two-stem drawing as the LL sign.
- Panel: V13's panel A, the same 12 W1 references (4STEM, CROSS, 4PI, looped hash, 4-over-hash, LL L05/16, PHI, C43, ZHOOK, 4TRI, BETA,
  VBAR_A), re-shuffled under new letters (seed 20261002). Options: N = a cipher sign not on the panel; O = ordinary handwriting.
- Answer key written outside the repository until the reply is in; its sha256 is printed by `build.py` and recorded in NOTES.md.

## Call (one blind Opus subagent; sheets only, told to open no other file)
Items (19): target T_L02_0 at W1/W2/W3 + a repeat of W1 (4); foil F_LL_DELLA at W1/W2/W3 + a repeat of W1 (4); in-span control R_LL W3 -> LL
(1); anchors (10): A_PLAIN_LES W1 -> O, A_PLAIN_IL W1 (observational only: V13's anchor, which went N), A_CROSS W1, A_4PI W1, A_C43 W2,
A_PHI W2, A_ZHOOK W2, A_4TRI W2, A_4STEM W1, A_HASH4O W1.

## Gates (fixed now)
- G1: >= 8 of the 9 scored anchors correct (A_PLAIN_IL not scored).
- G2: in-span control R_LL W3 -> LL.
- G3: both repeats equal their own W1 answer.
Any gate failing: CONTROL FAIL, nothing scored, the L02 opening stays held.

## Decision rule (fixed now; majority over the three windows)
- Foil O at >= 2/3 AND target LL at >= 2/3 -> endorse `L02 0 insert LL` (null; cipher count 100), V13's own condition met.
- Foil LL at >= 2/3 -> the reader cannot tell this hand's in-word 'll' from the LL sign by shape: hold (not mergeable by this instrument), whatever
  the target reads.
- Target O at >= 2/3 (foil O) -> reject the insertion (the mark is handwriting).
- Anything else (mixed, N) -> hold.
Statistic check (rule 3): the foil's answer is free to differ from the target's on every window (O vs LL vs N), so the control can fail.
