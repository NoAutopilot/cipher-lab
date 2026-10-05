# PREREG kp86h -- fr16045 f.275v block B lines 12-15 + full-page re-test vs Colbert 16 pt II pp.122-123 (RUN6-PIS, 5 Oct 2026)

Written and pushed before any blind pass of these four lines and before any decode. Same instrument as kp86f (PASS on f.275v
lines 1-16): statistic, nulls, seeds, arms, control and gate unchanged; only the transcription grows by four lines.

Material.
- Cipher: fr.16045 f.275v = Gallica btv1b9060906j canvas 563. Native region 1070,3900,2760,1250 fetched once (scratch, not
  committed; re-fetch `https://gallica.bnf.fr/iiif/ark:/12148/btv1b9060906j/f563/1070,3900,2760,1250/full/0/native.jpg`;
  x 1070 = kp86f's block-B sub-image left edge 950+120). Region y 80 = block B line 10, y 246 = line 11 (kp86f's centres
  1570/1756 + 2390), so lines 12-15 sit at about 390/560/740/910; the clear "a laquelle elle porte toute affection" follows.
- Crops: `python3 tools/iiif_lines.py --image <scratch>/srcB2_c563.jpg --out ciphers/fr16045-pisany-rome-1585/images --prefix f275vB2 --debug --max-width 1600 --overlap 100 --centres 390,560,740,910 --follow-slope 400 --slope-local --slope-margin 20`
  (slope fits 402/592/746/898; drift -15/-26/-3/+51 px). Montage of the 8 crops checked by eye: each crop's middle row is its own
  line. Line ids: L17-L20 = f275vB2_L01-L04 (block B lines 12-15), continuing kp86f's L01-L16.
- Clear copy: kp86h/colbert_f275v.txt = kp86f/colbert_f275v.txt byte for byte (it already runs to "seureté d'icelle", the end of
  the page's span). In-clear phrase (control plaintext only), as kp86f: --inms = the exact copy substring from "ou je suis que je
  ne la sors" to "je dis au Pape," (one string, as in the copy file).
- Keys: arm A key86.tsv as published (blob unchanged); arm B key86 + RUN4-PIS1 remap, beside A only.

Transcription: two blind Sonnet readers (A, B), the brief and sign sheet of kp86f copied unchanged (tx86h/PASS_BRIEF86f.md,
tx86h/SIGNSHEET86.png = tx86f's, md5 bc3420515e0e...), ONE subagent call per line per reader (4 + 4), prompt by
tx86h/make_prompt.sh, each given only that line's two crops and the sheet. Replies verbatim to tx86h/lines/A_Lnn.txt, B_Lnn.txt.
A reply that is not a label row is re-asked once; the second reply stands.
Assembly: tx86h/passA.tsv = tx86f/passA.tsv (L01-L16, unchanged) + the 4 new A rows; same for B. tx86h/local_passA.tsv /
local_passB.tsv = the 4 new rows only.
Reconciliation: `python3 tools/reconcile_passes.py tx86h/passA.tsv tx86h/passB.tsv --out-dir tx86h`, then
`python3 kp86d/reconcile_d.py tx86h` (unchanged) -> tx86h/ciphertext_f275r.tsv, renamed tx86h/ciphertext_f275v.tsv;
tx86h/local_ciphertext.tsv = its L17-L20 rows. err_2reader = 1 - agree share on the full page (gating); the L17-L20-only
agreement is reported beside it.

Test 1 (gating, = kp86f on the whole page): `python3 kp86h/kp86h.py --err <full-page err_2reader> --inms "<phrase>"` =
kp86d/kp86d.py UNCHANGED (nw_score; key-shuffle 1000 and order-shuffle 1000 nulls, p99; seeds as kp86d; positive control at
the measured err, 5 seeds, 200/200 nulls, pass >= 4/5) -> kp86h/kp86h_result.json.
Gate per arm (as kp86d/e/f): PASS if the reconciled target > p99 of both nulls AND that arm's control passes; control fails ->
NON-TEST; target fails at err > 0.10 with the control passing -> FAIL at that e.
Test 2 (local, gating for the new lines' grades only): `python3 kp86h/kp86h.py --local --err <same err> --inms "<phrase>"`, the
same wrapper and kp86d.main() on the L17-L20 tokens alone against the same copy; control N = the local decoded-letter count.
Same gate. A full-page PASS alone is mostly inherited from L01-L16, so it does not license C on L17-L20.

Grades (rule 4): if Test 1 arm A PASSes, the full page is regraded by kp86f/grades_f275v.py with paths changed (kp86h/grades_f275v_h.py
-> kp86h/grades_f275v.tsv): decoded letters aligned identically to the copy are C, the rest M; T31 tokens M. Tokens on L17-L20 are
C only if Test 2 arm A also PASSes; otherwise every L17-L20 token is M. Test 1 NON-TEST or FAIL: the committed kp86f grades and
reading stand, and the new lines are M. reading_f275v_M.txt / _tokens.tsv regenerated from tx86h/ciphertext_f275v.tsv by
tools/decode_key.py only on a Test 1 PASS; `--check`; judge pasted. No parameter changes after the first run.
