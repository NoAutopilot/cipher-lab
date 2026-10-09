# LANE SIG-5 worker jobs (account 1, lane orchestrator session_01JvVtEoTkDwoLi8A8sXXA3L; written 9 Oct 2026 04:4x UTC by date -u)

Lane brief .claude/briefs/lane-significance.md (+ lane-common-blast.md); starts from STATUS.md "LANE SIG handoff" (SIG-4) next list.
Gallica probe 04:43 UTC 9 Oct (IIIF manifest, one request): 403 -- next item 1 (Baluze/Gramont) skipped; items 2-4 run below.
Intake gate (pasted 04:4x UTC, exit 0): `lodewijk-van-nassau-1573-74: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`.

**Common to every worker** -- exactly as `.claude/briefs/runs/2026-10-09-acct1-sig4-jobs.md` "Common to every worker" (read it), plus:
every ROOM line ends "for LANE SIG-5 (account 1)"; prior-work step (`.claude/briefs/prior-work-step.md`) pasted before the first priced step;
rule 10 and rule 4a wording only; never "new", "first", "solved"; never AskUserQuestion; never print credentials; never name the owner.
Solvers: report what was found and where it was not found; do not classify novelty.

---

## SIG5-4612E (Opus 5.5, solver; cap $5, box 90 min, no network, no vision calls): 4612 crib placement, attempt 3 of 3 -- different INPUT, control first
Target lodewijk-van-nassau-1573-74. Read NOTES "## SIG-7208", "## SIG-4612C", "## SIG-4612D", both PREREGs and scripts, `sig7208/cribs_4612.tsv`,
`sig7208/key_7208_sig.tsv`, `ciphertext_4612_v3.tsv` (its clear/'?' rows), HYPOTHESES.md 4612 rows.
Rule 3's third-attempt clause: attempts 1 and 2 failed on OPPOSITE bars (false, then recall); a threshold between them is forbidden. This attempt
changes the INPUT, not a margin: (i) the clear words written in 4612 itself (the letter's clear-text rows) as positional context that fixes
topic and segment boundaries, and (ii) 7208's list-B name-code values graded H there (312 ville, 221 hollande; 335/336 only if graded H/C, else
out) as fixed anchors that a placement must not contradict and may be required to straddle. M values (270, 217, 276-as-Mastrecht) are NOT anchors.
0. Prior work pasted (`tools/prior_work.py lodewijk-van-nassau-1573-74 --item-spec 'shelfmark=KHA A 11;wvo=4612;date=1574-03-06;sender=Lodewijk van Nassau;recipient=Willem van Oranje' --step-type key`).
   First establish in one paragraph whether (i) and (ii) actually exist in usable quantity in 4612 v3 (how many clear rows, where; how many 312/221
   tokens in 4612). If neither gives at least a handful of anchor positions, STOP before any run: log "attempt 3 not run -- no different input
   available in 4612", leave the instrument at attempt 2 of 3 untested-by-this-tool, and finish NOTES. That is a valid outcome.
1. `sig4612e/PREREG.md` committed and pushed before any run: the SAME 25 cribs, 0.60 share, f calibration, seeds, pools (b)/(c), false bar
   <= 2.0/seed, recall >= 0.30, G > 0 as SIG-4612D (import its code, do not copy). Control (a) on the 5811 cut must receive the SAME kind and
   number of extra inputs at matched density (clear-word context rows and anchor codes drawn from 5811's own print at the 4612 counts) --
   otherwise the control cannot fail the way the target can (rule 3, AX-5799).
2. Control (a) first; any bar failing -> CONTROL BELOW GATE, crib placement on 4612 logged "[retired] for 4612, instrument crib_place (3 attempts)",
   untested-by-this-tool, not refuted; 4612 not scored.
3. On (a) PASS: (b), (c), target as SIG-4612C; on target PASS apply via a decode config, grades S at most / M in windows, decode_key --check exit 0,
   judge_plaintext on the decode and on the shuffled control's decode, quote stretches with M marked.
4. NOTES "## SIG5-4612E (9 Oct 2026, account 1, for LANE SIG-5)", HYPOTHESES.md row, Remaining gaps item, gaps_check, shrink guard. Units: code+test ~$1.5,
   control ~$1, target ~$1, NOTES ~$1.

---

## SIG5-58-270 (Opus 5.5 with at most 2 Sonnet vision calls; cap $3, box 60 min): code 58 in 5811/4610/4611, and 7208 p1_L11 pos9 (270 vs 276)
Target lodewijk-van-nassau-1573-74. Two small checks, one ROOM claim.
A. Code 58 (key_full z, grade I, "table rule, not observed in 4613/4615"). SIG-4612D: cribs from 5811's own print implied 58 -> V in 3 control
   seeds. Locate the 7 occurrences of 58 in ciphertext_5811.tsv and align each against the Groen IV CDLXXXIII text (the folder's `groen/` copy and
   the 5811 alignment already in the folder): which letter does Groen's text need at each slot (z, v/u, other, null, unclear)? Then the single
   occurrences in 4610 and 4611: does z or v read better in the surrounding decode (show the word both ways). Pre-state in NOTES before looking
   what counts: 58 -> v is supported only if >= 5 of the 7 5811 slots need v/u under the print and none needs z. Outcome: a proposed grade change
   for 58 in key_full (I -> C as v, or confirm z) written to HYPOTHESES.md and NOTES as a proposal with the slot table; apply it to key_full.tsv only if
   the pre-stated bar is met AND decode_key --check regenerates cleanly (rule 7) -- report the 4610/4611 token changes.
B. 7208 p1_L11 pos9: SIG-7208 kept 270 at M ("last digit 5/6/0 glyph"); it matters for 4612's two 276 slots via the list-B conflict 270/217.
   Prior work: NOTES "## SIG-7208" eye-settle lines. Fetch the 7208 PDF once from resources.huygens.knaw.nl (one request; sha1 must equal
   31aa506d73904d9034f99e4b263bcf48efeccc4e; regen_images.sh line 172-173 gives the render and crop commands; paste them), crop the token and
   the same hand's clear 0, 5 and 6 digits elsewhere on p1-p3 (at least 3 of each) into `sig7208/look_270/` (small crops only; commit them, under 1 MB).
   One blind Sonnet look at the target crop plus the digit exemplars (filenames neutral: no '270'/'276' in names), then your own look; record
   270 / 275 / 276 / undecided with the exemplar comparison in NOTES. Do not change any key value; update the conflict row in HYPOTHESES.md /
   key_conflicts.tsv with the reading of the sign. Also check what the period decipherment (f.223r, p5) writes at that place, if SIG-7208 aligned it.
NOTES "## SIG5-58-270 (9 Oct 2026, account 1, for LANE SIG-5)", gaps_check, shrink guard. Hosts: resources.huygens.knaw.nl 1 request.
