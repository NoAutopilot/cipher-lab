# DEB-SWARM-D log (disproof group: do c1 and c2 carry a readable language?)

Worker DEB-SWARM-D, 29 Sept 2026, box 03:08-06:08 UTC. score.py was not frozen when this group started (no FROZEN
line in swarm/README.md), so per the shared rules Phase 1 is done on this group's own hand-made controls
(`dcore.make`/`make_pair`), made at c1's and c2's own N, K, sign-count curve and line lengths, from the settled
drafts (punctuation-class boxes and the H43 clear spans dropped: c1 N 125 K 55, c2 N 643 K 122; X kept unless said).
The harness's sealed controls were never opened.

Every statistic is a z-score against the text's OWN within-line shuffles, so the sign-frequency curve alone
cannot make a signal; only order can. Language designs (letters or syllables in any homophonic key) keep order;
iid writing keeps none.

| time (UTC) | method | parameters | control result | real-text result | why it failed / what it says |
|---|---|---|---|---|---|
| 03:1x | order battery, first probe (`power_probe.py`) | c2 shape, 15 pct type noise, 8 per design | FR/EN/PT-HOMO: mi1 z +0.6..+2.4, bigram types>=2 z +1.4..+2.2, doubled z -2.2..-2.7; FR-SYLL mi1 +5.0, rep3 +19; NULL-IID all near 0 | c2: mi1 -1.03, mi2 -2.6, bg2 +1.31, rep3 +0.14, dbl -0.24 | c2 looks like the iid null on every statistic; a single statistic is weak for letter-homophonic designs, hence a summed score |
| 03:1x | test P, periodicity scan (`period.py`, `period.json`) | MI(sign, index mod p), p 2-16, whole-text shuffles; power: FR under 3/5/7 disjoint alphabets, c2 shape, 15 pct noise | POLY-3/5/7 text-order z median 55-56 (min 47.6); NULL-IID median 1.7 (max 2.6) | c2 best z 0.70 (p 15); c1 best z 3.06 (p 2, N 125, no power at that N) | periodic polyalphabetic with separate alphabets excluded for c2; alphabets that share one sign set are NOT tested |
| 03:1x | calibration (`calibrate.py`, `calib_*.jsonl`) | pairs (c1+c2 shapes, one key per pair), 8 designs x 40, noise 0.05/0.15/0.25, X-like null 0/0.13 | see summarize.py output; c2 score p5 of the four brief language designs at noise 0.15: +1.8..+9.5 (x 0), -0.5..+1.9 (x 0.13) | c2 score 0.66, pair 0.96, c1 0.96 | c2 below all but 0-15 pct of language controls at measured noise, at the NULL-IID median |

## Pre-registration of the blind control (written 03:15 UTC, before the blind set exists)

