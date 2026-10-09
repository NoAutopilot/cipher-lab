# FLOOR-AUDIT-803: the skipped-letter test over all 803 scored no.87 positions (TXE-T2, 9 Oct 2026)

LANE TX-ENGINEER round 3, account 4, Opus 5.5. Brief `.claude/briefs/runs/2026-10-09-account4-txe-t2.md`. Read-free: 0 vision
calls, 0 hosts. No truth file, BENCHMARK-TX.tsv or other instrument's file was edited; the excluded-doubtful scores below
come from a scratch copy of the truth. An auditor's proposal for a verifier (ASKS row 157), not a change to the benchmark.

Files: `no87_sites_803.tsv` (every non-1:1 site), `no87_skip_audit_803.tsv` (306 scored positions near a site, class and
reason each), `truth_flags_proposed.tsv` (the flag column, still 13 rows).

## Result in one line

**The 803-position test adds no doubtful position to TXE-T's 13** (alignment 8, clerk 4, key 1 -- 13/803 = 1.6%). Every
truth artifact the skip sites produce is already on the floor (wrong in all six passes), because a doubtful truth is wrong
for every reader that reads the hand faithfully. L: err_true 0.045 (36/803) as measured, 0.029 (23/790) with the 13 excluded.

## Sites (step 1)

Rebuilt by walking each `align_real.tsv` row's chunk through the clerk span's letters (`pairs.tsv`, folded as
`tools/interlinear_align.py plain_letters`); reproduces TXE-T's 43 skip sites and 81 skipped letters exactly.

| site kind | n |
|---|---|
| skip (clerk letters the aligner jumped) | 43 (81 letters) |
| multi-letter chunk on one sign (1:N; word signs and the per/che, gonottiet, atholici, quest chunks) | 29 |
| null/insertion (sign with no clerk letter, the 2:1 case) | 10 |
| excluded:off-sheet | 21 |
| excluded:span-uncertain (f178r L01 1-8) | 6 |
| excluded:key-split-T88 | 4 |
| excluded:no-key-sign-for-q | 1 |
| **total** | **114 sites at 108 distinct positions** |

Scored positions within two positions (same leaf) of any site: **306 of 803**.

## Classes (step 2)

Decision rule (TXE-T's, made explicit): if the committed sign is in the truth set, the clerk letter agrees with the key at
that sign, so any other chunking of the skipped letters would put a letter there that the key contradicts -- not equally
plausible: clean (key-corroborated). Only the 22 near-site positions where the committed sign is outside the truth set need
the alternative-chunking test.

| class | n of 306 | source |
|---|---|---|
| clean, key-corroborated | 284 | TXE-T2 |
| clean, conflict but truth stands (TXE-T reader-wrong) | 4 | TXE-T: f178r L02.19, L03.34; f178v L05.1; f179r L02.8 |
| clean, conflict but truth stands (new) | 8 | TXE-T2, below |
| alignment-doubtful | 8 | TXE-T, unchanged |
| clerk-doubtful | 2 | TXE-T, unchanged (f178v L05.9, L09.4) |
| key-doubtful | 0 | -- |

TXE-T's other 3 flags (key f178v L02.8; clerk f178v L02.12, L11.17) are not within 2 of a site and stand unchanged.

The 8 new conflict positions, each checked against an alternative chunking; in every one the skip or chunk cannot move a
letter onto the sign (a doubled letter skipped, or a 1:1 run that anchors it), and at least one pass reads a truth-set sign,
so the truth is reachable and the miss is the reader's:

| position | clerk | committed | reads A B C L E F | why clean |
|---|---|---|---|---|
| f178r L03.10 | l ("solo") | T65 (t) | T65 x4, T51, T95 | skip "gnolama" 2 back, s o _ o anchored; E F read l-signs |
| f178v L10.1 | t ("parte") | T92 (s) | T92 x4, T53, T53 | 1:1 p a r t e; T92/T53 look-alike |
| f178v L10.31 | c ("cio che") | T98 (s) | T98 x4, T18, T36 | c\|i\|oche or c\|io\|che both keep c here; F reads c |
| f178v L13.1 | c ("assicurare") | T27 (t) | T27, T26, T27, T27, T36, T36 | skip is the doubled s |
| f178v L14.22 | l ("castello") | T64 (h) | T64 x4, T13, T13 | skip is the doubled l |
| f178v L19.6 | d | T98 (s) | T98, T18, T98, T98, T18, T18 | d 1:1 after the per chunk |
| f178v L19.24 | d | T98 (s) | same split | chunk "re" 2 ahead, d 1:1 |
| f178v L20.17 | l ("alle") | T64 (h) | T64 x4, T13, T13 | skip is the doubled l |

Two patterns a verifier or the sorter should see, neither a flag by the brief's rule (readers split, not unanimous):
- **T98 for d**, 7 times in the letter (key_real 98: s 10/18, d 7): every one is split T98 / T18 across passes (B E F mostly
  T18), and B reads T98 for a T18 ref eight times elsewhere -- a T98/T18 look-alike pair in the readers, not a key conflict
  on present evidence. Only 2 of the 7 (L19.6, L19.24) are near a site; the rest are outside this test's scope.
- **T64 for l**, both times at a doubled "ll" (L14.22, L20.17), C/L read T64, E F read T13 (l): either a look-alike or an
  "ll" use of T64; an image check decides, not the tables.

## Scores (step 3; `tools/tx_bench.py --item birago1572-no87`, then `--bench` on a scratch BENCHMARK-TX copy pointing at a
truth copy with the 13 rows set `excluded:truth-doubtful`)

