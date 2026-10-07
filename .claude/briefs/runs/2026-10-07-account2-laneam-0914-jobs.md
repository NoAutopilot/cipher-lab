# LANE-AM-0914 jobs (account 2) -- 7 Oct 2026 10:1x UTC, lane orchestrator session_01Ng5f2sUU7u1X9HukiLR7mf

Lane brief: .claude/briefs/runs/2026-10-07-acct3-lanes-0914.md (LANE-AM-0914 section) + .claude/briefs/default-lane.md. Folders a-m only;
cap 40, box 10:12-16:12 UTC 7 Oct. Gate 0a: SESSION-SWEEP-account-2 row `claimed` since 5 Oct, never closed (>90 min) -- proceeding.
Backlog a: VERIFY-BACKLOG regenerated 10:12 UTC -- a-m rows are Birago (off limits) or "no verifier action". Backlog b: `tools/next_steps.py
--hot-only`, each row checked for freshness against NOTES.md dated sections and ROOM.md 6-7 Oct lines (FRESH-0914 still queued, so done here).
Stale rows corrected at 0 cost: fr16045-pisany T40 gap row (its named page-internal compare ran as D07-PISSD), fr3621-dinteville While-waiting
sorter item (built DIN-SORTER). Excluded: Birago, Armstrong, Debosnys, FRESH-0914's items (Monluc, rah-juan-manuel), owner-sorter-gated steps.
Every worker: one job, then stop. First check the named step is still undone (NEXT-STEPS.tsv lags the folders); if a dated NOTES.md section or a
ROOM done line already ran it, correct the Verdict line, report, and stop.

## Common rules for every job
- First commands: `git fetch origin && git checkout -B main origin/main`, `python3 tools/room.py --start`, `date -u`, then a ROOM claim line
  with `tools/room.py` naming your job id, folder, cap and box end time, addressed "for LANE LANE-AM-0914". If --start fails to push from a
  detached HEAD: `git push origin HEAD:main; git checkout -B main HEAD`.
- Read the folder's NOTES.md tail (Remaining gaps / Escalation / latest dated sections), HYPOTHESES.md and AUDIT.md section list first.
- Good-citizen rule and the CLAUDE.md host table for every request (one request per host at a time, >= 1.5 s apart; stop a host on
  429/403/challenge, one retry after a pause at most). Report request counts per host.
- Rule 3: any gate is pre-registered (a PREREG file committed and pushed before the scored run), with a matched control that can vary on the
  statistic tested; report both numbers. Rule 4 grades with counts. Rule 7: `tools/decode_key.py <folder> --check` (or the folder's own
  decode script --check) exit 0 before push if the reading or key changed. A reading change after AUDIT.md: say so in NOTES.md and flag in
  ROOM for a verifier.
- Rebase before writing shared files (status.json, PROGRESS.tsv, ROOM.md, HYPOTHESES.md); keep both facts on conflict. Run
  `python3 tools/file_shrink_guard.py <every file you touched>` before the final push; push with `python3 tools/room.py --push <paths>`.
- Partial targets: update "## Remaining gaps" / "## Escalation" (Verdict line) and pass `python3 tools/gaps_check.py <target>`.
- Words: never "solved", "cracked", "novel", "first", "new" for anything this project did; rule 10 wording only. Never name the owner; never
  print credentials (test presence with `test -n`). Never call AskUserQuestion. Solver/lookup jobs: report what was found and where it was
  not found; do not classify novelty.
- Stop at the cap or at 80% of the box, whichever first; do not start a unit that would cross 80% of either. A stop with work half done
  writes what was done and what remains into the folder's files. An Opus session floor is about 1.5; caps below assume it.
- Vision work: crop step mandatory and pasted (`tools/iiif_lines.py --image FILE --out DIR` or the --ark/--canvas form); give subagents only
  crop paths, one page/leaf per call, never a full-page image. Price: ~1.5 per Sonnet subagent pass, reconciliation = 1 unit.
- Sorters for the owner: `tools/sorter_preflight.py` PASS, handed to the account-3 orchestrator by ROOM flag; never publish or edit ASKS.md.
- Done: one ROOM line `done (<start>-<end> UTC by date -u, brief met|stopped at cap): <result, commit>` "for LANE LANE-AM-0914", then a
  five-line final report.

