# PREREG TX-ENGINEER-2 round 21 (lane incarnation 5, session_01ERAcUeCn1HuAUASaqBTzcf, 10 Oct 2026 02:1x UTC by date -u; pushed BEFORE any run, build or read; after incarnation 4's hand-over, TX-RED pass 14 F68/F69 and the orchestrator's first-jobs list of 02:0x)

Rules as PREREG-txeng2-5's preamble (readers blind; every output committed with its sha256 BEFORE any score; never score an eval item
for an experiment; never edit a *.truth.tsv by hand -- a verifier writes through the build script's flag column and a changed mask is a
NEW item, the old file kept; crop step pasted; no result JSON printed whole (F52); every headline figure value-level with the visual-ID
figure beside where one exists (F53)). `tools/tx_register.py --check benchmark-tx/PREREG-txeng2-21.md` output before the first spawn is
pasted below the sections: `OK benchmark-tx/PREREG-txeng2-21.md: names register rows and states a difference` (exit 0, 02:11:14 UTC). Gate in force unchanged: p < 0.05 at >= 24 on the flagged-excluded eval pool (29); eval looks 0; S2 look 1.

## WIT-FLAGS Verifier pass on the f.103r closing stretch's clerk-split flags against Groen's clerk-independent text (TXV-GROEN; Opus 5.5; cap 6; box 60 min; a VERIFIER session, never a reader, never the lane; TX-RED F64's open support question, pass 14 strategy 1)
Nearest prior: WIT-GROEN (PREREG-19 addendum, txeng2/witanchor/: the Groen IV pp.90*-91* passage aligns to dec_norm 8937-9459 at
ratio 0.79 / 0.65, selection-fair margins 0.46 / 0.27), V-VIV / TXV-VIV (txeng2/vivflags/: the verifier whose verdicts the build
re-applies through benchmark-tx/vivonne1573-f103r-confirm2.flags.tsv at align-conflict positions; it decided from the two blind clerk
reads, never from an independent witness), RE103 / TX-RE103 (the --start option: a changed build writes a NEW item, the frozen build
stays byte-identical, --check passes before and after), CA-S2 (PREREG-19; the fixed-scorer audit of the frozen S2 outputs; run_audit.sh).
What is different: the first flag decision on this item made from a text INDEPENDENT of the clerk decipherment (Groen printed the
closing passage from another manuscript copy): the automatic `clerk-split` flags (the two blind clerk reads disagree at the letter;
cmask in build_vivonne_confirm2.py) are the bulk of the 568 flags, and inside Groen's window a witness letter can confirm the merged
clerk letter where the clerk reads split. Nothing is re-read, no cipher sign is looked at, no truth value changes.
Steps, fixed now:
(1) `build_vivonne_confirm2.py` gains `--witness FILE` (as `--start` was added by RE103): without it the build is byte-identical to the
    frozen one (`--check` on the frozen item passes before and after the edit; both outputs pasted); with it, it writes a NEW item
    **vivonne1573-f103r-confirm2-w** (truth TSV + .sha256; BENCHMARK-TX.tsv row, split `confirm2`, notes naming this section and the
    witness; outputs folder benchmark-tx/outputs/vivonne1573-f103r-confirm2-w/ holding copies of the SAME six frozen files passZ_S2b,
    passA_S2, passB_S2, passA, passB, committed with hashes equal to txeng2/s2score/SHA256SUMS.prescore), truth and plain columns
    byte-identical to the frozen item (checked by script, the diff pasted: only the flag column may differ), the old item untouched.
    It also gains `--offsets OUT.tsv`: line, pos, dec_offset (= j0 + amap[k]), status, flag -- the per-position letter offset the
    verifier needs; a truth-adjacent file the verifier may read (it is a verifier), never a reader.
(2) The verifier's script (benchmark-tx/txeng2/witflags/wit_flags.py): Groen's passage pulled and normalised exactly as wit_groen.py
    (same regex, same fold, the p.90* clean part and the p.91* damaged part kept apart), aligned letter-by-letter to dec_norm at the
    WIT-GROEN offsets (clean 8937-9307, damaged 9270-9459; re-derived by the same best-window search, must agree within 5 letters else
    STOP); evidence = SequenceMatcher matching blocks of length >= 4 only (a letter outside a block, or in the damaged part where the
    OCR character is not alphabetic, is NO-EVIDENCE). For every scored position of the frozen item whose dec_offset lies in 8937-9459
    and whose flag carries `clerk-split` (with or without a TXV-VIV class): witness letter == the merged clerk letter (dec_norm) ->
    CONFIRM; == the OTHER blind clerk read's letter at that offset (tx/dec_*_passA/passB.txt, the build's clerk_mask inputs) ->
    CONFLICT; anything else -> NO-EVIDENCE. Output benchmark-tx/vivonne1573-f103r-confirm2.witness.tsv (header comment naming this
    section; columns line, pos, dec_offset, clerk_letter, passA_letter, passB_letter, witness_letter, part, verdict, reason), and the
    same table for the window's clerk-AGREED scored positions as the ceiling (step 3), never as verdicts.