| pass | as measured | 13 doubtful excluded |
|---|---|---|
| L (labels) | 0.045 (36/803) 95% 0.033-0.061 | 0.029 (23/790) 95% 0.019-0.043 |
| A | 0.069 (55/803) 95% 0.053-0.088 | 0.053 (42/790) 95% 0.040-0.071 |
| B | 0.100 (80/803) 95% 0.081-0.122 | 0.085 (67/790) 95% 0.067-0.106 |
| C (committed) | 0.053 (43/803) 95% 0.040-0.071 | 0.038 (30/790) 95% 0.027-0.054 |
| D (look-alike, f178r+f179r) | 0.049 (8/164) | 0.043 (7/163) |
| E (sheet) | 0.077 (62/803) 95% 0.061-0.098 | 0.062 (49/790) 95% 0.047-0.081 |
| F (fable) | 0.093 (75/803) 95% 0.075-0.116 | 0.079 (62/790) 95% 0.062-0.099 |
| dev_tune outputs (343 scored, 7 doubtful in dev) | | |
| J pair | 0.041 (14/343) | 0.021 (7/336) |
| S adj opus | 0.044 (15/343) | 0.024 (8/336) |
| P hints | 0.047 (16/343) | 0.027 (9/336) |
| R stab (and stabshuf2-5) | 0.050 (17/343) | 0.030 (10/336) |
| S adj fable | 0.050 (17/343) | 0.030 (10/336) |
| R stabshuf1 | 0.052 (18/343) | 0.033 (11/336) |
| L lattice lam4, M conf, M confshuf, V s1, V shift | 0.055 (19/343) | 0.036 (12/336) |
| U feature | 0.061 (21/343) | 0.042 (14/336) |
| K2 sr4 | 0.067 (23/343) | 0.048 (16/336) |
| G2 library r1 / base / r2 | 0.070 / 0.073 / 0.076 | 0.051 / 0.054 / 0.057 |
| V s0 | 0.070 (24/343) | 0.051 (17/336) |
| G compare m1b H_all / H_top1 / M lam1 / M confshuf lam1 | 0.085 (29/343) | 0.066 (22/336) |
| G compare m1b any_top1 / L lattice lam1 | 0.087 (30/343) | 0.069 (23/336) |
| G compare | 0.093 (32/343) | 0.074 (25/336) |
| T ordered / T shuffled (dev, 115) | 0.139 / 0.113 | 0.124 (14/113) / 0.097 (11/113) |

Every full-coverage pass loses exactly 13 errors and every dev_tune pass exactly 7 (2 for the T split): every pass gets every
doubtful position wrong, so excluding them shifts all instruments by the same count and **does not change any paired
comparison** (fixed/broken counts are unaffected); it moves absolute err_true down by about 1.6 points on the full item and
2 points on dev, which matters for TRANSCRIPTION.md's <=5% target: on the full item L (0.045) is under it either way and C
(0.053) only with the exclusion; on dev, J, S-opus and P are under 0.05 as measured, and R, S-fable, R stabshuf1, the 0.055
group, U and K2 cross under only with the exclusion.

## Caveats
- One auditor's judgement on tables (rule 3/7); a verifier session decides (ASKS row 157).
- The test covers positions within 2 of a site. The 14 conflict positions far from any site are TXE-T's 3 flags plus 11
  read-split or floor reader-wrong positions (e.g. the T98-for-d run, f178r L01.27-28, f178v L11.29 T60/T86); none was
  reclassified here.
- Positions where the committed sign is a homophone the readers swap are invisible to this value-level truth (build note).
