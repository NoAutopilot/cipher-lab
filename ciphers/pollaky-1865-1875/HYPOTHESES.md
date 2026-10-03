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
