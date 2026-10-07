# ST-LEDGER worker brief (account 1, LANE ST-LEDGER, session_016rC9SvHBi7gsLuXBh6whmZ; written 7 Oct 2026 21:4x UTC)

Parent round: .claude/briefs/runs/2026-10-07-acct3-steam.md, section ST-LEDGER (read it). You are one of the workers
named below. Read your own section, CLAUDE.md, ciphers/eckert-1864/NOTES.md sections 2-5 and the last four "## D12-E"/"## D4-E5"
sections (if your job touches Eckert), and the common tail in .claude/briefs/README.md.

Why this lane exists: the counted results (N3+ and D2+) from eckert-1864 came from entries NOT already printed in the Official
Records (OR): staff, quartermaster and operator telegrams (Augur, Howell, the QMG, Stanton to Dana). The last two reading chunks on
mssEC 19 (D4-E5, D12-E3) read 14 entries and every one was already in print (N1) -- the key works, the selection is what fails.
So this lane filters first (which entries are NOT in the OR, by their plain words, before anyone decodes), then reads only those.

0. `python3 tools/room.py --start` (if it fails to push from a detached HEAD: `git push origin HEAD:main; git checkout -B main
   HEAD`); `date -u`; read the last 30 ROOM.md lines; claim with `python3 tools/room.py "<ID> worker (account 1)" '<claim, cap,
   box end, for LANE ST-LEDGER>'` (single quotes). Halfway line at half your box; done line at the end "for LANE ST-LEDGER".
1. Good-citizen rule: one host at a time, >=1.6 s apart for hdl.huntington.org and archive.org, a few hundred requests per host
   per session at most, stop a host on 429/403/challenge after one retry. Images to scratch unless the brief says commit; crops with
   `tools/iiif_lines.py --image <file> --out <dir> ...` (paste the command); never hand a full page to a subagent; at most 4
   subagents at once.
2. Grading (rule 4) as eckert-1864 always has: H from the period key book (key.md = mssEC 41 Cipher No. 1; key-no2.md = mssEC 47
   Cipher No. 2; key-no9.md = mssEC 67), C from a clerk's form or a print, I inferred, M uncertain.
3. Close: push by explicit path (`python3 tools/room.py --push <paths>`), `python3 tools/file_shrink_guard.py` on every pre-existing
   file you touched (paste output), `python3 tools/gaps_check.py eckert-1864` if you touched its NOTES.md. Report what was found and
   where it was not found; do not classify novelty (rule 10); never the words solved, cracked, novel, first, new for anything this
   project did. Never call AskUserQuestion; never print credentials; never name the owner; read `date -u` before writing any time.
   Requests per host in the done line.
4. Cap and box are yours below. Stop before starting a unit that would cross 80% of either; the box is also a minimum.

---

## LS-SCOUT (Sonnet 5.5, cap $8, box 90 min): one key, many entries -- where else?

Steam brief step 1. Desk scout only: never decode, never open a target folder, never promote to the board.
Find digitised cipher ledgers, letter-books, telegram books and cipher registers where a key is held or printed alongside and
many entries are still unread. Start from (in this order, stop a source after ~15 minutes if it yields nothing):
 (a) the Eckert papers beyond mssEC 18/19: which mssEC volumes 1-36 are telegram ledgers (sent/received), their date ranges, which
     cipher book of mssEC 37-76 matches each (Tomokiyo sources/cryptiana/web/civilwar1.htm; the Huntington CONTENTdm collection
     p16003coll11 via the documented `CISOSEARCHALL^TERM^all^and` route and `dmGetItemInfo`); count pages with volunteer text;
     eckert-1862 folder already exists -- say what it covers and leaves;
 (b) US State Dept / War Dept telegram or letter books on loc.gov (JSON `?fo=json`) or NARA (IIIF route in CLAUDE.md host table),
     where a code book of the same office is digitised (e.g. the State Dept's 1867 Red Book / 1876 Pine/Blue code; check KEY-OFFICES.tsv
     and KEY-DESIGN.tsv first for keys already in the repo);
 (c) DECODE records (tools/decode_list.py, login-free) whose type is key and that have sibling ciphertext records of the same
     collection -- list the pairs;
 (d) Habsburg / Venetian dispatch registers for which Tomokiyo prints a key table (sources/cryptiana) -- name register + key page.
 Do NOT scout the Thurloe State Papers (LANE ST-REBUILD has them) nor anything in KEYHUNT-2026-10-07.tsv already (ST-ACCESS has those).
