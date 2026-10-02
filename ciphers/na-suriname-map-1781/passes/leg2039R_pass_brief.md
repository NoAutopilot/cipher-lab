# Blind transcription pass: RIGHT-HAND STRIP of the enciphered legend block of a 1781 Dutch manuscript map (one crop set, 15 images)

You are one of two independent readers. You have NO key and must not guess letter values. Transcribe the SHAPES of
the cipher glyphs, line by line, from the crops listed below, and write one TSV file. Do not read any other file in
the repository (no NOTES.md, no key, no other passes): your value is that you are blind.

## The images

Directory: /tmp/claude-0/-home-user-cipher-lab/7e308e82-f546-5684-a8a8-f29dd2fbba53/scratchpad/crops_2039_right/
Files: leg2039R_L01.jpg ... leg2039R_L15.jpg (15 horizontal bands, L01 at the top of the block, L15 at the bottom;
each band holds about two text lines; each band is ONE segment, 1300 px wide). These crops are the RIGHT-HAND STRIP
of the block: the left edge of every crop is NOT the start of a line -- the lines begin further left, outside the
crop, and run into it, so a crop usually starts mid-word or mid-clause (the first glyph may be cut in half: write
[?] for a half glyph and say "cut at left edge" in the note). What you are reading is the END of each line: the
right-hand part of each legend entry, and any short entries whose label letter sits in the right-hand column of the
block (some label letters -- a plain d, h or p -- may appear INSIDE these crops with their own short clause after
them, where a long line ends early and a new entry starts in the right-hand column). Read EVERY image with the Read
tool, one image per Read, in order L01, L02, ... L15. Bands may begin or end mid-line (a line can be split across two
neighbouring bands): say so in the note column. Write every line you see in a band, including lines with only a
few glyphs or only a flourish, and say in the note whether the line's ink reaches the crop's right edge or ends
in blank space before it.

What the block is: the top of the block has a title (two or three larger lines), then a heading, then a lettered
legend list -- each entry begins with a small plain label letter (a, b, c, ... up to about u, in the plain Latin
alphabet, probably followed by a stroke or stop) and then a description written in CIPHER. The cipher is a
substitution: each plaintext letter is replaced by one sign. The signs are a mix of (1) Latin-letter-shaped glyphs
(lowercase and capital, in a chancery hand), (2) Arabic digits used as letters (4, 5, 6, 7 are known to occur), and
(3) invented shapes. Arabic numerals that are genuinely numbers (gun counts, weights) may also appear in plain.
Place names and the label letters are plain.

## How to write a glyph

Use these shape codes where a glyph matches the description (they are SHAPE names only, no letter values are given
to you on purpose):
  [h-loop]   lowercase h with a looped ascender
  [l-bare]   a bare vertical stroke, no crossbar, no loop (like a tall l or a 1 without a flag)
  [delta]    a hollow wedge / closed triangle, like a Greek capital Delta or an A without crossbar
  [s-loop]   a chancery long-s / loop shape with a tall loop (S/s/p-like)
  [ezh-dot]  a reversed-3 / ezh shape, usually with a dot beside or inside it
  [o-plain]  a plain circular o
  [a-plain]  a plain round-bowl lowercase a
  [v-tall]   a tall looped V / J ascender shape
  [hash]     a 2-3 stroke ladder / tally / # mark
  [lambda]   an open hooked stroke like a Greek lambda
  [tilde]    a tilde-like wave mark standing on its own
Latin-shaped glyphs and digits that look exactly like a Latin letter or a digit: write the character itself (c, G,
y, 5, 7, 4, 6, m, ...). Keep case as drawn. For any other shape invent a short bracketed code that DESCRIBES it,
e.g. [z-tail], [x-dot], [3-caret], [w-loop], and use the same code every time the same shape recurs. Separate the
glyphs of one cipher word by single spaces, and words by " / ". Doubled marks ("##") are written as [hash] [hash].
A glyph you cannot resolve: [?]. A plain word (a place name, a number): write it in angle brackets, e.g. <Holland>,
<12>. A plain label letter at the start of an entry goes in the label column, not in the glyph string.

## Output

Write exactly one file: /tmp/claude-0/-home-user-cipher-lab/7e308e82-f546-5684-a8a8-f29dd2fbba53/scratchpad/PASSFILE
Tab-separated, header:  band	line	label	glyphs	conf	note
  band  = L01..L15; line = 1 or 2 within the band (3 if a third line shows); label = the plain label letter
  if a label letter is VISIBLE inside this crop on that line (else empty -- most lines here are continuations
  whose label sits outside the crop to the left); glyphs = the string described above; conf = H (every glyph clear),
  M (one or more glyphs uncertain) or L (mostly uncertain); note = anything another reader needs (cut at the band edge, cut at the left edge, "ink ends at x~900, blank
  to the right edge", "line reaches the right edge", alternatives for a glyph such as "pos3 could be [delta] or [a-plain]").
Then reply with a five-line report: lines read, entries with a plain label (list the labels in order), how many
distinct shape codes you used, which bands were hardest, and nothing else. Do not edit any other file, do not run
git, do not look at anything outside the crops directory.
