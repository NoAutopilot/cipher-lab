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

## Wave 2 (spawned 14:3x UTC). Gallica IIIF answered 503 to R11A-F5160 at 13:5x-14:0x: no wave-2 job depends on Gallica; if a job finds
it needs Gallica, one probe only, then stop that step and say so.

### R11A-AVS53 -- august-van-saksen-1561-64, WVO 53 p1+p2 native re-read (the AVS57 pattern). Cap 6.5, box 80 min.
Remaining gap "53 p1+p2 (f.266r-v, 13 cipher lines)": passes were cut from 100 dpi images/00053_p1.png. Fetch the native scan of 53 by the route
R11A-AVS57 used for 57 today (read its NOTES section R11A-AVS57 and images/manifest.json; R21 may already hold a native 53 -- check disk first),
crop p1+p2 lines with tools/iiif_lines.py --image, two blind Sonnet passes + reconcile (tools/reconcile_passes.py), re-run the 53 decode
(key_53 + exceptions_53), report M before/after. Units: fetch 1 + 2 passes x 2 pages + 1 recon = 6 x 1.5 -- if the page pair needs more than
4 pass calls, stop before the unit crossing 80% of cap. decode --check exit 0; a reading change after AUDIT.md -> NOTES note + ROOM verifier
flag (the lane runs one verifier carry-over for 53 and 57 together after you). Gaps_check.

### R11A-HEIN -- heinsius-vanhaersolte-1703, "Next step (cheap, depends on no one)" steps 1-2. Cap 3, box 50 min.
Huygens retroboeken Heinsius edition (CLAUDE.md host table: pages.json for the real image URL, >= 2 s apart, descriptive UA). Step 1: Deel 2
p.361-362 (letter 929) as crops via tools/iiif_lines.py --image, one read: does code 142 sit in a spaced-type (deciphered) passage, and what
does the edition print around it. Step 2: Deel 3 p.208 (letter 588): the spaced-type d'Alonne decipherment of a Haersolte cipher -- record
whether any cipher/clear pair there is usable as a crib for this folder. No key change without a pre-registered test. Units 2 x 1.5. Update
the folder's next-step section and Verdict (status line per rule 5 only).

### R11A-BOWES2 -- bowes-walsingham-1583, the SP 106 browse R11A-BOWES named (~$1). Cap 2, box 40 min.
TNA Discovery API only (no record-page scraping): browse SP 106 (ciphers) item list for any Bowes / Scotland 1580-84 key or alphabet; record
hits with references and digitisation flag. No key change. Update Remaining gaps / Escalation; gaps_check.

### R11A-F3789 -- fr3789-mariedemedicis-savary-1610, settle disagreements.tsv against the crops on disk. Cap 6, box 75 min.
NOTES follow-up: "a settling pass on disagreements.tsv against the image would sharpen ciphertext_draft.tsv into a citable ciphertext.tsv".
First check whether ciphertext.tsv already is that settled file (git log, NOTES); if so stop and report. Otherwise: crops are in images/
(no fetch); group the ~72 disagreement rows by crop, one Sonnet subagent call per ~20 rows given only the crop paths and the two readings,
plus your own reconciliation (units: 4 calls + 1 recon = 5 x 1.5 incl. floor). Write ciphertext.tsv with a per-row `settled_by` column;
rows still split stay marked, never silently repaired (rule 2). No decoding in this job. NOTES section + next step line.

Wave 2 sessions (14:24 UTC): R11A-AVS53 session_01MpRCUCgxYLJCKienJ4nxLe; R11A-HEIN session_01FeNp3N7ZVc64Q1zaSWuBP2; R11A-BOWES2
session_01B4RSNSFCHKg1DFbL47x42K; R11A-F3789 session_015C49zvPbrq3PRZkSGoDAXM.

## Wave 3 (spawned 14:5x UTC)

### R11A-AVSK -- august-van-saksen-1561-64, the Verdict's cheapest next: homophonic_anneal on native 53. Cap 3, box 50 min.
Re-run tools/homophonic_anneal.py (or the folder's own wrapper as the AVS53 section names it) on the native ciphertext_53.tsv from R11A-AVS53,
with a matched synthetic control (same N, K, homophone design, German corpus) run first; target only if the control reads. Question: sign 9
(= f by context) and the G1/G7 homophones. PREREG committed before scoring. A key/grade change after AUDIT.md -> NOTES note + ROOM flag; the
lane's verifier carry-over (R11A-AVSV) runs after you, so do not touch AUDIT.md. decode --check exit 0; gaps_check.

### R11A-BOWES3 -- bowes-walsingham-1583, DECODE metadata of the 20 undated SP 106/1-3 leaves (R11A-BOWES2's next). Cap 2, box 40 min.
Login-free DECODE listing/record metadata only (tools/decode_list.py; one request at a time, >= 1.5 s): for each of the 20 undated leaves,
record date clues, correspondents, script, and whether any could be a 1580-84 Scotland/Bowes key; no login, no images unless thumbnails are
login-free. Add to sp106_browse.tsv; NOTES + gaps_check.

### R11A-HAR -- harley-287-1587, the Verdict's cheapest next: lookalike pass on f.88r split pairs. Cap 3, box 50 min.
Disk only: run tools/lookalike_pass.py on the f.88r pass split pairs (images/f88r); then build the owner sign-sorter page for images/f88r with
its focus.tsv (tools/sign_sorter.py), PASS tools/sorter_preflight.py, open 5+ random tiles against the line image, and flag it in ROOM to the
account-3 orchestrator to publish (never publish yourself, never edit ASKS.md). Lookalike residue is agreement, not accuracy. NOTES + gaps_check.
