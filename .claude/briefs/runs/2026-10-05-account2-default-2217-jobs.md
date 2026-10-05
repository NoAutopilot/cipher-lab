# LANE DEFAULT-account-2-20261005-2217 jobs (account 2) -- 5 Oct 2026 23:1x UTC, lane orchestrator session_01J69aWeq2QaUGpDPaxaYDW4

Lane brief: .claude/briefs/default-lane.md (cap 60, box 23:11 UTC 5 Oct - 09:11 UTC 6 Oct). Backlog per WORK-QUEUE row 229: VERIFY-BACKLOG.tsv
(regenerated 23:08 UTC) then plain `tools/next_steps.py` runnable rows (not --hot-only), folders m-z plus leftovers (account 1 takes a-l).
Off limits: Birago, Armstrong, Debosnys. Every worker: Opus 5.5, one job, then stop. Each solver job first checks that its named step is still
undone (NEXT-STEPS.tsv lags the folders): if a dated NOTES.md section already ran it, take the folder's own Verdict "cheapest next" instead, if it
fits this job's cap and box and is not deep work on another folder; otherwise stop and report.

## Common rules for every job
- First commands: `git fetch origin && git checkout -B main origin/main`, `python3 tools/room.py --start`, `date -u`, then a ROOM claim
  line with `tools/room.py` naming your job id, folder, cap and box end time, addressed "for LANE DEFAULT-account-2-20261005-2217".
  If --start fails to push from a detached HEAD: `git push origin HEAD:main; git checkout -B main HEAD`.
- Read the folder's NOTES.md tail (Remaining gaps / Escalation / latest dated sections) and AUDIT.md section list before acting.
- Good-citizen rule and the CLAUDE.md host table for every request (one request per host at a time, >= 1.5 s apart; stop a host on
  429/403/challenge, one retry after a pause at most). Report request counts per host.
- Rebase before writing shared files (status.json, PROGRESS.tsv, VERIFY-BACKLOG.tsv, SECOND-OPINIONS-QUEUE.tsv, JSTOR-QUEUE.tsv,
  ROOM.md); keep both facts on conflict. Run `python3 tools/file_shrink_guard.py <every file you touched>` before the final push;
  push with `python3 tools/room.py --push <paths>`.
- Words: never "solved", "cracked", "novel", "first", "new" for anything this project did; rule 10 wording only. Never name the
  owner; never print credentials (test presence with `test -n`). Never call AskUserQuestion.
- Stop at the cap or at 80% of the box, whichever first; do not start a unit that would cross 80% of either. A stop with work half
  done writes what was done and what remains into the folder's files.
- Vision work: crop step mandatory and pasted (`tools/iiif_lines.py --image FILE --out DIR` or the --ark/--canvas form); give
  subagents only crop paths, one page/leaf per call, never a full-page image.
- Done: one ROOM line `done (<start>-<end> UTC by date -u, brief met|stopped at cap): <result, commit>` "for LANE
  DEFAULT-account-2-20261005-2217", then a five-line final report.

## Verifier job (rules as .claude/briefs/runs/2026-10-05-account1-default-2217-jobs.md "Verifier jobs", verbatim; read that section)

### D2B-SCHON -- na-schonenberg-1678-1716, Audit 2 + count (cap 5, box 60 min; 1 leaf, 3 items x ~1.3 + 1)
VERIFY-BACKLOG.tsv row "Schonenberg" (high, missing both). Audit 1 = AUDIT.md sections 1-5 (2 Oct 2026): body N0, L18 N0, L19 N2, leaf
N0, key period (body) / ours (L19 alignment); register note VER1-REG (5 Oct) set D3 96.1% C. Fresh session; you wrote neither. Try to break
N0 for the body (is the gloss really period? is there a print of the plaintext?) and above all L19's N2: search for any print or
transcription of the L19 address-line groups or the letter (Herrero Sanchez 2016 Hispania via OpenAlex/CORE/CrossRef full text; the 2016
Utrecht thesis; NA catalogue for 1.02.04 inv.63; Spanish court-correspondence editions; Google Books; IA be-api; solver repos). Set the
count via tools/depth_check.py; status.json target row audit_status 'two audits' and the depth fields; PROGRESS.tsv row for
na-schonenberg col `2` = x (and `C` as the tool decides; at N0 it stays '.'); regenerate VERIFY-BACKLOG.tsv. Append "## AUDIT 2 (D2B-SCHON,
<date>)". JSTOR rows both families. Do not touch the reading or decode.json.

## Solver jobs (solver template .claude/briefs/solver.md; intake gate output pasted below (23:14 UTC); report what was found and where
## it was not found; do not classify novelty; rule 4 grades; rule 7 --check before push; partial targets keep Remaining gaps /
## Escalation and pass `python3 tools/gaps_check.py <target>`)

