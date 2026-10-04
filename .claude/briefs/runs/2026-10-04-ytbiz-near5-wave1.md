# LANE-NEAR5 wave 1 (4 Oct 2026, written 06:2x UTC by LANE-NEAR5, account 2 / ytbiz, session_012hS4hPgLzzQfHLW7vuq5KC)

Common rules: the "Common to every job below" section of `.claude/briefs/runs/2026-10-04-ytbiz-near4-wave1.md`, with
"LANE-NEAR4" read as "LANE-NEAR5" everywhere (claims, done line addressed "for LANE-NEAR5 (account 2)").

## N5-VIVK -- fr16104-vivonne-spain-1572: known-plaintext test of the 4 June 1573 cipher letter against its clerk decipherment (Opus; cap USD 30; box 170 min)
Facts (NOTES.md N4-VIV2/N4-VIV3; read those two sections first). fr.16105 = ark btv1b9009663p; canvas c shows f.(c-4)v left and
f.(c-3)r right (`tools/gallica_folio.py` fit, residual 0). Cipher letter ink 40: cipher block f.100 (lower) - f.103r. Its clerk
decipherment ink 41 ("dechiffre de la precedente"): ff.104r-108v; f.104r illegible, ff.104v-108v legible plain French; it ends on
f.108v "... de ses necessitez". Tomokiyo (sources/cryptiana/web/henryiii.htm, "Vivonne in Spain") publishes the key used April
1572-Nov 1574 as images henryiii_Vivonne1.png ... Vivonne6.png (+ VivonneSig.png) at cryptiana.web.fc2.com, not on disk.
Intake gate: `python3 tools/intake_gate_check.py fr16104-vivonne-spain-1572` rc=0 (06:1x UTC, pasted by LANE-NEAR5).

Units (CLAUDE.md Usage 6, ~USD 1.5 per Sonnet one-page call): cipher f.102r, f.102v, f.103r (canvas 105 right, 106 left, 106 right)
x (2 blind passes + 1 reconciliation) = 9 units; decipherment pages that carry the plaintext of those three cipher pages -- by
proportion about ff.106v-108v (canvas 110 left - 112 left, 5 pages; confirm the start by finding the plaintext of f.102r's first
cipher words, widen by at most one page) x 2 blind passes, reconcile in the worker's own read = 10-12 units; Tomokiyo key images to
key data 2 units. ~22 units, ~USD 33 ceiling; stop before a unit that would cross 80% of the cap or box.

Steps.
1. Key on disk: fetch henryiii_Vivonne1..6.png and VivonneSig.png once (1.5 s apart, descriptive UA) into sources/cryptiana/web/
   (unmodified snapshots); turn the alphabet/nomenclator into `ciphers/fr16104-vivonne-spain-1572/key_tomokiyo.tsv` (code,
   meaning, source image, note). This is a `published` key (Tomokiyo), credited in NOTES.md. It is also the transcription
   reference sheet: give the subagents the sign inventory from it.
2. Crops: `tools/iiif_lines.py --ark btv1b9009663p --canvas N --region ... --out ciphers/fr16104-vivonne-spain-1572/images --debug`
   per page, command and output pasted in NOTES before the first subagent call; check the debug overlay. Subagents get crop paths only.
3. Cipher transcription: two blind Sonnet passes per page, `tools/reconcile_passes.py`, reconciliation by you from the crops; report
   err_2reader per page (TRANSCRIPTION.md row 2). Decipherment: two blind passes per page, merged by you; record abbreviations as
   written and keep a normalized version (lowercase, letters only, u/v and i/j folded, abbreviations expanded) -- rule 3's
   PX-BRODEC lesson: compare normalized to normalized only.
