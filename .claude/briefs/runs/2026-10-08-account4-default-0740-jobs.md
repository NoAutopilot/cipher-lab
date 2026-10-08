# LANE DEFAULT-account-4-20261008-0740 jobs (account 4) -- 8 Oct 2026 08:4x UTC, lane orchestrator session_01TUdEQx6bJBobRvPc1dUPfi

Lane brief: .claude/briefs/default-lane.md. Cap 60, box 08:35-18:35 UTC. Gate 0a: no SESSION-SWEEP-account-4 row in WORK-QUEUE.tsv, so no wait.
Backlog a: VERIFY-BACKLOG regenerated 08:40 UTC: 17 audit2 rows -- Birago off limits; nla-heinrich and colbert26 are N0 (Outreach gate 2
applies above N1 only); the 14 eckert-1864 rows are the account-3 AUD2-LS / ST-LEDGER-2 series (briefs 2026-10-08-acct3-aud2-ls.md,
-ledger2.md), left to that series. Nothing taken from a.
Backlog b: `tools/next_steps.py --hot-only` (refreshed 08:4x) runnable rows and blocked rows' parallel actions, each re-checked against the
folder's own current Verdict line (several NEXT-STEPS parallel cells were already run today by the account-1 0540 and account-2 0710 lanes).
Excluded: Birago, Armstrong, Debosnys; the Nevers no.41/no.54/no.60 pool and every folder named in the ytbiz-bnf-* briefs (LANE BNF-FOCUS,
live); eckert-1864 (account-3 audit series); ROOM claims < 6 h with no done (none of the folders below has one at 08:4x).
Guardrail share: no job below is on an N0/N1 text except as key-testing for unread siblings; reported at close.
Every worker: one job, then stop. First check the named step is still undone (a later ROOM done line or NOTES section may have run it);
if it was, write one ROOM line saying so and stop.

## Common rules for every job
- First commands: `git fetch origin && git checkout -B main origin/main`, `python3 tools/room.py --start`, `date -u`, then a ROOM claim line
  with `tools/room.py` naming your job id, folder, cap and box end time, addressed "for LANE DEFAULT-account-4-20261008-0740". If --start
  fails to push from a detached HEAD: `git push origin HEAD:main; git checkout -B main HEAD`.
- Read the folder's NOTES.md tail (Remaining gaps / Escalation / latest dated sections), HYPOTHESES.md and AUDIT.md section list first.
- Good-citizen rule and the CLAUDE.md host table for every request (one request per host at a time, >= 1.5 s apart; stop a host on
  429/403/challenge, one retry after a pause at most). Report request counts per host. Prefer files already on disk.
- Rule 3 (matched control first; a control that cannot differ from the target on the statistic is a non-test), rule 4 grading, rule 7
  (`--check` scripts). Pre-register any new gate in a PREREG-<JOB>.md pushed before the score is computed. A reading change after AUDIT.md:
  say so in NOTES.md and flag in ROOM for a verifier.
- Rebase before writing shared files (status.json, PROGRESS.tsv, ROOM.md, HYPOTHESES.md, NEXT-STEPS.tsv); keep both facts on conflict.
  Commit only your own paths. Run `python3 tools/file_shrink_guard.py <every file you touched>` before the final push; push with
  `python3 tools/room.py --push <paths>`.
- Partial targets: update "## Remaining gaps" / "## Escalation" (Verdict line) and pass `python3 tools/gaps_check.py <target>`.
- Words: never "solved", "cracked", "novel", "first", "new" for anything this project did; rule 10 wording only. Never name the owner; never
  print credentials (test presence with `test -n`). Never call AskUserQuestion. Solver jobs: report what was found and where it was not
  found; do not classify novelty.
- Stop at the cap or at 80% of the box, whichever first; do not start a unit that would cross 80% of either. A stop with work half done
  writes what was done and what remains into the folder's files. An Opus session floor is about 1.5; caps below assume it.
