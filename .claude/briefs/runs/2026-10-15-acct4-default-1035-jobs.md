# LANE DEFAULT-account-4-20261015-1035 jobs (account 4, lane orchestrator session_01LMotqtLAKk2egUhzTciYng) -- 15 Oct 2026 10:4x UTC

Lane brief: .claude/briefs/default-lane.md. Cap 60, box 10:36-20:36 UTC 15 Oct. Gate 0a: no SESSION-SWEEP-account-4 row.
Backlog = the previous account-4 lane's next list (STATUS.md "LANE DEFAULT-account-4-20261015-0645 handoff", closed 09:48 on budget) plus
`next_steps.py --hot-only` runnable rows, each checked against the folder's own latest NOTES.md Verdict. VERIFY-BACKLOG top rows are Birago/ceppo
(off limits) and eckert-1864 audit2 (googleapis 503 on every job since 12 Oct; parked on L79/L80).
Excluded: LANE DEFAULT-A1-0740-15 holdings (fr4735-monluc-lansac-poland-1573, fr5761-election-1519, pro3055-clinton-1779), LANE DEFAULT-A2-0810-15's
just-closed folders (matignon-mayenne-1586, oldenbarnevelt-brederode-1605), VIV-KEYSTONE (fr16104/fr16106), BNF-FOCUS (fr3982, fr3985-3990),
Birago family/ceppo, Armstrong, Debosnys, cipher-lab-private. colbert26 11/81 [retired] (rule 3 third attempt); es132 vision reader [retired].
Intake gate 10:4x UTC (tools/intake_gate_check.py, pass each): lodewijk-van-nassau-1573-74, clair1161-avis-flandre-1688, baluze167-davaux-1637,
fr2980-gramont.

## Common rules for every job
Exactly the "Common rules for every job" section of `.claude/briefs/runs/2026-10-15-acct4-default-0437-jobs.md` (read it in full, and the files it
points to), with these substitutions:
- address every ROOM line "for LANE DEFAULT-A4-1035-15 (account 4)"; export `CIPHERLAB_ACCOUNT=account-4` before any tools/room.py call;
- every claim/halfway/done ROOM line ends "usage: not readable here";
- images never go into git (scratchpad only; commit TSV/MD/scripts);
- no www.googleapis.com in this wave;
- a worker pays ~1 of start-up before its first unit (A4-0645 overruns): stop before a unit that would cross 80% of cap or box;
- solver jobs: report what was found and where it was not found; do not classify novelty.

## Wave 1 (10:4x UTC 15 Oct)

### LVN-P2K (Opus, cap 4, box 75 min, disk; resources.huygens.knaw.nl <= 4): lodewijk-van-nassau-1573-74 placement of the unplaced 4611 p2_K rows
A4-0645 next 1 / VER-LVN2's next: the ~48 unplaced 4611 p2_K rows (read AUDIT.md VER-LVN2 and NOTES.md LVN-P2B/LVN-P2RETX sections first; do not
repeat them). Place each row in the sequence by the method LVN-P2B used (same control, same PREREG family; write a short PREREG before scoring);
grade per rule 4, changes through the folder's corrections path + `decode_key.py --check`. Units: rows in batches of ~12 at ~0.6 each + 1 start-up.
Then, only if >= 30% cap is left: the eye check of 4610 H tokens ending in the flat-foot 2 (~0.3), verifier-style ruling kept/changed/undecided.
Rule 10: carry every grade change into AUDIT.md.

### C1161-275 (Opus, cap 5, box 90 min, disk only): clair1161-avis-flandre-1688 re-cut all 275 S windows by counting, blind re-sort
Latest Verdict: "re-cut all 275 S windows by counting and re-sort them blind (two readers), then So/Sl into the transcription and Sl=n at M, ~$4".
Read C1161-SSPLIT, C1161-SORT2 and C1161-RECUT sections first: the windows and crops exist on disk (or regenerate from the folder's own crop script,
disk images only; if the source images are not on disk, STOP and say so -- do not fetch). Re-cut every window by counting (as C1161-RECUT did for
three), apply gate K EXACTLY as first registered in C1161-SSPLIT's PREREG, then two blind readers in batches (one subagent call per batch of <= 40
windows, crop paths only), reconciliation as one more priced unit. If K passes on the full set: So/Sl into the transcription, the registered --try
with its power controls, Sl = n at M; else log the result and stop. Units: 2 readers x 7 batches x ~0.25 + reconciliation 0.5 + start-up 1.

### BAL-13X (Opus, cap 2.5, box 60 min, disk; openapi.bnf.fr <= 4, ROOM take/release): baluze167-davaux-1637 cross-run 13: control + 65 strokes
Latest Verdict cheapest next: (1) a registered cross-run control for 13: = Mr (4/4 glossed, within-run shuffle 2/200 ties, BAL-169C): PREREG first,
a null that can vary on the same axis as the statistic (CLAUDE.md rule 3: check the control can differ from the target by construction), --try
at every occurrence before anything enters key.tsv; (2) the two unsettled 65 strokes at full/max (c297, c232, c344 unfetched -- fetch only the
canvases these two strokes sit on, one region each). Then, if >= 30% cap left, the c276 R16 "d'une" E shape (epsilon or Ebar), one request.

### GRA-3038 (Opus, cap 2.5, box 60 min, gallica.bnf.fr/openapi.bnf.fr <= 12, ROOM take/release): fr2980-gramont cipher original of the 27 Feb 1530 Villandry letter
NOTES.md "fr.3038 no.19" section (N8-GRA, 4 Oct 2026) and the Keyhunt row: fr.3038 no.19 / f.42r (btv1b9060036k canvas 68) is a period decipherment
in clear; its cipher original is in no catalogue reached. Do the cloud half: the neighbour leaves fr.3038 ff.40-44 (canvases ~64-72, read the
labels with tools/gallica_folio.py first) at low resolution for a cipher block, then the same check of the Villandry-related leaves the N8 section
names but did not open. If a cipher original in this key is found: record shelfmark/canvas, crop the cipher (scratchpad only), and the alignment
plan with ~cost; do NOT align in this job. If none: log every leaf looked at. Units: ~10 leaf looks x ~0.15 + start-up 1.

Wave 1 spawned 10:42 UTC: LVN-P2K session_01TWF4xvqjvdLFnxeiwQW9Kp, C1161-275 session_01E2AiUscHxXZj6H2jPE5xDu, BAL-13X session_01LoaaUP4dMFqoGmR3Lo4mTs,
GRA-3038 session_019pgfgcdGMfeWiMqm9qnUSV (all Opus).
