# PREREG-GAPS202: seeded syllabary annealer on pooled R5005+R5006+R5007, matched control first

Written 3 Oct 2026 19:0x UTC (clock read), before any annealer run, by GAPS202-zeschau-seebach-1841 (account-4).
Script: `anneal_syllabary.py` (this folder). R5005 digits are Bourdeau's transcription
(`sources/cyphersolver/2026-10-03/zeschau1841/ct_R5005.txt` + `offsets.json`, dbourdeau/cyphersolver, MIT code /
CC BY 4.0 text, credited); R5006 (GAPS175/179) and R5007 (GAPS190/196) are ours.

## Target
- Parse: R5005 per line with Bourdeau's `offsets.json` phase; R5006 and R5007 each as one stream, phase by the
  higher pair IC (identical to `crib_test.py`). Tokens = two-digit groups; codes 00-99. N = 5,612 digits pooled
  (about 2,800 tokens); K = distinct codes in the pool (counted and printed by the script).
- Language per letter: R5005 and R5006 French, R5007 German (one shared key, segment-specific language models).
  The brief asked for a "synthetic German 1840s" control; 4,661 of the 5,612 digits are French, so a German-only
  control would not match the design. Deviation, stated here: the control matches the pool's language mix.

## Corpus (era check)
- French: `tools/data/fr19` (1830-1888 prose). German: `tools/data/de19` (first printed 1800-1840). Both closer in
  era to 1841-42 than `de1600` / `de20` / `fr16`. Neither is diplomatic register (novels/travel prose), so a judge
  FAIL near the gate is "judge cannot decide", not a negative (rule 3 register lessons).
- Language models (letter 4-grams, a-z) are trained on all files except one held out per language
  (fr19: pg796 Chartreuse; de19: pg31538 Schlemihl); the control plaintext is drawn from the held-out file.

## Design of the annealer (identical for control, target, shuffled target)
- Unit inventory: 26 letters + the 150 most frequent bigrams + 100 most frequent trigrams of the pooled training
  text, plus Bourdeau's 7 pin units if missing.
- State: one unit per code (one-to-one per code; several codes may share a unit = homophones allowed).
- Score: sum of segment 4-gram log10 probabilities of the decoded letter string (French model on French segments,
  German on German).
- Pins: Bourdeau's 7 values 11=la 70=pre 82=m 34=i 29=er 40=e 46=que are held FIXED in the target run (grade I;
  every token they produce is graded I, never above). The control holds 7 of its own true codes fixed (the 7 most
  frequent codes whose true units are the same unit types), so both sides get the same seeding advantage.
- Search: simulated annealing, moves = reassign one code to a random inventory unit (p 0.7) or swap two codes'
  units (p 0.3); 4 restarts x 30,000 moves per seed, linear temperature from 3.0 to 0.05; best restart kept.
  Seeds 2021, 2022, 2023 (three seeds each side).

## Matched control (run first)
- Synthetic syllabary: K_c units = the pool's own K, made of the 7 pin units + the most frequent letters and
  bigrams/trigrams of the training text up to K, each unit given one code (random assignment, seed-fixed).
- Plaintext: held-out French text sized to the R5005+R5006 token count, held-out German sized to R5007's; encoded
  by greedy longest-match over the synthetic inventory; the resulting digit stream gets 1 pct random digit
  substitutions (the measured transcription disagreement, GAPS190/196 two-pass agreement ~99 pct), then parsed the
  same way.
- Metric: token accuracy = share of non-pinned cipher tokens whose decoded unit equals the true unit.
- Gate: control mean token accuracy over the three seeds >= 0.60. Below that: CONTROL BELOW GATE, the target is
  NOT run, the step is logged "non-test at this N/design" in HYPOTHESES.md, stop.
  Headroom check (rule 3): the gate is a pass/fail of the control itself, not a gain gate; no ceiling issue.

## Target run, judge and shuffled-target check (only if the control clears the gate)
- Judge: `tools/judge_plaintext.py` with two folder-local specs (`judge_fr19.json` on the French decode of
  R5005+R5006, `judge_de19.json` on the R5007 decode); a candidate "clears the judge" only if both PASS.
- Shuffled-target check: the same annealer (same seeds) on the pooled target digits shuffled within each letter;
  its decode goes through the same judge. A judge PASS on the shuffled decode voids the judge for this family at
  this N (ARM-C1 rule).
- Outcome wording: any reading is S at most where the control passed and M otherwise; pins I. A candidate that
  clears the judge AND whose shuffled twin FAILs gets a "reading ready" ROOM flag; no status change.

## Addendum A (3 Oct 2026, 19:1x UTC, after control attempt 1, before attempt 2; target never run)
Attempt 1 (as written above): control mean token accuracy 0.032 (seeds 0.070 / 0.027 / 0.000), CONTROL BELOW GATE;
`anneal_control_v1.json`. Diagnostic: the control's own true key scores -3762.7 under the summed objective while the
annealer reached -3459.0, so the search is not the limit, the objective is: a summed log-probability rewards decodes
with fewer letters. One change only, nothing else touched (inventory, moves, seeds, gate, pins, corpora unchanged):
objective J = (summed log10 4-gram probability / decoded letter count) x token count (length-neutral, same
magnitude so the temperature schedule is unchanged). The true key's J is reported beside the annealer's. If attempt 2
is also below the gate, the step is logged "untestable by this annealer at this N" (rule 3 repeated-attempt clause
reached at the next try; no third tuning of the objective), target not run.
