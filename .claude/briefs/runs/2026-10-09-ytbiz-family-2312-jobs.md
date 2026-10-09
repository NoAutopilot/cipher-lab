# LANE FAMILY jobs (account 2, incarnation DEFAULT-account-2-20261009-2312, "FAMILY-A2m") -- 9 Oct 2026 23:3x UTC, lane orchestrator session_01WCSXR7Z6hu4DFE38HAkdCJ

Lane brief: .claude/briefs/lane-family.md (+ lane-common-blast.md). Cap 60, box 23:13 UTC 9 Oct - 09:13 UTC 10 Oct (80% 07:13). Started from
STATUS.md "LANE FAMILY handoff (incarnation DEFAULT-account-2-20261009-2009)" next list items 1, 2, 3, 4 (code 207 part), 5, plus the es132
Verdict's cheapest next (disk). Gate 0a: SESSION-SWEEP-account-2 stale-claimed since 5 Oct (prior incarnations proceeded). Exclusions as the
2009 jobs file (eckert-*, Huntington ledgers, lodewijk/jan-van-nassau, decode-*, bne20211, costabili, harley-287, fr16144, fr16045-pisany,
fr4735-monluc, craven-rupert-1648, sforza-pusterla, baluze167, huntington-blathwayt, ceppo-nevers-fr3251-1570s, pro3055-clinton-1779, birago-*,
hellen-frederick-1752, ra-karlxi, Armstrong/Debosnys, Gallica fetches, any folder with a ROOM claim < 6 h and no done).
Intake gate 23:2x UTC (tools/intake_gate_check.py, exit 0 each): na-suriname-map-1781 partial, vanbeuningen-dewitt-1657 found-solved (siblings
only), antt-msliv0638-brochado-1712 partial, sachsstaatsarchiv-manteuffel-1712 partial, antt-linhares-chave (terminal line, print step only),
es132-vargas-mexia-1578 (run by the worker before any step).
Checked before briefing: rah-salazar HTRC EF still MongoError at 23:2x UTC (1 request) -- not briefed.

## Common rules for every job
Exactly the "Common rules for every job" section of `.claude/briefs/runs/2026-10-09-ytbiz-family-1310-jobs.md` (read it in full), with these
substitutions: address every ROOM line "for LANE FAMILY-A2m (account 2)"; hosts this wave: service.archief.nl / www.nationaalarchief.nl
("NA": SUR-266 first, then VB-EYE after SUR-266's "NA release"); archive.org ("IA": LIN-BFSP2 only); resources.huygens.knaw.nl ("huygens":
VB-EYE only); no other external host unless the job names it. No Gallica. Halfway line: one ROOM line at half the box or half the cap,
whichever first (skip if done before).
Lessons carried: count tokens on the fetched image before planning vision calls; a glossed leaf is N0 by construction, a key test, not a
reading; push every PREREG in its own commit and check `git log origin/main -1 -- <PREREG>` before scoring; every Opus job in these folders
ran 1.4-1.7x its cap last incarnation (an Opus worker spends ~$2 reading a large folder before work) -- read only the sections named.

## Wave 1 (23:3x UTC 9 Oct)

