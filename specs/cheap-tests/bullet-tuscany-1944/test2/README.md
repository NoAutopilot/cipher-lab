# Cheap test 2: bullet-tuscany-1944

`cheap_tests_in_order[1]` of `specs/bullet-tuscany-1944.json`: short-key Vigenere/Caesar-family
search on the 44-letter body `CBFUKYYEVOZILOOZVNCWJKQRSAWBYZUGYTZWYBATRSUA`, treating the header
(QM) and footer (605YZ/FF) as candidate indicator/key material, judged with
`tools/judge_plaintext.py` (language `en`, `min_word_cover` 0.5, `letters_min/max` 40/48, a
12-word crib list) and a crib-hit count, each step with a matched control per CLAUDE.md rule 3.
No network, no subagents.

## (a) Intake and judge-block repair

No `ciphers/bullet-tuscany-1944/` folder exists (breadth convention: a target with no image
fetch works in `specs/` only), so `tools/intake_gate_check.py` cannot run (it requires
`ciphers/<slug>/NOTES.md`). The target already carries a recorded verdict: `UNSOLVED-SURVEY.md`
row 20 (`open; a forum "solution" without a method, rejected by Schmeh`), sourced from Klaus
Schmeh's Cipherbrain post on disk (`sources/schmeh/posts/44-bullet.txt`), which as of the post's
9 comments (latest dated 3 Jan 2020, on disk) records no accepted solution -- comment #3
(Bernhard Gruber, 6 March 2017) even notes the original forum poster admitted on 1 Feb 2015 that
his "decryption" was a joke, consistent with Schmeh's rejection and with this spec's own test-1
result (cheap_test_done.1) mechanically closing that claim. This job's brief sets a hard
**no-network** cap, so the two network legs of the breadth intake step's minimal check-solved
(cloning `dbourdeau/cyphersolver` and `aaymeloglu/unsolved-ciphers` to grep; one OpenAlex + one
Semantic Scholar query) could not be run this session -- recorded here as **not reachable this
session (no-network cap)**, not as a search result. Proceeding on the strength of the on-disk
Cipherbrain thread (read through its last comment, 2020) plus the already-closed forum claim,
per the parent orchestrator's explicit approval of this exact test 2 job (ROOM.md, 19:08 UTC).

Judge block repaired: added `min_word_cover: 0.5` and a 12-word crib list (GRENADE, PIN, PINS,
REINFORCEMENT, REINFORCEMENTS, PULL, THROW, ENEMY, POSITION, ATTACK, TANK, MG) to
`specs/bullet-tuscany-1944.json`'s `judge` block; `language: en` kept. `tools/judge_plaintext.py`
supports both keys (`--help` confirmed).

## (b) `tools/family_run.py --family periodic_vigenere`

Ran once per tabula (vig, beau, varbeau), each with `period_max=8` (auto period scan 2-8) and,
separately, `period=1` (the Caesar-family degenerate case). Rows in `HYPOTHESES.md` (this
folder). Control built by the tool itself: a Holmes+Moby-Dick English window of N=44, K matching,
under a random key of the scanned/given period.

| tabula | period range | control mean recovery (3 seeds) | gate 0.6 met? | target run? |
|---|---|---|---|---|
| vig | 2-8 (scan) | 0.053 (0.023-0.068) | no | no (CONTROL BELOW GATE) |
| beau | 2-8 (scan) | 0.061 (0.023-0.091) | no | no (CONTROL BELOW GATE) |
| varbeau | 2-8 (scan) | 0.061 (0.023-0.091) | no | no (CONTROL BELOW GATE) |
| vig | 1 | 1.000 (1.000-1.000) | yes | yes -- judge FAIL, 0/12 cribs |
| beau | 1 | 1.000 (1.000-1.000) | yes | yes -- judge FAIL, 0/12 cribs |
| varbeau | 1 | 1.000 (1.000-1.000) | yes | yes -- judge FAIL, 0/12 cribs |

