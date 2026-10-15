# LANE DEFAULT-account-4-20261015-1634 jobs (account 4, lane orchestrator session_016LJSnNaAqJveDTZ1JFKq8J) -- 15 Oct 2026 16:4x UTC

Lane brief: .claude/briefs/default-lane.md. Cap 60, box 16:34 UTC 15 Oct - 02:34 UTC 16 Oct. Gate 0a: no SESSION-SWEEP-account-4 row.
Backlog = STATUS.md "LANE DEFAULT-account-4-20261015-1441 handoff" next list (item 2 clair1161 now held by live DEFAULT-A2-1616 C1161-G1; item 3
matignon left to account 2), then `tools/next_steps.py --hot-only` runnable rows. VERIFY-BACKLOG top rows are Birago family (off limits).
Excluded: live DEFAULT-A2-1616 (august-van-saksen, antt-msliv0638-brochado, clair1161, fr4715-f61, harley-287), DEFAULT-A1-1426 (closing:
na-janssens-java, baluze167, fr5761), VIV-KEYSTONE (oldenbarnevelt-brederode, espagnol142, fr16104/fr16106), matignon, Birago family/ceppo/
nevers-birago, Armstrong, Debosnys, cipher-lab-private.
Intake gate 16:4x UTC (tools/intake_gate_check.py, pass each): lodewijk-van-nassau-1573-74, fr16045-pisany-rome-1585.

## Common rules for every job
Exactly the "Common rules for every job" section of `.claude/briefs/runs/2026-10-15-acct4-default-0437-jobs.md` (read it in full, and the files it
points to), with these substitutions:
- address every ROOM line "for LANE DEFAULT-A4-1634-15 (account 4)"; export `CIPHERLAB_ACCOUNT=account-4` before any tools/room.py call;
- every claim/halfway/done ROOM line ends "usage: not readable here";
- images never go into git (scratchpad only; commit TSV/MD/scripts);
- no www.googleapis.com in this wave;
- a worker pays ~1 of start-up before its first unit; Opus small jobs ran 1.3-2x their estimate today: stop before a unit that would cross 80% of
  cap or box;
- after `tools/room.py --push PATHS`, run `git status` and push any named path it left uncommitted;
- fetch + rebase before every push; write only your own NOTES.md section and subfolder;
- solver jobs: report what was found and where it was not found; do not classify novelty.

## Wave 1 (16:4x UTC 15 Oct)

### LVN-L04 (Opus, cap 2.5, box 50 min, disk only): lodewijk-van-nassau-1573-74 p1_L04 head "124, 127"
Verdict (LVN-L05W "Next"): give the p1_L04 head (eye-read "124, 127" by LVN-4610U/LVN-4610H) its own blind look by the LVN-L05W design --
wide crops by `lvnl05/cut_w.py` (token plus a neighbour each side, scratch only), an addendum PREREG (lvnl05/PREREG-LVN-L04.md) fixing the scored
tokens, the same-line H control and the gate pushed before any read; Sonnet subagent calls one per crop set, target + control, nothing else shown.
If the control gate passes and the blind read agrees, insert the head through `lvn10/inserts_lvneye.tsv` at M (key.tsv value for 124/127 if any,
else U) and regenerate every derived file with --check exit 0 (decode_key.py all decode*.json, lvn10/apply.py, settle.py, axnames/revisions.py),
carry the counts into AUDIT.md as LVN-L05W did. If the gate fails, no insert; log it. Do not re-cut the =tout word design (LVN-L05W: no third
re-cut). Units: PREREG 0.3, crops 0.2, 2 Sonnet calls x 0.3, apply + regen 0.5, write-up 0.3, start-up 1. NOTES "## LVN-L04".

### PIS-INT (Opus, cap 3, box 60 min, openapi.bnf.fr <= 3 with ROOM take/release, >= 3 s apart): fr16045-pisany-rome-1585 f.121 interlinear name glosses
Verdict (PIS-121B "Next (different instrument)"): the small interlinear name glosses written above cipher groups on f.121 (canvas 252 of
btv1b9060906j; PIS-121 saw them in the L17-L20 region, one read as "Cardinal Ferdinand"). Re-fetch c252 (1 request, sha1 must equal
407648e7e17b46283e3cb9200ad6b0056b5adaad), cut line crops with `tools/iiif_lines.py --image ...` (command pasted before the first subagent call),
find every interlinear gloss on the page, and read gloss + the cipher group under it: two blind Sonnet passes one crop per call + one reconcile
unit. Build hand pairs (group, gloss) and run them through `tools/interlinear_align.py` (never a private DP script) against the 1585 table
(key.tsv, key86.tsv as NOTES says applies to f.121): report per pair whether the table decodes the group to the gloss, with a shuffled-pair
control that can differ on this axis. No key.tsv or ciphertext edit; a pair that disagrees is logged, not resolved. Write pis_int/ and NOTES
"## PIS-INT". Units: fetch+crops 0.3, 2 passes x 0.5, reconcile 0.5, align + control 0.5, write-up 0.3, start-up 1.
