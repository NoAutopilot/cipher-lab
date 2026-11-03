# PREREG NEVREVOL-2 (3 Nov 2026, 02:4x UTC by date -u; account 4 worker NEVREVOL-PREREG, brief .claude/briefs/runs/2026-11-03-acct4-research-director-57.md)

Pushed before the positive control runs and before any vision pass. Supersedes the gate of PREREG-SUP-NEVREVOL.md (whose
value-shuffled-key null was shown powerless at N~190, controls_pos.txt); the statistic and the material are unchanged.

**Hypothesis.** The 264ext atlas (tools/keys/key60_atlas) fits the f.66 hand well enough that a key no.60 decode
(tools/keys/key60.tsv + ../fr3986-nevers-revol-1593/key_atlas_extra.tsv) of the six densest lines (L07-L11, L13; 12 crops in
images/v2) scores above chance.

**Statistic.** S = mean log10 4-gram score per letter (tools/judge_plaintext.py, fr model, fr16 corpus), first value of an a|b
entry, decoded signs in page order (unchanged from PREREG-SUP-NEVREVOL).

**Nulls (both, 200 each).** (a) 200 length-class value shuffles of key no.60 (values permuted only among signs whose first value
has the same length; seeds 1..200); (b) 200 shuffled-order nulls (the sign sequence permuted, real key; seeds 1..200).

**Gate (target and every control passage).** Real S ranks <= 10/201 against (a) AND <= 10/201 against (b).

**Positive control (first; `controls_sup.py --mixed` -> controls_mixed.txt).** Held-out fr16 passages (model on the first 80% of
the corpus, passages from the last 20%), enciphered into key no.60 with letter, syllable AND word signs. Sign-class shares are
set to no.60's own use on this letter: the 24 Sept 2026 draft's decoded tokens (reading_tokens.tsv, 280 with a value) are
letter 178 (63.6%), syllable (2-3 letters) 95 (33.9%), word (4+) 7 (2.5%). Encipherment is greedy per plaintext word: a word sign
when one exists for the word (with the probability tuned to the word share), else syllable signs for matching 2-3-letter
chunks (probability tuned to the syllable share), else letter homophones; the achieved shares are printed. N = 188 signs per
passage (the six lines' 24 Sept draft count). Injected sign error 0%, 10%, 20% (a wrong sign drawn uniformly from the key's
sign list), 10 passages each (seeds 1001-1010). The 51% pass agreement of 24 Sept is the warning that this hand's error may
lie at or beyond 20%.

**Stop criterion.** The passes run only if the positive control passes the gate in >= 8/10 passages at 0% AND >= 6/10 at 10%.
Otherwise: stop, log "control below gate at the hand's error band" in HYPOTHESES.md and NOTES.md, no vision call.

**If the control passes.** Pass A (this session, one crop per look, atlas labels of sign_guide.md), pass B (6 Opus subagent
calls, one per line pair, crops only, no key, no pass A); ciphertext_v2.tsv and reconcile_v2.tsv (settled from the image, never
from the key); controls_sup.py target branch against both nulls; HYPOTHESES.md row with both numbers. A target FAIL is a
control-backed non-reading only at an error level the control passed and that brackets 1 - pass agreement; otherwise a non-test.
Decode and grade only if the target gate passes, with judge output pasted.

## Decision
Belief: the length-class null keeps the power on mixed sign classes that it showed on single-letter homophones (controls_diag.txt 10/10 to 40%), so the control should pass at 0% and 10%.
Would change it: fewer than 8/10 at 0% or 6/10 at 10% -> word and syllable signs (which carry whole French words in any key) blunt the per-letter S, and this statistic cannot test the atlas on f.66 at N=188.
Observed: positive control (controls_mixed.txt, achieved shares letter 62.9 / syl 34.7 / word 2.3%) both-null rank <= 10/201 in 10/10 at 0%, 10/10 at 10%, 10/10 at 20%; report-only sweep added after the gated levels: 10/10 at 30%, 9/10 at 40%, 8/10 at 50%
Decision: continue -- control PASSES its gate; the two blind passes may run. The control still separates at 50% uniform error, which brackets the 24 Sept 49% disagreement, so a target FAIL at that agreement would be control-backed (uniform random errors, not lookalike errors: an assumption)
Target (added after the passes, 3 Nov 2026): the passes used sign_guide.md's ASCII tags, which are key.tsv's tags, so the control was re-run on key.tsv (`--local-key`, controls_mixed_localkey.txt: 10/10 at 0-30%, PASS) before the target was scored with it. The target scored S -1.5098, rank 2/201 against the length-class shuffles and 119/201 against the shuffled orders: DOES NOT BEAT CONTROL. Pass agreement 74.5%; pass A was not blind on L10 and L13.
Lesson: a decode can beat a key shuffle on letter frequencies alone. The shuffled-order null is the half of the gate that tests sequence, and here it is the half that failed. Name the tag set the passes will write in the PREREG, so the control runs on the key that will score the target.
