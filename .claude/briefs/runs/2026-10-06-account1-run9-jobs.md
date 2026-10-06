# LANE LANE-RUN9-account-1 jobs (account 1) -- 6 Oct 2026 05:5x UTC, lane orchestrator session_014wVbQ4hZf7B7kGezriLmXz

Lane brief: .claude/briefs/default-lane.md (cap 60, box 05:42-15:42 UTC 6 Oct). WORK-QUEUE row LANE-RUN9-account-1: RUN8's own named next
steps for folders a-h first (STATUS.md "LANE LANE-RUN8-account-1 handoff"), then tools/next_steps.py --hot-only runnable rows (S, M), BnF
tie-breaker. VERIFY-BACKLOG.tsv (regenerated 05:4x): only fr16142 "counted" rows (status.json already D0/not counted, AUDIT.md lines
176/200 -- a register-note lag, not a verifier job) and Birago (off limits). Off limits: Birago (incl. ceppo-nevers, nevers-birago,
birago-*), Armstrong, Debosnys, account-4 private-repo targets (bne20211-ferdinand, destaing-gerard, bowes-walsingham, hamilton-1650).
outreach/huntington-eckert-followup-2026-10.md is account 3's OUT-CHECK: no worker edits any outreach/ file.
Every worker: Opus 5.5, one job, then stop. Each solver job first checks that its named step is still undone (NEXT-STEPS.tsv lags the
folders): if a dated NOTES.md section already ran it, take the folder's own Verdict "cheapest next" instead if it fits this job's cap and
box and is not a campaign; otherwise stop and report. Caps per CLAUDE.md Usage 6: (subagent passes + 1 reconciliation) x ~1.5 per pass,
plus ~1.5 Opus session floor.
Intake gate (tools/intake_gate_check.py, 6 Oct 05:5x UTC): decode-2678-bnf-colbert127-gravel-1665, baluze103-letellier-marca-1644,
fr16045-pisany-rome-1585, costabili-modena-1491, eckert-1864, eckert-1862, fr3151-seure-1558, colbert26-lathuillerie-1644 all exit 0
("edition/page or full-text-search citation found within 6 lines").

## Common rules for every job
- First commands: `git fetch origin && git checkout -B main origin/main`, `python3 tools/room.py --start`, `date -u`, then a ROOM claim
  line with `tools/room.py` naming your job id, folder, cap and box end time, addressed "for LANE LANE-RUN9-account-1".
  If --start fails to push from a detached HEAD: `git push origin HEAD:main; git checkout -B main HEAD`.
- Read the folder's NOTES.md tail (Remaining gaps / Escalation / latest dated sections) and AUDIT.md section list before acting.
- Good-citizen rule and the CLAUDE.md host table for every request (one request per host at a time, >= 1.5 s apart; stop a host on
  429/403/challenge). Report request counts per host.
- Rebase before writing shared files (status.json, PROGRESS.tsv, SECOND-OPINIONS-QUEUE.tsv, JSTOR-QUEUE.tsv, ROOM.md); keep both facts
  on conflict. Run `python3 tools/file_shrink_guard.py <every file you touched>` before the final push; push with
  `python3 tools/room.py --push <paths>`.
- Words: never "solved", "cracked", "novel", "first", "new" for anything this project did; rule 10 wording only. Never name the
  owner; never print credentials (test presence with `test -n`). Never call AskUserQuestion. No depth/N-class edits (verifier's job).
- Stop at the cap or at 80% of the box, whichever first; do not start a unit that would cross 80% of either. A stop with work half
  done writes what was done and what remains into the folder's files.
- Done: one ROOM line `done (<start>-<end> UTC by date -u, brief met|stopped at cap): <result, commit>` "for LANE
  LANE-RUN9-account-1", then a five-line final report.

## Solver jobs (solver template .claude/briefs/solver.md; report what was found and where it was not found; do not classify novelty;
## rule 4 grades; rule 7 --check before push; pre-register any gate (PREREG file pushed before the answer is opened); a partial
## target keeps Remaining gaps / Escalation and passes `python3 tools/gaps_check.py <target>`; crops via tools/iiif_lines.py pasted
## before the first subagent call, never a full-page image to a subagent)

### R9-DEC2678 -- decode-2678-bnf-colbert127-gravel-1665: premise fix (Guibert, not Gravel) + sibling Guibert letter search (cap 3, box 50 min)
R8 read canvases 355-356: the letter is signed Guibert, maitre des courriers d'Allemagne (NOTES.md line ~250). Job: (1) correct the premise
in the folder's own files -- NOTES.md opening lines (status line untouched), spec/ status.json title/sender text fields if present (not depth/
N-class), with a dated note; do NOT rename the folder (record "folder name keeps the old catalogue label" in NOTES.md). (2) Run the NOTES.md
"Next (1)" search: other Guibert letters to Colbert, Jan-Feb 1665 (and Guibert cipher letters generally), in the Melanges de Colbert volumes
on Gallica (IIIF manifests / canvas labels via tools/gallica_folio.py; neighbouring canvases of vol. 127 and the adjacent volumes), DECODE
listing (tools/decode_list.py, login-free), Google Books/IA full text for "Guibert" + "courriers" + 1665. Per hit: shelfmark, canvas, in
cipher or clear, same cipher signs or not (thumbnail-level look only). Log every search with counts. Do not decode.