### D2B-THURP3 -- thurloe-printed, P3-postscript cross-check against the P5-P7 key (cap 1.5, box 40 min)
Intake gate: `thurloe-printed: partial (line 2) -- edition/page or full-text-search citation found within 6 lines`.
Verdict: "a P3-postscript cross-check against the P5-P7 key (key_stamford.tsv) for codes the postscript shares with them, ~$1". Script first:
list the P3 postscript codes, intersect with key_stamford.tsv and the P5-P7 alignments, report each shared code's value and support count;
regrade a P3 token only under a pre-registered rule written before the lookup (e.g. value attested >= 2 times in siblings, no conflict ->
C; one attestation -> M). Rule-4 conflicts logged with witnesses, never by majority. Do not touch P4 or the AUDIT.md classes; if the P3
reading changes, say so in NOTES.md and flag in ROOM for a verifier (rule 10 propagation is the verifier's).

### D2B-MANT27 -- sachsstaatsarchiv-manteuffel-1712, transcribe frame 0527 and gate per leaf (cap 5, box 70 min; 2 blind passes + 1 reconciliation at ~1.5 each)
Intake gate: `sachsstaatsarchiv-manteuffel-1712: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`.
Verdict: "transcribe file 0527 (ff.422v-423, dense glossed, never read; 2 passes + reconciliation, ~$3-4) and gate it per leaf". First check
the folio label: GAPS195 already did frame 0528 as ff.422v-423 -- confirm from images/loc694-08-09/frames.tsv and the frame itself which
folios 0527 is, and that it is not already transcribed. Then the GAPS195 shape exactly: crop step, two blind passes, reconcile_passes.py,
decode_key.py, the per-leaf shuffle gate (single-code glosses vs shuffle p95) before any code enters key.tsv (CLAUDE.md rule 3 per-unit
merge paragraph). Stop after 0527; the 0501 decision stays with the orchestrator.

### D2B-KARL -- ra-karlxi-fullmakt-1677, Bakes thesis full-text grep (cap 1, box 30 min)
Intake gate: `ra-karlxi-fullmakt-1677: open (line 1) -- edition/page or full-text-search citation found within 6 lines`.
Verdict cheapest next: grep the theses.cz download of the Bakes thesis for "1677"/"Naas"/"Nääs"/"fullmakt"/"plenipotentia"; record hits with
page and context in NOTES.md; update Remaining gaps / Escalation. If theses.cz is blocked from the cloud, log it and stop.

### D2B-RUBIN -- rubin-1953, locate and read the FBI FOIA file (cap 1.5, box 40 min)
Intake gate: `rubin-1953: open (line 1) -- edition/page or full-text-search citation found within 6 lines`.
Next step (NO-CRACKS): locate the FBI file on Rubin (~160 pp., obtained by Bauer; FBI Vault search "Rubin", archive.org mirrors, Cipher
Foundation, Pelling 3 Jan 2018, Bauer Unsolved! notes) for the FBI's transcription of the slip; if found, compare against ciphertext.txt's
2013-photo vs 2018-reproduction disagreements and record which it supports per position (transcription evidence, not a reading). Never edit
ciphertext.txt silently: record in NOTES.md and a variants file. If not reachable, log routes tried.

### D2B-RAY -- rayburn-2004, earliest Wayback capture vs images/Rayburn-Cryptogram.jpg (cap 1, box 30 min)
Intake gate: `rayburn-2004: open (line 1) -- edition/page or full-text-search citation found within 6 lines`.
Next step (NO-CRACKS): Wayback CDX for schneier.com/blog/archives/2006/01/handwritten_rea.html (Jan-Feb 2006 captures) and the image URL
it embeds; fetch the earliest image; compare with images/Rayburn-Cryptogram.jpg (dimensions, white-out areas, by script diff then one look);
mark tokens bordering a white-out in a column of ciphertext.tsv (or a sidecar TSV if the format forbids). Record in NOTES.md.

# Wave 2 (spawned as wave-1 slots free; same rules)

### D2B-LIPP -- ss-radio-lippert-1944, Gnegel's 2021 eBay specimen (cap 1, box 30 min)
Next step: Wayback CDX for ebay.de item 284276746819 and the Cipherbrain 2021 post's images; other "chiffrierter Funkspruch 1944" listings;
compare cipher groups with ours by script (identical / shuffled / different). Record as authenticity evidence; status stays open (rule 5).

### D2B-YOG -- yogtze-1984, lexical crib search of the six letters (cap 0.8, box 25 min)
Next step: script search of YOGTZE (and its reported variants) against 1984 German/Dutch licence-plate prefixes and food-technology
abbreviations; logged as a search (UNSOLVED-SURVEY row 26), no reading claimed.

### D2B-ROELL -- roell-vandedem-1809, NA 2.01.08 EAD grep for the 1808-09 code (cap 1.2, box 30 min)
Next step: fetch the NA 2.01.08 EAD once, grep cijfer/chiffre/Croiset/sleutel; record inventory numbers and availability flags.

### D2B-WOTT -- sp99-wotton-1622, folio 159 question (cap 1.5, box 35 min)
NOTES.md recommended step (1): resolve whether "159" in the description is a correspondent code or a folio cross-reference (TNA Discovery
API for SP 99/24 or the item's own record; read f.159 if imaged). Record; no decoding.