## Wave 1 (spawned 10:1x UTC 7 Oct). Intake gate output (10:1x UTC) pasted per job.

### AM-D1411P5 -- decode-1411-hhsta-vienna-1600, p.5 numerals, two blind passes + frozen T21r (Opus; cap 7.5, box 80 min)
Intake gate: `decode-1411-hhsta-vienna-1600: open (line 3) -- edition/page or full-text-search citation found within 6 lines`.
Folder Verdict (D07-D1411, 7 Oct 01:0x UTC): "cut and read p.5 numerals in two blind passes with the frozen T21r, same coverage and gloss
controls, ~$6". Opens unread text (pages 5-12 untranscribed). Full-size images are on disk from GAPS137 (check images/manifest.json; do not
refetch). Use per-number tiles or 4x line tiles as D07-D1411 did (line crops at 1840x112 were void in R12A-D1411LA -- digits too small).
PREREG first: frozen T21r table (no re-fit on p.5), the same coverage statistic and order-shuffled/key-permuted controls as R12A-D1411P4,
and, if p.5 carries gloss, the gloss-agreement control. Units: crop sheet 1 + pass A 1 + pass B 1 + reconciliation 1 + scoring 0.5 = ~4.5 x
1.5 + floor. If p.5 is too long for one call per pass, split by half-page and stop before a unit that crosses 80% of cap. Write p5 files beside
p4's, update Remaining gaps / Escalation / Verdict, gaps_check.

### AM-NEVF27 -- fr3416-nevers-fils-1589, period gloss over fr.4715 f.27r L09 at the lone '1' (Opus; cap 4.5, box 50 min)
Intake gate: `fr3416-nevers-fils-1589: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`.
Folder Verdict (D07-NEVF25): read the period interlinear gloss above f.27r L09 (crops in sibling_f27/, canvas f67 of btv1b52509819x) where
both blind passes saw a lone '1' between "onnehorscestes" (frame 1) and "aumoins" (frame 0). PREREG first: what the gloss must show for the
lone-figure frame switch to count as a C-grade witness of key-no.25 practice (e.g. the gloss runs straight from "...cestes" to "au moins"
with nothing for the '1'), and a control (the same question on a gloss span over a known null or a known code). If the gloss settles it,
re-judge f.35r token 79 (45 79 vs 4 57 9) only under the PREREG rule, re-run `decode_f35.py --check`, and flag ROOM for a verifier if any
count moves. Do not transcribe the rest of f.27r (that is a separate ~$30 job; name it in Remaining gaps if not already there).

