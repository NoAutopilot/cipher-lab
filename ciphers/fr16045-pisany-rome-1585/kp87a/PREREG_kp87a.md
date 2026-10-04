# PREREG kp87a -- fr16045 f.301v (24 Mar 1587) cipher vs its Colbert 16 pt II clear copy pp.338-339 (RUN5-PIS87, 4 Oct 2026)

Written and pushed before either blind pass of f.301v is started and before any decode of these lines.

Material.
- Letter: 24 Mar 1587, fr.16045 f.297-303. canvas = 2 x folio + 12 holds: c606 carries "24 mars 1587" and folio 297, c612 = f.300,
  c614 = f.301r, c616 = f.302r, c618 = f.303r (signature, "De Rome ce xxiiii Mars 1587"). Viewed at 700 px: c606, c609, c612, c614,
  c615, c616, c618. Cipher seen: f.301v (c615) only, a block of 9 full lines plus a 7-sign tail after the clear "certain" on the
  line above, ending at a full stop before the clear "Il me sembla Sire"; the left margin of f.301v carries a period decipherment
  of the block in a second hand ("que le prince de Parme avoit faict entendre au Roy Catho. ..."): not transcribed, not used.
  The faint marks at the foot of f.301r (c614) are show-through of this verso, not a cipher line (judged at 700 px). c607-c608,
  c610-c611, c613, c617 not viewed (a gap, not a claim that they carry no cipher).
- Cipher: Gallica btv1b9060906j canvas 615, native 3930x5907, region 1250,2950,2600,1700. 10 bands from
  `python3 tools/iiif_lines.py --ark btv1b9060906j --canvas 615 --region 1250,2950,2600,1700 --out ciphers/fr16045-pisany-rome-1585/images --prefix f301v --debug --max-width 1600 --overlap 100`
  (auto centres 80 262 410 556 736 926 1058 1231 1412 1563; overlay images/f301v_lines_debug.jpg checked by eye: one line per band).
  L01 = clear "luy mandoit po(ur) advis tres expres et certain" then 7 cipher signs; L02-L09 cipher; L10 cipher then clear
  "Il me sembla Sire". Margin-gloss fragments at the left edge of the crops are skipped.
- Clear copy: Melanges de Colbert 16 pt II (btv1b100341061) c588 p.338 l.11 "lequel luy mandoit pour advis tres expres et
  certain" to p.339 l.5 "... repliquer ce que dessus", read by this worker at 1400 px: kp87a/colbert_p338_339.txt (500
  normalised letters). The cipher's plaintext is expected to be p.338 l.12 "que le Prince de Parme" to p.339 l.3 "que l'on le
  pensast." (the copy's clear lines before and after match the original's clear text). The span is longer on purpose
  (semi-global alignment, free ends). Copy heading for the letter: c581 p.324 (RUN3-PISD).
- Key: arm A only = key86.tsv (Tomokiyo 1586-87, published) unchanged.

Transcription: two blind Sonnet readers, ONE LINE PER SUBAGENT CALL (each call gets only that line's s1/s2 crops and
tx87/SIGNSHEET86.png, copied unchanged from tx86d), brief tx87/PASS_BRIEF87.md; 10 lines x 2 readers = 20 calls. Each call
writes one row; rows are concatenated in line order into tx87/passA.tsv and tx87/passB.tsv with no edit. Reconciliation:
tools/reconcile_passes.py, then kp86d/reconcile_d.py (the RUN3 shape rules, unchanged) applied to tx87 ->
tx87/ciphertext_f275r.tsv (the script's fixed output name), copied to tx87/ciphertext_f301v.tsv. No sign-by-sign judgement.
err_2reader = 1 - agree share from reconcile_passes.py.

Statistic, decode rule, nulls (key-shuffle 1000, order-shuffle 1000, tools/stream_align.nw_score) exactly kp86/kp86.py;
positive control exactly kp86d.control() (copy span with the in-clear phrases "lequel luy mandoit pour advis tres expres et
certain" and "Il me sembla, Sire, que je pouvois repliquer ce que dessus" removed, first n_dec letters, key86, uniform homophone,
noise at the measured err_2reader, 200/200 nulls, 5 seeds, pass at >= 4/5). Script kp87a/kp87a.py (committed 1d7d50f7) ->
kp87a/kp87a_result.json. Why each null can differ from the target: key-shuffle changes which letter each sign yields; order-shuffle
keeps the letter multiset but breaks sequence, which the alignment needs.

Gate: PASS if the reconciled target > p99 of both nulls AND the control passes. Control fails -> NON-TEST. Target fails at
err > 0.10 with the control passing -> FAIL at that e, not a refutation of the table. Blind passes A and B scored too (not
gating). Grades: if PASS, decoded letters aligned identically to the copy are C, the rest M; if not PASS, all M. No parameter
changes after the first run. A second page only if the job stays under 80% of its USD 8 cap (none seen on the viewed canvases).
