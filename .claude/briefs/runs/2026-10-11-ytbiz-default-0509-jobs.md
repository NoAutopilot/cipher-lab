# LANE DEFAULT-account-2-20261011-0509 jobs (account 2, lane orchestrator session_01Gtsge7DYsP57RsomYTZuyY) -- 11 Oct 2026 05:3x UTC

Lane brief: .claude/briefs/default-lane.md. Cap 60, box 05:09-15:09 UTC 11 Oct (80% line 13:09). five_hour `allowed` at start.
Gate 0a: SESSION-SWEEP-account-2 stale-claimed since 5 Oct, proceeded (as every incarnation since 9 Oct). Backlog read 05:2x UTC:
VERIFY-BACKLOG.tsv regenerated (80 rows: audit2 35, counted 45; the high "counted" rows are D1 items depth_check already lists as
"class without a reading, not counted"; Birago rows off limits; eckert-1864 audit2 rows left to the account-1 LEDGER lanes); then
`next_steps.py --hot-only` runnable rows. Exclusions: Birago/Armstrong/Debosnys, eckert-* and Huntington ledgers, Gallica fetches.

## Common rules for every job
Exactly the "Common rules for every job" section of `.claude/briefs/runs/2026-10-09-ytbiz-family-1310-jobs.md` (read it in full), with these
substitutions: address every ROOM line "for LANE DEFAULT-A2-0509 (account 2)"; the hosts bullet below replaces the one there. Halfway line:
one ROOM line at half the box or half the cap, whichever first (skip if done before). Check `get_session` is not available to you: say
"cost not visible to this session" in the done line.
Hosts this wave: archive.org ("IA": THUR-BRV only, >= 1.5 s, <= 30 requests); open indexes / Google Books / IA full-text for AUD2-MANT
(keys per CLAUDE.md item 3, <= 60 requests per host); everything else disk only. No Gallica, no sachsen fetch.

## Wave 1 (05:3x UTC 11 Oct)

### V-PISA3 (Opus, verifier, cap 3, box 60 min): fr16045-pisany-rome-1585, check of the UNA3-PISA carry-over
The folder's own Verdict's cheapest next (NOTES.md l.1090). You are a verifier, not UNA3-PISA's session or any solver on this folder.
Read AUDIT.md "## Carry-over UNA3-PISA (9 Oct 2026)" (l.277 on) and the earlier V-PISA-T32 section as the pattern; NOTES.md "## UNA3-PISA";
una3_pisa/ (PREREG, scripts, outputs). Check: (a) the PREREG commit precedes the score commit (git log); (b) re-run the una3 scripts and
any `--check`, confirm the G1-G3 numbers; (c) the item C count reconciliation the carry-over names -- recount from the committed
reading_tokens/decode outputs and state the true C/H/S/M counts per item; (d) status.json propagation: the rows for this folder carry
the reconciled counts and depth fields (rule 4a; `python3 tools/depth_check.py` after); correct what is stale. Write "## AUDIT (V-PISA3)"
in AUDIT.md; no class raised unless the reading changed. Update the Verdict line's cheapest next; gaps_check must pass.

### BAL-SHAPE (Opus, cap 4, box 80 min): baluze167-davaux-1637, shape-level control of the f.228/f.229 letter signs
NOTES.md "## Remaining gaps (UNA3-BAL, 9 Oct 2026)" item 2. Intake gate (05:2x UTC, pasted): `baluze167-davaux-1637: partial (line 1) --
edition/page or full-text-search citation found within 6 lines`, exit 0. Disk only (native crops exist for f.228/229 and the glossed
Baluze 170 leaves -- if the glossed-leaf crops are not on disk, stop and say so; no Gallica). Design: pre-register in PREREG-BAL-SHAPE.md
before any read: blind sign tiles from f.228/f.229 letter positions mixed with tiles from the glossed Baluze 170 leaves of the same hand
whose letter value the gloss fixes (positive control) and from a different-hand/key leaf (negative control), one blind Sonnet tile
pass (two if the first is under gate), score agreement with the sealed labels; the control must be able to fail differently from the
target (rule 3, AX-5799/KHF-4 lesson: a vocabulary-overlap negative control). If the gate passes, regrade the f.228 M letter tokens it
licenses (rule 4) and re-run decode `--check`; if not, log non-test/negative honestly. Units: ~3 vision calls + 1 reconciliation at ~1.5.