### R9-BAL103 -- baluze103-letellier-marca-1644: the 9 context rule against calib/, then the f.50 sign sorter (cap 4, box 60 min)
Verdict cheapest next: "the 9 context rule against calib/, ~$1.5, then the f.50 sign sorter from r8b/focus.tsv". Job: (1) pre-register and
run the 9 context rule against calib/ (read the NOTES.md section that names it for the exact rule); report the numbers with control.
(2) Build an owner sign sorter for f.50 from r8b/focus.tsv (tools/sign_sorter.py; tile cut via the folder's existing crops or
tools/sorter_recut.py), run `python3 tools/sorter_preflight.py <sorter dir>` and paste its output; on PASS, append a ROOM flag "sorter ready
for account-3 orchestrator to publish (db capability)" with the path. Do not publish it yourself. On FAIL, fix what preflight names once,
re-run; if it still fails, report.

### R9-PIS -- fr16045-pisany-rome-1585: the four gl275 conflict crop compares (cap 2.5, box 40 min)
Verdict cheapest next: "the four gl275 conflict crop compares (T56, T31, T63, T05/T57) against the key table cells, ~$1". R8-PIS logged 4
gloss/key conflicts (rule 4) in HYPOTHESES.md. Job: for each conflict, crop the gloss token and the key-table cell (tools/iiif_lines.py
--region, pasted), one blind read per crop pair; record per conflict: key cell reads X / gloss reads Y / which side is a transcription
slip, or a genuine data conflict (rule 4: keep both, grade M where the witness does not match). Update HYPOTHESES.md and key/exceptions
only where a crop settles a transcription slip; --check; gaps_check.

### R9-COST -- costabili-modena-1491: the q-shape split across R1166 P1/P2/P4 (cap 3.5, box 50 min)
Verdict cheapest next: "the q-shape split (R8-COST, 6 Oct 2026) across R1166 P1/P2/P4 (~$2; with q and TT at C, P4 coverage would be
0.846 on the same passes, arithmetic only)". Job: pre-register the split criterion and the C-coverage gate (the existing 0.80 PREREG gate,
unchanged) before looking at outcomes; apply the split to the existing passes (no new full transcription; crop re-reads only for the q
tokens, batched per page); recompute C coverage per page with the control the PREREG names; report both numbers. A pass under the gate is
logged as such, not re-tuned (rule 3 third-attempt clause).

### R9-ECK64 -- eckert-1864: "(9)"-marked Jan-Mar 1864 entries past page 20 of mssEC 19 (cap 5.5, box 75 min)
Verdict cheapest next: "the (9)-marked Jan-Mar 1864 entries past page 20 of mssEC 19 read from the page images with key-no9.md, ~$4".
Units: pages of mssEC 19 past p.20 with (9)-marked entries; per page one line-crop batch + one blind read (~1.5/pass), stop before a page
that would cross 80% of cap or box. Fetch from Huntington CONTENTdm per the host notes (dmGetItemInfo / page images, one at a time,
>= 1.5 s), manifest images/manifest.json. Decode with the folder's decode_no9.py (or its current decoder) --check; grade per token (H from
the key book, M uncertain); report entries read, H/M counts before/after, and where OR prints the same telegram (compare, do not overclaim).
Do not edit outreach/ files.

### R9-ECK62 -- eckert-1862: "Apl"/"Washn" heading forms in the entry splitter, re-split (cap 2, box 35 min)
Verdict cheapest next: "add the "Apl"/"Washn" heading forms to the entry splitter and re-split (~$1)". Job: add the forms to the folder's
splitter (or the shared tool if it lives in tools/, with an offline test), re-split, re-run the folder's --check scripts, report entry
counts before/after and any entries that newly separate or merge. No new key values.

## Wave 2 (written 05:5x UTC; caps raised 06:0x for the ~3 Opus session floor seen in wave 1; intake gate 6 Oct 05:5x UTC exit 0 for every folder below)

