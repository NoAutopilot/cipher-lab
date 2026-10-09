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
