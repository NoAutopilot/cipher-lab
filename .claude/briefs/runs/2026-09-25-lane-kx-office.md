LANE KX job 2: KX-OFFICE, office map of the keys we hold. Sonnet (claude-sonnet-5). Stall alarm $6 (not a budget; see COMMON).
Parent: LANE KX orchestrator session_01JPoYAFvVfraJibxQdQfrqp. Read .claude/briefs/runs/2026-09-25-lane-kx-COMMON.md first; it binds.
ROOM role: "LANE KX worker KX-OFFICE (Sonnet, <your session id>)". Runs beside KX-XMATCH; do not touch its files.

Question: which unread letters were written by the same office, in the same years, as a key we already hold?

Files you may write: QUEUE.md (one new section only, appended at the end: "## Key reuse candidates (LANE KX, 25 Sept
2026)"), KEY-OFFICES.tsv (repo root), ROOM.md. Nothing else.

1. Keys: every table from `find ciphers -maxdepth 3 \( -iname 'key*.tsv' -o -iname 'key*.txt' \)` minus drafts,
   candidates, atlas, pass, conflicts, counts, align, crosscheck and trial files; plus published key tables on disk
   (sources/solver-diffs/*keys*.tsv, Bourdeau key46/key60, Tomokiyo transcriptions). For each, from the folder's
   NOTES.md (and AUDIT.md): office (sender and recipient, their posts), all correspondents known to use it, years of
   use, language, holding archive and shelfmark/volume, and the folios of the volume the letters sit in. Write
   KEY-OFFICES.tsv: key_path, office, correspondents, years, language, archive, shelfmark, folios_used, notes_source.
2. Candidates: for each office, search the repository's lists only (scripts read, models judge: grep, then read hits):
   QUEUE.md, POOLS.tsv, CATALOG.md, UNSOLVED-SURVEY.md, sources/decode/*.tsv metadata, sources/wvo, sources/huygens,
   sources/cryptiana, sources/solver-diffs, and every ciphers/*/NOTES.md "siblings"/"more under this key" section, for
   unread cipher letters by the same sender or recipient, or the same post, within the key's years +/- 3. Also the
   same manuscript volume's neighbouring folios named in any NOTES.md, manifest or catalogue on disk. A network check
   is allowed only to confirm images are online for a row you already found on disk (IIIF manifest or catalogue item
   page, <= 30 requests total, good-citizen rule); never a new scout sweep.
3. Rows: KX-01 onward in the new QUEUE.md section. Before writing each, grep QUEUE.md and every NOTES.md for its
   shelfmark and date: never re-list a row already there (if it exists, add one line under the section's "already
   listed" paragraph naming the existing row id and which key could read it -- that link is the value). Each row:
   id, item (sender -> recipient, date, shelfmark/folios), key that may read it (path), why (same office/years/volume),
   images online (yes with URL / no / unknown), copy-free (yes/no), existing check-solved verdict if any, and the
   owning lane if the folder or row belongs to another lane (R5: Salviati, Seure, Nevers, fr5761; PX, TX, OX files --
   list them, but mark `other lane: <X>`; the orchestrator notifies them). Rank rows copy-free and images-online first.
4. Do not decode, transcribe, or check-solve anything; do not open new target folders. Push QUEUE.md with
   `python3 tools/room.py --push QUEUE.md KEY-OFFICES.tsv` (rebase before editing QUEUE.md; keep both on conflict).

Final paragraph: first line "N keys mapped to O offices; R candidate rows (C copy-free with images online); A links to
already-listed rows", then the top five rows, files touched, request counts per host, cost.