(3) Controls, run BEFORE any flag is written and pasted in RESULTS.md: (a) ceiling -- the share of clerk-agreed (unflagged for clerk-
    split) scored positions in the window whose witness letter equals the clerk letter inside a block; this bounds what a CONFIRM rate
    can reach under OCR and copy variants; (b) selection-fair null -- 200 letter-shuffled copies of the clean part (50 of the damaged),
    each aligned at its own best window over dec_norm by the same routine, then the same CONFIRM rule applied at the same positions:
    the null distribution of CONFIRM counts (max, p95). Gate, declared: the pass is INFORMATIVE when real CONFIRM count > null max
    AND ceiling (a) >= 0.60; otherwise NON-TEST, nothing written to the build's inputs, verdicts reported only.
(4) Flag rule when INFORMATIVE (applied by the build from the witness file, never by hand): CONFIRM removes the automatic `clerk-split`
    flag at that position ONLY; a TXV-VIV class at the same position stays, with `clerk-doubtful` re-labelled `alignment-doubtful`
    (the clerk letter is confirmed, the key value still conflicts with it, so the doubt is alignment, not text) -- a CONFIRM never
    unflags an align-conflict position; CONFLICT keeps every flag and adds class `witness-conflict` (no correction: a correction needs
    the clerk image, LOCAL-QUEUE L75); NO-EVIDENCE changes nothing. Positions outside the window are untouched.
(5) RESULTS.md in benchmark-tx/txeng2/witflags/: counts (clerk-split positions in the window; CONFIRM / CONFLICT / NO-EVIDENCE by
    part; ceiling; null max and p95; flagged and unflagged totals of the new item beside the frozen 568 / 500), every commit hash with
    sha256, "Openings of eval truth: 1 (the verifier's own, this item)", no result file printed whole, a final "Verdict: measured:
    INFORMATIVE (N confirmed) / NON-TEST" line. Not opened: any reader pass on f.103r (outputs/vivonne1573-f103r-confirm2/*,
    tx/f103r_passA/passB.tsv, passA_S2/passB_S2/passZ_S2b), any f.103r line crop, any cipher sign.
