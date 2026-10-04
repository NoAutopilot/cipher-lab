# PREREG kp86g -- fr16045 f.247r (second 17 Sept 1586 letter) per-line pass vs Colbert 16 pt II p.54-55 (PIS1-247, 4 Oct 2026)

Written and pushed before any blind pass of f.247r and before any decode. Same instrument as kp86e/kp86f (kp86d/kp86d.py
unchanged through a thin wrapper, kp86g/kp86g.py = kp86f/kp86f.py with file paths changed only): nothing in the statistic,
nulls, seeds, arms, control or gate changes; only the page and its copy span.

Material.
- Cipher: fr.16045 f.247r = Gallica btv1b9060906j canvas 506 (3925 x 5777). Native region 550,1180,2800,1600 fetched once
  (scratch, not committed; re-fetch `https://gallica.bnf.fr/iiif/ark:/12148/btv1b9060906j/f506/550,1180,2800,1600/full/0/native.jpg`).
  The block has **9 cipher lines** (PIS1-INV's "~10" was a 360 px estimate), then clear "Nous sommes prests d'aller a
  l'audience Monsieur le cardinal, Monsieur de Luxembourg et moy, ou ie ne feray semblant de ce que dessus", then the
  closing and the date "De Rome ce 17e 7bre 1586". No clear words inside the cipher block: --inms not used.
- Crops: `python3 tools/iiif_lines.py --image <scratch>/src_c506.jpg --out ciphers/fr16045-pisany-rome-1585/images --prefix f247rL --debug --max-width 1600 --overlap 100 --centres 133,287,462,637,798,966,1141,1281,1456 --follow-slope 400 --slope-local --slope-margin 20`
  then L01, L07 (slope fits jumped: intercepts 208 and 1275 vs centres 133 and 1141) and L03 (s2 drifted toward L04 on the
  montage) re-cut fixed-y: same command without the slope options, `--only-lines 1,7` and `--only-lines 3`. Montage of all
  18 crops checked by eye: each crop's middle row holds its own line.
- Clear copy (primary known answer): kp86g/colbert_f247r.txt = Colbert 16 pt II p.54 l.16 "Je n'ay sceu respondre" to p.55
  "...du Cardinal de Saincte Croix." (read by this worker from c446 at 1400 px; one doubtful word "auec qu'elle?"). The span
  starts earlier than the page needs (~900 copy letters for ~400 cipher signs) because f.247r's first word is not known
  before decoding; nw_score is semi-global with free leading/trailing gaps on the clear side, as on every earlier page.
- Second witness: kp86g/dechiffre_f248.txt = the period decipherment f.248v (c509) lines 10-20, read by this worker from the
  native region 1100,1900,2825,1450. Witness comparison done BEFORE this PREREG, on the overlap "J'ay les mains liees ...
  Saincte Croix" only, both normalised to one convention (CLAUDE.md rule 3 PX-BRODEC: bracketed abbreviation letters
  expanded, lower case, letters only, j->i, v->u, y->i): 367 vs 369 letters, 362 matched by difflib = **0.986 / 0.981**.
  Caveat: the same worker read both, and the faint f.248v hand was read with the Colbert wording in view, so this agreement
  is an upper bound, not an independent measure. Colbert stays the scored text; the f.248v text is not scored separately
  (its earlier lines, covering p.54 l.16 - p.55 l.8, were not read in this job).
- Keys: arm A key86.tsv as published (blob 1085fcac, unchanged at HEAD 0ce7890d; PIS1-KEY has not landed a cell change, no
  done line at 17:3x UTC); arm B key86 + RUN4-PIS1 remap (T31->o, T45->u, T47->f, T57->n), beside A only.

Transcription: two blind Sonnet readers (A, B), tx86g/PASS_BRIEF86g.md (= tx86f's brief with page names changed), ONE
subagent call per line per reader (9 + 9 = 18 calls), each given only that line's two crops and tx86g/SIGNSHEET86.png.
Replies verbatim to tx86g/lines/A_Lnn.txt, B_Lnn.txt, assembled to tx86g/passA.tsv, passB.tsv. A reply that is not a label
row is re-asked once; the second reply stands.
Reconciliation: `python3 tools/reconcile_passes.py tx86g/passA.tsv tx86g/passB.tsv --out-dir tx86g` then
`python3 kp86d/reconcile_d.py tx86g` (RUN3 shape rules, unchanged; it writes tx86g/ciphertext_f275r.tsv, renamed to
tx86g/ciphertext_f247r.tsv). err_2reader = 1 - agree share from reconcile_passes.py.

Test: `python3 kp86g/kp86g.py --err <measured err_2reader>` = kp86d/kp86d.py UNCHANGED (nw_score; key-shuffle 1000 and
order-shuffle 1000 nulls, p99; seeds as kp86d; positive control at the measured err, 5 seeds, 200/200 nulls, pass >= 4/5)
-> kp86g/kp86g_result.json.
Gate per arm (as kp86d/e/f): PASS if the reconciled target > p99 of both nulls AND that arm's control passes; control fails
-> NON-TEST; target fails at err > 0.10 with the control passing -> FAIL at that e (not a refutation of the table).
Blind A and B scored too (not gating).

Grades (rule 4): only if arm A is a licensed PASS, decoded letters aligned identically to the copy are C, the rest M; T31
tokens M (HYPOTHESES.md data conflict) -- via kp86e/t31_grades.py through a thin wrapper that changes only file paths. If
NON-TEST or FAIL, every token stays M. `tools/decode_key.py ... --check`; judge pasted. No parameter changes after the
first run.
