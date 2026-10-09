You are a blind transcriber of an 18th-century Dutch manuscript page. Work ONLY from the image files listed below; do not
open any other file in the repository, do not search the web, do not try to decipher anything.

The page alternates two kinds of line: (1) a lighter, smaller line of ordinary Dutch handwriting ("gloss"), and (2) a
heavier line of cipher signs (Latin-letter-like shapes, digits, Greek-like signs and a few special signs), which may also
contain a few words in ordinary handwriting. Each crop is centred on ONE line; parts of the lines above and below may show
at the edges -- transcribe only the line at the vertical centre of the crop.

Crops (read in this order): /home/user/cipher-lab/ciphers/na-suriname-map-1781/images/sur372/372_0189_right_native_L01.jpg
through ..._L27.jpg (L01, L02, ... L27).

For each crop write one output row: crop id<TAB>kind<TAB>content
- kind = gloss | cipher | other
- gloss: the Dutch words exactly as written (keep the spelling; '?' for an unreadable letter; '[...]' for an unreadable word).
- cipher: one code per sign, separated by single spaces. Write '_' where the writer leaves a visible gap between sign
  groups. Write words in ordinary handwriting that sit inside a cipher line in braces, e.g. {20 Dec.}. Punctuation
  (comma, colon, full stop, dash) as itself. Unsure sign: '?' (or best guess followed by '?', e.g. 8?).
- If the centre line of a crop is the same line you already transcribed in the previous crop, write kind = other, content = dup.

Sign codes (shape names only; use exactly these):
  digits: 0 1 2 3 4 5 6 7 8 9
  lowercase Latin look-alikes: a b c d e f g h k l m n o p q r s t v w x y
  [ij]       y or ij with two dots above (ÿ)
  [lambda]   Greek lambda (λ)
  [psi]      Greek psi / trident (ψ)
  [delta]    triangle (Δ)
  [pi]       bar over an inverted V / Greek pi
  [sigma]    o / 6-like loop with a long bar or stroke to the right
  [hash]     three uprights crossed by two bars (#)
  [amp]      loop crossed by a diagonal stroke (&-like)
  [omega-bar] omega / w with a bar above
  [x-cross]  slanted cross / x with a long stroke (×-like, larger or more cross-like than the letter x)
  [x-dots]   x-like stroke with dots
  [sh-lig]   long s / f with a loop, h-like
  [s-dollar] S with a vertical stroke ($-like)
  [tau]      curly tau
  [I-bar]    bold I with a crossbar
  capital script letters when clearly a capital distinct from the lowercase: A B C D E G H L N P R S Y
  [other:description] for any sign not in this list (describe it briefly).

Write all rows to the output file named in your task, as plain TSV, no header, then reply with only: the number of rows,
how many are cipher lines, and the three signs you were least sure of.
