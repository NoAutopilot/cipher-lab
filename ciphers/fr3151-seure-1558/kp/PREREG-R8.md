# R8-SEURE pre-registration (6 Oct 2026, written 04:07 UTC by date -u; committed before any run)

Worker R8-SEURE (LANE-RUN8-account-1, account 1, Opus), brief `.claude/briefs/runs/2026-10-06-account1-run8-jobs.md` job R8-SEURE.
Named next step of D2-SEURE: a null-tolerant `nom_test` setting with its own 10%-null matched control first; R1/R2 only if the
control passes.

## The one change
`kp/nom_test.py` gains `--null-cost X` (passed to `tools/interlinear_align.run_align`; default -3.0 = every earlier run, byte-identical)
and `--control-gate ERR:SHARE` (exit 3, "CONTROL BELOW GATE", before any target alignment when the control misses). Setting
registered: **null cost -1.0**, a single value fixed here, not swept (rule 3 third-attempt clause: no tuning of this knob after the
answer is seen). Everything else as PREREG-RUN6B: same P, same R1/R2, R = 0.85/1.00/1.13, floor 12, max chunk 8, seed 1,
3 control keys x 20 shuffled-gloss draws, 200 shuffled + 200 rotated draws per target.

## Command
`python3 kp/nom_test.py kp/P.txt kp/f81R_recon_R1.tsv kp/f81R_recon_R2.tsv kp/result_r8.json --null-cost -1.0 --nulls 0.10,0
 --err 0,0.095,0.242 --ctl-seeds 3 --ctl-draws 20 --draws 200 --control-gate 0.095:0.66`
(0.095 = measured err_R agreement of the reconciled reads; 0.242 = the anchoring bracket PREREG-RUN6B added.) The 0%-null arm is run
at the same null cost so a miss can be read against both designs.

## Gates
- Control gate (mechanical, before targets): the control passes >= 2/3 keys at err 0.095 in BOTH the 10%-null and the 0%-null arm.
  Miss -> CONTROL BELOW GATE, targets not run; logged "null-tolerant setting untested-by-this-tool at null cost -1" (not refuted).
- Control power for reading a target miss as a test: also >= 2/3 at 0.242 in the 10%-null arm; else a miss is a "non-test above the
  agreement figure".
- Target gate (unchanged from N8-SEU/RUN6B): a read PASSes iff S* > p95 AND > max of BOTH shuffled and rotated nulls. PASS of R1 or R2
  -> H-span-under-nomenclator-with-nulls licensed; key fragment drafted at C/M only by a later job, VERIFIER WANTED. FAIL with control
  power -> negative conditional on this H-span, the reconciled reads and this one model; not a design-family negative.
- Stop rule: the run is backgrounded with a timeout ending before 80% of the box (04:40 UTC); unfinished cells are reported as not run.
