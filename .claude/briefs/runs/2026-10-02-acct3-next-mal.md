# NEXT-MAL (malsburg-hessen-1636): run the cheapest next step from the finish-or-blocker pass (2 Oct 2026, written by account 3; runs on account 2)

Model: Fable while it answers, else Opus 5.5 (never below). Cap USD 8.0, box 60 min; stop before any unit that would cross 80% of either.

The target's NOTES.md ends with "## Remaining gaps (finish-or-blocker pass, 1 Oct 2026)" and "## Escalation (1 Oct 2026)",
written by a classifier and checked by an adversarial second agent. Its verdict line:

    Verdict: keep going: 13 internal gaps; cheapest next: queue the LOCAL-QUEUE row for Arcinsys Hessen's record of HStAM 4 h Nr. 1411 (contents of the image numbers HCPortal omits), ~$0.5, then the three clear-page direct reads (f.12 "cifrat cela", f.14 foot, f.16 panel), ~$4.5, then key_crossmatch on the pool plus the marburg1635/Rabenhaupt/Heusner keys, ~$4

Job: run exactly that cheapest next step -- nothing else (CLAUDE.md Workers: stop when the brief is met).
1. `python3 tools/room.py --start`; read the last 30 ROOM.md lines; if a live claim (<6 h) from another session covers malsburg-hessen-1636, stop
   and post one line saying so. Otherwise claim: `python3 tools/room.py "NEXT-MAL (account 2)" "claim: malsburg-hessen-1636 -- cheapest next step from the finish-or-blocker section"`.
2. Read the two sections and the NOTES steps they cite. Run the step. Rules that bind it: rule 2 (image over transcription),
   rule 3 (any solver/family/judge run has its matched control first, both numbers reported; a control below its gate
   licenses nothing), rule 4 (grade per token), rule 7 (a changed reading regenerates with the target's decode script and
   --check, judge output pasted), rule 10 (never "new"/"first"), the good-citizen rule for outside hosts (one request at a
   time, >=1.5 s apart, stop on 403/429/challenge), Usage 6 (any transcription subagent gets line crops from
   tools/iiif_lines.py, never a full page). Do not touch ciphers/debosnys-1883 or any other target.
3. Write the result as a dated NOTES.md step, then update the finish-or-blocker sections IN PLACE for what this step settled
   (gap line's blocker/next, escalation mark [x] with the result, Verdict line, Read so far if a measured figure changed).
   Run `python3 tools/gaps_check.py malsburg-hessen-1636` and paste its line into your done line.
4. If the step needs a person or an owner-side host (LOCAL-QUEUE/JSTOR row, ASKS row), write that row and stop there.
5. Commit by explicit path; `python3 tools/room.py --push <paths>`; done line with the result in one sentence, cost, and
   request count per host. Do not edit status lines, status.json, STATUS.md or NEAR.md: flag the parent instead.
