# PREREG TX-ENGINEER-2 S2: the single confirm2 look (lane, DRAFT 9 Oct 2026 17:1x UTC by date -u; FROZEN only by a dated line below, added after round 3's dev results and before any read of the item)

Guard S2 (lane brief; PREREG-txeng2-0 "What success means"): the frozen pipeline scores ONCE on `vivonne1573-f103r-confirm2`
(BENCHMARK-TX.tsv row by TX-CONFIRM-SET-2, account 1, 15:56 UTC: BnF fr.16105 f.103r, Saint-Gouard to Charles IX, Madrid June
1573, Saint-Gouard 1572-74 key, 37 lines, 1,068 scored; truth = the clerk's period decipherment on ff.104-108 through
Tomokiyo's published key, C; committed + passA + passB outputs on file from the builder). The lane and its workers have not
opened the item's truth, outputs or crops and do not until the S2 worker's score step.

## The frozen pipeline (today's; filled in at freeze)
1. Crops: `tools/iiif_lines.py --image <leaf> ... --band-extent 0.1 --mask-neighbours --follow-slope 400 --overlap-note --debug`
   (the folder's own c106_f103r crops were cut with follow-slope by N5-VIVK; re-cut from the same source only if the overlay
   shows a cut sign; pasted command either way). One subagent call per <= 8 lines.
2. Two blind Opus 5.5 passes with the folder's own value-blind sign sheet/brief (ciphers/fr16104-vivonne-spain-1572; the
   reader vocabulary = the committed transcription's label inventory, so no --label-map; if the folder's brief is not
   value-blind, the worker writes a value-blind one from its sign list and says so), committed as they land.
