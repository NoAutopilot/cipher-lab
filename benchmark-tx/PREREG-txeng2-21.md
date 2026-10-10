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

## WIT-FLAGS result and step 6 (lane, dated 02:4x-02:5x UTC 10 Oct by date -u; TXV-GROEN session_01BxDzNbsyn3pYZ5xaRnAw9j, 2.58 D, done 02:25)
INFORMATIVE: 182 clerk-split positions in dec_norm 8937-9459 (of 323 scored); CONFIRM 84 (clean 65, damaged 19) / CONFLICT 0 / NO-EVIDENCE 98;
ceiling 125/141 = 0.887 (gate 0.60); shuffled null max 9 (clean 6 + damaged 3; p95 3). Item **vivonne1573-f103r-confirm2-w** (truth sha256
3523f652bebc846430ffcb609be0c6212747cdb6365abf244a3390448a44da51): flagged 492 / unflagged 576 (frozen 568 / 500); only the flag column
differs (84 rows: 76 clerk-split cleared, 8 clerk-doubtful re-labelled alignment-doubtful); outputs = s2score/SHA256SUMS.prescore. Limit the
verifier stated: under the block-only evidence rule a disagreeing witness lands in NO-EVIDENCE, so the pass can confirm a clerk letter and
never contradict one (CONFLICT is unreachable by construction, a one-sided instrument). Step 6, run ONCE by the lane 02:47:46 UTC
(`sh benchmark-tx/txeng2/scorerfix/run_audit_w.sh`; sha_check_S2_w.txt all OK; S2_flagged_w.txt, S2_plain_w.txt): **passZ_S2b 0.141 (81/576)
flagged-excluded under the witness-revised mask (60 position errors + 21 insertions; standard SER 0.127, S 39 D 23 I 11) beside the record
0.150 (75/500; 54 + 21; SER 0.134); as measured 0.296 (316/1068) unchanged**; passA_S2 0.139 / passB_S2 0.148 (record 0.148 / 0.154); the
builder's passA 0.043 (25/576) / passB 0.068 (39/576); committed 0.028 (16/576); --strict 0.123, agreement with the committed reader, not a
figure of record; the 76 positions the witness released carry 6 of passZ_S2b's errors (6/76 = 0.079). A corrected audit of the look of
22:22:57 UTC 9 Oct under a second declared mask, never a second look; S2 looks stay 1; openings this step 1 (the lane's re-score). The
truth and figures of record stay vivonne1573-f103r-confirm2's; whether the -w mask becomes the mask of record for a later frozen-pipeline
comparison is the orchestrator's decision, to be taken before any such comparison.

## OL1-BOXES result (lane, dated 02:5x UTC 10 Oct by date -u; TXE2-OL1BOXES session_01ALSUNe5oFQU9kqKJMmYXYW, 3.33 D, done 02:22)
35 of 35 lines boxed read-free: 1,412 boxes (1,284 sign, 128 mark; ghost-dropped 97 under a crop-relative rule the worker declared from
ratio numbers alone), overlays cvd_check PASS, folder 16 MB, benchmark-tx/txeng2/oracle1/{boxes,sorter}/. The sorter page FAILS
`tools/sorter_preflight.py` on two checks: (a) answerable -- the PREREG required one neutral pile and no focus while the gate requires a
non-empty focus and >= 2 named piles: the lane's PREREG error, two conditions no page can meet together as the tools stand; (b) shape 14.0%
vs 5% -- wide, strip-height and odd-ink boxes, which are the machine proposals' own bad cuts, the very thing the owner's pass is for. Nothing
published. Fix below (OL1-PAGE). Worker ledgered D: the brief was met where the brief was consistent.

## OL1-PAGE The oracle box-verify page made publishable: a declared box-verify mode in the preflight gate and the page rebuilt on the machine's cut kinds (TXE2-OL1PAGE; Opus 5.5; cap 4; box 45 min; read-free)
Nearest prior: OL1-BOXES (above: the boxes and the failing page), P1 / TXE2-BOXES (one neutral pile for a feed page), SORTER-PREFLIGHT
(tools/sorter_preflight.py, 6 Oct 2026: the five checks and their must-not-block tests), MQS-SORTER (blind mode; sorter_preflight fails
colour and colour-naming hints). What is different: a box-VERIFY page has no reading to pile by, so (i) `tools/sorter_preflight.py`
gains `--box-verify`: check 3's three shape counts (ink outside 3-60%, width over 2.5x the median, strip-height) are computed per hand
(median width per page set, not pooled across hands) and REPORTED to <stem>.shape_flags.tsv, never failing under this mode; the off-list
test and checks 1, 2, 4, 5 are unchanged; docstring states the must-catch (an unanswerable page -- empty focus or under 2 named piles --
still fails under --box-verify) and the must-not-block (a 14% shape page passes under --box-verify and fails without), each with an
offline test in tools/tests/test_sorter_preflight.py; SYSTEM.md row updated, `python3 tools/system_map_check.py` exit 0. (ii) The page
is rebuilt from the committed boxes with piles = the machine's geometric CUT KIND only: `sign box` (kind=sign) and `mark box` (kind=mark)
-- two named piles, no value, no label, no read, no top-1; the owner's decisions are the template's own controls (Fix the cut; Add a missed
sign / split a merged box; Not a letter) and any pile the owner creates; focus ("Check these first") = the shape-flagged tiles from (i),
each with a geometric focus note only ("wide for its line", "touches both strip edges", "ink outside 3-60%"; never a reader-split form,
never a colour word); lede = L74's instruction plus one sentence saying the piles are the machine's cut kind, not a reading; the blind-seed
sentence replaced as OL1-BOXES did. (iii) Paste `tools/sorter_preflight.py --box-verify` (PASS) and without the flag (its FAIL, for the
record), cvd_check, sha256 of page + data, RESULTS.md in txeng2/oracle1/ ("## OL1-PAGE"), "Openings of eval truth: 0"; nothing published
(the orchestrator publishes for L74). Cost: a tool option with two tests + a page rebuild, about 3; cap 4, box 45, 80% stop 36 min / 3.2.

## SHEET-VIV The pictured key sheet in place of the text-list sheet on the dev leaf f.102r (dev2) -- the one reader experiment with headroom runnable today (TXE2-SHEETVIV; Opus 5.5 worker, Opus 5.5 readers, Sonnet packet adjudicators; cap 22; box 120 min; TX-RED pass 15 F72 (ii))
Nearest prior: DV1b / TXE2-VIV102-BASE (the recipe this job copies and the baseline it is paired against: passZ_dv1 0.124 on dev2, 84/679
= 43 position + 41 insertions; passB_dv1 0.096), SH-VIV / TXE2-VIVSHEET (ciphers/fr16104-vivonne-spain-1572/glyphs/sheet_tomokiyo_v1.png
+ .tsv: 40 of 40 committed labels, value-blind, used by no reader), S2-READ / DV1b (the text-list sheet sheet_SIGNS_dv1.md), X1b / B1 / B2 /
B3b (sheet corrections, each a baseline change found through the truth), TX-SHEET / X7 (compare and exemplar layouts, retired: an exemplar
beside a doubtful tile). What is different: the sheet FORM is the treatment, declared before any read and built without the truth (SH-VIV
cut it from Tomokiyo's published drawings): the same two blind Opus passes, reconcile and packet adjudication as DV1b, with the pictured
whole-inventory sheet in place of the text list -- the form every other benchmark hand already has (printed key sheets), so a gain here
says the S2 hand's 15% / 30% is partly a sheet-form artefact and the product's sheet rule for a hand with a drawn key is "picture it";
no exemplar sits beside a tile, nothing is compared. Protocol, fixed: (1) reader_task = viv102base/reader_task.txt with the sheet reference
changed to glyphs/sheet_tomokiyo_v1.png (+ its token list from sheet_tomokiyo_v1.tsv), the [PLAIN:...] sentence of Amendment 9 (24), the
measured 250 px overlap sentence kept, "do not resize" kept; committed with sha256 BEFORE any read; crops = the same c105_f102r s1/s2 files
DV1b read, 5 calls per pass (<= 8 lines each), two blind Opus 5.5 passes; `tools/reconcile_passes.py`; packets of <= 16 DISAGREE rows to
fresh Sonnet calls, crops viewed, the tool-call file-access log committed per F63; passZ_sv assembled as viv102base/assemble_z.py does;
every output committed with its sha256 before the score. (2) ONE score: `tools/tx_bench.py passZ_sv.tsv passA_sv.tsv passB_sv.tsv --bench
BENCHMARK-TX.tsv --item vivonne1573-f102r-dev2 --paired benchmark-tx/outputs/vivonne1573-f102r-dev/passZ_dv1.tsv --exclude-flagged
--strict` (value-level headline, visual-ID beside); the as-measured run beside. (3) Dev gate, declared (F56/F59 endpoint): PASS = lines
improved > lines worsened at the line sign test p < 0.05 AND the unit-cost edit total on the 679 unflagged positions falls by >= 20%
against passZ_dv1 (its edits -> at most 0.8x); position McNemar reported beside; per item (dev2 is the only item: under F47 one item
carries all, so a PASS licenses a product recommendation on sheet form for this hand and a second-hand test, never an S1 claim, never any
f.103r step -- the S2 look is spent and f.103r is not touched). Power quoted (F62; tx_power --errors 84 --n 1234 --fix 0.3 --alpha 0.05,
1,000 draws, the position test): clean 1.000, noisy0.1 0.871, noisy0.5 0.000, worse / noop / random3 0.000; the line-level test's power
is not simulated by the tool (said, not hidden). Readers never see truth, decodes, passZ_dv1, other passes or sheet_SIGNS_dv1; the worker
opens no truth by eye (one scoring run; classify.py counts only). Output benchmark-tx/txeng2/sheetviv/ (RESULTS.md with every hash,
"Openings of eval truth: 0", "dev openings: 1"). Cost: DV1b ran 18.38 under cap 22; the same shape: cap 22, box 120, 80% stop 96 min /
17.6, stop before a pass or packet that would cross either.

## MARKS-DEV2 The ':' mark-class detector's read-free half on dev2 (TXE2-MARKS; Opus 5.5; cap 4; box 50 min; read-free: no reader, no vision call; the truth opened only by the scoring script; TX-RED pass 8 strategy 2 and pass 15 F72 (iii), decoupled from the oracle date)
Nearest prior: X19 (ink-count deletion detector: flagged 83-100% of lines, FAIL read-free -- a blanket flag), X12 (count-then-read, retired),
P1 / TXE2-BOXES and OL1-BOXES (glyph_atlas component boxes on line crops), DV1b (f.102r: 41 of the 84 unflagged errors are insertions;
S2-NOTE: the ':' mark dropped x24 on f.103r), Amendment 9 (21) (the instrument parked behind the oracle run). What is different: a shape
rule for ONE mark class -- two small stacked components with no stroke -- scored for recall and precision against a known answer and for
lift at the baseline's error positions against a position-shuffle null, never a blanket flag, never a fix; run now because it needs no
desk step (F72). Protocol, fixed before any truth is consulted: (1) components on the 37 f.102r line crops by the OL1-BOXES recipe
(build_ol1_boxes.py, no ghost rule change); (2) ':' candidate = two components each under 0.35 x the line's median sign height, x-overlap
>= 50%, vertical gap under 1.0 x the smaller's height, no third component overlapping either; mapped to reading positions by x-order as
OL1-BOXES orders boxes; (3) scored by script only: recall and precision of the candidates against the dev2 truth positions whose ref_sign
is ':' (the truth read by the script, never printed, never viewed; the mapping by order per line, with the line's box count beside its
position count so an order slip is visible); (4) lift: the share of passZ_dv1's errors on the 679 unflagged positions (the 43 position
errors and the 41 insertions, located by the fixed scorer's alignment) that fall at or within one position of a candidate, divided by the
share of all 679 positions that do; selection-fair null = 200 shuffles of the error positions within their lines; (5) output a doubt list
(line, position, reason) for the sorter feed, never a change to any pass or truth. Gate, declared: candidate instrument if recall >= 0.70
at precision >= 0.50 on ':' AND lift > the null's p95; FAIL read-free otherwise, with both numbers. A candidate licenses only a separate
PREREG (the detector as a lattice constraint at flagged positions, X3's shape, position-level gated per F47). RESULTS.md in
benchmark-tx/txeng2/marks/, every hash, "Openings of eval truth: 0", "dev openings: 1 (by script)". Cost: TXE2-BOXES 2 + a scoring
script; cap 4, box 50, 80% stop 40 min / 3.2.

## TX-RED pass 15 answers (lane, 02:5x UTC 10 Oct by date -u)
F70 adopted: one dated sentence each in the owner paragraph (research/TX-ENGINEER-2-2026-10-09.md), PREREG-S2's "Corrected audit" line and
TRANSCRIPTION.md's Today cell -- RE103 stopped at its control tolerance 01:2x, the 6500 alignment is the registered one to within 26
letters, no second truth, no re-score, the record stands on CA-S2; the -w corrected audit written beside in the same sentences. F71 adopted:
PREREG-21 went up in its own commit (8212de547, 02:11:19) before either spawn; from here a WORK-QUEUE row whose brief is a PREREG section
carries the PREREG's push hash, and a PREREG is never pushed only inside a room.py fold. F72 adopted: (i) was WIT-FLAGS (done, above);
(ii) SHEET-VIV and (iii) MARKS-DEV2 are PREREG'd above and spawned this check-in; Amendment 9 (21)'s "after the oracle run" order is
superseded for the read-free half by this line (the oracle date is the owner's).

Costs this check-in: TXE2-OL1PAGE 4, TXE2-SHEETVIV 22, TXE2-MARKS 4. Eval looks: 0. S2 looks: 1 (unchanged). Openings: WIT-FLAGS step 6 1
(the lane); SHEET-VIV 0 eval / 1 dev; MARKS-DEV2 0 eval / 1 dev; OL1-PAGE 0.

## OL1-PAGE amended (lane, 10 Oct 2026 02:59 UTC by date -u; the orchestrator's message of 02:52: "re-cut ... re-run the preflight ... then I publish"; the gate stays, the proposals change; BEFORE TXE2-OL1PAGE had changed any tool)
Step (i) is WITHDRAWN: no `--box-verify` mode is added to tools/sorter_preflight.py -- a mode that lets the page pass by reporting what the
gate counts would be gate-shopping on a page whose shape count is real (bad cuts are bad proposals, and they cost the owner's minutes).
Instead the proposals are re-cut by declared, read-free, per-hand geometric rules (all medians per hand, kind=sign boxes only), applied in
this order and logged per box (boxes_recut.tsv: box_id, rule, from, to): (1) over-wide -- a box wider than 2.5x the hand's median sign width
is split at the k-1 deepest valleys of its column ink profile into k = round(width / median width) boxes; (2) strip-height -- a box touching
both the top and bottom edge of its crop is trimmed to the rows of its own ink inside the line's core band (between the 5th and 95th
percentile rows of the line's ink profile); if it still touches both edges it is dropped as a neighbour-line intrusion and listed; (3) ink
outliers -- a box with ink under 3% is dropped (blank or speck); a kind=mark box is not a tile of its own: it goes to the sorter through
`--marks` attached to the sign box it overlaps in x (else the nearest sign centre within one median width), so the tile is cut around the
union and the mark stays visible (the sorter's own mechanism; the review's "retain small disconnected marks" is kept in marks.tsv and in the
tile); a mark with no sign in reach stays its own box and is listed; a kind=sign box over 60% ink is padded 2 px a side and re-measured.
Then `tools/sorter_preflight.py` as it stands must PASS: piles = `sign box` (and, where any mark stayed alone, `mark box`); focus = every
box a rule changed (split piece, trimmed, mark-attached union) with a geometric note only; lede as before. If the plain preflight still
fails on shape after the rules, the worker STOPS and reports the residual by class and hand -- no further rule is improvised and no gate
is touched; the lane and the orchestrator decide the next rule in a further dated line. Everything else in OL1-PAGE (read-free, no
publish, RESULTS section, "Openings 0", cap 4, box 45) stands. Published only by the orchestrator after a ROOM line carrying "preflight:
PASS" with the five check lines.
