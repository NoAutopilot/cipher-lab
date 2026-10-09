# TX program: the standing effort to raise per-sign transcription accuracy (owner's decision, 9 Oct 2026 ~17:10 UTC)

Owner, 9 Oct 2026: "I'd like to continue on this, because it is going to be our biggest challenge ... spin up to 10 recurring
towards the goal, refilled as others close. Make sure there's some sort of understanding on what had been tried before and what
failed. Point another one outside of these at the experiments as an adversarial stance to point out flaws in our approach ...
make sure you don't lose visibility / ownership to this work." This file is the charter every TX session reads first. Owner:
orchestrator (account-4). Written 9 Oct 2026 17:2x UTC by session_01VQDEedJCaaN7fFPGcNPUUD.

## Goal and what success means
Unchanged from `.claude/briefs/runs/2026-10-09-account4-lane-tx-engineer-2.md` "What success means" and
`benchmark-tx/PREREG-txeng2-0.md`: S1 held-out per-sign error lower under the new pipeline on a pool with >= 32 baseline errors,
paired fixed > broken at p < 0.01 (one eval look per experiment); S2 one look at the confirm2 item (vivonne1573-f103r-confirm2,
never opened before the final score); S3 a live letter; S4 the sorter doubt feed and value curve; S5 cost per 100 signs.
The product the owner needs: an unseen hand read at <= 5% (today 8.8% on Spinelli, 13-25% two-reader splits on the live letters).

## Slots (account 4; at most 10 recurring sessions on this programme at once, refilled as others close)
| slot | role | model | who spawns / refills | recurs by |
|---|---|---|---|---|
| 1 | orchestrator (account-4) -- owns the programme, reports to the owner | Fable | the owner / successor hand-over | its check-in (40 min) |
| 2 | LANE TX-ENGINEER-2 -- runs the experiment queue, pre-registers, ledgers its workers | Fable | the orchestrator; successor incarnation at ~700k context | its own send_later (30-45 min) |
| 3 | TX-RED -- the adversarial reviewer, outside the lane, never one of its workers | Fable | the orchestrator; successor at ~600k context | its own send_later (45 min) |
| 4-10 | experiment / build workers (one PREREG'd experiment or one benchmark item each) | Opus 5.5 or Fable | the lane, refilled from the register as each closes; the dispatcher if the lane is down (WORK-QUEUE TX-* rows) | one job, then done |
Refill rule: the lane keeps 5-7 workers live while the register has a runnable row; a slot freed by a done line is refilled
at the lane's next check-in, never left for the hour. Spawning stops only on `allowed_warning` past one check-in or `rejected`
(BUDGETS.md), and resumes at the reset.

## Memory: what has been tried and what failed (the rule)
One register, `research/TX-REGISTER.tsv`, compiled by `tools/tx_register.py` from every PREREG and RESULTS file of both campaigns
(benchmark-tx/PREREG-*.md, benchmark-tx/txeng*/**/RESULTS.md, research/TX-IDEAS*.md, TRANSCRIPTION.md's "Today" rows): one row
per experiment with id, family, mechanism attacked, unit/pool, dev result (fixed/broken/p), eval result (looks), verdict
(dev-FAIL / dev-PASS / moved-eval / did-not-move / non-test / retired / measured), and the one-line reason. A new PREREG is
accepted only if it names the register rows it is nearest to and says in one sentence what is different (a family retired under
rule 3's third-attempt clause is not re-run without a different instrument or new material). Every TX session reads the
register before its first action; the lane regenerates it at every check-in; TX-RED audits it.

## The adversarial reviewer (TX-RED)
Brief `.claude/briefs/runs/2026-10-09-account4-tx-red.md`. It reads every PREREG and RESULTS as they land and tries to break
them: leakage (readers seeing truth, decodes, other passes, exemplars that pull), circularity (truth recipes that score the
pipeline right by construction, keys rebuilt from the reads they score), gate shopping, power, unit/pool mismatches, the
"control cannot differ" shape (CLAUDE.md rule 3), over-claims in the owner's paragraph. It also reviews the STRATEGY: whether
the queue is attacking where the error mass is (the first campaign found errors that every reader gets wrong the same way, in
every presentation -- re-weighting the same passes cannot fix those; new information can) and names the three directions the
lane is not taking -- at least one of them from outside the programme's own frame (the other solvers' solved items, print,
another archive, a person's reading), per .claude/briefs/README.md "Outside the frame before 'blocked'" (owner, 9 Oct 2026). Findings go in research/TX-RED-2026-10-09.md (one dated entry per pass) and as ROOM lines "flag for LANE
TX-ENGINEER-2 and orchestrator (account-4)"; the lane answers each finding in the ideas register (adopted / rebutted with the
number / deferred with the reason) by its next check-in; the orchestrator reports open disagreements to the owner. TX-RED never
runs an experiment, never edits a PREREG, RESULTS, truth or key file.

## Visibility and ownership (the orchestrator's duties at every check-in)
1. get_session on the lane and TX-RED (cost, context, idle); ping a session silent past its own check-in time; successor from
   its brief if silent 60 min. 2. Read the register's new rows and TX-RED's new entry; keep the "TX programme" table in
   STATUS.md's orchestrator handoff current (slot | session | state | cost | last line | open red-team findings). 3. Hold the lane
   to the gate: no TRANSCRIPTION.md "Today" move without S1/S2; no eval look without a dev pass; the one-sentence "what is
   different" on every PREREG. 4. Carry the owner's view: the report (OWNER REPORT FORMAT) leads with experiments run / dev
   passes / eval looks / S1-S5 state / open red-team findings, in plain words.
