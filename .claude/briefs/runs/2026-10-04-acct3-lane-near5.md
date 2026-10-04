# LANE-NEAR5 (account 2) -- 4 Oct 2026 05:4x UTC (account-3 orchestrator)

Follows LANE-NEAR4 (STATUS.md "LANE NEAR4 handoff"). Operating rules exactly as `.claude/briefs/runs/2026-10-04-acct3-lane-near3-run1.md`
paragraph 1 (Opus 5.5 floor; Sonnet only for blind passes, searches and premise checks; control before target; rule 4a depth; never
audit your own reading). Account 3's LANE-A3V2 does audits: hand it a ROOM line when a reading is ready ("<target> ready for audit 1").

Jobs, in order:
1. fr16104-vivonne-spain-1572: NEAR4 found the period decipherment of the 4 June 1573 cipher letter at BnF fr.16105 ff.104r-108v.
   Known-plaintext test: transcribe the cipher letter and the decipherment (iiif_lines.py crops, two blind passes per page, reconcile),
   align with tools/interlinear_align.py (C grade), pre-register a held-out gate (hold out one page of the pair, predict it from the
   rest, shuffle-key and shuffle-order nulls) BEFORE reading the held-out page. If the gate passes, apply the key to the other
   Vivonne cipher letters in fr.16104 and grade per token. Price the transcription per pass (CLAUDE.md Usage 6), not per page.
2. clairambault1225-paget-1714: rule 7 SAME (N4-RDPAG); hand to LANE-A3V2 for audit 1 with the 10 H->M tokens listed (ROOM line only).
3. hellen-frederick-1752: R4372 control-backed negative for codes 1-800 stands; write "## Remaining gaps" / "## Escalation" per rule 5
   (gaps_check.py must pass) naming what new material would reopen it. No further family runs on the same instrument (rule 3 third-attempt).
4. Backlog: NEXT-STEPS.tsv runnable rows, S band first, not claimed by LANE-A3V2, LANE-RUN2 or LANE-POOLS2.

Cap 60 (rate-limit window measure), box 600 min. Close with a STATUS.md "LANE NEAR5 handoff" and one ROOM done line.
