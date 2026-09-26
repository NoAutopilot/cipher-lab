# malsburg-hessen-1636 sign pool (LANE B9 orchestrator)

Leaves enter only when `tools/leaf_pool_gate.py` says ADMITTED (pre-registered 08:19 UTC 26 Sept 2026: M share <= 0.15,
off-form <= 0.05, value-frequency cosine against the pool > relabel p95; CLAUDE.md rule 3 per-unit merge gate).
`pooled.tsv` is rebuilt from the admitted leaves' files; ILLEGIBLE rows and clear words ("Und") are dropped.

| Leaf | Record | Source file | Gate line | Signs pooled | Admitted |
|---|---|---|---|---|---|
| ff.3, 12 | 496, 497 | ciphertext.txt (bMAL3) | f.12 vs f.3: cosine 0.571 vs p95 0.514 | 351 | 26 Sept 09:35 (base) |
| f.23 | 505 | recon_0023/ciphertext_draft.tsv (bMAL23) | N=1503 M 0.144, off-form 0.039, cosine 0.826 vs p95 0.515 | 1,477 | 26 Sept 09:35 |
| f.28 | 507 | recon_0028/ciphertext_draft.tsv (bMAL28, L05-L44) | M 0.232 > 0.15 -- HELD (cosine 0.681 vs p95 0.514 passes) | 0 | held pending settle |

Pool at 09:35 UTC: **1,828 signs**, 173 distinct values (includes about 4% off-form signs from f.23, graded M).
