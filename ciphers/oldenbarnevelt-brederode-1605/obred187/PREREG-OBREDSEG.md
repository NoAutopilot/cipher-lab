# PREREG-OBREDSEG (15 Oct 2026, 09:3x UTC by date -u; worker OBRED-SEG, account 2, for LANE DEFAULT-A2-0810-15)

Pushed in its own commit before any statistic is computed. Inputs as on origin/main at 22dd0f5ea: OBRED-BAND's pooled pairs and
`interval()` (`obred187/band/band.py`, unchanged), `obred187/structure.json` runs (runs92, runs187), `tools/data/nl16`. Disk/CPU only.

Disclosure: this worker has read `band/reading_92_187.tsv` rows 1-19 and the run contexts before registering, and noticed by eye that
run 146 110 252 433 (fgh, e, l, s) before "van de zijde van 611 ende 612 ... gefourneert" could be "gelt" (t at the s/t band edge).
That guess is not part of any statistic below; it is reported only if the registered search returns it.

## Corpus / era (rule 3)
No nl17 corpus exists in tools/data. nl16 (1569-1589, moral/polemical prose, not letters) is the nearest era (16-36 years before the
1605 letter); nl18 (1770-1799) is not era-matched. Used: nl16, disclosed as era-near and register-mismatched (prose, not letters).
Text folded as OBRED-TRY's `fold` (i/j -> i, u/v/w -> v), alphabet `abcdefghiklmnopqrstvxyz`.

## Units
Letter sub-runs: each run of structure.json split at name codes (588-751); every sub-run is assumed to start and end at a word boundary
(runs sit between clear words). Each token carries OBRED-BAND's pooled interval [lo, hi].

## Search (one fixed decoder, used identically on target, nulls and control)
Lexicon: nl16 word unigram counts (folded, >= 2 occurrences, length >= 1). Word cost = -log10 p(w). DP over each sub-run: a word w
may cover positions i..i+|w|-1 if every letter is in its token's interval (cost 0) or one alphabet step outside it (edge tolerance,
+1.0 per such letter); an unknown letter costs 4.0 (any token). Minimum-cost path; trie search.
Recovered word: a lexicon word of length >= 4 on the best path. Statistic I = sum over tokens covered by recovered words of
log2(23 / width) (0 for an edge-tolerated letter): informative coverage, so wide intervals buy less.

## Target gate
Null (a), shuffled band: pooled pair letters permuted over the pooled codes, intervals recomputed, same search; 200 draws, seed 1605.
Null (b), order: token intervals permuted across all letter positions (sub-run lengths kept); 200 draws, seed 92. Both can change I.
Target passes when I_real > p95 of (a) AND > p95 of (b).

## Synthetic control (must pass before the target result is read as a test)
20 simulations, seed 1600. Lexicon from four nl16 files; text from the held-out fifth (`coor001boev01`). Per simulation: alphabetical
homophonic list on 1..587, band widths ~ nl16 letter frequency (band.py `synth_list`); 41 pool pairs (letters drawn from the held-out
text, uniform homophone); error: a share e of pool letters replaced by an alphabet neighbour; for each target sub-run length L,
consecutive held-out words from a random start until >= L letters (word-aligned, length near L); each letter enciphered by a uniform
homophone, interval from the pool. e = 0 and e = 0.25 (bracketing the real held-out hit rate 0.73-0.80); report each level's interval
hit rate. Per simulation: I vs a 50-draw shuffled-band null (pass if > p95); word precision (recovered words equal to the true word at
that span) and recall (true words >= 4 letters recovered).
CONTROL GATE at e = 0.25: >= 70% of simulations beat their null AND pooled precision >= 0.50. Control below gate -> the target result
is reported as a non-test at this N, whatever it reads.

## Grades and output
All words grade M. A word of length >= 5 is S only if the control gate passes, the target gate passes, and the control's pooled
precision for length >= 5 words at e = 0.25 is >= 0.80. `obred187/seg/seg.py` writes `seg_gate.json` and `seg_92_187.tsv`
(sub-run, span, codes, intervals, word, grade); `--check` exits 1 if stale. Never key.tsv; no sense of the letter is claimed.
