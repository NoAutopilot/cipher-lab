# PREREG-SALV-CRIB: isomorph crib scan from f57v's plain passage (13 Oct 2026, 22:13 UTC by date -u)

Worker SALV-CRIB (account 4, LANE DEFAULT-A4-2135), brief `.claude/briefs/runs/2026-10-13-acct4-default-2135-jobs.md`
"### SALV-CRIB". Disk only. Written and pushed in its own commit before any score is computed. Script: `crib_scan.py`.

## Material
- Cipher: `specs/fr2933-salviati-1525.json` `ciphertext` (327 sign runs, 2,939 tokens, current SALV-F56V split), as is.
  Windows lie inside one run (a plain box breaks a window). f56r-f57r runs are reported separately as a subset, but the
  gate is computed on all runs (a crib word may be enciphered anywhere in the letter).
- Cribs (SALV-57V's candidates, folded with `homophonic_anneal.fold`, v->u, j->i): pagare, contentato, diligentia,
  beueraggio, suggellata. Also scanned as variants, not gated: bisognera, prometto, salviati, octobre.

## Two views (two design hypotheses)
- F: each full sign (base^marks string) is one symbol; matches the cm design (code+mark types are homophonic letters).
- B: base code only, marks ignored; matches the base-as-letter design (marks ornamental or homophone variants).
(A syllabic or vowel-indicator design, where one sign stands for two letters, is not covered by this scan: logged as
untested-by-this-tool for that design, not as a negative.)

## Statistic
For crib w of length L and a view: H(w) = number of length-L windows inside runs whose symbol-equality pattern is
exactly the letter-equality pattern of w (bidirectional isomorph: equal symbols where w has equal letters, distinct
symbols where it has distinct letters). Also reported, not gated: the list of matching windows (leaf, line, position).

## Nulls (both computed; a crib passes only if it beats both)
1. shuffled crib: 1,000 random permutations of w's own letters (same letter multiset, different positions).
2. random Italian words: 1,000 words of the same length drawn uniformly from the distinct folded words of length L in the
   it16 corpus (the five files of `control/corpus_args.txt`), excluding the crib itself.
p = (1 + #null with H >= H(w)) / 1001, one-sided.

Rule 3 check (can the controls differ on this statistic?): H depends only on w's equality pattern; every gated crib has
repeated letters at fixed positions, so a permutation changes the pattern (the script prints, per crib, the share of
permutations whose pattern differs from w's; a crib with share 0 is a non-test and is reported as such). Random words
carry their own patterns. Both nulls can differ from the target.

## Gate (per crib, per view)
Hit: p <= 0.005 against BOTH nulls (5 gated cribs x 2 views = 10 tests, Bonferroni 0.05/10) AND H(w) >= 1.
Nothing else counts as a hit. A hit is a lead for a key trial (decode_key.py --try, every occurrence), never a key edit;
any value later accepted is M.

## Planted-crib positive control (before a miss is read as a negative)
Synthetic cipher with the target's own run lengths (327 runs, 2,939 tokens), Italian plain from the it16 corpus, one
copy of the crib planted at a random offset in a random run long enough to hold it.
- design F-matched: the target's code+mark types allotted to letters by `control/codemark_curve.py`'s alloc (frequency
  deficit), homophone drawn at the type's own target frequency;
- design B-matched: the 36 base codes allotted the same way, marks dropped;
- transcription error injected at the measured mix of `codemark_curve.py` CM_ERR (del:ins:code = 0.465:0.331:0.204) at
  both ends of the measured range, 0.064 and 0.146.
20 seeds per crib x view x error. Power = share of seeds where the planted crib passes the same gate as above (both
nulls, p <= 0.005; nulls 1,000 each). Also reported: share of seeds where the planted window itself is among the matching
windows (survives error and homophony).
Reading: at an error level where power >= 0.5 for a crib and view, a target miss is a control-backed negative for that
crib in that view at that error; where power < 0.5 the target miss is a non-test (the scan cannot see this crib under that
design at that error). A target hit at a view whose control power is < 0.5 is still reported but flagged as unsupported.

## The 3-sign insertion after "Pagare li" (f57v 16.23-25, `#^ #^ #^`)
Not a gated test (one occurrence, no null defined in advance). Descriptive only: count of base `#` in cipher runs, its
mark distribution, every run where `#` occurs 2+ times in a row, and the plain-text slot ("li ___ d' piu", a sum before
"d[ucati]"?). Any inference from it is I-grade.
