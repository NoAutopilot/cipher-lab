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
