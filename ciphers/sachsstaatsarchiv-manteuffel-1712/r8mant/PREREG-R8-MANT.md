# PREREG-R8-MANT (6 Oct 2026, written before the blind Sonnet read; R8-MANT, LANE LANE-RUN8-account-4, account 4)

Question: file 0527 (f.422v) run 7, "il n'y eut que [code], dit on, qui parla": is the code 898 or 98, and what gloss sits over it?
Material: URL file 0527.jpg (archiv.sachsen.de, sha256 bfd3ce7d...187d5); crop command
`tools/iiif_lines.py --image 0527.jpg --out z7 --region 860,1580,700,130 --prefix R7 --lines-per-crop 1 --views 3 --debug`
plus PIL zooms of box 870,1585,1200,1665 (3x), 930,1590,1080,1625 (gloss, 5x), 930,1615,1010,1665 (code, 5x).
Reads: (1) the worker's own eye, recorded in this folder before the subagent read is opened; (2) one blind Sonnet subagent, crop paths
only, asked to transcribe the code group digit by digit and every word written above or beside it, with no candidate values given.

Decision rule (fixed now):
- Code: if both reads give three digits, the code stays a three-digit 8x8 group (not 98); the 9/4 middle digit is recorded as both
  reads give it; if the reads disagree on 9 vs 4 the token keeps 898 with a note (the hand writes 4 like y, R7-MANT529).
  If both reads give 98, the gloss "Ilgen" stays and the code is corrected to 98 (agrees with key.tsv 98 Ilgen).
- Gloss: the run-7 gloss in f422v_0527/reconciled.tsv and pairs.tsv is changed only if BOTH reads put the same word directly over the
  code group (interlinear) and put "Ilgen" in the margin, not over the code. Then the interlinear word becomes the run's gloss at
  grade M, and "Ilgen" is noted as a marginal annotation. Otherwise the run is left as read (doubtful, "Ilgen", M).
- If the gloss changes, re-run pooled_mantp/pooled_gate.py --add0529 unchanged (PREREG-MANTP rule, same draws and seed) and apply its
  licensing rule as registered (C only with an occurrence on a cleared leaf and a C-graded gloss; else M). No other code is touched.

## Addendum 1 (6 Oct 2026, after both reads, before any re-run or score)
Outcome of the registered rule: both reads give three digits with middle digit 4 -> code 848 (not 98, not 898). Gloss: both reads put
"Ilgen" in the margin, not over the code, but they disagree on the word over the code (worker "l'Empire", subagent "Alexapice?" low) ->
gloss NOT changed (kept "Ilgen", M, doubtful, now on 848). Comparison (worker, after both reads): the leaf's undisputed 898 on f.422v
L_L05 ("que 898 est ... ", gloss l'Empire, both passes) has a closed-loop 9, like 939 on the next line; run 7's middle digit is open.
The code correction changes the pooled gate's input (run 7 leaves code 898), which the rule above did not foresee: the pooled gate is
re-run with pooled_mantp/pooled_gate.py --add0529 exactly as registered (PREREG-MANTP, seed 7101, 1000 draws), outputs copied to
r8mant/ with suffix _r8 (the committed _0529 outputs restored), and PREREG-MANTP's licensing rule applied unchanged. The 0527 per-leaf
gate (f422v_0527/shuffle_control_0527.py) is re-run too and reported; it does not license anything by itself here.
