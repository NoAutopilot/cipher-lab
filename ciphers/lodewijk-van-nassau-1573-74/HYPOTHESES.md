# lodewijk-van-nassau-1573-74 -- hypothesis families

Append-only. Rows below are written by `tools/family_run.py` (CLAUDE.md rule 3: the matched CONTROL number sits beside the TARGET number in every row; a row with gate met = no reports a control that could not read its own design, and the target was not run). Prose sections may be added above this table by workers.

## AX-4612 pre-registration (26 Sept 2026, 01:48 UTC, written before any target run)

Target: WVO 4612 numerals 1-120 (N=775, K=100, 20 runs; specs/lodewijk-4612.json). Family `block_homophonic`
(tools/families/block_homophonic.py). Gate: control mean recovery >= 0.6 over 3 seeds (1-3), 8 restarts, fr16 corpora,
--param gap=80. H1 width 5 offsets 0-4; H2 widths 4 and 6 (all offsets) only if H1's control passes and its target
fails the judge; H3 `homophonic --param profile=target` last, control first. A target "reads" only on a judge PASS
(fr16, three files); a control below 0.6 stops that family and is itself the logged result.

<!-- family_run.py table: one row per run, appended by the tool, never edited by hand -->

| date (UTC) | family | parameters | seeds | CONTROL mean (range) | TARGET best score | judge | gate met | label |
|---|---|---|---|---|---|---|---|---|
| 26 Sept 2026 01:49 | block_homophonic | N=775 K=100 restarts=8 corpus=lettresdecatheri01cathuoft_djvu.txt.gz+lettresdecatheri02cathuoft_djvu.txt.gz+lettresindites00marg_djvu.txt.gz width=5,offset=0,gap=80 | 1 | 0.722 (0.210-0.982) | -2175.295 | FAIL language: score=-1.302, null_p99=-1.718, real_p05=-0.944, real_median=-0.818, mode=both, N=775 | yes (gate 0.6) | AX-4612 H1 w5 o0 |
| 26 Sept 2026 01:50 | block_homophonic | N=775 K=100 restarts=8 corpus=lettresdecatheri01cathuoft_djvu.txt.gz+lettresdecatheri02cathuoft_djvu.txt.gz+lettresindites00marg_djvu.txt.gz width=5,offset=1,gap=80 | 1 | 0.722 (0.210-0.982) | -2142.207 | FAIL language: score=-1.312, null_p99=-1.718, real_p05=-0.944, real_median=-0.818, mode=both, N=775 | yes (gate 0.6) | AX-4612 H1 w5 o1 |
| 26 Sept 2026 01:51 | block_homophonic | N=775 K=100 restarts=8 corpus=lettresdecatheri01cathuoft_djvu.txt.gz+lettresdecatheri02cathuoft_djvu.txt.gz+lettresindites00marg_djvu.txt.gz width=5,offset=2,gap=80 | 1 | 0.722 (0.210-0.982) | -2161.736 | FAIL language: score=-1.324, null_p99=-1.718, real_p05=-0.944, real_median=-0.818, mode=both, N=775 | yes (gate 0.6) | AX-4612 H1 w5 o2 |
| 26 Sept 2026 01:52 | block_homophonic | N=775 K=100 restarts=8 corpus=lettresdecatheri01cathuoft_djvu.txt.gz+lettresdecatheri02cathuoft_djvu.txt.gz+lettresindites00marg_djvu.txt.gz width=5,offset=3,gap=80 | 1 | 0.722 (0.210-0.982) | -2141.159 | FAIL language: score=-1.28, null_p99=-1.718, real_p05=-0.944, real_median=-0.818, mode=both, N=775 | yes (gate 0.6) | AX-4612 H1 w5 o3 |
| 26 Sept 2026 01:53 | block_homophonic | N=775 K=100 restarts=8 corpus=lettresdecatheri01cathuoft_djvu.txt.gz+lettresdecatheri02cathuoft_djvu.txt.gz+lettresindites00marg_djvu.txt.gz width=5,offset=4,gap=80 | 1 | 0.722 (0.210-0.982) | -2133.318 | FAIL language: score=-1.3, null_p99=-1.718, real_p05=-0.944, real_median=-0.818, mode=both, N=775 | yes (gate 0.6) | AX-4612 H1 w5 o4 |
| 26 Sept 2026 01:54 | block_homophonic | N=775 K=100 restarts=8 corpus=lettresdecatheri01cathuoft_djvu.txt.gz+lettresdecatheri02cathuoft_djvu.txt.gz+lettresindites00marg_djvu.txt.gz width=4,offset=0,gap=80 | 1 | 0.852 (0.599-0.982) | -2121.755 | FAIL language: score=-1.241, null_p99=-1.718, real_p05=-0.944, real_median=-0.818, mode=both, N=775 | yes (gate 0.6) | AX-4612 H2 w4 o0 |
| 26 Sept 2026 01:54 | block_homophonic | N=775 K=100 restarts=8 corpus=lettresdecatheri01cathuoft_djvu.txt.gz+lettresdecatheri02cathuoft_djvu.txt.gz+lettresindites00marg_djvu.txt.gz width=4,offset=1,gap=80 | 1 | 0.977 (0.974-0.982) | -2115.745 | FAIL language: score=-1.277, null_p99=-1.718, real_p05=-0.944, real_median=-0.818, mode=both, N=775 | yes (gate 0.6) | AX-4612 H2 w4 o1 |
| 26 Sept 2026 01:55 | block_homophonic | N=775 K=100 restarts=8 corpus=lettresdecatheri01cathuoft_djvu.txt.gz+lettresdecatheri02cathuoft_djvu.txt.gz+lettresindites00marg_djvu.txt.gz width=4,offset=2,gap=80 | 1 | 0.966 (0.947-0.982) | -2105.265 | FAIL language: score=-1.299, null_p99=-1.718, real_p05=-0.944, real_median=-0.818, mode=both, N=775 | yes (gate 0.6) | AX-4612 H2 w4 o2 |
| 26 Sept 2026 01:56 | block_homophonic | N=775 K=100 restarts=8 corpus=lettresdecatheri01cathuoft_djvu.txt.gz+lettresdecatheri02cathuoft_djvu.txt.gz+lettresindites00marg_djvu.txt.gz width=4,offset=3,gap=80 | 1 | 0.966 (0.943-0.982) | -2108.927 | FAIL language: score=-1.33, null_p99=-1.718, real_p05=-0.944, real_median=-0.818, mode=both, N=775 | yes (gate 0.6) | AX-4612 H2 w4 o3 |
| 26 Sept 2026 01:57 | block_homophonic | N=775 K=100 restarts=8 corpus=lettresdecatheri01cathuoft_djvu.txt.gz+lettresdecatheri02cathuoft_djvu.txt.gz+lettresindites00marg_djvu.txt.gz width=6,offset=0,gap=80 | 1 | 0.717 (0.225-0.966) | -2186.973 | FAIL language: score=-1.302, null_p99=-1.718, real_p05=-0.944, real_median=-0.818, mode=both, N=775 | yes (gate 0.6) | AX-4612 H2 w6 o0 |
| 26 Sept 2026 01:58 | block_homophonic | N=775 K=100 restarts=8 corpus=lettresdecatheri01cathuoft_djvu.txt.gz+lettresdecatheri02cathuoft_djvu.txt.gz+lettresindites00marg_djvu.txt.gz width=6,offset=1,gap=80 | 1 | 0.873 (0.676-0.982) | -2184.899 | FAIL language: score=-1.286, null_p99=-1.718, real_p05=-0.944, real_median=-0.818, mode=both, N=775 | yes (gate 0.6) | AX-4612 H2 w6 o1 |
| 26 Sept 2026 01:59 | block_homophonic | N=775 K=100 restarts=8 corpus=lettresdecatheri01cathuoft_djvu.txt.gz+lettresdecatheri02cathuoft_djvu.txt.gz+lettresindites00marg_djvu.txt.gz width=6,offset=2,gap=80 | 1 | 0.972 (0.961-0.982) | -2205.635 | FAIL language: score=-1.366, null_p99=-1.718, real_p05=-0.944, real_median=-0.818, mode=both, N=775 | yes (gate 0.6) | AX-4612 H2 w6 o2 |
| 26 Sept 2026 02:00 | block_homophonic | N=775 K=100 restarts=8 corpus=lettresdecatheri01cathuoft_djvu.txt.gz+lettresdecatheri02cathuoft_djvu.txt.gz+lettresindites00marg_djvu.txt.gz width=6,offset=3,gap=80 | 1 | 0.972 (0.961-0.982) | -2239.331 | FAIL language: score=-1.347, null_p99=-1.718, real_p05=-0.944, real_median=-0.818, mode=both, N=775 | yes (gate 0.6) | AX-4612 H2 w6 o3 |
| 26 Sept 2026 02:01 | block_homophonic | N=775 K=100 restarts=8 corpus=lettresdecatheri01cathuoft_djvu.txt.gz+lettresdecatheri02cathuoft_djvu.txt.gz+lettresindites00marg_djvu.txt.gz width=6,offset=4,gap=80 | 1 | 0.977 (0.974-0.982) | -2197.671 | FAIL language: score=-1.313, null_p99=-1.718, real_p05=-0.944, real_median=-0.818, mode=both, N=775 | yes (gate 0.6) | AX-4612 H2 w6 o4 |
| 26 Sept 2026 02:02 | block_homophonic | N=775 K=100 restarts=8 corpus=lettresdecatheri01cathuoft_djvu.txt.gz+lettresdecatheri02cathuoft_djvu.txt.gz+lettresindites00marg_djvu.txt.gz width=6,offset=5,gap=80 | 1 | 0.813 (0.489-0.977) | -2167.638 | FAIL language: score=-1.283, null_p99=-1.718, real_p05=-0.944, real_median=-0.818, mode=both, N=775 | yes (gate 0.6) | AX-4612 H2 w6 o5 |
| 26 Sept 2026 02:03 | homophonic | N=775 K=100 restarts=8 corpus=lettresdecatheri01cathuoft_djvu.txt.gz+lettresdecatheri02cathuoft_djvu.txt.gz+lettresindites00marg_djvu.txt.gz profile=target | 1 | 0.660 (0.443-0.959) | -1865.040 | FAIL language: score=-1.213, null_p99=-1.718, real_p05=-0.944, real_median=-0.818, mode=both, N=775 | yes (gate 0.6) | AX-4612 H3 free homophonic |
| 26 Sept 2026 02:05 | block_homophonic | N=775 K=96 restarts=8 corpus=lettresdecatheri01cathuoft_djvu.txt.gz+lettresdecatheri02cathuoft_djvu.txt.gz+lettresindites00marg_djvu.txt.gz width=5,offset=0,gap=80 | 1 | 0.989 (0.978-0.997) | -1901.105 | FAIL language: score=-1.128, null_p99=-1.718, real_p05=-0.944, real_median=-0.818, mode=both, N=775 | yes (gate 0.6) | AX-4612 real-letter positive control 5811 (key.tsv design) cut to N=775 |
| 26 Sept 2026 02:05 | block_homophonic | N=775 K=94 restarts=8 corpus=lettresdecatheri01cathuoft_djvu.txt.gz+lettresdecatheri02cathuoft_djvu.txt.gz+lettresindites00marg_djvu.txt.gz width=5,offset=0,gap=80 | 1 | 0.739 (0.462-0.965) | -1823.690 | FAIL language: score=-1.048, null_p99=-1.718, real_p05=-0.944, real_median=-0.818, mode=both, N=775 | yes (gate 0.6) | AX-4612 real-letter positive control 4610 (key.tsv design) cut to N=775 |
| 26 Sept 2026 02:07 | block_homophonic | N=775 K=100 restarts=8 corpus=lettresdecatheri01cathuoft_djvu.txt.gz+lettresdecatheri02cathuoft_djvu.txt.gz+lettresindites00marg_djvu.txt.gz width=5,offset=0,gap=80,shuffle_target=1 | 1 | 0.722 (0.210-0.982) | -2224.320 | FAIL language: score=-1.387, null_p99=-1.718, real_p05=-0.944, real_median=-0.818, mode=both, N=775 | yes (gate 0.6) | AX-4612 H1 w5 o0 shuffle floor |
| 26 Sept 2026 02:07 | homophonic | N=775 K=100 restarts=8 corpus=lettresdecatheri01cathuoft_djvu.txt.gz+lettresdecatheri02cathuoft_djvu.txt.gz+lettresindites00marg_djvu.txt.gz profile=target,shuffle_target=1 | 1 | 0.660 (0.443-0.959) | -1921.249 | FAIL language: score=-1.217, null_p99=-1.718, real_p05=-0.944, real_median=-0.818, mode=both, N=775 | yes (gate 0.6) | AX-4612 H3 shuffle floor |
| 26 Sept 2026 02:08 | homophonic | N=775 K=96 restarts=8 corpus=lettresdecatheri01cathuoft_djvu.txt.gz+lettresdecatheri02cathuoft_djvu.txt.gz+lettresindites00marg_djvu.txt.gz profile=target | 1-3 | 0.562 (0.317-0.915) | not run (CONTROL BELOW GATE) | - | no (gate 0.6) | AX-4612 H3 real 5811 N775 |

