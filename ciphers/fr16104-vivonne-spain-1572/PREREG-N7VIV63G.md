# PREREG-N7VIV63G (4 Oct 2026, N7-VIV63G, LANE-NEAR7 worker, account 2) -- addendum to PREREG-N6VIV63.md / -N6VIV63B.md / -N6VIV63C.md

Written and pushed BEFORE any crop, blind pass or key.tsv decode of fr.16105 f.194r page lines 5-10 exists (12:4x UTC).
New material ("new"): f.194r page lines 5-10 only, re-cut from canvas c199 native region 4800,200,2950,2700 deskewed (angle fitted or -1.4 deg
as N6-VIV63C; the debug overlay is checked by eye BEFORE any pass, and a band straddling two written lines is re-cut, not passed). Exactly the
bands with two blind passes when the transcription is frozen; if fewer than six lines are kept, the dropped ones are named.
"Whole piece" = ff.190r-194r as frozen by N6-VIV63/63B/63C (unchanged) + the new lines inserted as f.194r rows L05-L10.

**Disclosure.** Every earlier ink-63 gate result is known (N6-VIV63C: whole -1.547 vs p99 -1.835; specificity real +0.288 vs wrong-key p99
+0.048; 24% wrong-key bare b2 pass). The whole-piece test below is ~99% already-seen material; only (i) is unseen. Nothing below is re-chosen
after a decode of the new lines.

**Frozen inputs.** tx/f194r_mid_pass{A,B}.tsv (the new passes, rows L01-L06 = page lines 5-10) -> tx/viv63c_f194r_compose.py (extended to insert
them as L05-L10; the other rows unchanged) -> tx/viv63_clean.py -> tools/reconcile_passes.py (default) -> RULES + RULES54 + RULES63 in
tx/viv63_decode.py. **No new label rule** for the new lines (splits left at pass A, as N6-VIV63C); nothing settled by "what decodes better".
key.tsv unchanged. Scorer fr16 NgramModel (add-k 4-gram), tokenisation, unread-code handling, seed 20260967, 200 draws each, as PREREG-N6VIV63.md.

## Gates
1. **b2** exactly as PREREG-N6VIV63.md (s = mean log10 4-gram prob/letter of the key.tsv decode; null = 200 letter-order shuffles; pass = s > p99).
   - (i) new lines alone (tag 'T-new-G'), controls C1 (f.103r) and C2 (ink 54) subsampled to the new lines' decoded letter count (contiguous
     window from token 0; tags 'C1-sub-G', 'C2-sub-G'). Both must pass with headroom (s - p99 > 0.01, null median < s), else (i) is
     "not a gate" and the new lines are reported descriptively. (Expected short: ~6 lines, a few hundred letters.)
   - (ii) whole piece ff.190r-194r (tag 'T-whole-G'); controls at full length must reproduce N6-VIV63 (C1 -1.715 vs -1.909, C2 -1.658 vs -1.829).
2. **Specificity**, rule unchanged from PREREG-N6VIV63C.md: 200 wrong keys (key.tsv's values permuted across its codes, unread set unchanged),
   seed '20260967-spec-G', each scored through b2 on the WHOLE piece; **PASS iff the real whole-piece margin > the wrong-key margin p99.**

## Key-questions context table (not a gate)
A code-context table for y, single o, c, V, e, 2, r: their frequency and neighbours in the ink-63 reads, and what (if anything) ink 40's
clerk-decipherment alignment (tx/key_support.py) gives them. Output is proposals with counts only; key.tsv is not touched and no proposal is
applied to any reading or gate here (a key change is a separate graded step under its own PREREG).

## What licenses what
- If (ii) and specificity PASS with both full controls passing with headroom: "piece 63 whole-piece gates re-run after f.194r L5-10: PASS",
  recorded as a "Revision after AUDIT 3 (N7-VIV63G)" note under AUDIT 3 (lines, tokens, H/M/U), class and depth untouched.
- Any other combination: reported as measured. Not gated: words read by eye, print_check hits, grade counts, the key-questions table.
