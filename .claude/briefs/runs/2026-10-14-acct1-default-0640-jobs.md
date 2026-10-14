# LANE DEFAULT-account-1-20261014-0640 jobs (account 1, lane orchestrator session_01E1t93edi7dJdePSmqpBJwW) -- 14 Oct 2026 06:5x UTC

Lane brief: .claude/briefs/default-lane.md. Cap 60, box 06:40-16:40 UTC 14 Oct. Gate 0a: SESSION-SWEEP-account-1 stale-claimed since 5 Oct,
proceeded as prior incarnations. First wave answers LANE BNF-FOCUS's 06:19 UTC flag (ROOM.md): George Lasry's "BnF cipher research"
(10 Oct 2026; 55 folders) was published in D. Bourdeau's cyphersolver repository (commit dde5b0ea, 13 Oct 21:01 UTC). Twelve of our folders
share a BnF volume with one of his items (sources/cyphersolver/2026-10-14-lasry/ours_same_volume.tsv); the four Birago/ceppo folders are
off limits to this lane; the other eight are checked here, item by item, before any more spend on them. This is a record check (light
guardrail: correcting a record), not cryptanalysis.

## Common rules for every job
Exactly the "Common rules for every job" section of `.claude/briefs/runs/2026-10-09-ytbiz-family-1310-jobs.md` (read it in full), with
these substitutions: address every ROOM line "for LANE DEFAULT-A1-0640-14 (account 1)"; the hosts bullet below replaces that file's
hosts lines. Export `CIPHERLAB_ACCOUNT=account-1` before any tools/room.py call. `get_session` is not available to you: say "cost not
visible to this session" in the done line. Never the words solved, cracked, novel, first, new for anything this project did.
**Hosts: github.com only** (public repository dbourdeau/cyphersolver, text CC BY 4.0, code MIT): one shallow sparse clone into your
scratchpad (`git clone --depth 1 --filter=blob:none --sparse https://github.com/dbourdeau/cyphersolver <scratch>/cs && git -C <scratch>/cs
sparse-checkout set targets/<lasry_folder> <any hub/report file you need>`), grep it, never a second clone; the hub page
dbourdeau.github.io/cyphersolver/lasry-bnf.html at most twice. No BnF/Gallica fetches in this wave (the leaf identity comes from our
folder's own NOTES/inventory and his profile.json/NOTES.md).

## The item check (every job)
1. Read our folder's NOTES.md head, AUDIT.md (if any), inventory/sources files: list our items (shelfmark, folio(s), date, sender ->
   recipient, what we read and at what grade/N-class/depth).
2. Snapshot his folder unmodified to `sources/cyphersolver/2026-10-14-lasry/<lasry_folder>/` (as BNF-FOCUS did for five; do not edit;
   if already there, skip). Record the cyphersolver HEAD hash.
3. Item-level match: for each of our items, is it the same leaf (shelfmark + folio + date + sender/recipient)? Answer match / partial
   (overlapping leaves or letters, say which) / no match (same volume, different item) with the evidence fields side by side.
4. Where it matches: his counts (pages, symbols/elements, % identified, method, extent) quoted from his files; and, only where we have
   a reading on disk, a short side-by-side of the first ~3 lines of plaintext (ours vs his) and one sentence on agreement. No re-solving,
   no key edits, no re-grading of our tokens.
5. Write `## Lasry BnF research check (14 Oct 2026, <JOB>)` in our NOTES.md: the table from 3, the quotes from 4, credit line (George Lasry,
   result; D. Bourdeau, publication, cyphersolver dde5b0ea; text CC BY 4.0), and what changes for our work.
   Status (rule 5): if every item we hold is matched by his reading with extent complete and we hold no prior/period decipherment that
   already made it `solved`, set the head status to `found-solved` with a one-line pointer to this section (the fr3613-rondinelli-1590
   NOTES.md line 2 is the model). If only some items match, keep the status and say which items remain ours to work. A `solved` (N0, gloss
   on the leaf) or `found-solved` (period print) folder keeps its status; only add the section.
   If the folder has `## Remaining gaps` / `## Escalation`, mark every gap his reading now covers as closed by prior work and re-run
   `python3 tools/gaps_check.py <target>` (paste the output in NOTES).
   AUDIT.md: do not change any N-class (verifier's job). Append one dated line "Prior-work notice (14 Oct 2026): ... see NOTES.md section"
   and post a ROOM flag "AUDIT re-class needed: <target>" when an AUDIT N2+ item is matched.
6. Do not touch status.json, NEAR.md, STATUS.md or the board (the lane orchestrator does). Report in five lines: per item match/partial/
   none, status before/after, flags raised. Report what was found and where it was not found; do not classify novelty.

## Wave 1 (06:5x UTC 14 Oct)
- LQ-SALV (Opus, cap 2.5, box 45 min): fr2933-salviati-1525 vs his `salviati1525` (Salviati, 16 Oct 1525, BnF fr.2933). Our folder is a
  NEAR.md row (rule 5) with ff.54r-57v transcribed; say for each leaf f.54r-57v whether his reading covers it.
- LQ-C1161 (Opus, cap 2.5, box 45 min): clair1161-avis-flandre-1688 vs his `clair1161` (BnF Clairambault 1161; his date "1554/1555 a
  hypothesis" vs our 1688 dating: say which leaves each covers and quote both datings' evidence without adjudicating). NEAR.md row.
- LQ-F5160 (Opus, cap 2.5, box 45 min): fr5160-letellier-1653 vs his `brienne5160` (Brienne -> Servien, 10 Jan and 1 Aug 1653, letter B
  undated, BnF fr.5160). We hold several folios (f.1, f.9, f.67, f.68, f.86-88, canvases 11-12/32): per folio.
- LQ-F4687 (Sonnet, cap 1.5, box 40 min): fr4687-paleologue-nevers vs his `paleologue1562` (BnF fr.4687, 1562-1564).
- LQ-REC4 (Sonnet, cap 2, box 50 min): four record-only checks, one section per folder, same steps: clair1067-brienne-poland-1646 vs
  `brienne1067`; clair1108-duvergier vs `vergier1696`; dupuy155-1597 vs `dupuy155`; dupuy468-anhalt vs `dupuy468`. These already read
  `solved` or `found-solved`; their status does not change; flag AUDIT re-class only per step 5.
