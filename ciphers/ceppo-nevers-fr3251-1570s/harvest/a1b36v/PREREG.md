# A1B-CEPPO-36V pre-registration (3 Oct 2026, written ~18:43 UTC, pushed before any blind read)

Brief `.claude/briefs/runs/2026-10-03-acct1-a1b-ceppo-36v.md`. Rule carried over UNCHANGED from A1B-CEPPO-87's unit 2
(`../a1b87/PREREG.md`, commit 6334b236); only the instance list is new.

## Instances (located by script in birago `harvest/f36/recon.tsv`, fr.3252 f.36v)
S76 in pass A, S58 in pass B (split, recon sign '?', M): v36top_L02 pos 7 and 32; v36mid_L01 pos 2; v36mid_L02 pos 11;
v36mid_L06 pos 9, 15, 28. S32 (printed r): v36mid_L03 pos 22 (pass B only), v36mid_L05 pos 10 (A=B).
Tiles of ~5-7 signs with the gloss band above, cut from the committed regions (ceppo `harvest/witness_f36/c38_f36v_*.jpg`),
target identified by its recon neighbours. As many tiles as the box allows, S32 first, then S76 in the order above.

## Readers
Two independent blind Sonnet subagent passes (A, B), one batch each, tiles only, no candidate values, no sign sheet.
Each reader lists the signs left to right with a short shape description and the letter written above each (or ? / none).
This worker is the reconciler and casts no vote.

## Rule (unchanged from 6334b236)
- A gloss counts only if both readers give the same letter above the identified sign.
- A gloss confirming the printed value adds a witness count only. A shape rule separating S31/S32/S76 needs >= 2 agreeing
  glossed instances per member with a deciding feature both readers name. S31 has no agreed glossed instance (A1B-CEPPO-87),
  so no 3-way rule is reachable here by construction; a 2-way S32-vs-S76 rule is recorded but f.87 tokens are regraded only
  if f.87's own S31/S32/S76 tokens are of the two members that have a rule AND the rule's deciding feature is legible on the
  f.87 tile -- not attempted in this job (no f.87 tile read is planned), so no f.87 regrade from this job unless a gloss
  CONTRADICTS a printed value, which is logged as a data conflict (rule 4) in HYPOTHESES.md and the f.87 tokens of that sign set to M.
- The S76/S58 split itself: if both readers' glosses agree on a letter over a split instance, that letter is recorded
  against the instance, not against either label.
