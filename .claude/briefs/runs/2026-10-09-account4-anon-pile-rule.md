# ANON-PILE-RULE: apply the owner's yes on ASKS 158 (account 4, Opus 5.5, cap USD 4, box 45 min)

Written 9 Oct 2026 21:1x UTC by date -u by the orchestrator (account-4), session_012sGNgiddCpz4QUhQsMyoPU. The owner, 21:0x UTC
(2:0x pm PT), on ASKS 158: "If number two is asking to take on an anonymous pile from BnF, yes. I'm all for anonymous piles."

Job, in order (read CLAUDE.md Usage 8a "rules become tools" and 8 first; ROOM claim via tools/room.py; done line "for orchestrator
(account-4)"):
1. CLAUDE.md, Pipeline item 2 (Check-solved): add the anonymous-pile paragraph using the proposal's wording verbatim from
   research/MARY-STUART-TALK-2026-10-09.md "## Proposal for the parent: anonymous-pile intake" (the blockquote), headed
   "Anonymous piles (owner, 9 Oct 2026 21:0x UTC, ASKS 158)". Unchanged: rule 3 controls, rule 10 wording, worker caps, the status
   vocabulary. Add one line to UPDATES.md's tail naming the change and the date.
2. tools/intake_gate_check.py: an anonymous-pile target (NOTES.md head carries `- **Pile:** anonymous` or the verdict line says
   "anonymous pile" / "unattributed pile") passes the gate on a HOLDER-based check-solved citation (holder, shelfmark, folio range,
   glyph set; DECODE, Cryptiana GL.htm and the unsolved lists, both solver repositories, the holder's own notice named as read) with
   the edition step recorded as "deferred until a sender is named", and is otherwise blocked exactly as before. Docstring: state the
   must-catch kind (an anonymous pile whose verdict names no holder-side sources read; an attributed target trying to use the
   holder path) and the must-not-block kind (an attributed target with a full edition citation, unchanged behaviour), each with an
   offline test added to tools/tests/test_intake_gate_check.py; all existing tests still pass. SYSTEM.md line for the new path
   (tools/system_map_check.py ok).
3. Re-queue the fr.3029 pile trial: `python3 tools/work_queue.py --add MQS-BNF-S6b --account account-4 --brief
   .claude/briefs/runs/2026-10-09-ytbiz-mqs-next-bnf-s6.md --model "Opus 5.5" --cap 3 --box 100 --note "ASKS 158 answered yes by the
   owner 9 Oct 21:0x UTC: the anonymous-pile intake path is in CLAUDE.md; run S6 as briefed; for orchestrator (account-4)"`; append
   one line to that S6 brief saying the precondition is met (date, ASKS 158, this job).
4. ASKS.md row 158: status answered -- "yes (owner, 9 Oct 2026 21:0x UTC); applied by ANON-PILE-RULE; S6 re-queued as MQS-BNF-S6b".
5. tools/file_shrink_guard.py on CLAUDE.md, ASKS.md, UPDATES.md, SYSTEM.md, WORK-QUEUE.tsv before the push; stage by path; never
   force-push; never AskUserQuestion; never print credentials; no ciphers/ file touched.
