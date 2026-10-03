# Successor prompt for the account-4 parent (rewritten 3 Oct 2026 12:2x UTC by session_011mUCfY7R8vtAG69d6fSJik, parent 4; parent 3 was session_01S3ZaR74RRQ7BPpHT5JGaGV)

You are the account-4 parent orchestrator for cipher-lab (github.com/NoAutopilot/cipher-lab), successor to
session_011mUCfY7R8vtAG69d6fSJik (parent 4). Read, in order: CLAUDE.md, SYSTEM.md, `.claude/briefs/parent.md` (esp.
"Keep slots full", "Orchestrator fallback chain", "Model floor"), STATUS.md "Check-in 44".."Check-in 66" paragraphs (the
newest are just above the "## Account-3 orchestrator handoff (session_0198Cv8ypBfBVfRToKVWx33M)" heading), the last 60
ROOM.md lines, NEAR.md. Role field for your ROOM lines: `account-4 parent`; export CIPHERLAB_ACCOUNT=account-4.

## Owner's standing instructions (2 Oct 2026, still in force)
- Fable is maxed: every session on Opus 5.5 (`claude-opus-5-5`), every subagent too; nothing below Opus 5.5.
- Keep slots full: hold 6 live account-4 workers (+ one CLOSER per wave). send_later check-in every 15 minutes while any
  worker is live; refill every finished slot. Stop spawning only at rate_limit_info `rejected`.
- seven_day `allowed_warning` (resets 5 Oct 20:00 UTC) is NOT a stop (BUDGETS amendment 27 Sept; account 3 confirmed
  06:06 UTC 3 Oct) -> 6 workers. No owner reply on the earlier compromise question; none needed now.
- Skip anything accounts 1/2/3 claimed under 6 h. Off limits: debosnys-1883 + private repo, hessen-1824,
  espagnol142-mercy-1648, all Nevers/Birago/Dinteville/fr3993/fr3416 (account 3 + LANE-A1 on account 1), account 2's
  colbert26/harley-287/na-raad-azie/fr2980-gramont (owner: do not resume). Outreach drafted only, never sent.
- Report to the person in short paragraphs, Pacific time first.

## Check-in loop (what worked 3 Oct 05:40-12:20, 23 check-ins, ~110 workers)
1. `git fetch -q origin main && git rebase -q FETCH_HEAD`; `date -u`.
2. Done lines: grep each live role name directly: `grep -E " \| ROLE[^|]*\| (done|flag|blocked)" ROOM.md | tail -1`
   (the awk role-field filter missed lines twice). get_session EVERY worker older than 20 min: cost vs cap; at >1.5x
   send_message priority now "STOP ... push what you hold" (GAPS68 ran USD 25 on a cap of 8 via an empty subagent
   placeholder -- every brief now says grep subagent prompts for unfilled placeholders).
3. Next job per target = its NOTES.md Verdict line or the worker's done-line "next". One target, one job. Generic brief
   `.claude/briefs/runs/2026-10-02-account4-gaps-step.md`; first prompt line "First action: `python3 tools/room.py
   --start` (never any git checkout/reset/pull/stash by hand; export CIPHERLAB_ACCOUNT=account-4 on every command)".
   NEXT-STEPS rows are often stale (mccormick, maurice-rupert, hza step 1 were already done): every NEXT-STEPS brief
   says "stale-check NOTES.md history first".
4. create_session: source_url https://github.com/NoAutopilot/cipher-lab, revision main, model claude-opus-5-5, tags
   ["cipherlab:account-4","cipherlab:worker"], title `LIVE account-4 worker <JOB> · <target>`.
5. One CLOSER per wave (`.claude/briefs/runs/2026-10-02-account4-closer.md` + CLOSER-22/23 amendment: it archives,
   records cost_usd AND appends LEDGER rows itself). Last: CLOSER-60.
6. STATUS.md: insert "Check-in N" paragraph before `## Account-3 orchestrator handoff (session_0198Cv8ypBfBVfRToKVWx33M)`
   (python replace). ROOM line via room.py --push. send_later 15 min listing live ids. Hand over again at ~700k context.

## Live at hand-over (3 Oct 2026 12:20 UTC) -- next check-in number 67
- CLOSER-60 session_01A5bShTiEAYw226oq9MWSpV (archives CLOSER-59, FT4q, GAPS98-102)
- FT4r-rousseau f.265r/f.266r pair gate, 722=i vs ti session_01JLG8DXrVABbyhWs59rk6FZ (cap 6)
- GAPS103-hza-hohenlohe LABW sibling sweep + Bue 161 copy-order ASKS row session_01CZpBL6JTqkEnM2QNjwtvFC (cap 3)
- GAPS104-sufi-fiddle Verdict step or park session_011aHfgshfbZY5He4V8wbBpN (cap 4)
- GAPS105-heinsius-dopff-1702 NEXT-STEPS session_01RaMSyFvyPxJMtDC1QuhyyD (cap 6)
- GAPS106-florence-dieci-responsive NEXT-STEPS session_0189NttUmNziUZark1Eu5w9L (cap 6)
- (parent 4 arms no more check-ins after hand-over)

## State of the leads
- naf14913-rousseau-venice-1743: numeral key from Rousseau's slips. f.213 pair fits only with 722 = i (f.206 pin says
  ti) -> polyvalence question; FT4r gates the new fifth pair f.265r/f.266r under both. A registered PASS on an
  independent pair -> brief a VERIFY. Still queued: f249 70 control draws in their own ~2.5 h box (never concurrent with
  another rousseau worker).
- na-suriname-map-1781 2077 legend: H 538 C 10 M 61 U 49, gate 0.765; N1 provisional (VERIFY4); stage 9 blocked on
  LOCAL-QUEUE L36/L41. No breakthrough alert.
- fr4715-vieuville-pool: f.7r follows Tomokiyo letters (fixed-key PASS); no.60 = Tomokiyo's published passage (slip
  upside down); PARKED on ASKS 114.
- bowes-walsingham-1583: code layer N0 published (Haynes 1992), status.json note corrected; L44 queued.
- goldbar-1933: Milton Kim claim = Enigma pass, below random control; open, claimed-unverified.
- hza-hohenlohe-1679: LABW Sf 35 Bue 161 encloses a cipher key (undigitised) -> owner copy order = a recovery job.
- sufi-fiddle: Arabic word-list match p 0.02; two readers converge on muhammad/barakat at M; no reading.
- PARKED today: vanspaen-vandergoes-1808, willem-van-hessen-1567 (KHA draft checked, owner sends; still needs rule-8
  Gmail prior-contact search + CONTRIBUTIONS row), riksarkivet-r4282-1628, bl-james-1669, fr4715-vieuville-pool.
- New corpora: tools/data/fr17, la17, de17, sv17 (all with per-fold LOO; p05 gate weak at N~1000, use held-out p01).

## Queue for the successor
- Results of the six live jobs; VERIFY-ROUSSEAU if FT4r passes.
- NEXT-STEPS rows not touched by accts 1/2/3 in 6 h (kaliningrad-2015, matignon-mayenne-1586 careful: rule-3 example);
  intake-gate failures (only account 3's remain at 11:22).
- Owner items to mention: KHA request ready to send after his Gmail check; LABW Bue 161 copy order (GAPS103 ASKS row);
  sign-sorter focus.tsv rows (r4282, sufi-fiddle).
