# Reconciliation of the f.30r-v passes (item 22), 24 Sept 2026

Reconciler: Opus, 02:55-03:15 UTC by `date -u`. Inputs: `passA_f30.tsv`, `passB_f30.tsv` (blind Sonnet passes),
the 110 line-half crops `images/crops_f30/*.jpg` (native resolution, committed at 355b871), the atlas
(`atlas/atlas_f29.png`, `atlas/atlas_f30add.png`) and the key tables (`sources/cryptiana/web/francisGramont.png`,
`sources/cryptiana/web/GL/BnF_fr3071_f17.png`). No image was fetched.

## Method

Same as the f.29r reconciler (`reconciliation.md`): every crop was read left to right by the reconciler with both
passes beside it. Each sign was settled from the image, and the passes served as a check. The settled reading
is `passR_f30.tsv` (one row per line half, same row ids as the passes; a trailing `?` marks a sign read with
doubt, `[?]` an illegible sign). `build_ciphertext_f30.py` aligns it with each pass (difflib on codes) and writes:

- `ciphertext_f30.tsv`: line, position, sign, confidence. Positions run across the a and b halves of a line.
  **h** means the sign is read firmly and at least one pass has the same code at the aligned position.
  **m** means it is read firmly from the image and neither pass agrees. **l** means uncertain or illegible.
- `reconciliation_f30_lines.tsv`: agreement per line (reconciler vs A, vs B, and A vs B) and h/m/l counts.
- `reconciliation_f30_signs.tsv`: every position where the settled sign differs from either pass, with both
  pass codes and the basis (agrees with A / agrees with B / both passes differ).
- `--check` exits 1 if any of the three is stale.

The 9(E)/g(V) lesson from the second reader was applied by shape: 9 has the long descender swinging left or
right under the next sign, and g has a closed bowl with a tail hooking back. The crops were read at their
native scale, not at a 2x zoom sign by sign, so single 9/g calls on faint crops remain possible errors.

## Result

1973 signs (plus dots) over 55 lines: **h 1333, m 474, l 166.**
Agreement of the settled reading with pass A: 63.5%; with pass B: 55.3%. The two passes agree with each
other on 60.8% of signs. Of the 1013 positions where the settled sign differs from at least one pass, 293
follow pass A, 132 follow pass B, and in 588 both passes differ from the image reading.

So, as on f.29r, the transcription rests mainly on one reader. The passes confirm about two thirds of it.

Per line (settled vs A / settled vs B / A vs B):

| line | vs A | vs B | A-B | line | vs A | vs B | A-B |
|---|---|---|---|---|---|---|---|
| r01 | .61 | .61 | .68 | r29 | .59 | .50 | .59 |
| r02 | .44 | .46 | .57 | r30 | .69 | .59 | .65 |
| r03 | .65 | .59 | .68 | r31 | .68 | .57 | .59 |
| r04 | .57 | .57 | .54 | r32 | .66 | .61 | .62 |
| r05 | .65 | .62 | .76 | r33 | .65 | .62 | .63 |
| r06 | .66 | .68 | .63 | r34 | .46 | .46 | .51 |
| r07 | .67 | .69 | .71 | r35 | .66 | .54 | .58 |
| r08 | .62 | .53 | .61 | v01 | .62 | .62 | .63 |
| r09 | .64 | .38 | .51 | v02 | .69 | .67 | .72 |
| r10 | .68 | .61 | .63 | v03 | .72 | .57 | .65 |
| r11 | .59 | .56 | .53 | v04 | .78 | .62 | .69 |
| r12 | .54 | .63 | .57 | v05 | .62 | .46 | .54 |
| r13 | .60 | .50 | .50 | v06 | .81 | .78 | .83 |
| r14 | .68 | .58 | .55 | v07 | .66 | .63 | .68 |
| r15 | .58 | .53 | .56 | v08 | .69 | .58 | .72 |
| r16 | .55 | .50 | .54 | v09 | .66 | .51 | .69 |
| r17 | .70 | .62 | .64 | v10 | .78 | .56 | .67 |
| r18 | .64 | .56 | .54 | v11 | .67 | .48 | .69 |
| r19 | .62 | .71 | .76 | v12 | .64 | .58 | .64 |
| r20 | .54 | .43 | .65 | v13 | .50 | .43 | .55 |
| r21 | .62 | .57 | .62 | v14 | .57 | .53 | .73 |
| r22 | .63 | .49 | .54 | v15 | .66 | .59 | .62 |
| r23 | .64 | .42 | .60 | v16 | .63 | .53 | .57 |
| r24 | .67 | .47 | .59 | v17 | .77 | .43 | .50 |
| r25 | .51 | .49 | .51 | v18 | .59 | .50 | .55 |
| r26 | .60 | .46 | .46 | v19 | .62 | .44 | .39 |
| r27 | .62 | .65 | .64 | v20 | .56 | .52 | .57 |
| r28 | .71 | .55 | .54 | | | | |

