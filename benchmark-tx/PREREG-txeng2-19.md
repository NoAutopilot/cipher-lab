# PREREG TX-ENGINEER-2 round 19 (lane incarnation 4, session_01GukpgU1yBAfju3zg6g8ayG, 10 Oct 2026 01:0x UTC by date -u; pushed BEFORE any run; the in-session jobs of a lane at lineage depth 8)

Rules as PREREG-txeng2-5's preamble. `tools/tx_register.py --check benchmark-tx/PREREG-txeng2-19.md` output before the first run (01:01:58 UTC): `OK benchmark-tx/PREREG-txeng2-19.md: names register rows and states a difference` (exit 0).
Context: this incarnation sits at lineage depth 8 (the limit): it can spawn no worker, so every job here is a script run by the
lane itself in its own session, exactly as PREREG-S2 already has the lane run the single score. No reader, no crop, no truth file
opened by eye; every score run is logged as an opening. Cost: the lane's own get_session reading, reported per check-in, not per job.
The orchestrator (00:5x message) creates incarnation 5 from its own session; the TX-PROGRAM lineage-depth rule records the fix.

## CA-S2 Corrected audit of the S2 look and of DV1b with the fixed scorer (TOOL-SCORER-FIX step 3, PREREG-txeng2-17; HELD until SCAN-103 reports; run by the lane)
Nearest prior: TOOL-SCORER-FIX / TXE2-SCORERFIX (the tool, 6896cf0e7; run_audit.sh prepared, not run), S2 look (txeng2/s2score),
DV1b (txeng2/viv102base), DV1d (dev2 the truth of record), SCAN-103 (PREREG-18, running). What is different: nothing is
re-read; the frozen outputs are re-scored once with the corrected scorer, both masks, --strict beside, and reported BESIDE the
figures of record as a corrected audit of the one look, never a second look. Decision rule (the orchestrator's, PREREG-17 "Order
change"): STANDS -> `sh benchmark-tx/txeng2/scorerfix/run_audit.sh` on the existing confirm2 truth; NOT BEST -> a NEW f.103r
truth is built read-free at the best offset by a separate PREREG first (old truth kept), then run_audit.sh with the new item id, and
passZ_S2b's two figures are reported beside the record 0.150 / 0.296. Output: benchmark-tx/txeng2/scorerfix/S2_*.txt,
DV1b_*.txt, sha_check_*.txt, and a "## Corrected audit" section in scorerfix/RESULTS.md; dated 'corrected audit' lines in
PREREG-S2, Amendment 9, the owner paragraph and TRANSCRIPTION.md's Today cell. Openings: 1 (confirm2) + 1 (dev2, dev).

## F55-REDERIVE The four baseline-change paired cells re-derived under drop_flagged with the fixed scorer (read-free; run by the lane; runs now, independent of SCAN-103)
Nearest prior: B1 / TXE2-BASE-SPIN (fixed 8 / broken 2), B2 / TXE2-BASE-SPIN2 (2 / 4), the fold (Amendment 9: 4 / 4), B3b /
TXE2-BASE-GUN2 (6 / 6) -- all four cells were computed by the pre-fix paired(), which ignored truth flags (TX-RED F55). What is
different: the same four comparisons re-run with the corrected scorer, which pairs on the flagged-excluded rows and reports
per-line edit totals (the new S1 endpoint, F56) with the position McNemar beside. Commands, fixed now: (B1) passZ_v4 --paired
passZ_pipeline; (B2) passZ_v5 --paired passZ_v4, both with --label-map benchmark-tx/txeng/confirm/collapse_map.tsv; (fold)
passZ_v5 --paired passZ_v4 with --label-map benchmark-tx/txeng2/basespin2/fold/collapse_map_fold.tsv; (B3b) gunther passZ_gv2
--paired passZ_pipeline; each with --bench BENCHMARK-TX.tsv --item <item> --exclude-flagged, sha256 of every input first. No
gate verdict rests on any cell (eval looks 0); the result is the corrected cells beside the old ones. Output: benchmark-tx/
txeng2/f55/ (SHA256SUMS.prescore, one .txt per cell, RESULTS.md). Openings: 2 (Spinelli, gunther; read-free re-scores).

## COMP-VIS F53 visual-ID companion scores on the Spinelli and gunther outputs (read-free; run by the lane)
Nearest prior: F53 (TX-RED pass 12; Amendment 9 (27)), TOOL-SCORER-FIX (--strict: exact ref_sign match), B2/fold (Spinelli
passZ_v5 under the fold map), B3b (gunther passZ_gv2). What is different: the first visual-ID figure beside a value-level one --
on these two items the truth's ref_sign is the atlas code and the truth set is the value-compatible set, so `--strict` scores
visual identity and the default scores value compatibility, from the same frozen outputs. Commands, fixed now: Spinelli passZ_v5,
passA_v5, passB_v5, passZ_pipeline, committed with --label-map .../fold/collapse_map_fold.tsv --exclude-flagged --strict; gunther
passZ_gv2, passA, passB, passZ_pipeline, committed with --exclude-flagged --strict. Reported as "value-level X / visual-ID Y" per
output and mask, no gate, no look. A strict figure above the value figure measures homophone or allograph credit in the value
score, not reader error alone (a shared value is never a visual equivalence, F53). Output: benchmark-tx/txeng2/compvis/
(SHA256SUMS.prescore, two .txt, RESULTS.md). Openings: counted with F55-REDERIVE's (the same two items, the same session).

## PROBE-R7 Reachability of the released detection models (TX-RED pass 12 strategy 1; one request per host; done 00:58 UTC, recorded here)
Nearest prior: none in the register (the first outside-the-frame instrument probe); the outside review section 3 and R7.
What is different: not an experiment -- a logged reachability result that decides whether a released detector can be tested on
our crops at all. Result (00:58-00:59 UTC 10 Oct, descriptive UA, one request per host, 1.6 s apart): github.com HTML and
api.github.com 403 (the proxy; SO-TX-CITE saw the same), raw.githubusercontent.com 200 (both READMEs saved to the scratchpad),
`git ls-remote https://github.com/dali92002/HTRbyMatching` answers (refs/heads/main c669cc41) so a clone is possible, HTRbyMatching
weights are Google-Drive links (drive.google.com answers 303 to one uc?export=download probe; the confirm-token flow untested),
DTLR (raphael-baena/DTLR) README 200 with pretrained and fine-tuned checkpoints also on Google Drive, huggingface.co/api/models
answers 200 with no HTRbyMatching entry. Verdict: reachable in principle (code by git, weights via Drive, one more request to
confirm a download); a model run is a separate PREREG (a worker with a GPU-less box: CPU inference on a few line crops, a cost
estimate first). No register row claims any result beyond reachability.

## OL1-MANIFEST ORACLE-LOCATION-1's line manifest, the precondition of LOCAL-QUEUE L74 (read-free; run by the lane; no annotation, no read)
Nearest prior: ORACLE-LOCATION-1 CANDIDATE (PREREG-17), P1 / TXE2-BOXES, DV1d (dev2), birago1572-no87 (the first campaign's
units), luzerne108a-p1 (TX-POOL-LEAF, unread by any pipeline so far). What is different: the final registration's sampling step
only, declared and committed before any annotation or fresh reader call: hands (1) vivonne1573-f102r (candidate lines
f102r_L01-L37 as BENCHMARK-TX's row lists them, crops ciphers/fr16104-vivonne-spain-1572/images/c105_f102r_L??_s{1,2}.jpg; the
visual route, the old truths never reused), (2) birago1572-no87 (candidate lines f178r_L01-03, f178v_L01-23, f179r_L01-03, 29
lines; crops ciphers/nevers-birago-fr3251-1572/harvest/), (3) the THIRD HAND, named now: **luzerne108a-p1** (La Luzerne legation
secretary, Philadelphia 1781; candidate lines p1_L01-L11, 11 complete lines, one crop per line on disk at
benchmark-tx/txpool/luzerne108a/crops/p1_L??.jpg; fewer than 12 so all 11 enter, above the minimum 6) -- chosen over
ceppo-f21v-S (its line crops are not committed, only regenerable) and gunther8246-p2 (today's figure 0.020 flagged-excluded
leaves no room for the 0.03 absolute condition); f.103r excluded. Sampling: `python3 benchmark-tx/txeng2/oracle1/make_manifest.py`
-- random.Random(20261010).sample over each hand's sorted candidate list, 12 per hand (all if fewer); a line is excluded before
sampling only if its crop file is absent on disk (checked by the script, listed), never by content, error or score. Output:
benchmark-tx/txeng2/oracle1/manifest.tsv (hand, line, crop paths) + manifest.tsv.sha256, committed in one push; then L74's
"not before the lane posts the line manifest" clause is met and the orchestrator is told. The final registration (reference
protocol, arms, scoring, PASS rule as PREREG-17 states them; the box-proposal step; the desk minutes per 100 signs) is a
dated section appended here once L74 is answered, before any annotation. Openings: 0.

Costs this round: the lane's own session (no worker). Eval looks this round: 0. S2 looks: 1 (unchanged). Openings: CA-S2 2 (one eval, one dev), F55/COMP-VIS 2.
