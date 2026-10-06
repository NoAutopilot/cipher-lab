# LANE LANE-RUN12-account-2 jobs (account 2) -- 6 Oct 2026 11:1x UTC, lane orchestrator session_0134Hz4BBL6omk3Bx6T3wpcv

Lane brief: .claude/briefs/default-lane.md (cap 60, box 11:12-21:12 UTC 6 Oct). WORK-QUEUE row LANE-RUN12-account-2: RUN11's named
next steps for this split (STATUS.md "LANE LANE-RUN11-account-2 handoff", "Open for the next i-r lane"), then tools/next_steps.py
runnable rows (S, M) and `parallel` actions (plain next_steps, not --hot-only). Folders i-r (account 1 a-h, account 4 s-z), plus
catokwacopa-1875 as pollaky-1865-1875's own named gap 3 (no other lane's claim on it in the last 900 ROOM lines).
VERIFY-BACKLOG.tsv i-r row: nla-heinrich-braunschweig-1519 audit2 (low) -- not run: AUDIT.md class is N0, and Outreach gate 2's
second audit applies only above N1. Off limits: Birago (incl. nevers-birago-fr3251-1572), Armstrong, Debosnys; riksarkivet-r4282-1628.
Dropped as already run (checked 11:1x): lambeth-bacon Baconiana page images (D2-BACON 5 Oct), rumpf NA re-probe (twice on 6 Oct),
naf14913 f.206r phrase search (NOTES line 1592), ormond Russell-Prendergast (R8-ORM).
Gate 0a: SESSION-SWEEP-account-2 row still `claimed`, its TSV (2026-10-05) on disk; RUN7-RUN11 proceeded past it the same way.
Every worker: Opus 5.5 (Sonnet 5.5 only where stated), one job, then stop. Each job first checks that its named step is still undone
(a dated NOTES.md section may already have run it); if so, stop and report rather than inventing work.

## Common rules for every job
- First commands: `git fetch origin && git checkout -B main origin/main`, `python3 tools/room.py --start`, `date -u`, then a ROOM claim
  line with `tools/room.py` naming your job id, folder, cap and box end time, addressed "for LANE LANE-RUN12-account-2".
  If --start fails to push from a detached HEAD: `git push origin HEAD:main; git checkout -B main HEAD`.
- Read the folder's NOTES.md tail (Remaining gaps / Escalation / latest dated sections), HYPOTHESES.md and AUDIT.md section list first.
- Good-citizen rule and the CLAUDE.md host table for every request (one request per host at a time, >= 1.5 s apart; stop a host on
  429/403/challenge, one retry after a pause at most). Report request counts per host.
- Rule 3: any gate is pre-registered (a PREREG file committed and pushed before the scored run), with a matched control that can vary on
  the statistic tested; report both numbers. Rule 4 grades with counts. Rule 7: `tools/decode_key.py <folder> --check` (or the folder's
  own decode script --check) exit 0 before push if the reading or key changed. A reading change after AUDIT.md: say so in NOTES.md and
  flag in ROOM for a verifier.
- Rebase before writing shared files (status.json, PROGRESS.tsv, ROOM.md, HYPOTHESES.md); keep both facts on conflict. Run
  `python3 tools/file_shrink_guard.py <every file you touched>` before the final push; push with `python3 tools/room.py --push <paths>`.
- Partial targets: update "## Remaining gaps" / "## Escalation" (Verdict line) and pass `python3 tools/gaps_check.py <target>`.
- Words: never "solved", "cracked", "novel", "first", "new" for anything this project did; rule 10 wording only. Never name the
  owner; never print credentials (test presence with `test -n`). Never call AskUserQuestion. Report what was found and where it was not
  found; do not classify novelty (verifier jobs excepted, where the brief says).
- Stop at the cap or at 80% of the box, whichever first; do not start a unit that would cross 80% of either. A stop with work half
  done writes what was done and what remains into the folder's files. An Opus session floor is about 1.5; caps below assume it.
- Vision work: crop step mandatory and pasted (`tools/iiif_lines.py --image FILE --out DIR` or the --ark/--canvas form); give
  subagents only crop paths, one page/leaf per call, never a full-page image. Price: ~1.5 per Sonnet subagent pass, reconciliation = 1 unit.
  Thumbnail/contact-sheet triage by the worker's own eye at low resolution is allowed for locating pages.
