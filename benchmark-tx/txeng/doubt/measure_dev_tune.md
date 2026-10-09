
## dev_tune vs L (benchmark-tx/txeng/units/labels_dev_tune.tsv): 14 wrong of 343 scored

Per signal
| signal / combination | wrong flagged | recall | flagged | share |
|---|---|---|---|---|
| show | 11/14 | 0.786 | 172/343 | 0.501 |
| disagree | 2/14 | 0.143 | 31/343 | 0.090 |
| bandcut | 5/14 | 0.357 | 59/343 | 0.172 |
| thin | 5/14 | 0.357 | 79/343 | 0.230 |
| contrast | 5/14 | 0.357 | 72/343 | 0.210 |
| stab | 1/14 | 0.071 | 18/343 | 0.052 |
| freq | 6/14 | 0.429 | 122/343 | 0.356 |
| latt | 5/14 | 0.357 | 19/343 | 0.055 |
| pair | 11/14 | 0.786 | 153/343 | 0.446 |
| n_signals>=2 | 13/14 | 0.929 | 218/343 | 0.636 |
| n_signals>=3 | 10/14 | 0.714 | 137/343 | 0.399 |
| n_signals>=4 | 7/14 | 0.500 | 57/343 | 0.166 |

Best OR-combination (k signals at most, share cap)
| k | cap | signal / combination | wrong flagged | recall | flagged | share |
|---|---|---|---|---|---|---|
| 1 | 0.1 | latt | 5/14 | 0.357 | 19/343 | 0.055 |
| 1 | 0.15 | latt | 5/14 | 0.357 | 19/343 | 0.055 |
| 1 | 0.2 | latt | 5/14 | 0.357 | 19/343 | 0.055 |
| 2 | 0.1 | latt | 5/14 | 0.357 | 19/343 | 0.055 |
| 2 | 0.15 | disagree+latt | 6/14 | 0.429 | 36/343 | 0.105 |
| 2 | 0.2 | disagree+latt | 6/14 | 0.429 | 36/343 | 0.105 |
| 3 | 0.1 | latt | 5/14 | 0.357 | 19/343 | 0.055 |
| 3 | 0.15 | disagree+latt | 6/14 | 0.429 | 36/343 | 0.105 |
| 3 | 0.2 | disagree+latt | 6/14 | 0.429 | 36/343 | 0.105 |

## dev_tune vs A (benchmark-tx/txeng/units/passA_dev_tune.tsv): 23 wrong of 343 scored

Per signal
| signal / combination | wrong flagged | recall | flagged | share |
|---|---|---|---|---|
| show | 19/23 | 0.826 | 172/343 | 0.501 |
| disagree | 10/23 | 0.435 | 31/343 | 0.090 |
| bandcut | 5/23 | 0.217 | 59/343 | 0.172 |
| thin | 10/23 | 0.435 | 79/343 | 0.230 |
| contrast | 8/23 | 0.348 | 72/343 | 0.210 |
| stab | 1/23 | 0.043 | 18/343 | 0.052 |
| freq | 7/23 | 0.304 | 122/343 | 0.356 |
| latt | 12/23 | 0.522 | 19/343 | 0.055 |
| pair | 11/23 | 0.478 | 153/343 | 0.446 |
| n_signals>=2 | 22/23 | 0.957 | 218/343 | 0.636 |
| n_signals>=3 | 18/23 | 0.783 | 137/343 | 0.399 |
| n_signals>=4 | 12/23 | 0.522 | 57/343 | 0.166 |

Best OR-combination (k signals at most, share cap)
| k | cap | signal / combination | wrong flagged | recall | flagged | share |
|---|---|---|---|---|---|---|
| 1 | 0.1 | latt | 12/23 | 0.522 | 19/343 | 0.055 |
| 1 | 0.15 | latt | 12/23 | 0.522 | 19/343 | 0.055 |
| 1 | 0.2 | latt | 12/23 | 0.522 | 19/343 | 0.055 |
| 2 | 0.1 | latt | 12/23 | 0.522 | 19/343 | 0.055 |
| 2 | 0.15 | disagree+latt | 14/23 | 0.609 | 36/343 | 0.105 |
| 2 | 0.2 | disagree+latt | 14/23 | 0.609 | 36/343 | 0.105 |
| 3 | 0.1 | latt | 12/23 | 0.522 | 19/343 | 0.055 |
| 3 | 0.15 | disagree+latt | 14/23 | 0.609 | 36/343 | 0.105 |
| 3 | 0.2 | disagree+latt | 14/23 | 0.609 | 36/343 | 0.105 |
