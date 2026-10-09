
## eval_heldout vs L (benchmark-tx/txeng/units/labels_eval_heldout.tsv): 15 wrong of 376 scored

Per signal
| signal / combination | wrong flagged | recall | flagged | share |
|---|---|---|---|---|
| show | 14/15 | 0.933 | 151/376 | 0.402 |
| disagree | 6/15 | 0.400 | 20/376 | 0.053 |
| bandcut | 5/15 | 0.333 | 63/376 | 0.168 |
| thin | 8/15 | 0.533 | 143/376 | 0.380 |
| contrast | 3/15 | 0.200 | 69/376 | 0.184 |
| stab | 1/15 | 0.067 | 10/376 | 0.027 |
| freq | 7/15 | 0.467 | 176/376 | 0.468 |
| latt | 6/15 | 0.400 | 7/376 | 0.019 |
| pair | 12/15 | 0.800 | 177/376 | 0.471 |
| vote4 | 4/15 | 0.267 | 6/376 | 0.016 |
| n_signals>=2 | 15/15 | 1.000 | 242/376 | 0.644 |
| n_signals>=3 | 13/15 | 0.867 | 142/376 | 0.378 |
| n_signals>=4 | 11/15 | 0.733 | 67/376 | 0.178 |

Fixed combination (chosen elsewhere, not re-chosen)
| signal / combination | wrong flagged | recall | flagged | share |
|---|---|---|---|---|
| latt+vote+selfcons | 6/15 | 0.400 | 7/376 | 0.019 |

## eval_heldout vs A (benchmark-tx/txeng/units/passA_eval_heldout.tsv): 18 wrong of 376 scored

Per signal
| signal / combination | wrong flagged | recall | flagged | share |
|---|---|---|---|---|
| show | 17/18 | 0.944 | 151/376 | 0.402 |
| disagree | 9/18 | 0.500 | 20/376 | 0.053 |
| bandcut | 6/18 | 0.333 | 63/376 | 0.168 |
| thin | 11/18 | 0.611 | 143/376 | 0.380 |
| contrast | 4/18 | 0.222 | 69/376 | 0.184 |
| stab | 2/18 | 0.111 | 10/376 | 0.027 |
| freq | 7/18 | 0.389 | 176/376 | 0.468 |
| latt | 7/18 | 0.389 | 7/376 | 0.019 |
| pair | 13/18 | 0.722 | 177/376 | 0.471 |
| vote4 | 5/18 | 0.278 | 6/376 | 0.016 |
| n_signals>=2 | 18/18 | 1.000 | 242/376 | 0.644 |
| n_signals>=3 | 16/18 | 0.889 | 142/376 | 0.378 |
| n_signals>=4 | 14/18 | 0.778 | 67/376 | 0.178 |

Fixed combination (chosen elsewhere, not re-chosen)
| signal / combination | wrong flagged | recall | flagged | share |
|---|---|---|---|---|
| latt+vote+selfcons | 7/18 | 0.389 | 7/376 | 0.019 |
