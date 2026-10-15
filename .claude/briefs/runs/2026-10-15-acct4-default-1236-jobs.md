# LANE DEFAULT-account-4-20261015-1236 jobs (account 4, lane orchestrator session_01XujJAdRCXr9a3KzuqA9wTH) -- 15 Oct 2026 12:4x UTC

Lane brief: .claude/briefs/default-lane.md. Cap 60, box 12:36-22:36 UTC 15 Oct. Gate 0a: no SESSION-SWEEP-account-4 row.
Backlog = the previous account-4 lane's next list (STATUS.md "LANE DEFAULT-account-4-20261015-1035 handoff", closed 12:03 on budget), each step
re-read from the folder's own latest NOTES.md Verdict. VERIFY-BACKLOG top rows are Birago/ceppo (off limits).
Excluded: live LANE DEFAULT-A1-1140-15 and LANE DEFAULT-A2-1109-15 holdings (both jobs files name these five folders only as excluded), VIV-KEYSTONE
(fr16104/fr16106), BNF-FOCUS, Birago family/ceppo, Armstrong, Debosnys, oldenbarnevelt-brederode-1605 (A2-1109 live), cipher-lab-private.
Intake gate 12:4x UTC (tools/intake_gate_check.py, pass each): clair1161-avis-flandre-1688, fr5761-election-1519, fr4735-monluc-lansac-poland-1573,
matignon-mayenne-1586, baluze167-davaux-1637.

## Common rules for every job
Exactly the "Common rules for every job" section of `.claude/briefs/runs/2026-10-15-acct4-default-0437-jobs.md` (read it in full, and the files it
points to), with these substitutions:
- address every ROOM line "for LANE DEFAULT-A4-1236-15 (account 4)"; export `CIPHERLAB_ACCOUNT=account-4` before any tools/room.py call;
- every claim/halfway/done ROOM line ends "usage: not readable here";
- images never go into git (scratchpad only; commit TSV/MD/scripts);
- no www.googleapis.com in this wave;
- a worker pays ~1 of start-up before its first unit; Opus small jobs ran 1.3-1.5x their estimate today: stop before a unit that would cross 80% of
  cap or box;
- after `tools/room.py --push PATHS`, run `git status` and push any named path it left uncommitted (A4-1035 tool note);
- solver jobs: report what was found and where it was not found; do not classify novelty.

## Wave 1 (12:4x UTC 15 Oct)

### C1161-S275 (Opus, cap 6, box 90 min, disk only): clair1161-avis-flandre-1688 s275 readers + gate K + registered --try on shc/hand.tsv windows
Latest Verdict: "the s275 PREREG readers, gate K and the registered --try on shc/hand.tsv windows (all 275 hand-placed), ~$4". Read C1161-SSPLIT,
C1161-SORT2, C1161-RECUT, C1161-275, C1161-HC and C1161-HC2 sections first. Windows from shc/hand.tsv (disk images only; if the source images are not on
disk, STOP and say so -- do not fetch). Two blind readers in batches (one subagent call per batch of <= 40 windows, crop paths only, no values),
reconciliation as one more priced unit; apply gate K EXACTLY as first registered in C1161-SSPLIT's PREREG. If K passes: So/Sl into the transcription,
the registered --try with its power controls, Sl = n at M; else log and stop. Units: 2 readers x 7 batches x ~0.25 + reconciliation 0.5 + start-up 1.

### ELEC-POOL (Opus, cap 4.5, box 75 min; archive.org <= 20, gallica/openapi.bnf.fr <= 6, ROOM take/release): fr5761-election-1519 Kluckhohn p.857 + pooled name signs
Verdict (ELEC-KLU) next (1)-(3) in order: (1) Kluckhohn p.857 against f.166v l.12-end for further signs (~0.5); (2) a PREREG'd pooled pairing across
the Coblenz-period fr.5761 letters Kluckhohn prints with "die Namen in Chiffren" (find them by his source lines, IA full text "5761"), to bring
oXo, Phi, Hbar, Lfo to >= 3 occurrences each, with a shuffled-name control that can vary on the pairing axis (~2.5); (3) only if >= 30% cap left,
oXo image-to-image vs the f.110 Catholicquer crop if on disk (~0.5). Grades per rule 4; no key edit without --try at every occurrence.

### MONL-K04 (Opus, cap 3, box 60 min, disk only): fr4735-monluc-lansac-poland-1573 K04-for-n --try, then K40/K45 value-blind sort
Verdict: "the K04-for-n --try on the 15 with its power control (~$1.5), then the K40/K45 value-blind sort (~$1)". Read MONL-L21 and MONL-CTL first.
`decode_key.py --try K04=n` at every occurrence with its power control (CLAUDE.md rule 3: the control must be able to differ). Then, if >= 35% cap left,
K40/K45 value-blind sort from disk crops (one subagent call, crop paths only). No key edit unless --try accepts and its control passed.

### MAT-OSPLIT (Opus, cap 4, box 75 min, disk only; gallica <= 6 if crops missing, ROOM take/release): matignon-mayenne-1586 o split + per-shape held-out test
Verdict (MAT-BOX): sort label o into its two shapes (plain o / stemmed o) over f.91 A-F and f.110, blind (crop paths only, no values), PREREG the
relabel test before scoring, then the MAT-KA block-held-out test per shape with its control. Read MAT-KA, MAT-EYE, MAT-BOX first. Grade M unless the
registered test passes; carry any grade change to AUDIT.md (rule 10). Units: sort ~1 (one call per <= 40 crops) + test ~1 + start-up 1.

### BAL-65G (Opus, cap 3, box 60 min; openapi.bnf.fr <= 8, ROOM take/release): baluze167-davaux-1637 glossed plain 65 on 169 c297/c232/c344 + Ebar re-check
Verdict cheapest next: (1) 169 c297, c232, c344 for a glossed plain 65 (~1; one region each at full res, scratch only); (2) the c281/c284/c267 E rows
re-checked for the Ebar form (~3 requests at 2400 px, record regen in images/manifest.json, ~0.8). --try before anything enters key.tsv.

Wave 1 spawned 12:43 UTC: C1161-S275 session_01DZ396T7SNCopDQYgyjzMpE, ELEC-POOL session_018ivXv18LBWy8VERLakdFPt, MONL-K04 session_01BLJnJAjibyEny4sN852o2U,
MAT-OSPLIT session_01TSeH8rDaQSB6d7UbeTGzcd, BAL-65G session_01BWPzuRzQAtJaPzPcwmkTeY (all Opus; caps 6/4.5/3/4/3 = 20.5).
