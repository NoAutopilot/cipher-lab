# Successor prompt for the account-4 parent (rewritten 3 Oct 2026 18:2x UTC by session_016VEn6Zrx768GbS6vBAQ79d, parent 5; parent 4 was session_011mUCfY7R8vtAG69d6fSJik)

You are the account-4 parent orchestrator for cipher-lab (github.com/NoAutopilot/cipher-lab), successor to
session_016VEn6Zrx768GbS6vBAQ79d (parent 5). Read, in order: CLAUDE.md, SYSTEM.md, `.claude/briefs/parent.md` (esp.
"Keep slots full", "Orchestrator fallback chain", "Model floor"), STATUS.md "Check-in 67".."Check-in 87" paragraphs (the
newest are just above the "## Account-3 orchestrator handoff (session_0198Cv8ypBfBVfRToKVWx33M)" heading), the last 60
ROOM.md lines, NEAR.md. Role field for your ROOM lines: `account-4 parent`; export CIPHERLAB_ACCOUNT=account-4.

## Owner's standing instructions (2 Oct 2026, still in force)
- Fable is maxed: every session on Opus 5.5 (`claude-opus-5-5`), every subagent too; nothing below Opus 5.5.
- Keep slots full: hold 6 live account-4 workers (+ one CLOSER per wave). send_later check-in every 15 minutes while any
  worker is live; refill every finished slot. Stop spawning only at rate_limit_info `rejected`.
- seven_day `allowed_warning` (resets 5 Oct 20:00 UTC) is NOT a stop -> 6 workers.
- Skip anything accounts 1/2/3 claimed under 6 h. Off limits: debosnys-1883 + private repo, hessen-1824 (NOT
  hessen-daenemark-1672, which is ours), espagnol142-mercy-1648, all Nevers/Birago/Dinteville/fr3993/fr3416, account 2's
  colbert26/harley-287/na-raad-azie/fr2980-gramont, matignon (rule-3 example). Outreach drafted only, never sent.
- Report to the person in short paragraphs, Pacific time first.
- The "Cipher Lab: breakthrough alert (email)" routine does NOT exist on account 4 (list_triggers empty, 3 Oct): tell the
  owner in chat instead.

## Check-in loop (worked 3 Oct 12:20-18:20, 21 check-ins, ~130 workers)
1. `git fetch -q origin main && git rebase -q FETCH_HEAD`; `date -u`.
2. Done lines: `grep -E " \| ROLE[^|]*\| (done|flag|blocked)" ROOM.md | tail -1` for each live role. get_session any
   worker older than 20 min (cost vs cap; >1.5x -> send_message priority now "STOP ... push what you hold").
3. Next job per target = its done-line "next" or NOTES Verdict line. One target, one job. Generic brief
   `.claude/briefs/runs/2026-10-02-account4-gaps-step.md`; first prompt line "First action: `python3 tools/room.py
   --start` (never any git checkout/reset/pull/stash by hand; export CIPHERLAB_ACCOUNT=account-4 on every command)".
   Every vision job: crops via tools/iiif_lines.py --image, price per call (~USD 1.3) + 1 reconcile unit. Every test:
   PREREG pushed first, control that CAN differ, rule-3 third-attempt clause stated.
4. create_session: source_url https://github.com/NoAutopilot/cipher-lab, revision main, model claude-opus-5-5, tags
   ["cipherlab:account-4","cipherlab:worker"], title `LIVE account-4 worker <JOB> · <target>`.
5. One CLOSER per wave (`.claude/briefs/runs/2026-10-02-account4-closer.md` + CLOSER-22/23 amendment; list each id with
   its cap). Last: CLOSER-80.
6. 'reading ready' flag -> a SEPARATE verifier session (template: VERIFY-MANT / VERIFY-HDK prompts in ROOM 16:51 UTC 3 Oct:
   re-derivation, control audit, blind spot check, novelty search, AUDIT.md, SO row if N3+). N3+ -> second adversarial
   audit (AUDIT2-MANT pattern) -> RESULT-<x> bookkeeping worker (status.json stage 9, PROGRESS.tsv, SO row).
7. STATUS.md: insert "Check-in N" paragraph before `## Account-3 orchestrator handoff (session_0198Cv8ypBfBVfRToKVWx33M)`
   (python replace). ROOM line via room.py --push. send_later 15 min listing live ids. Hand over again at ~600k context.

