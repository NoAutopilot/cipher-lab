# ST-LEDGER-4 worker brief (account 1, LANE ST-LEDGER-4, session_015WegULpZSVGVcFH1h999mf; written 8 Oct 2026 13:5x UTC)

Parent round: .claude/briefs/runs/2026-10-08-acct3-sibs-ledger3.md, section ST-LEDGER-4 and its "Common to both lanes" list (read
both). Method, reader steps and the verifier sections are those of .claude/briefs/runs/2026-10-08-acct2-st-ledger3-workers.md (and
the briefs it cites) unless changed here. Read CLAUDE.md, the LANE ST-LEDGER-3 handoff in STATUS.md, ciphers/eckert-1864/NOTES.md
"## LS-PRE", "## LS3-R9" and AUDIT.md "## AUDIT 2 (second adversarial, AUD2-LS3-B)" first. Every ROOM line ends "for LANE ST-LEDGER-4".

Intake gate (pasted 13:5x UTC): `eckert-1864: partial (line 3) -- edition/page or full-text-search citation found within 6 lines` (exit 0).

Why this lane starts with a filter, not a reader: round 3 read 8 entries to N3 and second audits lowered 5 of them to N1/N2. The reader's
pre-filter searched OR ser. I only; the misses were in OR ser. III vol. 4 (N2-BP), in the Huntington's own public transcription of a
sibling or of the entry itself (E70, E74, E86), in the press (O9-BC), and in a same-leaf sibling telegram (E81/E83/E84, 9858). A reader
costs ~0.55 per entry and a verifier ~0.6; filtering first is cheaper than reading entries that are already in print.

Common points for every worker: `date -u` before any time; ROOM claim (box end time) first, a halfway line, a done line; commit and push
every two units, never hand a step off; stop before a unit that would cross 80% of cap or box; one request at a time per host, >= 1.6 s
apart on hdl.huntington.org and >= 1.5 s on archive.org, stop a host on 429/403 after one retry; report requests per host; do not commit
OR djvu text, page images or bulk caches (scratch or sources/ia-fulltext/print-check/ only); file_shrink_guard before the final push;
`tools/gaps_check.py eckert-1864` after writing NOTES. Never call AskUserQuestion. Rule 10 wording only.

---

