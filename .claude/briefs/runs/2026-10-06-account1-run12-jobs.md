# LANE LANE-RUN12-account-1 jobs (account 1) -- 6 Oct 2026 17:4x UTC, lane orchestrator session_01NQQk5gfYfSCVJn2DyEdxFZ

Lane brief: .claude/briefs/default-lane.md (cap 60, box 17:40 UTC 6 Oct - 03:40 UTC 7 Oct). Gate 0a: SESSION-SWEEP-account-1 row still
`claimed` since 5 Oct 22:40, past the 90-min wait, proceeding as RUN11 did. Folders a-h, runnable rows only. Queue-row propagation flags
(oldenbarnevelt R14-OLDF2, august-van-saksen G4) already done (R14-OLDV 15:56, R11A-AVSV2 16:05). VERIFY-BACKLOG: fr16142 counted rows (high)
now free (DEFAULT-1240 closed 14:26). Gallica probe 17:4x: 200. Intake gate (tools/intake_gate_check.py) exit 0 at 17:4x for fr5160-letellier-1653,
heinsius-vanhaersolte-1703, fr16045-pisany-rome-1585, decode-2678-bnf-colbert127-gravel-1665, eckert-1862, august-van-saksen-1561-64,
decode-1411-hhsta-vienna-1600, baluze167-davaux-1637 ("edition/page or full-text-search citation found within 6 lines" each).
Excluded: Birago (incl. nevers-birago), Armstrong, Debosnys, anything owner-sorter-gated, any folder with a live ROOM claim < 6 h and no done.
Every worker: one job, then stop. Each job first checks its named step is still undone (NEXT-STEPS.tsv lags the folders); if a dated NOTES.md
section or ROOM done line already ran it, correct the folder's next-step line, stop and report.

## Common rules for every job
- First commands: `git fetch origin && git checkout -B main origin/main`, `python3 tools/room.py --start`, `date -u`, then a ROOM claim
  line with `tools/room.py` naming your job id, folder, cap and box end time, addressed "for LANE LANE-RUN12-account-1".
  If --start fails to push from a detached HEAD: `git push origin HEAD:main; git checkout -B main HEAD`.
- Read the folder's NOTES.md tail (Remaining gaps / Escalation / latest dated sections), HYPOTHESES.md and AUDIT.md section list first.
- Good-citizen rule and the CLAUDE.md host table for every request (one request per host at a time, >= 1.5 s apart; stop a host on
  429/403/challenge, one retry after a pause at most). Report request counts per host. Gallica: one probe first; if it fails, stop and say so.
- Rule 3: any gate is pre-registered (a PREREG file committed and pushed before the scored run), with a matched control that can vary on
  the statistic tested; report both numbers. Rule 4 grades with counts. Rule 7: `tools/decode_key.py <folder> --check` (or the folder's
  own decode script --check) exit 0 before push if the reading or key changed. A reading change after AUDIT.md: say so in NOTES.md and
  flag in ROOM for a verifier.
- Rebase before writing shared files (status.json, PROGRESS.tsv, ROOM.md, HYPOTHESES.md); keep both facts on conflict. Run
  `python3 tools/file_shrink_guard.py <every file you touched>` before the final push; push with `python3 tools/room.py --push <paths>`.
- Partial targets: update "## Remaining gaps" / "## Escalation" (Verdict line) and pass `python3 tools/gaps_check.py <target>`.
- Words: never "solved", "cracked", "novel", "first", "new" for anything this project did; rule 10 wording only. Never name the
  owner; never print credentials (test presence with `test -n`). Never call AskUserQuestion. Solver/lookup jobs: report what was found
  and where it was not found; do not classify novelty.
- Stop at the cap or at 80% of the box, whichever first; do not start a unit that would cross 80% of either. A stop with work half
  done writes what was done and what remains into the folder's files. An Opus session floor is about 1.5; caps below assume it.
- Vision work: crop step mandatory and pasted (`tools/iiif_lines.py --image FILE --out DIR` or the --ark/--canvas form); give
  subagents only crop paths, one page/leaf per call, never a full-page image. Price: ~1.5 per Sonnet subagent pass, reconciliation = 1 unit.
- Sorters: any sorter meant for the owner must PASS `python3 tools/sorter_preflight.py` and have 5+ random tiles opened against the line
  image before it is handed on; it is handed to the account-3 orchestrator (ROOM flag line) to publish. Never publish an artifact or edit
  ASKS.md yourself.
- Done: one ROOM line `done (<start>-<end> UTC by date -u, brief met|stopped at cap): <result, commit>` "for LANE LANE-RUN12-account-1",
  then a five-line final report.

