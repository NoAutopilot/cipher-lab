# PREREG-N6VIV53B (4 Oct 2026, N6-VIV53B, LANE-NEAR6 worker, account 2) -- addendum to PREREG-N6VIV53.md

Written and pushed BEFORE any key.tsv decode of fr.16104 f.171v (ink 53, 5 Sept 1572, last cipher page) exists, while its two blind
Sonnet passes are still running. The PREREG-N6VIV53 gloss gate on ff.170r-171r FAILED as registered (0.577 < 0.60 floor): that result
stands; it is not re-run, re-windowed or re-thresholded here (tx/viv53_test.py and tx/viv53_result.json stay on ff.170r-171r only).

**Disclosure.** The ff.170r-171r key.tsv decode (reading_piece53.tsv, N6-VIV53) was already on file and described in NOTES when the
statistic b2 below was chosen. b2 itself was fixed by N6-VIV63 (PREREG-N6VIV63.md) for ink 63, not chosen for ink 53, and is used
here unchanged. Gates (b-ii) and (c) include ff.170r-171r, whose decode was seen; only (b-i) is on unseen material.

**Crops.** The N6-VIV53 f.171v crop region (1250,1330,2950,2300) missed the first 3 cipher lines (checked against the c186 page at
1600 px); re-cut before any pass: `tools/iiif_lines.py --ark btv1b9009609w --canvas 186 --region 1250,950,2950,2680 --out
ciphers/fr16104-vivonne-spain-1572/images/p53 --prefix c186_f171v --follow-slope 400 --distance 80 --max-width 1600 --overlap 150 --debug`
-> 21 lines x 2 segments. f.171v has **21** cipher lines (not 18).

Inputs frozen when the passes land (not re-chosen after any decode): tx/f171v_pass{A,B}.tsv (two blind Sonnet passes, prompt = SIGNS.md
+ the page's crop paths); tx/viv54_clean.py; tools/reconcile_passes.py on the _c passes -> tx/rec_f171v/; tx/reconcile_vivk.py f171v
--viv54 (N5-VIVK's six rules + N5-VIV54's ':'/'o' rule, nothing added -- exactly N6-VIV53's path) -> tx/f171v_rec.tsv. key.tsv unchanged.
Tokenisation = tx/viv54_decode.py page_tokens() ("o o" -> "oo"); codes absent from key.tsv unread and dropped from letter strings.
Scorer = tools/judge_plaintext.py NgramModel (add-k 4-gram) on tools/data/fr16 (the three files of PREREG-N6VIV63), used RELATIVE to
nulls only. Seed string base "20261053" for every null below; 200 draws each.

## (a) Gloss check on f.171v's own glosses -- does not apply
Interlinear words on f.171v, read by this worker at native resolution from the cached source region (8 tiles, all 21 lines) BEFORE any
pass returned or any decode: **none** (no plain words above or between the cipher lines; the "37." at the end of L01 is part of the
cipher line; the closing "de Madril ce v^me de Sept^bre 1572" and signature lie below the region). 0 < 3, so (a) is not run.

## (b) b2, order beyond frequency (PREREG-N6VIV63's statistic, unchanged)
s = mean log10 4-gram probability per letter of the key.tsv decode; null = 200 letter-order shuffles of that same decode (multiset kept).
Pass = s > null p99. Positive controls, run first, same code path: C1 = N5-VIVK f.103r decode (tx/f103r_rec.tsv); C2 = ink 54 decode
(tx/f173r_rec.tsv + f173v_rec.tsv). Control rules as PREREG-N6VIV63 (fail or headroom < 0.01 or null median > s -> "not a gate").
- **(b-i) f.171v alone.** Controls are longer than f.171v, so each control is subsampled to f.171v's own decoded letter count (rule 3,
  last paragraph): the contiguous window of C1's / C2's code sequence starting at token 0 whose decode has that many letters. Both
  subsampled controls must pass b2 with headroom, or (b-i) is "not a gate" and f.171v is reported descriptively.
- **(b-ii) whole piece 53 (ff.170r-171v).** Controls at full length (shorter than the piece = harder, a control pass is conservative,
  as PREREG-N6VIV63). Gate as above. Per-page b2 figures reported, descriptive.

## (c) Specificity of b2 on the whole piece (registered before running)
200 wrong keys = key.tsv's 30 values permuted across its 30 codes (unread set unchanged), seed "20261053-wrong". Each wrong-key decode
of the whole piece is run through b2 exactly as the real key (its own 200 letter-order shuffles); margin = s - null p99.
Report: share of wrong keys that pass b2; the wrong-key margin distribution's median, p95, p99, max; the real key's margin.
**Pass (c) iff the real key's margin > the wrong-key margin p99.** (The N6-VIV63 post-hoc diagnostic found 5/50 wrong keys passing b2
on ink 63; b2 alone is therefore not taken as key-specific.)

## What licenses what
"fr16104-vivonne-spain-1572 piece 53 ready for audit 1" only if (b-ii) passes as a gate AND (c) passes. (b-i) passing alone, or (b-ii)
without (c), is reported as such and does not license it. Not gated: words read by eye, print_check hits, grade counts.
