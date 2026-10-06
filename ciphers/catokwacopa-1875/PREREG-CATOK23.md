# PREREG-CATOK23 -- spec tests 2 and 3 on our own pairs.tsv (6 Oct 2026, worker R12-CATOK23, account 2)

Committed and pushed before any statistic below is computed. Script: `catok23.py` (our own code; Bourdeau's
cyphersolver catokwacopa `mech.py`/`names.py`/`search.py`, MIT, read for the omission rule and the frames only).
Line numbers are Bourdeau's (pairs.tsv column 1).

## Model (the published one)
A reading P fits line (A, B) exactly when some order-preserving interleaving of A and B is a subsequence of P (no
misprints). Omissions = letters(P) - |A| - |B|.

## Sources (all fetched 6 Oct 2026, open, cited in NOTES.md)
- Names N_ours: (a) headword surnames (`^Surname,`) of Foster, *Alumni Oxonienses 1715-1886*, vols 1-4 (IA
  alumnioxonienses01univuoft, 02univuoft, 03univ, 04univuoft, djvu text); (b) capitalised words (mid-sentence, >=3
  occurrences) in those four plus *The Historical Register of the University of Oxford* (1888, IA historicalregist00univuoft)
  and the 10 period novels below whose lower-case form occurs <= 1/10 as often in the novels. Upper-cased, letters only,
  length 3-14. OCR noise is kept (it can only add fits, so it makes uniqueness harder, not easier).
- Period vocabulary V: lower-case words with count >= 3 in 10 Project Gutenberg novels of 1853-1875 (Tom Brown at Oxford
  26851, Verdant Green 4644 and 40338, Middlemarch 145, Bleak House 1023, Barchester Towers 3409, Our Mutual Friend 883,
  The Way We Live Now 5231, Great Expectations 1400, A Tale of Two Cities 98), plus 'a' and 'i'; other one-letter words out.
  Unigram log-probabilities from the same counts.

## Test 2 (name frames)
Frames are Bourdeau's five (names.py FRAMES): 8 'I ATTENDED {} LECSURS' CONINGTON; 25 same frame JOWETT; 24 'TOLD {}'
SHIRLEY; 15 '{} TOLD US TO ADD A SECOND MOTTO' CONINGTON; 10 '{} SCHOLARSHIP EXAMINATION' HERTFORD.
- Target statistic per frame: the names in N_ours (plus the published name) that fit exactly with omissions <= the
  published reading's. **Forced under our list** iff that set is exactly {published name}.
- Matched control per frame (seed 2023), 50 null lines: the frame with the slot filled by a random V word (count >= 20,
  not in N_ours, length within 2 of the published name); letters dropped at random positions to the published reading's
  omission count; the remaining letters split into an order-preserving random subset of size |A| (rest to B). And 50
  positive lines, same procedure with a random N_ours name (length within 2). Statistics: null false-unique rate (exactly
  one name fits) and null any-fit rate; positive power (the planted name is the unique fit).
- Gate: a frame forced under our list counts as control-backed iff null false-unique <= 0.10 and power >= 0.50.
  Otherwise it is reported as forced-by-list but non-discriminating (the control can and does vary on the count).

## Test 3 (unread lines 9, 12, 23, 26, 29)
- Search: k-best beam over (i, j) stream positions, words from V via a trie, <= 4 omitted letters per word, <= 12 per line
  (the design's budget), score = sum log p(w) - 2.3 per omitted letter, beam 60 partial readings per node, no positional
  prior. Top 20 distinct word sequences kept.
- **Unique** iff score(top1) - score(top2) >= 3.0 nats (top2 = best reading with a different word sequence).
- Matched control per target line (seed 2023), 20 synthetic lines: a window of consecutive words from a random position in
  the same 10 novels, letter count L+3..L+12 (L = |A|+|B| of that line, closest to a uniform draw in that range); the excess
  letters dropped at random positions; an order-preserving random subset of size |A| to A, rest to B. Statistics: unique
  rate, correct-unique rate R_c (unique and top1 equals the planted word sequence), unique-but-wrong rate W_c.
- Gate: a unique target reading may be graded S only if its line's R_c >= 0.50 and W_c <= 0.10. A non-unique target with
  R_c >= 0.50 is a control-backed "not forced by this method". A target with R_c < 0.50 is "untestable by this method at this
  length", whatever it returns (rule 3; not a negative).
- Bourdeau's own lines 9/12/23/26/29 verdict ("not decided by the letters") is his; this is our independent instrument.
