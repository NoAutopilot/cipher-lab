# PREREG NEVREVOL-3 (3 Nov 2026, 06:4x UTC by date -u; account 4 worker NEVREVOL-ATLAS-2, briefs .claude/briefs/runs/2026-11-03-acct4-research-director-59.md / -58.md JOB NEVREVOL-ATLAS)

Pushed before any vision pass. Same statistic, nulls and gate as PREREG-NEVREVOL-2.md; what changes is the label set the passes write.

**Hypothesis.** Labelled directly with key no.60's own 264ext atlas tags (tools/keys/key60_atlas/atlas264.tsv A01-A52 +
atlas264ext.tsv A53-A62, 62 exemplars, 41 distinct tags, contact_sheet_264ext.png), with no sign_guide.md tag step, the six
densest f.66 lines (L07-L11, L13; 12 crops in images/v2) decode under tools/keys/key60.tsv + ../fr3986-nevers-revol-1593/
key_atlas_extra.tsv to a sequence that beats both nulls.

**Label set (named here, per NEVREVOL-PREREG's lesson).** Each sign gets one of the 41 atlas tags exactly as written in the
atlas TSVs' `tag` column, or `?` when no atlas exemplar fits. `?` tokens are unkeyed and dropped from the decode, as the
target branch already drops unkeyed tags. No tag outside the 41 is written.

**Statistic.** S = mean log10 4-gram score per letter (tools/judge_plaintext.py, fr16 model), first value of an a|b entry,
decoded signs in page order.

**Nulls (200 each).** (a) length-class value shuffles of the same merged key (seeds 1..200); (b) shuffled orders of the target
sign sequence under the real key (seeds 1..200).

**Gate.** Real S ranks <= 10/201 against (a) AND <= 10/201 against (b). Scored by `controls_sup.py --v3` (the target2 branch
under key60.tsv + key_atlas_extra, reading ciphertext_v3.tsv; added for this run, no other change) -> controls_v3.txt.

**Control (cited, not re-run).** controls_mixed.txt: the same merged key, mixed letter/syllable/word encipherment at N=188,
both-null pass 10/10 at 0%, 10% and 20% (gated), 10/10 at 30%, 9/10 at 40%, 8/10 at 50% (report-only). It is on the key
that will score the target.

**Order.** This file pushed; pass A (this session, one crop per look, atlas tags) written to passes/nevrevol3_passA.tsv and
committed; only then pass B (6 Opus subagent calls, one per line pair s1+s2, given only the two crops, the contact sheet and
the two atlas TSVs; no key, no pass A); reconcile disagreements from the crops only (reconcile_v3.tsv, ciphertext_v3.tsv);
score once.

**Stated limits before the run.** (i) The control enciphers with all of key no.60's signs; the atlas covers 41 tags, so `?`
tokens shorten the scored sequence. If fewer than 150 keyed signs remain (80% of the control's N=188), a FAIL is logged as a
non-test at that coverage, not a control-backed negative. (ii) The control's errors are uniform; the hand's are lookalike
errors. (iii) 1 - pass agreement must sit inside the control's 0-50% band for a FAIL to be control-backed.

## Decision
Belief: removing the sign_guide -> key.tsv mapping step is the most likely thing to move the shuffled-order rank (119/201 under brief 57); I expect at best a marginal gain, since atlas coverage of the f.66 hand is untested.
Would change it: both ranks <= 10/201 -> decode with decode_key --check, judge pasted, grades per token; anything else -> stop.
Stop criterion: one run. PASS -> decode and grade, no second instrument in this session. FAIL -> no reading; gap logged "untestable-by-this-instrument at this N (rule 3); waits on the Revol-hand sorter, ASKS 102"; no re-run with other labels, thresholds or line choices.
Observed: A/B raw agreement 117/190 aligned tokens (61.6%; 86 agreed non-? signs); reconciled 188 signs, 110 keyed (H 86, M 24), 78 `?`. controls_v3.txt: real S -1.2206; rank 1/201 vs length-class shuffles; 34/201 vs shuffled orders (p95 -1.3386, max -1.1352); fr16 judge FAIL (-1.221 vs real_p05 -0.909, word cover 0.836 PASS). Gate: DOES NOT BEAT CONTROL.
Decision: stop (one run). Keyed signs 110 < 150, so by limit (i) this FAIL is a non-test at that coverage, not a control-backed negative; logged untestable-by-this-instrument at this N (rule 3), waits on the Revol-hand sorter, ASKS 102. The order rank moved 119 -> 34 against brief 57 and is still outside the gate; not re-run with other labels, lines or thresholds.
