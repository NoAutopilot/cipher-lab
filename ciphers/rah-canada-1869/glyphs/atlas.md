# Symbol legend, rah-canada-1869 (Nota cifrada del Conde de la Cañada, RAH 9/6958 nº 117/2-3)

Built once by the access/transcription worker (LANE R R4, 24 Sept 2026) from a first look at the two cipher
pages (`images/10137302.jpg`, `images/10137303.jpg`), before the two blind passes, per
`.claude/briefs/transcription.md`'s rule that two passes inventing their own codebook cannot be reconciled
row by row. This is a small, closed symbol set (mixed Arabic digits plus roughly a dozen recurring pen
marks), not the large invented-glyph case dupuy452's cluster pipeline was built for, so the atlas here is a
fixed label list rather than a pixel-prototype clustering run. **Both blind passes must use exactly these
labels** for any non-digit mark, in `[bracket]` form, and may add a new `[gNN]` label (numbered in the order
first seen, with a one-line description) only for a shape that genuinely matches none of the below — flag any
such addition at the top of the pass file so the reconciler can check it against the image.

Two example full-resolution cipher-line crops are kept beside this file for reference:
`example_p302_L07.jpg` (page 1, line under "carta que en forma de nota se estampa a continuación,") and
`example_p302_L17.jpg` (page 1, a later line). Read the actual page images for every line transcribed --
these two crops are orientation only, not the full symbol range.

| Label | Shape | Notes |
|---|---|---|
| digits `0`-`9` | plain Arabic numerals, as written | by far the commonest characters; write literally |
| `[dot]` | a small raised or centred dot, on its own | distinct from a decimal point attached to a digit run |
| `[cross]` | a cross/dagger with two short bars near the top of a vertical stroke (like a Lorraine cross or `‡`) | one of the commonest non-digit marks, often at a token's start |
| `[plus]` | a plain `+`, single crossbar | shorter and squarer than `[cross]` |
| `[circledot]` | a small closed circle with a mark (dot or short bar) inside it | resembles `⊙` or a Greek theta |
| `[circle]` | a plain open oval/circle, no interior mark | distinguish carefully from the digit `0`, which the same hand also writes as an oval -- if genuinely ambiguous, grade the token M and note it |
| `[equals]` | two short parallel horizontal strokes stacked | |
| `[dash]` | one short horizontal stroke, longer than one bar of `[equals]` | |
| `[loopn]` | a small cursive loop with a single hump, no dot (like a lowercase cursive n without the dot some hands give it) | very common as the last character of a token |
| `[loopm]` | a wider cursive loop with two humps (like a lowercase cursive m) | |
| `[bigloop]` | a taller looping flourish with a clear ascender (like a stylised cursive capital N or H) | often a whole token by itself or the first character of one |
| `[hook]` | a short stroke ending in an upward hook or tick (a small raised comma/arrow-like flick) | |
| `[tick]` | a tiny accent/apostrophe mark riding above another character | mark the character it rides above, e.g. `9[tick]` |

Ordinary punctuation the same hand uses in the clear-text lines (`.` `,` `-`) also appears inside the cipher
lines as apparent group/word separators; transcribe it literally rather than as a symbol label, and note in
the pass file whether you read it as a separator or as part of a token -- this is exactly the kind of row the
reconciler needs to settle from the image.

This legend is a starting point from one read at working resolution, not a verified ground truth: expect the
two blind passes to disagree on some of these labels (especially `[circle]` vs the digit `0`, and `[cross]`
vs `[plus]`), which is what `tools/reconcile_passes.py` is for.