(6) The lane then runs ONCE `sh benchmark-tx/txeng2/scorerfix/run_audit.sh vivonne1573-f103r-confirm2-w` with the S2_* names suffixed
    _w (CA-S2's files untouched) and reports passZ_S2b's two figures under the new mask BESIDE the record 0.150 / 0.296 and CA-S2 as
    "corrected audit, witness-revised mask (N unflagged)", never a second look; the truth of record stays vivonne1573-f103r-confirm2
    and its figures; whether the -w mask becomes the mask of record for any later frozen-pipeline comparison is the orchestrator's
    decision, taken before any such comparison, never after a number is seen. Openings: 1 (the lane's re-score).
Cost: the TXV-VIV row (about 4) + the --witness option; cap 6, box 60 min, 80% stop at 48 min / 4.8.

## OL1-BOXES Machine-proposed sign boxes, reading order and blind overlays on the 35 ORACLE-LOCATION-1 manifest lines, plus the owner's blind sorter page (TXE2-OL1BOXES; Opus 5.5; cap 5; box 60 min; read-free: no reader, no truth, no decode, no pass, no label)
Nearest prior: P1 / TXE2-BOXES (txeng2/boxes/: glyph_atlas default segment on line crops, s1/s2 joined at the overlap midpoint, one
neutral `unsorted` pile; it mapped tiles to passZ positions -- this job maps to NOTHING), OL1-MANIFEST (PREREG-19; the redrawn manifest
txeng2/oracle1/manifest.tsv sha256 978322f62c04d59097f521d73690db00d61a44e794af40546db3d9dfb34b45de, 12 f.102r + 12 no.87 f178v_L01-L12
+ 11 luzerne p1 lines, never re-sampled), ORACLE-LOCATION-1 CANDIDATE (PREREG-17: "machine-proposed boxes verified by the owner in the
sorter's blind mode, LOCAL-QUEUE L74"), X12 / X19 / X13 (model-generated counts and cells, retired). What is different: the proposals
exist for a PERSON to verify (L74's own text: "verify machine-proposed sign BOXES and reading order ... accept, move, split or merge
each box; never read a value"), which L74 cannot start without; no model reads anything, no count is compared to any read or truth, and
the output carries no value, no label, no top-1 and no machine guess. Order note: the orchestrator's first-jobs list placed this worker
after L74's answer; L74's own text needs these proposals first, so the lane runs it now (read-free, about 3-5) and says so in ROOM.
Steps, fixed now: (1) `pip install opencv-python-headless scikit-image scikit-learn pillow` (glyph_atlas.py needs cv2; a fresh
container lacks it); (2) for each manifest line: `tools/glyph_atlas.py segment` default mode (the no.87 atlas recipe) on the line's
crop(s) exactly as TXE2-BOXES did, two-crop lines joined at the s1/s2 overlap midpoint by its spin_join.py rule (three-crop no.87
lines: s1/s2 then s2/s3 the same way), `--median-h` from the crop's own ink if the default is speck-dominated (say which), small
detached marks KEPT as their own boxes (the review's section 3 item 3: a component rule is a proposal, never truth), boxes ordered
left to right into a reading order; output benchmark-tx/txeng2/oracle1/boxes/<hand>/<line>.tsv (box_id, crop, x, y, w, h in that
crop's pixels, order) and boxes_all.tsv; (3) overlays: <line>_overlay.jpg with numbered boxes in Okabe-Ito blue/orange on the crop
(`tools/cvd_check.py` passes; never red/green) AND the unmarked crop beside it (<line>_plain.jpg), the review's "preserve the unmarked
line"; (4) the owner's page: `tools/sign_sorter.py` blind mode -- --signs from the boxes (page = the crop image), --labels every tile
in one neutral pile `unsorted` (no label, no value, no cluster, no rank, no focus, no --show-values), --pages the crops, title
"Oracle boxes: verify the cuts", lede = L74's instruction in the owner's words (accept / bad cut / merge / add a missing box; never read
a value; time the first 100 signs), `tools/sorter_preflight.py` passes; written to benchmark-tx/txeng2/oracle1/sorter/ (page + data
JSON); the lane tells the orchestrator, who publishes (the worker publishes nothing); (5) RESULTS.md: boxes per line per hand (counts
only, compared to nothing), the recipe, the preflight and cvd_check outputs, every file's sha256, "Openings of eval truth: 0", "no read,
no truth, no pass opened". Cost: TXE2-BOXES ran 26 tiles for about 2; 35 lines (about 1,000-1,500 boxes) + a sorter page: cap 5, box
60 min, 80% stop at 48 min / 4.

## END-CIPHER The cipher side of the f.103r end anchor (TX-RED F69; read-free; run by the lane in-session; no truth, no reader)
Nearest prior: WIT-GROEN (the clerk side: Groen's text ends 95 letters before dec_norm's end), WIT-ANCHOR (the method), N5-VIVK (the
end anchor's origin: the f.103r stretch end-anchored on the clerk's closing paragraph), SCAN-103 (the stretch's weak support, fair
margin about 0.03). What is different: the committed reading of f.103r's LAST TWO cipher lines (tx/f103r_rec.tsv L36-L37, the folder's
own reading, not the truth) decoded with the published key (key.tsv C rows, the build's `pub` forcing) to a letter string, then aligned
by WIT-ANCHOR's routine to (a) Groen's normalised passage and (b) dec_norm's last 800 letters, each with a selection-fair null (200
letter-shuffled copies of the decoded string, each at its own best window). Gate, declared: the cipher side is ANCHORED if the decoded
string's best window in Groen's passage lies in its last 200 letters AND ratio - null max >= 0.03; else NOT ANCHORED, numbers reported.
Reads tx/f103r_rec.tsv, key.tsv, dec_norm.txt and the OCR; no truth file, no output file, no crop. Output benchmark-tx/txeng2/witanchor/
end_cipher.py, result_end.json, a section in witanchor/RESULTS.md. Openings: 0.

## F68 rule, numbered (TX-RED pass 14; a dated line also appended to PREREG-txeng2-20)
The F50/F64 rule for a rebuild of record after a window scan reads from this line: a rebuild of record needs (i) the candidate offset's
fair margin to exceed the registered offset's by more than TWICE the scan's own swing, where the swing = the standard deviation of the
fair margin over the five scan offsets on either side of the registered one (reported by the scan as a number), and (ii) equal slack:
the registered offset re-scanned with the same window slack as the candidate (or both windows of equal length after end-truncation).
On SCAN-103 (difference 0.009, swing 0.01-0.02) the rule as numbered reads the same way: no rebuild of record.

Costs this round: TXV-GROEN 6, TXE2-OL1BOXES 5, END-CIPHER the lane's session. Eval looks this round: 0. S2 looks: 1 (unchanged).
Openings: WIT-FLAGS 1 (verifier) + 1 (the lane's re-score); OL1-BOXES 0; END-CIPHER 0.
