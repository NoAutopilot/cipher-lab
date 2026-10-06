# LANE LANE-RUN8-account-2 jobs (account 2) -- 6 Oct 2026 03:1x UTC, lane orchestrator session_01Aeemo71BBJ5bPUjGtFFtM5

Lane brief: .claude/briefs/default-lane.md (cap 60, box 03:12-13:12 UTC 6 Oct). WORK-QUEUE row 241: RUN8, same tier as RUN7 --
tools/next_steps.py runnable rows (cost band S and M) and the `parallel` action of blocked rows, ranked by closeness to a counted result,
BnF tie-break; first RUN7's own named next steps in this split. Folders i-r (account 1 a-h, account 4 s-z). VERIFY-BACKLOG.tsv has no
row in i-r needing a verifier. Off limits: Birago (incl. nevers-birago-fr3251-1572), Armstrong, Debosnys; riksarkivet-r4282-1628 (account-4
private repo). Every worker: Opus 5.5, one job, then stop. Each solver job first checks that its named step is still undone (NEXT-STEPS.tsv
lags the folders): if a dated NOTES.md section already ran it, take the folder's own Verdict "cheapest next" instead if it fits this job's
cap and box and is not a machine transcription pass the TRANSCRIPTION.md / CLAUDE.md Usage 6 sorter rule hands to the owner; otherwise
stop and report.

## Common rules for every job
- First commands: `git fetch origin && git checkout -B main origin/main`, `python3 tools/room.py --start`, `date -u`, then a ROOM claim
  line with `tools/room.py` naming your job id, folder, cap and box end time, addressed "for LANE LANE-RUN8-account-2".
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
  found; do not classify novelty.
- Stop at the cap or at 80% of the box, whichever first; do not start a unit that would cross 80% of either. A stop with work half
  done writes what was done and what remains into the folder's files. An Opus session floor is about 1.5; caps below assume it.
- Vision work: crop step mandatory and pasted (`tools/iiif_lines.py --image FILE --out DIR` or the --ark/--canvas form); give
  subagents only crop paths, one page/leaf per call, never a full-page image. Price: ~1.5 per Sonnet subagent pass, reconciliation = 1 unit.
- Sorters (lane rule since RUN7): any sorter meant for the owner must PASS `python3 tools/sorter_preflight.py` and have 5+ random tiles
  opened against the line image before it is handed on; it is handed to the account-3 orchestrator (ROOM flag line) to publish. Never
  publish an artifact or edit ASKS.md yourself.
- Done: one ROOM line `done (<start>-<end> UTC by date -u, brief met|stopped at cap): <result, commit>` "for LANE LANE-RUN8-account-2",
  then a five-line final report.

## Wave 1 (spawned 03:2x UTC 6 Oct). Intake gate output (03:1x UTC) pasted per job.