## PF4 (Sonnet 5.5, worker; cap $4.5, box 100 min): the three-part pre-filter over the unread 1864 pool, no reading
Pool (paste the selecting script's output count): rows of ciphers/eckert-1864/entries-mssEC19.tsv with `already_read` blank, pointer
< 9149 (1864), and either (i) `cipher_guess` 9 (any priority; about 5), or (ii) `cipher_guess` 2 with priority 1 or 2 (about 37), or
(iii) `cipher_guess` 1 with priority 1 or 2 (about 73). Order: (i), then (ii), then (iii), lowest `or_cov` first within each.
For every pool row, three checks, each written as its own column:
(a) **Print, widened.** Add to the LS-PRE plain-token check (entries_mssEC19.py; add an option rather than a private copy if it needs
    one) OR ser. III vol. 4 (IA `cu31924079575373`) and vol. 5 (`cu31924079575381`) and ORN ser. I vols. 11-12 (find the IA identifiers
    with `_djvu.txt`; log them); then for each row one or two quoted phrases (4-6 consecutive plain words, the rarest) through the IA
    full-text API (`be-api.us.archive.org/fts/v1/search`, no identifier) -- record the hit identifiers, not page numbers (its page_num
    is not a locator). A hit names the volume.
(b) **Huntington full text.** CONTENTdm `CISOSEARCHALL^TERM^all^and` on p16003coll11, sixth path segment 1 (CLAUDE.md access playbook,
    Huntington row), for one or two distinctive plain words of the row (a surname, place or rare noun; two ANDed if one is too common).
    Any hit other than the row's own pointer: read its `transc` once (`dmGetItemInfo`) and record pointer, volume title and whether it
    states the row's substance in clear (y/n/unsure). Also read the row's own `transc`: an entry mostly in clear is N1-likely (E74).
(c) **Same leaf and neighbours** (offline, sources/mssEC19/p<pointer>.json): entries on the same page or +/- 1 page with the same
    addressee or the same header time, or sharing >= 3 rare plain tokens; mark `dup:<pointer/entry>` and whether that sibling is
    already read or in clear.
Verdict per row: `clean` (no hit in a, b, c), `print-likely` (a), `clear-sibling` (b), `dup` (c). A row may carry several.
**Known-answer control, before the pool (rule 3, a control that can fail):** run the same three checks on the 12 round-2/3 entries whose
audits settled the answer: lowered by print or clear copy -- N2-BP, E70, E74, E76, E83, E86, O9-BC, E77, O9-AL; held N3 by two audits --
E78, O9-BB, O9-BA (look up pointer and the audit's source in AUDIT.md). Report recall (lowered entries flagged) and false flags (held
entries flagged), both counts. If recall is under 5 of 9, say which check missed and fix it once before the pool; do not loop.
Huntington budget: at most 250 requests this session (control first); if the pool would exceed it, stop at the boundary of a group
and list the unchecked rows. archive.org at most 250.
Output: ciphers/eckert-1864/prefilter-ls4.tsv (pointer, page, entry, cipher_guess, priority, words, or_cov_widened, print_hits,
hunt_hits, hunt_clear, leaf_sibs, verdict) and the script that writes it (`prefilter_ls4.py`, re-runnable offline from its caches with
`--offline`). NOTES section "## PF4 (8 Oct 2026, account 1, for LANE ST-LEDGER-4)": the control numbers, the counts per verdict per group,
and the clean rows listed by group in the order a reader should take them. No decoding.

---

# Wave 2 (written 8 Oct 2026 15:0x UTC)
PF4 done (commit 9c07c7c7; NOTES "## PF4"): 115 pool rows -> 79 clean (group 2 No.2: 25; group 3 No.1: 54), group 1 (No. 9): 5 of 5
print-likely, so the No. 9 remainder of mssEC 19 is not read further. Control: recall 5 of 9, false flags 0 of 3. The four misses
(E70, E74, E76, E86) are entries whose body is already in clear, in order, in their OWN Huntington transcription -- no script check saw it.

## Readers LS4-R2a and LS4-R1a (Sonnet 5.5, solvers; cap $6 each, box 110 min each): the first ten clean rows of each group
- LS4-R2a: group 2 (Cipher No. 2, key-no2.md, decode_no2.py) in PF4's order: 8887/0 8915/1 8988/1 8902/0 9024/1 9057/2 9065/2 9067/0 9125/1 9126/0
- LS4-R1a: group 3 (Cipher No. 1, key.md, decode.py) in PF4's order: 9048/0 9097/0 9123/3 8965/1 8967/1 8996/1 9003/2 9030/0 9047/1 9049/2
Method: the LS3-R9 / LS3-R18 reader method of .claude/briefs/runs/2026-10-08-acct2-st-ledger3-workers.md (lane points, book per entry by
vocabulary share AND header label/time word, matched control = the other two books + a meaning-shuffled copy of the chosen book, IDs taken
after fetching, page images fetched once with crops cut by `tools/iiif_lines.py --image <file> --out <scratch dir>` -- paste the command --
read from the crops, volunteer text as second witness), with these additions:
0. **Step 0, own transcription (PF4's control miss), before any decoding:** read the row's own transcription (sources/mssEC19/p<pointer>.json).
   If the body reads in order as English and only names, times or a signature are code words, record "N1-likely: clear in the Huntington's
   public transcription (pointer P)" and do not decode it. Also skip PF4's weak flags: 8902/0 and 9125/1 carry a `u` Huntington hit -- read
   that hit's transcription first (prefilter-ls4.tsv `hunt_hits`) and skip the row if it states the substance.
1. A row PF4 called clean is "not found in what was searched" (its list), never unprinted. After decoding, one quoted-phrase pass of the
   DECODED plain text through be-api full text (one or two phrases per entry) before you file it -- the decoded words are what print carries.
2. A row that turns out to be another book than its group goes to that book's file under its next free ID (as LS3-R9 did).
3. Host share: the other reader works the same hosts at the same time. Keep >= 3 s between your own hdl.huntington.org requests and at most
   40 there; fetch your ten pages' images in one pass at the start, then work offline.
4. Push every two entries. Unit ~0.55 per entry; stop before an entry that would cross 80% of cap or box.
NOTES sections "## LS4-R2a (8 Oct 2026, account 1, for LANE ST-LEDGER-4)" / "## LS4-R1a (...)", with the per-entry table (row, ID, book,
three shares, clause counts chosen vs controls, H, step 0 and print result), Remaining gaps and Escalation, gaps_check after.
Report what was found and where it was not found; do not classify novelty.