4. PREREG (push `ciphers/fr16104-vivonne-spain-1572/PREREG-N5VIVK.md` BEFORE any decode of f.103r is compared with any plaintext):
   held-out page = cipher f.103r and the plaintext span after the training span's end. Statistic: letter agreement of the decoded
   held-out page against that plaintext span after a fixed alignment (name the tool and its settings, e.g. tools/stream_align.py or
   `interlinear_align.py stream` band/step), normalized as step 3.
   Arm A (C, independent): `tools/interlinear_align.py stream` on f.102r+f.102v vs their plaintext from a FLAT start (no --prior),
   key frozen, decode f.103r with it (codes unseen in training = unread).
   Arm B (published key): decode f.103r with key_tomokiyo.tsv, no training.
   Nulls for each arm, 200 draws each: (i) shuffled key (meanings permuted across the arm's codes), (ii) shuffled order (f.103r token
   order permuted, same key). Both can move the statistic. Pass for an arm: real > the 95th percentile of BOTH nulls, and you state
   in the PREREG the expected ceiling check (a null whose median is >= 0.95 voids the arm). Report both arms side by side, plus the
   per-code agreement of Arm A's frozen key with key_tomokiyo.tsv on codes with >= 3 training occurrences.
5. If at least one arm passes: write key.tsv for this target (Tomokiyo values, with C counts from Arm A where they agree; disagreements
   listed, never settled by majority -- rule 4), and STOP there (applying it to fr.16104 ff.157-159v is wave 2, not yours). If both
   fail: log the numbers in HYPOTHESES.md as a known-plaintext test, name the next step, stop.
NOTES "N5-VIVK" section, Remaining gaps / Escalation refresh, gaps_check OK line. Report what was found and where it was not found;
do not classify novelty. Gallica requests one at a time, >= 2 s apart; count requests per host.

## N5-VIV5S -- fr16104-vivonne-spain-1572 wave 2: the 5 Sept 1572 cipher block (fr.16104 ff.157-159v) read with key.tsv (Opus; cap USD 22; box 150 min)
Written 06:5x UTC after N5-VIVK (ROOM 06:47, dea9b614): Tomokiyo's 1572-74 key PASSed the pre-registered held-out test against the clerk
decipherment (Arm B 0.545 vs nulls p95 0.340/0.362); key.tsv = Tomokiyo values, 26 C / 4 M (S, y, b, A listed, not settled). Read NOTES
"N4-VIV" and "N5-VIVK" first, and reuse N5-VIVK's tx/SIGNS.md labels, crop settings and scripts (no private copies of shared tools).
Material: fr.16104 = ark btv1b9009609w; the letter (Gachard L, 5 Sept 1572, "en partie chiffree, sans le dechiffrement") runs f.157r-159v,
canvases 170 (right page f.157r) - 173 (left page f.159v); plain French first, then cipher (N4-VIV: about 150-175 cipher lines, est.).
Units: cipher pages x (2 blind Sonnet passes + 1 reconciliation) at ~USD 1.5 per call -- count the cipher pages from the 1600 px openings
first and state units x rate in NOTES before the first subagent call; stop before a unit that would cross 80% of cap or box.
0. Premise (cheap, before transcription): the same volume can file a decipherment out of place (Tomokiyo, Mousset p.xlviii). Look at
   canvases 174-180 and any "dechiffre de la precedente" leaf dated Sept 1572 within c.150-200 at 1200 px (<= 8 requests) and say whether a
   clerk decipherment of this letter exists. If one exists, stop after recording it (the letter is then not unread; the test becomes a
   known-plaintext check like N5-VIVK and is a separate brief).
1. Crops (tools/iiif_lines.py, command + output pasted), two blind passes per page, reconcile_passes.py, reconciliation from crops,
   err_2reader per page.
2. PREREG-N5VIV5S.md pushed before decoding: decode with key.tsv (tools/decode_key.py via decode.json, or N5-VIVK's decode script extended
   -- reproducible, rule 7 --check); judge `tools/judge_plaintext.py` with an fr16 spec (check corpus era per rule 3; state it) on the
   decode vs (i) the same transcription under 200 shuffled keys (key.tsv values permuted across codes) and (ii) the N5-VIVK held-out f.103r
   decode as a positive control of the same hand and key; pass rule stated before running.
3. Grade per token (rule 4): key source `published` (Tomokiyo), values checked against known plaintext in N5-VIVK; say which grade you use
   for C-supported values on unread text and why; M for the 4 M codes and for tokens on lines with reader splits left unsettled. Give counts.
