# malsburg-hessen-1636 sign pool (LANE B9 orchestrator)

Leaves enter only when `tools/leaf_pool_gate.py` says ADMITTED (pre-registered 08:19 UTC 26 Sept 2026: M share <= 0.15,
off-form <= 0.05, value-frequency cosine against the pool > relabel p95; CLAUDE.md rule 3 per-unit merge gate).
`pooled.tsv` is rebuilt from the admitted leaves' files; ILLEGIBLE rows and clear words ("Und") are dropped.

| Leaf | Record | Source file | Gate line | Signs pooled | Admitted |
|---|---|---|---|---|---|
| ff.3, 12 | 496, 497 | ciphertext.txt (bMAL3) | f.12 vs f.3: cosine 0.571 vs p95 0.514 | 351 | 26 Sept 09:35 (base) |
| f.23 | 505 | recon_0023/ciphertext_draft.tsv (bMAL23) | N=1503 M 0.144, off-form 0.039, cosine 0.826 vs p95 0.515 | 1,477 | 26 Sept 09:35 |
| f.28 | 507 | recon_0028/ciphertext_draft.tsv (bMAL28 + bMAL28B, L05-L57) | N=2363, M 0.214 > 0.15 -- HELD (cosine passes) | 0 | held |
| f.16 | 503 | recon_0016/ (bMAL16) | N=891, M 0.36, off-form 0.06-0.08 -- HELD (cosine 0.83 vs p95 0.56 passes) | 0 | held |
| f.24 | 505 | recon_0024/ (bMAL24, block 1 only) | N=211, M 0.27 -- HELD (cosine 0.777 vs p95 0.399 passes) | 0 | held |

Pool at 09:35 UTC: **1,828 signs**, 173 distinct values (includes about 4% off-form signs from f.23, graded M).

At the LANE B9 close (10:17 UTC): pool unchanged at 1,828 signs. bMALH ran homophonic profile=target on it: control 0.637, target FAIL (HYPOTHESES.md).
