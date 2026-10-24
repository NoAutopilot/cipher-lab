# Research director, wave 46 (24 Oct 2026, 05:2x UTC by date -u): program-C follow-ups from SCOUT-OPEN and CHECK-PEPYSNIC

Common tail .claude/briefs/README.md applies (ROOM claim/done with the usage phrase, wall-clock box, no AskUserQuestion, never a dollar
figure for yourself). Done line addressed for the account-4 parent. Gallica is not involved. Three small questions, one worker, in order;
stop at the box or the cap whichever comes first and say which questions were answered.

## JOB C-FOLLOW (account 4; Sonnet 5; cap USD 3; box 30 minutes; hosts: discovery.nationalarchives.gov.uk API (<=25 requests), archive.org full text and Google Books API (key, country=US) through tools/print_check.py (<=30 calls total), web search (<=6 queries); one request at a time, >=1.5 s apart; Price: vision calls: 0 x USD 0 = 0)

1. **Which TNA piece carries the "Decoded by P.R.O." gloss.** SCOUT-OPEN (QUEUE.md "Open-route candidates", 24 Oct) wrote that most of
   SP 84/165's undecoded-cipher items say "Decoded by P.R.O. For key see SP106/6 no.32"; the parent's own Discovery check (3 requests,
   ciphers/_triage/pepys-magdalene-nicholas-ciphers.md, parent note) found 0 such items in SP 84/165. Query the Discovery API for
   "Decoded by P.R.O." and for "SP106/6" (quoted, no series filter -- the series filter is broken), list every SP 84 item that carries
   the gloss with piece/item, folio, correspondents, date, and separately every SP 84/166, 168, 171 item that says "Undecoded cipher"
   without it (the scout named 9: 166/7,41,51,52,71,81,84,98; 168/26; 171/55). Write the two lists to
   harvest/C-FOLLOW-2026-10-24-sp84-gloss.tsv and a dated correction paragraph under QUEUE.md "Open-route candidates" naming which
   piece the gloss is really on. A PRO-decoded item is known text (key application at best); an undecoded item with SP 106/6 no.32 on
   file is a key-assisted candidate once imaged -- say which bucket each item falls in, nothing more.
2. **Print check on the Pepys items.** `python3 tools/print_check.py` is per target folder; since no folder exists, run its archive.org
   and Google Books calls by hand (the same endpoints, CLAUDE.md access playbook 3, `country=US`, key from the environment, never
   printed) for the phrases "triplicate in cipher", "Hansnaw", "Hanshaw" + 1648 + cipher, "Fanshaw" + "triplicate", "Letters in
   ciphers from The King", and "Keys of ciphers and letters"; record hits (title, year, page/snippet) in the triage file under a new
   "## Print check (C-FOLLOW, 24 Oct 2026)". A "no hits" line is a search result, never a novelty verdict (rule 10).
3. **Heathcote (Conington Castle) / Fanshawe papers: current holder.** LEAD-AO2 (same QUEUE section) rests on HMC 1899's Heathcote
   report; the papers were private in 1899. Web search and the TNA Discovery "record creators / other archives" entries for "Fanshawe
   family" and "Heathcote of Conington": name the holder today (a record office, a museum, a sale), the catalogue reference and its
   availability flag quoted from the holder's own record if one is found; write it to ciphers/_triage/heathcote-fanshawe-1659.md with a
   status word (`open` / `blocked` / `found-solved`) and the one sentence that decided it. Never promote, never create a ciphers/<slug>/
   folder, never decode.
Report: three answers in three lines, request counts per host, two more lines.
