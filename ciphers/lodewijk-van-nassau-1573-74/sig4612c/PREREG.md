# SIG-4612C pre-registration -- crib placement on 4612 v3 from 7208's known text

Written 9 Oct 2026 03:3x UTC by date -u, worker SIG-4612C (Opus) for LANE SIG-4 (account 1), before `crib_place.py` exists and
before any 4612 score. Brief: `.claude/briefs/runs/2026-10-09-acct1-sig4-jobs.md` "## SIG-4612C". Instrument: crib placement (new
material: 7208's period decipherment, SIG-7208); the retired LM-anneal / key_repair / word-segmentation instruments are not used.

## Data (fixed)
- Target: `ciphertext_4612_v3.tsv`. Stream: rows in file order; a sign that is an integer 1-120 is a stream token; an integer whose
  key_full value is NULL (121-122, 124, 126-135, 137-138, 141, 143-144) is SKIPPED (dropped, does not break); anything else (clear
  word, '?', name code, 123, 136, [blank]/[blot]/[spot]) BREAKS the segment. Same rule for `ciphertext_5811.tsv`, cut after its
  first 833 stream tokens (4612 v3's N).
- Key: `key_full.tsv` codes 1-120, single letters, folded by `ax4612tr/word_share_check_v3.fold` (J->I, U->V).
- Word share: share of keyed stream letters inside an fr16 word of >= 3 letters (the `word_share` rule of
  `ax4612tr/word_share_check_v3.py`, fr16 lexicon via `tools/french16_ngram.load()`), computed on the segments above.

## Topical cribs (fixed now; folded; length >= 6; each spelling variant is its own crib)
MASTRECHT MAESTRICHT MASTRICHT MASTRECH ENTREPRINSE ENTREPRISE STOCKEM STOKEM RIVIERE RIVIERES BATEAVLX BATEAVX CHEMIN BOMMEL
INTELLIGENCES HOLLANDE LENNEMY ENNEMIS CAVALLERIE COMMISSION GOVVERNEVR PRINCES AFFAIRES INTENTION GVERRE
(25 cribs, from `sig7208/cribs_4612.tsv`; 276 is NOT used as a value anywhere -- direction rule, lead only.)

## Procedure (identical for target and every control)
1. For each crib w and each start i inside one segment with room for len(w) tokens: agreement a = #j with key[code_{i+j}] == w[j].
   Accept the placement if a / len(w) >= 0.60 AND a < len(w) is not required (full matches are accepted, imply only confirmations)
   AND no code occurs twice in the window with two different crib letters.
2. Overlap: accepted placements are taken in order of (share desc, length desc, crib order, i); a placement overlapping an already
   kept one is dropped.
3. Each kept placement gives, per position, (code -> crib letter): a CONFIRMATION if equal to key, else a REASSIGNMENT.
   A code with two different implied letters across kept placements, or a reassignment of a code that another kept placement
   confirms, is CONTRADICTED and contributes nothing. The rest are the consistent reassignments.
4. Statistic G = word share (key with consistent reassignments applied) - word share (key), on the same text.
   Reported alongside: placements kept, consistent reassignments, reassignments supported by >= 2 kept placements.

## Controls (rule 3; each can move G differently from the target)
(a) Known-answer positive control: 5811 cut (N=833) with key_full perturbed: a fraction f of the distinct codes 1-120 occurring in the
    cut reassigned to a random different letter (letters of key_full's folded alphabet). f is calibrated BEFORE any crib is placed:
    f in {0.05, 0.10, ..., 0.40}, 20 seeds each, the f whose mean perturbed word share is closest to 4612 v3's own word share under
    key_full (the on-file 70.7% figure, recomputed by crib_place.py's segmenter and printed; it is the existing baseline, not a crib
    score). Then 10 seeds (perturbation seed s, crib draw seed s): cribs = for each topical crib's length, one word of that length drawn
    without replacement from Groen IV CDLXXXIII (5811's print, `groen/groen_IV_CDLXXXIII.txt` lines 162 and 174), folded, >= 6
    letters (nearest available length if none). Procedure run with the perturbed key as "key".
    RECOVERED = consistent reassignment c->L with c perturbed and L == key_full[c]; FALSE = any other consistent reassignment;
    RECOVERABLE = perturbed codes occurring inside an exact occurrence of one of that seed's cribs in the cut's TRUE key_full decode.
    Gate (a): pooled recall sum(RECOVERED)/sum(RECOVERABLE) >= 0.50 AND mean FALSE per seed <= 2.0 AND mean G > 0.
    sum(RECOVERABLE) == 0 counts as a FAIL. If (a) fails: stop, log CONTROL BELOW GATE, 4612 is not scored.
(b) Off-topic null on 4612: 200 draws; each draw = for each topical crib's length, one word of that length (nearest if none) drawn
    without replacement from the folded >= 6-letter words of `decipherment_7205.txt` and `decipherment_4614.txt` that are not in
    `decipherment_7208.txt` and not in the topical list. Seed 46120 + draw.
(c) Shuffled-order 4612: 200 permutations (seed 46220 + k) of 4612's stream tokens, segment lengths kept; topical cribs; G on the
    shuffled text against its own baseline.
Gate (target): (a) passes AND G_topical > p95(b) AND G_topical > p95(c) (p95 = 95th percentile, numpy 'linear' method).

## On PASS only
Apply the consistent reassignments through a decode config (never hand-edit key_full.tsv): reassigned codes graded S at most; tokens
inside a crib placement only M. `tools/decode_key.py ... --check` exit 0. On FAIL: crib instrument logged with attempt count 1, not
retired (unless (a) failed), and the next step named.

No parameter (0.60, the crib list, the pools, seeds, f grid) is changed after this file is pushed.
