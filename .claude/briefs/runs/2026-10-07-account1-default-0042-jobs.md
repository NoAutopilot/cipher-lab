# LANE DEFAULT-account-1-20261007-0042 jobs (account 1) -- 7 Oct 2026 00:4x UTC, lane orchestrator session_01K3xPt4vRjTP7t7Psb4Vezr

Lane brief: .claude/briefs/default-lane.md (cap 60, box 00:42-10:42 UTC 7 Oct). Gate 0a: SESSION-SWEEP-account-1 row still `claimed`, but its
TSV (SESSION-SWEEP-account-1-2026-10-05.tsv) has been on disk since 5 Oct; proceeding as RUN8-12 did, 0 exclusions. Backlog a: VERIFY-BACKLOG
regenerated 00:4x UTC -- only Birago (off limits) and nla-heinrich audit2 (N0, outreach gate 2 not needed) remain; the live verifier debt is the
NEVF-APPLY ROOM flag (fr3416, 23:44 UTC 6 Oct). Backlog b: `tools/next_steps.py --hot-only` runnable rows not touched in the last 6 h.
Excluded: NEWT-A-account-1 and NEWT-C-account-4 targets (live lanes), Birago, Armstrong, Debosnys, anything owner-sorter-gated.
Every worker: one job, then stop. Each job first checks its named step is still undone (NEXT-STEPS.tsv lags the folders); if a dated NOTES.md
section or ROOM done line already ran it, stop and report.

## Common rules for every job
- First commands: `git fetch origin && git checkout -B main origin/main`, `python3 tools/room.py --start`, `date -u`, then a ROOM claim
  line with `tools/room.py` naming your job id, folder, cap and box end time, addressed "for LANE DEFAULT-account-1-20261007-0042".
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
- Done: one ROOM line `done (<start>-<end> UTC by date -u, brief met|stopped at cap): <result, commit>` "for LANE DEFAULT-account-1-20261007-0042",
  then a five-line final report.


## Wave 1 (spawned 00:4x UTC 7 Oct). Intake gate output (00:4x UTC) pasted per job.

### D07-NEVFV -- fr3416-nevers-fils-1589, AUDIT propagation after NEVF-APPLY (verifier, Opus; cap 4, box 50 min)
Intake gate: `fr3416-nevers-fils-1589: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`.
NEVF-APPLY (account 1, commit c1101fad, 23:44 UTC 6 Oct) applied the owner's L05 sorter labels: graded counts moved H 75/M 27 -> H 81/M 21 of
102; AUDIT.md (depth_pct 73.5%) is now stale. You are a separate session from every solver and from NEVF-APPLY. Job (rule 10 propagation +
rule 4a): (1) re-run the folder's decode (`decode_f35.py` then `--check`) and recount grades; (2) judge token 79's pairing (45 79 null vs
4 57 9 = m) from the crops and the key sheet already on disk -- decide or leave M with the reason; (3) append "## AUDIT 3 (propagation)" to
AUDIT.md: new counts, depth re-check with tools/depth_check.py (D-level, depth_pct, depth_sentence), N-class unchanged unless the reading's
text changed (say whether any letter changed; NEVF-APPLY says only case changed); (4) carry the revision into status.json's result row and
into SECOND-OPINIONS-QUEUE.tsv row SO-NV02-F35 / its PROMPT file if the quoted reading or counts appear there; PROGRESS.tsv if it carries the
counts. No new novelty search beyond a 3-query phrase delta if the reading text changed. Do not decode other leaves.

### D07-PIST40 -- fr16045-pisany-rome-1585, key86 T40 image compare (Opus; cap 4, box 50 min)
Intake gate: `fr16045-pisany-rome-1585: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`.
Folder Verdict cheapest next: image compare of the f.302v T40 tokens with the key86 table's `a` and `s` cells (NOTES.md line ~929; the
tokens align to s 5 of 7). Disk only (crops and key image already on disk; if a crop is missing, re-cut it with tools/iiif_lines.py and paste
the command). PREREG first (what counts as T40 = s vs = a, and a control: the same comparison on 5 tokens of a settled sign of similar shape,
which must come out right before the T40 call counts). Units: 1 crop sheet + 1 blind Sonnet compare call + 1 reconciliation = ~4.5. If
settled, update key86.tsv/exceptions, re-run the folder decode --check, and record grade movement; flag ROOM for a verifier if counted
readings change. Update Remaining gaps/Escalation; gaps_check.py.

