# GAPSFIX (account 3 worker) -- 4 Oct 2026 17:5x UTC (account-3 orchestrator)
Job: bring six NOTES.md files into the rule-5 "finish or name the blocker" format so `python3 tools/gaps_check.py --all` passes, and
fix two wrong status lines. No decoding, no network, no new claims: summarize what each folder's own NOTES/AUDIT/HYPOTHESES already says.
A. Missing "## Remaining gaps" + "## Escalation" (status partial): bullet-tuscany-1944, eckert-1864,
   huntington-blathwayt-madrid-1728, lope-hurtado-1522. Format = tools/gaps_check.py docstring exactly. "Read so far:" from the folder's
   own measured counts (cite the section) or "unmeasured" + why. Each gap gets an honest blocker; internal gaps name "; next: <step>,
   ~$<cost>" taken from the folder's own written next step (its "While waiting" / "What would actually move this target" sections).
   An escalation step tried 3x with one instrument is [retired] naming it (rule 3); a known untried instrument is [ ].
B. LANE-NEAR8 flag: fr15575-syllabic-1592-95 and fr3151-seure-1558 read "blocked" on line 1 but carry workable gaps (fr15575: f.228
   L01-04 PASS, L05-08 FAIL; seure: a control-backed non-test). Read each folder's last sections; if any gap is internal/workable, set
   the line-1 status to `partial` and add the two sections; if every piece truly waits on an outside blocker, keep `blocked` and say why
   in one line under it. Also update status.json's status for any target you change (fetch+rebase first; keep others' edits).
C. Run gaps_check on each, then --all; file_shrink_guard on every touched file; commit by explicit path; ROOM done line with the
   per-target verdicts (keep going / parked / blocked kept).
Model Opus 5.5. Cap USD 4, box 40 min. ROOM claim/done via tools/room.py.
