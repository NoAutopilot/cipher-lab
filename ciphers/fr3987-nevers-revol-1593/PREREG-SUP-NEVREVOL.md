# PREREG SUP-NEVREVOL (20 Oct 2026, 02:3x UTC by date -u; account 2 worker for the owner-account orchestrator)

Brief: `.claude/briefs/runs/2026-10-20-acct4-research-director-28.md`, JOB SUP-NEVREVOL. Pushed before any pass or score.

Note on the step: the "six-line crop, two blind passes + reconcile against fr3986's sign_guide/atlas, decode, shuffled-key
control" wording in this folder's NOTES.md (Keyhunt 7 Oct 2026) was written for fr.3988 f.143r-v (Henri IV to Nevers), not
for f.66. The brief applies it to f.66; f.66 has never been read with the 264ext atlas, so it is new material for that
instrument (rule 3's [retired] entry in fr3986 covers the f.198 verso runs only).

**Hypothesis.** The f.66 cipher runs are key no.60 written in signs the 264ext atlas covers, so two blind atlas passes on
whole-line native crops agree well and the reconciled draft decodes with key no.60 (tools/keys/key60.tsv + fr3986
key_atlas_extra.tsv) into French measurably better than the same signs under a shuffled key.

**Material.** Six lines of f.66 (canvas 121), L07-L11 and L13 (the long run plus the next densest line; 24 Sept passA counts
41/19/42/39/17/29 signs), cut with `tools/iiif_lines.py --image images/src_ark_12148_btv1b90606320_f121_850_1350_3400_3600.jpg
--out images/v2 --prefix f66v2 --max-width 1900 --overlap 150 --only-lines 7,8,9,10,11,13 --top-margin 15 --overlap-note
--debug` (0 Gallica requests, the native region is on disk). Two blind Opus subagent passes, each given only the 264ext
contact sheet, atlas264*.tsv, tools/keys/key60.tsv, sign_guide.md and the 12 crops, in separate scratch folders, opposite
line orders. One reconciliation by the worker on the crops.

**Statistic.** S = mean log10 4-gram score per letter (tools/judge_plaintext.py fr model, fr16 corpus; first value of an a|b
entry), of the decoded signs in page order -- the same statistic as fr3986 controls_v2.py.

**Controls (run in this order).**
1. Positive control, first, before the passes: a French passage from the fr16 corpus enciphered into key no.60 single-letter
   homophones, same sign count as the six lines' 24 Sept draft (188), then sign errors injected at 0, 20, 40, 60% (a wrong
   sign drawn from the key's sign list); 10 seeds each. Scored as below (S vs 200 value-shuffled keys). Purpose: find the
   error level up to which this statistic at this N can tell a true key from shuffled ones.
2. Null for the target: 200 value-shuffled keys (the key's values permuted over its signs, seeds 1..200), S on the same
   reconciled signs. It can fail differently from the target: it changes every sign's value, which is what S measures.
3. Shuffled-target: 100 permutations of the reconciled sign order, real key, S.

**Gate.** Target "beats the control" iff real S ranks in the top 5% of the 200 value-shuffled keys (rank <= 10/201) AND
real S exceeds the 95th percentile of the 100 shuffled-target scores. Also reported: fr16 judge PASS/FAIL, pass agreement.

**Licensing.** A FAIL is logged as a control-backed non-reading only if the positive control passes (rank <= 10/201 in at
least 8/10 seeds) at the error level that brackets the measured pass disagreement (1 - agreement); otherwise it is a
non-test at this transcription error (rule 3, SALV-DIAG).

## Decision
Belief: the f.66 hand is closer to the office hand of leaf 298 than f.198's verso was (the 24 Sept unaided passes agreed 51% here vs 41% on f.198), so the atlas may carry over.
Would change it: pass agreement under 50% or S failing either control at rank > 10/201 / below shuffled-target p95 -> the atlas instrument does not carry to f.66 either.
Observed: <pending>
Decision: <pending>
Lesson: <pending>
