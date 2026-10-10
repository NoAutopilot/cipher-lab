# PREREG TX-ENGINEER-2 round 20 (lane incarnation 4, session_01GukpgU1yBAfju3zg6g8ayG, 10 Oct 2026 01:1x UTC by date -u; pushed BEFORE the build and before any re-score; the orchestrator's decision rule of 00:3x (PREREG-17 "Order change") applied to SCAN-103's NOT BEST)

Rules as PREREG-txeng2-5's preamble. `tools/tx_register.py --check benchmark-tx/PREREG-txeng2-20.md` output before the queue row (01:12:21 UTC): `OK benchmark-tx/PREREG-txeng2-20.md: names register rows and states a difference` (exit 0).
SCAN-103 (benchmark-tx/txeng2/scan103/RESULTS.md, 01:0x UTC): registered offset R = 6655 real 0.6049, selection-fair margin
0.0267 (< 0.03); best s = 6500 real 0.6139, margin 0.0357; 155 letters apart on a flat plateau (6200-6650, 0.593-0.614); the
registered point beats every shuffled key at every offset and reproduces the build's own control. Verdict NOT BEST under the
declared gate. The rule: a NEW f.103r truth is built read-free at the best offset by a separate job, the old truth kept, and the
frozen passZ_S2b is re-scored ONCE beside the record 0.150 / 0.296; look count unchanged; a corrected audit, never a new look.

## RE103 A new f.103r truth at offset 6500, read-free, and ONE re-score of the frozen S2 outputs against it (TX-RE103; Opus 5.5; cap 6; box 60 min; a worker via the account-4 dispatcher, WORK-QUEUE row TX-RE103, since the lane never builds or touches the confirm2 truth; brief = this section)
Nearest prior: SCAN-103 / TXE2-SCAN103 (the verdict and the best offset), DV1d / TXE2-VIV102-REANCHOR (the same operation on
f.102r: build_vivonne_f102r.py --start S aligning one stretch alone at a declared offset, control and selection-fair null
re-run, old item kept, the frozen passes re-scored once), TX-CONFIRM-SET-2 / N5-VIVK (build_vivonne_confirm2.py: the f.103r
stretch end-anchored through j0), TOOL-SCORER-FIX (the scorer the re-score uses), CA-S2 (PREREG-19: the fixed-scorer audit on the
EXISTING truth, run by the lane, so the scorer correction and the re-anchor stay separable). What is different: the f.103r
stretch is aligned alone with its start at dec_norm offset 6500 (SCAN-103's argmax), by the same DP (band 400) and the same
key forcing, exclusions, flag column (TXV-VIV's verdicts, re-applied by (line, raw sign)) and control as the frozen build;
nothing else in the recipe changes. Steps, fixed now: (1) `build_vivonne_confirm2.py` gains `--start S` exactly as
build_vivonne_f102r.py did (without it the build stays byte-identical to the frozen one; `--check` on the frozen item must still
pass before and after the edit); (2) `--start 6500` writes a NEW item **vivonne1573-f103r-confirm2-s6500** (truth TSV + .sha256,
BENCHMARK-TX.tsv row with split confirm2, n_positions / n_scored / n_excluded, the control line and SCAN-103 cited in notes; the
outputs folder benchmark-tx/outputs/vivonne1573-f103r-confirm2-s6500/ carries copies of the SAME six frozen files: passZ_S2b,
passA_S2, passB_S2, passA, passB, committed, hashes equal to s2score/SHA256SUMS.prescore); the old truth, row and outputs are
untouched; (3) the build's control at 6500 (published key vs 200 value-shuffled keys, the same seed) and the selection-fair
margin are printed and must agree with SCAN-103's confirm row (0.6139; fair margin 0.0357) within 0.005, else STOP and report
(no re-score); (4) ONE run of `sh benchmark-tx/txeng2/scorerfix/run_audit.sh vivonne1573-f103r-confirm2-s6500` (the fixed
scorer, both masks, --strict beside, paired vs committed) into benchmark-tx/txeng2/scorerfix/ with the item id in the file names
(the script's S2_* names are suffixed _s6500 by the worker before the run so CA-S2's files on the old truth are not overwritten);
(5) RESULTS.md in benchmark-tx/txeng2/re103/: the new item's counts, the control, the paired-by-line and position figures of
passZ_S2b beside the record (0.150 on 500 / 0.296 on 1,068, value-level) and beside CA-S2's fixed-scorer figures on the old truth,
every hash, "Openings of eval truth: 1 (the re-score)", "a corrected audit of the look of 22:22:57 UTC 9 Oct, never a second
look", no result file printed whole (F52), and a one-line "what moved and why" (re-anchor vs scorer) -- no gate, no verdict word
beyond "measured". Readers: none. Crops: none. The worker never opens a truth TSV by eye, never edits one by hand, never changes
flags. Cost: the DV1d row (2.55) + one scorer run; cap 6, box 60 min, 80% stop at 48 min / 4.8.

## CA-S2 on the existing truth (PREREG-19; the lane, in-session; run now, in the same window)
Executed by the lane as PREREG-19 declared, so that the fixed scorer's effect on the record is on file before RE103's re-anchor
effect: `sh benchmark-tx/txeng2/scorerfix/run_audit.sh` (default item), outputs under scorerfix/ with the plain names; the dated
"corrected audit" lines in PREREG-S2, Amendment 9, the owner paragraph and TRANSCRIPTION.md's Today cell are written from CA-S2
and extended once RE103 lands. Openings: 1 (confirm2, the existing truth) + 1 (dev2).

Costs this round: TX-RE103 6. Eval looks this round: 0. S2 looks: 1 (unchanged). Openings: RE103 1, CA-S2 2.