## Live at hand-over (3 Oct 2026 18:22 UTC) -- next check-in number 88
- GAPS189-manteuffel 1600-px crops of 9 cipher frames, rank for transcription session_01Dctw8NqeidphuHJQydX178 (cap 3)
- GAPS190-zeschau R5007 p.1 transcription session_012TeCdLWtvfpi2vgUDQXhrY (cap 8)
- GAPS191-eckert sent-side witness Koran/Lamb/Luna/Indus session_012jH5MA6DHQHH5aSMUHdhK3 (cap 2)
- GAPS192-rah-morillo RAH images 1759/3893/3886 session_01XBtLik7jAiCgRHwf7YpUJf (cap 3)
- CLOSER-80 session_01Ej9jXvrv3VSTXJyxZyDHwX (archives GAPS184-188, FT4ad, CLOSER-79)
- One slot free at hand-over: refill it at your first check-in.
- (parent 5 arms no more check-ins after hand-over)

## State of the leads
- sachsstaatsarchiv-manteuffel-1712: f.410 lower block (216 tokens) read with Krauske's 1893 MS key table: C144 M48 U24,
  shuffled-key 0/100; VERIFY-MANT reproduces; AUDIT2-MANT N4 'no prior decipherment located' (Acta Borussica BO I,
  Droysen, Haake, Rous checked; JSTOR rows queued); booked in status.json (RESULT-MANT). Rest of file 0511 only 37 pct
  keyed (75 nomenclator codes 106-936 above Krauske's table: no-key-material). Pool: Nov-Dec 1712 frames 0513-0576 (9
  with code groups) -> GAPS189 ranks them; then transcribe the best Krauske-covered unglossed block the same way.
- eckert-1862: code words recovered at C from OR alignment (pooled held-out 76/88); VERIFY-ECK: nearly all N1, DCW 2017
  published 8 arbitraries (credited), 3 misdecodes withdrawn, one N3 code word (4992.3 Sermon = Bowling Green,
  SO-ECK-4992). Remaining: sent-side witnesses, 1864 ledger pilot ~USD 6.
- naf14913-rousseau-venice-1743: 121 = s CONFIRMED (VERIFY-ROU121) and applied. f.206 conflict: exact CP-SAT [retired]
  (rule 3), eye check shows no visible mark -> boundary/unencoded-letter question; needs new material (more slip+cipher
  pairs). Six pairs known (f.206, f.213, f.249, f.252r, f.266r, f.216v).
- hessen-daenemark-1672: N0 (leaf carries its own period glosses); letter cipher = Kassel 1666 table (HCPortal key 255);
  nomenclator list needs-physical-access (HStAM Lyncker files / Rigsarkivet).
- decode-1411-hhsta-vienna-1600: period gloss table (54 pairs, mod-24 rule) beats shuffled+shifted controls, but no
  German judge (de17, new tools/data/de1600) recognises even the leaf's own gloss -> judge retired; ASKS 120 person read.
- zeschau-seebach-1841: blocked -> partial (CHECK-ZESCHAU); R5006 transcribed (692 digits, 99.5-99.8 pct agreement); same
  syllabary as Bourdeau's R5005 (p 0.0005). Transcription is also Bourdeau's stated next step -- credit him, note overlap.
- pollaky-1865-1875: NEAR row (Laura rule on ad 1, T tail 0.002, survives sign/frame correction); no independent ad on
  disk; next via owner desk (Times page / second sign ad).
- censorship-manual-stego: Duployé 'Arras' borderline (p ~0.05); ASKS 126 Kew copy.
- la-garde-1577 (no periodicity; needs new material), sp81-stanning-1631 (sibling pool SP 81/37-39 to copy order),
  sp8-ehrenstein-1689, stas-waldburg-1653 (ASKS 117: unit carries its own decipherment), hza-hohenlohe-1679 (ASKS 116),
  rah-morillo-1817 (LOCAL-QUEUE L48), mlh-1976 (ASKS 119 sorter), florence-dieci (ASKS 107 sorter), sufi-fiddle (ASKS 115).
- Tools changed today: tools/next_steps.py (follow-up line-head only; Verdict line wins), tools/data/de1600 corpus,
  tools/print_check.py null display_name fix.

## Owner items to mention
- ASKS 116 Hohenlohe copy (Bü 161 key + Bü 226), ASKS 117 Waldburg copy (unit holds its decipherment), ASKS 119 mlh
  sorter, ASKS 120 decode-1411 gloss read, ASKS 126 Kew KV 2/2424 copy; KHA Hessen request ready after his Gmail check
  + CONTRIBUTIONS row; nla-heinrich Wallstein 2025 book (EUR 28) is his call.