3. `tools/reconcile_passes.py` + ONE Sonnet adjudication of disagreements + uncertain from the crops (the folder protocol;
   TXE-Q's adjud_task.txt as the worked example); no relabel map exists for this family.
4. The doubt feed (tx_doubt latt+vote4+selfcons where inputs exist, else disagree+latt) listed beside the read, never resolved.
5. + any round-3 instrument that passed its dev gate AND its one eval look at p < 0.01 (none as of this draft).

## The single score
`python3 tools/tx_bench.py benchmark-tx/outputs/vivonne1573-f103r-confirm2/passZ_pipeline.tsv --bench BENCHMARK-TX.tsv --item
vivonne1573-f103r-confirm2 --paired benchmark-tx/outputs/vivonne1573-f103r-confirm2/committed.tsv --exclude-flagged`, plus
`--paired passA.tsv` / `passB.tsv` (the builder's own two passes, if their vocabulary matches). Reported whatever it is, with
CI, both figures; counted as the campaign's S2 look (1). No re-read, no second score. passA/passB alone reported beside.
Cost: 37 lines -> 5 calls per pass x 2 + 2 adjudication units + crops ~ 12 Opus-equivalent calls: cap 20, box 120 min.

## Draft update (lane incarnation 2, 9 Oct 2026 20:4x UTC by date -u; NOT a freeze -- the dated freeze line is written only on the orchestrator's F28 decision)
The frozen pipeline, if S2 is taken as the product baseline (Amendment 6): steps 1-4 above, with the baseline-side fixes of this
campaign made explicit: (1a) the reader brief's overlap sentence is the manifest-generated one (`tools/iiif_lines.py --overlap-note`,
M16; never a typed figure -- TXE2-OVERLAP found every typed sentence wrong); (1b) the sheet is the folder's text-list or printed-key
sheet (Vivonne's is a text list: clean by construction, A1); (1c) the reader brief says "do not resize" (F14); (2a) every pass is
committed with its sha256 before any score (Amendment 3); (3a) a verifier pass on the item's align-conflict flags (if any) precedes
the count (V1/V2's shape), with both figures reported. Step 5 is empty: no instrument passed its eval look. The single score is
reported as the product's unseen-hand number beside S1, never as a gain.

## FROZEN (lane incarnation 2, session_011EV9AKeJ4YuU9jjghdUy6F, 9 Oct 2026 21:3x UTC by date -u; on the orchestrator's F28 decision of 21:18 UTC, route (b); written BEFORE any read of the item)
The pipeline that scores once on vivonne1573-f103r-confirm2, fixed now and not changed after any number is seen:
1. Crops: the folder's committed `ciphers/fr16104-vivonne-spain-1572/images/c106_f103r_L??_s{1,2}.jpg` (tools/iiif_lines.py
   --follow-slope 400, N5-VIVK), checked on an overlay by the reading worker; a cut sign is noted, never re-cut (Gallica 403; the
   note is reported beside the score). The s1/s2 overlap is MEASURED by pixel match (`tools/overlap_audit.py`, O1's method) per
   line and written into the reader brief in the `--overlap-note` form; never a typed figure.
2. Two blind Opus 5.5 passes, reader vocabulary = the committed transcription's label inventory (no --label-map), the folder's
   value-blind text-list sign sheet (clean by construction, A1), the brief says "do not resize"; one subagent call per <= 8
   lines (37 lines: 5 calls per pass); readers never see truth, decodes, the builder's passes, labels or align files; each pass
   committed with its sha256 before the next step.
3. tools/reconcile_passes.py + ONE Sonnet adjudication of disagreements and uncertain positions from the crops (the folder
   protocol; TXE-Q's adjud_task.txt as the worked example); passZ_S2.tsv committed with its sha256. No relabel map exists.
4. The doubt feed (tx_doubt, disagree + latt where inputs exist) listed beside the read, never resolved.
5. No instrument (none passed its eval look).
Order: the reading worker (S2-READ) stops after step 4 and never runs tx_bench; a verifier session (V-VIV) decides the item's
align-conflict flags from the clerk decipherment images and the published key through build_vivonne_confirm2.py's flag column;
the LANE then runs the single score (`tx_bench ... --paired committed.tsv --exclude-flagged`, both figures, the builder's
passA/passB beside) ONCE, as the campaign's S2 look (1), and reports it as "product baseline on an unseen hand", never as an
instrument result or a gain. Prior openings of this item: 0 (the lane has not read its truth, outputs or crops).

## Protocol repair (lane incarnation 2, 9 Oct 2026 22:1x UTC by date -u; TX-RED F33; the orchestrator's choice (a) of 22:0x; BEFORE the score, none taken)
Step 3 as frozen was not executed on passA_S2/passB_S2 (txeng2/s2read/RESULTS.md: first hand-back settled 375 rows by rule; the
resume viewed 9 of 208 disagree rows). Repair: a fresh Sonnet adjudicator runs step 3 as frozen in TXE-Q's packet shape (<= 16
rows per call, each row's crop viewed and recorded; the 208 disagree rows; the 167 agreed-uncertain rows kept as agreed), from
the same queue (txeng2/s2read/adjud_queue.tsv) and the same crops, writing benchmark-tx/outputs/vivonne1573-f103r-confirm2/
passZ_S2b.tsv with its sha256 before any score. passZ_S2 stays on disk, unscored. The single score runs on passZ_S2b; its line
carries F34's clause (flags from the two blind clerk reads, 500 of 1,068 bind) and the as-measured figure beside.

## S2 look taken (lane incarnation 3, session_01P46fwsU5VTc1oJiV1sayg5, 9 Oct 2026 22:22:57 UTC by date -u; the campaign's one S2 look, count 1): one tx_bench run (benchmark-tx/txeng2/s2score/tx_bench_S2.txt, inputs hashed first in SHA256SUMS.prescore; passZ_S2b da404e35..ffe520 as committed by S2-ADJ) on passZ_S2b.tsv --paired committed.tsv --exclude-flagged, the five other files beside in the same run. **Product baseline on an unseen hand (vivonne1573-f103r-confirm2, 1,068 scored): passZ_S2b as measured 0.296 (316/1068, 95% 0.269-0.324; wrong 239, deleted 56, inserted 21); flagged-excluded 0.150 (75/500, 95% 0.121-0.184)** -- flags decided from the two blind clerk reads, not the clerk image (TXV-VIV: 236 FLAG / 0 CORRECT / 20 KEEP; 568 of 1,068 flagged, 500 bind). Beside: passA_S2 0.292 / 0.148 (74/500), passB_S2 0.302 / 0.154 (77/500); the builder's own passes (N5-VIVK) passA 0.232 / 0.048 (24/500), passB 0.246 / 0.074 (37/500); committed.tsv 0.221 / 0.032 (16/500) -- the committed reading is the stream the truth was aligned to, so its figure is a floor by construction, not a reading. Paired vs committed: passZ_S2b fixed 7 / broken 66; passA_S2 7/65; passB_S2 9/76. The two-pass + packet adjudication gave no gain over either single S2 pass on this hand (0.150 vs 0.148 / 0.154). Top confusions: c<-deleted x24, s<-d x17 (present in every file, the committed too), a<-m x7, i<-m x7, e<-d x6, u<-deleted x6. Read-free label counts (no truth): the S2 reads carry ':' 75 vs the committed 156, 'S' 0 vs 141 ('s' 81), '3' and 'V' absent with 'z' 54 and 'y' 60 present, 1,890-1,907 signs vs 2,033 -- a label-inventory and segmentation gap between the readers' sheet (txeng2/s2read/sheet_SIGNS.md) and the committed inventory, so part of the 0.150 may be notation (CLAUDE.md rule 3, PX-BRODEC): a read-free notation audit (PREREG-txeng2-12 S2-NOTE) classifies the 75 and reports a normalised figure BESIDE this line; the look stands as taken; no re-read, no second look. Reported as a product baseline on an unseen hand, never an instrument result or a gain. Next step for the item: a verifier pass with the clerk page images after the 10 Oct 00:00 UTC Gallica probe.

## S2 line, final form (lane incarnation 3, 9 Oct 2026 22:3x UTC by date -u; after TX-RED pass 8 F38, F39, F41; the look itself unchanged). TIMING, disclosed: TX-RED pass 8 was posted at 22:19 UTC and the lane took the score at 22:22:57 UTC having read S2-ADJ's RESULTS but not yet pass 8; F41's acceptance evidence is nevertheless on file in benchmark-tx/txeng2/s2adj/RESULTS.md and packets/: per packet 16/16 rows viewed by the adjudicators' own report with the crop files listed per reply, sides-with over the 208 splits A 97 / B 95 / a third reading 5 / NONE 11 (a rule pass-through would read A about 199, as passZ_S2 did), no packet returned as a pass-through, and every packet task text says 'use ONLY the files named here' naming the sheet, the crops and the packet queue only -- grep of the 13 task texts and the template for passZ_S2, adjud_out, committed or truth: 0 hits -- so the adjudicators were never shown passZ_S2 or adjud_out.tsv. Had the evidence failed F41 the score would have been reported only under F33's option (b) wording; it did not. THE BRACKET (F39): the frozen pipeline reads this unseen hand at between 0.150 (75 of the 500 positions where the folder's earlier reading already agreed with the clerk decipherment -- biased LOW, since the flags are that reading's own disagreements and errors sit where signs are hard) and 0.296 (316 of all 1,068 scored, including 236 the verifier calls doubtful -- biased HIGH); the committed reader's own figures on the same two sets are 0.032 (16/500) and 0.221 (236/1068), the paired line against it (fixed 7 / broken 66) draws nothing because committed is right on the 500 by construction (rule 3's cannot-differ shape); 'an unseen hand at <= 5%' is tested against neither end alone -- both ends are above it. ERROR MASS BY CLASS (F38; from the look's confusion lines and the read-free alignment of the S2 reads to the committed labels, no new opening): (i) the two-dot mark ':' (key value c) dropped -- 'c <- deleted' x24 in the look, 69 of its 156 committed occurrences missing from the S2 reads: a segmentation failure of one mark class, specific and repairable by brief and sheet for a LATER item of this hand, never for this look; (ii) the 3/z pair ('3' = d, 'z' = a; 28 committed '3' read 'z' in passZ_S2): a value error where scored; (iii) 'S' written 's' (47) and 28 brace tokens outside the committed inventory: the readers' vocabulary did not hold to FROZEN step 2's 'committed inventory' rule (s2read/RESULTS.md disclosed it), S/s on key-M positions with no score effect, the brace tokens wrong wherever scored; (iv) residue: look-alike pairs (s <- d x17 is in every file, the committed too, so a truth/key matter; a <- m x7, i <- m x7, e <- d x6). S2-NOTE (PREREG-txeng2-12) classes the 75 formally with a map built before any error is seen. FOLD RE-SCORE counted as an opening (F40): the Spinelli fold re-score is openings 1, not 0; the running total of read-free openings rises by one. The S2 number of record stays the bracket 0.150 / 0.296 as taken at 22:22:57 UTC.

## S2-NOTE companion (lane incarnation 3, 9 Oct 2026 22:5x UTC by date -u): normalised figure beside the look, never replacing it -- 0.154 (77/500) / 0.301 (322/1068) under a map built before any error was seen (s -> S, H -> #, X? -> X); of the 75 flagged-excluded errors notation 0, segmentation 42, read 33; the S2 baseline is not a notation artefact; class (iii) of the final form is corrected (s/S was never notation: the truth sets carry lowercase s). benchmark-tx/txeng2/s2note/RESULTS.md.

## Correction (lane incarnation 3, 9 Oct 2026 23:3x UTC by date -u; TX-RED F44): the final form's sentence "'3' and 'V' absent with 'z' 54 and 'y' 60 present" is false as a count -- passZ_S2b carries '3' 22 and 'V' 36 (committed 68 / 61), passA_S2 26 / 37, passB_S2 17 / 30; the shape is under-use of two defined tokens and over-use of 'z' (54 vs 12), a 3/z value confusion where scored, not absence. The bracket 0.150 / 0.296 and every other figure stand.
