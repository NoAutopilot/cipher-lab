# Successor prompt for the account-4 parent (written 3 Oct 2026 01:0x UTC by session_01SnKHiQk7k7VPDGhfcPeiVV, parent 2, at about 640k context)

You are the account-4 parent orchestrator for cipher-lab (github.com/NoAutopilot/cipher-lab), successor to
session_01SnKHiQk7k7VPDGhfcPeiVV (parent 2). Read, in order: CLAUDE.md, SYSTEM.md, `.claude/briefs/parent.md` (esp.
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

## Live at hand-over (spawned 00:47-01:05 UTC 3 Oct)
- GF4d-berthier-napoleon-1812 session_019KTd6tLrsNNB5PHjRXUA3F (SHD 1812 grand chiffre table from jfbouch images, test)
- FT4d-maurice-rupert-1645 session_01G169VTsd9Vkbjusw8bmSwK (DECODE 8443/8444 Osborne siblings, Decrypted)
- GAPS17-na-janssens-java-1811 session_01W41pgMxEbp5upS9LRzH7Kc (LM-context fill of 26 conflicting codes)
- FT4b-esp318-sicilia-1503 session_01DeGrV7xZoJQBXnpZG5MYzD (sign-sorter page for the owner; ASKS row)
- FT4-decode-4450-bnf-fr20506-1525 session_01FNRGdLiyChDAdqxWFukfEv (Novarien 1990 / Ranzo table premise)
- FT4-ra-crusenstolpe-1809 session_01Lv6ETFFbQop4Eeu7cw1W6F (Adlersparre 1809 och 1810 p.207)
- CLOSER-23 session_01Cg5adi8zY55eijnjtjay7C (archives the 01:05 wave and ledgers it)

## Queue (cheapest first; check each target's Verdict before briefing)
- fr4715-vieuville-pool: no.39 f.62r cleared its control, keyed .14/.13/.52; next per its Verdict (no.44 has 6 of 7
  word-codes still unread).
- decode-2754-bnf-baluze156-1636: Sabran f.146r key (29 signs, C) does not read f.157r (p 0.815) -- next key family
  per its Verdict.
- na-suriname-map-1781: period keys found (NA 1.05.03 inv. 86); 2039 H 290, 2061 H 176, Remarque native H 165; AUDIT
  item 3: 2039 N1 provisional (LOCAL-QUEUE L36, de Leeuw 1997), 2061 N0. Next: 2046 and 2077 legends under the period
  key (~9 each).
- pro3055-clinton-1779: 3868, 2380, 3050, 3077 all N0; 4833 cipher at Kew; next per Verdict (low value).
- mccormick-1999: note 2 line 10 image check (Sadak departs from the transcription).
- riksarkivet-r4282-1628: R4280/R4281 vs R4284 (numeric) instead.
- hellen-frederick-1752: Michell sibling key control-backed negative; next per Verdict.
- oldenbarnevelt-brederode-1605: file the drafted LOCAL-QUEUE row for DECODE key 2118.
- ormond-arran-1678: Carte MSS copy route; group 9 = 58 in both prints vs 57 in ciphertext.txt (flagged, not repaired).
- sp90-raby-1704: SP 87/2/37 f.68 possible clear copy (premise risk) first.
- moray-wood-1568: parked on ASKS 103 (no.804 test pre-registered, 20ba38af). na-schonenberg-1678-1716: parked (body
  N0). fr3986-nevers-revol-1593: parked on ASKS 102 (owner's sign sort). blitz-ciphers: parked pending new material.
  huntington-luzerne-destouches-1781: found-solved.
- More gate-fix batches: account-4's own earlier WEBCHECK targets still failing `tools/intake_gate_check.py` (list them
  with the loop in STATUS.md check-in 24's method; GF4-BATCH1-4 did 12).

## Lessons from parent 2 (2 Oct 21:00 -> 3 Oct 01:05, about 110 workers)
- Workers on own targets finish in 5-15 minutes; 15-minute check-ins keep slots near 6.
- A verifier's shelfmark search (VERIFY-SURINAME-2061) found de Leeuw 1997 after eight passes searched by catalogue
  words; that led to the period key the same hour. Premise and print checks search interior phrases and shelfmark
  strings, never only incipits (VERIFY-CLINTON: 2380 was in print in 1871).
- Pre-register candidate lists and thresholds in a commit before scoring (suriname GAPS10/11/14, moray no.804).
- A sign inventory with pass agreement below ~90 pct goes to the owner's sign sorter (fr3986 ASKS 102, esp318), not a
  third machine pass.
- file_shrink_guard.py crashes on .jpg paths: pass text paths only (flagged, not fixed).
