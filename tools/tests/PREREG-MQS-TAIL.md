# PREREG MQS-TAIL -- `tools/freq.py --tail N` (LANE MQS-3, account 4)

Written 9 Oct 2026, 10:06 UTC by date -u (commit eb3396cef; first draft said "10:1x", corrected), and pushed BEFORE any control below was run. Research row M23
(month, date, place and enclosure-mark symbols as one positional class; Lasry, Biermann and Tomokiyo 2023,
Cryptologia 47:2, pp.124-125 Fig. 12, p.137 n.99). Brief: `.claude/briefs/runs/2026-10-09-ytbiz-mqs3-tail.md`.

## Statistic and null

Per sign s: T(s) = occurrences of s in the edge window of every letter of the pool (the last N tokens with
`--tail-end end`, the first N with `start`, both with `both`). Null: for each letter i, its edge window is
replaced by a random contiguous window of the same length drawn from elsewhere in the pool (any letter j, a
start whose window does not overlap letter j's own edge window(s)); R = 2000 replicates, seed 1. A sign is
flagged when T(s) > the null's p95 for s (strictly), T(s) >= 2 and its one-sided p (share of replicates with
null T >= T(s)) <= 0.05. Signs are ranked by p, then by T(s) - null mean.

Why the null can fail differently from the known answer (rule 3): the statistic is a count at the edge
positions and the null moves the counted positions to random interior windows while keeping every token's
value and every letter's content, so a sign whose occurrences sit at letter ends gets a different count under
the null than in the target; a sign spread evenly through the letters does not. The manipulation (window
location) is on the same axis as the statistic (position), not orthogonal to it.

## Cell 1 -- known answer: Janssens pool (ciphers/na-janssens-java-1811)

Pool, cipher codes only, one letter per sequence (built by `tools/tests/mqs_tail_controls.py` from files on
disk): No.1 leaf 188 (`ciphertext.tsv`); No.2 gloss copy (`combined_passA.tsv` leaf 191 + `leaf192_reconciled.tsv`);
No.3 (`combined_passA.tsv` leaves 199-200); No.4 (`no4/no4_merge.tsv`); No.5 (`no5_cleancopy_passA.tsv`);
invnr 26 (`inv26_reconciled.tsv`, digits column). Leaf 190's partial copy and its raw lower block are left out
(they duplicate No.2). Month codes from key.tsv: 1089 Juillet (C), 845 Juin (C), 43 mars (C), 547 aoust (M).

Positions known before the run (from grep, not from the tool): datelines sit at letter HEADS on No.2 and No.3
("Batavia neuf Juillet", "onze Juillet") and on invnr 26 (845 at token 4); at letter ENDS on No.2 ("le trente
Juin. Fin.") and No.4 (547 last code); No.5 has 547 at token 17 and as its last code; 43 mars is mid-body on
No.3 (a date mentioned in the text, not a dateline). Because this pool puts datelines at both ends, the gate is
set on `--tail-end both`; `end` alone is reported beside it.

**Gate A (pre-registered):** `--tail 10 --tail-end both`, K = 10: at least 2 of the 3 edge-placed month codes
{1089, 845, 547} are flagged AND rank in the top 10. Expected: 1089 and 547 flagged; 845 borderline (n=3 in
the pool). 43 mars is expected NOT flagged (one body occurrence) -- reported, not gated.
**Reported beside it:** `--tail 10 --tail-end end`, K = 10: 547 and 845 ranks (expected 547 in top 10).

## Cell 2 -- mismatched: Lodewijk van Nassau pool (ciphers/lodewijk-van-nassau-1573-74)

Pool: `ciphertext_{4610,4611,4612_v3,4614,5801,5810,5811,7205,7206,7208}.tsv`, sign column, clear tokens
(`=...`), `[blank]` and empty cells dropped, so only cipher signs remain. The dates of these letters are written
in clear ("25 de Mars l'an 1574", NOTES.md), and the cipher is a letter cipher (key_*.tsv: letters and syllables),
so there is no month sign: the "must not rank month codes" condition is satisfied by construction and is NOT a
test. The falsifiable gate on this cell is the false-flag rate:

**Gate B (pre-registered):** `--tail 10 --tail-end both`: flagged signs <= 10% of the signs with total >= 5 in
the pool (nominal rate under no positional effect is about 5%; 10% allows for multiple testing and for real
closing formulas in cipher, e.g. a ciphered sign-off). Reported with the flagged list.

## Unit tests (offline, `tools/tests/test_freq.py`)

Synthetic pool: 30 letters of 80 tokens from 40 uniform body signs, a "month" sign planted in the last 3
tokens of 20 letters. Must catch: the planted sign ranks 1 and is flagged at `--tail 5`. Must NOT flag: the
same pool with each letter's tokens shuffled in place (positional effect destroyed) -- the planted sign is not
flagged in at least 9 of 10 shuffles.

## Outcome rule

Gates A and B both pass -> shelf grade `controlled-only` (one matched pool, one mismatched pool; no target run
from this job). Either misses -> `weak` with both numbers; the option ships, nothing is run on a target from it,
and it is not re-briefed. Results go to `tools/tests/MQS-TAIL-controls.tsv`.
