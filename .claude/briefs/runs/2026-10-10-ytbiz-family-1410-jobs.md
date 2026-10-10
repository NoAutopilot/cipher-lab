# LANE FAMILY jobs (account 2, incarnation DEFAULT-account-2-20261010-1410, "FAMILY-A2r") -- 10 Oct 2026 14:1x UTC, lane orchestrator session_01YGgwSiFSAd7MrSZekcvBL6

Lane brief: .claude/briefs/lane-family.md (+ lane-common-blast.md). Cap 60, box 14:11 UTC 10 Oct - 00:10 UTC 11 Oct. Started from STATUS.md
"LANE FAMILY handoff (incarnation DEFAULT-account-2-20261010-1109)" next list: item 1 (thurloe-printed l.44535) is the one runnable unread-cipher
lead; items 2-5 are known-text (Costabili a1), a campaign (Suriname), a retired instrument (Manteuffel y-glyph) or person/LOCAL-QUEUE gated.
Fresh `next_steps.py --hot-only` read 14:1x UTC: no other in-scope runnable row that prior incarnations had not already found done or gated
(august 53 p2 re-read 6 Oct; bl-gualterio waits on images; hessen-daenemark Brandt sweep done; la-garde nothing cheap; Thurloe P3/P10 residue
no-key-material). rah-salazar EF API probed by the orchestrator 14:15 UTC: still PrimaryUnavailable (1 request).
Gate 0a: SESSION-SWEEP-account-2 stale-claimed since 5 Oct, proceeded. Exclusions: eckert-* and Huntington ledgers (LANE LEDGER-15, account 1),
Gallica fetches, Armstrong/Debosnys/Birago.

## Common rules for every job
Exactly the "Common rules for every job" section of `.claude/briefs/runs/2026-10-09-ytbiz-family-1310-jobs.md` (read it in full), with these
substitutions: address every ROOM line "for LANE FAMILY-A2r (account 2)"; the "Hosts this wave" bullet there is replaced by the one below.
Halfway line: one ROOM line at half the box or half the cap, whichever first (skip if done before). Account 2 is at seven_day
`allowed_warning`: continue (blast rules) and say so in the done line.
Hosts this wave: archive.org ("IA": THUR-BM only, >= 1.5 s, <= 40 requests, take/release lines).

## Wave 1 (14:2x UTC 10 Oct)

Intake gate (14:1x UTC, pasted): `thurloe-printed: partial (line 2) -- edition/page or full-text-search citation found within 6 lines`, exit 0.
ROOM: no live claim on thurloe-printed (last THUR-V6 done 12:28 UTC 10 Oct).

