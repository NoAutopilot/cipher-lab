# TXE2-GUNSHEET: gunther8246-p2 calibration sheet crossed against the p.1 Japikse alignment (read-free)

LANE TX-ENGINEER-2 incarnation 2, account 4, Opus; PREREG benchmark-tx/PREREG-txeng2-9.md GS1 (TX-RED F31 c); brief
.claude/briefs/runs/2026-10-09-account4-txe2-round9.md row TXE2-GUNSHEET; 9 Oct 2026 21:3x UTC by date -u. No reader, no
subagent, no host request, no pass read, no p.2 row read. Nothing corrected: a sheet correction is a baseline change for a
later pre-registered job.

Openings of eval truth: 0

## Method (the A1 / sheets-all cross, applied to this sheet)
`python3 benchmark-tx/txeng2/gunsheet/cross_gun.py` -> cross.tsv (173 rows, one per exemplar). Crop p1cal_LNN = committed
line p1L(NN+1) (RESULTS.md: "MS p.1 cipher lines p1L02-L11"); the script asserts each crop's label list equals the committed
signs of that line, in order (10/10 lines match). align_letter.tsv rows are zipped with ciphertext.tsv as the build does and
only `p1*` rows are kept. Key value = the C rows of key.tsv under the build's own normalisation (lower case, v/w -> u,
König -> q). Verdicts: OK (key value = the aligned print letter); MISLABELLED (keyed, different single letter); no-alignment
(the aligner gave no single-letter chunk); off-key (label not a C row: M-grade m, unkeyed signs, BLOT). The key folds v -> u
but the print text keeps v, so two 34 = v positions are notation, not error (CLAUDE.md rule 3, PX-BRODEC); they are listed
as `OK (u/v notation)` and counted with OK.

## Counts (173 exemplars, p1L02-p1L11)
| verdict | n |
|---|---|
| OK | 142 |
| OK (u/v notation) | 2 |
| **MISLABELLED** | **6** |
| no-alignment | 6 |
| off-key | 17 |

Keyed and aligned: 150; of these 144 agree (0.960), 6 do not. Without the u/v normalisation the count would read 8 MISLABELLED.

## Every exemplar that is not OK
| tile (crop.pos) | line.pos | label | key value | print letter | verdict |
|---|---|---|---|---|---|
| p1cal_L01.9 | p1L02.9 | 34 | u | - | no-alignment |
| p1cal_L01.12 | p1L02.12 | aaa | s | - | no-alignment |
| p1cal_L02.1 | p1L03.1 | v | - | e | off-key |
| p1cal_L02.14 | p1L03.14 | m | - (M: l) | l | off-key |
| p1cal_L03.6 | p1L04.6 | BLOT | - | - | off-key |
| p1cal_L03.7 | p1L04.7 | lx | - | - | off-key |
| p1cal_L03.8 | p1L04.8 | 87 | m | - | no-alignment |
| p1cal_L03.9 | p1L04.9 | cro | - | - | off-key |
| p1cal_L03.10 | p1L04.10 | Ib | o | - | no-alignment |
| p1cal_L03.11 | p1L04.11 | tb | - | - | off-key |
| p1cal_L03.14 | p1L04.14 | xy | - | b | off-key |
| **p1cal_L03.16** | p1L04.16 | d6 | d | c | **MISLABELLED** |
| p1cal_L04.6 | p1L05.6 | 34 | u | v | OK (u/v notation) |
| p1cal_L04.7 | p1L05.7 | od | - | o | off-key |
| p1cal_L04.9 | p1L05.9 | 44_ | - | - | off-key |
| p1cal_L04.12 | p1L05.12 | b | - | g | off-key |
| **p1cal_L05.14** | p1L06.14 | Ib | o | s | **MISLABELLED** |
| **p1cal_L06.14** | p1L07.14 | d6 | d | c | **MISLABELLED** |
| p1cal_L06.15 | p1L07.15 | xr_ | - | h | off-key |
| **p1cal_L06.17** | p1L07.17 | 34 | u | e | **MISLABELLED** |
| p1cal_L08.5 | p1L09.5 | v | - | e | off-key |
| p1cal_L08.14 | p1L09.14 | m | - (M: l) | l | off-key |
| **p1cal_L08.15** | p1L09.15 | xb | h | a | **MISLABELLED** |
| p1cal_L09.7 | p1L10.7 | 98 | - | - | off-key |
| p1cal_L09.8 | p1L10.8 | bbb | - | e | off-key |
| p1cal_L09.9 | p1L10.9 | ro | g | - | no-alignment |
| p1cal_L09.10 | p1L10.10 | th | d | - | no-alignment |
| p1cal_L09.11 | p1L10.11 | Ol | - | l | off-key |
| **p1cal_L09.14** | p1L10.14 | ps | n | f | **MISLABELLED** |
| p1cal_L10.6 | p1L11.6 | m | - (M: l) | l | off-key |
| p1cal_L10.12 | p1L11.12 | 34 | u | v | OK (u/v notation) |

By label, MISLABELLED: d6 -> c x2, Ib -> s x1, 34 -> e x1, xb -> a x1, ps -> f x1. Read-free context (from the pool RESULTS.md,
already public, no p.2 row opened here): d6 = c and Ib = s are two of the label-level patterns that build already flagged as
`align-conflict` on p.2, so on this sheet they look like the same lumped-shape or key-gap question, not a reader's slip; which
it is needs the image and is not settled here. Off-key `m` (M-grade l) and `v` sit on print l and e three and two times.

## Inputs and outputs (commit, sha256)
| file | commit | sha256 |
|---|---|---|
| benchmark-tx/txpool/gunther8246-p2/sheet/calibration.tsv | 624d37662 | 01abf56bebd3c7809b16ed3a0b8e021392b283eee188623cb5bf552590cd54b9 |
| benchmark-tx/txpool/gunther8246-p2/align_letter.tsv (p.1 rows only) | 624d37662 | 5a255178ff25dcef7a7c0d26953f194101e2cd53f7c0eedf027a729a4dc6873a |
| ciphers/gunther-van-schwarzburg-1561/key.tsv | 624d37662 | 36e42e9c261661423cff435da93e9d6b316d34f7aeb1d3980ad8537b3381e82d |
| ciphers/gunther-van-schwarzburg-1561/ciphertext.tsv | 624d37662 | 208098452f84e97f5af1de165b6e07e872c8bb6096b0e8cb2b87305aafade50c |
| benchmark-tx/txeng2/gunsheet/cross_gun.py | this commit | 702009d14068c0713e99bc24a288c3ce6dea02f2ecfe85007028bc33b7b5f915 |
| benchmark-tx/txeng2/gunsheet/cross.tsv | this commit | 2d27817c7a0aeafedc479ff125405ab12ac51e72357feca8f674dd77b2778093 |

## Next step (suggestion, not run)
Whether to drop or relabel the 6 MISLABELLED tiles (and whether the d6/Ib split is a lumped shape) is a sheet correction,
B-class: a later pre-registered job with the image in hand. Requests 0; subagent calls 0.