- Vision work: crop step mandatory and pasted (`tools/iiif_lines.py --image FILE --out DIR ...` or the `--ark/--canvas` form, or the
  folder's existing crops); read line or strip crops, never a full page image; one page (or half page) per subagent call. Price ~1.5 per
  vision call, reconciliation one more unit.
- Done: one ROOM line `done (<start>-<end> UTC by date -u, brief met|stopped at cap): <result, commit>` "for LANE
  DEFAULT-account-2-20261008-0710", then a five-line final report.

## Wave 1 (spawned 08:4x UTC 8 Oct)
Intake gate 08:4x UTC (tools/intake_gate_check.py, each "-- edition/page or full-text-search citation found within 6 lines"):
`ceppo-nevers-fr3251-1570s: partial (line 1)`; `wvo-hessen-1564: partial (line 1)`; `pro3055-clinton-1779: partial (line 1)`;
`fr5160-letellier-1653: open (line 3)`; `fr16045-pisany-rome-1585: partial (line 1)`; `antt-msliv0638-brochado-1712: partial (line 1)`.

### D4V-CEPPO -- ceppo-nevers-fr3251-1570s: verifier on the f.21v S tokens (VERIFIER, Opus; cap 3, box 60 min)
The folder's Verdict (NOTES.md l.1048) names it: a verifier on the five f.21v tokens D22-CEPPO21 (6 Oct 2026, NOTES l.1371) moved M -> S,
plus the L10.6 f -> r change of D07-CEP21 that D07-CEPV (l.1471) already endorsed (do not redo D07-CEPV; cite it). You are not the solver.
Re-run the folder's decode with --check (rule 7), re-read the five tokens on the existing 4x tiles (no fetch unless a tile is missing),
test whether the R-8 witness-shape rule could have produced the S values on a shuffled/decoy tile set (a control that can fail differently),
and write "## AUDIT (D4V-CEPPO)" in AUDIT.md: per token hold / lower to M, with the reason; depth (rule 4a) unchanged unless your result
moves it, and say so. Propagate any lowering into NOTES.md (Remaining gaps / Verdict) and status.json if a result row cites these tokens.
Do not decode beyond the five tokens; do not classify novelty anew unless a reading changed.

### D4-WVO -- wvo-hessen-1564: crib-placement test against settled/key.tsv (solver, Opus; cap 4, box 80 min)
Verdict l.894 / Remaining gaps l.884: the crib-placement test against settled/key.tsv (k28 = b), ~$2. D2-WVO (account 2, 07:39-07:44 today)
ran the blind tile read and the neighbouring-PDF scan and explicitly left this test for the next job -- read its section first. Pre-register
the crib(s), placement rule, statistic and gate in PREREG-D4-WVO.md and push it before scoring; matched control = the same placement search
on a shuffled-key or wrong-text crib of the same length (must be able to differ from the target on the statistic). Report both numbers in
HYPOTHESES.md. If time remains inside 60% of the box, do the reference-strip eye read of the 33 tiles (l.892, ~1.5) as a second unit with its
own decoy gate; otherwise leave it named. NOTES/HYPOTHESES/gaps_check.

### D4-CLIN -- pro3055-clinton-1779: the rest of the B.148 p.123 cipher (solver, Opus; cap 5, box 90 min)
Verdict l.1569: "cheapest next: the rest of the p.123 cipher, ~$3.5". Image 1205 = B.148 p.123 (l.1567); the 1778 Army List key is
confirmed (l.1564). Crop the unread lines (`tools/iiif_lines.py --image <the on-disk frame> --out ...`, paste the command), two blind passes
on line crops + one reconciliation (3 units x ~1.5), decode with the folder's script and the 1778 key, grade per token (key-read cells H),
shuffled-key control on the same token count, `--check`, judge_plaintext if the folder has a spec. Report what was found and where it was not
found; do not classify novelty. If the reading of p.123 changes after AUDIT.md, flag for a verifier in ROOM.

### D4-F5160 -- fr5160-letellier-1653: assess the five unassessed escalation rows (worker, Opus; cap 2, box 45 min)
Verdict: "0 internal gaps; cheapest next: (clear-pages done, D1A-F68 8 Oct 2026, PASS; Français 20661-20662 is person-side) assess the five
unassessed escalation rows (known-keys, print, key-rebuild, image-check, retry), ~$1". For each row: mark [x] with the evidence already in
the folder, [n/a] with the reason, [ ] with "next: <step>, ~$<cost>", or blocked with the outside blocker -- from disk and KEY-OFFICES.tsv /
KEY-DESIGN.tsv / tools/design_prior.py; no fetch unless one catalogue lookup decides a row. Then gaps_check and a correct Verdict
("parked" only if every gap has an outside blocker and no step is untried). No cryptanalysis in this job.

### D4-PISA -- fr16045-pisany-rome-1585: f.275v head L04 wording, one-line read (solver, Opus; cap 3, box 60 min)
Verdict l.1066: "cheapest next: f.275v head L04 wording one-line blind read, ~$2 (D1A-PISG2, 8 Oct 2026: second blind reader G1 PASS 0.691,
G2 FAIL, blind single-call reader retired for G2; reconciliation 0.945 descriptive)". Read the D1A-PISG2 section first: the single-call blind
reader is [retired] for G2, so do NOT re-run that instrument on G2; this job is the L04 head wording only, by a different instrument
(e.g. the clear copy in Colbert 16 pt II beside f.275v, or a per-word tile read with a decoy set), pre-registered in PREREG-D4-PISA.md
before scoring. One vision unit + reconciliation. Grade per token; --check; NOTES/gaps.

### D4-BROC -- antt-msliv0638-brochado-1712: letter 134 doubled-loop / 't' image pass (solver, Opus; cap 7, box 110 min)
Verdict l.2272 / l.2270: "the doubled-loop / 't' image pass on letter 134 (crops with tools/iiif_lines.py --image, 2 blind passes + 1
reconciliation, ~$6)": letter 134's ff?/dd? tokens (m0275 pos 8 and 31, m0276-r1 ...; read l.2270 in full). Images are on disk (DigitArq
full JPEGs in images/); crop step mandatory and pasted. Pre-register in PREREG-D4-BROC.md what reading of each sign settles a token,
including a decoy/known-answer set from the appendix (atlas PX-BROGLYPH) so the pass can fail. 3 units x ~1.5. Apply settled tokens via the
folder's decode (key.tsv unchanged unless the per-unit merge clause of rule 3 is met), --check, grade, NOTES/gaps. Do not run the LM-context
rescoring (a separate job).

