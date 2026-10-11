# PREREG-THUR-BAMF (LANE DEFAULT-A2-0509, account 2; written 11 Oct 2026 ~06:15 UTC by date -u, before any score)

Target: Birch 1742 vol 6 p.160 (IA leaf n163), djvu l.19092, "A letter of intelligence from Col. Bamfylde", Paris,
April 7/17 1657 (date line p.161). Unglossed run: "out of the 745 12 36 39 30 20 37 8, the 356 20 17 72 35 94, who is his
62 22 43 37 42 61 43 27 61 43 27 36" (and "937" earlier in the sentence). Positions scored: the 24 numerals below 100
(letter codes); 745, 356 and 937 are word/name codes (>= 100) and are not scored. The ciphertext used is the reconciled
pass A (Sonnet, blind) / pass B (eye) / OCR read of crop bamf/crops/p160t_L01.jpg, fixed before scoring.

Key-family note (prior work): Tomokiyo (sources/cryptiana/web/thurloe.htm#Bampfield) separates a First Cipher (1655 to
at least 6 June 1657, Paris) from a Second Cipher (Frankfurt, late 1657). The target (April 1657, Paris) falls in the
First Cipher period, so the gating table is built from the 1655 Paris siblings; the Oct/Nov 1657 sibling l.68904 (p.576)
is reported only as a descriptive other-period comparison, not as the gating table.

## Table T (built before scoring)
Value -> letter pairs from Birch's printed interlinear gloss over Bamfylde's 1655 letters, vol 4 p.194 (l.15927), p.195
(Nov 24 1655 letter continued) and pp.231-232 (l.19043, Nov 22/Dec 2 1655), reconciled from pass A + pass B + OCR into
bamf/pairs_vol4.tsv. Only one-letter glosses over codes below 100 enter T. A value with conflicting letters takes the
majority letter; a tie leaves the value out of T. Word glosses over codes >= 100 are listed but do not enter the score.

## Statistic S
Mean per-position log10 probability of the decoded 24 positions under an interpolated character trigram model
(letters a-z, lambda 0.6/0.3/0.1 over tri/bi/uni, add-0.5 smoothing) trained on the clear English of Birch vol 6 djvu
(IA bim_eighteenth-century_..._1742_6, long s -> s, letters only, case folded), excluding djvu lines 19050-19200 (the
target letter). A position whose code is not in the key scores log10(1/26) and resets the context; the context also
resets at each run boundary (the three runs are separated by word codes / clear words).

## Controls and gate
1. Matched positive control FIRST (rule 3): two folds on the vol 4 pool, same table builder and statistic. Fold A: T
   built from p.194-195 pairs only, scored on the first 24 letter-code positions of p.232's glossed runs (reading
   order); fold B: T built from p.231-232 pairs only, scored on the first 24 letter-code positions of p.194-195. Each
   fold passes if S_heldout > p95 of 1000 value-shuffled tables (the fold's T with its letters permuted among its codes,
   seed 1657). If either fold fails, the target result is logged "non-test at this N with this table size", whatever S.
2. Target: S_target vs (a) 1000 value-shuffled copies of T (seed 1657; coverage is identical by construction, so
   coverage is reported only as a description, not as a test -- CLAUDE.md rule 3, bCAS/AX-5799), (b) key_downing.tsv
   and (c) key_lockhart.tsv (letter rows, codes < 100) applied identically.
   Gate PASS = S_target > shuffled p95 AND S_target > S_downing AND S_target > S_lockhart (and the control passed).
3. Only on PASS: decode script with --check, per-token grades (rule 4): C = code's letter attested >= 2 times
   consistently in the printed gloss, M = attested once, U = not in T. 24 letter positions is below any reasonable
   authentication distance for a homophonic letter table: a PASS licenses "fragments read" (D1) at most, never a
   reading of the letter. A FAIL or a control failure is logged as such (a non-test is a valid result).

Descriptive only (not gating): coverage under T, l.68904 (1657 Frankfurt-period) table, and Tomokiyo's First Cipher
table (bamp1.jpg, not on disk; host outside this wave).