### SUR-266 (Sonnet, cap 3, box 75 min, NA take/release, <= 150 requests, >= 1.9 s): na-suriname-map-1781 governor letters 1739-42 screen
Handoff 2009 next 1. Read NOTES "## SUR-GOV" and "## SUR-372" (method, controls, what counts as a hit) and sources/na-1.05.03/2026-10-09/
(EAD on disk, screen_gov.tsv). Screen NA 1.05.03 inv. 266, 267, 268, 269, 270 (1739-42, the Nieuw alphabet's issue years) for cipher
passages at thumbnail scale (IIIF 300-400 px), 1-in-15 per inventory, then every scan within +-5 of any hit, exactly as SUR-GOV did (seed
each contact sheet with one known cipher scan from inv. 373 and one plain scan; a sheet whose control is missed is a non-test, re-look it).
For every hit record glossed yes/no at >= 1200 px on ONE scan of the run (an interlinear gloss makes it N0, a key test only). Append to
screen_gov.tsv (or a sibling screen_gov_266.tsv), NOTES "## SUR-266" with counts per inventory and the unglossed cipher runs (inv, scans,
date if legible) as the only unread candidates. No transcription. If requests remain (<= 150 total) and time < 60% of box, continue to inv.
370, 371, 378-380 at every 10th scan not already looked at (screen_gov.tsv lists which were). Post "NA release" when done.

### BRO-CT (Opus, cap 4, box 70 min, disk only): antt-msliv0638-brochado-1712 crossed-t glyph compare and --try on letter 134
NEXT-STEPS parallel action + handoff 2009 next 3. Read NOTES "## BRO-DF" (the crossed-t lead, ~line 2641) and the Remaining gaps/Escalation
tail only. (1) Glyph compare: cut crops (tools/iiif_lines.py --image, pasted) of the three appendix 't' signs (Carta 74 and the two others BRO-DF
names) and letter 134's unkeyed 't' at m0276-r2 pos 16, plus 4 decoys (appendix l and t-like signs of other values); two blind Sonnet looks
"which of these are the same sign as X?" with decoys shuffled; the match is supported only if both looks pair the target with the crossed-t
set and not with a decoy. (2) Whatever (1) says, run `python3 tools/decode_key.py ciphers/antt-msliv0638-brochado-1712 --try t=l` (and the
runner-up value if the tool's avalanche lists one) at every occurrence in letter 134 and report each context. An accepted value is M unless
--try's own control passed for that value class (CLAUDE.md MQS-CROSSWORD line); never edit key.tsv in this job; write the result as a
NOTES section "## BRO-CT" and a HYPOTHESES.md row. Letter 134 as a whole still waits on ASKS 108. gaps_check.py after.

### MANT-207 (Opus, cap 3, box 60 min, disk only): sachsstaatsarchiv-manteuffel-1712 code 207 second witness + G01 third blind reads
Handoff 2009 next 4 (MANT-GUT's named next, NOTES ~lines 4024, 4100, 4165). (a) Code 207 'le Gr Tres.' is held on one witness: grep every
committed decode/transcription TSV in the folder for 207 (all leaves, glossed and unglossed); for each occurrence on a GLOSSED leaf, read the
gloss over it BLIND from committed crops (two Sonnet passes, gloss not shown to the reader beforehand); a second witness that reads the same
referent moves 207 M -> C only if the occurrence is on a different letter; list every occurrence with its context either way. If no crop is
committed for an occurrence, say so (no fetch). (b) A blind third read of G01 r2 pos4 (28 vs 29) and r1 pos13/14 (54 37 vs 59 39) from the
committed crops, then the G01 28/29 transcription fix with the folder's --check scripts and both gates re-run as MANT-GUT ran them (report any
number that moves). NOTES "## MANT-207", key.tsv only for a 207 C move, `decode_key.py ... --check` after. Do not start codes 199/321.

### LIN-BFSP2 (Sonnet, cap 2.5, box 60 min, IA take/release, be-api >= 1.5 s, <= 90 requests): antt-linhares-chave print step remainder
Handoff 2009 next 5. Read NOTES "## LIN-BFSP" (~line 1700-1722): the same 32-34 British and Foreign State Papers items, now the "Strangford"
and "Sousa Coutinho" families (plus the OCR variants "Linhàres", "Coutinho" alone if the control allows), each with its own positive control
on a volume known to carry the term (LIN-BFSP's first OR query FAILED its control -- run one term per query). Then the metadata fetch that
maps each item to its volume/years (LIN-BFSP's "Next"). Log every item x family searched with hit/no-hit in a TSV beside LIN-BFSP's; any hit
-> the surrounding sentence quoted and whether it concerns 1808-1812 Linhares/Strangford correspondence, nothing more. A search result for
the log, never a novelty verdict. NOTES "## LIN-BFSP2", gaps_check.py after.

### VB-EYE (Sonnet, cap 2, box 70 min; huygens first, NA ONLY after SUR-266's "NA release", <= 15 NA requests): vanbeuningen-dewitt-1657 inv.1540
Handoff 2009 next 2. Read NOTES "## VB-1540" and edition_check_1540.tsv. Eye-check NA 3.01.17 inv.1540 scans 0120 (19 Jul 1658) and 0134
(6 Aug 1658) -- the two letters with no edition date match: fetch each at ~1500 px (plus the facing/next scan if the letter continues), say
whether it carries cipher, whether a gloss or decipherment is on the leaf, and match it against Brieven aan Johan de Witt I and the De Witt
Brieven volumes (Huygens retroboeken full-text by date +-3 days and opening words; positive control: a letter VB-1540 already matched). Add rows
to edition_check_1540.tsv; NOTES "## VB-EYE". Letters printed in clear are N0. No transcription. If NA is still held at 60% of the box, do the
edition side only and say so.

### ES132-R7 (Opus, cap 4, box 80 min, disk only): es132-vargas-mexia-1578 test2 loader fix + owed rule-7 re-derivation
The Verdict's cheapest next (NOTES line ~102). Run tools/intake_gate_check.py es132-vargas-mexia-1578 and paste it first. (a) Fix the test2
loader for multi-word {CLEAR:...} tokens and re-score f.50r/f.52r exactly as the previous runs (report old and new numbers side by side; a fix
that moves a gate result goes in HYPOTHESES.md). (b) Repair settle_dup.py --check (ES132-SLIC, 8 Oct 2026 names the fault) so it exits 0 on
the committed state, then the rule-7 re-derivation owed after A3V3-ES132S: regenerate the settled f.89 reading from the transcription and the
key with the folder's decode script and --check; a difference above the M-graded tokens goes back to the reading (report it, do not paper
over it). Do not start the 40-candidate two-crop look. If a reading changes, carry it into AUDIT.md per rule 10's propagation paragraph and
any SECOND-OPINIONS-QUEUE.tsv row for this target. NOTES "## ES132-R7", gaps_check.py after.

## Wave 2 (23:5x UTC 9 Oct)
Wave 1 results (all done by 23:52, 11.76 by get_session): ES132-R7 both steps already on file (orchestrator briefed from a stale Verdict line --
lesson: grep the dated sections before briefing); BRO-CT match NOT SUPPORTED, t=l rejected, key unchanged; SUR-266 inv. 266-270 0 cipher in 120
scans; VB-EYE 0120/0134 plain prose, no unread candidate; MANT-207 no second witness on disk (0151 crop never committed), 0490 G01 fix applied,
gates unchanged; LIN-BFSP2 Strangford/Couttinho no 1808-12 hit, 13 cells unsearched (be-api 502s). Hosts this wave: sachsen (MANT-0151 only,
<= 6 GETs); NA (SUR-DENSE only); IA (LIN-BFSP3 only). Every job: prior-work check 1 on its own step FIRST -- if the step is already on file,
one ROOM line and stop.

### MANT-0151 (Opus, cap 3, box 60 min, sachsen take/release, <= 6 GETs): sachsstaatsarchiv-manteuffel-1712 694/08 frame 0151, code 207 witness
MANT-207's named next (NOTES ~lines 4300-4334). GAPS207's eye note (4 Oct) read 'le Gr. Chancelier 207' among glossed names on 0151; key.tsv holds
207 = 'le Gr Tres.' on one witness, so 0151 is either a second witness or a conflict. Fetch 0151 once at the archive's served size (manifest), cut
the line crop(s) carrying 207 with tools/iiif_lines.py --image (pasted), commit them, two blind Sonnet gloss passes over the 207 group (reader not
told the candidate values; decoys: two other glossed name codes on the same leaf). Report the blind reads verbatim. Same referent on a different
letter -> 207 M -> C in key.tsv with both witnesses cited; a different referent -> CLAUDE.md rule 4's conflict paragraph (record sender,
recipient, date, direction of each witness, log it in HYPOTHESES.md, grade 207 M where the witness does not match), never settled by majority.
decode_key.py --check after; NOTES "## MANT-0151"; gaps_check.py.

### SUR-DENSE (Sonnet, cap 3, box 75 min, NA take/release, <= 150 requests, >= 1.9 s): na-suriname-map-1781 inv. 370, 371, 378-380 denser screen
Handoff 2009 next 1, second half (SUR-266 did not reach it). Read NOTES "## SUR-GOV" and "## SUR-266"; screen_gov.tsv lists the scans already
looked at. Every 10th scan not yet looked at in inv. 370, 371, 378, 379, 380 at 400 px, same contact-sheet controls (one inv. 373 cipher scan +
one plain scan per sheet; a missed control = re-look), then +-5 around any hit, and glossed yes/no at >= 1200 px on one scan of any run (gloss =
N0, key test only). Append to screen_gov.tsv (or screen_gov_dense.tsv); NOTES "## SUR-DENSE" with counts per inventory and any UNGLOSSED cipher
run as the only unread candidate. No transcription.

### LIN-BFSP3 (Sonnet, cap 1.2, box 40 min, IA take/release, be-api >= 2 s, <= 40 requests): antt-linhares-chave BFSP remainder
LIN-BFSP2's "Next" (NOTES ~line 1738): retry the 13 unsearched item x family cells listed in its TSV (one retry each after a pause on a 502;
a second 502 = unsearched, logged), then the one advancedsearch metadata fetch that maps the items to volume/years. Same per-family controls as
LIN-BFSP2. Append to its TSV; NOTES "## LIN-BFSP3". A search result for the log, never a novelty verdict. gaps_check.py.

### ES132-40 (Opus, cap 4, box 70 min, disk only): es132-vargas-mexia-1578 two-crop look at the unsettled f.89 candidates
The Verdict's cheapest next (line 102, as corrected by ES132-R7). Prior-work check 1 first: grep the dated sections after A3V3-ES132S
(ES132-RD, ES132-SLIC, ES132-LOOK, ES132-AUDIT, ES132-R7) for any look already run on these candidates; if run, one ROOM line and stop. Else:
identify the unsettled '?' candidates A3V3-ES132S left (count them; the Verdict says 40), cut two crops each (letter body + duplicate f.93-95
counterpart) from images on disk (tools/iiif_lines.py --image, pasted), one blind Sonnet look per pair with decoys planted at a known rate
(ES132-AUDIT's planted-tile method; the control must reach its 0.80 catch gate or the look is a non-test and nothing is applied). Apply only
settlements the control licenses; re-run the folder's decode/--check and report every token that moved (M stays M unless the gate licenses).
NOTES "## ES132-40"; gaps_check.py. If a reading changes, carry it into AUDIT.md per rule 10's propagation paragraph.
