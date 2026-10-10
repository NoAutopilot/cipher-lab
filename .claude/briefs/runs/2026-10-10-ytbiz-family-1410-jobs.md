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