Frozen score (`dcore.score`): per text S = z(mi1) + z(bigram types seen twice or more) + z(repeated 3-grams) -
z(doubled adjacent signs); pair score = S(c1) + S(c2) + z(transfer c2->c1) + z(transfer c1->c2) (a bigram model
fitted on one text scored on the other, against shuffles of the fit text). Thresholds (`threshold.json`, chosen on
the calibration set only, noise 0.15 rows, NULL-IID vs FR-HOMO/EN-HOMO/PT-HOMO/FR-SYLL): c1 1.4, c2 3.5, pair 4.3;
score above = LANGUAGE, else NULL. Blind set: 100 pairs, design drawn at random from NULL-IID (prob 0.5) or one of the
four language designs, noise drawn from {0.10, 0.15, 0.20}, X-like null share from {0, 0.13}; fresh seeds; labels
written only to a sealed file outside the classifier's reach until every call is made. Bar for group D's Phase 1:
balanced accuracy >= 0.80 on the pair score and on c2 alone (the brief's "NULL told apart from the four language
controls, blind"). c1 alone is expected to fail (N 125) and is reported, not gated.
| 03:1x | own blind control (`blind.py`, `blind_result.json`; labels sealed in the session scratchpad until the calls were written) | 100 pairs, 50 NULL-IID / 50 of FR-HOMO, EN-HOMO, PT-HOMO, FR-SYLL, noise 0.10-0.20, X-like null 0 or 0.13 | pair score bal. acc 0.90 (language recall 0.88, null 0.92); c2 alone 0.90 (0.86 / 0.94); c1 alone 0.61 (no power at N 125, as pre-registered) | c1/c2 pair score 0.96 < 4.3 -> NULL; c2 0.66 < 3.5 -> NULL | bar (>= 0.80 on pair and c2) met on own controls |
| 03:2x | harness blind set B1-B5 (`harness_blind.py blind`, frozen pair threshold 4.3, 400 shuffles, reads only controls/B*.tsv) | score.py FROZEN ed4a3743 | pair scores B1 9.85, B2 0.84, B3 10.44, B4 13.66, B5 56.05 -> verdict committed in BLIND_VERDICT.tsv before --blind-check | -- | -- |
| 03:1x | score.py --blind-check on BLIND_VERDICT.tsv (verdict sha1 32df9850) | one check, first file | **5 of 5 correct: Phase 1 bar met** | -- | -- |
| 03:1x | same frozen test on the real texts in the harness reading (`harness_blind.py real`, `harness_real.json`; drops only `_`/MULTI + H43 clear spans, c1 132 / c2 658 signs) | 5 shuffle seeds x 400 | harness labelled controls: FR/EN/PT-HOMO-N15 8.8 / 13.1 / 13.5, FR-SYLL-N15 56.9, clean 17.5-86.2; NULL -0.5 | **pair score 0.39-0.91 -> NULL** (threshold 4.3) | the real texts sit with the harness NULL, eight to 60 points below every language control |
| 03:1x | escape routes, round 1 (`escape.py`, `escape.json`), 20 controls each at c2 shape, 15 pct noise | POLY-SHARED p 3/7/13 (Vigenere-like over one sign set), TRANS R 7/19/33 + MI-at-distance scan, NULLS 0.2/0.35/0.5 random nulls (+ X-like 0.13), WORDMIX (60 commonest words as signs, rest spelled), VERTICAL + vertical-neighbour MI | POLY-SHARED periodicity z 11.8-23.6 vs real 0.92 -> excluded; WORDMIX c2 score 6.2-17.1 vs real 0.72 -> excluded; NULLS 0.2 median 2.2 (15 pct <= real), 0.35 median 0.4 (60 pct <= real), 0.5 (85 pct) -> NOT excluded; MI-distance scan and vertical MI: no power (controls inside the null band) | -- | the distance/vertical tests are dead instruments at this N; replaced by test R (below) |
| 03:1x | escape routes, round 2 (`escape2.py`, `escape2.json`) | ANAGRAM (letters shuffled inside each word), RUNKEY (running-key Vigenere), AUTOKEY, NULLS 0.5/0.65, FR-HOMO reference | FR-HOMO ref median 8.4 (0 of 20 <= real); AUTOKEY median 4.4 (1 of 20 <= real); ANAGRAM median 1.3 (8 of 20); RUNKEY -0.7 (14 of 20); NULLS 0.5/0.65 (15, 11 of 20) | real c2 score 0.72 | NOT excluded: running key, word-internal anagram, random nulls at 35 pct or more of the signs |
| 03:2x | test S, space-sign gaps (`xgap.py`, `xgap.json`) | six commonest c2 signs; gap zero-share and dispersion vs 2,000 within-line shuffles; power: a space sign in FR at c2 shape | space-sign control p 0.000 on both statistics (10 of 10) | X: zero-gap share 0.141 (p_le 0.25), dispersion 3.69 (p_le 0.36); PCT, PCT-SLASH, CIRC-O likewise ordinary | X (and no other frequent sign) behaves like a word space; a Copiale-style spacing mark is excluded for the frequent signs |
| 03:2x | test R, re-reading (`reread.py`, `reread.json`) | c2 re-read down columns and by undoing columnar transposition of height R 2-60; frozen single-text score (60 shuffles) per reading, scan max | power: TRANS-7/19/33 pick their own R in 10-12 of 12, max median 7.9-8.8; VERTICAL picks columns 11 of 12, median 8.5; NULL-IID max 3.4-6.7 (12) | real c2 best R34 **8.18**, above 12 of 12 NULL-IID maxima; R34 at 1,000 shuffles: mi1 z 2.16, bg2 2.31, rep3 1.74, dbl -1.33 (`r34_detail.json`) | open: needs the target's own shuffle null for the scan max (`reread_null.py`, 200 scans) before it means anything |
| 03:30 | test R null from the target itself (`reread_null.py`, `rrnull_1-4.json`) | 200 scans of c2 shuffled within lines | shuffled-scan max: median 5.11, p95 6.89, p99 8.28, max 8.50 | real 8.18: **p = 0.010** (2 of 200 at or above) | one test family among about ten run here, so p 0.01 is weak; replication pre-registered below |

**Pre-registration (03:30 UTC, before running):** the R34 reading is logged as a lead only if BOTH hold: (a) the same
scan on c2 in the harness's reading (punctuation-class boxes kept, N 658; a real transposition would survive a
different box set only if those boxes are cipher signs, so either reading may carry it) or on c2 in this group's
reading with a fresh seed gives p <= 0.05 against its own 200-scan shuffle null; and (b) the R34 reading split into its
first and second halves (rows 1-17 and 18-34 of the grid, i.e. two separate stretches of the supposed plaintext)
scores above 0 on the frozen single-text score in BOTH halves at 1,000 shuffles. Otherwise it is logged as a
multiple-comparison tail, not a lead.
| 03:48 | pre-registered R34 replication (`r34_replicate.py`) | (a) fresh seed, 200 scans; (a) harness reading, 200 scans; (b) halves at 1,000 shuffles | -- | fresh: R34 7.52, p 0.03; harness reading: best R6 4.31, p 0.80; halves 5.55 / 4.23 | meets the pre-registration by its letter (fresh route + both halves); vanishes with the punctuation-class boxes kept; logged as a weak, fragile lead for the merge, nothing claimed (CASE.md) |
