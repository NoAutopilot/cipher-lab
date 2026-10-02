# Blind transcription pass: BnF fr.3252 f.100r, digit cipher (BIRAGO-NUM, 2 Oct 2026)

You transcribe a 16th-century Italian hand writing a cipher of digits. You do not decode anything.
Crops: ciphers/birago-fr3252-1571-72/images/f100/f100_LNN_s1.jpg and _s2.jpg, NN = 01..11 (22 files). Each line
is cut into two segments at a fixed x; s2 continues s1 directly (a digit can be split at the seam: write it once,
in the segment where most of it is, and flag the seam in the note column).

Hand forms (read these as digits):
- 4 looks like a "+" or a "t" with a tail (open-topped 4). It is the commonest digit. Write 4.
- 5 looks like a long "s". Write 5.
- 9 looks like a "g". Write 9.
- 1 is a short stroke, often WITH a dot above (looks like "i"). Write i for a dotted 1, 1 for an undotted 1.
- 2, 3, 6, 7, 8, 0 as usual.
Other signs:
- lower-case letters set into the digit stream: m, n, h, f (maybe others: c, a, l). Write the letter.
- a wavy sign like a tilde or division sign "÷" standing on the line: write |  (it brackets the cipher with "76").
- marks ABOVE a single digit: dot "." (one dot; NOT the dot of an i), two dots ":", bar "-", cross "+",
  wavy "~". Append the mark to that digit: 2. 8- 4: 7+ .
Line L01: only the part after the clear words "harebbe a caro" is cipher; start with the "76".
Line L08: the cipher ends before the clear words "Io dico la pura et mera uerita"; transcribe digits on both sides
of that clear phrase, and write the clear phrase as the single token CLEAR where it falls.
Line L11 ends the cipher (last token at the right).

Output: a TSV, one row per line segment: `line<TAB>seg<TAB>tokens<TAB>note`. tokens = every sign in reading order,
separated by single spaces (e.g. `8 4 0 i 3 3 9 2 9 3 0 8 2. 4 i`). note = anything doubtful (position and the two
readings you hesitated between), or empty. Read every crop yourself at full size; zoom (crop/enlarge with PIL) any
part you are unsure of. Do not guess a pattern from other lines. Do not decode.
