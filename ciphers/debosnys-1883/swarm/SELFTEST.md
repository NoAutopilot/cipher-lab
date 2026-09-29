# Harness self-tests (DEB-SWARM-0, 29 Sept 2026, 03:0x-03:1x UTC)

All on controls; the harness never fitted or scored a key on c1 or c2 (apart from the one frequency-only key below,
built from sign counts with no language model, to test the null). 1000 shuffles each; pct / pct_strat.

| key | fit -> test | recovery on test | fr_quad | fr_dict | vocab | passes the bar direction? |
|---|---|---|---|---|---|---|
| planted (sealed answer) | FR-HOMO c1 -> c2 | 74.5 | 100 / 100 | | | yes |
| planted | FR-HOMO c2 -> c1 | 94.7 | 100 / 100 | | | yes |
| random permutation of planted | FR-HOMO c1 -> c2 | 0.9 | 23.1 | | | no |
| random permutation of planted | FR-HOMO c2 -> c1 | 0.8 | 64.1 | | | no |
| frequency-only (counts -> French letter frequencies) | NULL c1 -> c2 | - | 99.9 / 93.9 | 0 / 0 | 0 / 0 | no |
| frequency-only | NULL c2 -> c1 | - | 99.9 / 83.5 | 0 / 0 | 74.1 / 64.0 | no |
| frequency-only | real c1 -> c2 | - | 97.7 / 77.3 | 61.7 / 35.6 | 84.5 / 74.0 | no |
| climber, French, 6 x 60000 | FR-HOMO c1 -> c2 | 1.1 | 70.9 / 47.5 | 89.9 / 83.4 | 5.3 | no (overfit on 132 signs) |
| climber | FR-HOMO c2 -> c1 | 25.8 | 100.0 / 99.6 | 96.8 / 91.4 | 70.7 | no (strat 996/1000) |
| climber | FR-HOMO c1+c2a -> c2b | 22.8 | 100 / 100 | 100 / 99.9 | 99.6 | yes (fold, one direction) |
| climber | NULL c1 -> c2 | - | 83.0 / 49.6 | 51.7 / 37.2 | 52.2 | no |
| climber | NULL c2 -> c1 | - | 78.7 / 17.7 | 0 / 0 | 84.2 | no |
| climber | NULL c1+c2a -> c2b | - | 93.7 / 86.6 | 7.6 / 5.1 | 71.3 | no |

Commands: `python3 score.py --selftest`; `python3 selftest_climb.py <FIT> OUT.tsv --restarts 6 --iters 60000 --seed 3`
then `python3 score.py OUT.tsv --fit <FIT> --test <TEST>`.

Reading: the plain-shuffle null alone passes frequency matching (99.9 on NULL); the stratified null does not. A
correct key passes both nulls both ways; a partial key (23-26 pct recovery) fitted on 450-650 signs passes or nearly
passes; a key fitted on c1 alone does not, even on the answer-known control. The climber on NULL passes nothing.
Leak closed before freezing: recovery mode is refused on the blind set, and an empty value never counts as recovered.