### R8-MATCUT -- matignon-mayenne-1586, deskewed re-cut of the f.110 sorter (cap 3.5, box 50 min; no vision subagent)
Intake gate: `matignon-mayenne-1586: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`.
RUN7 named step (R7-MATQA, 6 Oct 02:00, commit 5cf05d341; ASKS 146): the f.110 sorter in `sorter/` cut flat 52 px bands across 5 sloping
lines, 6/6 random tiles off label. Fix: a deskewed re-cut with `tools/sorter_recut.py` and `--region` (the sorter's build lacks it). Read
tools/sorter_recut.py --help and tools/sorter_preflight.py --help first (if scipy is missing, `pip install scipy` once). Re-cut from the
D2B-MATF110 line crops / native image on disk, rebuild per sorter/README.md, then (1) `tools/sorter_preflight.py` must PASS (paste its
output), (2) open 5+ random tiles against the line image yourself and list them with their line labels. Only if both pass: one ROOM flag
"matignon f.110 sorter re-cut, preflight PASS, ready for the account-3 orchestrator to publish, path ..." and update NOTES.md Verdict /
ASKS-146 reference text in NOTES only. If either fails after one fix attempt, write why in sorter/README.md and stop. No reading change;
status stays partial; NEAR.md row unchanged.

### R8-POLL -- pollaky-1865-1875 (NEAR row), image-check of ads 1-2 (cap 5.5, box 75 min; 2 blind passes + 1 reconciliation)
Intake gate: `pollaky-1865-1875: blocked (line 3) -- already terminal, nothing to gate` (status line reads blocked; the Verdict and the
`parallel` column name this as the action that depends on nobody).
Verdict cheapest next (GAPS211, 4 Oct): "image-check of ads 1-2 (one blind pass each plus a reconciliation, crops first), ~$4.5". Use the
page images already on disk (images/manifest.json); if an ad's image is not on disk, say so and do only what is. Crop each ad first
(paste the command), one Sonnet blind pass per ad per reader (pass A, pass B) on crops only, then `tools/reconcile_passes.py` and one
reconciliation unit from the image. Compare the reconciled text with ciphertext.txt per sign/group; any disagreement goes into NOTES.md as
a transcription correction candidate graded per rule 4 (ciphertext.txt is never silently repaired: write a corrections file and say which
tests on disk would change). If passes split by more than a tenth, stop after reconciliation and log the signs for the owner's sorter.
Status line and NEAR.md row: say whether the NEAR row's numbers change; never closed-negative (rule 5). Then gap 3 only if cap/box allow
(it will not; leave it named).

### R8-RUBIN3 -- rubin-1953, CR p.67 Block C at 300 dpi (cap 3, box 45 min; 2 blind passes + 1 reconciliation on one block)
Intake gate: `rubin-1953: open (line 1) -- edition/page or full-text-search citation found within 6 lines`.
Named next (D2B-RUBIN2, 6 Oct 00:20, commit e29f7ec5e): "CR p.67 Block C character by character, from the PDF re-rendered at 300 dpi for
that page only (re-fetch the PDF from cipherfoundation.org, 1 request; render p.67, rotate, crop Block C)". Do exactly that: 1 request,
render p.67 at 300 dpi (pdftoppm or PyMuPDF), rotate, crop Block C into line crops (paste command), one blind Sonnet pass per reader x 2 on
the crops, reconcile against the 136-char Block C on disk; settle vmie/vnie (graded M now) and the 3 K1/K2 slip positions if the image
allows. ciphertext.txt changes only with a logged witness table. Do not keep the PDF in the repo if over 5 MB (manifest + URL instead).

### R8-ROELL4 -- roell-vandedem-1809, inv. 348 scans 3-79 read in full (cap 4.5, box 60 min; scan triage by the worker, no subagent)
Intake gate: `roell-vandedem-1809: open (line 1) -- edition/page or full-text-search citation found within 6 lines`.
Named next (D2B-ROELL3, 6 Oct 00:42, commit 80b13e33e): "read scans 3-79 in full (~USD 3-4)" of NA inv. 348 (Van Dedem -> Testa handover,
Dec 1808-Feb 1809), looking for (a) any cipher or key item, (b) the 9 Feb 1809 despatch or a minute of the Constantinople legation that
the target's ciphered letter answers or encloses. service.archief.nl IIIF at a size that shows ciphered figures (not thumbnails), >= 1.5 s
apart, <= 90 requests. Record per scan in a TSV: scan, date, sender/recipient, language, cipher yes/no, one-line content. Then the folder's
Verdict line. Search result only; no novelty words.

### R8-RAY2 -- rayburn-2004, second blind transcription pass then test 2 (cap 3.5, box 50 min; 1-2 Sonnet passes + reconciliation)
Intake gate: `rayburn-2004: open (line 1) -- edition/page or full-text-search citation found within 6 lines`.
Verdict cheapest next (D2B-RAY, 5 Oct): "Wayback retry ~$0.2 (DONE as a fallback by D2B-RAY: live upload byte-identical), then second
blind transcription pass ~$1.5, then test 2 ~$1". Skip Wayback. Crop the grid rows from images/Rayburn-Cryptogram.jpg (paste command),
one blind Sonnet pass on crops, reconcile against the transcription on disk with tools/reconcile_passes.py, log the agreement rate and
disagreements (the 7 white-out margin tokens from copy_condition.tsv flagged). Then the spec's cheap test 2 (specs/ file; read its
`cheap_tests`) with its matched control, both numbers into the spec's cheap_test_done and NOTES.md; family_run.py if the test is a
family it supports.

### R8-KARL2 -- ra-karlxi-fullmakt-1677, Bakes 2018 book on dk.upce.cz (cap 2, box 30 min; lookup only)
Intake gate: `ra-karlxi-fullmakt-1677: open (line 1) -- edition/page or full-text-search citation found within 6 lines`.
Verdict cheapest next (D2B-KARL, 5 Oct 23:39): "Bakes 2018 book and articles, dk.upce.cz bitstream check and grep, ~$0.3" (the 2014
thesis is login-gated, HTTP 401). Find the 2018 book's handle on dk.upce.cz (DSpace REST/OAI or the handle page), check whether the
bitstream is open, and if it is, grep its text for 1677 / Naas / fullmakt / Karl XI / chiffr / šifr. If gated, one Google Books API query
(&country=US, key) and one OpenAlex query for the book's other open copies. Update Remaining gaps / Verdict; gaps_check PASS.
