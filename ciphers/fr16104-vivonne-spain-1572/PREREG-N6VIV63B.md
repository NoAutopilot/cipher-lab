# PREREG-N6VIV63B (4 Oct 2026, N6-VIV63B, LANE-NEAR6 worker, account 2) -- addendum to PREREG-N6VIV63.md

Written and pushed BEFORE any key.tsv decode of the new ink-63 pages exists (the blind passes of f.192r and f.192v were running at the time
of writing; f.193r not yet started). Pages in scope: the new pages read by N6-VIV63B (planned f.192r, f.192v, f.193r; exactly those with two
blind passes when the transcription is frozen, listed in NOTES "N6-VIV63B"). "Whole piece" = ff.190r-191v (N6-VIV63's frozen transcription,
unchanged) + the new pages.

**Disclosure.** b2 was chosen by N6-VIV63 and its target result on ff.190r-191v (-1.514 vs p99 -1.824, PASS) and the controls' results are
already known; the post-hoc 50-wrong-key diagnostic (5/50 pass b2, best wrong margin +0.061, real +0.311) is also known. The whole-piece
test below therefore contains already-seen material; the new-pages-alone test (i) is the only part on unseen material. Nothing below is
re-chosen after a decode of the new pages.

**Frozen inputs.** As PREREG-N6VIV63.md: tx/<page>_pass{A,B}.tsv -> tx/viv63_clean.py -> tools/reconcile_passes.py -> label rules RULES +
RULES54 + RULES63 in tx/viv63_decode.py; any further label rule for the new pages is settled by eye on crops BEFORE the first decode and is
committed in the same commit as the frozen passes (listed in the decode script header); key.tsv unchanged; tokenisation, unread-code
handling, scorer (fr16 NgramModel, add-k 4-gram) and seeds as PREREG-N6VIV63.md. Draws: 200 each.

## Gates
1. **b2 (order beyond frequency)**, exactly PREREG-N6VIV63.md: s = mean log10 4-gram probability per letter of the key.tsv decode; null = 200
   letter-order shuffles of the same decode; pass = s > null p99. Positive controls C1 (f.103r) and C2 (ink 54) re-run first through the same
   code (same seeds, so their numbers must reproduce N6-VIV63's: C1 -1.715 vs -1.909, C2 -1.658 vs -1.829); PREREG-N6VIV63.md rules 1-2
   (control failure or no headroom -> not a gate) apply unchanged. Run on (i) the new pages alone (seed tag 'T-new') and (ii) the whole piece
   (seed tag 'T-whole'). Per-page b2 on the new pages is descriptive.
2. **Specificity check (registered this time).** 200 wrong keys: key.tsv's 30 values permuted across its 30 codes (unread set unchanged),
   seed '20260967-spec'. Each wrong key decodes the WHOLE piece and is scored through b2 exactly as the real key (own 200-draw letter-order
   null, seed tag 'spec'); margin = s - null p99. Reported: share of wrong keys that pass b2; the wrong-key margin distribution's median, p95
   and p99 (tools/judge_plaintext.pct); the real key's whole-piece margin. **Pass rule, stated before running: specificity PASS iff the real
   key's whole-piece b2 margin > the wrong-key margin p99.** (A wrong-key b2 pass share is reported whatever it is; it is not itself a gate,
   since N6-VIV63's diagnostic already showed b2 alone false-passes ~10% of wrong keys at 6k letters.)

## What licenses what
- "fr16104-vivonne-spain-1572 piece 63 ready for audit 1 (all pages read so far)" only if b2 (i) PASSes AND b2 (ii) PASSes AND the specificity
  check PASSes, all with both positive controls passing b2 with headroom. If ff.193v-194r remain unread, the line says which pages.
- Any other combination: reported as measured, no audit-ready line. b1 (shuffled-key null) is not re-run as a gate (C1 failed it in N6-VIV63).
- Not gated: words read by eye, print_check hits, grade counts, per-page figures.
