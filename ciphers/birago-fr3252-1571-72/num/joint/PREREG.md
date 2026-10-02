# BIRAGO-NUM3 pre-registration (written and pushed before any control or target run)

Brief: .claude/briefs/runs/2026-10-02-acct3-birago-num3.md. Instrument: `tools/family_run.py --family phased_homophonic`
(new family, `tools/families/phased_homophonic.py`): the phase is NOT fixed beforehand. Each restart starts from a
hard-EM pair cut (as num/phase.py), then alternates (a) the homophonic anneal of tools/homophonic_anneal.py on the
current pair tokens, seeded with the last key, and (b) a Viterbi re-cut of every digit run under the current key's
trigram score plus the pair-type prior, stray single digits as nulls. Best restart by the joint objective.

Target input: `runs_digits.txt`, 48 plain-digit runs, 985 digits (f.119 Bourdeau ct2 + f.100r recon; letters dropped,
dotted/marked groups, wavy sign and CLEAR as breaks, same as phase.runs_from). Corpus: tools/data/it16dip (as BIRAGO-NUM).

Control (rule 3, first): synthetic it16dip text in the same design -- the target's own 48 run lengths (985 digits),
two-digit homophonic key over the 64 cells without 6/7, stray single digits at 5% of tokens, pairs never straddle a run
break. Recovery = share of true pair positions whose decoded token starts at the same digit AND reads the right letter
(phase and key both right).

Pre-registered gate: control mean recovery >= 0.6 over 3 seeds at **55 cells** (the upper end the brief names; the
target's pair-type entropy sits between the 40- and 62-cell controls). A 40-cell control is run and reported too, for
the curve, but does not gate. If the 55-cell control is below 0.6 the target is not scored ("non-test"); this is the
third attempt on the Nov 1571 numerical key (fixed-phase homophonic, crib drag, joint anneal), so a below-gate control
here retires this family for this target per rule 3's third-attempt clause until new material or another instrument.
If the target is scored, the judge (spec judge, it) runs on the decode, and a PASS is only reported beside a
--shuffle-target floor run of the same family. No token is graded above M without that.
