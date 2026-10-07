# LANE-AM-0914 jobs (account 2) -- 7 Oct 2026 10:3x UTC, lane orchestrator session_01Ng5f2sUU7u1X9HukiLR7mf

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

## Wave 1 (spawned 10:3x UTC 7 Oct). Intake gate output (10:2x UTC) pasted per job.

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
