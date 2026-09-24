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
