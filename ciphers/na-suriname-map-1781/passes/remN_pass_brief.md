# Blind transcription pass: the "Remarque" paragraph of a 1781 Dutch manuscript map, native resolution (one crop set, 18 images)

GAPS16-na-suriname-map-1781 (account-4), 2 Oct 2026. You are one of two independent readers. You have NO key and must not
guess letter values. Transcribe the SHAPES of the cipher glyphs, line by line, and write one TSV file. Do not read any other
file (no NOTES.md, no key, no other passes): your value is that you are blind.

## The images (read each with the Read tool, one per Read, in this order)
Directory: SCRATCH/cremN/
- remN_L01_s1.jpg, _s2, _s3 -- the heading of a paragraph (one short word, larger letters; it may sit in segment s1 only,
  the rest of that band may be map drawing or empty).
- remN_L02_s1..s3 ... remN_L06_s1..s3 -- the paragraph, five lines, small chancery hand; L06 is a short last line, and one
  other line may be short too. Each line is cut into three segments s1, s2, s3 left to right, with about 150 px overlap
  between neighbours: do NOT write the overlapping glyphs twice -- start each segment where the previous one ended.
Thin straight ruled lines (map construction lines) cross some crops: ignore them. Neighbouring lines may intrude at the top
or bottom edge of a crop: transcribe only the line centred in the crop. Segments with no text: write nothing for them.

The text is a substitution cipher: each plaintext letter is replaced by one sign. Signs are (1) Latin-letter-shaped glyphs
(lowercase and capital, chancery hand), (2) Arabic digits used as letters (3, 4, 5, 6, 7, 8, 9 occur), (3) invented shapes,
and (4) a few drawn symbols that stand for whole words (e.g. a doubled A with a bar through it, a box with three spires).
Genuine numbers may be plain.

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
Write exactly one file: SCRATCH/PASSFILE
Tab-separated, header: crop	glyphs	conf	note
  one row per LINE (not per segment): crop = remN_L01 ... remN_L06, glyphs = the whole line, s1 then s2 then s3 joined;
  conf = H/M/L; note = anything another reader needs (where a segment joins, uncertain glyphs by position).
Then reply with one line: the file path and the glyph count per line.
