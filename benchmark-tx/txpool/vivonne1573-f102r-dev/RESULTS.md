# vivonne1573-f102r-dev: dev item build and baseline (TXP-VIV102, PREREG-txeng2-13 DV1)

Worker TXP-VIV102 (account 4), for LANE TX-ENGINEER-2 incarnation 3. 9 Oct 2026, 22:32-22:4x UTC by `date -u`. Zero network.
Split **dev**: the Saint-Gouard clerk hand of 1573 is confirm2's unseen hand (f.103r), so this leaf can never be eval or
confirm (PREREG-txeng2-0 section 0b).

## Method

- `benchmark-tx/build_vivonne_f102r.py` = a copy of `build_vivonne_confirm2.py` with ITEM (`vivonne1573-f102r-dev`), the
  stream index (f.102r stretch `i0..i1` of the same f.102r+f.102v+f.103r stream instead of f.103r..end; the
  align-uncertain neighbour window and the control segment bounded by `i1`), line ids `f102r_L??`, the output dir and the
  input passes (`tx/f102r_rec.tsv`, `f102r_passA.tsv`, `f102r_passB.tsv`) changed. Key forcing (published Tomokiyo C rows),
  exclusions, oo handling and the flag rule (align-conflict, clerk-split) unchanged. The TXV-VIV override hook stays but
  reads `vivonne1573-f102r-dev.flags.tsv`, which does not exist (no verifier pass: dev).
- `--check`: `ok: truth, sha256 and outputs current (04bb775f...)`.
- Build counts: positions 1848, scored 1008, excluded 840 (align-uncertain 347, unaligned 200, letter-off-key 102,
  key-M y 98 / S 13 / b 6 / A 2, off-key 72). Flags on scored: align-conflict 360, clerk-split 384, any 605, none 403.
- Control (the build's own): f.102r match share, published key 0.552 vs 200 value-shuffled keys mean 0.438, p95 0.504,
  max 0.549, rank 1 of 201. **The margin over the shuffled maximum is 0.003** (confirm2: 0.605 vs max 0.557): the truth on
  this leaf is noisier than confirm2's; read the flagged-excluded figures and paired counts, not the as-measured level.
- Baseline: `tools/tx_bench.py --item vivonne1573-f102r-dev --exclude-flagged <output>`, one call per output (the tool
  treats several positional outputs as pieces of ONE pipeline: a first call with all three files together summed them,
  3.914 = 3945/1008 with 3622 inserted, a mis-invocation, not a figure; logged here, no other look). Plus one
  `--paired passA` call for passB.

## Commits and sha256

| file | sha256 |
|---|---|
| benchmark-tx/build_vivonne_f102r.py (3003e324a) | 3ddc0c31c333a8739c15efeb0225ccd2f9c961f4ebe01536bcfc08cdbe231d67 |
| benchmark-tx/vivonne1573-f102r-dev.truth.tsv (3003e324a) | 04bb775fab2ceb74a9093508ecefdea56d0104f7e0a5104f409580dd33f19527 |
| benchmark-tx/outputs/vivonne1573-f102r-dev/committed.tsv (3003e324a) | 47604e4cba994cca05d99fe07d8d421e335092fa7b2d100bc75dde98a0abe2db |
| benchmark-tx/outputs/vivonne1573-f102r-dev/passA.tsv (3003e324a) | f02463fb3963a6aa0331413ff203273ff42425238f7d1b6b3b691ef7f8b86e77 |
| benchmark-tx/outputs/vivonne1573-f102r-dev/passB.tsv (3003e324a) | 8e16cc3c9aedebf78d494b53c0d7ecc41e44dd4f04a1ff598d89867caa635a34 |
| ciphers/fr16104-vivonne-spain-1572/tx/f102r_rec.tsv (f0f817f8e, input) | 2cbc1f6551f0f4396dc01ae8fd505ce5cc6e5b0b35aef638a3db718d461ea22c |
| ciphers/fr16104-vivonne-spain-1572/tx/f102r_passA.tsv (f0f817f8e, input) | 526759ea7ec56f8a92010fcb641b7887b786d1cf51f91d5ceb8fc8a15dda3621 |
| ciphers/fr16104-vivonne-spain-1572/tx/f102r_passB.tsv (input) | 3cd1b6363d2fcad2256dc444e4157573dbe6e9ed847cce6b7735a792e906823f |
| benchmark-tx/build_vivonne_confirm2.py (f0f817f8e, the recipe copied) | df585f0e74ead75aac2083df7f24627d2963936dcd6d4f5cc2e1448094266a76 |

BENCHMARK-TX.tsv row appended in 3003e324a.

## Figures (err_true, 1008 scored; flagged excluded on 403)

| output | as measured | 95% | flagged excluded | deleted |
|---|---|---|---|---|
| committed (reconciled reference; home advantage, 0 flagged-excluded by construction) | 0.327 (330/1008) | 0.299-0.357 | 0.000 (0/403) | 0 |
| passA (blind Sonnet, N5-VIVK) | 0.330 (333/1008) | 0.302-0.360 | 0.007 (3/403) | 9 |
| passB (blind Sonnet, N5-VIVK) | 0.353 (356/1008) | 0.324-0.383 | 0.042 (17/403) | 15 |

Paired passB vs passA: fixed 5, broken 28, sign test p = 0.0001.
Top confusions (truth value <- read, committed): d<-d x10, s<-: x8, s<-m x8, a<-d x7, e<-d x6, u<-tz x6, r<-z x6, n<-tz x5.

## Read-free label counts in committed.tsv (column sign, 1848 rows)

':' 84, 'S' 16, 's' 112, '3' 19, 'z' 94.

Openings of eval truth: 0. (Nothing under outputs/vivonne1573-f103r-confirm2/, the f.103r truth, any c106_f103r crop,
txeng2/s2read/ or s2score/ was opened; the build reads tx/f103r_rec.tsv only as part of the aligned stream, as the recipe does.)

Verdict: measured: dev item built (1008 scored, 403 unflagged, truth sha256 04bb775f), baseline committed 0.327 / 0.000, passA 0.330 / 0.007, passB 0.353 / 0.042 (as measured / flagged excluded); control margin thin (0.552 vs shuffled max 0.549).
