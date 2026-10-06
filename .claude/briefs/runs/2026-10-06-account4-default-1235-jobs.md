# LANE DEFAULT-account-4-20261006-1235 jobs (account 4) -- 6 Oct 2026 12:4x UTC, lane orchestrator session_01EcBWEQJJDT6cyLwTMsgGkq

Lane brief: .claude/briefs/default-lane.md (cap 60, box 12:35-22:35 UTC 6 Oct). Gate 0a: no SESSION-SWEEP-account-4 row. Backlog a:
VERIFY-BACKLOG.tsv's three actionable rows (Noailles c262/c510, decode-2678 Gravel, NLA 1519) are all named in live/last-24h briefs of
accounts 1-2 (RUN9/RUN10) -- excluded. Backlog b: `tools/next_steps.py --hot-only` runnable rows and `parallel` actions, excluding
folders in ROOM lines since 06:38 UTC and in the live briefs (account-2 RUN12, account-1 RUN10, acct3 lane-priv1). Off limits: Birago,
Armstrong, Debosnys; bne20211-ferdinand-1478 and destaing-gerard-1779 (account-4 standing session); anything in a private repository.
Every worker: one job, then stop. Each job first checks its named step is still undone (NEXT-STEPS.tsv lags the folders): if a dated NOTES.md
section or a ROOM done line already ran it, take the folder's own Verdict "cheapest next" instead if it fits this job's cap and box and is
not a machine transcription pass the TRANSCRIPTION.md / CLAUDE.md Usage 6 sorter rule hands to the owner; otherwise stop and report.

## Common rules for every job
- First commands: `git fetch origin && git checkout -B main origin/main`, `python3 tools/room.py --start`, `date -u`, then a ROOM claim
  line with `tools/room.py` naming your job id, folder, cap and box end time, addressed "for LANE DEFAULT-account-4-20261006-1235".
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
  owner; never print credentials (test presence with `test -n`). Never call AskUserQuestion. Solver/lookup jobs: report what was found
  and where it was not found; do not classify novelty.
- Stop at the cap or at 80% of the box, whichever first; do not start a unit that would cross 80% of either. A stop with work half
  done writes what was done and what remains into the folder's files. An Opus session floor is about 1.5; caps below assume it.
- Vision work: crop step mandatory and pasted (`tools/iiif_lines.py --image FILE --out DIR` or the --ark/--canvas form); give
  subagents only crop paths, one page/leaf per call, never a full-page image. Price: ~1.5 per Sonnet subagent pass, reconciliation = 1 unit.
- Sorters: any sorter meant for the owner must PASS `python3 tools/sorter_preflight.py` and have 5+ random tiles opened against the line
  image before it is handed on; it is handed to the account-3 orchestrator (ROOM flag line) to publish. Never publish an artifact or edit
  ASKS.md yourself.
- No private-repository access in these sessions: if a step needs one, stop and say so in ROOM (the lane hands it to the standing session).
- Done: one ROOM line `done (<start>-<end> UTC by date -u, brief met|stopped at cap): <result, commit>` "for LANE DEFAULT-account-4-20261006-1235",
  then a five-line final report.


## Wave 1 (spawned 12:4x UTC 6 Oct). Intake gate output (12:4x UTC) pasted per job.

