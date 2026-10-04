# PREREG test 2 -- es132-vargas-mexia-1578 (RUN2-ES132, account 1, 4 Oct 2026, written ~02:50 UTC before any f.89r / f.89v / f.119v-upper decode)

Brief: `.claude/briefs/runs/2026-10-04-acct1-run2-wave1.md` job RUN2-ES132. Key: `key.tsv` (Cp.30, unchanged since test 0).
Route: `test1.py`'s statistics, extended in `test2.py` (imports test1/test0 functions; no statistic changed).

## Scope check (before any vision call)
`cabinet_noir_map.tsv` rows 89 and 119: `cn_read = no`. Fresh shallow clone of el-descifrador/cabinet-noir, 4 Oct 2026 ~02:48 UTC:
last commit still 47b6db9 (2 Oct 2026 14:15 UTC); es132-vargas-mexia/ holds 32 entries, none named for f.89, f.90, f.91, f.119
or f.120. No page in scope is dropped.

## Pages and order (Usage 6, priced per pass)
f.89r = canvas 86 right (cipher below the clear opening "Juan de Vargas Mexia / A dos del presente ...", about 24 lines);
f.89v = canvas 87 left (about 30 lines in three paragraphs); then f.119v upper (canvas 117), if pacing allows.
Unit = one blind Sonnet pass (crop paths only, never the key, Teulet or any reading) at ~USD 1.5; per page 2 passes + 1
reconciliation by this worker = 3 units. Cap USD 8 => ~1.5 pages; a unit is not started if it would cross 80% of cap (6.4)
or box (04:06 UTC). Reconciliation: A/B disagreements settled from the crops by this worker (no printed text exists for these
lines, so the reconciler has not read their plaintext); the blind passes are scored separately, so the reconciled number is
never the only one.

## (a) Printed known answer
None of f.89r, f.89v, f.119v upper is printed by Teulet: Teulet's 19 Sept 1578 paragraph is f.90v L10-L26 and his 15 Oct
1578 paragraph is f.119v lower (tests 0 and 1). Gate (a) therefore applies to no page in this job and is not run. If a
page turns out (by its decode) to overlap a Teulet paragraph, that is reported, and (a) is run exactly as PREREG_test1.md (a).

## (b) Unprinted text (all pages here)
Statistic S_b = mean log10 4-gram score (tools/judge_plaintext.NgramModel trained on es16, Teulet vol.5 Spanish with both
known-answer letters cut) of the key-decoded letters, codes dropped -- identical to test 1.
Nulls, each computed before the target's S_b in the same run:
- ARM-C1 / N-order: 200 token-order shuffles of the same page's tokens (seed 1578). If the standard judge
  (score > null_p99 AND > real_p05) PASSes the median shuffled-target decode, the judge is void as a gate here and only the
  decode-level gate below is read (as test 1).
- N-key: 200 key shuffles (letter values permuted among numeric bases, seed 1578).
Gate (b), per page and per blind pass: S_b > p99 of BOTH nulls. Reported for pass A, pass B and the reconciled text.
Can each null differ from the target on its statistic? Yes: S_b is an order-dependent 4-gram score, so permuting token order
changes the 4-gram contexts at every syllable join, and permuting key values changes the letters themselves; neither
manipulation is orthogonal to S_b (test 1's values moved under both). Caveat: the order shuffle keeps within-token letters,
so it is the closer, stricter null.
Calibration (power at this length): test 1's f.90v known-answer lines (504 letters) beat both nulls on both blind passes
(S_b -1.229 / -1.277 vs order p99 -1.432 / -1.428, key p99 -1.910 / -1.896). If a target page has fewer than 250 key letters,
its known-answer calibration is re-run on a same-length prefix of the f.90v known-answer lines; if that prefix does not beat
both nulls, the target page's result is a non-test, not a negative.
Judge held-out false negative (reported, never a PASS alone): es16 leave-one-file-out FN 60.7% at N=300 (folds 48.5-66.5%),
70.3% at N=600 (65.5-76.5%), one source volume, 5 folds: reliability of any real_p05 verdict unknown. A gate (b) pass is
"weak support that the key-applied text is Spanish-like beyond its own syllable inventory", the wording test 1 used.

## Transcription error
err_2reader per page = token-level disagreement between the two blind passes after `passnorm.py` (unchanged), aligned per
line with difflib on tokens. err_true not measurable (no benchmark item of this hand in BENCHMARK-TX.tsv).

## Grading (rule 4)
Key-decoded tokens M; codes >= 38 / cursive word codes / unreadable U, except values attested C in this folder
([Bul] embaxador, [Dul] Escocia, [Val] hasta, [ho] consideracion by position) -- those are listed, still not H. No H.
No novelty wording (rule 10).
