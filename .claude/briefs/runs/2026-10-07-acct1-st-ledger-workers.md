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

---

# Wave 2 (written 7 Oct 2026 22:3x UTC, after LS-PRE): read only the filtered entries

LS-PRE's `ciphers/eckert-1864/entries-mssEC19.tsv` ranks 893 segments; the lane picked priority-1 rows with words >= 50, `or_cov` <= 3
(no Official Records hit and a low near-hit cover; LS-PRE's calibration: recall 0.90 for entries of 60+ words, 0 false hits of 14),
dated 1864, non-headquarters addressees (Horner at New York, Sheldon at Fort Monroe, Mason, Sampson, McCaine in the Valley).
The filter is a ranking, not a verdict: some will still turn out printed.

## LS-R1 / LS-R2 (Opus 5.5, solver): read the listed entries with the period key

Entries (pointer/page/entry_on_page in entries-mssEC19.tsv; your IDs are fixed so the two of you never collide):
 LS-R1 (cap $11, box 120 min): 8934/42/1 E21, 8949/57/2 E22, 8955/63/1 E23, 8964/72/0 E24, 9023/131/1 E25, 9053/161/1 E26,
   9091/199/1 E27, 9091/199/2 E28, 9115/223/1 E29 (the long one last).
 LS-R2 (cap $9, box 110 min): 9051/159/1 E30, 9051/159/2 E31, 9054/162/1 E32, 9055/163/0 E33, 9056/164/0 E34, 9057/165/3 E35,
   9060/168/1 E36.
 If an entry is in Cipher No. 2 (header "(No 2)", Beckwith-style punctuation words), read it with key-no2.md into ciphertext-no2.txt
 instead, IDs N2-BG.. (LS-R1) or N2-BP.. (LS-R2), as the D4-E5 section did. If it is in the old vocabulary, key-no9.md / O9-AH.. (R1),
 O9-AP.. (R2). If none of the three keys reads at least 80% of its code-word tokens, stop that entry, record "key not in hand" with the
 counts, and go to the next -- do not guess.
Method exactly as D4-E5 (NOTES.md section "## D4-E5"): 2400 px IIIF image of the pointer to scratch
(`hdl.huntington.org/digital/iiif/p16003coll11/<pointer>/full/2400,/0/default.jpg`), strip crops with tools/iiif_lines.py (command
pasted in your NOTES section), read the crops yourself (no subagent), the volunteer text in ciphers/eckert-1864/sources/mssEC19/p<pointer>.json
as second witness; list every word where they disagree and which you took. Append the block to ciphertext.txt in the format of its
header comment (### E<n> | Page | pointer | date, addressee (operator)), `python3 decode.py --write` then `--check` exit 0; grade per token
(the decoder counts H/C; add any I/M by hand as earlier blocks do). After decoding, locate it in print: OR by date and correspondent (the
LS-PRE identifiers; djvu fetched once per volume), ORN, Lincoln Collected Works / Papers of U. S. Grant (Google Books API with key and
country=US), IA full text with 2-3 decoded phrases; record per entry where it was found and where it was not. Mark the row in
entries-mssEC19.tsv `already_read` with your ID.
Shared files: ciphertext.txt and reading.md are touched by both of you. Fetch + rebase immediately before each push; on a conflict keep
both sides' blocks in ID order and regenerate reading.md with `decode.py --write` (never hand-merge the derived block). Push after
every two or three entries, not only at the end.
Write a section "## LS-R<k> (7 Oct 2026, account 1, for LANE ST-LEDGER)" in NOTES.md: per-entry table (ID, date, from/to in the
decoded plain, H/C/I/M, found in print where / not located in what), the crop commands, requests per host. Update the Verdict line's
"cheapest next" (prepend; keep the older text). Price: ~1.1 per entry; stop before an entry that would cross 80% of cap or box.
Flag the batch for a verifier in ROOM. Report what was found and where it was not found; do not classify novelty.

## LS-V1 / LS-V2 (Opus 5.5, verifier; cap $6, box 75 min each) -- spawned by the lane after LS-R1 / LS-R2 finish

Separate session from every solver of the batch. CLAUDE.md "Verifier brief (template)" scoped to LS-R<k>'s entries. Re-derive with
`decode.py --check` (and decode_no2/no9 if used); spot-check two entries' strip crops against the IIIF image; for entries the solver
located in print, confirm the page by script and class N1 (a check, not a search). Spend the rest on the not-located entries: full search
per entry (OR by date and correspondent +/- 3 days, ser. III, ORN, sender/recipient papers -- e.g. Seward/State Dept for Horner's New York
traffic, Sheridan/Valley campaign for McCaine --, PUSG, Lincoln CW, Huntington full text, IA, Google Books, OpenAlex/S2/CORE, JSTOR-QUEUE
rows in both families). N-class + key `period` + text known/unknown + depth (rule 4a, D-level, depth_pct, one true sentence for D2+).
Append "## AUDIT (LS-V<k>)" to AUDIT.md; status.json result rows for N3+ entries only, one per entry in the format of the 7 Oct eckert
rows (rebase first); SECOND-OPINIONS-QUEUE.tsv row per N3+ entry in this session; correct any over-claim in the solver's section.
`tools/depth_check.py` passes for the rows you add. Do not decode other entries.

---

# Wave 3 (written 8 Oct 2026 00:2x UTC)

Wave 2 results: LS-R1 read E21-E29; LS-V1 classed E21, E23, E26, E27, E28 N3 (key period), E29 N2, E22/E24/E25 N1 -- 5 of 9 at N3
from the filter, against 0 of 14 in the last two unfiltered chunks. LS-R2 and LS-R2b both ended without a commit (E30-E36 are parked,
not read; see NOTES.md "## ST-LEDGER parked entries").

## LS-R3 (Opus 5.5, solver; cap $11, box 120 min) -- same section as LS-R1 / LS-R2 above, these entries and IDs:
 9110/218/2 E37, 9045/153/1 E38, 9045/153/2 E39, 9046/154/0 E40, 9097/205/2 E41, 8945/53/1 E42, 8975/83/0 E43, 9124/232/2 E44,
 9129/237/3 E45, 9130/238/1 E46 (Horner at New York, Sheldon at Fort Monroe, Sampson at Baltimore; no other worker holds them).
 No. 2 entries go to N2-BG..; old vocabulary to O9-AH... Commit and push after the first two entries. If a tool call is refused by
 your permission mode, do not work around it: push what you have, say which call was refused in ROOM, and stop.

## LS-V3 (Opus 5.5, verifier; cap $6, box 75 min) -- the LS-V1 / LS-V2 section above, scoped to LS-R3's entries.
