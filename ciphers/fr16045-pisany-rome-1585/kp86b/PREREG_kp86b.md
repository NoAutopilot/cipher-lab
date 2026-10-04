# PREREG kp86b -- fr16045 f.244v + f.245r (17 Sept 1586) cipher vs its Colbert 16 pt II clear copy (RUN4-PIS1, 4 Oct 2026)

Written and pushed before either blind pass of f.244v/f.245r is started, before any decode of these lines.

Material.
- Cipher: fr.16045 f.244v = Gallica btv1b9060906j canvas 501 (canvas = 2 x folio + 12; c502 carries the folio number 245):
  the cipher tail after the clear "... que l'on nous fait." (images/f244v_L00_L01.jpg) and 12 cipher lines
  (f244v_L01_s1 .. f244v_L12_s2), then the clear "... a Monsieur de la Fite ..." line below; f.245r = canvas 502, 7 cipher
  lines (f245r_L01_s1 .. f245r_L07_s2) ending at a full stop before the clear "A tant je prie". Crop commands in NOTES.md.
  Small interlinear letters above f.244v L02/L03 and f.245r L04/L05/L07 and the left-margin clear notes are a partial
  period decipherment: not transcribed, not used.
- Clear copy: BnF Melanges de Colbert 16 pt II (btv1b100341061) canvas 444 p.51 l.13 "Tout a cette heure Monsieur le
  Cardinal d'Est" to canvas 445 p.52 "... que personne n'en sache rien." (before "Dudit jour / Sire", the second 17 Sept
  letter), read by this worker from c444/c445 at 1600-1750 px: kp86b/colbert_p51_52.txt. Why this span and not the
  brief's pp.50-55: the copy runs p.50 l.15 ("dont il est question, mais que vostre Majeste fust ...") - p.51 l.12 in step with the clear lines of f.244v ("est question, mais que
  V.M. ..." to "... que l'on nous fait."); the next thing in the copy is the postscript "Tout a cette heure ...", which is
  also the text of f.244v's left-margin note (the period decipherment Tomokiyo mentions); pp.52 "Dudit jour" - 55 is a
  separate letter (f.246-247 per RUN3-PISD). Semi-global alignment leaves the clear side's ends free, so the span only
  has to contain the cipher's plaintext. If the cipher is not this postscript, the test FAILs, which is the point.
- Key: arm A = key86.tsv (Tomokiyo 1586-87, published) unchanged. Arm B = key86 with the label-level remap
  T31->o, T45->u, T47->f, T57->n from unit (a) (kp86b/cellcheck_a.md), fitted on f.244r only; f.244v/f.245r are held out.

Transcription: two blind Sonnet passes per page (4 subagent calls: f.244v A/B, f.245r A/B), brief tx86b/PASS_BRIEF86b.md
(values withheld, same sheet SIGNSHEET86). Reconciliation: tools/reconcile_passes.py then the RUN3 shape rules of
tx86/reconcile86.py unchanged (kp86b/reconcile_b.py applies them to the new files), no sign-by-sign judgement -> 
tx86b/ciphertext_f244v_f245r.tsv. err_2reader = 1 - agree share from reconcile_passes.py over both pages.

Decode rule, normalisation, statistic (tools/stream_align.nw_score), nulls (key-shuffle 1000, order-shuffle 1000) and
positive control (the clear span enciphered with the arm's key, letters only, noise at the measured err_2reader, 5 seeds,
200/200 nulls, pass at >= 4/5) exactly as PREREG_kp86.md, run per arm with its own key. Script kp86b/kp86b.py ->
kp86b/kp86b_result.json, committed with this file.

Gate per arm: PASS if the reconciled target > p99 of both nulls AND that arm's control passes. Control fails -> NON-TEST.
Target fails at err_2reader > 0.10 with the control passing -> FAIL at that e, reported as read with the reader error,
not a refutation of the table. Blind passes A and B are scored too (not gating). Folio sub-scores descriptive.
Arm B is reported beside A, never in place of it: B "helps" only if B PASSes and B's reconciled score exceeds A's;
no threshold on the difference is claimed, and B never enters key86.tsv from this test alone.
Grades: decoded letters that align identically to the copy are C (known plaintext), the rest M; key-source H only
in the sense of the published table. No parameter changes after the first run.