4. `tools/print_check.py` on 5-10 distinctive decoded phrases (Gachard II's entry L summary and quotes are the obvious overlap: report which
   decoded passages Gachard summarises or quotes). Report what was found and where it was not found; do not classify novelty.
5. NOTES "N5-VIV5S", reading file + script, Remaining gaps / Escalation refresh, gaps_check OK line; status.json untouched (orchestrator).
   ROOM done line for LANE-NEAR5 with the judge numbers beside the controls; if the judge passes, add "fr16104-vivonne-spain-1572 ready for
   audit 1" in the same line.

## N5-VIVTAB -- fr16104-vivonne-spain-1572: per-letter table of fr.16104/16105, which cipher pieces lack a clerk decipherment (Opus; cap USD 5; box 60 min)
Written 07:4x UTC after N5-VIV5S (ROOM 07:02, 95bf17e0): Gachard's "sans le dechiffrement" flag was wrong for both letters it named; the
5 Sept 1572 letter's decipherment is ff.162r-163r. The pool's value now rests on whether ANY cipher piece in fr.16104/16105 lacks a clerk leaf.
1. f.164 letter to the Queen, 5 Sept 1572 (old piece 52, full cipher): Gachard II entry (IA labibliothquen02gachuoft djvu, already used) and
   the leaves after it (canvases ~178-186) for a "dechiffre de la precedente".
2. One 1200 px pass over every canvas of fr.16104 (btv1b9009609w, 324) and fr.16105 (btv1b9009663p, 249) not already described in NOTES,
   by contact sheets (several openings per image read, as N4-VIV3 did; no subagent transcription), building `piece_table.tsv`: canvas,
   folio, old ink piece no., docket date, addressee, cipher (none/partial/full), "dechiffre" leaf (canvas or none), note. Requests one at
   a time >= 2 s, <= 300 Gallica requests total; if the per-sheet vision budget would cross 80% of cap, stop and table what is done.
3. Result: the list of cipher pieces with no decipherment leaf (with estimated cipher lines), each a candidate for a later read with key.tsv.
   NOTES "N5-VIVTAB", Remaining gaps / Escalation refresh, gaps_check OK line. Report what was found and where it was not found.

## N5-HEL7 -- hellen-frederick-1752: key-rebuild of codes 1-800 by context, control first (Opus; cap USD 10; box 90 min)
Read NOTES "N4-HEL6" (Part B statistic, its held-out R4369 positive control, the out-of-vocabulary note) and the LANE-NEAR5 gaps refresh.
R4370 and R4372 are retired for 1-800 (rule 3); this is a different instrument (cryptanalytic, grade S at best). Disk only.
1. PREREG-HEL7.md pushed before any target run: objective = N4-HEL6 Part B junction PMI (fix the OOV scoring at the unseen floor first, as
   N4-HEL6's tool note says, with an offline test), assignment space = a value per code 1-800 drawn from a candidate vocabulary you fix in
   the PREREG (e.g. fr18 + Fagel 5177 clear pages' top-N words/syllables), anneal settings, seeds.
2. CONTROL FIRST (rule 3 + CLAUDE.md "subsample the positive control"): blank R4369's own 801+ values on a code set matched to the target
   (same token count, same distinct-code count and occurrence profile as the 1-800 codes in R1953), rebuild them with the same anneal, and
   score recovery (exact value) against R4369. Gate stated in the PREREG (e.g. recovery >= 3x the shuffled-assignment baseline AND >= 0.20).
   If the control misses its gate: stop, log "untestable by this instrument at this N" in HYPOTHESES.md, no target run.
3. Only if the control passes: run on codes 1-800, report values that recur stably across seeds as S candidates (never H), per-code with
   occurrence counts; refresh the reading only for tokens whose value is stable across all seeds and fit their context in both directions.
NOTES "N5-HEL7", HYPOTHESES.md row (target and control side by side), NEAR.md row Evidence/Last-touched, near_check, gaps_check OK line.
