# LANE FAMILY jobs (account 2, incarnation DEFAULT-account-2-20261010-1709, "FAMILY-A2s") -- 10 Oct 2026 17:2x UTC, lane orchestrator session_01CWL2QHKvh44Ynngqh4eVJf

Lane brief: .claude/briefs/lane-family.md (+ lane-common-blast.md). Cap 60, box 17:13 UTC 10 Oct - 03:13 UTC 11 Oct. Started from STATUS.md
"LANE FAMILY handoff (incarnation DEFAULT-account-2-20261010-1410)" next list: item 1 waits on LOCAL-QUEUE L77; items 2-3 (other Blank Marshall
letters printed in cipher without a gloss, decodable under the period key sheet BL Add MS 4166 f.117; other Thurloe agents whose period keys are
in Add MS 4166) are the runnable in-scope leads. Fresh `next_steps.py --hot-only` read 17:1x UTC: no other in-scope runnable row that the 1109/1410
incarnations had not already found done or image/person-gated (bl-gualterio waits on images; hessen Brandt, la-garde, clinton, manteuffel as in
those handoffs). Gate 0a: SESSION-SWEEP-account-2 stale-claimed since 5 Oct, proceeded. Exclusions: eckert-* and Huntington ledgers (LANE
LEDGER-16/17, account 1), Gallica fetches, Armstrong/Debosnys/Birago.

## Common rules for every job
Exactly the "Common rules for every job" section of `.claude/briefs/runs/2026-10-09-ytbiz-family-1310-jobs.md` (read it in full), with these
substitutions: address every ROOM line "for LANE FAMILY-A2s (account 2)"; the "Hosts this wave" bullet below replaces the one there.
Halfway line: one ROOM line at half the box or half the cap, whichever first (skip if done before). Account 2 is at seven_day
`allowed_warning`: continue (blast rules) and say so in the done line.
Hosts this wave: archive.org ("IA"): THUR-BM3 only, >= 1.5 s, <= 40 requests, take/release lines. THUR-AGENTS and THUR-3370: disk only, no host.

## Wave 1 (17:2x UTC 10 Oct)

Intake gate (17:1x UTC, pasted): `thurloe-printed: partial (line 2) -- edition/page or full-text-search citation found within 6 lines`, exit 0.
ROOM: no live claim on thurloe-printed (FIX-THURBM2 done 16:3x, LANE FAMILY-A2r done 16:47 UTC 10 Oct).

