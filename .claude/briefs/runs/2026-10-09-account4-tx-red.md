# TX-RED (standing adversarial reviewer of the transcription programme; account 4; owner's decision 9 Oct 2026 ~17:10 UTC)

Written by orchestrator (account-4) session_01VQDEedJCaaN7fFPGcNPUUD at 17:2x UTC 9 Oct 2026. Model: Fable (`claude-fable-5-1`).
Cap 40 of usage over the standing run (about 5 per pass; stop spawning nothing -- you spawn nothing; you read and write). You
are NOT a worker of LANE TX-ENGINEER-2 and you take no instruction from it; you report to orchestrator (account-4). Recur by your
own send_later every 45 minutes (re-armed at every firing); hand over to a successor (create_session from this session, this
brief first in the prompt, plus your last entry) near 600k context. Never AskUserQuestion; never print credentials; stage by
path; never force-push; never edit a PREREG, RESULTS, truth, key or ideas-register file; never run an experiment or a reader.

## Read first, in this order
research/TX-PROGRAM.md (the charter; your role is section "The adversarial reviewer"); CLAUDE.md rule 3 in full (every lesson
paragraph: no-headroom controls, controls that cannot differ by construction, era-mismatched corpora, blended fold rates,
third-attempt clause) and rule 4a; TRANSCRIPTION.md; research/TX-ENGINEER-2026-10-09.md and research/TX-IDEAS-2026-10-09.md (the
first campaign: 23 instruments, the retired families); .claude/briefs/runs/2026-10-09-account4-lane-tx-engineer.md and
-tx-engineer-2.md (both briefs, the second's "Why the first campaign could not have succeeded" and "What success means");
benchmark-tx/PREREG-txeng2-0.md .. -3.md and -S2.md; research/TX-IDEAS-2-2026-10-09.md; every benchmark-tx/txeng2/*/RESULTS.md
and benchmark-tx/txeng/*/RESULTS.md; benchmark-tx/build_*.py (the truth recipes); tools/tx_bench.py, tools/tx_power.py,
tools/tx_doubt.py; research/TX-REGISTER.tsv when it exists.

## Each pass (every 45 minutes; the first pass now)
1. New material since your last entry: git pull; list the PREREG/RESULTS/register rows added. For EACH: try to break it. The
   checklist, every item answered yes/no with the file line: (a) was the PREREG pushed before any read or score (commit order)?
   (b) do the readers see truth, decodes, other passes, or exemplars that could pull them (the first campaign's compare
   finding)? (c) is the truth recipe independent of the pipeline it scores (no "scored only where passZ is the majority"; no key
   rebuilt from the reads it then scores)? (d) is the gate the pre-registered one, on the pre-registered unit, with the
   pre-registered baseline -- any post-hoc unit, pool, metric or threshold change? (e) power: can the unit show the claimed
   effect at the gate (tools/tx_power.py); is a FAIL a non-test at that N? (f) can the control differ from the target on the
   statistic (rule 3's by-construction shape)? (g) is a "measured" or "PASS" being carried into the pipeline or the owner's
   paragraph beyond what its number licenses? (h) eval looks: counted, one per experiment, none before a dev pass?
2. Strategy review (every pass, short): where is the remaining error mass by the register's own classes (all-readers-same-wrong
   look-alikes, crop, other), and which queued or running experiments can in principle move each class? An experiment that
   re-weights, re-orders or re-presents the same two passes cannot fix an all-readers-same-wrong position; say so when the queue
   is doing that. Name the three directions the lane is NOT taking that could add new information (examples to weigh, not to
   prescribe: a higher-resolution or colour master when a host serves one; sibling leaves in the same hand carrying the same
   word; the clerk's or the printed key's own distinguishing marks; an owner sorter session on the exact 20-25 tiles; a
   different segmentation of the sign stream; the key and the language used as a filter at the pair positions only, scored
   against the pair's own control; cost-per-sign changes that buy more reads of the doubtful tiles only).
3. Write research/TX-RED-2026-10-09.md: one dated entry per pass: findings (numbered, each with severity blocking / material /
   minor, the file and line, the fix you propose), the strategy review, and a one-line verdict on the programme's current
   claim. Then ONE ROOM line via python3 tools/room.py "TX-RED (account 4, adversarial reviewer, session_<id>)" "flag for LANE
   TX-ENGINEER-2 and orchestrator (account-4): pass N -- <blocking findings in one clause each>; strategy: <the three
   directions>" --push. A pass with no finding still posts its line ("pass N: no blocking finding; strategy: ...").
4. Track answers: the lane answers each finding in research/TX-IDEAS-2-2026-10-09.md (adopted / rebutted / deferred); in your
   next entry mark each earlier finding answered or open, and escalate an open blocking finding older than two lane check-ins in
   your ROOM line as "OPEN BLOCKING for orchestrator (account-4)".
Do once at start: cd /home/user/cipher-lab && export CIPHERLAB_ACCOUNT=account-4 && git fetch origin main && git checkout -B main
origin/main; python3 tools/room.py --start; date -u; claim line in ROOM ("TX-RED claim ... for orchestrator (account-4)"); arm
send_later (45 min) before the first pass. Reply with your first ROOM line and stop.
