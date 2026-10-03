# pollaky-1865-1875 -- hypotheses (append-only)

Opened 3 Oct 2026 (GAPS156, account-4). Rule 3: each family row carries its matched control beside the target.

## Ad 2 (1871 telegram), 10x10 homophonic bigram design (Ernst's sibling prior) -- GAPS156, 3 Oct 2026

Statistic: non-overlapping bigram IC, phase 0. Null: 200 uniform digit strings of the same length. Controls: synthetic
10x10 homophonic encipherments of English (tools/data en sources), A = frequency-proportional, B = random allocation.
Script: scripts/bigram_prior.py (seed 156). Pre-registered in NOTES.md before scoring (commit dca24eee).

| text | N bigrams | target IC | null p95 | null tail | control A power | control B power | verdict |
|---|---|---|---|---|---|---|---|
| ad 2 1871 | 57 | 0.0138 | 0.0144 | 0.085 | 0.053 | 0.869 | A: non-test (untestable by bigram IC at N=57); B: inconclusive |
| sib 1864 | 25 | 0.0267 | 0.0200 | 0.010 | 0.030 | 0.345 | below power both variants: no licence |
| sib 1865 | 28 | 0.0185 | 0.0185 | 0.125 | 0.048 | 0.440 | below power both variants: no licence |

Status of the hypothesis: untested-by-this-tool for design A (not refuted); open for design B.

## Ad 1 (1865 sign script), Laura's bars-x-dots component rule -- GAPS160, 3 Oct 2026

Statistic T: mean add-one bigram log10 prob of "timeto"+X+"shall" (clear frame as crib); W: word-segmentation coverage.
Controls at N=10: A 2000 shuffled-sign orders, B 2000 random-sign strings over the rule's 21 cells, C 104 sibling
rules. Positive control: 2000 corpus windows over a-u. Script: scripts/laura_rule.py (seed 160). Pre-registered in
NOTES.md before scoring (commit 577aeea6).

| text | X | target T | A p95 (tail) | B p95 (tail) | C rank | W vs B p95 | power (T / W) | verdict |
|---|---|---|---|---|---|---|---|---|
| ad 1, our table | bencabuchp | -1.1405 | -1.2895 (0.002) | -1.2026 (0.019) | 1/104 | 0.6 vs 0.6 | 0.981 / 0.868 | supported on T (design candidate); W does not clear |
| ad 1, Laura's sign 04 | bendabuchp | -1.1074 | -1.2555 (0.001) | -1.2045 (0.005) | 1/104 | 0.5 vs 0.6 | same | same |

Status: supported as a design candidate on letter-bigram order (post-hoc rule; C weak by construction); no word read,
10 letters M.

## Ad 2 (1871 telegram) = Boyouk's 1867 "ELOPED" clear ad, one group per 1-3-word chunk -- GAPS164, 3 Oct 2026

Statistic S: log10 share of monotone alignments (each group 1-3 consecutive words) in which the two "91" groups cover
identical chunks. Control: 2000 same-length windows of period English prose (Holmes 1892, Huck Finn 1884, Pride 1813).
Positive control: 200 synthetic chunk codes from fresh windows. Script: scripts/boyouk_align.py (seed 164). Pre-registered
in NOTES.md before scoring (commit f065906d).

| plaintext | groups | S target | control p95 (tail) | power | verdict |
|---|---|---|---|---|---|
| whole ad (73 words) | 36 split | -2.962 | -2.330 (0.384) | 0.335 | untestable |
| minus address (64) | 36 split | -1.970 | -1.983 (0.045) | 0.315 | untestable |
| whole ad | 35 joined | -2.795 | -2.394 (0.268) | 0.375 | untestable |
| minus address | 35 joined | -2.080 | -2.088 (0.048) | 0.320 | untestable |

Status: untested-by-this-tool at N=36 with one repeated group (power < 0.5), not refuted.
