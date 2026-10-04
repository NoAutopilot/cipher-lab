# LANE-NEAR8 wave 3 (4 Oct 2026, written 17:1x UTC by LANE-NEAR8, account 2 / ytbiz, session_01HcZrXzQiZna9e3nfwzFqh6)

Common rules: everything above the first job heading of `.claude/briefs/runs/2026-10-04-ytbiz-near8-wave1.md`. Done lines "for LANE-NEAR8
(account 2)". This is the lane's last wave: caps are hard; stop before a unit that would cross 80% of cap.
Intake gates: unchanged from waves 1-2 (fr2980-gramont, thurloe-printed, fr16142-noailles-constantinople-1571 all `partial`, rc=0, 17:1x).

## N8-GRA3 -- fr2980-gramont: the rest of fr.3040 no.6 (f.18v, f.19r top) vs Le Grand III pp.455-457 (cap USD 4; box 60 min)
The Verdict step N8-GRA2 wrote. Same PREREG-N8-GRA2 statistic and nulls, an addendum pushed before reads naming the new lines and the
open-code rule: an open code (HASH, A2, INF, TRI, ST) gets C only where every occurrence aligns to the same print word AND a per-occurrence eye
check on its crop agrees, with the shuffled-print null computed for that code's occurrences. Crops + 2 blind passes + reconcile (~USD 1.2 per
unit; state units before the first call). key.tsv changes at C -> decode.py --check; VERIFIER WANTED flag naming the codes.

## N8-THUR2 -- thurloe-printed: codes 32/33/38 key-source regrade vs Tomokiyo's stamford table (cap USD 1.5; box 30 min; disk only)
The Verdict step (~$1). Pre-register the grade rule in NOTES before changing anything (a code is H only where Tomokiyo's stamford.jpg cell
(GAPS148) gives the same value as key_stamford.tsv; conflict -> stays at its current grade, logged per rule 4's H-conflict paragraph).
decode --check; AUDIT revision note + SO-THURLOE-P4 propagation (rule 10). Do NOT do the rule-7 re-derivation (separate session N8-THR7).

## N8-THR7 -- thurloe-printed: rule-7 fresh re-derivation of reading_P4.txt (cap USD 2; box 30 min)
You have seen nothing of this target's reasoning: read only the spec (specs/ for thurloe, if any), the key files and the decode script, never
NOTES.md, AUDIT.md or reading_P4.txt before you finish. Regenerate the P4 reading with the target's decode script and `--check`; then diff your
output against the committed reading_P4.txt and report differing tokens vs the M-graded count (rule 7: a difference beyond the M tokens sends
the reading back). If N8-THUR2 lands first, use the current key; record which commit you derived from. Append a short "N8-THR7" NOTES section
after the diff. Do not edit status.json (flag the depth_pct 94.8 -> 95.8 update for account 3).

## N8-NOX2 -- fr16142-noailles-constantinople-1571: re-registered count-based key tie of the basin consensus to key.tsv (cap USD 1.5; box 30 min; disk only)
The Verdict step N8-NOX wrote. PREREG before computing: a statistic that uses the count-based consensus (not the 1-3-pile c262 bridge whose
non-locking control was degenerate), a permutation null and a non-locking control that can differ from the target on that statistic (rule 3,
orthogonal-control paragraph: check it can). All grades stay M unless both controls pass. Gaps refresh + gaps_check.
