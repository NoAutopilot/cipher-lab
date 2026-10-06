# LANE DEFAULT-account-2-20261006-2209 jobs (account 2) -- 6 Oct 2026 22:1x UTC, lane orchestrator session_01DfJ7KB48PGfFxMBC3v3gpk

Lane brief: .claude/briefs/default-lane.md (cap 60, box 22:11 UTC 6 Oct - 08:11 UTC 7 Oct). Gate 0a clear (SESSION-SWEEP-account-2 done
23:21 5 Oct). VERIFY-BACKLOG: only actionable rows are Birago (off limits) and nla-heinrich audit2 (class N0, gate 2 needs it only above N1:
not briefed). NEXT-STEPS --hot-only: 32 runnable rows, most worked today by RUN7-RUN15 (account 2), RUN12 (account 1), RUN13 (account 4) and
DEFAULT-account-1; rows touched in ROOM in the last 6 h or whose named step already ran are not briefed. Off limits: Birago (incl.
nevers-birago-fr3251-1572), Armstrong, Debosnys. Gallica probe 22:1x UTC: IIIF manifest HTTP 200.
Every worker: Opus 5.5, one job, then stop. Each job first checks that its named step is still undone (a dated NOTES.md section may already
have run it); if so, correct the NOTES.md next-step line, stop and report rather than inventing work.

## Common rules for every job
- First commands: `git fetch origin && git checkout -B main origin/main`, `python3 tools/room.py --start`, `date -u`, then a ROOM claim
  line with `tools/room.py` naming your job id, folder, cap and box end time, addressed "for LANE DEFAULT-account-2-20261006-2209".
  If --start fails to push from a detached HEAD: `git push origin HEAD:main; git checkout -B main HEAD`.
- Read the folder's NOTES.md tail (Remaining gaps / Escalation / latest dated sections), HYPOTHESES.md and AUDIT.md section list first.
- Good-citizen rule and the CLAUDE.md host table for every request (one request per host at a time, >= 1.5 s apart; stop a host on
  429/403/challenge, one retry after a pause at most). Report request counts per host.
- Rule 3: any gate is pre-registered (a PREREG file committed and pushed before the scored run), with a matched control that can vary on
  the statistic tested; report both numbers. Rule 4 grades with counts. Rule 7: `tools/decode_key.py <folder> --check` (or the folder's
  own decode script --check) exit 0 before push if the reading or key changed. A reading change after AUDIT.md: say so in NOTES.md and
  flag in ROOM for a verifier.
- Rebase before writing shared files (status.json, PROGRESS.tsv, ROOM.md, HYPOTHESES.md, NOTES.md of a folder another job also touches);
  keep both facts on conflict. Run `python3 tools/file_shrink_guard.py <every file you touched>` before the final push; push with
  `python3 tools/room.py --push <paths>`.
- Partial targets: update "## Remaining gaps" / "## Escalation" (Verdict line) and pass `python3 tools/gaps_check.py <target>`.
- Words: never "solved", "cracked", "novel", "first", "new" for anything this project did; rule 10 wording only. Never name the
  owner; never print credentials (test presence with `test -n`). Never call AskUserQuestion. Report what was found and where it was not
  found; do not classify novelty (verifier jobs excepted, where the brief says).
- Stop at the cap or at 80% of the box, whichever first; do not start a unit that would cross 80% of either. A stop with work half
  done writes what was done and what remains into the folder's files. An Opus session floor is about 1.5; caps below assume it.
- Vision work: crop step mandatory and pasted (`tools/iiif_lines.py --image FILE --out DIR` or the --ark/--canvas form); give
  subagents only crop paths, one page/leaf per call (or the stated crop batch), never a full-page image. Price: ~1.5 per Sonnet
  subagent pass, reconciliation = 1 unit. Thumbnail/contact-sheet triage by the worker's own eye at low resolution is allowed.
- Sorters: any sorter meant for the owner must PASS `python3 tools/sorter_preflight.py` and have 5+ random tiles opened against the line
  image; it is handed to the account-3 orchestrator (ROOM flag line) to publish. Never publish an artifact or edit ASKS.md yourself.
- Done: one ROOM line `done (<start>-<end> UTC by date -u, brief met|stopped at cap): <result, commit>` "for LANE DEFAULT-account-2-20261006-2209",
  then a five-line final report.

## Wave 1 (spawned 22:15 UTC 6 Oct). Intake gate output (22:1x UTC) pasted per job.