Output: `LEDGER-SCOUT-2026-10-07.tsv` at repo root, columns: ledger, holder+shelfmark, url (catalogue record or IIIF manifest),
digitised (y/n/partial + how verified), key_in_hand (repo path or url of key; "printed in X p.Y"; "no"), entries_est, unread_est,
printed_share_guess (is the plaintext likely in a printed series such as the OR? name it), rank_score = unread_est x key(1/0.5/0) x
digitised(1/0.5/0) x (1 - printed_share_guess), note. Plus a 10-line `LEDGER-SCOUT-2026-10-07.md` naming the top 3 and why. Check
each top-3 ledger against the steam brief rule 1 sources only far enough to say "not found decoded in <sources>" -- a full check-solved
is a later worker's job. Report what was found and where it was not found.

## LS-PRE (Sonnet 5.5, cap $7, box 150 min): which mssEC 19 entries are NOT already in the Official Records?

Tooling + filter. Script-first; no model reads pages.
1. `tools/huntington_transc.py` (new shared tool, --help, offline test in tools/tests/ on a saved JSON fixture): given a CONTENTdm
   collection alias and a pointer range, fetch `dmGetItemInfo/<alias>/<pointer>/json` (field `transc`, plus `title`), one request every
   1.6 s with a browser UA, cache to a directory (skip pointers already cached), write one JSON per pointer. Route documented in
   ciphers/eckert-1864/NOTES.md D4-E5 section. mssEC 19 = object 9302; find the page pointer range from the compound object's
   `dmGetCompoundObjectInfo` (or the known page n = pointer - 8892 stretch -- verify at both ends; there are 415 page images).
   Cache for mssEC 19 committed under `ciphers/eckert-1864/sources/mssEC19/` (text JSON only, about 1 MB; no images).
2. Segment every page's volunteer text into entries (header line with "Washn"/"Wash'n"/a date and time, addressee line, body,
   signature). For each entry: page, pointer, index on page, header text, addressee, signature/sender in clear if any, body word count,
   counts of Cipher No. 1 / No. 2 / No. 9 marker words (the same three vocabularies no2-candidates.tsv used: k1/k2/k9 columns -- reuse
   that script logic if it is in the folder; else build from key.md, key-no2.md, key-no9.md word lists), and the longest runs of
   ordinary English words (the ledger is in reading order; code words replace names and key terms only).
3. OR check before decoding: fetch once the IA `_djvu.txt` of OR ser. I volumes covering Jan 1864-Dec 1865 (vols 32-34, 35-46 all parts,
   47-49, 51-53 as identified by IA advancedsearch `title:(war of the rebellion) AND volume`; keep the identifier list in the TSV header
   or a sidecar file this time), ser. III vols 4-5, and the ORN ser. I vols 9-12 if cheap; to scratch only. For each entry, normalise
   and search 3-5 of its longest plain-word runs (5+ words) plus date+addressee; record `or_hit` = vol:part:page-ish (or the IA
   identifier + offset) when a run matches, `none` otherwise. Calibrate on the 65+ already-read entries (ciphertext.txt E1-E20,
   ciphertext-no2.txt, ciphertext-no9.txt): report how many of those known-printed entries your check finds (recall) and how many
   known-not-located ones it wrongly hits (false hits) -- write both numbers in the TSV header. If recall < 0.7, say so and still write
   the file (it is a ranking, not a verdict).
4. Output `ciphers/eckert-1864/entries-mssEC19.tsv`: pointer, page, entry_on_page, header, addressee, sender_clear, words, k1, k2, k9,
   cipher_guess (1/2/9/clear/mixed), or_hit, already_read (E/N2/O9 id if read; match by pointer + header), priority (1 = cipher entry,
   no or_hit, not read, sender/addressee not Halleck-Grant-Lincoln-Stanton-to-army-commander; 2 = cipher, no or_hit; 3 = the rest).
   Also one short section "## LS-PRE (7 Oct 2026)" appended to ciphers/eckert-1864/NOTES.md: counts by priority and cipher, the
   recall/false-hit calibration, identifiers used. Do not decode anything. Do not edit no2-candidates.tsv except to add nothing.