## Wave 1 (spawned 17:4x UTC)

### R12A-NOXV (VERIFIER) -- fr16142-noailles-constantinople-1571, VERIFY-BACKLOG rows "Noailles c262 25 Apr 1572" and "Noailles c510-516 7 Jul 1574" (missing: counted, priority high). Cap 2.5, box 45 min.
You are a verifier, not a solver: do not decode. Read VERIFY-BACKLOG.tsv's two rows, AUDIT.md (VER1-NOX AUDIT 1: both N0 D0, text known),
the D1-F16142A section (6 Oct: 2 of 36 labels PASS S), PROGRESS.tsv rows 51-52 and status.json's fr16142 results. Apply rule 4/4a with
`tools/depth_check.py`: set depth, depth_pct, depth_sentence, depth_check, decode_status in status.json and the count decision in PROGRESS.tsv
(an N0 item is "not countable" -- say so with depth_check.py's output pasted into AUDIT.md "## Count (R12A-NOXV)"). If anything since AUDIT 1
(D1-F16142A's 2 S labels, R10-NOX2 gloss lines) changes depth, carry it in; never raise the N-class. Re-run `python3 tools/verify_backlog.py`
and confirm both rows move to "no verifier action". Do not touch the Dupuy date-only text-check (another job).

### R12A-F5160 -- fr5160-letellier-1653, Colbert 26 part III sweep (canvases 405-779, ark btv1b10035069t). Cap 4, box 70 min.
NOTES.md "R11A-F5160" (1) lists the 271 unchecked canvases; Gallica was down then. Fetch each unchecked canvas once at a small size (thumbnail,
e.g. /full/600,/0/default.jpg; >= 1.5 s apart; manifest once) and screen for figure-group cipher with a script-first pass (ink-density / digit-run
heuristic is fine as a pre-filter) and your own eye on flagged pages only, in batches of at most 20 thumbnails per look. Record per canvas
(cipher / clear / blank) in colb26/sweep_405_779.tsv; for any cipher page, its canvas, folio label and a 1-line description; no transcription.
Unit = 20 canvases ~0.3. Update Remaining gaps / Escalation / next-step line.

### R12A-HEIN -- heinsius-vanhaersolte-1703, Deel 3 the 16 unread H.A. 918 pages. Cap 2, box 40 min.
NOTES.md "Next step" item 2: read the 16 pages R11A-HEIN3 left (listed in its section), same method and source as R11A-HEIN3 (IA text/pages
on disk or one fetch each), and say per page whether the print shows cipher numbers, spaced passages, a key or a number-to-word pair.
Record in the same TSV R11A-HEIN3 wrote. Update the Next step section.

### R12A-PISRS -- fr16045-pisany-rome-1585, finish D4-PISRS's killed f.275r control/null and commit the 4 shape-settled T36 labels. Cap 3, box 60 min.
D4-PISRS stopped at cap with the f.275r control/null killed (resume: `python3 pisrs/pisrs.py f275r`). (a) Run it to completion and write the
f.275r numbers beside f.244r's in the D4-PISRS section and HYPOTHESES.md (gain vs random 9-token relabels). (b) Remaining gaps' cheapest next:
commit the 4 f.275r shape-settled T36 labels into tx86e with the downstream regeneration (disk only); decode --check exit 0; any reading change
after AUDIT.md -> NOTES note + ROOM verifier flag. Disk only, no requests. Gaps_check.

### R12A-G2678 -- decode-2678-bnf-colbert127-gravel-1665, the 6 unlooked 1664 Gravel leaves in Mél. Colbert 120-124. Cap 3, box 50 min.
NOTES.md "D1-DEC2678M" names the six leaves (and how they were located); Gallica was down then. Look at each leaf (one canvas fetch each at a
readable size, line crops only if a page has figure groups) for figure-group cipher. Record per leaf in the folder's sweep TSV; if a cipher
leaf turns up, its canvas/folio and a 1-line description, no decode. Update the key-rebuild gap line and Verdict. Gallica probe first.

### R12A-ECKV (VERIFIER) -- eckert-1862, grade decision on the Lehigh/Hurlbut row (D1-ECK62S, 6 Oct). Cap 2.5, box 45 min.
You are a verifier, not the solver: D1-ECK62S found Lehigh 13 uses in sent ledgers mssEC 18-19, 10 date-aligned to OR, 8 print-read all Canby
(6) or "can be" (2), 0 Hurlbut, held M "for a verifier grade decision". Read ec18/lehigh_uses.tsv, the D1-ECK62S section and AUDIT.md; decide
the grade of the affected token(s) per rule 4 (C needs known plaintext matched to this very use; a period key value read elsewhere is not C for
this token unless the OR print of this telegram is the plaintext), record the decision with reasons in AUDIT.md "## Carry-over R12A-ECKV",
apply it through the folder's decode script and --check (exit 0), carry into status.json / any SECOND-OPINIONS-QUEUE.tsv row for this target.
Do not run the Leghorn/Leopard sweep (another job).

## Wave 2 (spawned as wave-1 slots free, from 18:0x UTC)

### R12A-D1411P4 -- decode-1411-hhsta-vienna-1600, p.4 numerals. Cap 6.5, box 90 min.
Verdict's cheapest next: cut and read p.4 numerals in two blind Sonnet passes against the frozen T21r, reconcile, and score with the same
coverage controls D4-1411P3 used for p.3 (shuffled p99, shifts max, leaf gloss reference; pre-register before scoring, copy D4-1411P3's prereg).
Units: crops 1 + 2 passes + 1 reconcile + scoring 1 = 5 x 1.5 (well, ~1.3 each with Opus floor). Report both numbers; grades with counts.

### R12A-BALS -- baluze167-davaux-1637, sign sorter for the 170 f.228 hand. Cap 3, box 50 min.
Verdict's cheapest next. Build the sorter from D1-BAL170B's reconciled f.228r/f.228v crops with tools/sign_sorter.py (TRANSCRIPTION.md),
PASS tools/sorter_preflight.py, open 5+ random tiles against the line image, then flag it to the account-3 orchestrator in ROOM to publish.
Do not decode f.228 (that waits on the owner's sort). Update Remaining gaps / Escalation.

### R12A-SEUT -- fr3151-seure-1558, Tournon 1556 key from fr. 3138 fo. 22r. Cap 6, box 90 min.
Verdict's cheapest next: cut fo. 22r (13 lines, slip decipher legible at M) with tools/iiif_lines.py --ark/--canvas (gallica_folio.py for the
canvas), build an image-exemplar reference sheet from the leaf, two blind Sonnet passes against it, reconcile; then try the Tournon key on the
items 43/44 cipher body ONLY through a pre-registered gate with a matched control (same key on shuffled cipher / wrong-key control as R9-SEURE2
did for La Guiche). Units: crops 1 + sheet 1 + 2 passes + 1 recon + test 1 = 6 x ~1. Gallica probe first.

### R12A-AVS175 -- august-van-saksen-1561-64, WVO 175 pp.3-8 for a hand that separates Qf. Cap 4.5, box 70 min.
RUN11 handoff item (3): look at WVO 175 pp.3-8 (on disk per images/inventory.tsv, or one fetch each from the R21 route) for a glossed hand
that separates Qf (126's K and Qf M); crops first, then at most 5 lines read in one Sonnet pass; any grade change only through a pre-registered
test; a reading change after AUDIT.md -> NOTES note + ROOM verifier flag (N4 target). Gaps_check.

### R12A-ECKLEG -- eckert-1862, Leghorn/Legend/Leopard date-aligned sweep (after R12A-ECKV). Cap 3, box 50 min.
Verdict's first half: the same date-aligned sweep D1-ECK62S ran for Lehigh (ec18/lehigh_uses.tsv, its script), for Leghorn, Legend and
Leopard in mssEC 18-19 sent ledgers, against the OR print. Record in ec18/<word>_uses.tsv; no grade change by the worker (hand the result to a
verifier via ROOM flag if a grade would move). decode --check exit 0.

## Wave 3 (from 18:1x UTC)

### R12A-REQ2678 -- decode-2678-bnf-colbert127-gravel-1665, draft REQUEST.md for AE CP Allemagne 194 (ASKS row 150). Cap 2, box 40 min.
Draft `ciphers/decode-2678-bnf-colbert127-gravel-1665/REQUEST.md` per CLAUDE.md access playbook item 4 and outreach/README.md (rule 1 AI
disclosure, rule 1a voice): what is needed (the Gravel cipher letters of Jan-May 1665 in AE CP Allemagne 194, and why: a second text in the
f.349 key for code 29 and cells 22:/0), the institution's public contact address read from its own contact page with the date (Archives
diplomatiques, La Courneuve), subject line, blank recipient-name and sign-off placeholders, links per Outreach gate (6). Status `drafted`; do
not send, do not run the gate-7 fact check yourself (a separate session does). Write a ROOM flag naming the draft so the account-3
orchestrator queues the gate-7 check. Update the folder's Remaining gaps line to "waiting-on ASKS 150". Rule 9: no personal data.
