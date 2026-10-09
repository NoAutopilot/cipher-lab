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
