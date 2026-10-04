# PREREG-N6VIV63 (4 Oct 2026, N6-VIV63, LANE-NEAR6 worker, account 2)

Written and pushed BEFORE any key.tsv decode of fr.16105 ff.190r-191v (ink 63, 10 Oct 1573) exists and before the blind passes have
returned (passes running at the time of writing). No interlinear words were seen on ff.190r-194r at 1600 px (NOTES "N6-VIV63"), so the
N5-VIV54 gloss check (gate a) does not apply: gate (b) below.

Inputs, frozen when the passes land (not re-chosen after any decode): tx/f190r|f190v|f191r|f191v_rec.tsv = two blind Sonnet passes per page,
tx/viv63_clean.py (drops DUP and [PLAIN:...] rows/stretches and '[...]', pass A 'π' -> P), tools/reconcile_passes.py, tx/reconcile_vivk.py's
label rules with --viv54 (RULES + RULES54) applied by tx/viv63_decode.py exactly as tx/viv54_decode.py. key.tsv unchanged (Tomokiyo's
published values, N5-VIVK). Tokenisation = tx/viv54_decode.py page_tokens() ("o o" -> "oo"); codes absent from key.tsv are unread and
dropped from decoded letter strings. Scorer = tools/judge_plaintext.py NgramModel (add-k 4-gram) built on the fr16 corpus (Catherine de
Medicis Lettres I, II; Marguerite de Valois letters: 16th-c. French court letters, era/register-matched to a 1573 ambassador's letter;
three files, < 5, which is why the statistic is used RELATIVE to nulls of the same decode, never against real_p05). Seed 20260904+63 =
20260967 for every null; 200 draws each.

## Statistics (both relative to nulls built from the same transcription)
- **b1, key fit:** s = mean log10 4-gram probability per letter of the key.tsv decode. Null = 200 shuffled-key decodes (key.tsv's 30 values
  permuted across its 30 codes; unread set unchanged). Pass b1 = s > null p99. The null can move s (letters change with the key).
- **b2, order beyond frequency:** same s. Null = 200 letter-order shuffles of the same key.tsv decode (letter multiset kept, order destroyed).
  Pass b2 = s > null p99. This null keeps unigram frequency, so b2 can only pass if the decode carries French n-gram ORDER, not just a
  French-looking letter frequency (a wrong but frequency-similar key could pass b1; it cannot pass b2 by frequency alone). The null can
  move s (4-grams change with order).

## Positive controls (run first, same code path, same seed scheme)
- C1: N5-VIVK's held-out f.103r decode (tx/f103r_rec.tsv under key.tsv; known plaintext = clerk decipherment, N5-VIVK Arm B PASS).
- C2: N5-VIV54's ink-54 decode (tx/f173r_rec.tsv + f173v_rec.tsv under key.tsv; gloss check PASS 0.609 vs p95 0.354).
The target (~4 pages) is longer than either control (~1.8-2.0k letters each); the brief asks for controls subsampled to the target's token
count, which cannot be done upward, so the controls are run at their full length (shorter = harder for the control, so a control pass is
conservative) AND the target is additionally scored per page (each page ~ the controls' length), reported beside the whole-piece figure.
Rules, in order:
 1. If C1 or C2 fails b1 (resp. b2) against its own null, b1 (resp. b2) is NOT a gate here: reported descriptively, no PASS/FAIL claimed.
 2. Ceiling/headroom (rule 3): if a control's own null p99 is within 0.01 of its real s, or a null median exceeds the real s, the statistic
    has no headroom at that length: not a gate.
 3. Otherwise the target (whole ff.190r-191v decode) PASSes b1 / b2 iff s > its own null p99.
"fr16104-vivonne-spain-1572 piece 63 ready for audit 1" is licensed only if b2 passes as a gate (b1 alone shows only that the key family
fits, which is expected of a 1573 Saint-Gouard letter inside Tomokiyo's April 1572 - Nov 1574 key span; it is reported beside b2).
Per-page b1/b2 results are descriptive. Not gated: words read by eye, print_check hits, the grade counts.
