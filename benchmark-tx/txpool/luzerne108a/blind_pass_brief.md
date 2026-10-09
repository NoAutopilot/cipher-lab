# Blind transcription pass, Huntington mssDE 108(A) (TX-POOL-LEAF-2, 9 Oct 2026)

You are one of two independent readers of the cipher figures on line crops of an 18th-century French letter written entirely
in a numerical code: groups of 1-4 figures separated by dots. You transcribe the FIGURES only, exactly as written. You do not
know, and must not look up, what any group means.

Read ONLY the crops named in your task (one page: `benchmark-tx/txpool/luzerne108a/crops/pN_L01.jpg` .. `pN_Lnn.jpg`). Do not open
any other file in this repository (no NOTES.md, no ciphertext, no key, no other pass, no other image of this letter, no build
script, nothing under ciphers/); the pass is void if you do.

## The crops

One crop per line, top to bottom of the page (L01 = top line). Each crop is the whole line, about 700-950 px wide, figures about
20-30 px tall: enlarge them (2-3x with PIL into your own scratch directory, never into the repository) and read in short
stretches, left to right. Pieces of the line above or below may show at a crop's edge: they belong to the neighbouring line;
ignore them. A few groups have a small word written UNDER them in another hand (a later annotation): ignore every word; read
only the figures on the line.

Crop note (written by tools/iiif_lines.py --overlap-note):
- p1: each line is one crop (no segments, no overlap).
- p2: each line is one crop (no segments, no overlap).
- p3: each line is one crop (no segments, no overlap).
- p4: each line is one crop (no segments, no overlap).
- p5: each line is one crop (no segments, no overlap).
- p6: each line is one crop (no segments, no overlap).

## The hand's figures (shape guide, 18th-century French clerk)

- `4` is open and looped, often like a small h, L or a 4 with a curled stem; `44` often looks like "hh" or "LL".
- `5` is often like a long s or a 2-shaped S (ſ / S); do not confuse with 3 (two bowls) or 9.
- `7` has a long stroke descending far below the line, often slanting left (/); several 7s may cross the line below.
- `1` is a plain short stroke; `11` and `111` can look like "u", "ll" or "ııı": count the strokes. `1` before a figure in a
  4-figure group (1022, 1151, 1188) is a thin stroke easy to miss.
- `9` has a closed bowl and a tail below; `6` a bowl at the bottom with a stem rising; `8` two stacked loops; `0` a small o,
  sometimes left open.
- Groups are separated by dots; a dot can be faint or missing. When two figure-clusters are clearly separated by space, they
  are two groups.

## Output

A TSV, header `passage	pos	sign_id	alt	conf	note`, one row per group, left to right, every line of your page:
- passage = the crop name without .jpg (p1_L01), pos = 1, 2, 3 ... within the line,
- sign_id = the figures of the group as you read them (e.g. 436),
- alt = your second-best reading if you are not sure (else empty), conf = H (sure) / M (probable) / L (guess),
- note = anything about a doubtful figure (struck, blotted, overwritten, cut by the crop edge).
Never skip a group: if illegible, write your best guess with conf L and a note. Return ONLY the TSV rows (with header) in your
final message.
