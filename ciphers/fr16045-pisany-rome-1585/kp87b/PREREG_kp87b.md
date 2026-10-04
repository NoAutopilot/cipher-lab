# PREREG kp87b -- fr16045 f.302v (24 Mar 1587) cipher vs its Colbert 16 pt II clear copy pp.341-342 (PIS1-302, 4 Oct 2026)

Written and pushed before either blind pass of f.302v is started and before any decode of these lines.

Material.
- Letter: 24 Mar 1587, fr.16045 f.297-303 (canvas = 2 x folio + 12). Cipher on f.301v (kp87a, PASS) and f.302v (c617, this test).
- Cipher: Gallica btv1b9060906j canvas 617 (native 3924x5904), region 1380,2080,2544,1720 fetched once to scratch
  (re-fetch: https://gallica.bnf.fr/iiif/ark:/12148/btv1b9060906j/f617/1380,2080,2544,1720/full/0/default.jpg). 11 lines:
  L01 = clear "qui ne qu'elle commandera" then cipher; L02-L11 cipher; L11 is the last line of the block (the next line opens
  in clear "Pour l'Indult"). Crops (centres by eye on a 50-px grid; montage checked: every crop's middle row holds its line):
  `python3 tools/iiif_lines.py --image <scratch>/src_c617_1380_2080_2544_1720.jpg --out ciphers/fr16045-pisany-rome-1585/images --prefix f302v --debug --max-width 1600 --overlap 100 --centres 80,210,380,500,660,830,990,1130,1280,1410,1590 --follow-slope 400 --slope-local --slope-margin 20`
  then L10 fixed-y (its slope fit jumped onto L09): the same command with `--only-lines 10` and no slope options.
- Clear copy: Melanges de Colbert 16 pt II (btv1b100341061) c589 p.341 l.19 "Il m'a bien asseure ... commandera." to c590
  p.342 l.11 "Pour l'Indult qu'elle m'a commande pourchasser", read by this worker at 1400 px: kp87b/colbert_p341_342.txt. The
  cipher's plaintext is expected to be p.341 l.20 "Je suis le plus trompe homme du monde" to p.342 l.10 "si je ne l'en
  advisois." (the copy's clear text on both sides matches the original's clear text; the margin gloss opens "Je suis le plus
  trompe homme"). The brief's inference "pp.339-341" was wrong: c588 p.339 l.4 onward is the Montmorency and Rusticucci
  paragraphs, f.302r's clear text.
- Margin gloss (second witness): native region 380,2200,1100,1600 of c617, read by this worker before any pass:
  kp87b/gloss_f302v.txt (literal, struck words and doubtful letters marked) and kp87b/gloss_f302v_expanded.txt (abbreviations
  expanded -- Mrs -> Messieurs, po(ur) -> pour, vre Mate -> vostre Maieste -- struck words dropped; spelling kept). Both texts
  go through kp86.norm (one convention) before any score. Noted before scoring: the gloss reads "qu'il a mo?ins?" where the
  copy has "qu'il a plus", and omits "sinon" (possibly lost at the margin edge).
- Keys: arm A = key86.tsv (Tomokiyo 1586-87, published) unchanged; arm B = key86 + kp86d.REMAP_B (PIS1 remap) beside it.

Transcription: two blind Sonnet readers, ONE LINE PER SUBAGENT CALL (each call gets only that line's s1/s2 crops and
tx87b/SIGNSHEET86.png, copied unchanged from tx87), brief tx87b/PASS_BRIEF87b.md; 11 lines x 2 readers = 22 calls. Each call
writes one row (tx87b/rowsA|rowsB/Lnn.tsv); rows are concatenated in line order into tx87b/passA.tsv and passB.tsv with no edit.
Reconciliation: tools/reconcile_passes.py (--out-dir tx87b), then kp86d/reconcile_d.py tx87b (RUN3 rules, unchanged) ->
tx87b/ciphertext_f275r.tsv (the script's fixed output name), copied to tx87b/ciphertext_f302v.tsv. No sign-by-sign judgement.
err_2reader = 1 - agree share from reconcile_passes.py.

Statistic, nulls, decode rule, positive control and gate: kp87a/kp87a.py UNCHANGED, called by kp87b/kp87b.py (committed with
this file) once per arm with --clear kp87b/colbert_p341_342.txt, --inms "Il m'a bien asseure de n'y faire autre chose que ce
qu'elle commandera." "Pour l'Indult qu'elle m'a commande pourchasser", --err = measured err_2reader. Nulls: key-shuffle 1000,
order-shuffle 1000 (tools/stream_align.nw_score); control: kp86d.control (5 seeds, 200/200 nulls, pass >= 4/5).
Gate (arm A decides): PASS if the reconciled target > p99 of both nulls AND the control passes. Control fails -> NON-TEST.
Target fails at err > 0.10 with the control passing -> FAIL at that e, not a refutation of the table. Blind A and B scored too
(not gating). Arm B is reported beside A; nothing enters key86.tsv from this test.
Gloss witness (not gating, reported): W1 = nw_score(gloss, copy) vs 1000 order-shuffles of the gloss letters (p99); W2 =
kp86.test(reconciled tokens, key86, gloss) with key-shuffle/order nulls. The gloss is a period decipherment on the leaf: it can
corroborate the copy, but C grades come from the copy alignment only.
Grades: if arm A PASSes, decoded letters aligned identically to the copy are C (kp87a/cgrades87.py logic, paths changed, in
kp87b/cgrades87b.py), the rest M; if not PASS, all M. Any key86 cell the alignment contradicts is noted in HYPOTHESES.md (T31
stays M unless settled by the copy). No parameter changes after the first run.