### D22-COL26P -- colbert26-lathuillerie-1644: per-code positional test of the open f.23 codes (Opus; cap 3, box 45 min; scripts only)
Intake: `colbert26-lathuillerie-1644: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`
The Verdict line names the cheapest next step: a per-code test of the open f.23 codes in key_f23_anchor_r10.tsv with a POSITIONAL statistic
(the value at the anchor-predicted offset in the gloss, not span-contains, so a common letter such as e can reach significance), with the
held-out units named before the run. Read NOTES.md "## R10-COL26B/C/D" and the Escalation first so you reuse their scripts, units and
control B. Write PREREG (codes tested, held-out units, statistic, control that permutes the gloss letters at the predicted offset so it CAN
differ from the target on this statistic, per-code gate and a multiple-comparison correction), commit and push it before scoring. Then score;
per code report target vs control p95 and P. A code clearing its gate is S (not C) and is listed, not merged into key.tsv unless the PREREG
named that merge and decode --check passes. Update NOTES.md section + Remaining gaps / Escalation; gaps_check passes. Unit estimate: 1 script
build + 1 run, no vision.

### D22-LINTRIM -- antt-linhares-chave: front-trim and adjacent-join enumeration with the worked-example known-answer control (Opus; cap 4, box 50 min)
Intake: `antt-linhares-chave: blocked (line 3) -- already terminal, nothing to gate` (status as written; NOTES Verdict reads keep going)
The key sheet allows trims "do principio, ou do fim" and its worked example joins adjacent fragments ("Rus"+"si"+"a"); the committed reading
uses end-trims only. Remaining gaps names the trimmed/fragment tokens (man, d, he, o x3, do, pauperr, ven, ha). Build an enumerator: for each
fragment token, every front-trim and end-trim of its book word allowed by the key's own rules, and every join with adjacent fragments.
Known-answer control FIRST: the key sheet's own worked example (and any other example the sheet gives) must be recovered by the enumerator at
rank 1 under the scoring you choose (pt18 corpus, tools/judge_plaintext.py's pt18 or a word list from tools/data/pt18); if it fails, stop and
log "non-test: enumerator fails its known-answer control". PREREG the scoring rule and what counts as a resolved token (e.g. unique top
candidate with margin) before scoring the target tokens; pushed first. Report per token: candidates, chosen, margin; grade S at most for a
resolved token (M otherwise). If the reading changes: the folder's decode script --check exit 0, flag a verifier in ROOM (AUDIT.md exists).
Remaining gaps / Escalation updated; gaps_check passes. No network beyond what is on disk unless a page the key needs is absent (DigitArq
rule: >=3 s apart, <=20 requests).

### D22-F3151D -- fr3151-noailles-1558: date-locating pass over fr. 10773 for a clear copy of the 13 Nov 1558 letter (Opus; cap 3, box 50 min)
Intake: `fr3151-noailles-1558: open (line 1) -- edition/page or full-text-search citation found within 6 lines`
NOTES.md "## IMG-GALLICA1" surveyed Gallica fr. 10773 (btv1b52527305r, copies of Noailles's Venice/Constantinople dispatches) at thumbnail
size only: whether it holds a clear copy of no. 33 (Noailles at Venice to the Cardinal de Lorraine, 13 Nov 1558) is not established. Run the
named step: bisection on the folio labels (tools/gallica_folio.py for canvas/folio mapping), reading copy headings at about 1000 px, about 6-8
leaf views (each a crop of the heading region via tools/iiif_lines.py --ark --canvas --region, not the full page; read by your own eye or
one Sonnet call per crop). Goal: locate Nov 1558 in the volume; if a copy of a 13 Nov 1558 letter to Lorraine (or other Nov 1558 letters to
Lorraine) is found, record folio/canvas, transcribe its first and last lines, and save the crops in the folder (manifest entry). Do NOT align
it to the cipher in this job (that is the next job; write it as the next step with a cost). If the volume does not reach Nov 1558 or skips it,
say so with the dates seen at each bisection point. Gallica: one request at a time, >=2 s apart, stop on altcha/403. Update NOTES.md and the
next-step line. Unit estimate: 8 crops x ~0.3.

### D22-CEPPO21 -- ceppo-nevers-fr3251-1570s: f.21v S65/S80 witness-shape settle (Opus; cap 4, box 50 min)
Intake: `ceppo-nevers-fr3251-1570s: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`
The Verdict line names: f.21v S65/S80 witness-shape settle on 4x tiles (~$4). The f.36v blind-read instrument is [retired]; this is f.21v and
the witness-shape method (as VERIFY-CEPPO-WP and the f.87 L04.39 unit did: shape evidence + rank under each value, 201-key control) -- read
those sections and reuse their scripts. Steps: list the f.21v tokens whose value hangs on S65 vs S80; cut 4x tiles (tools/iiif_lines.py or the
folder's own tile script; paste the command); PREREG what shape evidence settles each token and the decision rule, pushed before reading; read
the tiles yourself (or 2 blind Sonnet calls on the tile batch, 1 reconciliation); then decode under each assignment and report the score and
rank vs the 201-key control. Grade per token (S only if shape and score agree; else M). decode --check exit 0 if anything changes; Remaining
gaps / Escalation; gaps_check passes. If the instrument proves unable to separate S65/S80 on f.21v, mark the step [retired] with the
instrument named.

## Wave 2 (spawned 22:17 UTC 6 Oct)

### D22-FTS -- six "depends on nobody" printed-source searches, one Sonnet worker (Sonnet; cap 5, box 75 min; ~0.6 per item + 1 write-up)
Catalogue/full-text search only: no transcription, no decoding, no vision beyond reading a hit page's OCR text. Each item: check the
named step is still undone (read the folder's NOTES.md "While waiting"/Premise check and the last dated section); run it; append a dated
section "## D22-FTS (6 Oct 2026)" to that folder's NOTES.md with every query, host, hit count and the snippet of any hit, and update the
"While waiting" line (mark [done], name what is left). Hits are search results for the log, never a novelty or found-solved verdict
(rule 10); if a hit looks like a printed clear text or decipherment of the very item, say so in ROOM with a flag line for the lane and stop
that item there. Hosts: archive.org advancedsearch / be-api fts, Google Books API (key + country=US), Huygens retroboeken (>=2 s), Gallica
SRU; per CLAUDE.md host table, one request at a time >=1.5 s apart, report counts per host. Intake (22:1x UTC): sacchetti and 9970 open
with citation found; belmesseri, salvago, della-torre "blocked, already terminal"; heinsius-dopff open with citation found.
1. bl-sacchetti-nunzio-1623: Barberini-side nunciature editions (Nuntiaturberichte / Barb. lat. series) by full text for "Sacchetti" with
   "cifra"/"ziffera".
2. belmesseri-napoli-1627: the folder's pass (d) -- Spanish-side literature full-text search (IA be-api/advancedsearch, Google Books).
3. salvago-caraffa-1691: Atti della Società Ligure di Storia Patria (memoriedigitaliliguri.it, reachability test first; IA copies if any)
   for "Caraffa" 1691 and "Coysis".
4. della-torre-olanda-1690: Huygens retroboeken Staten-Generaal / Resolutien 1690 for Della Torre's mission (clear copy of a despatch).
5. decode-9970-simancas-1527: read Galende 1994 p.163 (shallow clone of github.com/dbourdeau/cyphersolver into your scratchpad, grep
   esp318/lit/galende1994.txt only; MIT/CC BY, cite) for the 1527 letter's Simancas Estado leg. 1563 citation.
6. heinsius-dopff-1702: Marlborough-side editions not yet grepped (Snyder, Marlborough-Godolphin Correspondence; Murray's Letters and
   Dispatches) for the 1702 letters, IA full text.
Stop at the cap; items not reached are listed as not reached in your done line.

## Wave 3 (spawned 22:35 UTC 6 Oct) -- follow-ups named by wave 1-2

### D22-FTS2 -- four page-level follow-ups to D22-FTS / D22-F3151D leads, one Sonnet worker (Sonnet; cap 4, box 60 min; ~0.7 per item + write-up)
Same rules as D22-FTS (search and page reading only, no decoding, rule 10, host table, request counts). Append "## D22-FTS2 (6 Oct 2026)"
to each folder's NOTES.md and update its While waiting / next-step line.
1. della-torre-olanda-1690: read Correspondentie van Willem III en Bentinck (Huygens retroboeken) KS 24 alphabetical letter list p.800 and
   the 1690 letters it indexes for Della Torre: is any despatch printed in clear? (pages.json for the page image only if OCR is unclear.)
2. fr3151-noailles-1558: the next step D22-F3151D named -- Gallica SRU (dc.title/dc.source "Noailles" + "Venise", 1558) and BnF
   archivesetmanuscrits ("Noailles" "1558" copies) for another digitised register of Noailles's own Venice dispatches; for any hit, the
   manifest canvas labels and one heading check near Nov 1558 (crop, not full page). Report hits; do not align.
3. bl-sacchetti-nunzio-1623: Quazza, La guerra per la successione di Mantova (IA identifier in the folder's D22-FTS section) -- read the
   "dal nunzio Sacchetti" passages and footnotes: which archive/series of Sacchetti's dispatches does Quazza cite, and does he quote any
   deciphered passage of 1623? 
4. belmesseri-napoli-1627: Negri, Archivio Soc. rom. 34 (archivio34sociuoft, djvu on disk or one download): the footnotes citing Modena
   (ASMo Cancelleria ducale, Ambasciatori Roma/Napoli) -- list the cited series/buste and whether Negri prints any deciphered passage that
   could be the b.20 letter's text.
