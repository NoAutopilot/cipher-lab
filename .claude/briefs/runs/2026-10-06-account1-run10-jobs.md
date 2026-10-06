# LANE LANE-RUN10-account-1 jobs (account 1) -- 6 Oct 2026 09:5x UTC, lane orchestrator session_01CaidpjF7GC2DXjAnB1T7Dw

Lane brief: .claude/briefs/default-lane.md (cap 60, box 09:41-19:41 UTC 6 Oct). WORK-QUEUE row LANE-RUN10-account-1: the previous a-h round's
named next steps first (STATUS.md "LANE LANE-RUN9-account-1 handoff", "Open for the next a-h lane"), then tools/next_steps.py --hot-only runnable
rows (S, M), BnF tie-breaker. VERIFY-BACKLOG.tsv (regenerated 09:44): only fr16142 "counted" register-lag rows and Birago (off limits).
Off limits: Birago (incl. ceppo-nevers, nevers-birago, birago-*), Armstrong, Debosnys, account-4 private-repo targets (bne20211-ferdinand,
destaing-gerard, bowes-walsingham, hamilton-1650). No worker edits any outreach/ file.
Every worker: Opus 5.5, one job, then stop. Each solver job first checks that its named step is still undone (NEXT-STEPS.tsv lags the
folders): if a dated NOTES.md section already ran it, take the folder's own Verdict "cheapest next" instead if it fits this job's cap and
box and is not a campaign; otherwise stop and report. Caps per CLAUDE.md Usage 6: (subagent passes + 1 reconciliation) x ~1.5 per pass,
plus ~1.5-3 Opus session floor.
Intake gate (tools/intake_gate_check.py, 6 Oct 09:4x UTC): decode-2678-bnf-colbert127-gravel-1665, fr3151-seure-1558,
huntington-blathwayt-madrid-1728, fr3416-nevers-fils-1589, fr16142-noailles-constantinople-1571, eckert-1862, baluze103-letellier-marca-1644,
florence-dieci-responsive all exit 0 ("edition/page or full-text-search citation found within 6 lines"); eckert-1864 exit 0 in RUN9.

## Common rules for every job
- First commands: `git fetch origin && git checkout -B main origin/main`, `python3 tools/room.py --start`, `date -u`, then a ROOM claim
  line with `tools/room.py` naming your job id, folder, cap and box end time, addressed "for LANE LANE-RUN10-account-1".
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
  LANE-RUN10-account-1", then a five-line final report.


## Wave 1 (written 09:5x UTC from the RUN9-account-1 handoff)

### R10-DEC2678V -- VERIFIER, decode-2678-bnf-colbert127-gravel-1665: P2/P3 reading under the Tomokiyo Colbert-Gravel 1672 key (cap 3.5, box 45 min)
Template: CLAUDE.md "Verifier brief (template)" and .claude/briefs/verifier.md. Claim under audit: R9-DEC2678C's "Tomokiyo's published
Colbert-Gravel 1672 key PASSes PREREG ca9a62902 on R2678 P2/P3; H 11 M 2 U 2 of 15; decode_key --check 0". You are not the solver and do not
protect its conclusions. (1) Confirm the PREREG commit predates the scored run (git log order), re-run the scoring and decode_key --check,
check the shuffled-key/shuffled-order controls CAN differ for the statistic (CLAUDE.md rule 3 orthogonality paragraph) and that the matched
power at N=14 is honestly computed. (2) Check the key's provenance (sources/cryptiana snapshot, credit Tomokiyo, key: published) and that
the letter is Gravel, Ratisbon 29 Jan 1665 (f.349). (3) Novelty search per the template families incl. tools/print_check.py on the reading's
phrases; Gravel's Ratisbon despatches in print (Recueil des instructions, Allemagne; Auerbach) -- a short reading may be summarised in print.
(4) AUDIT.md: N-class, key source, depth per rule 4a (tools/depth_check.py), safe/unsafe sentence; SECOND-OPINIONS-QUEUE row if N3+. Do not
decode beyond re-running the committed script.

