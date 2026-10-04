# PREREG N8-BAL -- Baluze 168 f.246-247 bare passage vs Tomokiyo's quoted fragments (4 Oct 2026, written 16:3x UTC, pushed before any new image fetch or score)

Worker N8-BAL (account 2, for LANE-NEAR8), brief `.claude/briefs/runs/2026-10-04-ytbiz-near8-wave1.md` job N8-BAL.

**Known answer (the test, never an input).** Tomokiyo, Cryptiana louisxiii.htm (sources/cryptiana/web/louisxiii.htm, line 310) for
Baluze 168 f.246 "(of D'Avaux?) to Chavigni ... undeciphered": F1 "c'est ce qu'on pouvoit desirer dudit Salvius pour ce regard";
F2 "de ne consentir aucune suspension d'armes quand on viendra a traiter si ce n'est que le". Neither fragment is shown to a
reader subagent; the worker does not use them to label any sign.

**Transcription.** Crops of the cipher lines of c508-510 by `tools/iiif_lines.py` (command pasted in NOTES). Letter-sign glossary for
this hand: from the leaf's own glossed letters if any; the leaf is bare, so signs are labelled against Tomokiyo's letter block by the
readers (as A3V3-BALB). Two blind Sonnet passes (A, B; same prompt as passes/passA_prompt.txt, no fragment text), then one
reconciliation by this worker that may only choose between A's and B's token, or write `?`; every choice is logged. The worker has
read the fragments, so the reconciled transcription is NOT blind: passes A and B are each scored on their own as the blind figures.

**Statistic** (`n8bal/score_f247.py`, committed with this file): fitting alignment of each normalized fragment into the decoded
passage string; agreement = fragment letters equal to a cipher-derived letter / fragment letters in non-clear-word columns; a
fragment with < 10 letters opposite cipher counts as not overlapping. Pooled over F1+F2.
**Null:** key values shuffled within sign class, 2000 draws, seed 1, p99.
**Gate (fixed now):** PASS iff pooled agreement >= 0.60 AND > null p99, on the reconciled transcription. Reported beside it: pass A
alone, pass B alone (blind), each against its own null. If the reconciled transcription passes and neither blind pass beats its own
null p99, the verdict is written "PASS conditional on a non-blind reconciliation", not PASS.
**Positive control** (`n8bal/planted_control.py`, run before this file was pushed): both fragments planted with key.tsv between clear
filler, scored by the same script: 1.000 at 0% token error; mean 0.903 (min 0.814) at 10%; 0.824 (min 0.661) at 20%; 0.717 (min 0.551)
at 30%, 20 seeds each. The statistic can reach the gate at reader error up to about 20-30%; a smoke test with no real plant gave
null p99 ~0.37, so the null can differ from the target (rule 3 orthogonality check: shuffling key values changes the decoded letters,
which is what the statistic counts).
**Not done here:** 170 ff.228-230 (brief: do not start). Grades: numerals read from Tomokiyo's table H, letter signs labelled by shape H
as in key.tsv, anything a reader marked `?` M; a PASS raises nothing to C (the quote is a published reading of this very passage).
