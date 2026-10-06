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
