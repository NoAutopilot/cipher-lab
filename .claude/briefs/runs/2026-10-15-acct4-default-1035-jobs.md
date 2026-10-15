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

## Wave 1 result (11:0x UTC): LVN-P2K 4.91 D, C1161-275 3.05 N (localiser gate L2 FAIL, stopped as registered), BAL-13X 3.22 D, GRA-3038 1.71 N. Workers 12.89.

## Wave 2 (11:1x UTC 15 Oct)
LANE DEFAULT-A1-0740-15 closed 10:49 and LANE DEFAULT-A2-0810-15 closed 10:15, so their folders are open to this lane; their handoffs' "next" lists
in STATUS.md are the source of jobs 4-6. Intake gate 11:05 UTC, pass each: matignon-mayenne-1586, fr4735-monluc-lansac-poland-1573, fr5761-election-1519.

### LVN-K15 (Opus, cap 3, box 60 min, disk; resources.huygens.knaw.nl <= 3): lodewijk-van-nassau-1573-74 K15 second row, 18/39 re-seat, flat-foot 2
LVN-P2K's next (NOTES.md LVN-P2K section): the K15 85 M second row, the 18/39 re-seat and the positional-differs pairs (~1.5); then the eye check of
4610 H tokens ending in the flat-foot 2 (~0.3), verifier-style ruling kept/changed/undecided. Changes through the corrections path + decode_key
--check; carry every grade change into AUDIT.md (rule 10). Do not repeat LVN-P2K's rulings.

### C1161-HC (Opus, cap 5, box 90 min, disk only): clair1161-avis-flandre-1688 hand-counted S ticks per line, then the registered sort
C1161-275's next: hand-counted ticks per S line (c187L/c188L first) to replace the automated localiser that failed L2 (18/30). This is a different
instrument (counting by eye per line), so it is not a third attempt of the same one; write that in the PREREG. Order: hand-count c187L/c188L first and
re-run the L2 eye check (same 30-window sample design, same gate 26) on them; only if L2 passes on the hand-counted lines extend to the rest, then
gate K exactly as first registered, two blind readers in batches (crop paths only, <= 40 windows per call), reconciliation as one priced unit. If L2
fails again, stop and log the localisation step [retired] with both instruments named. Units: counting ~0.15 per line x lines + readers as C1161-275.

### MAT-BOX (Opus, cap 3, box 60 min, disk; openapi.bnf.fr <= 4, ROOM take/release): matignon-mayenne-1586 --try BOX=u on f.110, o/c image check
A2-0810 handoff next: `decode_key.py matignon-mayenne-1586 --try BOX=u` on f.110 (125 U tokens, 5/5 eyed as the BOX2 shape by MAT-EYE) with --try's own
power control (a known wrong value on an H code must be rejected; if the control fails the try is a non-test and nothing enters key.tsv); PREREG
first. Then the image check of the o and c labels (~1). Every leaf's judge before/after.

### MONL-L21 (Opus, cap 4.5, box 90 min, disk; openapi.bnf.fr <= 3 to regenerate crops, ROOM take/release): fr4735-monluc-lansac-poland-1573 c268 L21-L25
A1-0740 next 1: c268 L21-L25 as its own job: line crops with tools/iiif_lines.py (paste the command) or the folder's regen scripts, two blind passes
+ reconciliation (3 units at ~1 each + start-up 1), same method and controls as the L16-L20 read (MONL-K04 / MONL-CTL sections). Then, only if >= 30%
cap is left, the K04-for-n --try on the 11 left with its power control.

### ELEC-383 (Opus, cap 3, box 60 min, disk; gallica/openapi.bnf.fr <= 10, ROOM take/release): fr5761-election-1519 nr. 383 bisection
A1-0740 next 2: nr. 383 bisection back from fr.5761 f.172 (~2), by the method ELEC-PAIR / the nr. 357 localisation used (read those NOTES.md sections
first). Locate, crop (scratchpad), record shelfmark/canvas and any printed counterpart page; pair against print only if found and >= 40% cap left.

