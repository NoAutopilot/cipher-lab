# PREREG-D2-COL26 -- value-independent test of the six codes DA1-COLV lowered to M (registered before scoring)

Worker D2-COL26 (account 2, LANE DEFAULT-account-2-20261008-0710), 8 Oct 2026, written ~07:35 UTC by date -u, pushed before
siblings/d2col26_test.py is run. Brief: .claude/briefs/runs/2026-10-08-account2-default-0710-jobs.md, job D2-COL26.

**Codes and values under test** (the R10-COL26B sibling values; key_f23_anchor_r10.tsv): 20 = i, 30 = s, 67 = leur, 81 = me,
85 = na, 96 = que. For 81 and 85 the f.23-gloss values (il, luy) are scored too, reported side by side, same gate.

**Scoring units = glossed two-digit sibling units OUTSIDE every value-choice unit of all six codes.** Union of the six codes'
R10-COL26B `units=` lists: c32, c3536, c3940, c47, c48, c49, c50, c54, c55, c56, c63. Glossed two-digit units outside that union:
**c30** (ciphertext.tsv canvas 30 + siblings/c30_gloss_reconciled.tsv), **c33** (siblings/c33_reconciled.tsv), **c51** (lines 51* of
siblings/c5051_reconciled.tsv), **c62** (lines 62* of siblings/c6263_reconciled.tsv). All already transcribed with their gloss; no
vision call. Occurrence counts before scoring (counted, not scored): 20: 20, 30: 35, 96: 12, 81: 3, 85: 2, 67: 0.
Grain: these units have no word-level pairing except c62 (DA1-COL3, which failed its own instrument check there), so the unit of
observation is the gloss LINE, as in c30/c33/c6263_test.py. Word-grain is not available without a new vision pass; the brief's
"word-grain ordered walk" is approximated by an anchor-BRACKETED ordered walk (below), which localises each occurrence inside its line.

**Statistic (bracketed walk).** Per line: run the ordered greedy walk (c33_test.py's walk; norm() letters only, lowercase, v->u,
j->i, bracketed gloss words dropped) over the line's codes using ONLY the anchor set = key_f23.tsv C codes as committed now (23
codes; none of the six). For an occurrence of a tested code at token index j, lo = end of the last anchor match before j (0 if none),
hi = start of the first anchor match after j (line length if none). HIT if the hypothesised value occurs as a substring starting at
>= lo and ending at <= hi. Per code: H = hits over all occurrences in cleared units, N = occurrences.

**Per-unit instrument check (Szembek / rule 3 per-unit clause).** Before any code is scored, each unit's anchor walk (anchor hits
summed over its lines) must beat its own length-matched control (P < 0.05, more than p95). A unit that fails contributes nothing.

**Controls (both can differ from the target on the statistic: they change the French each occurrence meets and the anchor brackets).**
(L) length-matched: each line's gloss replaced by a random window of the same length from the f.23 main-text gloss bank
(interlinear/f23w_pairs.tsv), anchors re-walked on the window; 10000 draws. (S) shuffled-gloss: glosses permuted over the lines of the
same unit, anchors re-walked; 10000 permutations. Seed 20261008.

**Gate per code:** N >= 5 in cleared units (else TOO-SHORT); power floor: P_min (the P if every occurrence hit) under control L must be
< 0.05/6 = 0.0083 (else UNDERPOWERED); PASS iff H > p95 and P < 0.0083 under BOTH controls; otherwise FAIL. Bonferroni over six codes.
Values under test for 81/85 as above (il, luy counted within the same 0.05/6 family; no extra correction, reported, not used to merge
unless it alone passes).

**Merge rule.** A PASS on 20, 30 or 96 makes that sibling value a value-independent C lead for the 1648 sibling key; it does NOT
re-raise the f.23 token grades (key_f23.tsv) where DA1-COLV's rule-4 conflict applies (81, 85, 67, 96 with f.23 gloss conflicts);
for 20 and 30, which have no f.23-gloss conflict recorded, a PASS returns the code to C in key_f23.tsv with a note naming this job
and is flagged in ROOM for a verifier. FAIL / UNDERPOWERED / TOO-SHORT: key unchanged, the code stays M.
