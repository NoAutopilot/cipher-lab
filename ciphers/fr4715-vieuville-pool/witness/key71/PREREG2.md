# Pre-registration 2: key no.71 (BnF fr.3995 f.133r) re-gated on an UNSEEN known answer
GAPS-fr4715-vieuville-pool-15 (account-4), written 3 Oct 2026 03:3x UTC (clock read), committed and pushed BEFORE any
score is computed. The first gate (PREREG.md, commit 7778b15d; result e69bbb1a: A 5/5, B 25/33 = 0.758 < 0.80, FAIL)
stays on record as a FAIL. This is the second attempt at gating this key; rule 3's third-attempt clause applies to
any further re-gate: if this one fails, the key is not re-gated a third time with the same instrument.

## Disclosure (what the worker had seen before writing this)
- GAPS-14's NOTES section, which prints key no.71 entries for Motz 13 22 27 44 49 52 57 71 93 99, places 93, persons
  6/7/8 13 14 22 25/26/27 44 71 and the letter header. Codes in those cells are excluded below.
- Cabinet Noir's README (lines grepped for "3995|133r|n°71"), which states that 64 of their 69 sure values are
  identical in key no.71 and names a few cells (~35/36/37 Mayenne, ~2 Roy d'espaigne, ~5 Savoie, ~8, ~13, '64, '93,
  ''84). So the *key* is expected to agree; what this tests is whether OUR blind transcription
  (witness/key71/key71_reconciled.tsv, pass A not told any gloss) reproduces it. The worker has NOT opened
  key71_reconciled.tsv's word-code rows, nor the value or proof columns of the selected rows below, before this commit.

## Unseen known answer U (fixed by rule, then listed)
Source: `sources/cabinet-noir/2026-10-03/montholon1589_complements.tsv` (Cabinet Noir v1.2.1, CC BY 4.0).
Rule: rows with type `code` or `nom`, status beginning `SÛR`, whose proof column does not cite key no.71
(regex `n°71|n° 71|clé d.époque|3995|133r|f.133`: none does), with a mark that selects one layer (`'` one dot -> Motz;
`~` bar -> Noms propres), EXCLUDING any code whose key-71 cell in that layer GAPS-14 used or printed (Motz '49 '93;
persons ~13 ~14 ~27 ~71) and any unmarked code (5). Letter rows and spelled-out `mot` rows are excluded: they test the
letter layer, which GAPS-14's part B already scored.
Resulting U (8 items): Motz '29 '51 '74 '84 '94 '97; persons ~15 ~37.
Why fair: these values come from period glosses and usage in Montholon's letters (status SÛR / SÛR-G), not from the
key leaf; none entered GAPS-14's registration, scoring or printed output; and our transcription of the leaf was made
blind to them.

## Statistic and match rule
For each U item: the key no.71 cell for that number in the layer its mark selects (`scripts/key71_regate.py`, loading
the key exactly as `scripts/key71_control.py` does). Each item is `match`, `conflict` (the cell exists and does not
match) or `absent` (no cell: the number falls between crops or is missing). Match: the Cabinet Noir value is split
into alternatives on `, ; / ( )` and ` ou `, `?` stripped; with `norm_tokens` from key71_control.py (case, accents,
u/v, i/y, dropped h, the same alias and stop lists), an alternative A matches entry E if A's tokens are a subset of
E's or E's (non-empty) tokens are a subset of A's.
REAL = matches; SHARE = matches / (matches + conflicts).

## Controls (both can vary on the statistic's own axis: they change which value meets which cell)
- Label permutation: the 8 values permuted over the 8 (code, layer) slots, all 40,320 permutations (exact).
- Random code: each item given a uniform random number in its layer's range (Motz 11-99, persons 1-89), same layer,
  10,000 draws, seed 71.

## Gate (PASS only if all hold)
1. scorable (matches + conflicts) >= 6 of 8; otherwise NON-TEST (not a FAIL, not a PASS).
2. SHARE >= 0.80.
3. REAL > p95 of both controls (strictly).
If PASS: read no.44's six open slots (.03 x2, .07, .49, .57, .6) from the key, grade H only where the slot's mark
selects one layer unambiguously and the key cell was read by two reads (pass A + reconciliation); otherwise M; then
`decode --check` must exit 0. If FAIL or NON-TEST: stop, no slot read, log in HYPOTHESES.md as the second attempt.
The GAPS-14 numbers are reported beside these.
