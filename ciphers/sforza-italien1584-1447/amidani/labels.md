# Label sheet for Amidani 1447 cipher slips (SFZ-1, 7 Oct 2026)

Built by SFZ-1 from a look at f.366 (italien 1584, Gallica canvas 360), aligned where possible with Bourdeau's
f.68/f.70 descriptions (ciphers/sforza-maino-1446/signs.tsv). One ASCII label per sign. Both reading passes use these
labels. A sign that fits none: write N1, N2, ... and describe it once in a note at the end of the pass. A sign you
cannot read: `?`. A sign you are unsure between two labels: `a/b?`.

| label | description |
|---|---|
| + | plain cross / plus sign (very common) |
| a | a as written (round a) |
| b | plain b, also 6-like b with closed bowl, no bar |
| B | b whose bowl ends in a hooked tail to the right ("bo" / b with flourish, like b followed by a small curl) |
| c | c as written |
| d | d with curled/apostrophe-like ascender bent left (like a backwards 6 or the letter eth) |
| D | divide-like sign: a short vertical or t-like stroke followed by a colon (":" dots), "t:" or "÷" |
| F | double long stroke with crossbar: looks like "ff" or two barred long-s side by side |
| f | single long s / f with crossbar (one stroke of F) |
| # | double-barred cross: two vertical strokes crossed by two horizontal bars, like "#" or "H" with bars |
| g | figure like a g with descender bar |
| H | h-like sign whose right leg descends below the line in a hook, like a 4 or "y" upside down (Bourdeau's looped h) |
| h | h-like sign with a hook/curl at top-left: like "ʒ" standing on h, or "h" with a flag (narrow, compact) |
| J | yogh/3-like sign with a horizontal bar crossing its descender (Bourdeau's barred yogh) |
| 3 | plain yogh / 3 without bar |
| l | slanted stroke with a short crossbar, like "/" or "ł" (often in pairs "l l") |
| O | small o followed by a long horizontal tail stroke to the right ("o-") |
| o | sigma-like: small o with a bar on top extending right ("σ") |
| Q | phi: circle with a vertical stroke through it |
| q | q-like sign with a horizontal stroke through its descender, often preceded by a dash ("-q") |
| R | "or"/"ɒı"-like sign: a reversed-c bowl followed by a short stroke (looks like "or" or "ɔı") |
| S | long-s-like composite "ccſ"/"aſ": a small curl joined to a tall long-s stroke |
| m | m-like multi-stroke sign followed by a long s ("mſ", "ms"), as one unit |
| T | pi: π (two legs and a top bar) |
| U | "bu"/"hu": an h- or b-like stroke joined to a u, as one unit |
| W | wave sign: a horizontal "~" or sideways omega "-ω" |
| x | x as written |
| Y | gamma-like / y-like sign with a short tail (like the Greek gamma) |
| z | z as written |
| 7 | 7 |
| 8 | 8 |
| t | t-like sign with a high bar and the stem bent ("T" with a hook) |
| > | > |
| e | e / epsilon-like |
| k | k-like sign |

A superscript small circle or dot above a sign (e.g. above x or 8): write the label followed by `^` (e.g. `x^`).
Clear (uncoded) words written in ordinary script among the signs: write them as `w:word` (e.g. `w:adusse`), one token.

## Additions made while reading (SFZ-1, 7 Oct 2026)

- `cX` (two characters, `c` + a letter, e.g. `cp cr ci cm cu`): a sign written in the shape of a cursive minuscule letter X, run
  together with its neighbours so that the group looks like a clear word ("primu", "tanno", "lano", "adusse", "maxie", "mea").
  The alignment shows these groups are cipher, not clear text (e.g. f.366 "adusse" aligns to "sonno"), so each letter-shape is
  a separate sign label; the same shape is assumed to be the same sign wherever it occurs.
- `A`: a-like sign with a bar or tilde above (ā). `P`: b with a bar through the ascender (ƀ). `n`: ∩-shaped sign. `K`: ß-like
  (fi-ligature-like) sign. `X`: a large cross with a loop (f.148 L7 only). `V`: circle with a horizontal bar (θ). `4`: 4-like.
- Deviation from the brief: these were read by SFZ-1 itself (one reader), not by two blind Sonnet passes; see NOTES.md.

## Additions made for f.70 (italien 1583, 1446; SFZ-70, 7 Oct 2026)

Both blind passes on f.70 found its commonest signs outside the 1447 sheet. Their pass-local N-labels were harmonised by
description into these labels (Bourdeau's f.70 code in brackets, from the token alignment in sforza-maino-1446/NOTES.md):
- `Nc` vertical stem with two short bars to the right, comb-like "⊧" [F]. `Nr` stem with one mid bar to the right, "⊢" [+].
- `Na` double arrow "⇒" [>]. `Nb` b/6 with a bar or flag across the top, "ƀ" [E, B]. `Np` p/rho with a rising flag [p, also J/H/c].
- `Ns` tall long-s "ʃ" [S]. `Ny` looped psi-like sign on a stem [Y, X]. `Nm` small r/gamma with a tail [r]. `Nh` hatched sign. `Nw` wave/"oo" flourish.
None of these has a value in key.tsv: the 1447 reader used no label with these descriptions. Their nearest 1447 labels by
description are in f70_test.py NEAREST. SFZ-70 compared two crops by eye (f.148 L3, f.366 L2) and saw no comb or one-bar-stem signs
there. That is a spot check, not a sign-by-sign audit of the 1447 slips.
