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
| 03:30 | order battery, first probe (`power_probe.py`) | c2 shape, 15 pct type noise, 8 per design | FR/EN/PT-HOMO: mi1 z +0.6..+2.4, bigram types>=2 z +1.4..+2.2, doubled z -2.2..-2.7; FR-SYLL mi1 +5.0, rep3 +19; NULL-IID all near 0 | c2: mi1 -1.03, mi2 -2.6, bg2 +1.31, rep3 +0.14, dbl -0.24 | c2 looks like the iid null on every statistic; a single statistic is weak for letter-homophonic designs, hence a summed score |
| 03:40 | test P, periodicity scan (`period.py`, `period.json`) | MI(sign, index mod p), p 2-16, whole-text shuffles; power: FR under 3/5/7 disjoint alphabets, c2 shape, 15 pct noise | POLY-3/5/7 text-order z median 55-56 (min 47.6); NULL-IID median 1.7 (max 2.6) | c2 best z 0.70 (p 15); c1 best z 3.06 (p 2, N 125, no power at that N) | periodic polyalphabetic with separate alphabets excluded for c2; alphabets that share one sign set are NOT tested |
| 03:50 | calibration (`calibrate.py`, `calib_*.jsonl`) | pairs (c1+c2 shapes, one key per pair), 8 designs x 40, noise 0.05/0.15/0.25, X-like null 0/0.13 | see summarize.py output; c2 score p5 of the four brief language designs at noise 0.15: +1.8..+9.5 (x 0), -0.5..+1.9 (x 0.13) | c2 score 0.66, pair 0.96, c1 0.96 | c2 below all but 0-15 pct of language controls at measured noise, at the NULL-IID median |

## Pre-registration of the blind control (written 03:5x UTC, before the blind set exists)

Frozen score (`dcore.score`): per text S = z(mi1) + z(bigram types seen twice or more) + z(repeated 3-grams) -
z(doubled adjacent signs); pair score = S(c1) + S(c2) + z(transfer c2->c1) + z(transfer c1->c2) (a bigram model
fitted on one text scored on the other, against shuffles of the fit text). Thresholds (`threshold.json`, chosen on
the calibration set only, noise 0.15 rows, NULL-IID vs FR-HOMO/EN-HOMO/PT-HOMO/FR-SYLL): c1 1.4, c2 3.5, pair 4.3;
score above = LANGUAGE, else NULL. Blind set: 100 pairs, design drawn at random from NULL-IID (prob 0.5) or one of the
four language designs, noise drawn from {0.10, 0.15, 0.20}, X-like null share from {0, 0.13}; fresh seeds; labels
written only to a sealed file outside the classifier's reach until every call is made. Bar for group D's Phase 1:
balanced accuracy >= 0.80 on the pair score and on c2 alone (the brief's "NULL told apart from the four language
controls, blind"). c1 alone is expected to fail (N 125) and is reported, not gated.
