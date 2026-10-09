# PREREG SUR-0745 (9 Oct 2026, 02:2x UTC by date -u; pushed BEFORE either blind pass is run; score.py is pushed with it, unchanged after)
LANE FAMILY-A2e (account 2), job SUR-0745. Unit: NA 1.05.03 inv. 373 scan 0745 **LEFT page** (22 gloss+cipher pairs, crops_manifest.tsv),
held out (not in T = 0693+0702+0730 sign tables; never transcribed; FAM-SUR373 look.tsv is a 600 px description only). Scope, stated:
the right page of 0745 mixes plain-only lines with glossed cipher lines and would be a second unit of two more vision calls, past the
USD 4 cap; it is not run whatever the result. Design follows AUDIT.md V-SUR0744 (c) and V-SUR0744R: the DOT question is dropped (no
headroom: dot-label permutation p99 at 1.000 on 0744R), dotted and undotted y-family are pooled as [y-fam].

## Readers (as SUR-BLIND / SUR-0744R, unchanged)
Two independent blind Sonnet calls (A forward crop order, B reverse), crop paths only, the SUR-BLIND reader prompt and vocabulary
(`[ij]` dotted y/ij shape, `y` undotted; reader decides). No values, no key, not told what is tested. Each pass's gloss rows are its own.
Cipher tokens never edited; notation-only step (glyph -> vocabulary code) in mk.py. No reconciliation edits the passes: unit verdicts
need BOTH passes (the reconciliation unit is the per-crop y-family count comparison A vs B, descriptive).

## Scoring (score.py, as committed with this file; R15-SURALIAS alias_run.py and R14-SURDP dp_align.py loaded unchanged)
C1 = 10,000 deranged-gloss draws, master seed 7450, shared by (0), (a), (b).
0. Scan: keyed aligned n, A; SAME SYSTEM iff A >= 0.50 and A > C1 p99.
(a) CLASS gate, dot dropped (per pass): every reader y-family token ([ij], y, ÿ) tagged; share of aligned tagged tokens whose gloss
    letter is m or n; null = the same share under C1; PASS iff n_al >= 10, share >= 0.60, share >= C1 p99 + 2/n_al, and SAME SYSTEM.
    [ij]-only share reported, not gated (SUR-0744R's tag set, for continuity).
(b) SPLIT gate (per pass): S = n/(m+n) over aligned y-family tokens whose gloss letter is m or n. Null: S under the same C1 draws
    (draws with m+n > 0). Two-sided at 1%: LEANS n iff S > C1 p99.5; LEANS m iff S < C1 p0.5; else NO SPLIT SHOWN.
    Non-test iff m+n < 10, fewer than 5,000 usable draws, or p0.5 == p99.5.
    **Can the control differ? (rule 3, checked before this file, on 0744R, not the target: calib_0744R.out.)** Yes: derangement moves
    which gloss letters face the y-family positions; on 0744R the C1 S has sd 0.052/0.049, 227/221 distinct values, p0.5-p99.5
    0.630-0.897 / 0.667-0.921, and the real S (0.763/0.765) sits inside -> NO SPLIT SHOWN on both 0744R passes. Stated limit: C1 S
    centres on the page's gloss n:m base rate, so this gate asks "does the y-family prefer n (or m) beyond the letters' own frequency";
    NO SPLIT SHOWN is consistent with one sign class carrying both m and n, not a proof of it.
(c) Descriptive, no gate: for gloss m and gloss n positions in the real alignment, which cipher codes face them (on 0744R: gloss m is
    faced by [y-fam] 18/22 and 19/19; gloss n by [y-fam] 58/81 and 62/85, then l 13/12). T has no other m sign, so (c)'s m row is
    partly the aligner's table, not an independent finding.
Unit verdicts: a gate's unit verdict is its per-pass verdict when both passes agree; otherwise "not shown (passes disagree)".

## Consequences
Whatever the result: no edit to key.tsv, key_period_*.tsv, conflicts.tsv, any transcription file or token grade. CLASS PASS = a third
held-out page for [y-fam] = {m,n}. LEANS n / LEANS m on both passes = a candidate split for a verifier (one unit only; no key row).
NO SPLIT SHOWN = no m/n preference beyond base rate at this N. To the lane for a separate verifier. Rule 10: report only.