### THUR-BM3 (Opus, cap 8, box 150 min, IA <= 40): thurloe-printed, the other Blank Marshall letters in Birch vols 6-7 -- glossed or not, and decode any unglossed one under the period key f.117
Read ONLY: NOTES sections "## THUR-BM", "## THUR-BM2", "## FIX-THURBM2", the last "## Remaining gaps" / "## Escalation"; `bm/bm_letters.tsv`,
`bm/bm_letters.py`, `bm/decode_44535.py`, `bm/key_period_f117.tsv`, `bm/slips.tsv`, `b146/manifest.tsv`, `b146/v6_leaves.tsv`; HYPOTHESES.md rows
for 135 and 113/173.
Already aligned (do not redo): ll.3370, 40469, 44535, 65889, 77385, 83274, 86815, 89881. Units to look at, vol 6 (bim_ item
`bim_eighteenth-century_a-collection-of-the-stat_thurloe-john_1742_6`, pages `https://archive.org/download/<id>/page/n<leaf>_w2000.jpg`; leaf from
the djvu line via b146/v6_leaves.tsv's mapping or the page-number line in the OCR): ll.10287 (37 numerals), 16481 (26), 17948 (26), 69171 (12),
84125 (Thurloe TO Blank Marshall, 19), 14147 (5), 45614 (6), 64300 (4).
Step 0 (prior work): `python3 tools/prior_work.py thurloe-printed --item-spec 'shelfmark=Birch 1742 vol 6 Blank Marshall letters;sender=Blank Marshall;recipient=Thurloe' --step-type read --fetch`,
paste output and exit code; check 1 by hand (ROOM, NOTES, AUDIT, HYPOTHESES, WORK-QUEUE for each line number) and check 3 against
sources/cryptiana/web/thurloe.htm's "Blank Marshall" section (it says which BM letters Tomokiyo used; record per letter).
Step 1 (census, vision): fetch the vol 6 djvu text once (b146/manifest.tsv names it) and the leaves of the eight units once (manifest rows in
b146/manifest.tsv); for each, crop step pasted (`tools/iiif_lines.py --image FILE --out ciphers/thurloe-printed/bm/crops ...`), one Sonnet call
per leaf on the strip crops: is there a numeral cipher passage, and is it printed with an interlinear/following decipherment? Then vol 7
(`collectionofstat07thur`, djvu text once): run bm_letters.py's logic on it with a vol-7 heading list found by grep ("Blank", "Marſhal",
"Marshal", "Bruges" in headings) -> `bm/bm_letters_v7.tsv`; image-check only vol-7 units with >= 20 numerals, at most 6 leaves.
Output `bm/census_v6v7.tsv`: vol, djvu line, leaf, page, date, direction, numerals, cipher yes/no, gloss printed yes/no/partial, note.
Step 2 (only for a unit with a cipher passage and NO printed gloss): two independent transcriptions (pass A = djvu OCR window by script; pass B =
one Sonnet call per page on line crops, no key shown), reconcile by eye on the crops (one unit). Decode with `bm/key_period_f117.tsv` through a
`--check` script (generalise decode_44535.py into `bm/decode_bm.py <line>` rather than copying it; keep decode_44535.py's output byte-identical
and its --check exit 0), grades per rule 4 (H for groups the sheet states; M for slips/unkeyed; give counts), shuffled-key control (permute
the sheet's values over its codes, >= 200 draws, 4-gram score p95) BEFORE reading the decode, then `prior_work.py ... --reading <reading>
--network` (G3) and paste it. A Thurloe-to-BM letter (84125) may use the same sheet in the other direction: test it the same way; if the
shuffled control is not beaten, log "not this key" in HYPOTHESES.md and stop on that unit.
A decode that beats its control with a clause above the authentication distance: one ROOM flag "THUR-BM3 reading l.<n> for a first verifier".
Units: 8 vol-6 leaves + <= 6 vol-7 leaves at ~0.3 per Sonnet call = ~4.2; djvu fetch/grep ~0.3; per unglossed letter ~2 (2 passes + reconcile +
decode/control); Opus floor 1.5. Cap 8: do not start an unglossed-letter unit once 6 is spent -- list it in Remaining gaps with its cost.
NOTES "## THUR-BM3", Remaining gaps / Escalation / Verdict, gaps_check.py. Report what was found and where it was not found; do not classify novelty.

### THUR-AGENTS (Sonnet, cap 2.5, box 75 min, disk only): thurloe-printed, which Thurloe agents with a period key in BL Add MS 4166 have letters printed in Birch IN CIPHER WITHOUT a gloss
Read: sources/cryptiana/web/thurloe.htm (via `python3 tools/html2text.py`), the folder's index.tsv, AUDIT.md section list, `b146/hits.tsv`,
`b146/v6_hits.tsv`, the key_*.tsv file names and the NOTES "## THUR-B146" / "## THUR-V6" sections. No network (if the IA djvu texts are not on
disk, say which volumes' census is therefore incomplete; do not fetch).
Step 0: `python3 tools/prior_work.py thurloe-printed --item-spec 'shelfmark=BL Add MS 4166 ff.77-124;recipient=Thurloe' --step-type lookup --fetch`,
paste output and exit code.
Task: one row per Add MS 4166 key section in Tomokiyo's page (f.77-78 R4880 ... f.123-124 R4901) and per agent section above it: agent, key
folio, DECODE R-id, Birch volume/page references Tomokiyo gives, whether Tomokiyo says he reconstructed/deciphered that agent's letters, which
of those letters our folder already holds (P-number, key file, AUDIT class), and which Birch numeral passages in b146/*hits.tsv (vols 1, 4, 6)
are by that agent and have NO printed gloss (v6 leaves already classed by THUR-V6; vols 1 and 4 hits not yet image-classed -- mark them
"unclassed"). Output `bm/agents_4166.tsv` and a ranked list in NOTES "## THUR-AGENTS": best three candidates for a cheap read under a period
key (unglossed in print + period key image on DECODE), each with its cheapest next step and cost. Also note the Meadowe (f.102-103, R4890)
and Downing (f.115-116, R4896) keys against the folder's Remaining gaps. Units: one read of the page + one cross-match pass; ~2. Report what
was found and where it was not found; do not classify novelty.

### THUR-3370 (Sonnet, cap 1.2, box 45 min, disk only): thurloe-printed l.3370 word/name codes paired against the period key sheet
The folder Verdict's cheapest next (FIX-THURBM2): "l.3370 name pairing against the period sheet, ~$0.5". Read NOTES "## THUR-BM2" and the last
Remaining gaps; `bm/key_period_f117.tsv`, `bm/key_blankmarshall_7.tsv`, `bm/pairs7/` (l.3370 pairs), `bm/bm_gate7.py` docstring.
Step 0: prior_work.py `--item-spec 'shelfmark=Birch 1742 vol 6 l.3370;date=1657-02-11;sender=Blank Marshall;recipient=Thurloe' --step-type align --fetch`
(KNOWN is the input for align, not a stop), paste it. Task: for l.3370's codes 109-191, 481, 733, pair Birch's printed gloss spans with the
sheet's names 102-139 (sheet value = Birch gloss? agree / disagree / sheet silent), write `bm/l3370_names.tsv` (code, birch_gloss, sheet_value,
verdict) by a script with `--check`; disagreements are rule-4 data conflicts to log in HYPOTHESES.md with both witnesses, never settled by
majority. Do not edit key_blankmarshall_7.tsv (generated). Units: one script + one look; ~0.8. Report what was found and where it was not found.
