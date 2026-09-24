# specs/ — machine-readable problem specs for the public unsolved-cryptogram list

Written 24 Sept 2026 (UNSOLVED-SURVEY.md, PROCESS-2026-09-24.md). One JSON per item in the survey's top ten, in the
spirit of the curated Erdős-problem repository that the 2025-26 AI-mathematics results ran on: the ciphertext as
transcribed (with its source and fetch date, or `ciphertext_pending` with where to get it), the alphabet, the known
constraints, the cheap tests in order, and a `judge` block that `tools/judge_plaintext.py` reads to score a candidate
plaintext without a person. `cheap-tests/` holds the three tests actually run on 24 Sept 2026 with their controls.

    python3 tools/judge_plaintext.py specs/koehler-1944.json --file candidate.txt

A PASS from the judge is a gate for a verifier (CLAUDE.md rule 10), never a reading. A spec's `cheap_tests_in_order`
are proposals; only `cheap_test_done` entries report numbers, and each reports its matched control (rule 3).