### R9-SEURE -- fr3151-seure-1558: Henri II-era French keys vs the reconciled f81R reads (cap 4.5, box 55 min)
Verdict cheapest next: "test Henri II-era French keys (Tomokiyo, Lasry GL) against the reconciled f81R reads, ~$3". Job: list candidate
keys on disk or in sources/ (Tomokiyo cryptiana snapshots, Lasry GL tables already transcribed; no new transcription of a key beyond one
small table), pre-register the fit statistic with a shuffled-key / wrong-era-key control that CAN differ from the target (rule 3 orthogonality
paragraph), push PREREG, then score. Per key: fit, control, verdict. No decode claimed unless the control is cleared.

### R9-COL26 -- colbert26-lathuillerie-1644: pre-registered per-code control for the anchor leads (cap 3, box 35 min)
Verdict cheapest next: "a pre-registered per-code control for the anchor leads 21 = t, 20 = i, 23 = n, 83 = s (R7A-COL26 post hoc) and 12 = c
(38 of 58 off f.23) on every cleared unit, canvas 62-63 included (R8-COL26), ~$0.5". Script job, no vision: PREREG first, per-code real vs
shuffle p95 on each cleared unit with per-unit breakdown (CLAUDE.md rule 3 per-unit paragraph); key changes only for codes the PREREG passes.

### R9-HUNT -- huntington-blathwayt-madrid-1728: context-fill of the 18 unkeyed BLA186/191(a) groups (cap 4.5, box 55 min)
Verdict cheapest next: "context-fill of the 18 unkeyed BLA186/191(a) groups with a BLA185 blanking control, ~$3". Run the BLA185 blanking
control first (blank known groups, fill from context, measure recovery); only if it clears its pre-registered gate, fill the 18 groups,
grade M/S per the gate. Report both numbers.

### R9-NOX -- fr16142-noailles-constantinople-1571: text-check the date-only Dupuy matches (cap 3, box 35 min)
Verdict cheapest next: "text-check the date-only Dupuy matches, ~$1". Read the matched Dupuy texts against the folder's readings/gloss
for each date-only match; per match: text agrees / differs / not the same letter. Do not touch depth/N-class (status.json D0 stays; a
verifier sets it). Also note in NOTES.md that PROGRESS.tsv rows 51-52 lack the "not counted" note VERIFY-BACKLOG keys on (one line, do
not edit PROGRESS.tsv).

### R9-VIEU -- fr3975-vieuville-1587: print_check of the clear phrases (Sonnet, cap 1.5, box 25 min)
NOTES next: run tools/print_check.py with the letter's readable clear phrases ("eschevins et maire de ville", "St Aignen", 30 Sept 1587)
against IA, Google Books (country=US) and OpenAlex. Report hits (search results only, rule 10) in NOTES.md.

### R9-NEVF -- fr3416-nevers-fils-1589: L05 glyph-atlas test re-registered without class 0 (cap 4.5, box 55 min)
Verdict cheapest next: "the L05 glyph-atlas test re-registered without class 0 (pos 5/13/17/20), ~$3". PREREG first (new registration,
class 0 excluded, same gate otherwise), then run; report real vs control; a FAIL is logged, not re-tuned.

## Wave 3 (written 06:1x UTC from wave 1's own Verdict lines; intake gate exit 0 for every folder below, 6 Oct 06:1x UTC)

### R9-BAL103B -- baluze103-letellier-marca-1644: circled/plain 9 crop read on the 42 tokens (cap 3, box 35 min)
Verdict cheapest next (R9-BAL103): "the circled/plain 9 crop read on the 42 tokens, ~$1.5". Crops via tools/iiif_lines.py (pasted), one
blind read batch; corrections TSV only where the read is unambiguous; re-decode --check, fr17 judge before/after. Do not touch the sorter
files already flagged for account 3.

### R9-ECK64B -- eckert-1864: mssEC 19 pages 61+ and unmarked pp.21-60 old-vocabulary entries (cap 5, box 60 min)
Verdict cheapest next (R9-ECK64): scan pages 61 onward and the unmarked entries of pp.21-60 for old-vocabulary entries, read them with
key-no9.md, search O9-U/O9-V in OR I/35 pt 2 and ser. III vol. 4. Per-page units as R9-ECK64; stop before a unit crossing 80%.

### R9-PIS2 -- fr16045-pisany-rome-1585: T31 per-token crop compare vs T45/T36 table cells (cap 3.5, box 45 min)
Verdict cheapest next (R9-PIS): "the T31 per-token crop compare against the T45/T36 table cells (11 tokens f.244r + 13 f.275r, ~$2)".
Crops pasted; one blind batch per leaf + 1 reconciliation; rule 4 for any data conflict.