### F143-DEC (Opus, cap 6, box 100 min): fr3985-nevers-revol-1593 folder, BnF fr.3988 f.143r -- decode-level key-family discrimination
KHF-4's named next (NOTES.md "## Keyhunt 7 Oct 2026", last paragraph; the orchestrator's say-so is this brief). Intake gate (pasted):
`fr3985-nevers-revol-1593: blocked (line 1) -- already terminal, nothing to gate`, exit 0 (a different-instrument test on a sibling
leaf, not a status change). Disk only: keyhunt_f143/img/c304_reg.jpg (f.143r) -- if lines 6-9 cannot be cropped legibly from it, stop and
say so (no Gallica). Pre-register PREREG-F143-DEC.md before any decode: crop step pasted (`tools/iiif_lines.py --image ... --out
keyhunt_f143/dec/crops`), one blind transcription of lines 6-9 against key60's sign list (tools/keys/key60.tsv, fr3986 sign_guide) plus a
second blind pass for reader error; decode with key60 vs (i) >= 200 value-shuffled key60 keys, (ii) the Mayenne 1592 key (fr.4715 f.61r,
the KHF-4 negative control, if its table is on disk), judged by `tools/judge_plaintext.py` with the best era-matched French corpus in
tools/data (say which; note the fr16 fold-spread caveat in CLAUDE.md). Gate: key60 decode above the shuffled p95 AND above the Mayenne
decode. Grade any tokens (rule 4); a PASS licenses only "the leaf decodes under no.60 better than controls", not a reading. Report what
was found and where it was not found; do not classify novelty. Units: 2 vision + 1 reconcile + CPU.

### AUD2-MANT3 (Opus, second verifier, cap 7, box 140 min): sachsstaatsarchiv-manteuffel-1712, Audit 2 for three results
status.json results titled "SHStA Dresden Loc. 694/08 frame 0176 (letter of 2 July 1712)..." (N3 D1, audit V-MANT0176), "... 694/08 frame
0454 (autumn 1712)..." (N2 D2, V-MANT0454) and "... 694/09 frame 0136 (about Apr 1713...)" (N2 D1, V-MANT0136). You are a session separate
from those verifiers and from every solver on the folder. CLAUDE.md "Verifier brief (template)" steps 1-5, per item: try to find each
reading's plaintext or decipherment in print (Manteuffel / Flemming / Augustus II correspondence editions, Krauske 1893 and its sources,
Saxon diplomatic histories, Google Books country=US + key, IA full text, OpenAlex/S2/CORE, Persée/HAL), phrase searches on the decoded
spans, JSTOR-QUEUE rows in both families (i) and (ii) for the owner's runner. Upheld/lowered class per item, depth unchanged unless
wrong. Write "## AUDIT 2 (AUD2-MANT3)" in AUDIT.md, set audit_status 'two audits' and the audit_refs in status.json for each, and for
any N3+ item the SECOND-OPINIONS-QUEUE.tsv row (CLAUDE.md, verifier duty). Do not decode. Units: 3 items x ~2.

### THUR-BRV (Sonnet, cap 1.5, box 45 min, IA <= 30): thurloe-printed, locate Brieven V (1723-25) / the 1725 Verbael on IA
The folder's Verdict cheapest next (~$0.5). Read the last "## Remaining gaps" / "## Escalation" and the dutch1653/ notes for what text is
wanted (the Dutch of 27 June and 22 Aug). IA advancedsearch + metadata only (IA take/release); for each candidate item record identifier,
title, volume, years, access (full view / lending / printdisabled) and whether its djvu text contains the two dates; fetch the djvu text
only of a full-view hit and grep it. Write findings in a dated NOTES.md section and update the Remaining gaps line. No reading, no decode.

## Wave 2

