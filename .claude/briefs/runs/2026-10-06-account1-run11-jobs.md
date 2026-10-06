# LANE LANE-RUN11-account-1 jobs (account 1) -- 6 Oct 2026 13:4x UTC, lane orchestrator session_01VY6JLgy3WfXhUMpgVLxBbE

Lane brief: .claude/briefs/default-lane.md (cap 60, box 13:41-23:41 UTC 6 Oct). Gate 0a: SESSION-SWEEP-account-1 row still `claimed` but its
TSV is on disk (5 Oct), proceeding as RUN8-10 and DEFAULT-1240 did. Folders a-h. VERIFY-BACKLOG: only fr16142 register lag (held by the live
DEFAULT-account-1-20261006-1240 lane) and Birago (off limits); the queue row's propagation flags (lodewijk, wvo-hessen, manteuffel) are outside a-h
or held by RUN13-account-2 / RUN11-account-4. Excluded (live lanes): DEFAULT-account-1-1240's folders (baluze167, ceppo-nevers, decode-1162,
decode-2678, es132-vargas, eckert-1862, fr16104, fr16142, fr3151-seure); DEFAULT-account-4-1235's (bl-gualterio, bne20211, castelcicala,
clair571, clairambault1225, clairambault296, decode-1411, destaing, esp318, fr15575, fr16045, fr16106, fr16144, fr4715-f61); Birago, Armstrong,
Debosnys, antt-linhares (check-solved blocked, L10); anything owner-sorter-gated. Every worker: one job, then stop. Each job first checks its
named step is still undone (NEXT-STEPS.tsv lags the folders); if a dated NOTES.md section or ROOM done line already ran it, stop and report.

## Common rules for every job
- First commands: `git fetch origin && git checkout -B main origin/main`, `python3 tools/room.py --start`, `date -u`, then a ROOM claim
  line with `tools/room.py` naming your job id, folder, cap and box end time, addressed "for LANE LANE-RUN11-account-1".
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
- Done: one ROOM line `done (<start>-<end> UTC by date -u, brief met|stopped at cap): <result, commit>` "for LANE LANE-RUN11-account-1",
  then a five-line final report.

## Wave 1 (spawned 13:5x UTC)

### R11A-BRO -- antt-msliv0638-brochado-1712 (NEAR row), letter 134 neighbouring clear prose as a paraphrase crib. Cap 8, box 90 min.
Remaining gaps "Letter 134's neighbouring clear prose" and "Body leaves ... m0200": (a) eye-check m0200 from disk (images/, no fetch) for cipher
and record it in body_leaves.tsv; (b) crop (tools/iiif_lines.py --image) and read once the clear text of m0277 (rest of letter 134), m0272
(22 Oct 1713) and m0278 (letter 135, 29 Oct 1713), all on disk in images/body/, one Sonnet pass per leaf, grade M; (c) list any sentence that
restates or bears on the coded content of letter 134's two spans, and test the candidate reading against it only through a gate pre-registered
before the comparison (a matched control: the same comparison against clear prose from leaves not adjacent to letter 134). Units: 1 + 3 + 1 = 5
x 1.5. Do not change key or grades unless the gate passes; if it does, regrade per rule 4, decode --check, flag a verifier in ROOM (NEAR row
stays; a reading change after AUDIT.md needs a verifier carry-over). Update Remaining gaps / Escalation; gaps_check.

### R11A-AVS57 -- august-van-saksen-1561-64, WVO 57 p3 native re-read. Cap 6.5, box 80 min.
Remaining gap "57 p3": R21 fetched native scans for 74/98/126/53 only, never 57. Fetch 00057 (same source/route as R21's native scans, read
images/manifest.json and the R21 section for it; good-citizen rule), crop p3's 7 lines with tools/iiif_lines.py --image, two blind Sonnet passes
+ reconcile with tools/reconcile_passes.py, then re-run the 57 decode (key_74 + exceptions_57) and report the M count before/after. Units: fetch
1 + 2 passes + 1 recon = 4 x 1.5. decode --check exit 0; a reading change after AUDIT.md -> NOTES note + ROOM verifier flag. Gaps_check.

### R11A-BOWES -- bowes-walsingham-1583, known-keys rung for the code layer. Cap 3, box 50 min.
"While waiting (RUN4-WAITBF)": Tomokiyo's Walsingham-Wotton 1585 reconstruction (cryptiana elizabeth.htm, its images) tried against the code
layer (85, 0100 and the M codes), plus one TNA Discovery API search for a Bowes-period key. Any code value adopted needs a pre-registered
test with a control (e.g. the same key against shuffled code assignments); otherwise record the rung as run with its numbers. Cite Tomokiyo.
Units: ~2 x 1.5. Update Remaining gaps / Escalation; gaps_check.

### R11A-F5160 -- fr5160-letellier-1653 (BnF), the "Next step (READ2-RELABEL, 3 Oct 2026)" section. Cap 4, box 60 min.
Run that section's named step (images on disk or Gallica; tools/gallica_folio.py, tools/iiif_lines.py). Read the section first, state its unit
count x 1.5 in your ROOM claim, and if it exceeds the cap do the first units that fit and write the remainder as the next step. Status line
only as rule 5 allows; if it reaches partial, Remaining gaps / Escalation + gaps_check.

### R11A-F4712 -- fr4712-nevers-duchesse (BnF), same-writer test for the f.13r glossed codes. Cap 3, box 50 min.
Verdict: f.13r's 6 glossed codes cover 6 of f.10r's 37 tokens but stay M "because the f.13r and f.10r hands were not shown to be the same
writer", so the pre-registered crib gate (>=3 C) fails. Pre-register (PREREG file pushed first) a hand-comparison test: digit-shape crops of
f.10r vs f.13r (both from disk or Gallica, tools/iiif_lines.py), scored blind by one Sonnet pass against a control set of digits from a different
known hand in the same volume or fr.3985-family (state which); same-writer verdict only if f.13r matches f.10r clearly above the control. If it
passes, the 6 codes may go M -> C per the existing prereg crib gate and decode --check; if not, record it. Units: 2 x 1.5. Gaps/Verdict update.

Wave 1 sessions (13:47 UTC): R11A-BRO session_01W956MpDJkoqmskt4DHsvuW; R11A-AVS57 session_01KmmzQKP2X8ZTyV55UfB6Jk; R11A-BOWES
session_0145YsNTpBkFf2otrvtFyLiS; R11A-F5160 session_01X9FL3BVx1RMPd79CqY6UMh; R11A-F4712 session_01AkncNGNWxxdttd8XzuPnYA.
