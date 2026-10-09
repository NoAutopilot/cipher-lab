# LANE FAMILY jobs (account 2, incarnation DEFAULT-account-2-20261009-2009, "FAMILY-A2l") -- 9 Oct 2026 20:3x UTC, lane orchestrator session_01W6XyGb1V3L3go1GwgTTvpA

Lane brief: .claude/briefs/lane-family.md (+ lane-common-blast.md). Cap 60, box 20:10 UTC 9 Oct - 06:10 UTC 10 Oct (80% 04:10). Twelfth
incarnation: started from STATUS.md "LANE FAMILY handoff (incarnation DEFAULT-account-2-20261009-1815)" next list items 1, 2, 4, plus the
next_steps --hot-only cheapest/parallel actions for na-suriname-map-1781, antt-msliv0638-brochado-1712 and antt-linhares-chave, and supply (c)
(KEY-OFFICES pools). Gate 0a: SESSION-SWEEP-account-2 stale-claimed since 5 Oct (prior incarnations proceeded). Exclusions as the 1815 jobs
file (eckert-*, Huntington ledgers, lodewijk/jan-van-nassau, decode-*, bne20211, costabili, harley-287, fr16144, fr16045-pisany, fr4735-monluc,
craven-rupert-1648, sforza-pusterla, baluze167, huntington-blathwayt, ceppo-nevers-fr3251-1570s, pro3055-clinton-1779, birago-*,
hellen-frederick-1752, ra-karlxi, Armstrong/Debosnys, Gallica fetches, any folder with a ROOM claim < 6 h and no done).
Intake gate 20:2x UTC (tools/intake_gate_check.py, exit 0 each): sachsstaatsarchiv-manteuffel-1712 partial, antt-msliv0638-brochado-1712
partial, antt-linhares-chave partial, na-suriname-map-1781 partial.
Checked stale before briefing (prior-work check 1, by the orchestrator): wallis-emus203 Thurloe vols 2-5 grep done 6 Oct; ormond-arran
Russell-Prendergast read done 6 Oct (R8-ORM); rah-juan-manuel CSP Spain II map done 8 Oct (D1A-RJM); rah-salazar HTRC EF still MongoError at
20:2x UTC (1 request) -- not briefed.

## Common rules for every job
Exactly the "Common rules for every job" section of `.claude/briefs/runs/2026-10-09-ytbiz-family-1310-jobs.md` (read it in full), with these
substitutions: address every ROOM line "for LANE FAMILY-A2l (account 2)"; hosts this wave: www.archiv.sachsen.de ("sachsen": MANT-CEN5 only,
sheet/thumbnail scale, <= 80 requests); service.archief.nl / www.nationaalarchief.nl ("NA": SUR-0745 only); no other external host unless
the job names it. No Gallica. Halfway line: one ROOM line at half the box or half the cap, whichever first (skip if done before).
Lessons carried: inventory size estimates over-read -- count tokens on the fetched image before planning vision calls (1510); a glossed leaf
is N0 by construction, a key test, not a reading (1815); push every PREREG in its own commit and check `git log origin/main -1 -- <PREREG>`
before scoring.

## Wave 1 (20:3x UTC 9 Oct)

### MANT-CEN5 (Sonnet, cap 2.5, box 75 min; sachsen take/release, sheet scale only): sachsstaatsarchiv-manteuffel-1712 unglossed-leaf census
Handoff 1815 next 1. The pool's glossed leaves are N0 by construction; only code runs with NO interlinear gloss AND NO following clear
rendering are unread material. Build `census_unglossed.tsv` (frame, loc 694/08|09, page/stamp, date if known, code-run count estimate,
gloss yes/no/partial, clear-rendering-follows yes/no, already-read-by (NOTES section), evidence crop path) from what is on disk FIRST:
frame_inventory.tsv, frame_classify*.tsv, inventory_r12dmant06.tsv, inv08*.tsv, the MANT-CENSUS / CEN2 / CEN3 / CEN4 sections, the f*_09
folders and mant0609/. Then extend to 694/09 frames and any 694/08 frames no census covered, at sheet/thumbnail scale from sachsen (fetch once,
manifest), one Sonnet look per contact sheet, a second look on any frame it calls unglossed. Also (handoff next 4) fix inv08g.tsv row 0503 to
"= 0502 (re-photograph), read". Output: the TSV, a NOTES section "## MANT-CEN5", and the top 3 unglossed candidates ranked by code-token count
with the leaf's date. No transcription, no decode. Units: ~6-10 sheet looks at ~0.2 each + 1 reconciliation. Report what was found and where it
was not found; do not classify novelty.

