# PREREG-GAPS166 (3 Oct 2026, ~16:40 UTC, account-4): calibrating the f.410 fr18 FAIL against a period gloss

Written and pushed before f.467 (694/08 file 0579) is transcribed or any score below is computed.

Question: f.410's keyed decode (f410/candidate.txt, 190 letters) scores -1.038 on the fr18 judge vs real_p05 -0.99
(FAIL by 0.05), above all 20 shuffled-key decodes (best -1.17). Is the miss the key or the judge at this length/register?
Calibration (CLAUDE.md rule 3, ZX-DEC349 lesson): the leaf f.467 carries a period interlinear decipherment of its own
code groups. That gloss is genuine period plaintext of the same kind (the deciphered portions of a Manteuffel report).

Procedure: crops by tools/iiif_lines.py --image; two blind Opus passes read the interlinear gloss words (and the code
groups under them); reconcile; gloss text G = the reconciled gloss words in order, as written (no normalisation beyond
the judge's own a-z folding). Scored with tools/judge_plaintext.py specs/sachsstaatsarchiv-manteuffel-1712.json, the
same fr18 judge. Length matching: L = min(letters(G), 190). If letters(G) < 190, the candidate is also scored on every
contiguous L-letter window (step 10) and the mean/min/max reported beside G; real_p05 is the judge's own at each length.

Margin m(x) = score(x) - real_p05 at x's length.

Decision rule:
- letters(G) < 40: non-test (judge letters_min); logged as such, no flag, next step named.
- m(G) < +0.05 (the period gloss itself fails or only grazes the gate): the fr18 judge cannot certify genuine period
  gloss text of this register at this length, so the f.410 FAIL is the judge's limit, not a key negative. Then, if the
  f.410 candidate beats all 20 shuffled-key decodes (already 20/20) AND m(candidate at L) >= m(G) - 0.10 (the decode
  scores within 0.10 of the genuine gloss), flag 'reading ready' for a separate verifier. Otherwise no flag.
- m(G) >= +0.05 and the candidate (at L) still FAILs: the judge does read genuine period gloss of this kind, so the
  f.410 FAIL stands as a FAIL on the gate (cause: transcription split tokens, M alternatives, U gaps); no flag; next
  step is a transcription or key repair on f.410, not a new judge.
Shuffled controls: the existing f410/shuffled_00..19 are re-scored unchanged; additionally the gloss text is scored with
its letters shuffled (20 seeds) as a null sanity check (must fall far below G).
Caveat stated in advance: a gloss of a ciphered passage may be dominated by names and titles (f.468's were), a register
the fr18 corpus under-represents; that biases m(G) down, which is exactly the calibration in question.

Addendum (before any transcription or scoring, same session): letters(candidate.txt) by a-z count is 263, not 190 (GAPS162's
"about 190" was an estimate). Read L = min(letters(G), 263) wherever 190 appears above; nothing else changes.

Addendum 2 (16:4x UTC, after a 1/4-size layout look at file 0579 only, before any line is read or scored): f.467 is a
French clear report with a few code groups glossed interlinearly; the gloss words alone may fall under 40 letters. So
the passes also read the clear text, and a second calibration text C2 = the leaf's period plaintext as its decipherer
had it (clear text with each glossed code run replaced by its gloss, unglossed codes dropped) is scored the same way.
The decision rule is applied to G if letters(G) >= 40; otherwise to C2, reported as "C2 substituted for G (G too
short)". C2 is the same register as f.410 (Manteuffel's own French reports to Flemming), which is the calibration asked.
