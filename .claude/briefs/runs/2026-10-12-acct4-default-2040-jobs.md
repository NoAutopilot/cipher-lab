# LANE DEFAULT-account-4-20261012-2040 jobs (account 4, session_01Maz2cK8aHkMaLKKykShMP5), 12 Oct 2026

Brief: .claude/briefs/default-lane.md. Gate 0a: no SESSION-SWEEP-account-4 row in WORK-QUEUE.tsv. Probes 20:45 UTC 12 Oct (date -u):
Gallica 403, googleapis 503, archive.org 200. VERIFY-BACKLOG regenerated 20:47: high rows Birago only (off limits); audit2 rows N0/N1
(eckert-1864, Manteuffel 0436), gate 2 n/a. `next_steps.py --hot-only`: read row by row; most `parallel` actions are already run (MAT-F179
twice, VERIFY-HELLEN, naf14913 605 verify, R10-SRCH wallis, LAG-CHECK, BLA-TRY, HAR-GLOSS, ES132-RD) or Gallica/googleapis-bound. Two live rows.
Common tail: `.claude/briefs/README.md`. Claim/halfway/done lines in ROOM.md via `tools/room.py` with "for LANE DEFAULT-A4-2040 (account 4)".
Cost from get_session is the orchestrator's; stop before a unit that would cross 80% of cap or box.

Hosts this wave: archive.org ("IA", THUR-198 only, <= 15 requests, >= 1.5 s apart, take/release lines). SUR-GAPS is disk only.

### THUR-198 (Opus, cap 4, box 60 min): thurloe-printed, vol 4 n198 (p.195) and vol 6 l.76732
NOTES.md "## THUR-94B" and "## Remaining gaps (THUR-94B, 12 Oct 2026)". Intake gate 20:49 UTC (exit 0). Units (~1.5 each incl. crop + one look):
(1) vol 4 (collectionofstat04thur) leaf n198 = p.195: re-image, cut strip crops with `tools/iiif_lines.py --image <leaf> --out <dir>` (paste the
command and its output before any vision call), and read runs 3 and 6 for codes 25 and 51 with their printed glosses, on committed crops;
(2) vol 6 (collectionofstat06thur) l.76732, the other glossed Bamfylde Second Cipher letter: locate the leaf from the djvu/OCR first (script,
not a model read), crop the same way, tabulate every cipher cell with its printed gloss, and compare against vol 6 p.576 (THUR-94) and Tomokiyo for
94, 45, 87, 25, 51. Key rule unchanged: a key value changes only on two printed glosses; conflicts go to HYPOTHESES.md with both witnesses.
`--check` on any script touched; crops committed (small JPEG strips, never full leaves; images under 30 MB per folder). On an IA 5xx: one retry
after a pause, then stop the host and report. Update Remaining gaps / Escalation, run `tools/gaps_check.py thurloe-printed`. Report what was found
and where it was not found; do not classify novelty.

### SUR-GAPS (Opus, cap 2, box 45 min): na-suriname-map-1781, Remaining gaps refresh (record correction), disk only
LANE DEFAULT-A2-1810's handoff (STATUS.md, 12 Oct): the Remaining gaps list is stale -- the 2046/2077 legends were transcribed 2-3 Oct (GAPS18/19)
-- and owed a refresh before any lane takes its "not-attempted" rows. Read NOTES.md end to end for the gap sections (Remaining gaps, Escalation,
While waiting, SUR-372, SUR-IJ, SUR-MRICH, FAM-SUR373) and the folder's files. Write a new "## Remaining gaps (SUR-GAPS, 12 Oct 2026; replaces
...)" and "## Escalation (SUR-GAPS ...)" per rule 5 / `tools/gaps_check.py`'s docstring: each gap with its true blocker and dated evidence (file or
section), done steps marked [x] with the job that did them, [retired] where rule 3's third-attempt clause applies (name the instrument), and a
Verdict line. Also correct the "## While waiting" action line if it names a done step. No new reading, no grade change, no status-line change;
inv. 372 transcription stays a campaign decision for the orchestrator (name it, with its cost band, do not run it). `tools/gaps_check.py
na-suriname-map-1781` must pass; `python3 tools/next_steps.py` should then show the refreshed next step (paste its row). Report what changed.
