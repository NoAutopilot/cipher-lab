# tx_power: pass share of planted instruments per gate (draws 1000, seed 1)
A pass is fixed > broken and two-sided sign test p < alpha. clean: fixes FIX of the errors, breaks none; noisyK: also breaks correct signs at base_err x K; worse: breaks 0.3E, fixes none; noop; random3: 3% of positions flipped at random.

| unit | E | N | fix | clean@0.01 | clean@0.05 | noisy0.5@0.01 | noisy0.5@0.05 | noisy0.1@0.01 | noisy0.1@0.05 | worse@0.01 | worse@0.05 | noop@0.01 | noop@0.05 | random3@0.01 | random3@0.05 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| eval_heldout_ds | 9 | 376 | 0.3 | 0.000 | 0.020 | 0.000 | 0.000 | 0.000 | 0.011 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| eval_heldout_ds | 9 | 376 | 0.5 | 0.027 | 0.265 | 0.000 | 0.002 | 0.016 | 0.120 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| f152r | 4 | 73 | 0.3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| f152r | 4 | 73 | 0.5 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| eval_pool_ds | 13 | 449 | 0.3 | 0.026 | 0.180 | 0.000 | 0.001 | 0.004 | 0.062 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| eval_pool_ds | 13 | 449 | 0.5 | 0.295 | 0.692 | 0.001 | 0.007 | 0.081 | 0.305 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |

## Smallest E (baseline errors) at which a clean fixer passes >= 80% of draws (N = 10E)
| fix | alpha 0.01 | alpha 0.05 |
|---|---|---|
| 0.3 | 33 | 25 |
| 0.5 | 20 | 14 |
