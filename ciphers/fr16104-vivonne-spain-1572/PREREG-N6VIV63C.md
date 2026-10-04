# PREREG-N6VIV63C (4 Oct 2026, N6-VIV63C, LANE-NEAR6 worker, account 2) -- addendum to PREREG-N6VIV63.md / PREREG-N6VIV63B.md

Written and pushed BEFORE any crop, blind pass or key.tsv decode of the last ink-63 cipher pages exists. Pages in scope ("new"): f.193v and
f.194r (cipher lines only, the plain close of f.194r excluded), exactly those with two blind passes when the transcription is frozen (listed in
NOTES "N6-VIV63C"; if only f.193v is read within the cap/box, "new" = f.193v alone and the result line says f.194r is unread).
"Whole piece" = ff.190r-193r (N6-VIV63 + N6-VIV63B frozen transcriptions, unchanged) + the new pages.

**Disclosure.** b2 and its results on ff.190r-191v (N6-VIV63) and ff.192r-193r (N6-VIV63B: new -1.560 vs p99 -1.809; whole -1.536 vs -1.826;
specificity real margin +0.290 vs wrong-key p99 +0.043) are known. The whole-piece test therefore contains ~11.8k already-seen letters; the
new-pages-alone test (i) is the only part on unseen material. Nothing below is re-chosen after a decode of the new pages.

**Frozen inputs.** As PREREG-N6VIV63B.md: tx/<page>_pass{A,B}.tsv -> tx/viv63_clean.py -> tools/reconcile_passes.py (default settings) ->
label rules RULES + RULES54 + RULES63 in tx/viv63_decode.py; any further label rule for the new pages is settled by eye on crops BEFORE the
first decode and committed with the frozen passes; key.tsv unchanged; scorer fr16 NgramModel (add-k 4-gram), tokenisation and unread-code
handling as PREREG-N6VIV63.md; seed 20260967; 200 draws each.

## Gates
1. **b2** exactly as PREREG-N6VIV63.md: s = mean log10 4-gram probability per letter of the key.tsv decode; null = 200 letter-order shuffles of
   that decode; pass = s > null p99. Positive controls C1 (f.103r, tx/f103r_rec.tsv) and C2 (ink 54, f173r+f173v) run first through the same code.
   - **(i) new pages alone** (seed tag 'T-new-C'). The controls are longer than the new pages, so each is **subsampled to the new pages' own
     decoded letter count** (rule 3, last paragraph; as PREREG-N6VIV53B.md (b-i)): the contiguous window of the control's code sequence from
     token 0 whose decode has that many letters (tags 'C1-sub-C', 'C2-sub-C'). Both subsampled controls must pass b2 with headroom
     (s - p99 > 0.01 and null median < s), else (i) is "not a gate" and the new pages are reported descriptively.
   - **(ii) whole piece ff.190r-194r** (tag 'T-whole-C'). Controls at full length (C1 1,770, C2 1,793 letters; shorter than the piece, so a
     control pass is conservative); both must pass b2 with headroom (their numbers must reproduce N6-VIV63: C1 -1.715 vs -1.909, C2 -1.658 vs -1.829).
   Per-page b2 on the new pages: descriptive.
2. **Specificity (registered).** 200 wrong keys: key.tsv's 30 values permuted across its 30 codes (unread set unchanged), seed
   '20260967-spec-C'. Each decodes the WHOLE piece and is scored through b2 exactly as the real key (own 200-draw letter-order null); margin =
   s - null p99. Reported: wrong-key b2 pass share; margin median, p95, p99, max; the real key's whole-piece margin.
   **Pass rule, stated before running: specificity PASS iff the real key's whole-piece b2 margin > the wrong-key margin p99.**
   (Not a gate on its own: the wrong-key pass share, 19.5% at 11.8k letters in N6-VIV63B.)

## What licenses what
- "fr16104-vivonne-spain-1572 piece 63 ready for audit 1 (all pages)" only if (i) PASSes with both subsampled controls passing, (ii) PASSes
  with both full controls passing, AND specificity PASSes. If f.194r is unread, the line names it instead of "all pages".
- Any other combination: reported as measured, no audit-ready line for the new pages (ff.190r-193r's earlier audit-ready line stands as written).
- Not gated: words read by eye, print_check hits, grade counts, per-page figures.
