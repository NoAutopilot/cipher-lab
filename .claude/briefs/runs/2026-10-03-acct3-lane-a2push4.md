# LANE A2PUSH4: account-2 lane orchestrator (account-3 orchestrator, 3 Oct 2026 16:3x UTC; account 2 has usage, LANE-A2PUSH3 spent)

Operating rules exactly as `.claude/briefs/runs/2026-10-03-acct3-lane-a1.md` "Pace" (lane orchestrator on account 2, Opus 5.5,
workers via create_session on account 2, source_url https://github.com/NoAutopilot/cipher-lab, model claude-opus-5-5 (Sonnet only for
pure search/check-solved jobs), ~6 live, refill within 15 min via send_later, ledger every worker from get_session, stop on five_hour
allowed_warning/rejected, then "LANE A2PUSH4 handoff" in STATUS.md and one done ROOM line). You do no solving yourself.

Split with account 1 (LANE-A1B) so the two never collide: you take NEXT-STEPS.tsv rows whose folder starts with g..z; LANE-A1B takes a..f.
Never take a folder the account-4 parent holds (its GAPS*/FT4* lines in the last 6 h; as of 16:2x UTC: decode-1411, eckert-1862,
hessen-daenemark-1672, sachsstaatsarchiv-manteuffel-1712, naf14913-rousseau-venice-1743, pollaky-1865-1875, sp54-maclean-1745,
ula-degeer-1644, fr4715-vieuville-pool, sufi-fiddle, riksarkivet-r4282-1628, sp81-stanning-1631, sp8-ehrenstein-1689, mlh-1976,
thurloe-printed, la-garde-1577, heinsius-dopff-1702, rumpf-vandebie-heinsius-1716-19, stas-waldburg-1653, hza-hohenlohe-1679,
florence-dieci-responsive, nla-heinrich-braunschweig-1519, bl-james-1669), nor any folder with a ROOM claim younger than 6 h.
Birago (birago-*, nevers-birago-*) waits on the owner's sorter: no machine passes there. Do not resume interrupted A2-* work.

Backlog, in this order:
1. WORK-QUEUE.tsv rows `queued` for account `other`.
2. Your own lane's follow-ups from LANE-A2PUSH3 (STATUS.md "LANE A2PUSH3 handoff"): lambeth-bacon-649 (Pott 1896 MS: Francis Bacon
   Society holding -- an outreach draft for the owner, no send), sp81-wroth-1596 (key-sheet copy request draft), fr15564-mercoeur-1586
   (next named step only if it is not too-short at the measured reader split).
3. `python3 tools/next_steps.py`, then NEXT-STEPS.tsv `runnable` rows g..z top-down (e.g. harley-287-1587, jan-van-nassau-1572-75,
   lodewijk-van-nassau-1573-74, matignon-mayenne-1586, pro3055-clinton-1779, sp99-wotton-1622, zeschau-seebach-1841, kaliningrad-2015,
   moustier-altars, scorpion-1991, untersberg-code, viganego-torino-1717, sanguszkow-mniszech-dunin-1714, rah-salazar-soria-sanchez-1524-28,
   na-raad-azie-1800, sp78-yorke-1749), one worker per row, the row's own named step and cost; then needs-image rows whose image route is
   documented in the CLAUDE.md host table.
Every brief: pre-register before any score, matched control (rule 3), cap and box from the per-unit rate (Usage 6), crop step as a pasted
tools/iiif_lines.py command before any vision call, "report what was found and where it was not found; do not classify novelty".
