# LANE FAMILY jobs (account 2, incarnation DEFAULT-account-2-20261009-0009, "FAMILY-A2d") -- 9 Oct 2026 00:2x UTC, lane orchestrator session_01PeUeA4FVwJ7Jiq5Y34XqKk

Lane brief: .claude/briefs/lane-family.md (+ lane-common-blast.md). Cap 60, box 00:09-10:09 UTC 9 Oct. Fourth incarnation: started from
STATUS.md "LANE FAMILY handoff" (DEFAULT-account-2-20261008-2209) next list, then next_steps.py --hot-only runnable rows in scope (re-checked
by hand). Gate 0a: SESSION-SWEEP-account-2 row stale-claimed since 5 Oct (prior incarnations proceeded; ROOM 9073 done). Exclusions:
eckert-* (LANE LEDGER, account 1), lodewijk-van-nassau-1573-74 and baluze167 (LANE SIG-1, account 1, live), huntington-blathwayt and
ceppo-nevers (account-4 LANE DEPTH, 8 Oct; D3-BLA2 says a fourth pass of its design would hit rule 3's third-attempt clause), Gallica
fetches, Birago/Armstrong/Debosnys, every folder with a ROOM claim < 6 h and no done line.
Intake gate 00:2x UTC (tools/intake_gate_check.py): hessen-daenemark-1672 partial, sachsstaatsarchiv-manteuffel-1712 partial, la-garde-1577
open, pro3055-clinton-1779 partial, na-suriname-map-1781 partial -- each "edition/page or full-text-search citation found within 6 lines",
exit 0; antt-linhares-chave "already terminal, nothing to gate" exit 0 (lookup job only, no deep work).

## Common rules for every job
- First commands: `git fetch origin && git checkout -B main origin/main`, `python3 tools/room.py --start`, `date -u`, then a ROOM claim line
  with `tools/room.py` naming your job id, folder, cap and box end time, addressed "for LANE FAMILY-A2d (account 2)". If --start fails to push
  from a detached HEAD: `git push origin HEAD:main; git checkout -B main HEAD`.
- Prior work (`.claude/briefs/prior-work-step.md`): run `python3 tools/prior_work.py <slug> --item-spec '...' --step-type <type> --fetch`
  first and paste its output and exit code (exit 4 = the LOOK/UNCHECKED rows it lists are owed by you, then `--record` them); then checks
  1-4 by hand where v1 does not reach, one line per check (route, query, result) in your NOTES.md section BEFORE the first priced step;
  check 5 after any decode. A check that did not run is "unchecked". If check 1 shows the step already done, one ROOM line and stop.
- Read the folder's NOTES.md tail (Remaining gaps / Escalation / latest dated sections), HYPOTHESES.md and AUDIT.md section list first.
- Good-citizen rule and the CLAUDE.md host table (one request per host at a time, >= 1.5 s apart; stop a host on 429/403/challenge, one
  retry after a pause at most). Report request counts per host. Prefer files already on disk. No Gallica.
- Shared hosts: post `<host> take` / `<host> release` ROOM lines around each batch to www.archiv.sachsen.de ("sachsen"),
  resources.huygens.knaw.nl ("huygens"), service.archief.nl / www.nationaalarchief.nl ("NA"), archive.org ("IA"); if another worker of
  this lane holds the host (a take with no release in the last 30 min), work from disk meanwhile and wait.
- Rule 3 (matched control first; a control that cannot differ from the target on the statistic is a non-test), rule 4 grading, rule 7
  (`--check` scripts). Pre-register any new gate in a PREREG-<JOB>.md pushed before the score is computed.
- Rebase before writing shared files; keep both facts on conflict. Commit only your own paths. Run
  `python3 tools/file_shrink_guard.py <every file you touched>` before the final push; push with `python3 tools/room.py --push <paths>`.
- Partial/open targets: update "## Remaining gaps" / "## Escalation" (Verdict line) and pass `python3 tools/gaps_check.py <target>`.
- Words: never "solved", "cracked", "novel", "first", "new" for anything this project did; rule 10 wording only. Never name the owner; never
  print credentials. Never call AskUserQuestion. Solver jobs: report what was found and where it was not found; do not classify novelty.
- Stop at the cap or at 80% of the box, whichever first; do not start a unit that would cross 80% of either. Opus session floor ~1.5.
- Vision work: crop step mandatory and pasted (`tools/iiif_lines.py --image FILE --out DIR ...`); line or strip crops only, never a full
  page image to a subagent; one page (or half page) per subagent call; ~1.5 per vision call, reconciliation one more unit.
- Done: one ROOM line `done (<start>-<end> UTC by date -u, brief met|stopped at cap): <result, commit>` "for LANE FAMILY-A2d (account 2)",
  then a five-line final report.

- Hosts this wave: arcinsys.hessen.de / Arcinsys image host ("arcinsys"), digitarq.arquivos.pt ("digitarq", >= 3 s, <= 150), archiv.sachsen.de
  ("sachsen"). One worker per host; the jobs below are already split so no two share one.

## Wave 1 (00:2x UTC 9 Oct)

### HDK-131 (Opus, cap 3, box 75 min): hessen-daenemark-1672, full sweep of the neighbour Dänemark 131 for cipher and glosses
NOTES "Known-keys and sibling check (A2-HDK)" item 3 sampled 8 of 106 leaves of HStAM 4 f Dänemark Nr. 131 (Arcinsys archivalDescriptionId
537589, METS mets?detailid=v537589; image path .../daenemark_131/hstam_4_f_staaten_d_nr_daenemark_131_NNNN.jpg): Friedrich von Brandt's 1672
reports from Copenhagen, all clear on the sample. Goal: the other 98 leaves, looking for (a) numeral code groups (3-digit nomenclator like
Nr. 125's 601 Dennemarck / 229 Berlin, or the 2-digit letter table of HCPortal key 255) and (b) interlinear or marginal glosses over such
groups, or a separate decipherment / key sheet. Method: "arcinsys take"; fetch each leaf once at <= 1000 px long side, >= 2 s apart (stop the
host at 403/429/challenge), keep them in the scratchpad (not committed), build contact sheets of 9-12 leaves (PIL) and one vision call per sheet:
"which leaves show numeral code groups or glosses over them; none/light/heavy". Positive control: place Nr. 125's images 0003 and 0004 (on
disk, ciphers/hessen-daenemark-1672/images) blind among the sheets; if the sheet pass misses either, the scale is too small -- halve the sheet
size. Any hit: native-resolution crop for one Opus look (code range vs 601/229/834; glossed?; est. groups; date and sender). Write
dk131_inventory.tsv (leaf, date/sender if visible, cipher none/light/heavy, glossed y/n), a NOTES section "HDK-131 (9 Oct 2026)", the
manifest of URLs (not images) and update "## Remaining gaps"/"## Escalation" (siblings rung) with gaps_check passing. No transcription, no
decoding. ~$2.5 (about 98 requests + 9-11 sheet calls + <= 3 crop looks).

### LIN-SIB (Opus, cap 3.5, box 90 min): antt-linhares-chave, CLNH maço 86 items /02 and /09 thumbnail sweep for cipher
SIBLINGS-2026-10-08.tsv row 1 / NOTES "Keyhunt 7 Oct 2026": maço 86 /02 (126 images) and /09 (212) never opened; /11 is the cipher item (the
positive control). Method as KH1-E did for /04 and /01: tools/digitarq_fetch.py (read its --help), "digitarq take", the `/api/rdigital/{docId}`
page list and thumbnails at the size KH1-E used, >= 3.5 s apart, <= 150 requests this session (stop at 403/429). Build montages locally;
one vision call per montage: "which images show numeral-group blocks or a cipher passage inside prose". Positive control: two /11 cipher pages
(already on disk in this folder's images/, or one fetch) placed blind in a montage; a miss means the scale is too small (say so; enlarge).
Any hit: one fetch at working size and one Opus look (key family: this folder's dictionary key -- numeral ranges as key.tsv -- or other;
date, writer). If the request budget runs out before /09 ends, stop and record the last image index. Write keyhunt/2026-10-09-LINSIB.tsv
(item, image index, cipher none/light/heavy), a NOTES section "LIN-SIB (9 Oct 2026)", update SIBLINGS row state, "## Remaining gaps"
/"## Escalation"; gaps_check. No decoding. ~$3.

### MANT-EYE (Opus, cap 3, box 75 min): sachsstaatsarchiv-manteuffel-1712, eye check of 0214's tokens + 694/09 0007/0009 at native
Handoff next 1. (a) V-MANTR8 / AUD2-MANTR8 rest the f0375_08 pooled gate (7/1000) mainly on frame 0214, whose tokens were never eye-checked on
crops (V-MANTR8: "no crops on disk"; AUD2-MANTR8 eye-checked two runs on the holder frames). Cut line crops of 0214 (and of 0375's rows that
carry a decoded run in f0375_08/runs.tsv) with tools/iiif_lines.py --image (fetch the native frames once, "sachsen take"; URLs in
images/loc694-08-09/frames.tsv), one blind Sonnet pass per crop set + your reconciliation against f0375_08/ciphertext.tsv; list every
disagreement; if any token inside a decoded run changes, regenerate (decode_key.py --check) and rerun f0375_08/shuffle_gate_0375.py with the same
seeds, both numbers before/after. Carry any change into AUDIT.md (dated line under AUDIT (V-MANTR8) and AUDIT 2 (AUD2-MANTR8)) and SO-MANT-0214.
(b) 694/09 frames 0007 and 0009 at native beside 0008 (the heavy glossed frame): glossed? continuation of 0008's letter? est. code tokens; one
Opus look each on crops. NOTES section "MANT-EYE (9 Oct 2026)", Remaining gaps update, gaps_check. ~$2.5.

### LAG-NEXT (Opus, cap 3, box 75 min): la-garde-1577, the next family on the base-code text at N=229 (CPU only)
NOTES Verdict: "running_key family_run with matched control at 0.055/0.084 plus the LAG-GAP score-gap gate, ~$2"; handoff next 2 adds
"syllabary/wordcode, design_prior first". Run `python3 tools/design_prior.py` for this letter first and paste it; then take the ONE family it
ranks highest among those not yet in HYPOTHESES.md (running_key if design_prior gives no better-supported one), run it with tools/family_run.py
at the measured error levels 0.055 (base code) and 0.084 (bracketing, rule 3 error-band clause) with its matched control first, and score with
the LAG-GAP gate design (PREREG-LAG-GAP.md, power check on held-out controls first; if the gate has no power for this family, stop and log
"non-test" -- do not swap gates). Pre-register in PREREG-LAG-NEXT.md and push before scoring. Both numbers into HYPOTHESES.md, NOTES section
"LAG-NEXT (9 Oct 2026)", Remaining gaps / Escalation, gaps_check. No network. Target stays open (rule 5) whatever the result.

### CLIN-RG (Opus, cap 2, box 60 min): pro3055-clinton-1779, the p.123 re-gate (CPU only, no vision)
NOTES "Addendum B2" / Verdict: "re-gate with the class rule fixed (a full pair inside an un-underlined letter run is a letter cell) and an
anchored per-column alignment (start at the decoded run), pre-registered, ~$1.5, no new vision". Inputs: p123_full_reconciled.tsv, the 1778
key, p.102's clear text (read at H). Pre-register PREREG-CLIN-RG.md (rule, alignment, statistic, control: the page-permuted key with 1000
seeds, and also a shuffled-column control that CAN differ on the alignment statistic -- check that before scoring) and push before scoring.
Report both numbers; a PASS confirms the 1778 key on the rest of p.123 (key check on a text read at H: known-text share); a FAIL is logged as
the second attempt of this design (rule 3 third-attempt clause: no third). NOTES section "CLIN-RG (9 Oct 2026)", Remaining gaps, gaps_check.

### SUR-0744R (Opus, cap 5, box 100 min): na-suriname-map-1781, 0744 right half under V-SUR0744's gate
Handoff next 3: "0744 right + 0745 only with V-SUR0744's dot-label permutation gate + 10k-draw p99 pre-registered (~4.5 per unit)". This job
does ONE unit, 0744 right. Read NOTES "V-SUR0744" and the 0744-left sections first (the method, the y-family class caveat). Images on disk
(images_manifest_full.tsv; regen script if a page is missing -- NA host only if needed, "NA take"). Pre-register PREREG-SUR0744R.md (the
dot-label permutation gate, 10,000 draws, p99, the statistic and the held-out rule) and push before scoring. Crop step pasted
(tools/iiif_lines.py --image), two blind passes + one reconciliation, score. NOTES section "SUR-0744R (9 Oct 2026)", HYPOTHESES row, Remaining
gaps, gaps_check. Stop before 0745 whatever the result (one unit per brief).

## Wave 2 (00:4x UTC 9 Oct) -- same common rules. Wave 1 results: ROOM done lines 00:20-00:36 and LEDGER rows of 9 Oct (FAMILY-A2d).
Hosts this wave: digitarq (LIN-SIB2 only), sachsen (MANT-0609Y only), arcinsys (HDK-BRANDT only, <= 10 requests), NA (V-SUR0744R only if needed).

### LIN-SIB2 (Opus, cap 4.5, box 100 min): antt-linhares-chave, maço 86 /09 m0021-m0212 thumbnail sweep
LIN-SIB (NOTES "LIN-SIB (9 Oct 2026)", keyhunt/2026-10-09-LINSIB.tsv) stopped at the request budget at /09 m0020. Same method, same /11
positive control placed blind, same scale; DigitArq >= 3.5 s apart, <= 150 requests per DigitArq session -- if 192 thumbnails need more than
one budget, stop at 150 and record the last index (do not exceed it). Append to keyhunt/2026-10-09-LINSIB.tsv, NOTES "LIN-SIB2 (9 Oct 2026)",
SIBLINGS row state, Remaining gaps / Escalation, gaps_check. No decoding.

### HDK-BRANDT (Sonnet, cap 2.5, box 60 min): check-solved and premise check on the Brandt 1672 cipher leaves of Dänemark 131
HDK-131 (NOTES "HDK-131 (9 Oct 2026)", dk131_inventory.tsv) found 7 leaves of HStAM 4 f Dänemark Nr. 131 (0020 0021 0049 0050 0062 0063
0064) carrying Friedrich von Brandt's numeral cipher from Copenhagen, 1672, with a period decipherment on 0020 (margin, running German) and
0049 (letter per group). Run the check-solved procedure (.claude/briefs/check-solved.md, six sources, including the "## Premise check"
(a)-(d)) for these leaves as one candidate item: Arcinsys record text, HCPortal (api.hcportal.eu) and DECODE listings for "Dänemark 131" /
Brandt, the two solver repositories (grep only), Cipherbrain / Cryptiana, an edition of Brandt's Copenhagen reports or the Hessian-Danish 1672
files (Urkunden und Actenstücke zur Geschichte des Kurfürsten Friedrich Wilhelm for the Brandenburg side, Rommel), open-index scholarship.
Write the verdict as a section "HDK-BRANDT check-solved (9 Oct 2026)" in ciphers/hessen-daenemark-1672/NOTES.md (not a new folder; the
orchestrator decides on a folder from your verdict), with: open/found-solved/blocked word, editions and pages actually read, what fraction of
the cipher the two glossed leaves cover (count groups vs glossed groups from the crops HDK-131 left, or <= 10 arcinsys requests), and the
cheapest first test (e.g. build the letter table from 0049's per-group gloss and test it on 0050/0062-0064 with a shuffled control). No
decoding, no key building. gaps_check on hessen-daenemark-1672.

### MANT-0609Y (Opus, cap 5.5, box 110 min): sachsstaatsarchiv-manteuffel-1712, 694/09 frame 0007 gloss pairs + offset-1 stride-3 sweep
(a) MANT-EYE found 694/09 frame 0007 glossed (~18 tokens; 0008 is its verso). Crop (iiif_lines.py --image, native frame from the sachsen
host), two blind passes + reconciliation of the code groups AND their glosses; compare every gloss pair with key.tsv (Krauske 1-401): agree /
disagree / not in key, counts. Known text used as a key check (guardrail share), C on agreeing values. (b) Then the remaining ~84 unseen 694/09
frames at stride 3 offset 1 (mant0609/inventory_stride3.tsv shows what is seen), the MANT-0609X method (<= 800 px, >= 2 s, contact sheets, blind
positive control 0015/0052), stopping (b) before 80% of cap or box. Append to inventory_stride3.tsv / rank_unglossed.tsv, NOTES "MANT-0609Y
(9 Oct 2026)", Remaining gaps, gaps_check. No transcription beyond 0007.

### V-SUR0744R (Opus, cap 2.5, box 60 min): na-suriname-map-1781, separate verifier of SUR-0744R's class-gate PASS
SUR-0744R (NOTES "SUR-0744R (9 Oct 2026)", PREREG-SUR0744R.md 94e16aee, HYPOTHESES row) reports the CLASS gate ([ij] in m|n) PASS on both blind
passes of 0744 right and the DOT gate FAIL with no headroom. You did not run it. Re-run its scorer (--check) and 3 fresh seeds of the 10k-draw
control, confirm the held-out rule was kept (no 0744R reading used to build the classes), check whether the control CAN differ from the target on
the class statistic (rule 3 non-test clause), spot-check 5 crops against the two passes' labels, and say whether the PASS stands, is fragile, or
is a non-test. Write "## AUDIT (V-SUR0744R)" in AUDIT.md (no N-class change unless the reading changed; depth per the depth bar only if a
reading claim exists), and correct any over-claim in NOTES/HYPOTHESES. Do not run 0745.

### BERGH-GRP (Opus, cap 7.5, box 120 min): wvo-11106-bergh-1572, sign-group reads with a de-stacked layout (the second instrument)
NOTES Verdict / BERGH-STRIP "What would settle it": same 19 gate windows and the same PREREG truth table, re-registered for GROUP scoring in
PREREG-BERGH-GRP.md and pushed before any pass: readers answer "box numbers that together make one sign -> label" (e.g. 3+4 -> y); each number
drawn directly under its own box, no shared verticals (offset sideways when two boxes share an x-range). Build the strips locally from the atlas
on disk (no network), ~4 Sonnet vision calls (2 per pass) + 1 reconciliation, score against the truth table, both numbers vs the registered
gate. This is the second attempt with a different instrument; if it fails, say what a third would need (rule 3: no third run of this one).
PASS: write atlas/group_sign.tsv for the 19 windows only; the sorter rebuild is a separate job. NOTES "BERGH-GRP (9 Oct 2026)", Remaining
gaps, gaps_check.

### LAG-SYL (Opus, cap 3, box 75 min): la-garde-1577, syllabary family control at the measured error (CPU only)
NOTES Verdict (after LAG-NEXT): "syllabary family_run control at the measured error 0.055/0.084, ~$2". Check tools/family_run.py for a
syllabary family (or the nearest matched-design one; if none exists, stop and log "no matched-design tool" -- do not build a solver). Matched
control first at 0.055 and 0.084 (the `noise` parameter LAG-NEXT added to running_key may need the same in this family: add it with an offline
test if so), target only if the control mean meets the gate, scored with the LAG-GAP gate design after its power check. PREREG-LAG-SYL.md pushed
before scoring. Both numbers in HYPOTHESES.md, NOTES "LAG-SYL (9 Oct 2026)", Remaining gaps, gaps_check. Target stays open (rule 5).
