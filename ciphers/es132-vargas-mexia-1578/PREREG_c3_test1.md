# PREREG Cipher 3 pool test 1 -- es132-vargas-mexia-1578 f.41r (LANE-POOLS2 ES132-C3, account 1, 4 Oct 2026, written ~06:28 UTC, before any f.41r decode)

Brief: `.claude/briefs/runs/2026-10-04-acct1-pools2-es132c3.md`. Key: `key.tsv` (Cp.30, unchanged since test 0). Scorer: `test2.py --page f41r`
(test2's `score()`, i.e. test1's statistic; no statistic changed), writes `c3_test1_f41r_result.json` and `reading_f41r.txt`; `--check` exits 1 if stale.

## Letter (step 1)
f.41r = Gallica canvas 38, right page. Tomokiyo TOC (spanish3D.htm): no.21-23 (f.41, 44, 46) Philip II to Juan de Vargas Mexia, Madrid,
29 April 1578, Vargas Mexia's Cipher 3, undersigned by Antonio Perez. `cabinet_noir_map.tsv`: f.41 `cn_read = no`; cabinet-noir (fresh clone
4 Oct 2026 06:2x UTC, last commit 47b6db9, 2 Oct 2026) reads f.44 and f.46 (same date) but has no f.41 folder. Chosen from six 900 px looks
(canvases 34, 38, 76, 147, 178, 182 = f.37, 41, 79, 150, 181, 185) because it carries the most cipher on one page: 30 lines, all cipher
after the clear address "Juan de Vargas Mexia |" in L01. Caveat: f.41 may share content with the same-day f.44/f.46 letters that
cabinet-noir read; not compared in this job (their lecture.md not opened, nothing copied).

## Transcription
Crops `images/f41r_L01..L30_s1/s2.jpg` (`tools/iiif_lines.py`, region 3500,1300,3150,3800, --follow-slope 300). Two blind Sonnet passes
(`run2/pass_prompt_f41r.md` = test 2's shape notation, crop paths only, no key, no text) -> `passes/f41r_passA.tsv`, `_passB.tsv`;
normalised by `test2.load_pass` (unchanged); reconciled by this worker from the crops by shape, key not consulted per span, unsettled
spans flagged '?' -> `ciphertext_f41r.tsv`. err_2reader = test2.err2.

## Statistic, nulls, gate (all lines L01-L30; {CLEAR} tokens dropped, codes dropped)
S_b = mean log10 4-gram per letter (tools/judge_plaintext.NgramModel on `es16/`, Teulet vol.5 Spanish, known-answer window cut) of the
key-decoded letters. Nulls, computed before the target's S_b in the same run: N-order = 200 token-order shuffles of the page's own tokens
(seed 1578, ARM-C1); N-key = 200 key shuffles (seed 1578). Gate: S_b > p99 of BOTH nulls; reported for pass A, pass B and reconciled.
Primary verdict = both blind passes (the reconciled number is never the only one).
Orthogonality (rule 3): S_b is order-dependent (4-gram contexts across syllable joins) and letter-dependent, so both nulls can move it.
Positive control in the SAME run: test 1's f.90v unprinted lines (L01-L09, L27) for pass A, pass B and reconciled, scored by the same
`score()`; on file from test 1: reconciled -1.048 vs p99 -1.396 / -1.801. The control must PASS in this run, or the f.41r result is
reported as a non-test.
Judge caveat: es16's held-out false-negative rate is high (test 1: N=300 blended 60.7%, folds 48.5-66.5%; N=600 70.3%), one volume,
5 folds, so the standard judge line is reported, never gated. A FAIL of gate (b) is "judge cannot decide", not a negative for Cp.30
on this letter, UNLESS the key-shuffle null also overlaps the real score (real <= key p99), which would count against Cp.30 here.
ARM-C1: if the standard judge PASSes the median order-shuffled decode, the judge is void (it is not gated anyway).

## Grades (rule 4, per the brief)
Reconciled key tokens: S where gate (b) PASSes on both blind passes and the control passes, M otherwise; '?' tokens M; cursive word
codes, brace words and numbers >= 38 left as codes (U), counted. No H or C possible (no print, no key-source reading of this letter).
Gate is page-level, so S here means "page passes a control-backed statistical gate", not per-token verification.

## design_prior (step 3)
`tools/design_prior.py --no-write` on ciphertext_f41r.tsv and on ciphertext_f90v.tsv (calibration, Cp.30 known). f.90v (run 06:27 UTC):
454 tokens, multi-sign plausible (d=0.35), letter-for-letter excluded, nearest key = this folder's key.tsv (d=0.12). A disagreement
on f.41r is a finding, not a stop.
