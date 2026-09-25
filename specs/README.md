# specs/ — machine-readable problem specs for the public unsolved-cryptogram list

Written 24 Sept 2026 (UNSOLVED-SURVEY.md, PROCESS-2026-09-24.md). One JSON per item in the survey's top ten, in the
spirit of the curated Erdős-problem repository that the 2025-26 AI-mathematics results ran on: the ciphertext as
transcribed (with its source and fetch date, or `ciphertext_pending` with where to get it), the alphabet, the known
constraints, the cheap tests in order, and a `judge` block that `tools/judge_plaintext.py` reads to score a candidate
plaintext without a person. `cheap-tests/` holds the three tests actually run on 24 Sept 2026 with their controls.

    python3 tools/judge_plaintext.py specs/koehler-1944.json --file candidate.txt

A PASS from the judge is a gate for a verifier (CLAUDE.md rule 10), never a reading. A spec's `cheap_tests_in_order`
are proposals; only `cheap_test_done` entries report numbers, and each reports its matched control (rule 3).

Ordering `cheap_tests_in_order` (25 Sept 2026, RETRO-2026-09-25l): a raw statistic (index of coincidence, letter
frequency chi-squared) with no operationalized yes/no hypothesis often lands inside more than one candidate
family's control band and settles nothing -- LANE B3's six parallel first tests on ranks 21-30 (ROOM.md 19:47)
split exactly on this line: bGLD, bYOG and bUNT each asked one sharp yes/no question against a matched Monte
Carlo control and came back decisive (a control-backed negative, a negative, and a control-backed positive
lead); bBLZ's bare IC/frequency profile (N=581) matched the monoalphabetic-English control's band case-folded
and matched neither candidate case-sensitive, and its own worker named the fix: "the obvious test 2 is
family_run masc with an English judge." When the target has enough length for `tools/family_run.py` (roughly
N>=150-200) and no sharper hypothesis is available, write `cheap_tests_in_order[0]` as the cheapest applicable
`family_run.py` family (masc first) with the judge, not a bare IC/frequency comparison -- `family_run.py`
returns a categorical control-gated PASS/FAIL, which a raw statistic in an overlap zone cannot. Below that
length (bSSR N=37/45, bRAY N=74, same day: IC fell inside every candidate control's band at once), say so in
the spec itself -- the test-1 note names the length problem and points straight at the next test that does not
depend on IC -- rather than let a $2-3 worker rediscover the null result each time.