- Sorters: any sorter meant for the owner must PASS `python3 tools/sorter_preflight.py` and have 5+ random tiles opened against the line
  image; it is handed to the account-3 orchestrator (ROOM flag line) to publish. Never publish an artifact or edit ASKS.md yourself.
- Done: one ROOM line `done (<start>-<end> UTC by date -u, brief met|stopped at cap): <result, commit>` "for LANE LANE-RUN12-account-2",
  then a five-line final report.

## Wave 1 (spawned 11:2x UTC 6 Oct). Intake gate output (11:1x UTC) pasted per job.

### R12-RJMPUB -- rah-juan-manuel-1521, rule-1 check: is any of the 28 letters' decipherment already published? (Sonnet 5.5, cap 2.5, box 45 min)
Intake gate: `rah-juan-manuel-1521: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`.
RUN11 (R11-RJMKEY) transcribed Tomokiyo's published Juan Manuel letter alphabet (cryptiana JuanManuel.png) and flagged that a published
key implies someone has had working decipherments. Before any further solver work: search, and log each family searched/unreachable
with the query and date, in a "## Published-decipherment check (R12-RJMPUB)" section: (a) Tomokiyo's own pages that carry the table
(cryptiana.web.fc2.com: the page embedding JuanManuel.png and its siblings; the Cryptiana blog post and comments) -- what source does he
cite for the table (a decipherment, a key sheet, a printed edition)?; (b) Bourdeau's and Aymeloglu's repositories, grep for Juan Manuel /
RAH Salazar A.23 / R95xx DECODE ids (clone shallow, grep only); (c) DECODE listing records R9501-R9530 (tools/decode_list.py, login-free)
for "Status: Decrypted" or attached decipherment documents; (d) RAH catalogue description of Salazar A-23 (OAI-PMH per the CLAUDE.md
host table, no Anubis pages); (e) Google Books API (`&country=US&key=...`) and IA be-api full text for "Juan Manuel" + cifra/descifrado
+ 1522/1521, <= 20 calls; (f) Kolosova: whether any open route to her 2017 thesis annex exists other than the Teseo PDF (L17). Result:
list every published decipherment located (which letter, where, page), or "none located by <method>". Do not decode; do not classify
novelty. Update Remaining gaps / Escalation [print] line and gaps_check.

### R12-SURSWP2 -- na-suriname-map-1781, 1-in-4 sweep of NA 1.05.03 inv. 373 scans 0270-0599 for further glossed cipher (cap 3.5, box 60 min)
Intake gate: `na-suriname-map-1781: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`.
The Verdict's cheapest next, exactly as R11-SURSWP ran 0005-0269 and 0800-1024 (NOTES.md section "R11-SURSWP-..."): reuse its
passes/inv373_sweep_r11/ scripts (plan.py, fetch.py, sheets.py) extended to 0270-0599, every 4th label skipping scans R10-SUR already
sampled, 600 px thumbnails from service.archief.nl IIIF one at a time >= 1.9 s apart (<= 90 requests), contact sheets with scan 0693 as
the positive control tile on every sheet, read by your own eye; zoom any candidate from the thumbnail, and at most 3 candidates at a
higher size. Write passes/inv373_sweep_r12/look.tsv (one row per scan, cipher/gloss/key flags). If a glossed cipher passage is found,
record scan numbers and a one-line description only; do not transcribe in this job. Update the Verdict / Remaining gaps, gaps_check.

### R12-CATOK23 -- catokwacopa-1875 (pollaky-1865-1875 gap 3), spec tests 2-3 with a synthetic-line control (cap 5.5, box 80 min)
Intake gate: run `python3 tools/intake_gate_check.py catokwacopa-1875` and `... pollaky-1865-1875` yourself and paste both; if the
catokwacopa gate exits non-zero, stop and report.
specs/catokwacopa-1875.json cheap tests 2 and 3, on our own pairs.tsv (NEXT-CAT, 2 Oct 2026). Test 2: independently re-derive the
exact-fit name search that forces CONINGTON/JOWETT/SHIRLEY/HERTFORD (Bourdeau's catokwacopa, MIT, cite it; read his NOTES and ads.py
for the omission rule, write our own script) against our own period proper-noun list (built from open sources you can cite: e.g. 1870s
peerage/baronetage/House of Commons lists on IA, gazetteers) -- does each forced line stay unique under our list and not only his?
Test 3: the five unread lines (9, 12, 23, 26, 29) against an enlarged period vocabulary under the same omission rule, with the matched
control the spec names: how often the forced-fit method returns a unique answer on synthetic lines of the same length and omission budget
built from random period English. Pre-register both tests and the uniqueness criterion (PREREG committed and pushed before scoring).
Report target and control numbers side by side in HYPOTHESES.md and the spec's cheap_test_done; grade any line reading per rule 4 (S
only with the control passing). Update catokwacopa's and pollaky's Remaining gaps / Escalation, gaps_check both; NEAR.md pollaky row's
numbers if they change (tools/near_check.py exit 0).

