# Research director, wave 21 (18 Oct 2026, 13:1x UTC by date -u): program C/A, the Haldimand-service cypher pool

Common tail: .claude/briefs/README.md applies (ROOM claim/done with the usage phrase, wall-clock box, no AskUserQuestion, never a dollar
figure for yourself, `tools/experiment_log.py --check`). The job ends with the six research-director questions in one line each.
Report what was found and where it was not found; no novelty class (rule 10). Never promote, never solve.

## JOB HALD-POOL (account 4; Sonnet 5; cap USD 4; box 50 minutes; hosts: archive.org (djvu text of Brymner's Reports on Canadian Archives 1884-1889 and their be-api full-text search; at most 30 requests), web search; Price: vision calls: 0 x USD 0 = 0)

Why now: ciphers/sherwood-cossit-1781 showed that Haldimand-service cypher on the free LAC Haldimand reels (heritage.canadiana.ca series
oocihm.lac_mikan_105513) can be read once the code book is known: Entick, *New Spelling Dictionary* (1781), page and printed column line
(ciphers/sherwood-cossit-1781/decode_entick.py, book/entries_image.tsv). Leighton and Matyas 1985 (snippets) also name a Haldimand
page.column.line+1 Entick form and a code-list (word/sublist) form; ciphers/pro3055-clinton-1779 holds the 1778 title-page book key.
SCOUT-KEYS (QUEUE.md, 17 Oct) saw the other Brymner cypher mentions only as "single news items with no key beside them" -- with the key
family in hand that is no longer the bar. Question: how many Haldimand-service cypher items survive on the reels, in which system, and
which are unread?
Scripts read, models judge (Usage 2): no page images in this job.
1. From the djvu text of each Report 1884-1889 (Haldimand calendars), split the entries by script and keep every one with
   cypher/cipher/cyphers/decypher/"in figures"/"numbers" (log the regex), with its B-volume, page, date, correspondents and Brymner's words.
   Write harvest/HALD-POOL-2026-10-18.tsv.
2. Classify each row from Brymner's words only: cipher text present / only mentioned; decipherment or translation beside it (yes/no/
   unknown); channel (Vermont negotiations, Clinton-Haldimand, Indian Department, Montreal/Quebec agents, other); likely system if the
   words say (book, dictionary, list, title page, unknown). Map each B-volume to its BL Add MS number and reel (CHECK-SHERWOOD and
   SHERWOOD-PAGES give H-1649..H-1655 = Add MS 21804-21834, H-1736 = 21835-21838, H-1737 continues 21838; extend from the series list).
3. Prior work per row: grep this repository (ciphers/pro3055-clinton-1779, sherwood-cossit-1781), the Collections of the Vermont
   Historical Society vol. II (it prints some Haldimand cyphers "with translations": list which), Bourdeau and Aymeloglu (shallow clones),
   DECODE cache, Cryptiana haldimand.htm.
4. Rank: unread cypher text present, Entick-era (1780-1784), on a free reel, with a crib (Sherwood/Mathews summary, a reply, a plain copy)
   first. Write a QUEUE.md section "## Haldimand-service cypher pool (18 Oct 2026)" with the top rows and the next cheap test per row
   (fetch the frames, apply decode_entick.py, priced per page).
Report: rows found, how many with cipher text present and unread, top three with their test and price, five lines.