### BAL-302 (Opus, cap 2.5, box 60 min, disk; openapi.bnf.fr <= 4, ROOM take/release): baluze167-davaux-1637 c302 65 stroke + c276 E shape
BAL-13X's unfinished steps: c302 at max for the second unsettled 65 stroke (plain 65 or 65'), and the c276 R16 "d'une" E shape (epsilon or Ebar),
one request each; then the c281/c284/c267 E rows re-checked for the Ebar form from disk. Grades only through --try / corrections path.

Wave 2 spawned 11:07 UTC (all Opus): LVN-K15 session_01WnnJ9pzDt8fH7hThJqb9Qq, C1161-HC session_016YqJHBfHfmBde2Ev3yP1ad, MAT-BOX session_01JhUAPckKoKXE2bx7zekheM,
MONL-L21 session_01RTGPs8zcLH2bZbB74BR7tg, ELEC-383 session_012L9kaYq2URo6Scnrt63kyU, BAL-302 session_015zwNFFyQ8tmh2t8P5vRuwf. Wave 1 sessions archived.

## Wave 2 result (11:3x UTC): LVN-K15 4.42 D, C1161-HC 4.51 D (hand count L2 29/30 PASS), MAT-BOX 4.19 N (BOX=u reject), ELEC-383 2.92 D, BAL-302 2.45 N;
MONL-L21 running. Overruns 1.40-1.47x again: wave 3 caps are set at ~1.5x the unit estimate and workers stop at 80% of them.

## Wave 3 (11:4x UTC 15 Oct) -- last wave
Intake gate oldenbarnevelt-brederode-1605 11:05 UTC pass.

### C1161-HC2 (Opus, cap 4.5, box 75 min, disk only): clair1161-avis-flandre-1688 hand count of the remaining 62 S lines
C1161-HC's next: hand-count the remaining 62 lines (149 S) by the same per-piece method into shc/hand.tsv, then the L2 eye check on a fresh 30-window
sample drawn from these lines (same design, gate 26). Stop there: readers, gate K and --try are the next job, not this one.

### ELEC-KLU (Opus, cap 3.5, box 60 min, openapi.bnf.fr <= 4; archive.org/be-api <= 10, ROOM take/release): fr5761-election-1519 nr. 383 start + print pair
ELEC-383's next: c334-c335 + f.166v at 2400 px (find the letter's start, f.165v-166r), then Kluckhohn's n863-n864 pairing under ELEC-PAIR's rule
(shuffle control, both-sided pairs only). archive.org is allowed for this job (good-citizen rule: 1.5 s apart, one at a time).

### BAL-PCT (Opus, cap 2, box 40 min, openapi.bnf.fr <= 2, ROOM take/release): baluze167-davaux-1637 the two measured regions
BAL-302 recorded measured boxes: c302 pct:37,40,10,5/max and c276 pct:53,78.5,8,5/max. One request each; rule the c302 65 stroke (plain 65 or 65')
and the c276 R16 E (epsilon or Ebar). Grades only through --try / the corrections path.

### OBRED-TRY2 (Opus, cap 4, box 60 min, disk only): oldenbarnevelt-brederode-1605 context --try on the 20 Dutch word leads
A2-0810 handoff next: the 20 nl16 word leads from OBRED-SEG (all M) tested in context: a pre-registered --try (or the folder's equivalent) per lead
at every occurrence, with a power control that must reject a known wrong value before any lead is accepted; accepted leads stay M unless the control
licenses S. Read OBRED-SEG/OBRED-BAND sections first.

### VER-LVN3 (Opus, cap 2, box 45 min, disk; resources.huygens.knaw.nl <= 2): lodewijk-van-nassau-1573-74 verifier for LVN-K15's three named rows
Verifier hat, not the solver's session: K16/18, K30/15 (moved to undecided after the decode was seen) and K31/14 81 H. One crop each beside the H
exemplars, ruling kept/changed/undecided; changes through the corrections path + decode_key --check; carry into AUDIT.md (rule 10).

Wave 3 spawned 11:35 UTC (all Opus): C1161-HC2 session_01EUR1kYw7sCgZ5ipdgYatPe, ELEC-KLU session_01MxQnH7iB48f6vKYRD8Cxsq, BAL-PCT session_01Qg6ZynHb1kxgcJ5yMtg84v,
OBRED-TRY2 session_01AQKNNThwoctkiovEK5nvJA, VER-LVN3 session_017nKocXNb4sk4JWnubdEEon. Wave 2 archived except MONL-L21 (running).
