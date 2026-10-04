# PREREG kp86f -- fr16045 f.275v (4 Nov 1586) per-line pass vs Colbert 16 pt II pp.122-123 (PIS1-275V, 4 Oct 2026)

Written and pushed before any blind pass of f.275v and before any decode. Same instrument as kp86e (PASS on f.275r):
nothing in the statistic, nulls, seeds, arms, control or gate changes; only the page and its copy span.

Material.
- Cipher: fr.16045 f.275v = Gallica btv1b9060906j canvas 563 (3925 x 5906). Native region 950,950,2975,3650 fetched once
  (scratch, not committed; re-fetch `https://gallica.bnf.fr/iiif/ark:/12148/btv1b9060906j/f563/950,950,2975,3650/full/0/native.jpg`).
  The page holds two cipher blocks: block A, 5 lines (after 4 clear lines at the head of the page, which are a period
  decipherment in a smaller hand, with more of it in the left margin); then 4 lines of clear ("que je ne la sors qu'a demy
  ... je dis au Pape"); block B, 15 lines, the first opening with the clear word "touchant"; then the clear "a laquelle elle
  porte toute affection ...". 20 cipher lines > 18, so per the brief the first 16 are read: block A L01-L05 and block B
  lines 1-11 (= L06-L16 here). Block B lines 12-15 are left to Remaining gaps.
- Sub-images (scratch) cut from the region: block A = (120,0,2760,830), block B = (120,1440,2760,3400).
- Crops (centres by eye on a 50 px grid, the auto-detector merged lines):
  `python3 tools/iiif_lines.py --image <scratch>/blkA_c563.jpg --out ciphers/fr16045-pisany-rome-1585/images --prefix f275vA --debug --max-width 1600 --overlap 100 --centres 95,265,410,570,725 --follow-slope 400 --slope-local --slope-margin 20`
  `python3 tools/iiif_lines.py --image <scratch>/blkB_c563.jpg --out ciphers/fr16045-pisany-rome-1585/images --prefix f275vB --debug --max-width 1600 --overlap 100 --centres 90,265,415,590,760,930,1095,1260,1410,1570,1756 --follow-slope 400 --slope-local --slope-margin 20`
  then block B line 5 fixed-y (its band's centre row fell between two lines): same command with centre 785 for line 5,
  no slope options, `--only-lines 5`. Montage of all 32 crops checked by eye: each crop's middle row is its own line.
  Line ids: L01-L05 = f275vA_L01-L05; L06-L16 = f275vB_L01-L11.
- Clear copy: kp86f/colbert_f275v.txt = kp86d/colbert_p121_123.txt from "ne le me communiquer" to "seureté d'icelle"
  (one paragraph, line break removed), checked by eye against Colbert c480 at 1400 px (pp.122-123) in this job.
  In-clear on the page (removed from the control's plaintext only, kept in the scored copy, as kp86d's CLEAR_IN_MS):
  --inms "ou je suis que je ne la sors ... je dis au Pape," (the exact substring in the copy file, 4 lines of clear).
- Keys: arm A key86.tsv as published; arm B key86 + RUN4-PIS1 remap (T31->o, T45->u, T47->f, T57->n), beside A only.

Transcription: two blind Sonnet readers (A, B), tx86f/PASS_BRIEF86f.md, ONE subagent call per line per reader (16 + 16),
each given only that line's two crops and tx86f/SIGNSHEET86.png, plus a note where clear handwriting is on the line (L05
ends in clear "ou ie suis"; L06 starts with clear "touchant"). Replies verbatim to tx86f/lines/A_Lnn.txt, B_Lnn.txt,
assembled to tx86f/passA.tsv, passB.tsv. A reply that is not a label row is re-asked once; the second reply stands.
Reconciliation: `python3 tools/reconcile_passes.py tx86f/passA.tsv tx86f/passB.tsv --out-dir tx86f` then
`python3 kp86d/reconcile_d.py tx86f` (RUN3 shape rules, unchanged) -> tx86f/ciphertext_f275v.tsv (renamed from the
script's output if it names the file for f.275r). err_2reader = 1 - agree share from reconcile_passes.py.

Test: `python3 kp86f/kp86f.py --err <measured err_2reader> --inms "<the phrase above>"` = kp86d/kp86d.py UNCHANGED
(nw_score; key-shuffle 1000 and order-shuffle 1000 nulls, p99; seeds as kp86d; positive control at the measured err,
5 seeds, 200/200 nulls, pass >= 4/5) -> kp86f/kp86f_result.json.
Gate per arm (as kp86d/kp86e): PASS if the reconciled target > p99 of both nulls AND that arm's control passes; control
fails -> NON-TEST; target fails at err > 0.10 with the control passing -> FAIL at that e (not a refutation of the table).
Blind A and B scored too (not gating).

Grades (rule 4): only if arm A is a licensed PASS, decoded letters aligned identically to the copy are C, the rest M; T31
tokens M (HYPOTHESES.md data conflict) -- via kp86e/t31_grades.py if it takes the page's files as arguments, else a thin
wrapper that changes only file paths. If NON-TEST, every token stays M. `tools/decode_key.py ... --check`; judge pasted.
The period gloss in the margin is not scored in this job (Remaining gaps). No parameter changes after the first run.
