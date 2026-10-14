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

## Wave 2 (spawned 06:52 UTC 14 Oct; brief text recorded late, 07:3x UTC -- the 06:5x append was skipped by a failed chained pull, so both
## workers ran from the ROOM spawn line and the folder's own gap lines)
- BAL169-F22 (Opus, cap 4.5, box 75 min, openapi.bnf.fr <= 12): baluze167-davaux-1637 Baluze 169 f.22r bare passage, crop + two blind
  passes + reconciliation, period key application with key.tsv and decode_key.py --check, the 169 ff.52/97/142 method. Done 07:04 (H 4 I 1 M 19).
- BAL167-SWEEP (Opus, cap 5, box 80 min, openapi.bnf.fr <= 300 at >= 3 s): Baluze 167 c1-250 at 300 px, BAL169-SWEEP method, controls the
  listed 167 cipher canvases, <= 15 looks at 1000 px; survey.tsv new rows only; no transcription.
Hosts (both): openapi.bnf.fr only, descriptive UA, one request at a time >= 3 s apart, take/release ROOM lines, one retry after 60 s on
403/429/5xx then stop; never gallica.bnf.fr. The folder's images/ is at 29 MB: never over 30 MB (AX2-SHRINK method or a regen script).

## Wave 3 (07:3x UTC 14 Oct) -- George Lasry's published key sheets as a new instrument; one verifier
Context: LQ-SALV / LQ-C1161 / LQ-F4687 (NOTES sections "Lasry BnF research check (14 Oct 2026, ...)") found his reading of each item partial
and his key published as a sheet image in the snapshot (`sources/cyphersolver/2026-10-14-lasry/<folder>/lasry_p0NN_1.png`; text CC BY 4.0,
credit George Lasry, published by D. Bourdeau, cyphersolver dde5b0ea). A published key is grade-H material where its value is unmarked and
M where his sheet marks "?"; the mapping from our sign labels to his exemplars is your eye work and is graded by its own agreement (two
blind subagent matchings of our atlas exemplars to his sheet, each not shown the other; a label is mapped only where both agree, else M).
Every job: intake gate output pasted (all exit 0 at 07:3x UTC: fr2933 `open (line 1)`, clair1161 `partial (line 1)`, fr4687 `blocked
(line 1) -- already terminal`); PREREG-<JOB>.md pushed before any score; rule 3 control = the same decode under a key with values permuted
within sign class (>= 200 draws), scored by the folder's spec judge (`tools/judge_plaintext.py specs/<slug>.json --file ...`) or, with no
spec, by the count of in-lexicon words of length >= 4 against the permuted-key distribution (p99); the control can differ from the target
on this statistic (the key changes the text). Apply through the folder's decode layout (decode.json / key file, `tools/decode_key.py
<t> --check` exit 0), never overwrite our existing key.tsv: write `key_lasry.tsv` beside it and a decode block or decode_lasry.json. Grades
per rule 4 in NOTES with counts. Disk only, no BnF fetches unless a crop is missing (then openapi.bnf.fr per wave 2 hosts, <= 6). Report
what was found and where it was not found; do not classify novelty. Update Remaining gaps / Escalation (known-keys rung) / Verdict;
gaps_check; NEAR.md is the lane's to update, not yours (say the numbers in the done line).

### SALV-LKEY (Opus, cap 5, box 90 min): fr2933-salviati-1525, his 78-symbol syllabary key (salviati1525/lasry_p031_1.png) on our ff.54r-57v
Our sign inventory: glyphs/atlas.tsv + atlas.png (and labels.json). Units: two blind mapping passes (atlas exemplars vs his sheet, ~1.5
each, one call per atlas part), your reconciliation (~1), decode + control + judge (~1). Report per leaf the share of tokens mapped, the
judge score vs the permuted-key p99, and the best stretch. Our transcription's measured pass-to-pass disagreement is 14.6% (SALV-DIAG):
say whether the decode beats control despite it. NEAR row numbers in the done line.

### C1161-LKEY (Opus, cap 3, box 60 min): clair1161-avis-flandre-1688, his key (clair1161/lasry_p073_1.png) vs our key.tsv
Named next in LQ-C1161's gap line ("a ~$1 key concordance"). Concordance first: per sign, our value / his value / agree-disagree-new; then
apply his values only for signs we hold at M/U or unread (`key_lasry.tsv`, decode block), with the permuted-key control; report how many
of the 4 faces he left "in part" gain readable stretches. Disagreements are a data conflict (rule 4: record both, do not settle).

### F4687-LKEY (Opus, cap 3, box 60 min): fr4687-paleologue-nevers, his key (paleologue1562/lasry_p033_1.png) on our canvases 8-10
LQ-F4687: canvas 8 matches his deciphered part, canvases 9-10 (his f.6v/f.7v, transcribed by us, unread) unconfirmed. Map, apply, control
as above; canvas 8 is the known-answer control (agreement with his deciphered text there gates reading 9-10: pre-register the threshold).
Status stays as the folder's head says unless rule 5 moves it; name what still blocks it.

### VER-BAL22 (Opus, cap 4, box 75 min): verifier, baluze167-davaux-1637 Baluze 169 f.22r reading (BAL169-F22, 14 Oct)
CLAUDE.md "Verifier brief (template)" in full, claim under audit: the BAL169-F22 section's reading of 169 f.22r ("...obligee de se deffaire
de Milandre ... qu'elle en voulust donner le commandement a Mr de Ransau dont j'escris ... au S. de la Boderie", H 4 I 1 M 19). The solver
session was BAL169-F22 (session_01ThV43oDmKJK4XeTgdCDTXN); you are separate. N-class and depth (rule 4a) for this item in AUDIT.md (append a
dated section; do not rewrite earlier sections); correct any over-claim; SECOND-OPINIONS-QUEUE row only if N3+. JSTOR-QUEUE rows in both
families (i) and (ii). Hosts: archive.org (be-api fts, advancedsearch), Google Books API (country=US, key; 503 at 06:5x -- one retry after
a pause, then log unreachable), OpenAlex/S2 with keys, 1.5 s apart.

## Wave 4 (07:5x UTC 14 Oct; last of the lane) -- the named next steps of wave 3
Common rules and hosts as above. Each job is its folder's own named cheapest next; read the wave-3 worker's NOTES section first.
Pre-register before scoring; rule 3 control first; no key.tsv overwrite (`--try` tests, never edits); grades per rule 4; gaps_check.

### SALV-TRY (Opus, cap 2.5, box 45 min, disk only): fr2933-salviati-1525, `--try nt^=ss` on key_lasry.tsv
SALV-LKEY's named next ("--try nt^=ss (f54r L14 vs his excerpt), ~2"). `python3 tools/decode_key.py ciphers/fr2933-salviati-1525 --try ...`
at every occurrence, its own control, with his f.54r L13-15 excerpt (salviati1525/NOTES.md) as the known answer for that line only; then
re-score the two SALV-LKEY statistics (word hits, 4-gram) with the same 300 permuted keys. Accepted value M unless --try's control passed for
its class. Report both numbers before/after; NEAR numbers in the done line. Do not start a further mapping pass.

### C1161-V2 (Opus, cap 2.5, box 45 min, disk only): clair1161-avis-flandre-1688, his nomenclature digit pairs as units (V2)
C1161-LKEY's named next ("V2 digit pairs as units, ~1.5"; PREREG condition in its PREREG file). Same gate and permuted control as V1;
conflicts with our key stay recorded both ways (rule 4). Report V2 vs p99 and faces gaining a licensed stretch.

### BAL167-FIN (Opus, cap 3.5, box 60 min, openapi.bnf.fr <= 200 at >= 3 s): baluze167-davaux-1637, Baluze 167 canvases 251-429
Exactly BAL167-SWEEP's method (its NOTES section), canvases 251 to the volume's end (429 per BAL167-SWEEP; confirm from the manifest), <= 12
looks at 1000 px; controls = listed 167 ff.127, 143, 157, 205 in range. Take/release ROOM lines. New survey.tsv rows only; volumes gap line
(167 done; 168, 171 remain); Verdict; gaps_check. No transcription.