### D07-NOXT -- fr16142-noailles-constantinople-1571, widen the atlas-pile to key.tsv bridge with c262 tiles (Opus; cap 4, box 50 min)
Intake gate: `fr16142-noailles-constantinople-1571: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`.
Folder Verdict cheapest next (NOTES.md ~line 1440/1512): place the c262 tiles (glossed, key.tsv values known from Tomokiyo's key) under the
owner's settled atlas labels so more than 17 piles carry a key.tsv value -- this builds the key bridge for the unread c510-516 cipher (the
guardrail purpose). Scripts first (tile ids, owner pile labels, c262 token-to-key mapping are on disk); vision only for tiles a script cannot
place (cap 2 subagent calls, crop paths only). Report piles bridged before/after, conflicts (a pile carrying two key values) listed, not
resolved by majority. No decode of c510-516 in this job; name it as the next step with its cost.

### D07-VIV53 -- fr16104-vivonne-spain-1572, ink 53 per-position e/o crops vs key cells f, m, p (Opus; cap 6, box 70 min)
Intake gate: `fr16104-vivonne-spain-1572: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`.
Folder Verdict cheapest next (AUDIT 4; whole-label test negative, D1-F16104K): per-position crops of the ink 53 tokens labelled e/o against the
Tomokiyo key image's cells f, m, p. PREREG committed and pushed before the scored compare (statistic, a known-answer control on positions whose
cell is already settled, gate). Crop step mandatory and pasted (tools/iiif_lines.py --image ... --out <scratchpad or folder crops dir>);
subagents get crop paths only. Units: crop cut + 2 blind Sonnet compare passes + 1 reconciliation = ~6. If the control misses its gate, stop
before the target compare and log "non-test". If labels change: decode --check, grade counts, ROOM flag for a verifier (counted reading).

