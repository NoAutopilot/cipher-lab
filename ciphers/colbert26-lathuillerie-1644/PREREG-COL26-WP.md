# PREREG-COL26-WP (account 1, LANE DEFAULT-A1-1840, 13 Oct 2026): word-level pairing of canvas 20-21 for 42, 11, 6

Registered before any score and before any pairing exists. Script: `interlinear/c20c21_word_wp.py` (its docstring is the full rule).

**Rule 3 third-attempt check.** Canvas 20-21 has had two instruments for these leads: A4-COLALN (tools/interlinear_align DP hard-EM,
unit = whole gloss row vs whole cipher run, statistic = agreeing chunk count, deranged-gloss control: per-unit FAIL) and D07-COL26K
(unit = row, statistic = value anywhere in the row gloss within +-0.25 of the token's relative position, rotation control: 42 held-out
underpowered, 11 FAIL, 6 FAIL). COL26-42 was a non-test (no s(ieur) token). The word-level pairing is a different instrument: the unit
is a gloss WORD paired to a span of code groups, and the pairing comes from the horizontal placement of the small hand over the groups
in the image (new material: a placement dataset neither earlier test used); the statistic is the within-word offset (o_j = round(j*L/k)
+-1) and the control permutes words over spans (Control W, DA1-COL's instrument, which separated real from shuffled pairings on four
sibling canvases). It is not the same instrument with a changed knob, so the step is run, not logged untested-by-this-tool.

**Values:** 42 = si, 11 = le (hits 'les'), 6 = je (normalised ie). **Known answers:** 83 = de, 31 = que (key_f24 C, from f.24 alone).

**Selection correction.** The three leads were picked by eye from this leaf (A4-RFCOL), so the scored side is in-sample on the value
choice. Gate alpha = 0.05/m, m = the number of distinct codes with N >= 2 on canvas 20-21 that are not grade C in key_period.tsv (computed
by the script from the committed files). 0.05/3 is printed for comparison only.

**Stage 0 (power, before any pairing).** Idealised best case per code: every occurrence whose unit gloss holds a word with the value at
offset 0 or 1 is a hit, paired alone on that word; under Control W it hits with p = (such words)/(words in the unit). P_min = P(chance
>= ideal H). P_min >= alpha => NON-TEST for that code: no vision is spent on it and it is not scored. All three NON-TEST => stop.

**Stage 1 (only for live codes).** One blind Sonnet pass per canvas on line crops (no key, horizontal placement only), mechanical
reconciliation; instrument check 83+31 pooled (H > p95, P < 0.05, else NON-TEST); power = positive control subsampled to the code's N
(power < 0.5 and a miss = FAIL-LOWPOWER); PASS iff H > p95 and P < alpha. No key edit unless PASS, then only via `decode_key.py --try`,
grade M unless --try's own control passed.
