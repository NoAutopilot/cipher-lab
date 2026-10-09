# PREREG-MQS-LOOKALIKE-SLIPS (9 Oct 2026, LANE MQS-2, account 4)

Written and pushed before any control is scored (CLAUDE.md rule 3). Tool: `tools/decode_key.py --lookalike A~B[,C~D...]`
(new option, added alongside --try / --special-scan). Source of the idea: Lasry, Biermann and Tomokiyo 2023
(Cryptologia 47:2) pp.123-124 (Fig. 11), p.136 n.95, App. B pp.198-200 (enciphering errors; a sign written for its
look-alike twin); research/MARY-STUART-TALK-2026-10-09.tsv row M25.

## Statistic

For a declared look-alike pair A~B, every occurrence of A is scored as if it were B, and every occurrence of B as if
it were A, ONE position at a time (the other occurrences keep their value): gain = window score with that one token
read as its twin's value minus the window score with its own value (the `--try` window score: fr16 character model,
+-8 tokens). An occurrence is flagged as a candidate slip when gain >= 3.0 bits (T, fixed here; the `--try` breakage
threshold). A report: a flag is a candidate for an image check, never a key or reading edit.

## Known answer (same design, length and language as the intended use)

Intended use: French and Spanish letter ciphers read with a key (dupuy468-anhalt, rah-morillo-1817 carry recorded
encipherer slips). Control material: the Danzay stream (tools/tests/decode_configs/fr20140-danzay-1557.json, the
committed graded reading, real 1557 French, 2 jobs), fr16 model. 10 seeds. Per seed: draw a pair (A, B) of distinct
H-graded codes whose values are single, different letters, each with n >= 5; plant k = 6 slips by rewriting 6 random
occurrences of A as B (in memory; nothing written). Run the scan with the pair A~B.

- **R (recall)**: planted positions flagged / 6, pooled over seeds. Gate: R >= 0.50 (>= 30/60).
- **F (false flags)**: unplanted occurrences of A or B flagged / their count, pooled. Gate: F <= 0.10.
- **N (shuffled-pair null)**: the same planted stream, scanned with the pair B~C, C a random other H single-letter
  code (value not A's, not B's). Flag rate at the 6 planted positions (now coded B), pooled. Gate: R - N >= 0.30.
  Why N can differ from R on this statistic: it examines exactly the same positions with the same threshold; only the
  partner's value changes. A planted spot is a wrong letter in real prose, so many substitutes may improve it; if the
  scan flags because "any change helps here", N rises toward R and the gate fails. A null that cannot vary
  (e.g. shuffling token order, which does not change which positions are planted) is not used.
- **D (must NOT flag)**: unmodified Danzay stream, 10 random pairs as above: flags / occurrences examined <= 0.10.

Ceiling check: if R = 1.00 and N = 0, the result is reported at k = 6 only; the statistic is per position, so k does
not change R's expectation; a k = 2 row is reported (not gated) to show the per-seed spread with fewer slips.

## Outcome rule

All four gates met: shelf grade `controlled-only` for French letter ciphers of the Danzay design (fr16); Spanish and
nomenclator word signs untested (no grade there). Any miss: the option ships `weak` with both numbers, is not
re-briefed, and nothing is run on a target from it. No target's key, reading, status or AUDIT.md changes in this job.

## Results (appended after the run)

Disclosure: before the controls ran, the offline test (tools/tests/test_decode_key_lookalike.py, seed 1, one planted
slip on the most frequent letter code) was run once to check the code path; no threshold, statistic or gate was
changed after it or after the controls. Control seeds 1000-1009; rows in tools/tests/MQS-LOOKALIKE-SLIPS-controls.tsv
(k = 6) and MQS-LOOKALIKE-SLIPS-controls-k2.tsv (k = 2, reported).

| control | result | gate | verdict |
|---|---|---|---|
| R planted-slip recall (Danzay, k=6, pair A~B) | 45/60 = 0.750 (k=2: 15/20 = 0.750) | >= 0.50 | PASS |
| N shuffled-pair null at the planted positions (B~C) | 24/60 = 0.400; R - N = 0.350 (k=2: 9/20, R - N = 0.300) | R - N >= 0.30 | PASS (narrow; k=2 exactly at the gate) |
| F false flags, unplanted occurrences of A/B | 40/370 = 0.108 | <= 0.10 | MISS |
| D unmodified stream, same 10 pairs | 45/430 = 0.105 | <= 0.10 | MISS |

Outcome (rule above): **weak**. The scan finds three in four planted twin slips, but at T = 3 bits it also flags about
one in ten ordinary occurrences of the pair, and the shuffled-pair null shows that 40% of planted spots are "improved"
by an arbitrary other letter -- much of the recall is "a wrong letter in prose reads better changed", not the twin.
On a 600-token letter with a frequent pair, expect several false candidates per true slip. Not re-briefed; nothing run
on a target. Untested: Spanish, word signs, real (unplanted) slips such as those recorded on dupuy468-anhalt.
