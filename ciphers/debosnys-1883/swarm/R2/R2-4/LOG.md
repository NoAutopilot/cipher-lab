# R2-4 LOG

| time (UTC) | step | parameters | control | target | note |
|---|---|---|---|---|---|
| 08:16 | PREREG.md committed (572aa02d) | classes by drawing, alpha, gates | -- | -- | before any count |
| 08:18 | line_units.py FAST=1 | smoke test | -- | -- | IndexError: extreme-width token with no +-20 pct neighbour (K3 random draws); fallback to 5 nearest widths added; exact Poisson-binomial slot null added (the infinite-shuffle limit of the registered null) so K1/K2 run at full count |
| 08:19 | line_units.py full | seeds fixed | K1 0.310, K1r 0.297 FAIL; K2 1.000/0.006 pass; K3 0.054 FAIL (marginal), 1.000 pass | T1 5/8 p 3.4e-6; T2 p_layout 0; T3 1/4 p 0.957 | controls fail the registered all-gates rule: target unlicensed; no second attempt |