### R10-SEURE3 -- fr3151-seure-1558: rebuild the Babou 1558 key (fr. 3138 no. 13 f.32) and test it on R1/R2 (cap 4, box 50 min)
Verdict cheapest next (R9-SEURE2): "rebuild the Babou 1558 key (fr. 3138 no. 13 f. 32, cipher + decipherment) and test it on R1/R2 with the
unigram statistic and own-text power control first, ~$3". Locate the leaf with tools/gallica_folio.py; crops via tools/iiif_lines.py
pasted; the cipher/decipherment pairs go through tools/interlinear_align.py (grade C/period). PREREG (statistic, own-text power control at
the target's N and coverage, gate) pushed before scoring R1/R2; power control below gate = NON-TEST, stop. A FAIL with power is a result.
If the leaf is not digitised or carries no decipherment, log that and stop.

### R10-HUNT2 -- huntington-blathwayt-madrid-1728: re-registered context-fill, attempt 2 of at most 3 (cap 3, box 40 min)
As R9-HUNT2 in .claude/briefs/runs/2026-10-06-account1-run9-jobs.md (not run there): bracket fix + margin-filtered gate against the
shuffled-context control at matched margin; PREREG fixes margin threshold and gate BEFORE running, on FRESH seeds only (4-6+), pushed first.
If the control fails again, log "attempt 2 FAIL" and name a different instrument as next (rule 3 third-attempt clause); do not tune again.

### R10-NEVF2 -- fr3416-nevers-fils-1589: L05 sign-sorter build for a person's read (cap 3, box 35 min)
As R9-NEVF2 (not run there): build with tools/sign_sorter.py for positions 4/5/7/13/15/16/17/20 of L05, run tools/sorter_preflight.py and
paste its output; on PASS a ROOM flag for the account-3 orchestrator to publish (db capability). Do not publish.

### R10-ECK64C -- eckert-1864: image-check the eleven O9-W..AG entries (mssEC 19 pp.26-61) (cap 4.5, box 55 min)
Verdict cheapest next (R9-ECK64B): the eleven entries were read from the volunteer text only. Fetch only the needed mssEC 19 page images
(Huntington CONTENTdm, per the host table), crops via tools/iiif_lines.py --image pasted, one blind pass per entry group + reconciliation;
corrections into the folder's corrections/reading files, decode_no9.py --check exit 0. Grade changes only where the image differs.

### R10-BAL103C -- baluze103-letellier-marca-1644: pre-registered 9 shape split (g-tail vs short) against the f.171r 9s (cap 3, box 40 min)
Verdict cheapest next (R9-BAL103B): PREREG first (shape classes defined on f.171r control 9s, whose values are known; gate: the split must
separate f.171r's known values above a label-permutation p95 before it is applied to f.50 tokens). Crops via tools/iiif_lines.py pasted, one
blind shape read + reconciliation. If the control does not separate, NON-TEST, stop; key.tsv untouched either way unless the gate passes.

## Wave 2 (written 09:5x UTC; refills as wave-1 workers finish; intake gate exit 0 for every folder below, 6 Oct 09:4x-09:5x UTC)

### R10-NOX2 -- fr16142-noailles-constantinople-1571: c262 gloss lines below L13, one cut and read (cap 2.5, box 30 min)
As R9-NOX2 in the run9 jobs file (not run there): crops pasted, one blind read, gloss.tsv rows added with grades; if the reading feeds an
existing pre-registered test, re-run it with --check. No depth/N-class edits; flag the verifier if any number in status.json depth_check
moves (rule 10 propagation).

### R10-ECK62S -- eckert-1862: split2 cascade regeneration (cap 3.5, box 45 min)
Verdict cheapest next (R9-ECK62): regenerate the ec18 cascade (main, --assign-free, --read ...) under split2=True (671 -> 729 entries),
scripts and disk only; report which committed numbers move (the 2 wrongtel/confpair targets 9969.543, 9985.564, 1 print_q, 6 assign_free);
every regenerated output keeps its --check; the legacy split stays available. No reading claims beyond what the regenerated scripts show.

### R10-FLOR2 -- florence-dieci-responsive: --median-h option on tools/glyph_atlas.py segment, re-run tuning, c.127 sorter tiles (cap 3, box 45 min)
Verdict cheapest next (R9-FLOR): add a `--median-h` (shared scale) option to tools/glyph_atlas.py segment WITH an offline test in
tools/tests/, re-run atlas_tune/run_tune.sh for L05/L07/L08/L09 s1, then a sorter-tile build for c.127 L02-L18 from the tuned boxes;
tools/sorter_preflight.py pasted; on PASS a ROOM flag for the account-3 orchestrator to publish. Do not publish. No vision subagent needed.

### R10-COL26B -- colbert26-lathuillerie-1644: anchor_split re-run with 23 = n as a C anchor (cap 2, box 30 min)
Verdict cheapest next (R9-COL26): re-run anchor_split on the 14 cleared units with 23 = n now a C anchor (new pre-registered copy pushed
first, control B and gate unchanged), then a per-code control for any new lead with held-out units named before the run. Scripts only.

### R10-LIN -- WITHDRAWN 09:48 UTC (intake gate: check-solved verdict reads `blocked (pending L10: Textos Politicos 1993)`; not spawned) -- antt-linhares-chave: front-trim and join enumeration with its worked-example known-answer control (cap 3.5, box 45 min)
Verdict cheapest next (R8-LIN): the front-trim and join enumeration, known-answer control first (PREREG pushed before the target run);
control below gate = NON-TEST, stop. Use tools/judge_plaintext.py with the era-matched pt18 corpus. No depth/N-class edits.

## Wave 3 (written 10:0x UTC from wave 1's own Verdict lines; intake gate exit 0 for every folder below, 6 Oct 09:4x-10:0x UTC)

### R10-BAL103D -- baluze103-letellier-marca-1644: enlarge the f.171r 9 control to >= 7 known 9s, then run r10/PREREG.md (cap 3.5, box 45 min)
Verdict cheapest next (R10-BAL103C): f.171r L5 onward, crops via tools/iiif_lines.py pasted, one blind pass + alignment against f.172r
for the known values, until >= 7 known 9s (>= 2 of value i); then run r10/PREREG.md exactly as registered (no edits to its gate). If the
enlarged control still cannot reach power, NON-TEST and stop; key.tsv/exceptions untouched unless the registered gate passes.

### R10-DEC2678S -- decode-2678-bnf-colbert127-gravel-1665: sommaire sweep of Mel. Colbert 126-130 for Ratisbon cipher letters (cap 3, box 40 min)
Verdict cheapest next (after R10-DEC2678V): Gallica IIIF manifests / tables (sommaires) of Melanges Colbert 126-130, one request at a time,
for Gravel (or other Ratisbon) letters 1664-1666 in the same two-digit+diacritics design; log each volume checked, canvas/folio of every
hit, and whether any carries an interlinear decipherment. No decoding in this job; list hits for the next brief.

### R10-HUNTTNA -- huntington-blathwayt-madrid-1728: TNA Discovery API search for a contemporary decipherment of BLA191(a) (Sonnet-tier search, run on Opus; cap 1.5, box 25 min)
Verdict cheapest next (R10-HUNT2): TNA Discovery API (per the host table) over SP 94/98-100 and SP 36/13-14 descriptions for a decipherment
or copy of BLA191(a); record each query and hit count; no image fetches beyond one per real hit.

### R10-SEURE4 -- fr3151-seure-1558: fr. 3138 nos. 9 (Tournon 1556) and 24 (Morvilliers 1549) for a legible decipherment (cap 2.5, box 35 min)
Verdict cheapest next (R10-SEURE3): locate both on btv1b90601662 with tools/gallica_folio.py; look for a legible interlinear decipherment;
if one reads, rebuild that key through tools/interlinear_align.py and test it on R1/R2 with the own-text power control first (PREREG
pushed before scoring; power below gate = NON-TEST). If neither reads, log and stop.

## Wave 4 (written 10:2x UTC from waves 2-3's own Verdict lines; intake gate exit 0 for every folder below, 6 Oct 09:4x-10:2x UTC)
Wave 2-3 sizing note: two jobs ran 1.17-1.19x cap (a tool option + test + build in one job; two blind passes + alignment). Caps below
add one unit of margin; stop before a unit that crosses 80% of the cap.

### R10-BAL103E -- baluze103-letellier-marca-1644: fr17 judge test of 9 = s on f.50 (cap 2, box 30 min)
Verdict cheapest next (R10-BAL103D): PREREG first (statistic: tools/judge_plaintext.py fr17 score of the f.50 decode with every 9 read s vs
the committed decode; control that CAN differ: the same substitution at an equal number of random non-9 positions / a shuffled-value
control; gate fixed before scoring). Scripts and disk only; key/exceptions change only if the registered gate passes; decode_key --check.

### R10-COL26C -- colbert26-lathuillerie-1644: held-out check of 15 = e and 32 = u on the f.23 margin postscript (cap 1.5, box 25 min)
Verdict cheapest next (R10-COL26B): PREREG names the held-out span and the gate before the run; scripts and disk only; key_f23 changes
only on a gate pass, graded per rule 4.

### R10-DEC1162 -- decode-1162-modena-ambung-1492: the clear-text transcription pass (cap 3.5, box 45 min)
Verdict cheapest next: the clear-text transcription pass (does not wait on the g/q sort, ASKS 144). Crops via tools/iiif_lines.py pasted
(one subagent call per page, never a full page image), one blind pass + reconciliation; clear text into the folder's files with per-line
image refs. No cipher reading changes in this job.

(R10-HUNTTNA and R10-SEURE4 from wave 3 are spawned in this refill.)
