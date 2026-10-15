# PREREG-HEID1621H (written before any count is computed; 15 Oct 2026, 22:1x UTC by date -u)

Job: .claude/briefs/runs/2026-10-15-acct4-depth-steps-2.md, JOB HEID-1621H. Disk only, no network, no reader subagents, 0 vision calls.
No decode, no key, no reading; nothing here assigns a value to any unit.

## Material on disk (checked before writing this)
- heid1621g/reads_raw.txt (375 and 423, readers A and B, verbatim), heid1621g/recon_375.txt, recon_423.txt, ../ciphertext.tsv (379,
  reader splits in its `alt`/`note` columns), heid1621g/agree_375_379.tsv.
- **The HEID-1621G line crops are NOT on disk in this container** (they lived in that session's scratch; regen_heid1621g.sh re-fetches
  them with 5 service.archief.nl requests, which this brief forbids). So the look-alike pass has no image to re-read: step 1 below runs
  the tool's `confusion` and `reconcile` stages on the reads on disk with an explicit "no re-read" row per flagged tile.

## Step 1: look-alike pass on the trailing letter signs (tools/lookalike_pass.py)
- Agreement rows (idA, idB, status, passage, posA), one per letter position: 375 reader A vs B; 423 reader A vs B; 379 reader A vs B
  (from ciphertext.tsv notes "A x, B r" etc.; where the note gives only the eye's alternative, the row is the eye vs the readers); and
  the cross-witness pair 375 (reconciled) vs 379 (reconciled) for each aligned unit's letter (passage "x375_379"). status = split when
  the two labels differ after nothing more than stripping "?" (case kept: S vs s and B vs b are different labels here).
- `confusion` over all of them -> confusion.tsv (the named pairs).
- Flagged tiles = every letter position where the two labels of any row differ. Re-read rows: label NONE, conf L ("no re-read: crops not
  on disk, no vision call licensed"). By the tool's fixed rule (firm re-read matching A or B settles, else UNSETTLED) every flagged tile
  stays UNSETTLED and goes to focus.tsv (for tools/sign_sorter.py --focus; never blocking).
- Per letter sign after the pass: agreement = positions where every reading of that sign agrees / positions carrying it.
- Control re-run: units of 375 after the pass vs 379 after the pass, same difflib rule and same 0.90 gate as PREREG-HEID1621G.
  Expected by construction: unchanged (37/45 = 0.822), since no tile can settle without a re-read. PASS >= 0.90 would license letters at
  S-as-transcribed; FAIL keeps the letters M and the spec marks the letter an unreliable field.

## Step 2: pooled spec
specs/brederode-heidelberg-1621.json rewritten as the pooled version: 13 Aug units (379, 375 witness: numbers 96/96, letters 37/45) + 17
Sept units (423, 14). The letter field is declared unreliable unless step 1's control passes.

## Step 3: test 1 at the pooled N (heid1621h/pooled.py, seed 1621; same nl16 files, pool and held-out split as t1/inventory.py)
Unit keys (letters excluded unless step 1 passes; numbers only):
- KT "as transcribed": 13 Aug key = the numeral tuple (as t1); 17 Sept key = its numeral tuple (S1 = one number). N = 45 + 14 = 59.
- KF "single = first number" (the hypothesis under test, never treated as fact): every unit keyed by its first numeral.
Statistic: K (distinct keys) at N=59; its percentile in 2000 windows of 59 tokens of the frozen nl16 word, syllable-proxy and letter
pools, where each window is two pieces of 45 and 14 tokens from independent places (the two-letter division).
Decision rule: "word band" if K lies within the word pool's [p05, p95] and nearer the word median than the letter median; "below the
word band" if K < word p05 and > letter p95; "letter band" if within the letter pool's [p05, p95]. Anything else undecided.
Matched control C3 (run first, gate 0.90): 300 synthetic word codes built from the held-out nl16 file (coor001boev01): two pieces of 45
and 14 words from independent places; each word type gets a random (n, n+1) pair and a letter tag; in the 45 piece the unit is the pair,
in the 14 piece it is the single first number on 12 of 14 units and an extra-numeral run (3 numerals) on 1 and a bare number on 1 (the
target's own form split); keyed and scored by the same functions as the target under KT and KF. C3 accuracy = share of replicates
the decision rule calls "word band". Below 0.90 the inventory test is a non-test at N=59 and the target verdict is not read.
C2 (rank-match, carried from t1, gate 0.50) is recomputed at N=59 for the record; the target's rank-match is not run unless it passes.

## Step 3b: counted test of "single = first number" (letters as transcribed, flagged M)
Over the 12 S1 units of 423: k_first = number equals the first numeral of some 13 Aug P unit (379) [number only], and k_first_letter
= same with the same letter; k_either, k_either_letter for either numeral. Observed counts are computed by the script, not copied.
Nulls (10000 draws each, seed 1621): V (value null) -- each S1 number replaced by a uniform draw from the range of the 13 Aug numerals
(10-84), recount number-only statistics; P (shuffled pairing) -- the 12 S1 letters permuted among the 12 S1 numbers, recount the
letter statistics. Report one-sided p = share of null draws >= observed. Both nulls can move the statistic they are paired with (V
changes numbers, P changes number-letter pairing). A p < 0.01 makes "single = first number" (or "either") a counted lead, M; it is
never a key or a reading.

## Stop rule
Cap USD 5 or 80% of the 75-minute box (box 22:12-23:27 UTC; no unit started after 23:12), whichever first.
