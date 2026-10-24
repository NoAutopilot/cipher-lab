# Research director, wave 45 (24 Oct 2026, 04:0x UTC by date -u): LEAD-AO1 verification -- Pepys Papers (Nicholas), Magdalene College

Common tail .claude/briefs/README.md applies (ROOM claim/done with the usage phrase, wall-clock box, no AskUserQuestion, never a dollar
figure for yourself). Done line addressed for the account-4 parent. Gallica is not involved.

## JOB CHECK-PEPYSNIC (account 4; Sonnet 5; cap USD 4; box 45 minutes; hosts: archive.org (full text + djvu text of named volumes, <=20 requests), cudl.lib.cam.ac.uk (browser tool if curl 403s, <=15), www.magd.cam.ac.uk / Pepys Library pages (<=10), Google Books API (key, country=US, <=15), OpenAlex/S2 (keys, <=10), web search; one request at a time, >=1.5 s apart; Price: vision calls: 0 x USD 0 = 0)

Program C, lead verification before any scoring. SCOUT-OPEN (24 Oct, QUEUE.md "Open-route candidates", harvest/SCOUT-OPEN-2026-10-24.tsv
row LEAD-AO1) found in *Report on the Pepys Manuscripts* (HMC 1911, archive.org `reportonpepysman0000unse_f0i4`) that the Pepys Papers at
Magdalene College, Cambridge (Sir Edward Nicholas's Civil War and exile papers) hold undeciphered cipher items (report items (5) 1648 Aug 5
to the Duke of York; (303); (352); (71) "triplicate in cipher from Mr Hansnaw") beside a key register (p.308: about ten period ciphers).
Both filters look met from the catalogue text alone. Establish, in this order, and stop at the first finding that kills the lead:
1. Prior plaintext / decipherment (check-solved, .claude/briefs/check-solved.md, run by holder + shelfmark since the items are catalogue
   entries): whole-volume grep of the HMC report's djvu text for every "cipher" item with its date and correspondents; then the Nicholas
   editions -- Warner, *The Nicholas Papers* (Camden Society, 4 vols, 1886-1920; archive.org) and the Clarendon State Papers calendar
   (Ogle/Bliss/Macray, archive.org) -- for the same date+correspondent; Cryptiana (sources/cryptiana), DECODE listing cache
   (tools/decode_list.py, login-free), both solver repos by grep for "Pepys", "Nicholas", "Magdalene". Record each as searched or
   unreachable with the date.
2. Where the physical items are now and whether images exist: the Pepys Library's own catalogue (Magdalene College) and CUDL's Pepys
   Library collection; quote the catalogue record's availability flag, not a portal's "no items" (CLAUDE.md access playbook head).
   State the reproduction route (the Library's own request page, with its public address read from the page and the date).
3. Only if 1 finds no plaintext and 2 finds the items: `python3 tools/prior_work.py pepys-magdalene-nicholas-ciphers` and
   `python3 tools/scout_rubric.py` on the pool (estimate signs from the report's item descriptions; a pile of several letters in one
   key family counts as a pool, CLAUDE.md pipeline 3 selection rule).
Write `ciphers/_triage/pepys-magdalene-nicholas-ciphers.md`: status word (`open` / `found-solved` / `blocked`), the check-solved sentence
naming each edition and the pages or full-text search actually read, the holder record and flag, the route, the rubric score, and
"## Premise check" (CLAUDE.md pipeline 2). Never promote to the board; never create a ciphers/<slug>/ folder; never decode. Append a
one-line pointer under QUEUE.md "Open-route candidates" LEAD-AO1. Report: verdict, the one finding that decided it, hosts and request
counts, five lines.
