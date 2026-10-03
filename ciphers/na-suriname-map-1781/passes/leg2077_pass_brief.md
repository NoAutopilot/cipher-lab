# Blind transcription pass: the title and legend block of a 1781 Dutch manuscript map, native resolution (20 lines, 40 images)

GAPS19-na-suriname-map-1781 (account-4), 3 Oct 2026. You are one of two independent readers. You have NO key and must not
guess letter values. Transcribe the SHAPES of the cipher glyphs, line by line, and write one TSV file. Do not read any other
file (no NOTES.md, no key, no other passes, no other image): your value is that you are blind.

## The images (read each with the Read tool, one per Read, in this order)
Directory: /home/user/cipher-lab/ciphers/na-suriname-map-1781/images/crops_2077_leg/
- leg77_L01_s1.jpg, leg77_L01_s2.jpg ... leg77_L20_s1.jpg, leg77_L20_s2.jpg (do NOT open leg77_lines_debug.jpg).
- L01-L03: a three-line title (large letters), all cipher. L04: a plain heading. L05-L19: a lettered legend; entries start
  with plain labels "a,", "b,", ... and are EITHER cipher OR plain Dutch (e.g. "Menagerie", "huijs voor den Opsigter"), often
  both on one line; some entries run over to the next line. L16 is a SHORT fragment at the left (a word carried down from L15):
  transcribe only that fragment. L20: one line below the legend.
Each line is cut into two segments s1, s2 left to right, with about 150 px overlap: do NOT write the overlapping glyphs twice --
start s2 where s1 ended. Neighbouring lines intrude at the top or bottom edge of most crops (the lines are close together):
transcribe ONLY the line centred in the crop. Map drawing or a long diagonal ruled line crossing a crop: ignore it.

The cipher is a substitution: each plaintext letter is replaced by one sign. Signs are (1) Latin-letter-shaped glyphs
(lowercase and capital, chancery hand), (2) Arabic digits used as letters (3, 4, 5, 6, 7, 8, 9 occur), (3) invented shapes,
and (4) a few drawn symbols that stand for whole words (e.g. a doubled A with a bar through it, a box of spires, a ladder #).

## How to write a glyph
Shape codes (SHAPE names only):
  [h-loop] h with looped ascender; [l-bare] bare vertical stroke; [delta] hollow triangle; [s-loop] chancery long-s/loop
  shape (S/p-like); [ezh-dot] reversed 3 / ezh with a dot; [o-plain] plain o; [v-tall] tall looped V; [hash] 2-3 stroke
  ladder/# mark; [lambda] open hooked stroke like Greek lambda; [psi] trident / Greek psi; [pi] bar over an inverted V;
  [thorn] large looped capital C/epsilon-like initial with a curl below the line; [f-loop] long f with loops above and
  below; [u-dots] y/u with two dots above (two dots over any other letter: [x-dots] where x is that letter); [d-loop] looped
  script d (stem curling back left); [d-hook] a 6- or delta-like bowl with a tall ascender hooked right; [w-tilde] w/omega
  with a bar or tilde above; [MM] doubled A with a crossbar; [hand-box] box of vertical bars with pointed tops; [4-bowl] a 4
  with a closed bowl; [dash] a long dash on the line; [tilde] a standalone wave mark; a letter with a dot or grave above:
  [a-dot], [a-grave], [delta-grave] etc.
Latin-shaped glyphs and digits: write the character (c, G, y, b, g, q, 5, 7, ...). Keep case as drawn. Distinguish g (9-like
bowl with a curved or looped descender) from q (bowl with a straight descender) and from 9 (a 9 sitting on the line) as best
you can and say in the note when unsure. Other shapes: invent a short bracketed code and use it consistently. Glyphs of one
word separated by single spaces, words by " / ". Unresolvable glyph: [?].
PLAIN text (labels a, b, ...; plain Dutch words; numbers): write each plain word as <...> with its exact spelling as drawn
(e.g. <f> <Menagerie> ; <g> <huijs> <voor> <den> <Opsigter>), including ij/ÿ as you see it. Punctuation as <,> <.> <;>.

## Output
Write exactly one file: PASSFILE
Tab-separated, header: crop	glyphs	conf	note
  one row per LINE (not per segment): crop = leg77_L01 ... leg77_L20, glyphs = the whole line, s1 then s2 joined;
  conf = H/M/L; note = anything another reader needs (where the segments join, uncertain glyphs by position).
Then reply with one line: the file path and the glyph count per line.
