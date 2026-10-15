# LANE DEFAULT-account-4-20261015-1441 jobs (account 4, lane orchestrator session_01XHeiyMvc9LoEpDS1XcWNCC) -- 15 Oct 2026 14:4x UTC

Lane brief: .claude/briefs/default-lane.md. Cap 60, box 14:42 UTC 15 Oct - 00:42 UTC 16 Oct. Gate 0a: no SESSION-SWEEP-account-4 row.
Backlog = STATUS.md "LANE DEFAULT-account-4-20261015-1236 handoff" next list (its items 3-5 -- fr4735, fr5761, baluze167 -- are now held by live
DEFAULT-A1-1426), then `tools/next_steps.py --hot-only` runnable rows. Each step re-read from the folder's own latest NOTES.md Verdict.
Excluded: live DEFAULT-A1-1426 (fr5761, colbert26, fr4735, baluze167, na-janssens, fr3198) and DEFAULT-A2-1410 (willem-van-hessen, pro3055,
na-suriname, harley-287, fr3151, fr16144, fr16045, decode-1162/1168, bne20211, august-van-saksen) holdings, VIV-KEYSTONE (fr16104/fr16106,
espagnol142), Birago family/ceppo, Armstrong, Debosnys, cipher-lab-private.
Intake gate 14:4x UTC (tools/intake_gate_check.py, exit 0 each): matignon-mayenne-1586, clair1161-avis-flandre-1688, lodewijk-van-nassau-1573-74.

## Common rules for every job
Exactly the "Common rules for every job" section of `.claude/briefs/runs/2026-10-15-acct4-default-0437-jobs.md` (read it in full, and the files it
points to), with these substitutions:
- address every ROOM line "for LANE DEFAULT-A4-1441-15 (account 4)"; export `CIPHERLAB_ACCOUNT=account-4` before any tools/room.py call;
- every claim/halfway/done ROOM line ends "usage: not readable here";
- images never go into git (scratchpad only; commit TSV/MD/scripts);
- no www.googleapis.com in this wave;
- a worker pays ~1 of start-up before its first unit; Opus small jobs ran 1.3-1.8x their estimate today: stop before a unit that would cross 80% of
  cap or box;
- after `tools/room.py --push PATHS`, run `git status` and push any named path it left uncommitted;
- two jobs in this wave share matignon-mayenne-1586: each writes only its own NOTES.md section and its own subfolder; fetch + rebase before every
  push; never edit key.tsv, ciphertext or status lines another job may touch;
- solver jobs: report what was found and where it was not found; do not classify novelty.

## Wave 1 (14:5x UTC 15 Oct)

### MAT-ORL (Opus, cap 6, box 75 min, disk only): matignon-mayenne-1586 o relabel by shape + --try oA=i / oB=a
Verdict (MAT-R2): re-label the 13 leaves' o by shape (plain oA / stemmed oB) using MAT-O3X and MAT-R2's agreed labels, PREREG before the run, then
`tools/decode_key.py --try` oA=i and oB=a at every occurrence with its power control (rule 3: the control must be able to differ on this axis). No
key.tsv edit unless --try accepts with the control passing; an accepted value enters at S only where the control licenses it, else M. Tokens not
covered by the two readers' crops stay o (unlabelled), never guessed. Read MAT-OSPLIT, MAT-O3X, MAT-R2, MAT-BOX, MAT-KEY first. Units: PREREG 0.5,
relabel script 1, two --try runs with controls 2 x 0.8, write-up 0.5, start-up 1.

### MAT-F91 (Opus, cap 4, box 60 min, disk first; gallica/openapi.bnf.fr <= 4 only if MAT-NOM's crops are not on disk, ROOM take/release): matignon-mayenne-1586 f.91-92 margin decipherment
Escalation siblings/clear-pages: the f.91-92 Cipher-1 letter with its margin decipherment (Tomokiyo l.638) was located and cropped 15 Oct (MAT-NOM)
but not transcribed. Transcribe the margin gloss (two blind Sonnet passes, one line crop per call, crop step pasted per CLAUDE.md Usage 6, plus one
reconciliation unit), and the cipher it glosses where on the same crops; then say whether f.91-92 is in this target's key (compare to key.tsv,
count matches and conflicts) or Cipher-1, and what pairs it adds as C. Write align/f91/ and NOTES "## MAT-F91"; no key.tsv edit (a merge needs a
per-unit control, CLAUDE.md rule 3 Szembek paragraph). Units: crops 0.3, 2 passes x ~0.6, reconcile 0.6, comparison 0.5, start-up 1.

### C1161-EXC (Opus, cap 3.5, box 60 min, disk only): clair1161-avis-flandre-1688 blind exemplar matching of the 24 unmapped labels
Verdict: "blind exemplar-crop matching of the 24 unmapped labels beside his sheet (two passes, one call per label group), ~$2". Read C1161-S275 and
the sections it cites first. Two blind Sonnet passes, one call per label group, crop paths only (no values), plus one reconciliation unit; PREREG the
agreement rule before the passes. If the source images are not on disk, STOP and say so. Known-text item (N0 faces): residue only, keep under cap.
Units: 2 passes x ~4 groups x ~0.15, reconcile 0.4, start-up 1.

### LVN-4610U (Opus, cap 3, box 60 min, disk only): lodewijk-van-nassau-1573-74 the 9 undecided 4610 rows + p1_L05 head
A4-1236 next 6: the 9 undecided 4610 rows LVN-4610H listed (non-2 misreads) ruled by eye on the disk crops, then p1_L05 head (81/125
untranscribed) if >= 40% cap left. Grades per rule 4; any H -> M or M -> H change carried into AUDIT.md per rule 10's propagation clause and the
C/H share recomputed. Do not touch LVN-NAMES's codes >120 (VIV-KEYSTONE's job). If crops are not on disk, STOP and say so. Units: 9 rows x ~0.1,
p1_L05 head 2 passes + reconcile ~1, start-up 1.
