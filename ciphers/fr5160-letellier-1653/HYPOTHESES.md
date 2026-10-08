# HYPOTHESES -- fr5160-letellier-1653

| date | job | hypothesis | instrument | control | target | gate | result |
|---|---|---|---|---|---|---|---|
| 8 Oct 2026 | D1A-F68 | key_1659 (from f.86/f.88 + f.87) reads f.67 in agreement with its clear copy f.68r | test_f68_key1659.py, per-aligned-token agreement, PREREG-D1A-F68.md | f.68r words shuffled within lines, 1000x: mean 0.474, p99 0.518 | 0.801 (419/523) | S > p99 | PASS |
| 8 Oct 2026 | D4-F5160B | key_1646 / Tomokiyo 1647 / Tomokiyo 1651 / key_1659 reads the canvas 11-12 block or canvas 32 (text-level reconciled) | trial_1653.py, fr16 order-5 bits/char over keyed runs, trial_1653_c11c32.tsv | 200 key derangements per key and letter; synthetic French at the same keyed positions (all four keys separate on it) | pooled c11+c32: 1646 z -2.96, 1647 z 1.89, 1651 z 0.89, 1659 z 2.84 (0/200 derangements >= real) | real > every derangement and synthetic separates | key_1659 PASS at character level only (c32, pooled; c11 1/200 >= real), no French words; others FAIL; no reading |