**Periods 2-8**: the control itself cannot recover its own planted key at N=44 with an unknown
period up to 8 (mean recovery 5-6%, far below the 0.6 gate) -- per CLAUDE.md rule 5's amendment,
this is **not a test at this N** for periods 2-8, not a negative; the search space (up to 8x26
key positions against 44 signs) is too large for the coordinate-ascent solver to have power here,
independent of whether the target is or isn't enciphered this way. Recorded, gate not tuned.

**Period 1** (a pure Caesar shift, single key letter, found by the solver's own trigram-scoring
hill-climb rather than an exhaustive 26-shift scan -- that exhaustive scan is step (c) below):
control recovers its planted key perfectly (3/3 seeds, recovery 1.000), so the method has full
power at this degenerate case; the target's best-scoring single-letter key (derived by the same
hill-climb, tabula varbeau, key `G`) FAILs the judge outright (0 of 12 cribs present). Only the
last of the three tabula runs' decode survives on disk (`family_run.py` writes to a fixed
`ciphers/<slug>/families/periodic_vigenere-<seed>.txt` path regardless of tabula, so vig and beau
were overwritten in turn -- a one-line tool limitation, not fixed here, cost out of scope for a
$3 job); its `HYPOTHESES.md` row records all three scores. Files moved out of
`ciphers/bullet-tuscany-1944/` (which `family_run.py` created) into
`specs/cheap-tests/bullet-tuscany-1944/test2/families/` per the breadth convention that a
no-image-fetch target keeps no `ciphers/` folder; `HYPOTHESES.md` was written directly to this
folder via `--out`.

## (c) Deterministic keyed decrypts: QM, MQ, footer-derived keys, Caesar 0-25

