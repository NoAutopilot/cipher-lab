# R7-SUR pre-registration (account 2, 6 Oct 2026, written before the call)

Job: GAPS64 Verdict's cheapest next -- one blind same-hand look at (a) L08:51 / L10:30 "noo[l]e" (reader code g, now l H by
GAPS37's F2 call) and (b) the [sigma] i/e split, L11:17 (aligned i, M) vs L10:66 (aligned e, M). One Sonnet subagent call.

Tiles: single-sign crops of `images/2077_legend_native.jpg`, boxes in `cut_tiles.py`, 3x Lanczos, in `images/crops_r7sur/`;
shuffled to Q1-Q6 / R1-R8 by `build_tiles.py` (seed 20261006, mapping in `blind_key.json`, not shown to the reader).
Queries: q1 L08:51, q2 L10:30, q3 L11:17, q4 L10:66; known-answer controls c1 L08:37 (F2 l, H), c2 L08:5 (F1 g, H).
References (2 per class, labelled only by index): F1 g (L06:4 C, L11:19 H), F2 l (L10:61 C, L12:26 C), e-class sign a
(L11:7, L11:15), i-class signs (L06:8 [f-loop], L10:60 m). Neighbour fragments may show at tile edges; the reader is told to
judge the centred sign.

Reader is asked, per Q: the best-matching R (or "none"), a 0-1 confidence, and the runner-up; and whether Q-tile pairs show
one letterform. No values, codes or words are given.

## Gate (the call counts as a test only if)
c1 -> an F2 ref (rl1/rl2) and c2 -> an F1 ref (rg1/rg2), each at >= 0.6. The controls can fail (they are drawn from the same
g/l family as the queries and can be matched to the wrong form). Gate FAIL: no change to any token; logged as a non-test.

## What each answer changes (only on gate PASS)
- q1, q2 (each separately): -> F2 ref at >= 0.6: no change (l H stands; a second blind call agrees with GAPS37); "noole" stays
  a non-word, logged as a spelling/abbreviation question, not a reading error. -> F1 ref at >= 0.6: the token is downgraded to
  M g|l (value l kept, exceptions row, grade M) -- an image call alone never sets a new H value here (GAPS23's rule binds value
  changes to the 2078 parallel, and these tokens have none). -> any other ref, "none", or < 0.6: no change, logged.
- q3, q4: both already sit at M under GAPS23's rule (clause (ii) 6/6), capped by transcription conf. Nothing in this call can
  raise or change their value. Logged descriptively only: same letterform as each other at >= 0.6 -> "one sign aligned to two
  values (i, e)"; different -> "two look-alike signs under one reader code"; a match to an e-class or i-class ref at >= 0.6 is
  logged as which value class the shape resembles. No exceptions row either way.
- decode_key --check must exit 0 after any change; 2077 H/C/M/U before (H 538 C 10 M 61 U 49) and after are reported.