### R12-CLINVHS -- pro3055-clinton-1779, the 2380 witness conflicts against the printed VHS Collections II (1871) p.192 (Sonnet 5.5, cap 1.5, box 30 min)
Intake gate: `pro3055-clinton-1779: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`.
NOTES.md lines ~1174, 1253, 1323 say VHS Collections II p.192 "not checked" for the 2380 conflicts (the cipher lacks "with the 650
Recruits and Artillery from Europe" in p.121 and the P.S.; move/movements; Chesapeak/Chesipeak). Find the volume on IA (advancedsearch
+ the item's _djvu.txt; page image of p.192 if OCR is doubtful, <= 15 archive.org requests) and record, per conflict, which witness the
print follows (quote it). Witness record only (rule 4: no majority vote; nothing in the key or reading changes). Also: the verifier
R11-CLINV5 asked that a later session drop the bar at c4.6 in passes/.../p122_reconciled.tsv and rerun check_2380_p122.py -- do that and
record the rerun output. Update the 2380 conflicts entry and AUDIT.md's 2380 section only by appending a dated witness note.

### R12-CRUSLB -- ra-crusenstolpe-1809, Litteraturbanken.se Crusenstolpe author page and texts via a real browser or its JSON API (Sonnet 5.5, cap 1.5, box 30 min)
Intake gate: `ra-crusenstolpe-1809: open (line 1) -- edition/page or full-text-search citation found within 6 lines`.
NEXT-STEPS parallel action: the author page is JS-rendered (NOTES.md line 81). Try litteraturbanken.se's own JSON API first (find it from
the page's network calls or its public docs), else tools/browser_fetch.js; list Crusenstolpe's works held there and full-text search them
for chiffer / chiffre / 1809 / Portefeuille / the cipher's own named details in NOTES.md. <= 40 requests to the host, >= 1.5 s. Record
each query and hit; update the While waiting / Verdict lines.

### R12-LVN16 -- lodewijk-van-nassau-1573-74, letter 4616 image-check: its 27 M tokens and 19 unsegmented digit groups at 300 dpi (cap 4.5, box 70 min)
Intake gate: `lodewijk-van-nassau-1573-74: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`.
Remaining gaps item 3 (transcription, not-attempted for 4616): 4616 carries 27 M tokens and all 19 unsegmented digit groups (e.g.
81/28/2), read so far only from 150-dpi images. Re-derive 300-dpi line crops for just the lines carrying them (regen_images.sh /
images_manifest_full.tsv give the source; tools/iiif_lines.py --image or --ark/--canvas, paste the command), one page per Sonnet call,
two blind passes on those crops + your reconciliation (~4-5 units). Settle each token from the image where you can; segment each digit
group into key_full codes (decode_key.py --split-check helps, the image decides). Write corrections to ciphertext_4616.tsv only with a
per-row note, regenerate with the folder's decode (decode_4616_full.json) and --check exit 0; recount C/H/M/U for 4616 and the
57.5% figure; flag a verifier in ROOM if the reading changed. Update Remaining gaps item 3 / Escalation image-check, gaps_check.

## Wave 2 (spawned as wave-1 slots free, from 11:3x UTC 6 Oct). Intake gates 11:2x UTC.

### R12-KAL8 -- kaliningrad-2015, the R10-KAL7 lexicon word-segmentation driver on the remaining schemes S1, S1s, S3, S3-soft and German (cap 3.5, box 60 min)
Intake gate: `kaliningrad-2015: open (line 1) -- edition/page or full-text-search citation found within 6 lines`.
NOTES.md "R10-KAL7" Next steps: the same driver, no tool change, on each remaining scheme (lexicon from a held-out book group of the
matching corpus in tools/data: ru19 / ru19_lat / ru19_soft; de19 or de1600 for German as NOTES.md's earlier rows chose). One PREREG for all
five schemes before scoring (gate, positive control per scheme = a synthetic text of the same N through the same scheme, shuffle
control); one HYPOTHESES.md row per scheme with both numbers. A scheme whose positive control misses its gate is a non-test, not a
negative. Stop before starting a scheme that would cross 80% of cap or box. Update Next steps / Verdict.

### R12-OLDCORP -- na-oldenbarnevelt-2442-1605 step (d'): an era-matched Spanish judge corpus, state letters 1598-1621 (cap 5, box 75 min)
Intake gate: `na-oldenbarnevelt-2442-1605: open (line 1) -- edition/page or full-text-search citation found within 6 lines`.
Build `tools/data/es1600/` from public-domain printed state correspondence of 1598-1621 (CODOIN volumes on IA, _djvu.txt, letters of the
period only, editorial apparatus stripped by script; >= 5 source files so the fold check means something), with a README naming every
source (IA identifier, volume, pages kept) and the stripping rule. Register it in tools/judge_plaintext.py's LANG_CORPORA the way es17c /
pt18 were added (read their commits), add an offline test, and run the held-out leave-one-file-out false-negative check: report the
blended rate AND the per-fold spread (CLAUDE.md rule 3, es17c/en paragraphs). Then, only if na-oldenbarnevelt-2442's committed reading
exists, score it under es1600 beside es17a and the shuffled-null controls and paste both outputs. No reading or key change. Update the
folder's Next steps; name the corpus in SYSTEM.md if system_map_check requires it (run tools/system_map_check.py).

### R12-SURSIGN -- na-suriname-map-1781, one Opus blind call on context tiles: L08:51 / L10:30 g|l and [sigma] L11:17 vs L10:66 (cap 4, box 50 min)
Intake gate: `na-suriname-map-1781: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`.
NOTES.md "While waiting" (line ~2556): R7-SUR's single-sign Sonnet look failed its control gate. Cut 2-3-sign context tiles for the
four named tokens plus known-answer tiles of g, l and [sigma] from glossed context (the control), shuffled together, unlabeled; PREREG
(control must score >= the gate you register before the target tiles are read) committed before the call; one blind Opus subagent call
on the tile sheet. Report control and target answers side by side; settle a token only if the control passes. Any change: decode --check
exit 0, verifier flag. Wait for R12-SURSWP2's done line in ROOM.md before pushing NOTES.md edits (rebase; keep both facts).

## Wave 2b (spawned 11:4x UTC 6 Oct, with wave 2). Wave 1: five done (5 D), workers so far 8.50 (get_session).

### R12-LVNV -- verifier, lodewijk-van-nassau-1573-74: carry R12-LVN16's 4616 reading revision into AUDIT.md (cap 2.5, box 40 min)
You are a verifier, not the solver (R12-LVN16, commit 0d10d1b6e). CLAUDE.md rule 10 propagation paragraph and "Verifier brief" item 4:
re-run the folder's 4616 decode --check yourself; open at least 8 of the settled rows and 4 of the 14 split slash groups against the
300-dpi crops the worker cut (images/... per its NOTES section) and say for each whether the image supports it; check the PREREG
predates the scored control (git log times); check the "121 -> 221 hollande H" change against key_full and its witness. Then update
AUDIT.md (dated section: counts before/after, 57.5% -> 58.3%, any row you overturn, which you mark in a corrections note rather than
editing the worker's files) and any SECOND-OPINIONS-QUEUE.tsv row for this target, and depth fields in status.json only via
tools/depth_check.py if the depth figure moves. N-class unchanged unless the text changes what was printed. Do not decode anything new.

### R12-LVN10 -- lodewijk-van-nassau-1573-74, letter 4610 image-check: its 131 M tokens at 300 dpi (cap 6, box 80 min)
Intake gate: `lodewijk-van-nassau-1573-74: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`.
The same protocol R12-LVN16 used on 4616 (read its NOTES.md section and scripts first; reuse settle.py with --letters 4610): 300-dpi
line crops for only the lines carrying 4610's M tokens (paste the crop command), one page per Sonnet call, two blind passes per page +
your reconciliation (units: pages x 2 + 1 at ~1.5; state the page count in your claim and stop before a page that would cross 80% of
cap or box), the same pre-registered known-answer control on H rows (PREREG pushed before scoring). Corrections to ciphertext_4610.tsv
with per-row notes, decode --check exit 0, recount, ROOM flag for a verifier (the reading changed after AUDIT.md). Coordinate with
R12-LVNV (verifier on 4616, running now): rebase before touching NOTES.md; never edit AUDIT.md. Update gaps item 3, gaps_check.

## Wave 3 (spawned 11:5x UTC 6 Oct). Wave 2: SURSIGN stopped (step already run, R7-SUR2/R8-SUR3 -- the brief's stale source, not the
worker's error), LVNV done (2 rows overturned), LVN10 control FAIL (nothing applied; pass B truncated past crop 11); KAL8, OLDCORP,
CATOK23 live. Workers so far 15.91 ledgered. Intake gates 11:5x UTC as wave 1.

### R12-RJM42 -- rah-juan-manuel-1521, held-out test of both letter alphabets on R9502's first page (f.42) (cap 6.5, box 85 min)
Intake gate: `rah-juan-manuel-1521: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`.
The Verdict's cheapest next (R11-RJMKEY, R12-RJMPUB): two blind passes (shared inventory, sorter labels as they stand) on R9502's first
page, crops only (paste the crop command; DECODE full-size image per NOTES.md routes, one browser login at most), plus a read of the
period decipherment's clear text for the same letter (Salazar A.23 f.42 "Texto descifrado" -- locate it on the record's images; if it is
not on any image you can reach, stop after the passes and say so). PREREG before scoring (pushed): the alignment method fixed in
advance, the statistic (letter-hit rate of each key on aligned letter-cipher tokens), shuffled-key controls, and the gate. Note that
Tomokiyo prints this letter's first line (R12-RJMPUB): exclude that line from the scored span or score it separately, so the held-out
claim is clean. Units: 2 passes + 1 reconciliation + 1 gloss read at ~1.5 + floor; stop before a unit that would cross 80%. Report both
keys' numbers and controls; no key/grade change unless a key passes. Update Remaining gaps / Escalation, gaps_check.

### R12-RJMFRAG -- rah-juan-manuel-1521, where is the 6 Jun 1522 letter (Salazar A-24 ff.147-148) "Publicado un fragmento en ..."? (Sonnet 5.5, cap 1.5, box 30 min)
Intake gate: as R12-RJM42.
Rule-1 lead from R12-RJMPUB. Find the venue the Índice de la colección Salazar y Castro cuts off (Google Books snippet queries inside the
Índice volume for the entry, `&country=US&key=...`, <= 15 calls; sources/salazar-castro-index/ on disk first), then check the venue
itself (IA / Google Books full text) for the fragment: which letter, which lines, clear or deciphered, page. Record in NOTES.md's
published-decipherment section; update the [print] Escalation line. Do not decode; do not classify novelty.

### R12-SURSWP3 -- na-suriname-map-1781, inv. 373 offset sweep (labels n = 2 mod 4) for further glossed cipher (cap 3, box 50 min)
Intake gate: `na-suriname-map-1781: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`.
The Verdict's next (R12-SURSWP2/R12-SURSIGN): the same scripts and protocol as passes/inv373_sweep_r12/ (control 0693 tile on every
sheet), labels = 2 mod 4 across 0005-1024 skipping everything already sampled, <= 120 IIIF requests >= 1.9 s apart, stop at the ceiling
and record the covered range. look.tsv in passes/inv373_sweep_r12b/. Candidates: scan numbers and one line only. Update Verdict, gaps_check.

### R12-LVN16R -- lodewijk-van-nassau-1573-74, R12-LVNV's two follow-ups on 4616 (cap 2, box 35 min)
Intake gate: as R12-LVN16 (wave 1).
(1) Fix lvn16/score.py to read lvn16/ciphertext_4616_pre.tsv (AUDIT.md "R12-LVNV": the logged reproduce line rewrites aligned.tsv against
the post-apply file); rerun and confirm 193/210 and 194/210 and a byte-identical aligned.tsv. (2) The eye pass R12-LVNV named on the 12 H
control rows both readers contested (3 vs 7, 8 vs 9): open each at 300 dpi from the existing crops yourself, record what the image shows
beside the H value; this tests the control, not the target -- if the H value looks wrong on the image, list it as a possible key-sheet or
transcription conflict for a verifier (do not edit key or H rows). Push; ROOM done line.