<!-- Below: a key-seeded anneal (tools/homophonic_anneal.py --init, LANE AX2 26 Sept 2026), not one of family_run.py's
registered families, so appended here by hand rather than by the tool. Gate: control (5811's real ciphertext, cut to
4612 v3's N, started from key_full with 20 pct of codes 1-120 randomly reassigned) recovers >= 0.90 of key_full's own
token reading, 3 seeds, before any target run. -->

| 26 Sept 2026 05:51 | homophonic (key-seeded, --init) | N=833 K=96 restarts=8 iters=40000 order=3 corpus=lettresdecatheri01cathuoft_djvu.txt.gz+lettresdecatheri02cathuoft_djvu.txt.gz+lettresindites00marg_djvu.txt.gz, init=key_full with 20% of 120 codes reassigned | 1-3 | 0.699 (0.643-0.731) | not run (CONTROL BELOW GATE) | - | no (gate 0.90) | AX2-4612 key-seeded anneal, control = 5811 cut to N=833, per-seed 0.731/0.643/0.723; a 150000-iter re-check of seed 1 alone reached 0.786, still below gate -- not under-converged at 40000, the design itself cannot repair a 20%-wrong key at this N/K |

<!-- Below: tools/key_repair.py (local per-code repair against fr16 order-5 total logp), LANE AX2
26 Sept 2026, AX2-4612S -- not one of family_run.py's registered families, appended by hand. Gate (a):
null control (key_full applied to its own correctly-keyed 5811-cut ciphertext) proposes <=2 changes.
Gate (b): known-answer control, 3 seeds (8 codes swapped in pairs + 2 hidden as bigrams) recovers
>=6/8 on average AND <=2 false changes on the other codes. -->

| 26 Sept 2026 06:56 | key_repair (local per-code, not a family_run.py family) | N=833 (5811 cut) margin=3.0 rounds=4 candidates=26 letters+NULL+60 bigrams+20 trigrams | 1 (null) | not applicable | 100/110 codes changed (152 change-events) | - | no (gate <=2 false positives) | AX2-4612S (a) null control on key_full/5811-cut |
| 26 Sept 2026 06:56 | key_repair (local per-code, not a family_run.py family) | N=833 (5811 cut) margin=3.0 rounds=4, 8 codes swapped in 4 pairs + 2 hidden as bigrams, seeded 46120+seed | 1-3 | 0.000 recovery (0.000-0.000); max 88 false changes | not run on 4612/5799 (CONTROL BELOW GATE) | - | no (gate >=0.75 recovery AND <=2 false changes) | AX2-4612S (b) known-answer control; root cause: total (not mean) logp of the decoded stream unconditionally rewards deleting a code to NULL, since every character's own logp is negative -- see NOTES.md AX2-4612S section |

<!-- Below: tools/key_repair.py, LANE AX2 26 Sept 2026, AX2-4612S2 -- re-run of AX2-4612S's controls
with the objective fixed (--objective excess, default; --no-null-below 121, default). Same gates as
AX2-4612S. -->

| 26 Sept 2026 07:35 | key_repair (local per-code, excess objective) | N=833 (5811 cut) margin=3.0 rounds=4, objective=excess, no_null_below=121, candidates=26 letters+NULL+60 bigrams+20 trigrams | 1 (null) | not applicable | 53/110 codes changed (64 change-events; 1 to NULL, 15 to a different letter, 48 to a bigram/trigram) | - | no (gate <=2 false positives) | AX2-4612S2 (a) null control on key_full/5811-cut, --objective excess (down from AX2-4612S's 100/110 under --objective total, still far above gate) |
| 26 Sept 2026 07:43 | key_repair (local per-code, excess objective) | N=833 (5811 cut) margin=3.0 rounds=4, objective=excess, no_null_below=121, 6 codes swapped in 3 pairs + 2 hidden as bigrams, seeded 46120+seed | 1-3 | 0.625 recovery (0.500-0.750); bigram-only recovery 0.500 (3/6); 53 false changes every seed | not run on 4612/5799 (CONTROL BELOW GATE) | - | no (gate >=0.75 recovery AND <=2 false changes) | AX2-4612S2 (b) known-answer control; recovery up sharply from AX2-4612S's 0.000 but false-change count unchanged (53, same ~codes as the null control regardless of which 8 are perturbed) -- root cause shifted from unconditional NULL-seeking to unconditional preference for inserting a top-corpus-frequency bigram/trigram (always above the mean mu, so summing more of them beats a correct single letter); see NOTES.md AX2-4612S2 section |

## Key conflict: code 172 (logged 26 Sept 2026 08:06 UTC, LANE AX2 orchestrator, CLAUDE.md rule 4)

Three H-grade period witnesses disagree on code 172; none is resolved by frequency.
| witness | sender -> recipient | date | 172 reads | source |
|---|---|---|---|---|
| WVO 4614 period decipherment | Lodewijk -> Willem | 4 Apr 1574 | le Conte Jean (1x, "mon frere [172] lequel") | NOTES AX-COMP, AX-REDERIV2 |
| WVO 7206 period decipherment (p8) | Willem -> brothers | 30 Jan 1574 | Lumbres (3x) | NOTES AX2-BLANKS, AX2-172 |
| WVO 5801 interlinear gloss + Groen IV CDXXIII | Willem -> Jan and Lodewijk | 28 May 1573 | le conte Louis de nassau | NOTES AX2-5801ADJ |
The direction-of-correspondence theory (AX2-172) failed on 5801. Consequence: 5797 p6_spot4 (Jan and Lodewijk -> Willem, 22 Oct 1573)
has no licensed value for 172; grade M wherever 172 is read outside its witness letter; AUDIT.md A4 withdrew the spot's class (V9-NA172-3).
key_full.tsv keeps its 4614 value with this conflict noted (axmerge4/proposal.tsv KEEP_NOTE rows).
