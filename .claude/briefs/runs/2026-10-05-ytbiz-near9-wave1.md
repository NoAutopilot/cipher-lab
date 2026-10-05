# LANE-NEAR9 wave 1 (5 Oct 2026, written 05:2x UTC by LANE-NEAR9, account 2 / ytbiz, session_011SW24uoRbdvoyBAWiy9m98)

Lane brief: `.claude/briefs/runs/2026-10-05-acct3-lane-near9.md`.
Common rules: the "Common to every job below" section of `.claude/briefs/runs/2026-10-04-ytbiz-near4-wave1.md`, with "LANE-NEAR4" read as
"LANE-NEAR9" everywhere (claims "(account 2 worker, for LANE-NEAR9)", done line addressed "for LANE-NEAR9 (account 2)"). You run on Opus 5.5;
reading subagents Sonnet. Subagent readers RETURN text; you write files. One target, one step; stop when met (Usage 7); a follow-up is a
one-line suggestion in NOTES. Do not touch: fr16045-pisany-rome-1585, fr15575-syllabic-1592-95, fr16142-noailles-constantinople-1571,
birago-fr3252-1571-72, august-van-saksen-1561-64, clairambault1225-paget-1714, fr3151-seure-1558, eckert-1864, lope-hurtado-1522,
huntington-blathwayt-madrid-1728 (LANE-RUN6), bne20211-ferdinand-1478, fr4712-nevers-duchesse, armstrong-madison-1808, debosnys-1883, any owner
sorter file. Do not edit status lines, status.json, STATUS.md, NEAR.md: flag instead. Never write a dollar figure for yourself. No novelty words
(rule 10). Never call AskUserQuestion. Never print credentials or the DECODE account name. Never name the owner.

Intake gates (pasted by LANE-NEAR9 before briefing, below the jobs).

## N9-GRAV -- VERIFIER: fr2980-gramont, key.tsv ST = L at grade C (cap USD 4; box 50 min)
You are a verifier, not the solver (N8-GRA2/N8-GRA3 were other sessions); do not protect their conclusion. Claim under audit: "ST = L now C in
key.tsv (4/4, eye-checked)" (NOTES section "fr.3040 no.6 f.18v + f.19r top vs Le Grand III pp.455-456 ... (N8-GRA3)", PREREG-N8-GRA3.md /
PREREG-N8-GRA2.md). Steps: (1) re-run the committed alignment/statistic scripts from disk and confirm 0.838 / 0.871 and the null p99s reproduce
(report any drift); (2) independently eye-check every ST occurrence in fr.3040 no.6 (Gallica btv1b9059870w canvases 32-34, crops via
`tools/iiif_lines.py`, pasted) against the aligned Le Grand III pp.454-457 word: is the sign ST (not a look-alike) and does the print give L at that
position? (3) check ST elsewhere: does L read sensibly at every ST in f.30 / f.29r under key.tsv (list each, with the word it makes)? Any
counter-case drops C to S or M. (4) Check the "C" grade itself: rule 4 C = from known plaintext; is the Le Grand print a decipherment of this very
letter (date, recipient match)? Write a dated section "## Verification of ST = L at C (N9-GRAV, 5 Oct 2026)" in AUDIT.md with the verdict
(CONFIRMED / LOWERED to S|M, with reasons), and correct key.tsv + `python3 tools/decode_key.py ciphers/fr2980-gramont --check` only if lowered.
Do not touch z (N9-GRAZ owns it). Do not decode anything new.

## N9-GRAZ -- fr2980-gramont: z image check, A vs R (cap USD 2; box 40 min)
NOTES Verdict line ("cheapest next: image-check, the z sign ..."). fr.3040 no.6 aligns z to R in 23/26 occurrences against key.tsv's A (listed in the
N8-GRA3 section). PREREG first (short file `PREREG-N9-GRAZ.md`, pushed before looking): what counts as "z is two signs" (shape split visible on the
crops and consistent with the A/R split) vs "one sign, key error" vs "one sign, homophone with two values". Then crop the 26 fr.3040 no.6 z
occurrences and f.30's z occurrences (`tools/iiif_lines.py`, pasted), and the z cells in the Tomokiyo and Lasry key images on disk; one Sonnet
blind shape-sort call (no values shown) on the z crops, then you compare. Report: split / no split, what each sub-shape aligns to, and the effect
on f.30 under each hypothesis (count of words that change, list them). key.tsv changes only if the prereg's split criterion is met (then the new
value at the grade the evidence gives; decode --check). Gaps refresh.

