# SCOUT-BOURDEAU-WEB: Bourdeau's public Unsolved Catalogue diffed against our queue (account 1, Sonnet, cap USD 3, box 60 min)

Written 9 Oct 2026 22:4x UTC by date -u by the orchestrator (account-4), session_012sGNgiddCpz4QUhQsMyoPU, on the owner's question at
22:3x UTC ("Bourdeau has a target list on his website ... have we ever taken a look at those as targets?"). Snapshot on disk:
sources/cyphersolver-site/catalogue-2026-10-09.html (dbourdeau.github.io/cyphersolver/catalogue.html, fetched 9 Oct 2026 21:4x UTC; his text
is CC BY 4.0: cite, never copy into a target folder). The orchestrator's quick cross-match: 62 rows; 38 of the top 60 already in QUEUE.md,
CATALOG.md or a ciphers/*/NOTES.md head; 22 never queued. The 26 Sept scout read his on-disk CATALOGUE.md (194 rows), not this scored web view.

Job (scout rules: CLAUDE.md Pipeline 1; never promote, never solve; tools/scout_rubric.py for the score; the outside-the-frame rule in
.claude/briefs/README.md): parse every row of the snapshot (priority, date, item, shelfmark, DECODE/Gallica links, his status, his "Verify
first"); match each against QUEUE.md, CATALOG.md, ciphers/ folders and UNSOLVED-SURVEY.md by shelfmark and DECODE record id (write the
match table to sources/cyphersolver-site/catalogue-2026-10-09-diff.tsv: his no., our match or "-", his score, image online yes/no and where);
for the unmatched rows, score with tools/scout_rubric.py, check KEY-OFFICES.tsv / KEY-DESIGN.tsv for a key family we already hold, and run
the holder-side part of check-solved only as far as the cached sources on disk allow (sources/cryptiana GL.htm and unsolved lists,
sources/decode, LANDSCAPE.md); write QUEUE.md rows (rebase first; the usual columns; credit "Bourdeau catalogue web no. N, 9 Oct 2026")
for the unmatched rows whose images are online, and a separate short list "no image online -- reproduction order candidates" (the HHStA
Vienna pair, Florence 1425, Cluj, Esterházy, Mniszech) for the owner's desk, as a note in QUEUE.md, not an ASKS row. Requests: the
snapshot is on disk; at most 10 DECODE record pages (tools/decode_list.py, 2 s apart) to confirm image availability; no Gallica before
10 Oct 00:00 UTC. Done line "for orchestrator (account-4)": rows parsed, matched, newly queued (ids), reproduction candidates; cost by
get_session is the orchestrator's; file_shrink_guard on QUEUE.md; stage by path; never force-push; never AskUserQuestion.