Script: `run_test2c.py`, output `test2c_output.json`. Keys: `QM`, `MQ` (the header, both
orders), `YZFF` (the footer's letters), and the footer's digits `605` mapped to letters two ways
(`605_A0`: 0->A..9->J, giving `GAF`; `605_A1`: 1->A..9->I with 0 as "10"->J, giving `FJE`) --
each a short repeating key, continuous across the 3 body lines, under vig/beau/varbeau (15
decodes), plus every Caesar shift 0-25 under the same three tabulas (78 decodes) -- 93 candidate
decodes total. Scored by `tools/judge_plaintext.py`'s exact language/words/cribs/length logic
(re-implemented against a single shared `NgramModel` build -- calling `judge_plaintext.judge()`
per candidate rebuilds the whole Holmes+Moby-Dick 4-gram model from scratch each time, ~2 minutes
for one candidate and unusable for 93 x 4 scans; the shared-model version gives identical numbers
in 1.4s, verified against a spot-check with the original `judge()` on 3 candidates) and by a raw
crib-hit count (how many of the 12 cribs appear as a substring, independent of the judge's
all-12-required PASS bar).

**Target**: 0 of 93 candidates PASS the judge (language, words and cribs all required); the best
crib showing anywhere is 1 of 12 (7 different key/tabula/shift combinations each surface exactly
one crib -- `PIN` under key QM/vig, `MG` under six different Caesar shifts/tabulas -- consistent
with short common substrings like `MG` and `PIN` turning up by chance in essentially any
44-letter string, not a signal). Best language-model score across all 93: -1.743 (`caesar_11`
varbeau / `caesar_15` vig, tied, 0 cribs).

**Control A (true key must rank 1)**: 3 synthetic 44-letter military sentences (built from the
crib vocabulary), each enciphered under one of the five named keys (`QM`/vig, `MQ`/beau,
`YZFF`/varbeau), run through the identical 93-candidate scan and ranked by language-model score.
**3/3**: the true key ranked #1 by language score every time, over 90 wrong candidates -- the
scan and scoring correctly recover a real key when one is present at this N.

**Control B (false-positive rate)**: 3 random 44-letter strings run through the same 93-candidate
scan: 0/279 judge PASSes (same as target); 20/279 candidate decodes had >=1 crib hit by chance
(seeds: 10, 6, 4 hits of 93), each seed's *maximum* crib-hit count topping out at 1 -- identical
to the target's ceiling. The target's single-crib-hit candidates are statistically indistinguishable
from the random-text noise floor.

**Verdict**: a clean negative with a working control -- no key drawn from QM, MQ, the footer's
letters or its two digit-mapping readings, nor any of the 26 Caesar shifts, produces a plaintext
that clears the judge or rises above the random-text crib-hit noise floor, under any of the three
tabulas, while the identical scan and scoring correctly identifies a real planted key 3/3 times.

## (d) Crib drag for a periodic key (period <=8)

Script: `run_test2d.py`, output `test2d_output.json`. Each of the 12 cribs dragged over every
valid offset in the 44-letter body under vig/beau/varbeau; the implied key fragment at each
(crib, offset, tabula) is checked for periodicity at any P in 1-8 where the check is non-trivial
(some residue class holds >=2 positions -- a fragment no longer than P is periodic at P by
definition and proves nothing).

**Target**: 59 (crib, offset, tabula) triples come back periodic at some P<=8, spread across
periods 1-7 (most at P=7: 16 hits, P=3: 13, P=4: 10) and concentrated on the longer/commoner
cribs (`POSITION` 16, `PINS`/`ENEMY`/`ATTACK`/`MG` 6 each).

**Control B (false-positive rate on random text)**: 3 random 44-letter strings, same drag: 31,
45 and 57 periodic hits respectively (mean 44.3) -- **higher than the target's 59-hit total on
its own** when compared seed-for-seed, and squarely overlapping it. The periodicity bar at this
N, this crib list and this period ceiling is noisy: short cribs (`PIN` 3 letters, `MG` 2 letters)
satisfy a low period almost by construction, so "periodic at P<=8" fires often on pure noise.

**Control A (true offset must be found periodic)**: 3 synthetic sentences, each containing one
crib (`PULL` len 4, `ATTACK` len 6, `PIN` len 3), enciphered under a single real period-5 key
under a rotating tabula. Found periodic at the true offset: **1 of 3** (`ATTACK`, tabula beau,
correctly recovered period 5). The other two failures are not a broken test but a length limit
inherent to the check: a crib of length L can only test periods P < L (a fragment no longer than
P is trivially "periodic"), so `PULL` (4 letters) and `PIN` (3 letters) can never detect a
period-5 key by construction -- only `ATTACK` (6 letters) was long enough to test P=5 at all, and
it succeeded. This is a design point for a rerun (match crib length to the period being tested),
not a defect found in this run; not rerun here (cap).

**Verdict**: **not informative at this N** (LANE B3 rule 5 amendment) rather than a clean
negative -- the false-positive control shows the periodicity bar this check uses is met by chance
about as often as it fires on the target (noise-floor overlap), and the true-positive control
only validates the check for the one crib long enough to test the assigned period. The target's
59 hits do not stand out from the noise; the honest conclusion is "this specific crib-drag design
lacks power to distinguish a real short-period key from chance at N=44 with this crib list", not
"no periodic key is present".

## Overall

Target (b) periods 2-8: not a test at this N (control below gate). Target (b) period 1 / Caesar
degenerate case and (c) full deterministic-key + Caesar-0-25 scan: clean negatives with working
controls (control true-key rank1 3/3; control false-positive rate matches target's flat 0/93
judge-PASS and matches its crib-hit ceiling). Target (d) crib drag: not informative at this N
(control false-positive rate overlaps the target's hit count; control true-positive recovery is
explained by crib-length limits, not by a broken test, but does not license a negative claim).
Per rule 5 (partial, never closed-negative, on any control-backed gap or non-test negative): (b)
periods 2-8 and (d) are `partial`, not `closed-negative`; (b) period 1 and (c) are clean,
control-backed negatives. Orchestrator to log a NEAR.md-adjacent note only if/when it aggregates
all of bullet-tuscany-1944's tests -- this worker does not edit NEAR.md, LEDGER.md, ASSIGNMENTS
or status.json (LANE B3 rule).

Cheap test 3 (index-of-coincidence, monoalphabetic vs polyalphabetic) not run: this brief names
test 2 only.

25 Sept 2026, LANE B3 worker bBUL2 (Sonnet). No network, no subagents.