### R9-DEC2678B -- decode-2678-bnf-colbert127-gravel-1665: locate Gravel's other cipher letters (cap 3, box 40 min)
NOTES "Next (1)" (R9-DEC2678): R2733 (Mel. Colbert 168bis f.553, 1674) and the AE Correspondance politique Allemagne volume(s) for Jan 1665
(Gravel's Diet dispatches to Lionne). Locator job only: find the volume shelfmark/ark and canvas range (Gallica SRU / manifest labels,
archivesetmanuscrits, DECODE R2733 login-free metadata); thumbnail-level look whether the same two-digit groups occur. Do not transcribe
or decode.

### R9-FLOR -- florence-dieci-responsive: glyph_atlas threshold tuning on c.127 (no vision) (cap 3, box 40 min)
Verdict cheapest next: "glyph_atlas threshold tuning on c.127 (no vision) so the sorter can cover lines L02-L18, ~$1.5". Script-only;
report coverage before/after per line; do not build or publish a sorter in this job.

### R9-ELEC -- fr5761-election-1519: full-text search of Deutsche Reichstagsakten J.R. I (Sonnet, cap 1.5, box 30 min)
NOTES next: archive.org be-api fts and Google Books API (country=US) on Deutsche Reichstagsakten Jungere Reihe I for "chiffre"/"Ziffer" +
Moltzan/Cordier; log every query and hit count (search results only, rule 10).

## Wave 4 (written 06:2x UTC from wave 2's own Verdict lines; spawned only as budget allows; intake gate already exit 0 above)

### R9-SEURE2 -- fr3151-seure-1558: Bourdeau's guiche1551 key vs R1/R2 (cap 3.5, box 45 min)
Verdict cheapest next (R9-SEURE): "fetch Bourdeau's guiche1551 key and test it against R1/R2 with a coverage-checked statistic and own-text
power control first, ~$2.5". Bourdeau's code is MIT/text CC BY (credit him, CLAUDE.md rule 8); the power control runs first and must clear
its PREREG gate, else NON-TEST and stop.

### R9-NEVF2 -- fr3416-nevers-fils-1589: L05 sign-sorter build for a person's read (cap 3, box 35 min)
Verdict cheapest next (R9-NEVF): "the L05 sign-sorter build for a person's read (pos 4/5/7/13/15/16/17/20), ~$1". Build with
tools/sign_sorter.py, run tools/sorter_preflight.py and paste; on PASS a ROOM flag for the account-3 orchestrator to publish (db capability).
Do not publish.

### R9-NOX2 -- fr16142-noailles-constantinople-1571: c262 gloss lines below L13, one cut and read (cap 2.5, box 30 min)
Verdict cheapest next (R9-NOX): "c262 gloss lines below L13, one cut and read, ~$0.5". Crops pasted, one blind read, gloss.tsv rows added
with grades; if the reading feeds an existing pre-registered test, re-run it with --check. No depth/N-class edits; flag the verifier if
any number in status.json depth_check moves (rule 10 propagation).

### R9-HUNT2 -- huntington-blathwayt-madrid-1728: re-registered context-fill, attempt 2 of at most 3 (cap 3, box 40 min)
Verdict cheapest next (R9-HUNT): bracket fix + margin-filtered gate against the shuffled-context control at matched margin. The margin
gate was seen post hoc on seeds 1-3, so the new PREREG fixes margin threshold and gate BEFORE running, on FRESH seeds only (4-6+),
pushed first. If the control fails again, log "attempt 2 FAIL" and name a different instrument as next (rule 3 third-attempt clause);
do not tune again.

### R9-DEC2678C -- decode-2678-bnf-colbert127-gravel-1665: the 1672 Gravel key (Mel. Colbert 159 f.102) tested on R2678 (cap 4, box 50 min)
R9-DEC2678B found Mel. Colbert 159 f.102r-v (btv1b10035602g canvases 107-108, Gravel to Colbert 23 Apr 1672) in the same two-digit+diacritics
design with a contemporary interlinear decipherment; Tomokiyo reconstructs that key on louisxiv0.htm (cite him, rule 8). Job: (1) build the
1672 key: Tomokiyo's table if on disk/snapshot-able (sources/cryptiana/, snapshot unmodified), else read f.102's interlinear pairs from line
crops (tools/iiif_lines.py pasted) into tools/interlinear_align.py (grade H/period key). (2) PREREG before decoding R2678: statistic (e.g.
fraction of R2678 groups covered + fr17 judge on the decode), matched controls that CAN differ (shuffled-key decode of R2678; a held-out f.102
line decoded with the key built without it), gate. Push PREREG. (3) Run; report both numbers; grade per token (H period key where the key
cell is read, M otherwise); a decode only via tools/decode_key.py with --check. A 1672 key on a 1665 letter may not fit: a FAIL is a result.
Report what was found and where it was not found; do not classify novelty.