### MANT-GUT (Opus, cap 2, box 50 min, disk only): 0490 gutter run gate (a) with the leaf's own clear rendering as the gloss span
Handoff 1815 next 2 (V-MANT0490L's named next). Read AUDIT.md "AUDIT (V-MANT0490L)", the MANT-0490L section and f0490_08/. The 38-letter
gutter run is followed by its own clear rendering on the leaf: pre-register (PREREG-MANTGUT.md, own commit, pushed and checked BEFORE any
score) gate (a) exactly as MANT-0490L/MANT-0136B ran it (key.tsv decode of the blind-pass gutter digits vs the clear rendering read BLIND in
two passes from committed crops, real agreement vs key-shuffle p99, per-class breakdown, the control able to differ on the statistic). If a
crop the clear rendering needs is not committed, say so and stop (no fetch). A key test, not a reading: no grade above C from the rendering,
key.tsv rows unchanged unless the gate PASSes and then only M -> C for codes the rendering attests twice. `decode_key.py ... --check` after.

### BRO-DF (Opus, cap 3.5, box 80 min, disk only): antt-msliv0638-brochado-1712 appendix data faults
NEXT-STEPS parallel action (Remaining gaps bullet "Appendix data faults"): reconcile _anchors.json against ciphertext_appendix.tsv on Cartas 74
and 92 (89 vs 84 thin-code hits) against images/full_*_m0286 and m0289 (line crops via tools/iiif_lines.py --image, pasted); correct m0281 idx10
'z±' (code 7), the false 'e que' anchor at m0281 idx56, Carta 92's missing z on m0289, D4V-BROC's m0291 Carta 96 f.f -> ff; image-compare the
bare 9 at m0290 idx82 / m0292 idx29 and the 4 x/d/f occurrences on m0289-m0291 (two blind Sonnet looks per doubtful crop; undecidable stays
so). Re-run scripts 01-04 and `decode_key.py ... --check`; report every key tally that moved and whether letter 134's open codes moved (expected
not). Data hygiene, not a reading; the appendix's period plaintext is already known (N0). gaps_check.py after.

### LIN-TRIM (Opus, cap 2.5, box 60 min, disk only): antt-linhares-chave front-trim and join enumeration under a whole-string pt18 char model
The Verdict's cheapest next: re-score the front-trim and join enumeration (D22-LINTRIM's candidates) with a whole-string pt18 character model
with context across word boundaries (tools/data pt18 corpus; the word-unigram run D22-LINTRIM passed its control and changed nothing; DA1-LIN's
per-word letter 5-gram failed its gluing gate). Pre-register (PREREG-LINTRIM2.md, own commit before scoring): the model, the matched control
(the same enumeration on known-answer spans of this maço with planted trims/joins at the target's rate; gate on control recovery and check
the control can differ from the target on the statistic), and what a change in the top candidate means (M stays M unless the control passes
and the margin clears its p95). Do NOT touch the column-count sub-step (retired, rule 3). gaps_check.py after.

### SUR-0745 (Opus, cap 4, box 80 min; NA take/release): na-suriname-map-1781 inv. 373 scan 0745 right page, more glossed lines
SUR-KB / SUR-PARTIAL's named next: "more glossed lines (0745 right page, ~$3), not more draws". Read SUR-KB, SUR-PARTIAL, SUR-POOLPC and the
0744/0745 L sections first; prior-work checks 1-2 (is 0745 R already on disk or read?). Fetch 0745 once at native if not on disk (manifest),
count glossed cipher lines on the image before planning, crops pasted, two blind passes of cipher + one blind gloss read, reconciliation. Add
the lines to the pooled set ONLY under a PREREG amendment pushed before any re-score; then re-run the SPLIT statistic exactly as SUR-POOLPC
with the per-unit control for 0745 R first (rule 3 per-unit merge paragraph: a unit that ties its own control is held out of the pool). No key
change above M; to a verifier if anything moves. Report what was found and where it was not found; do not classify novelty.

