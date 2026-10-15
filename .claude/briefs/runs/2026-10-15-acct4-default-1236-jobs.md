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

## Wave 1 result (13:0x UTC): C1161-S275 7.99 D (Sl=n accept +1113.2, M), ELEC-POOL 2.80 N (pool empty), MONL-K04 1.98 D (lead only), MAT-OSPLIT
3.92 N (split FAIL), BAL-65G 3.92 N. Workers 20.62. clair1161 held this wave (N0 face text; known-text share).

## Wave 2 (13:1x UTC 15 Oct)
Intake gate 13:07 UTC: lodewijk-van-nassau-1573-74 pass (the other four passed at 12:4x).

### MONL-K14 (Opus, cap 4.5, box 75 min; openapi.bnf.fr <= 12, ROOM take/release): fr4735-monluc-lansac-poland-1573 K14/K34-for-s, K62-for-m --try, then K04|K12 + K40/K45 sort
Latest Verdict (MONL-K04): (1) the K14/K34-for-s and K62-for-m pseudo-code --try with controls (disk only, ~0.5 each; same design as MONL-K04's
PREREG d15cebaf1: n-facing target, power control, wrong-facing control); (2) then, if >= 40% cap left, regen_monll11/16/21.sh (fetch only what
those scripts name, scratch only) and the K04|K12 + K40/K45 value-blind sort in one job (one subagent call per <= 40 tiles, crop paths only), ~2.
Leads only unless --try accepts with its controls passed; no key edit otherwise.

### BAL-65L (Opus, cap 3.5, box 60 min; openapi.bnf.fr <= 12, ROOM take/release): baluze167-davaux-1637 plain 65 below line 9 on 169 c179/c180/c183/c184/c187, then 168/170
Latest Verdict (BAL-65G): c179, c180, c183, c184, c187 below line 9 line by line (on BAL-169's fetch list, ~1), then, if none and >= 40% cap left,
the same-hand glossed letters in Baluze 168/170 for a plain 65 (~1.5; find them from NOTES.md/the catalogue first, one region per canvas). If a
glossed plain 65 is found: --try at every occurrence with its control before anything enters key.tsv.

### LVN-4610H (Opus, cap 3, box 60 min, disk only): lodewijk-van-nassau-1573-74 the rest of 4610's H tokens ending in 1 or 8
Latest Verdict: "next: the rest of 4610's H tokens ending in 1 or 8, ~$1.5" (the flat-foot 2 confusion LVN-K15 found on p1_L04/L09). Read LVN-K15,
LVN-EYE and VER-LVN3 first. Eye each token on the 300 dpi line crops (crop step pasted, tools/iiif_lines.py --image), ruling kept/changed/undecided
per token, changes through the folder's corrections path + decode_key.py --check; carry every grade change into AUDIT.md (rule 10). Units: tokens in
batches of ~15 at ~0.4 + 1 start-up.

### ELEC-VERSO (Opus, cap 4, box 75 min; gallica/openapi.bnf.fr <= 10, ROOM take/release): fr5761-election-1519 Coblenz versos ff.160-165 + f.51r-53r key compare
Verdict (ELEC-POOL) next (1)-(2): (1) image check of the versos of ff.160-165 at 1000 px (~6 canvases, ~1.5) for name signs Kluckhohn did not
flag; (2) compare oXo, Phi, Hbar, Lfo with the f.51r-53r keys (c105-c109 on disk, ~1). Then, only if >= 30% cap left, (3) fr.3897 Joachim items
36-38 for second witnesses (ELEC-PAIR next 3). All M unless a registered pairing with a control that can vary on the pairing axis passes.

### MAT-O3X (Opus, cap 3, box 60 min, disk only; gallica <= 6 if crops missing): matignon-mayenne-1586 o split re-sort on 3x per-token crops
MAT-OSPLIT next: 3x per-token crops of the 78 f.91 o tokens (fix MAT-OSPLIT's 6 X join errors first), blind re-sort (crop paths only, no values),
re-run mat_osplit.py under the SAME PREREG ee2c00674 gate. This is the second attempt at this split: if it fails again, log it and hand the o
split to the owner's sign sorter as the next step (rule 3: no third machine attempt).

Wave 2 spawned 13:09 UTC: MONL-K14 session_01Ceamd3rTT2QY8cezSDifK3, BAL-65L session_01GVPDmXM11HgQnRDDELxyaD, LVN-4610H session_01AQvZdQD2ubyHt2yzfmEz7q,
ELEC-VERSO session_01PFKu5WgiukffCMR1c6Wq3R, MAT-O3X session_016uPs7XyaqXeRUYtYqPgM13 (all Opus; caps 4.5/3.5/3/4/3 = 18).

## Wave 2 result (13:3x UTC): MONL-K14 1.78 D (K14=s lead), BAL-65L 4.01 N, LVN-4610H 5.42 D (2 H->M, 1.81x), ELEC-VERSO 3.07 D (four signs match f.51r
block 5/5, single reader M), MAT-O3X 4.71 D (split PASS 30/50 vs p95 20 on 3x crops, candidate S). Workers 18.99; lane workers 39.61.

## Wave 3 (13:3x UTC 15 Oct; last wave, sized to the remaining budget)

### MAT-R2 (Opus, cap 1.5, box 40 min, disk only): matignon-mayenne-1586 second blind reader on MAT-O3X's 78 3x o crops
MAT-O3X next: a second, independent blind reader (one Sonnet call, crop paths only, no values, no first-reader labels) on osplit/o3x crops;
agreement with MAT-O3X's sort (A/B/X) and kappa, written under a PREREG addendum committed before the call. Re-run mat_osplit.py under the same gate
on the second reader's labels. No key/label/reading edit; record in HYPOTHESES.md and NOTES.md. Do NOT start the 13-leaf relabel.

### ELEC-R2 (Opus, cap 2, box 45 min, disk + openapi.bnf.fr <= 4, ROOM take/release): fr5761-election-1519 blind second reader on the f.51r block + its note
ELEC-VERSO next: a blind second reader (one subagent call, crop paths only, no ELEC-VERSO matches shown) matching the four nr. 383 signs (oXo, Phi,
Hbar, Lfo) against the f.51r lower block rows and the side note (Orval?), under a PREREG addendum before the call, with a decoy-row control that can
vary on the matching axis. All M unless the registered rule says otherwise; key.tsv unchanged unless --try at every occurrence accepts.

### MONL-SORT (Opus, cap 3.5, box 60 min; openapi.bnf.fr <= 12, ROOM take/release): fr4735-monluc-lansac-poland-1573 regen + one value-blind sort
MONL-K14 next: regen_monll11/16/21.sh (fetch only what they name, scratch only), then ONE value-blind sort of K04|K12 + K14|K37 + K40/K45 tiles (one
subagent call per <= 40 tiles, crop paths only), with the in-band controls MONL-CTL used; PREREG addendum before the call. Relabels only by the
registered rule; decode_key/align/score --check after.

Wave 3 spawned 13:33 UTC: MAT-R2 session_01Coxngskfb3yt89gN9hySCb, ELEC-R2 session_012M6RzZ7dgZMDMhQy9XYfhd, MONL-SORT session_01VMJiqXX4GdfmxQdmRmeoCg (all Opus; caps 1.5/2/3.5 = 7).
