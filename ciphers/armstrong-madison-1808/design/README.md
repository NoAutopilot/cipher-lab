# design/ -- ARM-DESIGN, 26 Sept 2026 (LANE ARM, Fable)

`python3 design_stats.py --sims 60 --seed 1` regenerates everything here offline from
`tools/data/uscodes-1800/*.tsv` (+ the THE=972 usage strings in its `stats.py`), `tools/data/en18/*.txt.gz` and
`../ciphertext.txt` (about 10 s). Outputs: `stats_real.tsv` (target, four real THE=972 letters, pooled),
`stats_sim.tsv` (per design x statistic: mean, sd, p05/p50/p95 over 60 simulated 369-token letters, target value
and percentile), `table_layout.txt` (WE028 and THE972 alphabetical-run structure, first letter per hundred),
`sim_tokens_example.tsv` (first 120 tokens of one simulated letter per design), `run_log.txt` (console summary
incl. OOV drop counts, Zipf K fits, en18 coverage curve). Verdict and reading of the numbers: HYPOTHESES.md
"ARM-DESIGN"; next job's spec: `family_C_spec.md`. Seeds: design i uses `random.Random(1000*seed + i)`.
