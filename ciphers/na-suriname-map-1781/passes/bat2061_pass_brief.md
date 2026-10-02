# Blind transcription pass: enciphered legend block of a 1781 Dutch manuscript map (one crop set, 20 images)

You are one of two independent readers. You have NO key and must not guess letter values. Transcribe the SHAPES of
the cipher glyphs, line by line, from the crops listed below, and write one TSV file. Do not read any other file in
the repository (no NOTES.md, no key, no other passes): your value is that you are blind.

## The images

Directory: /tmp/claude-0/-home-user-cipher-lab/d4feee8f-4acd-5367-9fa7-f36854ce6cca/scratchpad/crops_2061/
Files: bat2061_L01_s1.jpg ... bat2061_L10_s2.jpg (10 bands, one text line each, L01 at the top; each band is cut
into two segments: _s1 the LEFT part (x 0-1300) and _s2 the RIGHT part (x 1100-2300), sharing a 200-px overlap -- read
_s1 then _s2 and merge the line, do not transcribe the overlap twice). Read EVERY image with the Read tool, one image
per Read, in order L01_s1, L01_s2, L02_s1, ... Ignore the file bat2061_lines_debug.jpg.

What the block is: a numbered list "No 1," ... "No 6," (the "No" and the number are plain), each followed by a mix of
plain Arabic numerals (counts, weights), a recurring plain-looking capital monogram (write it [MM] if it looks like a
doubled/ligatured M), small plain-looking marks, and CIPHER words; then a centred heading line in cipher; then a
lettered legend (plain label letters a, b, c, ... g, each followed by a stop or comma, then a description in CIPHER),
which runs over three lines. The cipher is a substitution: each plaintext letter is replaced by one sign. The signs
are a mix of (1) Latin-letter-shaped glyphs (lowercase and capital, in a chancery hand), (2) Arabic digits used as
letters, and (3) invented shapes. Genuine numbers may also appear in plain: when a digit group stands directly
before or after [MM] or is preceded by "No", treat it as a plain number <..>; a digit standing inside a cipher word
is a glyph. A legend line holds several entries: put each entry on its own output row (same band, line 1, 2, 3 ...)
with its label, and a continuation of the previous entry on its own row with an empty label.

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
A glyph you cannot resolve: [?]. A plain word (a place name, a number, "No"): write it in angle brackets, e.g. <Holland>,
<12>. A plain label letter at the start of an entry goes in the label column, not in the glyph string.

## Output

Write exactly one file: /tmp/claude-0/-home-user-cipher-lab/d4feee8f-4acd-5367-9fa7-f36854ce6cca/scratchpad/PASSFILE
Tab-separated, header:  band	line	label	glyphs	conf	note
  band  = L01..L10; line = 1, 2, 3 ... one row per entry within the band; label = the plain label letter
  if the line is a legend entry (else empty); glyphs = the string described above; conf = H (every glyph clear),
  M (one or more glyphs uncertain) or L (mostly uncertain); note = anything another reader needs (cut at the band
  edge, overlap merged, alternatives for a glyph such as "pos3 could be [delta] or [a-plain]").
Then reply with a five-line report: lines read, entries with a plain label (list the labels in order), how many
distinct shape codes you used, which bands were hardest, and nothing else. Do not edit any other file, do not run
git, do not look at anything outside the crops directory.
