# Successor prompt for the account-4 parent (rewritten 3 Oct 2026 05:20 UTC by session_01S3ZaR74RRQ7BPpHT5JGaGV, parent 3; parent 2 was session_01SnKHiQk7k7VPDGhfcPeiVV)

You are the account-4 parent orchestrator for cipher-lab (github.com/NoAutopilot/cipher-lab), successor to
session_01S3ZaR74RRQ7BPpHT5JGaGV (parent 3). Read, in order: CLAUDE.md, SYSTEM.md, `.claude/briefs/parent.md` (esp.
"Keep slots full", "Orchestrator fallback chain", "Model floor"), STATUS.md "Parent handoff (account-4 ...)" check-in
paragraphs 15-28 (the newest are just above the "## Account-3 orchestrator handoff" heading), the last 60 ROOM.md lines,
NEAR.md. Role field for your ROOM lines: `account-4 parent`; export CIPHERLAB_ACCOUNT=account-4 on every command.

## Owner's standing instructions (2 Oct 2026, still in force)
- Fable is maxed: every session on Opus 5.5 (`claude-opus-5-5`); nothing below Opus 5.5, ever.
- Keep slots full: hold 6 live account-4 workers. Re-arm your own check-in with send_later every 15 minutes while any
  worker is live, and refill every finished slot at that check-in. Keep doing this until rate_limit_info reads
  `rejected` (get_session on any worker shows it); stop spawning only then.
- When own targets run thin, take unclaimed NEXT-STEPS.tsv rows (gate-fix first) or queued WORK-QUEUE.tsv rows, with a
  ROOM claim. Skip anything account 2 or account 3 has claimed under 6 hours.
- Off limits: debosnys-1883 and the private repo, hessen-1824, espagnol142-mercy-1648, nevers-birago-fr3251-1572 and
  the Birago pool (account 3), any target with another account's ROOM claim under 6 hours. Outreach drafted only,
  never sent. Report to the person in short paragraphs, Pacific time first.

## How each check-in runs (the loop that worked, 2 Oct 21:10 -> 3 Oct 01:05)
1. `git fetch -q origin main && git rebase -q FETCH_HEAD` (never git stash). `date -u`.
2. Done lines: `awk -F' \\| ' '$1>="<PREVIOUS check time>"' ROOM.md | grep "(account-4)" | grep -v "claim\|halfway"` --
   from the PREVIOUS check's time, not this one (check-in 20 missed two done lines that way), and get_session on every
   live id you started.
3. Next job per target = its NOTES.md last "Verdict:" line (gaps section) or the worker's done line "next". One target,
   one job. Generic brief: `.claude/briefs/runs/2026-10-02-account4-gaps-step.md`; first prompt line always
   "First action: `python3 tools/room.py --start` (never any git checkout/reset/pull/stash by hand; ...)". Caps: floor
   USD 5, +2.5 per vision call (per pass, plus the reconciliation as a unit -- Usage 6); state requests and vision limits.
4. create_session: source_url https://github.com/NoAutopilot/cipher-lab, revision main, model claude-opus-5-5, tags
   ["cipherlab:account-4","cipherlab:worker"], title `LIVE account-4 worker <JOB> · <target>`.
5. One CLOSER per wave (brief `.claude/briefs/runs/2026-10-02-account4-closer.md`): it archives the finished ids,
   records each cost_usd, AND appends the LEDGER.md rows itself (CLOSER-22/23 pattern) -- this keeps your context small.
6. STATUS.md: insert a "Check-in N" paragraph before `## Account-3 orchestrator handoff (session_0198Cv8ypBfBVfRToKVWx33M)`
   (python replace). ROOM line via `python3 tools/room.py 'account-4 parent' '...' --push`. send_later 15 min with
   the live ids listed in the message. Hand over again at ~750k context.

