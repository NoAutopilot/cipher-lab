# DIN-PRINT pre-registration (account-3 in-session worker, 3 Oct 2026, written before any score was computed)

Brief: `.claude/briefs/runs/2026-10-03-acct3-din-print.md`. Target fr3621-dinteville-1592. Disclosure: before writing
this file I read the print OCR (`../../print/revue-champagne-t12-1882-pp340-341.txt`) beside `../gloss_pairs.tsv` and
`../key_syl.tsv` by eye; no alignment, consistency or n-gram score was computed on the print before this commit.

## 1. One convention for both texts (rule 3, PX-BRODEC)
`print_pairs.tsv` gives, per glossed cipher segment of f.128, the print span (*Revue de Champagne et de Brie* XII, 1882,
p.340) and the gloss (from `../gloss_pairs.tsv`), both normalised the same way: lowercase; accents folded; apostrophes and
punctuation dropped; j -> i, v -> u, y -> i; numerals written as French words (2 -> deux; the print's 45, OCR-garbled as
'îa', -> quarante cinq, a gloss dependency logged in the note column); the gloss's unexpanded '+' marks dropped (the print
has none). Print words are used verbatim under this convention; period spellings are NOT restored from the gloss
(vu stays vu, charges stays charges), so no gloss reading re-enters the print side. Clear words on the leaf are not
aligned (as in align_f128.py).

## 2. Alignment (tools/interlinear_align.py, no private aligner)
Primary: exactly the key_syl settings (align_f128.py --syl: numeral codes >= floor 100, max_chunk 3, seg_bonus 0,
len_prior 1.0, null_cost -1.0, wildcard none, keep f/s apart), plain = print_norm. Only the plain text changes vs key_syl.
Secondary (reported, not a gate): letter mode (code-prefix, 0-1 letter per sign, null_cost 0), as align_f128.py default.
Statistic: consistency (align_f128.py's definition: over sign types aligned >= 2 times, top-letter count / occurrences).

## 3. Key-blind controls on f.128 (must fail)
(a) every rotation of the concatenated print_norm letters, re-split into the original word lengths; (b) 1000 random
permutations of the same letters (seed 20261003), re-split the same way. Gate: real consistency > max of (a) AND
> p95 of (b). If the primary fails the gate, the print key is not used on f.130 and the job reports that.
Also reported (not a gate): the same alignment on gloss_norm (one convention, + dropped) so the print-vs-gloss difference
is not a notation artefact; rows changed vs key_syl.tsv = sign types whose top meaning differs, plus added/dropped types.

## 4. f.130r with the print key (no hill-climb repair)
Key = key_print.tsv top meanings. Statistic, runs and model exactly as f130/score_f130.py (fr16 4-gram mean log10
P/letter inside keyed runs). Controls: 1000 free shuffles of the letter values among keyed signs (seed 20261003, as
A2-DIN2) and 1000 frequency-banded shuffles (blocks of 4 signs adjacent in f.130 frequency rank, seed 31001, as VERIFY-DIN).
Gate: real > p95 of both. Grades per token (rule 4): C if the key_print row has agree >= 3 and agree/n >= 0.5 (support
from the print alignment) and the f.130 sign conf is H; M if keyed otherwise; U if unkeyed. No S grade (no repair, no
separate control). h and D are graded by this same rule, no special case.

## 5. Date
If a crop of the f.130 date line is on disk it is looked at once; otherwise the date stays flagged (3 or 4 July).