### THUR-BM (Opus, cap 9, box 150 min, IA <= 40): thurloe-printed, Blank-Marshall (Bruges) key from the four glossed vol 6 letters, then l.44535
The folder Verdict's cheapest next (THUR-V6, 10 Oct 2026): "Blank-Marshall pool alignment with a check of leaf 378, ~$3". Read ONLY the
NOTES sections "## THUR-B146", "## THUR-V6", "## Remaining gaps (THUR-V6 ...)", "## Escalation (THUR-V6 ...)", `b146/v6_hits.tsv`,
`b146/v6_leaves.tsv`, `b146/v6_crops/manifest.json`, the AUDIT.md section list, and the docstring of `tools/interlinear_align.py`.
Bim_ item: `bim_eighteenth-century_a-collection-of-the-stat_thurloe-john_1742_6`, pages `https://archive.org/download/<id>/page/n<leaf>_w2000.jpg`.
Step 0 (prior work, before any priced step): prior_work.py with `--item-spec 'shelfmark=Birch 1742 vol 6 l.44535 p.374;date=1657-07-08;sender=Blank;recipient=Marshall'`
(step-type decode) and paste it; check 1 by hand (ROOM, folder, AUDIT, HYPOTHESES, SIBLINGS, WORK-QUEUE for 44535 / Blank / Marshall / Bruges);
then fetch leaf 378 (and 376 if the letter heading is not on 377) and look for a printed decipherment of l.44535 after the cipher ("The same
decyphered", a clear version, a footnote). If Birch prints one, l.44535 is a key-source pair like the others: record it, align it with the pool
(step 2) as a fifth pair, skip step 3's reading and say so. Also grep the cached vol 6 OCR for other letters of the same correspondent in
1657-58 (heading words "Blank", "Marshall", "Bruges") not among the five, and list them (no image fetch beyond the five letters' leaves).
Step 1 (transcription of the four glossed letters, ll.40469 leaf 341, 65889 leaf 553 (+552 if it opens there), 77385 leaves 648-649, 89881
leaf 759; and l.44535 leaf 377): fetch each leaf once (manifest in b146/), crop step pasted (`tools/iiif_lines.py --image ... --out
ciphers/thurloe-printed/bm/crops ...`), numeral groups and the printed interlinear gloss read by TWO independent passes: pass A = the cached
djvu OCR text of the window (script, no model), pass B = one Sonnet subagent call per page on line crops (numerals and gloss, no key shown);
reconcile disagreements by eye on the crops (one more unit). Printed type, so disagreement should be low; if A and B differ on more than a
tenth of the groups on a page, run a second Sonnet pass on that page before reconciling. Output `bm/<line>_pairs.tsv` (group -> gloss span)
in the folder's existing *_pairs.tsv format, and `bm/l44535_ciphertext.tsv`.
Step 2 (key and known-answer gate): PREREG-THURBM.md pushed in its own commit (check `git log origin/main -1 -- <file>`) BEFORE any score:
leave-one-letter-out -- build a key from three glossed letters with `tools/interlinear_align.py`, decode the fourth, score per-group agreement
with its printed gloss (classes: letter/syllable groups vs word/name codes reported separately), against a shuffled-key control that CAN differ
(permute the key's values over its codes, >= 200 draws, p95); gate = all four folds above their own p95 AND pooled held-out agreement >= 0.70
on codes the training key covers; report coverage (share of held-out groups the training key covers) beside it. Then build the full key from all
four (`bm/key_blankmarshall.tsv`, counts, grade per the folder's convention for print-gloss keys).
Step 3 (only on gate PASS and no printed decipherment of l.44535): decode l.44535 with the full key through a `--check` script (rule 7, e.g.
`tools/decode_key.py` with a decode.json in bm/), per-token grades (rule 4: H/C/S/M/I counts), coverage, the same shuffled-key control on
l.44535, and `tools/judge_plaintext.py` with an era-matched English corpus if the folder's spec names one (paste the output, PASS or FAIL); then
prior_work.py `--reading <reading> --network` (G3) and paste it. A clause above the authentication distance: one ROOM flag line "THUR-BM reading
for a first verifier" for the lane. On gate FAIL: log the family row in HYPOTHESES.md, do not decode, and name what more material would lift
coverage.
Units: ~5 pages x (1 OCR script + 1 Sonnet call ~0.8) + 5 reconciliation looks ~0.5 + a possible second pass on 2 pages + align/gate/decode
~1.5 + Opus floor 1.5 = ~8; cap 9. NOTES "## THUR-BM", Remaining gaps / Escalation / Verdict, gaps_check.py. Report what was found and where
it was not found; do not classify novelty.

## Wave 1 results (costs by get_session)
- THUR-BM 11.03 / 9 (Opus, 1.23x over): leaves 377-378 carry no printed decipherment of l.44535; key bm/key_blankmarshall.tsv (104 agreed
  codes, 1 split) from ll.40469/65889/77385/89881, PREREG-THURBM gate PASS both blind passes (pooled 0.871/0.861; every fold above p95 <0.10);
  l.44535 151/151 groups C, 4-gram -1.007 vs shuffled-key p95 -1.431; 3 more glossed BM letters listed (ll.3370, 83274, 86815). ROOM flag for
  a first verifier. Commit bd6d47855.

## Wave 2 (15:0x UTC 10 Oct)
Hosts this wave: archive.org ("IA": V-THURBM and THUR-BM2 share it -- take/release lines, the second waits for the first's release; <= 30
requests each). No other host than the open indexes / Google Books API for V-THURBM.

### V-THURBM (Opus, cap 6, box 120 min): FIRST VERIFIER, thurloe-printed l.44535 (Blank-Marshall at Bruges, 8 July 1657 N.S., Birch vol 6 p.374)
A separate session from the solver (THUR-BM, session_013aecKkuzFyrHQ1JDKgUb4x); do not protect its conclusions. Use the CLAUDE.md "Verifier
brief (template)" steps 1-5 in full, with step-type `audit` for prior_work.py. Claim under audit: "l.44535, printed in cipher without a
decipherment in Birch 1742 vol 6 p.374, reads 151/151 groups at C under a key rebuilt from Birch's printed decipherments of four sibling
Blank-Marshall letters (bm/reading_l44535.txt)". Inputs: NOTES "## THUR-BM", bm/ (key, gate, decode_44535.py, crops, PREREG-THURBM.md).
(a) Rule 7: re-derive the reading from bm/l44535_ciphertext.tsv + bm/key_blankmarshall.tsv with `bm/decode_44535.py --check` and by your
own independent script; eye-check the ciphertext on bm/crops/l44535_p374_L0*.jpg (numerals group by group) and the slip groups the solver
names ("tyemselues", "mepllow", "nany", "preuennted", "dew heeret", key code 9 s|b) -- record per slip: transcription slip, encipherment slip
or key gap; regrade anything not supported (M/I). (b) Rule 10 search, logged per family: Birch vols 1-7 (other places the same letter or its
substance could print: an abstract, an "intelligence" letter of the same week), Calendar of State Papers Domestic 1657-58, Clarendon State
Papers (Calendar vol. III, Macray 1876) for the Royalist side of the same news (Charles Stuart at Brussels, Gloucester to the field, Hyde,
creditors, July 1657), Nicholas Papers vol IV (Camden), Firth/Scott on Thurloe's intelligencers ("Blank"/"Marshall" identity; e.g. Firth,
EHR, and Underdown, Royalist Conspiracy), Bodleian MS. Rawl. A. catalogue (whether the manuscript itself carries a decipherment), IA/HathiTrust
EF/Google Books phrase search on 2-3 distinctive clear+decoded phrases (with a positive control phrase from a glossed sibling), the open indexes,
the solver repositories; JSTOR-QUEUE rows in both families (i) and (ii). (c) N-class with key source (`period`: rebuilt from period
decipherments printed by Birch), depth per rule 4a (`tools/depth_check.py`) with one true content sentence if D2+, safe/unsafe sentences.
(d) Write AUDIT.md "## AUDIT (V-THURBM, l.44535)", status.json fields per the folder's convention, and a SECOND-OPINIONS-QUEUE.tsv row if N3+.
If N3+ D2+, add one WORK-QUEUE.tsv row `AUD2-FAMILY-A2r-1` (account-3, brief: CLAUDE.md verifier template, second adversarial audit of this
item) per lane-common-blast.md "Results", and a ROOM line naming it for the account-3 orchestrator. file_shrink_guard on every touched
file. Do not decode anything else, do not touch other targets. Units: re-derivation + eye check ~1.5, searches ~2, write-up ~1, floor 1.5.

### THUR-BM2 (Opus, cap 6, box 120 min, IA after V-THURBM's release or between its takes): thurloe-printed, Blank-Marshall key witnesses from ll.3370, 83274, 86815
NOTES THUR-BM Remaining gaps bullet 2. Prior-work step (prior_work.py, step-type key) first and pasted. Fetch the leaves of the three glossed
letters (bm/bm_letters.tsv gives the OCR windows; find leaf by the running heads as THUR-V6 did), crop step pasted, two blind Sonnet passes per
letter on crops exactly as THUR-BM did (passes in bm/passes/, pairs bm/<line>_pairs_B<k>.tsv), then extend the key into a SEPARATE file
`bm/key_blankmarshall_7.tsv` and re-run the PREREG-THURBM gate unchanged as a leave-one-letter-out on all seven letters (write the seven-letter
table to bm/gate7.tsv; the pre-registered rule is not changed, only the pool). Then report, for l.44535's slip groups and code 9, what the
three extra witnesses say -- as a proposed FIX list in NOTES, NOT applied: do not edit key_blankmarshall.tsv, reading_l44535.*, AUDIT.md or
status.json (V-THURBM is auditing the committed reading in parallel; a change after its audit is a rule 10 propagation the orchestrator
schedules). NOTES "## THUR-BM2", Remaining gaps / Escalation / Verdict, gaps_check.py. Units: 3 letters x 2 passes ~0.8 + reconcile ~0.5 +
gate ~0.5 + floor 1.5 = ~5.5. Report what was found and where it was not found; do not classify novelty.
