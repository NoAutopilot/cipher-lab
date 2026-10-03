# Blind transcription pass: the legend block of a 1781 Dutch manuscript map, native resolution (one crop set, 22 images)

GAPS18-na-suriname-map-1781 (account-4), 3 Oct 2026. You are one of two independent readers. You have NO key and must not
guess letter values. Transcribe the SHAPES of the cipher glyphs, line by line, and write one TSV file. Do not read any other
file (no NOTES.md, no key, no other passes, no other image): your value is that you are blind.

## The images (read each with the Read tool, one per Read, in this order)
Directory: /home/user/cipher-lab/ciphers/na-suriname-map-1781/images/crops_2046_leg/
- leg46_L01_s1.jpg, leg46_L01_s2.jpg ... leg46_L11_s1.jpg, leg46_L11_s2.jpg (do NOT open leg46_lines_debug.jpg).
- L01, L02: a two-line title (larger letters, centred). L03: a heading. L04-L06: three lines that begin with a plain label
  "No.1." / "No.2." / "No.3." and mix plain numbers with cipher. L07: a second heading. L08-L11: a lettered list, entries
  starting with plain labels "a.", "b.", ... (several entries per line).
Each line is cut into two segments s1, s2 left to right, with about 150 px overlap: do NOT write the overlapping glyphs
twice -- start s2 where s1 ended. Map drawing at the left edge of some crops: ignore it. Neighbouring lines may intrude at the
top or bottom edge of a crop: transcribe only the line centred in the crop.

The text is a substitution cipher: each plaintext letter is replaced by one sign. Signs are (1) Latin-letter-shaped glyphs
(lowercase and capital, chancery hand), (2) Arabic digits used as letters (3, 4, 5, 6, 7, 8, 9 occur), (3) invented shapes,
and (4) a few drawn symbols that stand for whole words (e.g. a doubled A with a bar through it, a box with three spires).
Genuine numbers, the line labels (No.1., No.2., No.3.; a., b., c., ...) and gun counts/calibres (e.g. 1., 2, 24, 18, 6, 8) may be PLAIN: write them as <...> with the exact text.

## How to write a glyph
Shape codes (SHAPE names only):
  [h-loop] h with looped ascender; [l-bare] bare vertical stroke; [delta] hollow triangle; [s-loop] chancery long-s/loop
  shape (S/p-like); [ezh-dot] reversed 3 / ezh with a dot; [o-plain] plain o; [v-tall] tall looped V; [hash] 2-3 stroke
  ladder/# mark; [lambda] open hooked stroke like Greek lambda; [psi] trident / Greek psi; [pi] bar over an inverted V;
  [thorn] large looped capital C/epsilon-like initial with a curl below the line; [f-loop] long f with loops above and
  below; [u-dots] y/u with two dots above; [d-loop] looped script d (stem curling back left); [w-tilde] w/omega with a bar
  or tilde above; [MM] doubled A with a crossbar; [hand-box] box of vertical bars with pointed tops; [4-bowl] a 4 with a
  closed bowl; [dash] a long dash on the line; [tilde] a standalone wave mark.
Latin-shaped glyphs and digits: write the character (c, G, y, b, g, q, 5, 7, ...). Keep case as drawn. Distinguish g (9-like
bowl with a curved or looped descender) from q (bowl with a straight descender) and from 9 (a 9 sitting on the line) as
best you can and say in the note when unsure. Other shapes: invent a short bracketed code that describes them and use it
consistently. Glyphs of one word separated by single spaces, words by " / ". Unresolvable glyph: [?]. Plain word or number:
<...>. Punctuation (comma, full stop) as <,> <.>.

## Output
Write exactly one file: PASSFILE
Tab-separated, header: crop	glyphs	conf	note
  one row per LINE (not per segment): crop = leg46_L01 ... leg46_L11, glyphs = the whole line, s1 then s2 joined;
  conf = H/M/L; note = anything another reader needs (where the segments join, uncertain glyphs by position).
Then reply with one line: the file path and the glyph count per line.
