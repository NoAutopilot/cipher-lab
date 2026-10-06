# R14-SUR2039 PREREG -- inv. 373 gloss words as cribs on 4.VEL 2039's "Verklaringe der Letteren" (6 Oct 2026, account 2)

Committed and pushed before `crib2039.py` exists or any placement is counted.

Target text: `reading_2039_legend_nieuw_tokens.tsv` (current key: Nieuw Secreet period key + code groups + GAPS15 image
exceptions; 482 tokens H 290 C 11 M 170 U 11), entries a-s (the head line is excluded: it is the heading). Code-word tokens
(`buskruit`) are barriers: no window spans one.

Crib list (fixed, from R13-SUR730 and R14-SUR746 gloss-word lists; R14-SUR758 listed none): smeedery, affuyten, affuyt,
beslag, geschut, fortres, fortificatie, werken, linie, verstopping, boom, touwen, wal (13).

Canonical letters (both sides): lowercase; ij -> y; j -> i; u -> v. A token value with alternatives (g|l, k|i, c|z) matches
either letter.

Placement rule. Window = the crib's length L at an offset fully inside one entry, no barrier inside.
- Tier 1 (fit): every H/C token in the window matches the crib letter; at least 1 M/U position in the window; anchors A
  (agreeing H/C positions) >= max(3, ceil(L/2)).
- Tier 2 (near-fit): exactly one H/C mismatch, otherwise as tier 1 (A counts the agreeing H/C positions).
Descriptive only: how many M positions in the window also agree with the crib.

Controls (both can vary on the statistic: which positions are H/C and what they read).
- (a) Within-entry shuffle: the tokens (value + grade) of each entry permuted, barriers kept in place, 1000 seeds
  (seed 2039..3038); same crib list, same rule. Report real total fits per tier beside the control mean, p95 and the
  fraction of seeds >= real.
- (b) Matched-length gloss words: the distinct words of the 0693-0758 glosses (0693 align_words.tsv plain column; 0702,
  0730, 0746, 0758 gloss_reconciled.tsv), canonicalised, length >= 3, crib words removed. For each real placement, p_b =
  fraction of same-length control words that place on the same entry at the same tier with >= the same A.

Survivor gate: a placement survives if p_b <= 0.05 with >= 20 control words of that length (fewer = "untestable at this
length", reported, not a survivor). A survivor is graded S at most (rule 4), entered in no key file; key.tsv untouched.
Aggregate: the crib list "beats control (a)" if the real tier-1 total sits at or above the shuffle p95.
Non-test clause: if control (a)'s mean tier-1 total is 0 and real is 0, the run is a non-test at this rule (no headroom).
