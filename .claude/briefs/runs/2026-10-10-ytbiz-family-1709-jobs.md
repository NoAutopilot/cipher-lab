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

## Wave 1 results (costs by get_session)
- THUR-AGENTS 1.61 / 2.5 (Sonnet): bm/agents_4166.tsv (38 rows); three agents tie to a 4166 sheet by heading (Blank Marshall R4897, Meadowe
  R4890/1, Downing R4896/5); ranked: BM small windows (THUR-BM3 covers), vol 7 sweep + Downing R4896, Meadowe l.69008 (vol 6 p.487~, 232
  numerals, heading OCR "Denmark ...") under R4890 with glossed l.75081 as the held-out control.
- THUR-3370 0.98 / 1.2 (Sonnet): bm/l3370_names.tsv; 19 codes: 9 agree, 4 referent, 1 conflict (115 Birch Don John vs sheet Rochester, logged), 5 sheet-silent.

## Wave 2 (17:4x UTC 10 Oct)
Hosts this wave: de-crypt.org ("DECODE"): THUR-MEAD only, ONE browser login (`tools/decode_browser_login.js`, `--guess-fullsize`), >= 2 s apart,
<= 15 requests. archive.org ("IA"): THUR-MEAD may fetch <= 4 vol 6 leaves ONLY after THUR-BM3's IA release line (THUR-BM3 holds IA; read ROOM;
work the DECODE part first).