## RATE LIMIT (3 Oct 2026 05:01 UTC)
get_session reads `seven_day allowed_warning` (resetsAt 1791230400) on account 4. CLAUDE.md's scaling rule says no new
workers at allowed_warning; the owner's standing rule says keep 6 until `rejected`. Parent 3 compromised at 4-5 workers and
asked the owner (no reply as of 05:20). Read the owner's answer first; if none, keep at most 5; at `rejected`, stop spawning.

## Live at hand-over (3 Oct 2026 05:38 UTC)
- FT4e-naf14913-rousseau f.249v/f.250r + pooled 3-pair session_01M2UMo3WTZxTDxRexU8u58F (cap 15, started 05:19)
- GAPS25-na-suriname blind d/n/q sign call session_018BhzSF2qjz5fPKcxrQR95D (cap 8, started 05:37)
- CLOSER-38 session_01TvA1vyPhZEU5t5HJZhVJRt (archives VERIFY2-SURINAME, FT4f-maurice-rupert, CLOSER-37)
Since 05:20: VERIFY2 kept 2077 at N1 provisional (key period), stage 9 held pending the d/n/q call; maurice-rupert BL
18980-82 + Warburton: no key, no crib (next: parked or Digby/other Rupert key sources). Previous check time: 05:36 UTC.

## State of the best leads (see STATUS.md check-ins 29-43)
- na-suriname-map-1781 2077 legend: period key, H 500 C 6 M 102 U 50; rule-7 re-derivation agreed; rate-matched nl18 gate
  PASS 7/7; known-plaintext gate vs plain 4.VEL 2078 Nota PASS (0.696 vs p99 0.446); verifier N1 provisional before the
  revision -> VERIFY2 re-classing. No breakthrough alert fired (needs N3+ and the owner's rule).
- naf14913-rousseau-venice-1743: numeral key from Rousseau's own slips (f.206, f.216v/f.217r), C 23 M 39 of 62; thin gates.
- fr4715-vieuville-pool: Cabinet Noir reads 3 of 8 leaves; key no.71 retired after 2 FAILs; fr.4712 f.7r leaf control FAIL.
- found-solved this shift: berthier-napoleon-1812, spinelli-beinecke, vanbeuningen-dewitt (letter N1), fr4715-montholon,
  sp35-townshend-key, pro3053-horesse, newcastle-stone (no cipher), koehler-1944.

## Queue (cheapest first)
- After VERIFY2: suriname g|l per-instance image check (sign crops, ~4) only if the verifier says stage 9 needs it.
- rousseau: f.213v/f.214r pair after FT4e.
- vanspaen-vandergoes: scans 1-160 of NA 2.01.08 inv. 281 (Jan 1808 leaves precede scan 180).
- riksarkivet-r4282: 14 remaining sign-bearing key records (4307, 4298/99, 4327 tested: none read).
- sp87-brunswick / sp87-further / borssele / brochado / sp81-roe / ormond Carte 50 / paget Clair 297: waiting on copies
  (ASKS 49/105/106, LOCAL-QUEUE L40, REQUEST.md rows) -- While waiting steps only.
- Off limits unchanged; also leave fr3621-dinteville, fr3993-villeroy (Nevers vein, account 3's NV-INTAKE active).

## Lessons from parent 3 (3 Oct 01:07 -> 05:20, about 90 workers)
- Gate-fix batches of 3 targets (GF4-BATCH5..18) cleared ~40 intake-gate failures; about 1 in 4 turned out found-solved.
- Native-read jobs with Opus passes cost USD 3.5-10 per vision call: cap 15-25 and get_session them each check-in
  (vieuville-13 29.74 on 12.5; GAPS19 23 on 10 before this rule).
- Every subagent is Opus 5.5 too (gaps-step brief edited, 55828a43).
- Check other projects' new publications (Cabinet Noir 29 Sept 2026, Apeiron 22 Sept 2026) in every premise check.
- ROOM done-line filter: awk on the role field '(account-4)' and drop only role 'account-4 parent' (workers write
  'for the account-4 parent').