## N9-COSV -- VERIFIER: costabili-modena-1491, N8-COS 10 sign values at C (cap USD 4; box 50 min)
You are a verifier, not the solver. Claim under audit: "R1166 P1-P2 key: 10 sign values at C (N8-COS)" (NOTES section "R1166 P1-P2 group-level
crops (N8-COS ...)", `align/PREREG-N8-COS.md`, pass files in `align/`). Steps: (1) re-run the committed scoring from the committed pass files:
pass A 0.575, B 0.459 vs shuffle p95 0.244/0.219, floor 0.430 -- reproduce or report drift; (2) for each of the 10 values, list every group where
it rests (cipher group, gloss chunk above, both passes' reads); a value resting on one group or on passes that disagree is not C (rule 4: C needs
the gloss to fix the value unambiguously); (3) compare with decode-1168-modena-costabili-1492/key.tsv (the 9 agree / z differs claim) and say
whether the decode-1168 key is an independent witness or derived from the same images; (4) if crops are not on disk, one DECODE browser login
(`tools/decode_browser_login.js`) for R1166 P1-P2 only, images never committed. Write "## Verification of the N8-COS C values (N9-COSV, 5 Oct
2026)" in AUDIT.md: per value CONFIRMED C / LOWERED (S|M) with the reason; carry any lowering into the folder's key file and NOTES Remaining gaps.

## N9-XM -- key_crossmatch leads, one matched-control check each (cap USD 4; box 50 min)
ROOM.md 5 Oct 02:53-02:54 lists four nightly `tools/key_crossmatch.py` hits: (a) fr3993-villeroy-1595 keys/key_f200_no57_syll.tsv on
sanguszkow-mniszech-dunin-1714/ciphertext.tsv stat 4.12; (b) hellen-frederick-1752 key_r4370/key_decode.tsv on the same ciphertext 3.63;
(c),(d) clair1161-avis-flandre-1688 two/key_shuf4_s1.tsv and pool/key_shuf3_s1.tsv (themselves shuffled control keys) on
decode-1168-modena-costabili-1492/ciphertext.tsv 3.95 / 3.85 (gate 3.292, null p99 3.498). Read `tools/key_crossmatch.py --help` and its source
first. PREREG one file (`research/PREREG-N9-XM.md` or under each target's folder) before computing: for each lead, the statistic the tool uses on
that target, scored for the cross key AND for >= 200 random keys of the same size/value alphabet AND for >= 200 permutations of the cross key's
values (shuffled key), plus the same cross key on a letter-order-shuffled copy of the target; a lead survives only if the cross key beats the
shuffled-key p99 on that very ciphertext. Expectation to test, not assume: (c)/(d) say the decode-1168 ciphertext scores high for any key -- if so,
report the tool's gate as miscalibrated for that ciphertext (per-target null needed) and propose the one-line tool fix in ROOM as a flag (do not edit
the tool unless the fix is a per-target null with an offline test, Usage 8). For a survivor, print the first 60 decoded tokens and say by eye whether
any word stretch is in a language; no reading claimed, no grades written. Results in each target's NOTES (short section) + a line in
HYPOTHESES.md where the folder has one. Disk only, no network.

## N9-BUL -- bullet-tuscany-1944: native-resolution photo check + forumfree thread fetch (cap USD 1.5; box 30 min)
NOTES Verdict line ("cheapest next: native-resolution image check of the photo + forumfree thread fetch, ~$1"). It is a NEAR row: read its NEAR.md
row first. Fetch the photo at native resolution from the source named in NOTES (good-citizen rule, one request at a time, browser UA only where
the host table says), record manifest; check the transcription on disk against it sign by sign (one Sonnet call with crops if needed, or your own
eye); fetch the forumfree thread once (`tools/browser_fetch.js` if curl is challenged; on a challenge stop, single retry). Report transcription
corrections (list) and anything in the thread that bears on status (a claimed solution, a better image, provenance). If a claimed solution is found,
record it verbatim with the URL and date and do not evaluate novelty. Update NEAR.md row's Evidence/Last-touched only (allowed for this job),
`python3 tools/near_check.py`. Gaps refresh.

## N9-BAL -- baluze167-davaux-1637: re-fetch Baluze 168 c511-512, look for a glossed letter in the f.246 hand (cap USD 3.5; box 50 min)
NOTES Verdict line. Earlier fetch of c511-512 returned Gallica 404/500 (N8 handoff). `tools/gallica_folio.py` on the Baluze 168 ark to confirm
the canvas/folio map first (paste), then one native fetch per canvas (1.5 s apart, single retry). Then survey the volume's other leaves in the f.246
hand for a letter carrying an interlinear or marginal decipherment (contact-sheet at low resolution from the IIIF image API, <= 40 requests; one Sonnet
call per contact sheet asking only "which leaves carry cipher with a clear gloss above or beside it"). Output: a TSV of candidate glossed leaves
(canvas, folio, what is glossed, how much). No transcription in this job; price the next step (group crops + 2 passes + reconcile per leaf) in the
Verdict. Gaps refresh.

```
fr2980-gramont: partial (line 3) -- edition/page or full-text-search citation found within 6 lines
rc=0
costabili-modena-1491: partial (line 1) -- edition/page or full-text-search citation found within 6 lines
rc=0
bullet-tuscany-1944: partial (line 3) -- edition/page or full-text-search citation found within 6 lines
rc=0
baluze167-davaux-1637: partial (line 1) -- edition/page or full-text-search citation found within 6 lines
rc=0
sanguszkow-mniszech-dunin-1714: open (line 1) -- edition/page or full-text-search citation found within 6 lines
rc=0
decode-1168-modena-costabili-1492: found-solved (line 3) -- edition/page or full-text-search citation found within 6 lines
rc=0
```