### D07-D1411 -- decode-1411-hhsta-vienna-1600, p.4 4/5 re-read on per-number tiles + T21r rescore (Opus; cap 6, box 70 min)
Intake gate: `decode-1411-hhsta-vienna-1600: open (line 3) -- edition/page or full-text-search citation found within 6 lines`.
Folder Verdict cheapest next: re-run the p.4 4/5 re-read (R12A-D1411LA's la/ tiles, prompt and pinned rule) on per-number enlarged tiles
(R12A-D1411LA's line-crop re-read was void, 83/83 '?'), then rescore T21r against the same frozen controls (no control or gate moved after
seeing numbers; the earlier PREREG stands, cite it). Cut per-number tiles from the DECODE full-size p.4 image on disk (if absent, the
re-fetch command in Remaining gaps; one browser login at most). A 5-tile pilot first: if the pilot still returns '?' on 3+ of 5, stop and log
the instrument as void at this resolution. Units: tiles + 2 read passes + rescore = ~6.

### D07-COL26K -- colbert26-lathuillerie-1644, canvas 20-21 positional known-answer statistic per candidate code (Opus; cap 3, box 40 min)
Intake gate: `colbert26-lathuillerie-1644: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`.
Folder Verdict cheapest next (after D22-COL26P's span-level positional test, 0 PASS of 26): the canvas 20-21 positional known-answer statistic
per candidate code (42 si, 11 le/les, 6 je) with f.24 as held-out, scripts only. PREREG committed and pushed before the scored run, naming a
control that can vary on the statistic (rule 3: e.g. rotated/shuffled position assignment, not a value shuffle of a position-only statistic),
the Bonferroni correction and the power at each code's own N (subsample the positive control to that N, rule 3 last paragraph). Report target
and control side by side per code; UNDERPOWERED is a result, not a negative. No vision. If a code passes, write it as S in key_* with the
evidence and flag ROOM for a verifier only if a counted reading changes. Then the word-level pairing (~$6) is named, not run.

## Wave 2 (spawned 01:0x UTC 7 Oct; follow-ups named by wave 1 plus next_steps rows). Intake gate output (01:0x UTC) pasted per job.
antt-linhares-chave skipped: intake gate `blocked (line 3) -- already terminal`.

### D07-NOX510 -- fr16142-noailles-constantinople-1571, place the 14 split-pile c262 tiles, then decode c510-516 through the bridge (Opus; cap 5, box 60 min)
Intake gate: `fr16142-noailles-constantinople-1571: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`.
Folder Verdict (D07-NOXT, 7 Oct): place the 14 split-pile c262 tiles (~1), then the c510-516 decode through the 19-pile bridge, pre-registered
(~2). The 4 label conflicts D07-NOXT listed stay listed, not resolved by majority. PREREG committed and pushed before the decode: statistic,
a control that can vary on it (e.g. the same decode with the bridge's key values permuted among piles, and a shuffled-order text), gate.
Grade every decoded token (rule 4: S only where the control is beaten; M otherwise). judge_plaintext.py only if a spec exists. Any reading
produced is a candidate for a verifier; flag ROOM. Vision at most 2 subagent calls on crop paths.

### D07-NEVF25 -- fr3416-nevers-fils-1589, sibling key-no.25 letter for the L05 pairing (Opus; cap 5, box 60 min)
Intake gate: `fr3416-nevers-fils-1589: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`.
Folder Verdict (AUDIT 3, 7 Oct): check a sibling key-no.25 letter (fr.4715 f.27 or f.38) for orphan single digits, to settle the L05
"45 79 (null)" vs "4 57 9 (m)" pairing. Locate the leaf via tools/gallica_folio.py (paste the call), crop with tools/iiif_lines.py (paste),
read the figure runs (one subagent call per page, crop paths only, 2 blind passes + 1 reconciliation, ~1.5 each). Decide in advance (PREREG)
what pattern in the sibling settles the pairing either way and what leaves it open. Do not decode the sibling beyond what the question needs;
if it carries an unread cipher, say so in NOTES.md as a next step with a cost. If L05 grades change: decode --check and ROOM flag for a verifier.

### D07-PISSD -- fr16045-pisany-rome-1585, key86 T40 page-internal same/different compare (Opus; cap 4, box 50 min)
Intake gate: `fr16045-pisany-rome-1585: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`.
Folder Verdict (D07-PIST40, 7 Oct: table-cell compare a NON-TEST, control 1/5): compare the f.302v T40 tokens with the same page's own
C-graded T17 tokens as same/different pairs, disk only. PREREG first with a matched control that must pass (known-same and known-different
pairs from C-graded tokens on the page, mixed blind into the set). If the control misses, stop and log non-test; this is then the third
instrument on T40 (rule 3 third-attempt clause: mark the step [retired] with the instrument named, unless a genuinely different instrument
remains). Units: pair sheet + 1 blind Sonnet call + 1 reconciliation, ~3.5.

### D07-ECK62 -- eckert-1862, per-token override table in ec18.py at full regeneration (Opus; cap 4, box 50 min)
Intake gate: `eckert-1862: partial (line 3) -- edition/page or full-text-search citation found within 6 lines`.
Folder Verdict cheapest next: the per-token override table in ec18.py at its next full regeneration (Lehigh + Leghorn/Legend/Leopard grades,
R12A-ECKV2), ~$3. Scripts only. Rule 7: the regeneration's --check exits 0 and the committed readings match; list every token whose grade
moved (before/after counts). If counted readings change, flag ROOM for a verifier. The No. 4 book (13 words) stays waiting on the desk read.

### D07-CEP21 -- ceppo-nevers-fr3251-1570s, f.21v S10/S26 and S13/S69 witness-shape rule, then a 4x read (Opus; cap 5, box 60 min)
Intake gate: `ceppo-nevers-fr3251-1570s: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`.
Folder Verdict cheapest next: derive the S10/S26 and S13/S69 witness-shape rule from the fr.3252 glosses (as D22-CEPPO21 did for S65/S80 via
fr.3252 f.36v), PREREG it before reading, then read the f.21v tokens on 4x tiles (~$3). Do not re-run the [retired] instrument (blind model
reads of the a1b36v tiles). Crop step pasted; crop paths only. Grade changes: decode --check, counts before/after, ROOM flag for a verifier if
a counted reading changes.
