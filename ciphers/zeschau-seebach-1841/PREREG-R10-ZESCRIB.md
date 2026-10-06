# PREREG R10-ZESCRIB -- crib-drag of French diplomatic formulae for a near-exact seed (zeschau-seebach-1841)

Written 6 Oct 2026 before any crib placement was scored on control or target (clock read with date -u, 10:45 UTC).
Worker R10-ZESCRIB, LANE LANE-RUN10-account-4. Script: `crib_drag.py` (disk only).

Why: R10-ZESBASIN found the word-parse objective ranks the true key first but has no basin (k=1 return 0.32), so any
search needs a near-exact seed. This is a different instrument (rule 3 third-attempt clause): fixed probable-word cribs
dragged along the cipher, each placement checked for pattern consistency with an injective one-code-per-unit key and
Bourdeau's 7 grade-I pins, then ranked by the unchanged objective.

## Crib list (fixed here; folded lowercase, accents and apostrophes dropped, as wordseg_syllabary.words_of)
jailhonneurde, monsieurlebaron, votreexcellence, samajestelempereur, samajesteleroi, legouvernement, lecabinetde,
saintpetersbourg, lecomtedenesselrode, jevousprie, veuillezagreer, lassurancedemaconsideration, tresdistinguee,
votredepeche, vosrapports, lempereur, lesaffaires, lapolitique, lesinstructions, queje, ilestimportant, danslinteret,
conformement, delapartde, relativement  (25 cribs; chosen from 1840s French diplomatic dispatch usage, not from the
control text, which was not inspected for them).

## Procedure
- Control: `wordseg_syllabary.build_control()` unchanged (2,666 tokens, K 98, 7 pins, 1 pct digit error, held-out fr1810
  text for the two French segments, de19 for the German). Cribs are dragged on the French segments only.
- Crib tokenisation: greedy longest match over the generator's unit list (the rule every prior control used; the target
  would use the same rule-derived list); the first and last token are dropped (boundary-dependent), the core is dragged.
- A placement is consistent if, inside the window, unit->code is one-to-one both ways, every pin code carries its pin unit,
  and every pin unit sits on its pin code.
- Score of a consistent placement: J (word-parse LLR, unchanged) of the full key = pins + crib codes, the rest filled by
  wordseg_pt.freq_init with those codes fixed. Rank within that crib's consistent placements, ties counted against.
- True instance: a control position where the crib core equals the generator's true tokens.

## Gates (control first; all three must pass before the target is run)
- G0 testability: >= 3 true instances in the control French text across the list. Fewer -> NON-TEST (the list does not
  occur at this N), target not run.
- G1 ranking: share of true instances whose placement ranks in the top 3 of its crib's consistent placements >= 0.50.
- G2 seeding: seed = pins + top-1 placements of every crib whose top-1 J beats its second by >= 50, merged in order of
  that margin, skipping any that conflict; fill by freq_init; then first-improvement code-code swap passes over the
  non-seed codes (seed fixed) until a pass accepts nothing or 4 passes. Non-pin token accuracy >= 0.60. Reported beside
  the same passes from pins-only freq_init (the no-crib baseline), so the crib's own gain is visible.
- Control below any gate -> NON-TEST at this N for this crib list; target not run; logged in HYPOTHESES.md.
- If all pass: the same procedure on pooled R5005+R5006 French pairs; output placements and seeded key only, no reading
  graded above M, verifier flag in ROOM.