### THUR-MEAD (Opus, cap 5.5, box 120 min): thurloe-printed, Meadowe's period key sheet (BL Add MS 4166 f.102-103, DECODE R4890; R4891 the second copy) and the class of l.69008
Read: NOTES "## THUR-AGENTS", `bm/agents_4166.tsv`, "## THUR-V6" (l.75081), `b146/hits.tsv` rows 69008/75081, `b146/v6_hits.tsv`,
`bm/key_period_f117.tsv` + `bm/audit_period_key.py` (the f.117 transcription is the model to copy), sources/cryptiana/web/thurloe.htm
"Meadowe" section (E=6/50/50, 559 Denmark, 610 Dutch ambassador), the DECODE section of CLAUDE.md's host table.
Step 0: `python3 tools/prior_work.py thurloe-printed --item-spec 'shelfmark=BL Add MS 4166 f.102-103;sender=Philip Meadowe;recipient=Thurloe;date=1657' --step-type key --fetch`
and `--item-spec 'shelfmark=Birch 1742 vol 6 l.69008 p.487;sender=Philip Meadowe;recipient=Thurloe' --step-type read`, paste both with exit codes;
check 1 by hand (R4890, R4891, 69008, Meadowe in NOTES/AUDIT/HYPOTHESES/ROOM/WORK-QUEUE).
Step 1 (DECODE, one login): fetch R4890 and R4891 full-size images (and, in the same login, R4896 and R4895 images for a later Downing job --
fetch only, no reading). Manifest in `ciphers/thurloe-printed/keys4166/manifest.json` (record, image, bytes, sha1, size); keep the folder
under 30 MB (JPEG at native size; if over, keep the manifest and the Meadowe images only). Scrub the account name from any saved HTML.
If full-size is refused, record the exact response and stop the sheet step (thumbnails are not a transcription source).
Step 2 (IA, after THUR-BM3's release): leaf for p.487 of the bim_ vol 6 copy (and the facing leaf), strip crops (`tools/iiif_lines.py --image`),
one Sonnet call: heading/correspondent, cipher present, printed gloss present? Record the class. If l.69008 is not Meadowe, or is glossed,
say so: the sheet still gets transcribed (step 3) as a key source for the glossed control, but no decode of l.69008 is planned.
Step 3 (sheet transcription): crop the R4890 sheet into row strips, two independent Sonnet passes per image (no Birch gloss shown), reconcile
by eye (one unit), cross-check against R4891 where legible (a second period copy: disagreements listed, not settled by majority).
Output `keys4166/key_period_meadowe_f102.tsv` (code, value, class letter/syllable/word/name, pass agreement, R4891 agreement) plus
`keys4166/meadowe_sheet.py --check` (rule 7 regeneration from the pass files). Spot-check against Tomokiyo's stated values (E=6/50, 559, 610).
Do NOT decode any letter in this job; the known-answer gate on l.75081 and the l.69008 decode are the next wave's, priced from what you find.
Units: DECODE fetch ~0.4; IA class ~0.4; sheet 2 images x 2 passes ~0.8 each = 3.2 + reconcile 0.8; Opus floor 1.5 => ~6, cap 5.5: if the
sheet is denser than f.117, transcribe R4890 f.102 only and list f.103 in Remaining gaps. NOTES "## THUR-MEAD", Remaining gaps / Escalation /
Verdict, gaps_check.py. Report what was found and where it was not found; do not classify novelty.

## Wave 1-2 results so far (costs by get_session)
- THUR-BM3 9.68 / 8 (Opus, 1.21x over): bm/census_v6v7.tsv -- vol 6's eight units are all printed in clear (OCR numerals were prose numbers);
  vol 7 has seven BM cipher letters (Jun-Sep 1658), all printed with a gloss; no unglossed BM letter in vols 6-7. Vol 7 IA page_numbers.json
  off by one (leaf = page + 7). Vol 5 not searched.
- THUR-MEAD (running at 17:5x): R4890 sheet letters/nulls/names transcribed (keys4166/key_period_meadowe_f102.tsv, 189 codes); l.69008 is
  Jephson, glossed (p.577), not Meadowe. Images of R4896 (Downing) on disk.

## Wave 3 (18:0x UTC 10 Oct)
Hosts this wave: archive.org ("IA"): THUR-V57 only, after THUR-MEAD's IA release line, <= 20 requests, take/release. THUR-83274: disk only.

### THUR-V57 (Sonnet, cap 3, box 100 min, IA <= 20): thurloe-printed, Birch vols 5 and 7 -- every cipher passage classed glossed / unglossed, by agent
The djvu texts are on disk: `sources/ia-fulltext/thurloe-gz/collectionofstat05thur_djvu.txt.gz`, `..._07thur_...` (do not refetch). Read NOTES
"## THUR-B146", "## THUR-BM3", "## THUR-AGENTS", `bm/agents_4166.tsv`, `bm/census_v6v7.tsv`, `b146/hits.tsv`, index.tsv (P2-P28 already in the
folder: vol 5 P25-P28 and vol 7 Fauconberg P16-P24 are KNOWN, list them as such, do not re-class).
Step 0: `python3 tools/prior_work.py thurloe-printed --item-spec 'shelfmark=Birch 1742 vols 5 and 7 numeral passages;recipient=Thurloe' --step-type lookup --fetch`, paste with exit code.
Step 1 (disk): `python3 tools/ia_numeral_runs.py <id> --cache <dir holding the gunzipped texts> --inline-run 4 --tsv ...` on vols 5 and 7, with
the B146 positive control (vol 3's 18 known windows, as b146/control.tsv did; report recall); then for each hit window: the letter heading
(correspondent, place, date) from the OCR, agent attribution against agents_4166.tsv, and the OCR gloss evidence (alphabetic rows interleaved
with numeral rows, "The same decyphered", etc.). Also grep vol 5 headings for Blank Marshall ("Blank", "Marſhal", "Bruges", "B. M.") with
`bm/bm_letters.py DJVU --vol 5` if the option fits (else a --vol flag in the same style, vol 6/7 outputs byte-identical, --check exit 0).
Step 2 (IA, <= 18 leaves, vol 5 `collectionofstat05thur`, vol 7 leaf = page + 7 per THUR-BM3): image-class ONLY the windows whose OCR gloss
evidence is ambiguous AND whose agent has a period key in Add MS 4166 (Blank Marshall R4897, Meadowe R4890, Downing R4896/R4895) or is
unattributed; strip crops (`tools/iiif_lines.py --image`), one Sonnet call per leaf. Output `bm/census_v5v7_all.tsv` (vol, djvu line, page,
leaf, heading, date, agent, 4166 key, numerals, gloss: yes/no/partial/unknown, evidence: ocr|image, note) and NOTES "## THUR-V57" with the list
of unglossed passages under a key in hand, ranked by numeral count. Do not transcribe or decode. Units: script ~0.5; <= 18 Sonnet looks at
~0.12 = 2.2; stop before a look that crosses 80% of cap. Report what was found and where it was not found; do not classify novelty.

### THUR-83274 (Sonnet, cap 1, box 45 min, disk only): thurloe-printed, l.83274's last two unglossed rows under the period key f.117
Read NOTES "## THUR-BM2" (l.83274), the last Remaining gaps, `bm/pairs7/l83274_pairs_B1.tsv`/`B2.tsv`, `bm/passes/` for l.83274, `bm/crops/`
for its page, `bm/key_period_f117.tsv`, `bm/slips.tsv`, `bm/decode_44535.py`.
Step 0: prior_work.py `--item-spec 'shelfmark=Birch 1742 vol 6 l.83274;sender=Blank Marshall;recipient=Thurloe' --step-type decode --fetch`, paste it.
Task: from the two blind passes (they already hold the numerals of the two unglossed rows; if not, eye-read them on the committed crop and say
so), decode under the f.117 sheet with a `--check` script (`bm/decode_83274_tail.py`, or extend decode_44535.py's pattern without changing its
outputs), grade per rule 4 (H for sheet-stated groups, M for slips/unkeyed; counts), shuffled-key control on the same groups (permute the
sheet's values over its codes, >= 200 draws, 4-gram p95; say if the run is too short for the control to discriminate) computed before
reading the text; then `prior_work.py ... --reading <file> --network` (G3) and paste it. Write NOTES "## THUR-83274". A residue of two rows is
small: no verifier flag unless it carries a clause above the authentication distance. Units ~0.7. Report what was found and where it was not found;
do not classify novelty.

## Wave 3 results (costs by get_session)
- THUR-MEAD 6.79 / 5.5 (Opus, 1.24x): keys4166/key_period_meadowe_f102.tsv 189 codes (H 166, M 23), five sheet-internal conflicts; word list
  left; l.69008 = Jephson glossed. R4896 P2/P3 images on disk.
- THUR-V57 1.88 / 3 (Sonnet): bm/census_v5v7_all.tsv 148 groups, control 10/10; 7 imaged all glossed; 118 not classed (OCR cannot see the
  vol 5/7 gloss style); no BM/Meadowe headings in vols 5/7 outside BM3's seven.
- THUR-83274 0.99 / 1 (Sonnet): 29 groups H 28 M 1 under f.117; control a non-test at 28 letters (disclosed); below AD.

## Wave 4 (18:2x UTC 10 Oct)
Hosts this wave: archive.org ("IA"): THUR-V7LOOK only, <= 25 requests, take/release.

### THUR-V7LOOK (Sonnet, cap 2.5, box 80 min, IA <= 25): thurloe-printed, image-class the unclassed Downing / headingless vol 7 groups and vol 5 l.15486
Read NOTES "## THUR-V57" and its Remaining gaps, `bm/census_v5v7_all.tsv`, the page-to-leaf notes in "## THUR-BM3" (vol 7 leaf = page + 7, OCR
page estimates off by up to 2 pages).
Step 0: prior_work.py `--item-spec 'shelfmark=Birch 1742 vol 7 Downing numeral passages;sender=George Downing;recipient=Thurloe' --step-type lookup --fetch`, paste it.
Task: page-locate first (fetch the leaf, read the printed page number on a header strip; move by the difference, never guess twice), then one
strip crop per group (`tools/iiif_lines.py --image`), one Sonnet call or an eye read per strip: glossed / unglossed / partial. Order: the three
headingless vol 7 groups (ll.37197, 37263, 37730) and vol 5 l.15486 first, then the Downing groups in THUR-V57's ranked order by numerals until
8 Downing groups are classed or the cap/requests run out. Stop rule for the Downing tail: if all 8 sampled Downing groups are glossed, stop and
say so (Birch glosses Downing systematically; the remaining 21 are then "not classed, prior strongly glossed"). Update `bm/census_v5v7_all.tsv`
in place through `bm/v57_final.py` (its --check must stay exit 0; add the new evidence as image rows) and write NOTES "## THUR-V7LOOK" with any
unglossed passage under a key in hand (Downing R4896) ranked by numerals. Do not transcribe or decode. Units: ~12-16 leaf fetches + ~12 strip
looks at ~0.12; stop before a look crossing 80% of cap. Report what was found and where it was not found; do not classify novelty.

## Wave 4 results (costs by get_session)
- THUR-V7LOOK 1.94 / 2.5 (Sonnet): 13 more groups image-read, all glossed (8 Downing, 3 "headingless" = Fauconberg to H. Cromwell p.413,
  vol 5 l.15486 = Montagu p.179); stop rule hit; 21 Downing groups "not classed, prior strongly glossed". Birch vols 5-7: no unglossed
  passage under a key in hand found.

## Wave 5 (18:5x UTC 10 Oct)
Hosts this wave: resources.huygens.knaw.nl ("huygens"): THUR-DUTCH only, >= 2.1 s, <= 60 requests, take/release. archive.org ("IA"): THUR-V146
only, <= 30 requests, take/release.

### THUR-DUTCH (Sonnet, cap 3, box 100 min, huygens <= 60; github.com sparse clones <= 2): thurloe-printed, Birch vol 1 Dutch 1653 cipher letters -- premise check against the De Witt editions
Context: Birch 1742 vol 1 prints intercepted 1653 Dutch letters with numeral cipher (b146/hits.tsv vol 1 rows with "Beverning/Vande Perre 1653
family" in on_file). LANDSCAPE.md row 43: "Dutch ciphers 1653, Beverning and Vande Perre to Boreel" closed-negative by both solver repositories;
Aymeloglu recovered the alphabet of Vande Perre's letters to de Bruyne (unsolved-ciphers/vande-perre-1653, cyphersolver/thurloe). Tomokiyo:
sources/cryptiana/web/dutch.htm. Question: does a printed clear text exist for any of these cipher letters (the Dutch side kept deciphered or
plain copies: Japikse's Brieven van/aan Johan de Witt, Huygens retroboeken `dewitt`), which would make them known-plaintext pairs for a key
(recovery, grade C) and open the closed-negative Boreel letters to a key-in-hand read?
Step 0: `python3 tools/prior_work.py thurloe-printed --item-spec 'shelfmark=Birch 1742 vol 1 Dutch ambassadors 1653;sender=Beverning;recipient=De Witt;date=1653-08-08' --step-type lookup --fetch`,
paste with exit code; check 1 by hand (grep Beverning, Perre, Boreel, Nieuport, 1653 in this folder, ROOM, CATALOG, LANDSCAPE, sources/).
Step 1 (disk + 2 sparse clones): list every vol 1 Dutch cipher passage from b146/hits.tsv (djvu line, page, heading, date, numerals) -> the IA
vol 1 djvu text if needed is `collectionofstat01thur` (sha1 in b146/manifest.tsv; fetch once only if not on disk, 1 IA request, after THUR-V146's
release or before its take -- read ROOM). Sparse-clone (grep only, never copy code: Aymeloglu has no licence) `aaymeloglu/unsolved-ciphers`
path `vande-perre-1653` and `dbourdeau/cyphersolver` path `targets/thurloe` (or whatever path holds it); record what each read, which letters,
their key and their negative, with the commit hash.
Step 2 (huygens): in Brieven van Johan de Witt deel 1 and Brieven aan Johan de Witt deel 1 (retroboeken `dewitt`; sources/huygens/NOTES.md
gives the search route), search each Birch letter by correspondent pair and date (+-1 day, Old/New Style) and by a distinctive clear phrase
from Birch's own English summary or clear part; positive control: one 1653 letter you know is printed there (say which). Record per letter:
printed clear text yes/no (edition, page, note "uit cijfer"/"gedechiffreerd"/plain copy), or the edition's own footnote on a cipher.
Output `dutch1653/pairs_census.tsv` (birch_vol, djvu_line, page, date, sender, recipient, numerals, gloss_in_birch, solver_state,
edition_hit, edition_page, note) and NOTES "## THUR-DUTCH" ranking candidate pairs (cipher in Birch + clear text in the edition) by numerals,
with the cheapest next step (transcription + interlinear_align) and cost. Do not transcribe or decode. Units: clones ~0.3, ~20-40 huygens
queries + OCR page reads ~1.5. Report what was found and where it was not found; do not classify novelty.

### THUR-V146 (Sonnet, cap 2.5, box 80 min, IA <= 30): thurloe-printed, image-class the unclassed Birch vol 1/4/6 numeral windows (non-Blank-Marshall)
Read NOTES "## THUR-B146", "## THUR-V6", "## THUR-AGENTS", `b146/hits.tsv`, `b146/v6_hits.tsv`, `bm/census_v6v7.tsv`, the page-to-leaf method in
"## THUR-BM3"/"## THUR-V7LOOK" (read the printed page number first, then move by the difference).
Step 0: prior_work.py `--item-spec 'shelfmark=Birch 1742 vols 1 4 6 numeral passages;recipient=Thurloe' --step-type lookup --fetch`, paste it.
Units, in this order: vol 6 Jephson ll.68655, 75347; Bampfield 19092, 68904; Hague 41201, 94181; Gookin? 4076 (109 numerals); vol 4 hits in
b146/hits.tsv with numerals >= 20 (Broghill 4057 first); vol 1 non-Dutch hits with numerals >= 20 (the Dutch 1653 rows belong to THUR-DUTCH:
skip them). One strip per unit (`tools/iiif_lines.py --image`), one Sonnet call or eye read: cipher yes/no, gloss printed yes/no/partial,
correspondent. Output `b146/census_v146.tsv` and NOTES "## THUR-V146": any unglossed cipher passage, its correspondent, and whether a glossed
sibling pool of the same correspondent exists in Birch (the THUR-BM route: rebuild a key from glossed siblings, then read the unglossed one).
Do not transcribe or decode. Stop at 80% of cap. Report what was found and where it was not found; do not classify novelty.

## Wave 5 results (costs by get_session)
- THUR-DUTCH 2.16 / 3 (Sonnet): Brieven van Johan de Witt dl 1 (Japikse) p.72 prints De Witt's 1653 key (1-66 homophonic alphabet; OCR column
  order scrambled); p.92 n.2 says it serves the Beverning/Nieuwpoort letters (Thurloe I pp.304, 308-309, 336/339 "geheel te ontcijferen");
  Dutch clear texts in print for the 24 Jul De Witt letter (Van Sypesteyn; edition pp.99-101 extracts; Birch l.32198-32400, p.351, 397
  numerals) and the 18 Jul envoys' letter (Nijhoff Bijdragen X p.291; Birch l.31246, p.339, 196 numerals). Boreel letter (Birch p.435,
  l.38695, 128 numerals; closed-negative at both solver repositories) symbols 6-33 inside the key's range. dutch1653/pairs_census.tsv.
- THUR-V146 1.84 / 2.5 (Sonnet): 12 imaged units with cipher, 7 glossed, 4 partial, 1 unglossed (vol 6 l.19092 Bamfylde p.160, ~24 numerals;
  glossed Bamfylde siblings l.68904 p.576 and vol 4 pp.194-195, 231-232). Vol 1 non-Dutch hits not read (djvu 500).

## Wave 6 (19:1x UTC 10 Oct)
Hosts this wave: resources.huygens.knaw.nl ("huygens") and archive.org ("IA"): DUTCH-KEY only (take/release; huygens <= 10, IA <= 20).

### DUTCH-KEY (Opus, cap 7, box 150 min): thurloe-printed/dutch1653 -- the printed De Witt 1653 key read from the page image, known-answer test on Birch vol 1 pp.351 and 339, then the Boreel letter p.435 under it with a matched control
Read: NOTES "## THUR-DUTCH" and its Remaining gaps, `dutch1653/pairs_census.tsv`, `dutch1653/edition/VAN_DEWITT_01_071-073, 091-101`,
`dutch1653/edition_evidence.tsv`, `b146/hits.tsv` vol 1 rows, the "## THUR-BM" PREREG/gate pattern (bm/PREREG-THURBM.md, bm/bm_gate.py),
the docstrings of `tools/decode_key.py` (--try, decode.json) and `tools/judge_plaintext.py` (is there a 17th-c. Dutch corpus in tools/data? say).
Credit: the key is printed by Japikse (after Fruin) -- grade H for values it states (rule 4); Bourdeau (cyphersolver targets/thurloe) and
Aymeloglu (unsolved-ciphers vande-perre-1653) worked the Boreel letter and logged it stuck/not read by their alphabets; cite both, copy nothing.
Step 0: `python3 tools/prior_work.py thurloe-printed --item-spec 'shelfmark=Birch 1742 vol 1 p.435;sender=Beverning;recipient=Boreel;date=1653-09-27' --step-type decode --fetch`
(adjust the date to what the leaf shows), and the same for p.351 (`--step-type key`), paste both with exit codes.
Step 1 (key, huygens <= 10): fetch the edition page image of p.72 (and p.71/73 if the table spans) via pages.json (image_url), crop the table,
read it yourself (one Sonnet pass + your own eye read; printed type) -> `dutch1653/key_dewitt_1653.tsv` (code, letter, source page) with a
`--check` script; note p.92/p.107's statements (codes above 100 for persons/countries; Beverning's extra numerals).
Step 2 (IA <= 20): Birch vol 1 `collectionofstat01thur` leaves for p.351, p.339, p.308-309 and p.435 (page-locate by the printed page number;
the vol 1 djvu text answered 500 to THUR-V146, so use the page image header). Crop step pasted (`tools/iiif_lines.py --image ...`); the numerals of
each cipher passage read by TWO passes (pass A: one Sonnet call per page on line crops; pass B: a second Sonnet call or your own eye read),
reconciled by eye (one unit) -> `dutch1653/ct_p351.tsv`, `ct_p339.tsv`, `ct_p308.tsv`, `ct_p435.tsv` (line, position, token).
Step 3 (known-answer gate, PREREG first): write `dutch1653/PREREG-DUTCHKEY.md` and push it in its own commit (check `git log origin/main -1 -- <file>`)
BEFORE decoding anything: the gate is that the printed key decodes p.351 (whose Dutch clear text is printed, edition pp.99-101 extracts / Van
Sypesteyn) to that Dutch text at >= 0.80 letter agreement on the aligned spans, against a shuffled-key control that CAN differ (permute the key's
letters over its codes, >= 200 draws, p95), with coverage (share of tokens < 67) reported; p.339 and p.308 scored by a Dutch letter 4-gram or
the judge if a Dutch corpus exists (say which; else the shuffled-key control on 4-gram-free statistics such as word-list hits from the p.99-101
Dutch extracts), as supporting folds. Then decode through a `--check` script (decode.json + `tools/decode_key.py`, or `dutch1653/decode_dutch.py`).
Step 4 (only on gate PASS): decode p.435 (Boreel) with the same key, codes > 100 left as name codes (M), shuffled-key control on p.435 itself
computed before reading the text, plus a matched control in the sense of rule 3 (a synthetic Dutch text of 128 tokens enciphered under this
key family with the same code-group share: does the scoring separate it from shuffles at this N? report both numbers). Grades per rule 4 (H for
key-stated values; M for misprints/unkeyed; counts). Then `prior_work.py ... --reading <file> --network` (G3) on any reading and paste it.
A reading beating its control with a clause above the authentication distance: one ROOM flag "DUTCH-KEY reading p.<n> for a first verifier".
On gate FAIL: log the row in HYPOTHESES.md, do not decode p.435, say what failed.
Units: key read ~0.8; 4 pages x 2 passes ~0.6 each = 4.8 (Sonnet passes are cheaper; your own eye read counts as a pass) + 4 reconciles folded in;
gate/decode/control ~1; Opus floor 1.5. If at 5.5 spent before p.435 is transcribed, stop and list it with its cost. NOTES "## DUTCH-KEY",
Remaining gaps / Escalation / Verdict, gaps_check.py. Report what was found and where it was not found; do not classify novelty.
