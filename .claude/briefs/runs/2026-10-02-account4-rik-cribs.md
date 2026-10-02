# RIK-CRIBS: riksarkivet-r4282-1628 -- R4282's own clear-Latin phrases as cribs (Escalation item "clear-pages")

Written 2 Oct 2026 01:0x UTC (clock read) by the account-4 parent (session_01SEzoee67SivPooFpTkxMme).
Role field for ROOM.md lines: `RIK-CRIBS (account-4)`. Model: Fable 5.1 (Opus 5.5 if Fable fails). Cap: USD 4.
Box: 40 minutes. Disk only: no network, no vision. Intake gate: `python3 tools/intake_gate_check.py
riksarkivet-r4282-1628` -> "open (line 1) -- edition/page or full-text-search citation found within 6 lines (exit 0)"
(WEBCHECK-riksarkivet-r4282-1628, 2 Oct 2026 00:18 UTC).

## The job, in one line

NOTES.md "## Escalation", the first unticked item: R4282's own clear-Latin cribs ("et qualis sit eius futurus status
dubitatur", "sed tamen ut res", "tractatus magnas admodum", "Mittatur nobis responsum") were not tried by bRIK (26 Sept
2026). Drag each clear phrase along the R4282 cipher stream as a crib under same-sign-same-letter constraints, with a
matched control, and say whether any placement beats chance.

## Steps

1. `python3 tools/room.py --start`; last 30 ROOM.md lines; claim line.
2. Read NOTES.md "What this is", "Test run (bRIK)" and "Escalation"; `r4282_transcription_bourdeau.txt` (Bourdeau's
   transcription, CC BY 4.0 -- cite); `scripts/crib_test.py` for the sign parsing. Note where the clear phrases sit
   relative to the cipher runs (a clear phrase immediately before or after a run is a candidate for the run's content
   only if the sense continues; a phrase inside a sentence that resumes in cipher is the stronger crib).
3. Use `tools/crib_pattern.py` (H28, 28 Sept 2026: drags a known phrase along a sign-coded text under
   same-code-same-letter constraints, tolerated misreads, scored by the implied partial key's whole-text unigram,
   against shuffled-order controls; `--help` first, test in tools/tests/test_crib_pattern.py). Run each of the four
   phrases, and the bRIK homophonic letter->signs key as a `--lock`-style constraint only if the tool supports it
   (do not add an option unless it is small and tested; otherwise run unconstrained and say so). Control: the tool's
   own shuffled-order placements, plus one phrase of the same length drawn from a Latin corpus in tools/data
   (la18 or la_repo) that is NOT on the leaf (a negative crib), so a "best placement" number has a floor.
4. Report per phrase: best placement, its score vs the shuffled-order p95 and vs the negative crib's best, the
   implied partial key (letters -> signs) and whether it agrees or conflicts with bRIK's crib key from the R4284
   leaf (agreement on even 3-4 letters across two independent cribs is the signal; conflict is a finding too).
   Grade any letter value M at most (rule 4; the CRYPT B5 "S needs two words" line). No reading is claimed.
5. HYPOTHESES.md: one row per phrase with target and control numbers side by side. NOTES.md: a dated section
   "## RIK-CRIBS (2 Oct 2026, account-4)" and tick the Escalation item with a one-line result. Status word stays `open`.
6. Commit by explicit path, rebase on origin/main, `python3 tools/restricted_guard.py --outgoing`, push to main.
   Done line with the numbers. Stop; the 68 untried key records (Escalation item 2) are DECODE-image-gated and not this job.

Rule 3 (control beside every number), rule 10 wording. The common tail of `.claude/briefs/README.md` applies in full.
