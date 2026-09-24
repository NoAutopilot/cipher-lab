LANE B breadth worker: dorabella-1897. Sonnet (claude-sonnet-5). Cap $3.
Common rules: `.claude/briefs/runs/2026-09-24-lane-b-common.md` (read it first; it governs).

Spec: specs/dorabella-1897.json. Run `cheap_tests_in_order[0]` and its matched control, nothing else. Write both numbers into the spec's `cheap_test_done` (with date, method, cost). Judge any candidate plaintext with `tools/judge_plaintext.py` and paste its output. Cap $3. Report in five lines; do not run test 2; rule 10 wording; a negative's done line carries the target and control numbers side by side.

The test needs the text of Alice Elgar's July 1897 letter to Mrs Penny as printed in Powell 1937. Check, one host at a time: archive.org metadata and be-api fts for Powell's Memories of a Variation (any edition) and for a quotation of that letter elsewhere (Cipher Mysteries, Wase 2025 via OpenAlex/Crossref abstract); Google Books is LANE V3's, do not use it. If the letter text is not reachable without a loan or a person, stop: blocked line in cheap_test_done, ASKS row (a page read in a lending-only book), report. If it is reachable, run the index rule under the four encodings with the 200-random-string control.
