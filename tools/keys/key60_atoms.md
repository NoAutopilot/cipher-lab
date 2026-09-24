# Transcription atoms for cipher no.60 letters (LANE R5 F3, 24 Sept 2026)

Blind passes on no.60 letters write one ATOM per row: the smallest separately written glyph, not the key's
compound signs (the key has compounds such as `to`, `g+`, `+o`, `pi`, `X++`; `tools/keys/key60_segment.py`
joins atoms into key signs afterwards, so passes never have to decide segmentation).

| tag | the shape on the leaf |
|-----|-----------------------|
| `0`-`9`, `10`, `12` ... | Arabic figures. A run of figures written together is ONE token (`12`, `20`, `24`, `109`). |
| `π` | pi-shaped sign (two legs under a bar) |
| `ß` | German sharp-s / beta shape |
| `∞` | two closed loops side by side (figure eight lying, "oo" joined) |
| `o` | one small closed circle |
| `λ` | lambda |
| `∂` | cursive d with its stem looped back to the left |
| `ſ` | long s (tall, descender, no crossbar) |
| `f` | f with crossbar |
| `¢` | c or small circle with a vertical stroke through it |
| `∠` | a lying v / angle open to the right |
| `+` | plain cross |
| `‡` | cross with two bars (dagger) |
| `#` | two verticals crossed by two bars |
| `=` | two short horizontal bars |
| `/` `//` `///` | one, two or three slanting strokes written as a group |
| `x` | small x; `X` large x-shaped cross |
| `T` | T; `⊥` inverted T |
| `E` | capital E (or epsilon-shaped ε) |
| `3` | the figure 3 or a z-shaped 3 (ȥ) |
| `a b c d e g h i j k l m n p q r s t u v w y z` | the Latin letter as written (write `p` for plain p; `ꝑ` for p with a loop or stroke through the descender) |
| `.` | a free-standing dot (keep it; it may be a null or part of a sign) |
| `^` | a superscript mark written above the preceding sign |

Doubtful sign: append `?` to the tag (`ß?`). Unreadable: `??`. Clear French words inside a cipher line: one
row with the sign column `=word` (e.g. `=de`). A superscript letter written above (e.g. `te` over Ma): `=^te`.

## Atlas from interlined leaves (LANE R5 G, 24 Sept 2026)

`tools/keys/key60_atlas/`: `atlas.tsv` (80 sign instances, 42 distinct tags, each with the contemporary interlined value
it sits under), `contact_sheet.png` (one crop per row, the box marks the approximate centre -- centres were placed from
reduced views and can be off by one sign; read the row's `context` column to pick the right glyph), `src/` (the two native
regions and three 1000 px overviews, `src/manifest.json` with URL and sha1). Sources: fr.3985 canvas 264 (Instruction of
31 Aug 1593, gloss written ABOVE each cipher line on this page, not below as Bourdeau's atlas60.md says for part of it --
the "de la couronne" run proves the direction: `g λ < X ++ ꝺo v T` sits under the gloss "de la couronne") and fr.3986
canvas 298 (f.152, Henri IV to Nevers, Oct 1593, gloss above). c.298 is a neater office hand than c.264 and than the
Revol copies; c.264 is the one to calibrate against. The values are the model's alignment of sign to gloss (grade S, not H).

Agreement with key60.tsv: 67 yes, 7 form (value agrees, this hand writes the sign so it reads as another tag), 2 partial,
4 no. The places where this hand and the key tags part company, which is what the F1-F3 passes tripped on:

| this hand writes | read as tag | gloss value | key60 says | consequence for a pass |
|---|---|---|---|---|
| `+o` | `to` | le | to = i, +o = le | the two are one shape here; decide by context (le vs i) |
| `20` | `ro` | u | 20 = u, ro = me | "ro" in a pass is probably 20 = u |
| `++` | `ll` / `11` with a bar | u | ++ = u | transcribe `ll`/`11` as `++` |
| `φ` | `f` with a loop | ca | f = e, φ = ca | a looped f is ca, a plain f is e |
| `X+` and `X++` | the same barred x | se / si | X+ = se, X++ = si | the hand does not separate them; value from context |
| `L40` | `Lo` (no 4) | qui | L40 = qui, Lo = fi | Lo before a vowel-less run is qui |
| `ꝑ` | p with stroke | e | ꝑ = so (M) | conflicts with the key; one instance only |
| `v` | open v | u (twice), o (once) | v = li, v' = u | v is not li in this hand |
| `σ` | o with tail | li | none | not in the key |
| `ll4` | ll with small 4 | p | none (10 = p, v+ = p) | not in the key; possibly v+ |

Not done (cap): the rest of c.264, c.266, c.268 and the other lines of c.298, which would add the rarer syllable and word
signs; f.151 (c.297 overview fetched, not cut). Suggestion: extend from c.264's lower half first (same hand as the copies).
