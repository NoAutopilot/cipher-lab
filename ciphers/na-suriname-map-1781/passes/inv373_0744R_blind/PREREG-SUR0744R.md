# PREREG SUR-0744R (9 Oct 2026, 00:3x UTC by date -u; pushed alone BEFORE either blind pass is run or read, before score.py exists)
LANE FAMILY-A2d (account 2), job SUR-0744R. Unit: NA 1.05.03 inv. 373 scan 0744 **RIGHT page** (22 gloss+cipher pairs, crops_manifest.tsv),
held out (not in T = 0693+0702+0730 tables; never transcribed; SUR-BLIND ran 0744 left only). One unit; 0745 is not run whatever the
result. Gates are V-SUR0744's "What 0744 right and 0745 must show" (AUDIT.md), with the brief's 10,000 draws and p99.

## Readers (as SUR-BLIND, unchanged)
Two independent blind Sonnet calls (A forward crop order, B reverse), crop paths only, the SUR-BLIND reader prompt and vocabulary:
`[ij]` = y/ij shape with two dots, `y` = same shape undotted, reader decides dots from the image; no values, no key, not told what is
tested. Each pass's gloss rows are that pass's own gloss. Cipher tokens never edited; one notation-only step (glyph -> vocabulary code,
as SUR-BLIND mk.py) before scoring. No reconciliation edits the passes: as in SUR-BLIND, the unit verdict needs BOTH passes (the
reconciliation unit is this worker's own per-crop [ij]/y count comparison A vs B, descriptive).

## Scoring (score.py; R15-SURALIAS alias_run.py functions and R14-SURDP dp_align.py loaded unchanged; T = 0693+0702+0730 + [sh-lig]={h})
dp_align maps `[ij]`, `y`, `ÿ` to one code [y-fam] = {m,n}; the alignment is therefore identical whatever the dot labels.
0. Scan level: keyed aligned n, A, C1 = 10,000 deranged-gloss draws (seed 7440); SAME SYSTEM iff A >= 0.50 and A > C1 p99.
(a) CLASS gate (per pass): reader `[ij]` tagged (as SUR-BLIND run 1). Statistic: share of aligned tagged tokens whose gloss letter is
    m or n. Null: the same share under the same 10,000 C1 draws; p99 = the 9,900th sorted value. PASS iff n_al >= 10, share >= 0.60,
    share >= C1 p99 + 2/n_al (at least two token steps above p99), and SAME SYSTEM. n_al < 10: non-test.
(b) DOT gate (per pass): all reader y-family tokens (`[ij]` + undotted `y`) aligned once against the real gloss (dp_idx); for each aligned
    token record (dotted?, gloss in {m,n}?). Statistic: dotted m|n share. Null: dot labels permuted among the aligned y-family tokens,
    10,000 draws (seed 7441), dotted count fixed; p99 = 9,900th sorted value (p95 reported, not gated). PASS iff dotted n_al >= 10,
    undotted n_al >= 10, and dotted share > permutation p99. Non-test (stated before scoring) if either n_al < 10 or all aligned
    y-family tokens share one agree value (the permutation then cannot differ from the target). Descriptive: exact two-sided Fisher.
Unit verdicts: CLASS PASS iff (a) PASS on both passes; DOT PASS iff (b) PASS on both passes; one pass only = "not shown (passes
disagree)"; both FAIL = FAIL.
(c) Descriptive only (no gate, input to the next unit's design): pooled y-family aligned against gloss m vs n counts, per pass.

## Consequences
Whatever the result: no edit to key.tsv, key_period_*.tsv, conflicts.tsv, any transcription file or token grade. A CLASS PASS adds a
second held-out page for the [y-fam] = {m,n} class; only a DOT PASS on both passes would make `[ij]` a separate value worth a verifier's
key-row ruling. If (b) fails or is a non-test again, V-SUR0744 (c) applies: the next unit drops the dot and tests m vs n pooled.
Handed to the lane for a separate verifier. Rule 10: report only.
