# PREREG-R11-SIENAPOOL (6 Oct 2026, written 13:5x UTC by date -u, before any scored run)

Job R11-SIENAPOOL (LANE LANE-RUN11-account-4). Script `specs/cheap-tests/siena-concistoro-2308/sign_overlap_pool.py`.
Only `--inventory-only` (parse sizes, no statistic) has run before this file was pushed.

Pieces: no. 7 (agent J, 363 tokens) vs fasc. 2 nos. 4, 6, 9, 11, 14, 15, 17, 18, 19, 20, 21, 22 (code numerals only), 23, 24 (P2), 25:
m = 15 siblings. Transcripts as Bourdeau's agents named the signs (dbourdeau/cyphersolver targets/siena1421/transcripts @ adbf9a1,
CC BY 4.0; not copied here). Drawn-sign names differ between agents (G, J, K, L, others), so only same-agent pairs (J: nos. 9, 19, 21)
compare drawn signs on one naming convention; for other pairs overlap is carried mainly by letters and digits named as themselves.
No. 29 (key scrap, letter values only) excluded.

Statistics: J = Jaccard of sign-type inventories; B = shared sign-bigram types within runs.
Nulls, 2000 draws, seed 11: J against curveball swap randomisation of the piece x sign incidence matrix (keeps inventory sizes and
each sign's piece count -- so the control can vary J pair by pair, and discounts ubiquitous letters/digits); B against within-piece token
shuffles of both pieces. p = (#null >= obs + 1)/(n + 1).

Gate: a sibling "clears the null" iff pJ <= 0.05/15 = 0.00333. B is reported, not gated. For each clearing sibling, list signs shared
with no. 7 that occur at most 3 times in no. 7 (word-code candidates); no reading, no grade, no family run. If none clears: logged as
"no sibling above the inventory null", which does not exclude a shared nomenclator (naming conventions differ; short pieces).