### D4-PISRS -- fr16045-pisany-rome-1585, re-score kp86/kp86e arm A with R9-PIS2's 9 settled T31 tokens relabelled (Opus; cap 2.5, box 45 min; disk only)
Intake gate: `fr16045-pisany-rome-1585: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`.
R9-PIS2 "next" (ROOM 06:33, NOTES ## R9-PIS2): relabel only the 9 tokens pis2/t31_tokens.tsv settles by shape (8 T36, 1 T45), re-run the
kp86/kp86e arm A scoring exactly as its last run (same script, same control/shuffle, PREREG addendum pushed before the scored run stating the
relabel and that the gate is unchanged), report target vs control before and after. Key86/tx changes only if the gate says so; decode --check.
Write "## D4-PISRS" in NOTES.md and the HYPOTHESES.md row; update Remaining gaps / Escalation; gaps_check.py pass.

### D4-1411P3 -- decode-1411-hhsta-vienna-1600, p.3 numerals: cut, two blind passes, pre-registered word-coverage test of T21r (+ h alt) (Opus; cap 9, box 110 min)
Intake gate: `decode-1411-hhsta-vienna-1600: open (line 3) -- edition/page or full-text-search citation found within 6 lines`.
Folder Verdict cheapest next (DEF1-1411 Remaining gaps 1 and 3). Units: p.3 crop step pasted (tools/iiif_lines.py --image on the GAPS137
full-size p.3 image on disk) + 2 blind Sonnet passes over p.3 line crops (one call per pass, crops only) + 1 reconciliation = 3 units x ~1.5,
then the test (~2). PREREG committed and pushed BEFORE the scored run: statistic (word coverage against the de1600 lexicon or the folder's
own word list, as DEF1-1411 defined it), the frozen tables T21r and the h alternative unchanged, controls = shuffled target and the 23
residue shifts (the controls DEF1-1411 used, which can vary on coverage), pass rule stated numerically. Report target vs control numbers.
Do not retune the tables after seeing p.3. Write "## D4-1411P3" in NOTES.md; HYPOTHESES.md row; Remaining gaps / Escalation; gaps_check.py.

### D4-VIVMOUS -- fr16106-vivonne-longlee-1579, known-keys rung: Mousset 1912 pp.lviii-lix table to disk and applied to f.101v (Opus; cap 3, box 60 min)
Intake gate: `fr16106-vivonne-longlee-1579: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`.
"## While waiting (RUN4-WAITBF)" action and Escalation [ ] known-keys. Read Mousset 1912 pp.lviii-lix (the printed Longlee/Vivonne
reconstruction) from the IA djvu text and, where the table layout needs it, the IA page image (one page at a time, >= 1.5 s apart; the
`_djvu.txt` route first; a lending-only item -> be-api fts only, say so and stop). Transcribe the table to key/mousset1912.tsv (credited,
key source `published`). Apply it to the f.101v transcription on disk with tools/decode_key.py (or a decode.json), grade per rule 4 (a
published key read = H only where the sign identity is settled; tokens whose sign the c107 sorter still splits stay M), and report how many
tokens read and whether the result agrees with the copy (c110-c112) where test 1 aligned them. A published-key check, not a fit: no
key edits beyond the printed table. Write "## D4-VIVMOUS" in NOTES.md; tick or annotate Escalation known-keys; gaps_check.py pass.

### D4-PAG13 -- clairambault296-paget-1713, apply the sister folder's 1714 Paget key to the 1714 letters' unglossed spans; list open codes (Opus; cap 2.5, box 45 min; disk only)
Intake gate: `clairambault296-paget-1713: open (line 1) -- edition/page or full-text-search citation found within 6 lines`.
"## While waiting (FT4-clairambault296-paget-1713)" action: using clairambault1225-paget-1714's key.tsv and transcriptions (read-only
there; do not edit the sister folder's files), apply the key to the 1714 letters' own unglossed spans, and write to this folder a
residue table (code, count, letters/positions, key value or OPEN, grade) so the 1713 letter can be tested the day Clairambault 297 p.249
arrives. No novelty or status change (stays open, parked on the BnF order). Write "## D4-PAG13" in NOTES.md.

### D4-ESPLL -- esp318-sicilia-1503, re-count rows l and ll of key/key_gran_cifra.tsv against the key-sheet crops (Opus; cap 1.5, box 30 min; disk only)
Intake gate: `esp318-sicilia-1503: open (line 1) -- edition/page or full-text-search citation found within 6 lines`.
Folder Verdict "meanwhile" step (A4-RFESP note: rows l and ll show 3 signs each on the sheet, the TSV carries 5). Eye-check every row of
key/key_gran_cifra.tsv against the key/ crops on disk (crop paths only to any subagent; prefer doing it yourself on zooms), correct the slot
counts with a note per change (old -> new, crop file), and do not label sorter piles (that waits on ASKS 104). If decode_key.py or a decode
script reads that TSV, run its --check. Write "## D4-ESPLL" in NOTES.md; Remaining gaps / Escalation; gaps_check.py pass.

### D4-F61PR -- fr4715-f61-mayenne-1592, print search on f.61r's full clear text (Sonnet; cap 1.5, box 40 min)
Intake gate: `fr4715-f61-mayenne-1592: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`.
Folder `parallel` action: refresh phrases.txt with the reconciled, normalised phrases of scripts/f61r_clear_reading.tsv (as the NOTES.md
While-waiting line describes), run `python3 tools/print_check.py ciphers/fr4715-f61-mayenne-1592` (IA full text, Google Books with
country=US + key, OpenAlex with the key header), and write the hits/no-hits table into a dated "## D4-F61PR" NOTES.md section. Search result
only: a no-hit is a search result for the log, never a novelty verdict. Update that Remaining gap's line; gaps_check.py pass.
