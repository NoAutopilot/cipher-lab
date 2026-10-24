# Research director, wave 48 (24 Oct 2026, 08:0x UTC by date -u): SP 106/6 key, second DECODE pass; SP 84/166-171 pool intake check

Common tail .claude/briefs/README.md applies (ROOM claim/done with the usage phrase, wall-clock box, no AskUserQuestion, never a dollar
figure for yourself). Done lines addressed for the account-4 parent. Gallica is not involved. Two jobs, two workers, independent.

## JOB DECODE-KEY32B (account 4; Sonnet 5; cap USD 3; box 30 minutes; hosts: de-crypt.org only, ONE browser login with tools/decode_browser_login.js, <=16 fetches, >=2 s apart; Price: vision calls: 0 x USD 0 = 0)

Continuation of DECODE-KEY32 (ciphers/sp84-fuente-1662/NOTES.md "## DECODE fetch (DECODE-KEY32, 24 Oct 2026)" and
sources/decode/2026-10-24-sp106-6-keys/candidates.tsv): id 432 is ruled out; ids 509 (3 pp), 506 (1 p, "the same cipher" as 509) and 497
(2 pp) are the unopened French candidates for TNA SP 106/6 nos. 31, 32, 35 (Tomokiyo's structural descriptions are quoted in that
NOTES section: no. 32 an alphabetical encoding table with person/town/country sequences; nos. 31/35 numbers to 999 in nine mark classes).
1. One login; fetch RecordsView and the full-size page images for 509, 506, 497 (`--guess-fullsize`, `--max-files` sized for 6 pages
   of thumbnails + full images = 12); if the budget and box allow, the next two French candidates by rank in candidates.tsv.
2. Images stay in your scratchpad (sources/decode/NOTES.md: raw DECODE images are not committed); commit per record only
   manifest.json (url, bytes, sha256, content-type, pixel size) and a README.md with your at-a-glance verdict against the fingerprint
   above -- `match no. 32` / `match no. 31 or 35` / `no match` / `undecided` -- and the one visual reason (table layout, numeral
   ranges, mark classes, endorsement text if legible). No transcription, no reading, no key.tsv.
3. Update candidates.tsv's plausibility_note for every record opened and append "## DECODE fetch, second pass (DECODE-KEY32B, 24 Oct
   2026)" to ciphers/sp84-fuente-1662/NOTES.md. Never print credentials; scrub the account name from saved pages.
Report: per record match/no match/undecided with the reason, request count, five lines.

## JOB CHECK-SP84POOL (account 4; Sonnet 5; cap USD 4; box 40 minutes; hosts: archive.org (advancedsearch + djvu text, <=20), Google Books API (key, country=US, <=10, one retry on 503 then log), discovery.nationalarchives.gov.uk details endpoint (<=20), tools/decode_list.py cache (no network); Price: vision calls: 0 x USD 0 = 0)

Check-solved (.claude/briefs/check-solved.md) by holder and shelfmark, run before any folder exists, for the pool in
harvest/C-FOLLOW-2026-10-24-sp84-gloss.tsv: 10 undecoded letters (SP 84/166 ff.19, 85, 106, 108, 167, 184, 188, 213; SP 84/168 f.60;
SP 84/171 f.123; Wickfort and De Bacquoy to Williamson, Nicholas, Bennet; 1660-63) and their 8 PRO-decoded siblings in SP 84/165
(ff.13, 105, 106, 184, 190, 192, 213, 214; key SP 106/6 no. 32).
1. Editions: Calendar of State Papers Domestic, Charles II, 1660-61, 1661-62, 1663-64 (archive.org; find the volumes with
   advancedsearch, fetch the djvu text once each, whole-volume grep for Wickfort/Wicquefort, Bacquoy/Bacquoij, "undecoded",
   "in cipher", and each letter's date and folio); say for every one of the 18 items whether the calendar prints the decoded
   text, summarises it as cipher, or omits it, with volume and page. The PRO decodes (the 8) are expected to be printed there as
   plaintext -- confirm or deny per item. Then CSP Venetian/Foreign do not cover SP 84 (note it) and Cryptiana chauran.htm
   (sources/cryptiana/web/, on disk) for every mention of these folios.
2. Solver repositories (sources/cyphersolver*, a shallow clone of aaymeloglu/unsolved-ciphers grepped only) for Wickfort, Bacquoy,
   "SP 84/166", "SP 84/168", "SP 84/171"; DECODE listing cache (tools/decode_list.py) for any SP 84 record.
3. Discovery details endpoint for each of the 10 undecoded items: quote the note field, `digitised`, and `accessConditions`.
Write ciphers/_triage/sp84-wickfort-bacquoy-1660-63.md: status word (`open` / `found-solved` / `blocked`), the check-solved sentence
naming each edition and the pages or full-text search actually read, a per-item table (reference, folio, date, correspondents, calendar
treatment with page, PRO-decoded yes/no), "## Premise check" (CLAUDE.md pipeline 2), and the estimated cipher-sign count of the pool from
the calendar's descriptions. Never promote, never create a ciphers/<slug>/ folder, never decode. Report: verdict, how many of the 8 PRO
decodes are in print, how the 10 undecoded items are treated, hosts and request counts, five lines.
