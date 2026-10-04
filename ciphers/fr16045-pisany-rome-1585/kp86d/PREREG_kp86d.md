# PREREG kp86d -- fr16045 f.275r (4 Nov 1586) cipher vs its Colbert 16 pt II clear copy pp.121-123 (RUN4-PIS2, 4 Oct 2026)

Written and pushed before either blind pass of f.275r is started and before any decode of these lines.

Material.
- Letter: 4 Nov 1586, fr.16045 f.272-280. Contact views of c556-c573 at 700 px (RUN4-PIS2): canvas = 2 x folio + 12 holds
  (c562 carries the folio number 275). c556-c561 (f.272r-f.274v) are clear; cipher blocks on c562 (f.275r, lower half),
  c563-c568 (dense cipher with interlinear letters) and the head of c569; c570-c572 clear (signature on c572), c573 blank.
  Only f.275r is taken in this job (cap): the remaining cipher pages are a named gap.
- Cipher: f.275r = Gallica btv1b9060906j canvas 562, region 900,2600,2850,2520 at native size. 15 bands from
  `python3 tools/iiif_lines.py --ark btv1b9060906j --canvas 562 --region 900,2600,2850,2520 --out ciphers/fr16045-pisany-rome-1585/images --prefix f275r --debug --max-width 1600 --overlap 100`
  (auto-detected centres 114 274 441 616 762 934 1101 1277 1446 1607 1821 1978 2124 2263 2425; overlay
  images/f275r_lines_debug.jpg checked by eye: each band holds its own line). L01 = clear "... auquel i'estois, et" then
  cipher signs at the right end; L07 = cipher then clear "Mais croyant que Monsieur de"; L08 = clear "Luxembourg" then
  cipher; L02-L06 and L09-L15 cipher only. Small interlinear letters above several lines and the left-margin clerk notes
  are a partial period decipherment: not transcribed, not used.
- Clear copy: Melanges de Colbert 16 pt II (btv1b100341061) c479 p.121 l.14 "et ay trouve que le Pape" (the original's
  clear text on f.275r ends "... je me suis esclarcy du doute auquel i'estois, et", matching p.121 l.13-14) to c480 p.123
  end "... tant plus volontiers.", read by this worker from 1400 px canvas images: kp86d/colbert_p121_123.txt. The span is
  longer than the cipher on purpose; semi-global alignment leaves the clear side's ends free. The clear words "Mais croyant
  que Monsieur de Luxembourg" stay in the copy text (the cipher stream skips them; the alignment pays an inner gap).
- Key: arm A = key86.tsv (Tomokiyo 1586-87, published) unchanged. Arm B = key86 with RUN4-PIS1's label remap T31->o,
  T45->u, T47->f, T57->n (fitted on f.244r; f.275r held out). B reported beside A, never in place of it.

Transcription: two blind Sonnet passes (tx86d/PASS_BRIEF86d.md, values withheld, sheet SIGNSHEET86 copied unchanged to
tx86d/), one subagent call each over the 30 crops. Reconciliation: tools/reconcile_passes.py then the RUN3 shape rules of
tx86/reconcile86.py unchanged (kp86d/reconcile_d.py applies them to tx86d), no sign-by-sign judgement ->
tx86d/ciphertext_f275r.tsv. err_2reader = 1 - agree share from reconcile_passes.py.

Decode rule, normalisation, statistic (tools/stream_align.nw_score) and nulls (key-shuffle 1000, order-shuffle 1000):
exactly kp86/kp86.py (imported). Why each null can differ from the target: key-shuffle changes which letter each sign
yields (matched count can move independently of order); order-shuffle keeps the letter multiset but breaks sequence, which
the alignment needs.
Positive control (matched N and design, same clear text): the copy span with the in-clear phrase removed, first n letters
(n = decoded letter count of the reconciled target), enciphered with the arm's key (uniform random homophone, letters
only), sign noise at the measured err_2reader, scored against the full copy text with its own nulls (200/200); 5 seeds;
passes at >= 4/5. Script kp86d/kp86d.py -> kp86d/kp86d_result.json.

Gate per arm: PASS if the reconciled target > p99 of both nulls AND that arm's control passes. Control fails -> NON-TEST.
Target fails at err > 0.10 with the control passing -> FAIL at that e, reported as read, not a refutation of the table.
Blind passes A and B scored too (not gating). Grades: decoded letters aligned identically to the copy are C (known
plaintext), the rest M; H only in the sense of the published table. No parameter changes after the first run.