## How the disagreements were settled (by class)

Most of the 1013 differences fall into a few systematic classes. Each was settled on the crops.

1. **Codes outside the atlas.** Pass A wrote `J` 60 times for the tall j with strokes (the atlas `r3`, R) and
   `r` 36 times for r-with-dot (`nr`, N). Pass B wrote `sq` for the open box. These are normalised before
   alignment. They are code slips, not different readings.
2. **Ascender lines copied into a row.** Pass A's f30r_L08a begins with the L07a signs that intrude from above.
   Its f30r_L16b begins with a copy of L15b (the bleed the passes worker flagged). The settled rows read only
   the signs on the row's own base line.
3. **Barred 2.** A 2 with a stroke through or under it is distinct from the plain 2, which has a tick above it
   (atlas). Both passes wrote `2`. It was settled as `zb` (key: null, M) wherever the bar is visible, 36
   positions. Read as a null, it removes a letter from Q·VIL and similar sequences.
4. **N-with-hook and the small sign after it.** The √-like N with a hook is `nq` (Lasry Q, row 2). The passes
   wrote `n6`, `D`, `br` or `2`. The small r/2-shaped sign that often follows it, and the free-standing n-shape,
   were given a new code `n` (not in key.tsv).
5. **Open box with a bar** (`BOX`). The atlas files it under `sq` (Lasry X, a filled box). On f.30 it occurs 27
   times, in contexts where X cannot stand. It was kept as its own code, unkeyed (see NOTES.md, unkeyed signs).
6. **Crossed S** (`Sx`) was separated from `5` and `sl`. **re** (an r-hook joined to e) was separated from
   `eh`. **ev** was separated from `oi`. **v** (a v-shape distinct from `yt`'s curled t) was separated from `yt`.
   **lz** (atlas: small l-z form) was separated from `dl` and `A2`. **B8** (a figure 8 with a cross stroke) was
   separated from `INF`. Each is listed with its contexts in `unkeyed_f30.tsv`.
7. **Long-s family.** Pass B wrote `ST` 118 times. It covered the plain long s (`sl`), the arch (`ss2`), the
   long s joined to t (`ST`) and the r3/yt shapes. The crops separate them. `ST` is kept only where the t is
   joined, 18 times.
8. **Remaining one-off differences** (the 9/g, D/br, lt/Rt, Af/fh calls) were read from the crop. In the
   signs file their basis is the pass they agree with, or "both passes differ".

Illegible or blotted spots stay `[?]` (4) or `?` (l). The four `[?]` are the blot at f30r_L02 (first sign),
f30r_L08b (first sign), f30r_L22a (first sign) and f30r_L26b (a sign under the blot). The first sign of f30r_L23,
also under a blot, is `2?`. The
f30r_L07-L09 blot region the passes worker flagged was legible on the crops.
