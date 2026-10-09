
## dev_tune vs L (benchmark-tx/txeng/units/labels_dev_tune.tsv): 12 wrong of 343 scored

Per signal
| signal / combination | wrong flagged | recall | flagged | share |
|---|---|---|---|---|
| show | 10/12 | 0.833 | 172/343 | 0.501 |
| disagree | 2/12 | 0.167 | 31/343 | 0.090 |
| bandcut | 5/12 | 0.417 | 59/343 | 0.172 |
| thin | 5/12 | 0.417 | 79/343 | 0.230 |
| contrast | 5/12 | 0.417 | 72/343 | 0.210 |
| stab | 1/12 | 0.083 | 18/343 | 0.052 |
| freq | 5/12 | 0.417 | 122/343 | 0.356 |
| latt | 5/12 | 0.417 | 19/343 | 0.055 |
| pair | 11/12 | 0.917 | 153/343 | 0.446 |
| pairclf | 2/12 | 0.167 | 13/343 | 0.038 |
| vote | 6/12 | 0.500 | 30/343 | 0.087 |
| selfcons | 7/12 | 0.583 | 39/343 | 0.114 |
| conf | 7/12 | 0.583 | 90/343 | 0.262 |
| countchk | 7/12 | 0.583 | 282/343 | 0.822 |
| n_signals>=2 | 12/12 | 1.000 | 285/343 | 0.831 |
| n_signals>=3 | 12/12 | 1.000 | 218/343 | 0.636 |
| n_signals>=4 | 10/12 | 0.833 | 157/343 | 0.458 |

Best OR-combination (k signals at most, share cap)
| k | cap | signal / combination | wrong flagged | recall | flagged | share |
|---|---|---|---|---|---|---|
| 1 | 0.1 | vote | 6/12 | 0.500 | 30/343 | 0.087 |
| 1 | 0.15 | selfcons | 7/12 | 0.583 | 39/343 | 0.114 |
| 1 | 0.2 | selfcons | 7/12 | 0.583 | 39/343 | 0.114 |
| 2 | 0.1 | vote | 6/12 | 0.500 | 30/343 | 0.087 |
| 2 | 0.15 | latt+vote | 9/12 | 0.750 | 36/343 | 0.105 |
| 2 | 0.2 | latt+vote | 9/12 | 0.750 | 36/343 | 0.105 |
| 3 | 0.1 | vote | 6/12 | 0.500 | 30/343 | 0.087 |
| 3 | 0.15 | latt+vote+selfcons | 10/12 | 0.833 | 48/343 | 0.140 |
| 3 | 0.2 | latt+vote+selfcons | 10/12 | 0.833 | 48/343 | 0.140 |

## dev_tune vs A (benchmark-tx/txeng/units/passA_dev_tune.tsv): 21 wrong of 343 scored

Per signal
| signal / combination | wrong flagged | recall | flagged | share |
|---|---|---|---|---|
| show | 18/21 | 0.857 | 172/343 | 0.501 |
| disagree | 10/21 | 0.476 | 31/343 | 0.090 |
| bandcut | 5/21 | 0.238 | 59/343 | 0.172 |
| thin | 10/21 | 0.476 | 79/343 | 0.230 |
| contrast | 8/21 | 0.381 | 72/343 | 0.210 |
| stab | 1/21 | 0.048 | 18/343 | 0.052 |
| freq | 6/21 | 0.286 | 122/343 | 0.356 |
| latt | 12/21 | 0.571 | 19/343 | 0.055 |
| pair | 11/21 | 0.524 | 153/343 | 0.446 |
| pairclf | 2/21 | 0.095 | 13/343 | 0.038 |
| vote | 14/21 | 0.667 | 30/343 | 0.087 |
| selfcons | 16/21 | 0.762 | 39/343 | 0.114 |
| conf | 15/21 | 0.714 | 90/343 | 0.262 |
| countchk | 14/21 | 0.667 | 282/343 | 0.822 |
| n_signals>=2 | 21/21 | 1.000 | 285/343 | 0.831 |
| n_signals>=3 | 21/21 | 1.000 | 218/343 | 0.636 |
| n_signals>=4 | 19/21 | 0.905 | 157/343 | 0.458 |

Best OR-combination (k signals at most, share cap)
| k | cap | signal / combination | wrong flagged | recall | flagged | share |
|---|---|---|---|---|---|---|
| 1 | 0.1 | vote | 14/21 | 0.667 | 30/343 | 0.087 |
| 1 | 0.15 | selfcons | 16/21 | 0.762 | 39/343 | 0.114 |
| 1 | 0.2 | selfcons | 16/21 | 0.762 | 39/343 | 0.114 |
| 2 | 0.1 | vote | 14/21 | 0.667 | 30/343 | 0.087 |
| 2 | 0.15 | latt+selfcons | 18/21 | 0.857 | 44/343 | 0.128 |
| 2 | 0.2 | latt+selfcons | 18/21 | 0.857 | 44/343 | 0.128 |
| 3 | 0.1 | vote | 14/21 | 0.667 | 30/343 | 0.087 |
| 3 | 0.15 | latt+vote+selfcons | 19/21 | 0.905 | 48/343 | 0.140 |
| 3 | 0.2 | latt+vote+selfcons | 19/21 | 0.905 | 48/343 | 0.140 |