### POOLS-A2l (Opus, cap 3, box 70 min; disk first, then <= 15 catalogue requests per host, one host at a time): supply (c)
List KEY-OFFICES.tsv rows in this lane's families (Dutch, German, Iberian, British/Irish, Scandinavian; not BnF-only, not Huntington ledgers,
not the excluded folders) whose office/key family has UNREAD cipher letters on the same host: e.g. Sociëteit van Suriname secret correspondence
(NA 1.05.03), De Witt / Van Beuningen circle (Huygens retroboeken, NA), Oxenstierna-Gustav Adolf (Riksarkivet / printed Skrifter), Trew
Posthius (Bavarikon), Willem van Hessen / Orange chancery (WVO), Puebla / Spanish 1495-1507 (Bergenroth, Simancas via PARES cache), Linhares
(digitarq). Disk first (each folder's NOTES siblings/pool sections, SIBLINGS-2026-10-08.tsv, QUEUE.md), then catalogue confirmation. Write
POOLS-2026-10-09-A2l.tsv (key_path, office, host, unread item ids, signs estimate, key-in-hand grade, prior-work check 1-3 result per item,
p_move, cost) and rank the top three for a check-solved worker in wave 2. No transcription, no new target folders, no scouting outside these
key families.

## Wave 2 (21:0x UTC 9 Oct)
Wave 1 results: MANT-CEN5 census (0181, 0491 the only unglossed, unattributed code leaves), MANT-GUT gate PASS (gutter C 24 M 14), BRO-DF
faults fixed, LIN-TRIM non-test (gluing gate FAIL, char scorers retired for trim/join), POOLS-A2l top 3 (Suriname governor letters; Van
Beuningen inv.1540; Juan Manuel -- parked on ASKS 138/L17, not briefed). Pricing lesson: every Opus job in wave 1 ran 1.5-1.7x its cap; an
Opus worker spends ~$2 reading a large folder before work. Caps below are set accordingly; stop at the cap all the same.
Hosts this wave: sachsen (MANT-0181 first, then MANT-0491 after its "sachsen release"); NA (SUR-GOV, then VB-1540 after its "NA release";
VB-1540 works from disk and the huygens host meanwhile); IA ("IA": LIN-BFSP only).

### MANT-0181 (Opus, cap 6, box 100 min, sachsen take FIRST): sachsstaatsarchiv-manteuffel-1712 694/08 frame 0181 (+0182 if continuation)
MANT-CEN5 top unattributed unglossed leaf: stamp 138, Dresden 6 Juillet 1712, Flemming to Manteuffel, right page, 7 inline runs ~35 tokens,
no gloss, no clear rendering after; 0182's unglossed runs may continue it. Prior-work step in full BEFORE any transcription: check 4 = Acta
Borussica BO I and Droysen IV.1 by date (+-3 days) and both correspondents, Flemming's printed correspondence, Krauske; check 2 = 0180-0184
on disk/sheets for a clear copy or gloss. Fetch 0181/0182 once at native (manifest), COUNT tokens on the image before planning. Crops
pasted, two blind Sonnet code passes, reconciliation. PREREG-MANT0181.md (own commit, checked on origin) BEFORE decoding: decode under
key.tsv; gate = fr18 judge on the decode vs (i) key-shuffled decodes p95 and (ii) the SHUFFLED-TARGET decode (CLAUDE.md rule 3: a judge that
passes the shuffled-target decode is void as a gate at this N -- then say "judge cannot decide" and grade by key alone). Grades per token
(rule 4): H only where key.tsv is H; S needs the gate; else M. Print-check the decoded phrases (G3) before any "not located" sentence. Report
what was found and where it was not found; do not classify novelty. If it beats its control, the orchestrator sends it to a first verifier.

### MANT-0491 (Opus, cap 5, box 90 min, sachsen after MANT-0181's "sachsen release"; prior-work from disk meanwhile): 694/08 frame 0491
MANT-CEN5: stamp 393, Berl. 14 Nov 1712; runs 103.34.26.27 x3, 34.22.60.53.39.27, 60.16.54.53.11, 36.31 plus 155 187 257, ~35 tokens, two
small words above (pouvoir, Flem.) = partial gloss, no clear rendering after. Same procedure as MANT-0181 (prior-work 1-4 first: BO I by date,
the 0490/0494 neighbours already read -- does 0491 continue 0490's mid-Nov dispatch?). The two glossed words are a tiny known answer: score
them blind, report them, but they do not make a gate (N < 5, say so). PREREG-MANT0491.md before decoding; same judge + shuffled-target rule.

### SUR-GOV (Sonnet, cap 3, box 75 min, NA take/release, <= 150 requests, >= 1.5 s): na-suriname-map-1781 governor letters image screen
POOLS-A2l rank 1. NA 1.05.03 governor's incoming letters: screen the unlooked inv. 370, 371, 372 (1780) and 378, 379, 380 (1783-84) for
cipher passages at thumbnail scale (IIIF 300-400 px), 1-in-10 sample per inventory first, then every scan within +-5 of any hit; then inv.
266-270 (1739-42, the Nieuw alphabet's issue years) 1-in-15 if requests remain. Seed every contact sheet with one known cipher scan from inv.
373 (0744 or 0745) as a positive control and one plain scan as a negative; a sheet whose control is missed is a non-test, re-look it. Output
sources/na-1.05.03/2026-10-09/screen_gov.tsv (inv, scan, cipher yes/no/possible, glossed yes/no, date if legible) and a NOTES section
"## SUR-GOV". No transcription. Report counts per inventory and requests per host.

### VB-1540 (Sonnet, cap 2.5, box 70 min; NA after SUR-GOV's "NA release" (<= 30 requests); huygens host for the edition, <= 30 requests):
vanbeuningen-dewitt-1657 inv.1540 per-letter edition match
POOLS-A2l rank 2. Read VB-SCREEN2 and edition_check_1539_1541.tsv first. For each cipher-bearing scan of NA 3.01.17 inv.1540 (1658, 141
scans; a 1-in-7 sample saw groups at 0036): find the letter it belongs to (date line, endorsement) and match it against Brieven aan Johan de
Witt I (Huygens retroboeken full-text by date/opening words). Output edition_check_1540.tsv (scan, letter date, endorsement, cipher yes/no,
printed yes/no with page, printed in clear over the cipher span yes/no/unknown). Letters printed in clear are N0 (key tests at most); list
only the unprinted cipher-bearing letters as candidates. No transcription, no decode.

### LIN-BFSP (Sonnet, cap 2.5, box 60 min, IA take/release, be-api >= 1.5 s, <= 80 requests): antt-linhares-chave print step
The Verdict's cheapest next: be-api full-text sweep of the 33 unchecked British and Foreign State Papers volumes (read NOTES line ~976 and
the print rung for which volumes are checked and which phrases/names to use; run a positive control per query family on a volume known to
carry the term). Log every volume searched with hit/no-hit; any hit -> the surrounding sentence quoted, nothing more. A search result for the
log, never a novelty verdict. gaps_check.py after.

## Wave 3 (21:5x UTC 9 Oct)
Wave 2: MANT-0181 and MANT-0491 both "judge cannot decide / FAIL" at 37-51 tokens (all M, key unchanged) -- unglossed Manteuffel leaves under
~60 tokens are not worth further Opus reads; VB-1540 no unprinted cipher letter in 5 read; LIN-BFSP 31/32 zero. SUR-GOV found the one live
lead: NA 1.05.03 inv. 372 scans 0184-0194+, an 11+-scan enciphered letter (Jul-Oct 1780, Latin letters + digits, clear paragraph heads), unread.
Lane spend at this point ~42 of 60 (workers 38.4 + orchestrator ~4).

### SUR-372 (Opus, cap 7, box 110 min; NA take/release, <= 40 requests, >= 1.9 s): na-suriname-map-1781 inv. 372 enciphered letter, premise + first test
Read NOTES "## SUR-GOV" (its "next steps" list), the key files (key_period.tsv Oud, key_period_nieuw.tsv + key_period_codes_nieuw.tsv Nieuw,
inv. 86 key sheet) and how 373_0693 and the 2077/2039 legends were decoded. In order, stopping where a step says stop:
(1) Close the run: fetch 0183 and 0195 (and further out until clear text on both sides, <= 8 scans), at 600 px; then 0189 and the first and
last cipher scans at >= 1500 px (manifest entries; commit only the crops later steps need, folder under 30 MB).
(2) Prior-work step in full (checks 1-4), pasted before any transcription: own work; the leaf and neighbours -- is there an interlinear gloss
at 1500 px, a decipherment slip, or a clear copy/"vertaling" anywhere in inv. 372 after the run, or in the Sociëteit's outgoing letter-books
(1.05.03 inv. for 1780 minutes) -- check the EAD on disk (sources/na-1.05.03/2026-10-09/) for the 1780 outgoing/register items and look at
most 10 scans of the obvious one; holder EAD note; editions/scholarship (de Leeuw 1997 TvZ 16 -- what does it cover? Google Books
country=US, OpenAlex keyed). A gloss or clear copy makes it N0: then it is a key test, say so and score it as one.
(3) If not stopped: crop one page (the best-legible, ~20 lines; `tools/iiif_lines.py --image ... --out ... --debug` pasted), two blind
Sonnet passes + one reconciliation, ciphertext tsv. Write PREREG-SUR372.md (own commit, checked on origin) BEFORE decoding: decode under
each of the two period keys (Oud / Nieuw); gate = Dutch judge (tools/judge_plaintext.py, an 18th-c. Dutch corpus if tools/data has one --
say which and whether era-matched) on each decode vs key-shuffled decodes p95 AND the shuffled-target decode (rule 3: a judge PASS on the
shuffled-target decode voids it), plus a word-hit count against a Dutch lexicon vs the same nulls. A key whose decode does not beat its nulls
is a negative for that key on this page only (state the transcription agreement rate beside it).
(4) Grades per token (rule 4): H only where the period key is H and the gate passed; else M. G3 print-check on decoded phrases if anything reads.
Write NOTES "## SUR-372", update Remaining gaps/Escalation, gaps_check.py. Report what was found and where it was not found; do not classify
novelty. If a key reads, the orchestrator sends it to a separate first verifier.
