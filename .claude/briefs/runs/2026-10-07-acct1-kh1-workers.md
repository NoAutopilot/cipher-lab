# KH-1 worker brief (LANE KH-1, account 1, 7 Oct 2026 17:4x UTC) -- unread siblings for keys already held

Lane brief: .claude/briefs/runs/2026-10-07-acct3-keyhunt.md (read it in full). Common tail: .claude/briefs/README.md.
You are worker KH1-<X>; your key rows (KEY-OFFICES.tsv, header = row 1) and folders are named in your spawn prompt.
Model Opus 5.5. Cap USD 6, box 150 min, whichever first; stop and push at 80% of either (minute 120).

Why: today's only counted results came from applying a key we already hold to sibling entries nobody had decoded.
The deliverable is the COUNT of unread siblings per key, with every candidate logged, plus at most one test decode.

0. `python3 tools/room.py --start`; `date -u`; read the last 30 lines of ROOM.md and the last 20 of UPDATES.md; ROOM
   claim line naming KH1-<X>, your folders, cap and box end time.
1. For each key row: read the key folder's NOTES.md (search logs, "siblings", "other letters", finding-aid notes, Tomokiyo
   pages in sources/cryptiana/) FIRST -- much of the sibling list is already on disk. Then list the same office's OTHER
   letters within the key's validity window +/- 3 years in digitised holdings, by API/script only (Usage 2): Gallica SRU
   and the BnF archivesetmanuscrits finding aid for BnF volumes (the same volume's other folios, neighbouring volumes of
   the same fonds/series), TNA Discovery API, Nationaal Archief, DigitArq (`tools/digitarq_fetch.py`), Europeana; and the
   printed calendar/edition index the folder already names. One host at a time, >=1.5 s apart, good-citizen rule, a few
   hundred requests per host at most; stop on a 403/429/challenge.
2. Keep only letters that are (a) digitised and fetchable from the cloud (CLAUDE.md host table), (b) carry cipher,
   (c) NOT already a folder under ciphers/ (grep the shelfmark and folio across ciphers/*/NOTES.md and QUEUE.md) and NOT
   already read by Bourdeau/Aymeloglu/DECODE/Tomokiyo (grep sources/ including sources/cryptiana/, sources/cyphersolver*,
   sources/decode/; clone a solver repo only to grep it for the shelfmark), and (d) no interlinear decipherment, no
   printed clear text found (say where you looked).
3. At most ONE survivor per worker gets the test (pick the one with the most cipher and the cleanest key match):
   `tools/gallica_folio.py` / native fetch, `tools/iiif_lines.py --image|--ark ... --out <scratchpad>` (paste the crop
   command before the first vision call; crops only, never a full leaf), two blind Sonnet-subagent passes on ONE leaf
   (about 2.5 per call; plus one reconciliation unit), `tools/reconcile_passes.py`, decode with the held key
   (`tools/decode_key.py` or the folder's decode script), matched control = the same key with values shuffled, same N,
   scored the same way (judge with `tools/judge_plaintext.py` where a corpus fits the language and era). Report both
   numbers side by side. Do not start the test if it would cross minute 120 or 80% of cap: list it as `next` instead.
   - control passed (target clearly above shuffled key, judge PASS or near): create `ciphers/<slug>/` with
     ciphertext.txt (as transcribed), NOTES.md first line `blocked` (pending check-solved; the intake gate forbids deep
     work before it), the decode output and the numbers; flag it in ROOM.md for the lane to send check-solved. No AUDIT,
     no novelty words.
   - control failed: one line in the KEY folder's NOTES.md under "## Keyhunt 7 Oct 2026" with both numbers.
4. Write every candidate considered (kept or dropped, with reason) to `KEYHUNT-2026-10-07-KH1-<X>.tsv` at the repo root,
   columns exactly: key_path, letter, shelfmark, digitised, cipher, already_read_by, glossed, action, result. One row per
   letter (or per volume/series where a whole series was dropped for one reason). Also append to the key folder's
   NOTES.md a short "## Keyhunt 7 Oct 2026" section: sources searched with date, unread-sibling count, the file name.
5. Push with `python3 tools/room.py --push <paths>`. Done line in ROOM.md: "done (<start>-<end> UTC by date -u, <cap|box|
   brief met>): unread siblings per key: <path>=<n>, ...; test: <letter> target <x> vs shuffled-key control <y> | none;
   for LANE KH-1". Report in five lines (first line: the counts), stop.

Rules: no new targets beyond step 3's folder, no campaigns, no status-line edits to existing folders. Report what was
found and where it was not found; do not classify novelty; never the words solved, cracked, novel, first, new for anything
this project did. Never call AskUserQuestion. Never print credentials. Never name the owner. Read the clock with `date -u`.
If the auto-mode classifier denies a command, flag it in ROOM.md and stop. Stop and push at USD 6 or 150 minutes.
