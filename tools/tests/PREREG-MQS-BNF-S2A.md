# PREREG-MQS-BNF-S2A (written 9 Oct 2026, 06:4x UTC by date -u, before any notice was fetched or scored)

Job: MQS-BNF-S2A (LANE MQS-2, account 4), S2 first half of MQS-BNFPILE's "Later sessions". Score with
`tools/bnf_findingaid.py --pile` every Français-fonds finding aid that (a) the 9 Oct census
(`sources/bnf-census/2026-10-09/census.tsv`, first-page arks) or (b) the 23-25 Sept passes
(`sources/solver-diffs/2026-09-2[345]-*.tsv`, any "Français NNNN" shelfmark) hit, and that is not already on disk
(`sources/bnf-census/2026-10-09/pile-dev-set.tsv`). Fetch once to `sources/bnf-findingaids/2026-10-09/`, 2 s apart,
descriptive UA, hard ceiling 190 requests to archivesetmanuscrits.bnf.fr; stop the host on any 403/429/challenge.
No reading, no decoding, no status/key/AUDIT change. --pile's shelf grade is `weak` and stays `weak` whatever happens
here (PREREG-MQS-BNFPILE C5: one calibration point; this session adds no independently found pile with a known answer).

Statistic on the target set: per volume, `bare` and `open_bare` (scorer unchanged); class `pile` = open_bare >= 5
(PILE_MIN, set 9 Oct before this job). Output: the per-volume TSV, sorted, with digitised yes/no/unknown.

## K1 Known answer (reproduction, same design)
fr.2988 (cc49442s, saved 9 Oct) scored inside the fresh set. Expected: bare 26, rank 1 of the combined set by `bare`,
open_bare 0 (notice's own Bibliographie applied). Gate: all three exact. It shows only that the scorer still reads the
one real pile on file among the new notices; not power.

## K2 Planted pile in a fresh notice (same design, length and language as the intended use)
Plant 10 bare items ("Pièce en chiffre.", folios every 4) and, separately, 5 bare items (= PILE_MIN) into ONE fresh
S2A notice chosen with `random.Random(20261009)` from the fetched notices that have an item list. Score with portals on.
Expected: both planted volumes rank in the top 5 of the S2A set by open_bare; the 5-item plant reaches class `pile`.
Gate: 10-item rank <= 5 AND 5-item rank <= 5. Why it can fail: a fresh notice's own Présentation/Bibliographie or a
portal hit marks the planted items known, or the neighbour/place-name proxy reads them named; and the fresh set may
hold real volumes with more open bare items, pushing the plant down. Not at ceiling: the base notice is real and unseen.

## N1 Across-volume permutation null (can differ from the target on the statistic)
Pool every scored item of the S2A set + fr.2988, permute item texts across volumes (per-volume item counts kept),
200 permutations, seed 20261009; statistic = max `bare` in any one volume. Expected: real max = 26 (fr.2988); null
p95 <= 6. Gate: real max > null p95 (and the K2 10-item plant, with fr.2988 removed, likewise > its own null p95).
Why it can differ: max-per-volume depends on which volume holds which item, which is exactly what the permutation
changes; a scorer that counted bare items independently of grouping (or a pile spread thin) would tie the null.
A within-volume order shuffle cannot change `bare` and is NOT used (rule 3, "control that cannot vary").

## Ceiling check
K1 and K2 are pass/fail reproduction and plant checks, not rates; no restart dimension exists (deterministic scorer).

## Reporting
Both numbers for every gate; every volume with open_bare >= 1 listed with digitised flag; class `pile` volumes that are
not digitised are handed to S2B for the ONE batched REQUEST.md (ASKS 38 pattern) -- this session writes no REQUEST.md.
A volume-level notice with no item list is `image-triage`, never a negative.
