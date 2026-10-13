# Blind shape pass (SUR-LEGK, 13 Oct 2026): one cipher word on a 1781 Dutch manuscript map

You are one of two independent readers. You have NO key and must not guess letter values. Read exactly one image and
nothing else in the repository (no NOTES.md, no key, no other passes, no other images): your value is that you are blind.

Image: /home/user/cipher-lab/ciphers/na-suriname-map-1781/images/crops_2039_legk/legk_entry_x4.jpg
It shows one enciphered word (a substitution cipher: one sign per plaintext letter; signs are Latin-letter shapes in a
chancery hand, digits used as letters, and invented shapes), enlarged 4x. The word ends at the comma; the small letter
after the comma (right edge) is a plain label for the NEXT entry, not part of the word -- do not transcribe it.

## Shape codes (shape names only, no values)
Write each sign with one code. Use the character itself for a sign that looks exactly like a Latin letter or digit (keep
case). Bracketed codes available (use one only if it fits; invent a short descriptive bracketed code otherwise):
  [psi]          trident / Greek psi with a long stem
  [ij]           a dotted i and a dotted j written together as ONE ligature sign (two dots, one descender)
  [y-loop]       a y-like sign with a small loop above
  [d-loop]       a script d whose ascender loops back down to the left
  [delta-small]  a small round bowl whose ascender curls back over the bowl with a flag (like a Greek delta)
  [lambda]       an open hooked stroke like a Greek lambda
  [hash]         a 2-3 stroke ladder / tally mark
  [?]            cannot resolve
Separate signs by single spaces.

## Two questions to answer explicitly
Q1. Between the first sign and the "a"-shaped sign there are dotted strokes. Count how many SEPARATE signs that stretch is
(1 or 2) and give the code(s). Say how many dots you see, which stroke(s) carry a descender, and whether the strokes touch.
Q2. The sign immediately after the "w"-shaped sign: which code, and describe what its ascender does (straight, loops back
down, curls back over the bowl with a flag, ...).

## Output
Write exactly one file: PASSFILE
Tab-separated, header:  pos	code	conf	note
pos = 0,1,2,... left to right over the word's signs only; conf H/M/L; note = what you saw (alternatives as "or ...").
Then reply in at most six lines: the full code string, your Q1 answer (count, codes, dots, descender, touching), your Q2
answer (code and ascender description), and nothing else. Do not edit any other file, do not run git.
