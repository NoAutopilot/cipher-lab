# Provisional sign-shape legend, fr.3151 no.33 (Noailles), NX-3151G

Built by the worker from one visual skim of the crops before dispatching blind passes, so both passes use the
same vocabulary (positions can then be compared literally; shape identification itself is still done
independently and blind by each pass). Not a cryptanalytic classification -- purely "what shape is this ink
mark", the same role tools/glyph_atlas.py plays for other targets, done by eye here because the corpus is small
(~200 signs).

Numerals: read as literal two-or-one-digit Arabic numerals wherever legible (e.g. `20`, `30`, `70`, `100`, `9`,
`12`). Do not code a numeral into one of the letter-codes below.

Non-numeral pen-drawn signs, by shape (use the closest code; if nothing fits, use `unkN` for a new N per pass,
i.e. `unk1`, `unk2`... within your own pass, and add one line per unkN in a `NOTES:` section at the end of your
reply describing the shape in words, e.g. "unk1 = closed loop with two tails, bottom-left of line 4"):

- `plus`   -- a small `+` cross, short strokes of near-equal length
- `hash`   -- a lattice / double-cross mark, like `#`
- `tbar`   -- a vertical stroke topped with a horizontal bar (an upside-down T / a capital T), no loop
- `dash`   -- an isolated short horizontal stroke, no vertical component
- `slash`  -- a single diagonal stroke, `/`
- `pipe`   -- a single vertical stroke used as a separator (not part of a numeral)
- `hookC`  -- an open hook or crescent, unclosed, like a `C` or `⊂`
- `loop6`  -- a closed loop with a descending tail, like a cursive `6` or `G`
- `wmark`  -- a wavy horizontal squiggle, two or three humps, like a cursive `w` or tilde
- `starX`  -- an X-shaped or asterisk-like mark, strokes crossing at a point
- `tri`    -- a triangle or `Δ`-shaped mark
- `Hmark`  -- two vertical strokes joined by a horizontal crossbar, like `H` or `π`
- `Qtail`  -- a loop with one long descending tail, like `Q` or a reversed `9`
- `spiral` -- a small closed spiral or curl, like `Ω` or `@`
- `Ymark`  -- a Y-shaped or flag-topped stroke
- `circleO`-- a plain closed circle or oval, no tail
- `dotmark`-- a small dot or short tick sitting above/beside another sign (diacritic-like, not a full sign on
              its own -- note if it looks like it belongs to the sign before or after it)
- `arrowL` -- an L-shaped or sharply bent stroke
- `zigzag` -- a zigzag or M/W-like jagged stroke (distinct from the smoother `wmark`)

Mark every reading you are not confident of with a trailing `?` on the token (e.g. `hookC?`). Where a position
looks like a plaintext word squeezed onto the same line as cipher signs (common in this letter -- cipher signs
and French cursive words share physical lines), write the word literally, lower-case, prefixed `w:` (e.g.
`w:mon`, `w:seigneur`) so it is not mistaken for a sign code -- do not try to decode the cipher.