### THUR-BAMF (Opus, cap 5, box 100 min, IA <= 25, after THUR-BRV's IA release): thurloe-printed, the Bamfylde pool -> vol 6 l.19092
STATUS.md "LANE FAMILY handoff (incarnation DEFAULT-account-2-20261010-1709)" next 2 and NOTES.md l.3528-3547 (Bamfylde pool gap). Intake gate
(pasted): `thurloe-printed: partial (line 2) -- edition/page or full-text-search citation found within 6 lines`, exit 0. Steps: (0) prior work,
incl. Tomokiyo sources/cryptiana/web/thurloe.htm for any Bamfylde key/sheet; (1) image p.161 of vol 6 (does a printed decipherment follow
l.19092? if yes, align it and stop with a C-grade note) and the vol 4 p.195/p.232 continuations (b146/manifest.tsv, crop step pasted, one
Sonnet call per page on strip crops); (2) build a Bamfylde code->meaning table from the glossed siblings (l.68904 p.576, vol 4 pp.194-195,
231-232) with `tools/interlinear_align.py` (grade C per pair, counts); (3) PREREG-THUR-BAMF.md pushed before the read: coverage of
l.19092's ~24 numerals by the table vs >= 200 value-shuffled tables and vs a different correspondent's key (key_downing or key_lockhart),
gate = above shuffled p95 and above the other key; (4) read only if the gate passes, grade per token (rule 4), decode script with
`--check` (rule 7). Below authentication distance is expected (~24 numerals): say so; a non-test is a valid result. Report what was found
and where it was not found; do not classify novelty. Units: ~3 vision + CPU.

### F143-DEC2 (Opus, cap 5, box 90 min, disk only): fr3985-nevers-revol-1593 folder, fr.3988 f.143r -- the F143-DEC test re-scoped
F143-DEC (05:2x UTC) stopped at its material check and wrote two design notes in NOTES.md (section F143-DEC, l.~250-275): read them first.
Orchestrator's choice: option (a) -- use f.143r L05-L08 from keyhunt_f143/img/c304_reg.jpg (legible), not L06-L09; and replace control arm (ii)
by the reverse foreign-key arm F143-DEC proposed (a key60-tag blind transcription of the Mayenne leaf m61_reg.jpg's lines, decoded with key60,
judged the same way: a foreign-key text that key60 should NOT read). Arm (i) (>= 200 value-shuffled key60 keys) unchanged. Everything else
as F143-DEC's brief above (PREREG pushed first, crop step pasted, two blind passes on the target lines, judge with the named corpus and the
fold-spread caveat). Gate: key60 decode of f.143r above the shuffled p95 AND above the Mayenne reverse-arm decode. If the reverse arm itself
scores at or above shuffled p95, the judge does not separate key families at this N: log non-test.

## Wave 3 (06:1x UTC 11 Oct)

### THUR-BAMF2 (Opus, cap 3, box 75 min; IA <= 20 with take/release; cryptiana.web.fc2.com <= 4): thurloe-printed, Bamfylde p.160 open codes
NOTES.md "## THUR-BAMF" and its "## Remaining gaps (THUR-BAMF, 11 Oct 2026)" item 1. Fetch Tomokiyo's Bampfield First Cipher table image (bamp1.jpg,
from the page sources/cryptiana/web/thurloe.htm links to; and bamp2.jpg if one more request) into ciphers/thurloe-printed/bamf/tomokiyo/
(credit Tomokiyo, rule 8); compare its letter values with our 51-code table code by code (agree/disagree/absent, as a TSV) -- an
independent known-answer check on our table, not a replacement. Then look up 937, 745, 356 (word/name codes) and 94 in his table and in
the other glossed 1655-57 Bamfylde letters of vols 4-6 (djvu headings named in that gap line; numerals near glosses by script, image
only for a unit that carries one of the four codes, at most 4 leaves). Any value found: grade C (print gloss) or H (period table as
published), never S by context; re-run bamf/decode_bamf.py with the additions and `--check`. Do not re-score the gate. Update NOTES.md
section + Remaining gaps; gaps_check must pass. Report what was found and where it was not found; do not classify novelty.
After THUR-BAMF2: V-BAMF (Opus, verifier, cap 3, box 60): first verifier of the p.160 fragments (rule 10 + rule 4a), briefed separately.