### AM-ECK64N2 -- eckert-1864, the Cipher No. 2 twin of O9-AE on mssEC 19 p.61 (Opus; cap 2.5, box 40 min)
Intake gate: `eckert-1864: partial (line 3) -- edition/page or full-text-search citation found within 6 lines`.
NOTES.md line ~589 (B0709-A1, 7 Oct): above O9-AE on p.61 the same order went in Cipher No. 2 as a "(No 2)" entry, Buckley to Hunter at New
Orleans, 30 Apr 1864, not yet in the folder. Job: transcribe that entry from the p.61 image (the IIIF route B0709-A1/R10-ECK64C used; crop
command pasted), decode it with key-no2.md (the folder's No. 2 decode route), and compare word by word with O9-AE's plain. Grade per token
(C where O9-AE's plain fixes the word, H where key No. 2 reads it). Report agreement count and any code word whose No. 2 value differs from
key-no2.md (a key correction or a clerk variant). Update Remaining gaps / Verdict, gaps_check, decode --check.

### AM-ECK62Q -- eckert-1862, dated `?p` mssEC 18 entries under split2 against the image for marker words (Opus; cap 4.5, box 60 min)
Intake gate: `eckert-1862: partial (line 3) -- edition/page or full-text-search citation found within 6 lines`.
Folder Verdict (D07-ECK62, 7 Oct): "the dated `?p` mssEC 18 entries under split2 against the image for marker words, ~$4". Take the dated
`?p` entries from ec18/s2/ (print_q), pick the image pages by date, crop each entry (command pasted), and check by eye or one blind pass per
page for marker words the volunteer transcription dropped (signature/route words, Hurlbut/Grant, "No 2"/"No 3" book markers). PREREG first:
what a marker word must look like to move an entry from `?` to a book, and a control (the same look at entries already assigned to a book,
which must come out right). Units: priced per page crop call, stop before 80%. Record entries moved, grades, ec18.py --check / decode --check.

### AM-LOOK -- five catalogue/lookup items, a-m (Sonnet 5.5; cap 3, box 60 min; no deep work, no transcription)
Each item: check it is still undone (grep the folder NOTES.md), do it, append a dated "## AM-LOOK (7 Oct 2026)" paragraph to that folder's
NOTES.md with what was searched, hits, and requests per host; fix the folder's While-waiting / Verdict line if the item is now done. Stop
each item at ~0.5.
1. bl-farnese-cipher: a full-view copy of Cardauns 1909 (Nuntiaturberichte aus Deutschland 1. Abt. Bd. 5, Legationen Farneses und Cervinis
   1539-1540) on IA (advancedsearch, title/creator variants, `bub_gb_` scans) or the Google Books API (`country=US`, key), HathiTrust
   bibliographic API for an htid. If full text is found, run the folder's named phrase search in it.
2. fr3984-sega-1593: OpenAlex (Bearer key), Semantic Scholar (x-api-key), Persée, HAL, CrossRef for the Sega legation / Baudouin-Desportes
   1593 correspondence (tools/print_check.py where it fits); list secondary works that excerpt the edition.
3. fr3986-nevers-revol-1593: from the BnF archivesetmanuscrits finding aid for fr.3985/fr.3986 (catalogue only, no images), list the other
   Nevers-to-Revol letters of 1593 with folio and date, naming sibling leaves in the same copyist's hand (NOTES.md line ~529).
4. fr16045-pisany-rome-1585: does Tomokiyo (sources/cryptiana on disk first, then cryptiana.web.fc2.com) name the shelfmark of the original
   1586-87 key table he reproduces (henryiii_Vivonne5.png)? If yes, find its Gallica ark via SRU/IIIF. Remaining gaps row "key86 T40".
5. fr5160-letellier-1653: one fetch of Colbert 26 canvas 679 at `full/600,/0/native.jpg` (the two earlier tries 404'd at another size; the
   info.json gives the true size), look for cipher, and close part III in NOTES.md.

## Wave 2 (spawned 10:3x UTC 7 Oct; follow-ups named by wave 1). Intake gate output as wave 1 for eckert-1864; fr3986 below.
Wave 1 results: AM-ECK64N2 N2-L read H 13 (2f2e7308c, AUDIT flag); AM-NEVF27 non-test (control 3/14); AM-ECK62Q 0/25 moved (control PASS);
AM-LOOK 5 lookups done (fr3986 finding aid: items 68 and 75 "avec chiffre", Nevers to Revol 7 and 9 Oct 1593). AM-D1411P5 still running.

### AM-ECK64K -- eckert-1864, the Kimber entry of 11 June 1864 (Vicksburg) opening p.90, pointer 8982 (Opus; cap 2.5, box 40 min)
Intake gate: `eckert-1864: partial (line 3) -- edition/page or full-text-search citation found within 6 lines`.
Folder Verdict (updated by AM-ECK64N2): read it with key-no2.md, disk + 1 IIIF page (crop command pasted, AM-ECK64N2's strip-crop route),
check against the OR volume for its date (on disk if harvested; else one IA full-text query). Grade per token (H by key, C where a printed
twin fixes the word). Add it as the next N2 entry in reading-no2.md beside N2-L, decode_no2 --check, update Verdict, gaps_check, and add your
entry to AM-ECK64N2's ROOM AUDIT flag (one flag line naming both entries for the verifier). Report what was found and where it was not found.

### AM-REV68 -- fr3986-nevers-revol-1593, census of sibling items 68 and 75 ("avec chiffre", Nevers to Revol, Vese 7 Oct and Coire 9 Oct 1593) (Opus; cap 3.5, box 50 min)
Intake gate: `fr3986-nevers-revol-1593: blocked` (terminal state; this is a sibling census, not deep work on the target letter).
fr.3986 is Gallica btv1b9060631k (481 canvases, all "NP", so folio labels are useless; give tools/gallica_folio.py eye-checked anchors or step
through 300 px thumbnails, >= 2 s apart). Find the canvases of finding-aid items 68 and 75 (they fall between item 58, 4 Oct, and item 77, 7 Oct;
use the target letter f.198 / item 101 canvas and any item already located in NOTES.md as anchors). For each: does it carry cipher, is it the same
copyist's hand and sign family as f.198/f.298 (side-by-side crop sheet, crop command pasted, by eye), is there an interlinear decipherment or
clear-text twin? Record canvases, sign-family verdict and counts of cipher lines in NOTES.md; if same family, cut line crops into a folder
for the owner's sorter (do not build or publish a sorter) and name the next step (tiles added to ASKS 102's sorter, or a crib). No reading.
Gallica requests <= 60. Report what was found and where it was not found.

## Wave 3 (spawned 10:5x UTC 7 Oct): the two verifier flags raised by waves 1-2. Separate sessions from every solver named.
Wave 2 results: AM-ECK64K N2-M (Kimber 11 June 1864, p.90) H 13, 342df8ee9, AUDIT flag 620c2c4c8; AM-REV68 items 68 = f.146v, 75 = ff.157r-v,
same no.60 family and copyist by eye, 15 line crops in images/siblings/ (6ecaa98c3, flag for the account-3 orchestrator / ASKS 102 sorter).
AM-D1411P5: p.5 266 numbers, T21r_h12 PASS 0.628 vs gloss 0.613 (thin), S 114 / M 152, p.5 left page a copy of p.2; verifier flagged.

### AM-ECKV -- eckert-1864 AUDIT propagation for N2-L and N2-M (verifier, Opus; cap 2.5, box 40 min)
You are a separate session from AM-ECK64N2 and AM-ECK64K. CLAUDE.md "Verifier brief (template)" steps 1-5, scoped to the two entries
reading-no2.md gained after AUDIT.md was written: N2-L (p.61, Buckley to Hunter at New Orleans, 30 Apr 1864, twin of O9-AE; 2f2e7308c) and
N2-M (p.90, Kimber 11 June 1864, Burglar/QMG to Canby on the Vicksburg & Shreveport gauge; 342df8ee9). (1) re-derive both with the folder's
No. 2 decode script and `--check` (rule 7), check H 13 + H 13 against key-no2.md and the crops; (2) novelty search per entry, scaled to two
short telegrams: OR ser. I vols for the dates (N2-L's plain is O9-AE's, so its class follows O9-AE's; N2-M: OR I/34 pt 4 and the Meigs/Canby
correspondence, IA full text, Google Books with country=US, a phrase search on the decoded text), log every family searched or unreachable;
(3) N-class, key source (`period`), depth line per entry; append "## AUDIT (propagation, AM-ECKV)" to AUDIT.md, update status.json result rows
and any SECOND-OPINIONS-QUEUE.tsv row for this target if it quotes counts; a new SO row only for an entry at N3 or better. Do not decode other entries.

### AM-D1411V -- decode-1411-hhsta-vienna-1600, adversarial check of AM-D1411P5's p.5 PASS and 114 S grades (verifier, Opus; cap 4, box 50 min)
You are a separate session from AM-D1411P5 and every earlier decode-1411 solver. No AUDIT.md exists (no reading claimed); this is a rule-3/rule-4
check, not a novelty audit. Read NOTES.md "## AM-D1411P5 step" and d1411p5/. (1) Confirm the PREREG commit predates the scored run (git log
order) and list every deviation; (2) re-run the scoring script(s) and `--check`; (3) the result rests on a thin margin (0.628 vs gloss 0.613),
two post-score crop-split merges and a left page that copies p.2 (82/95 numbers equal): re-score on the independent material only (p.5 minus the
p.2 copy) and without the post-score merges, against the same controls, and report both numbers; (4) decide per the PREREG's own grade rule
whether the 114 S grades stand, drop to M, or stand only on the independent part; write the verdict as "## AM-D1411V verifier" in NOTES.md,
correct the grade counts, Remaining gaps and Verdict line if they change, gaps_check. Do not read new pages or re-transcribe.
