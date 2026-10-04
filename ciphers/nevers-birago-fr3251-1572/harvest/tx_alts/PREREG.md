# TX-ALTS pre-registration (4 Oct 2026, written before any new pass or decode run)

Brief: .claude/briefs/runs/2026-10-04-acct3-tx-additions.md (TX-ALTS). Item: BENCHMARK-TX birago1572-no87 (eval).
Baseline reproduced from disk before this file: current two-pass lattice (tx_decode/no87_topk.tsv) holds the clerk's
value at 27 of 97 top-1 errors (wrong + unvalued) -- 2 of 22 on f178r, 25 of 70 on f178v, 0 of 5 on f179r.

## Test 1 (disk only): tool change on the existing passes
`key_decode_lattice.py from-passes --keep-alts` (every reader-written alternative kept, exempt from the 0.02 floor and
the top-4 cut) on the existing A/B passes vs the current lattice. Reported: truth-in-lattice, err_true at lam 4.

## Test 2 (vision): the a/b? rule
Lines: f178r L01-L03 + f179r L01-L03 (the six no.87 lines with existing crops not used for any lam tuning; 27 of the
97 errors). One new blind Sonnet pass N per page under the a/b? rule (2 subagent calls, one page each, line crops
only). Comparison isolating the alternatives on the same reads (paired, same signs):
  ALTS  = lattice from (N with every alternative, B)   via from-passes --keep-alts
  FIRST = lattice from (N first choice only, B)        via from-passes, N's alternatives stripped
Also reported beside them: CURRENT = (A, B) as in TX-DECODE.
Gates (fixed here):
  G1 coverage: truth in the ALTS lattice at >= 50% of FIRST's top-1 errors on the six lines (research note #3 target).
  G2 err_true: lattice decode at lam 4 (the standing setting since TX-DECODE's re-tests; lam 1 also reported, not
     gated), --lang it16dip, printed key key_1572_sheet.tsv, truth tx_decode/truth87.tsv. Paired over aligned truth
     positions: fixed = FIRST wrong/U and ALTS right; broken = FIRST right and ALTS wrong/U. Adopt only if fixed >
     broken with a one-sided sign test p < 0.05. Coverage up with no err_true gain = "not adopted" (research note).
  Decode on the six lines alone (the lattice decoded per page set), top-1 err_true also reported.
Limit stated in advance: 6 lines, ~180 signs, ~27 errors -- a sign test needs >= 5 net fixes with none broken to reach
p < 0.05, so a null here is low-power, logged as such, not as a negative of the rule.
