# Blind transcription pass prompt (N4-ES132B, 4 Oct 2026, copied from run2/pass_prompt_f120r.md with only the page and line count changed), used verbatim for pass A and pass B of f90r
You are transcribing a 16th-century Spanish cipher written in numerals with small marks. You see ONLY line crops. Do not
guess meaning; do not try to decipher. Read each crop image with the Read tool, in order, and transcribe every token.

Crops: /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/images/f90r_LNN_s1.jpg and _s2.jpg for NN = 01..27 (the page has two paragraphs: L01-L21 and L22-L27) (a band may fall in a blank gap between paragraphs: write the row with no tokens)
(s1 = left half, s2 = right half of the same line; the halves overlap a little at the join: do not duplicate tokens there).
Each crop may show parts of the lines above/below at its edges: transcribe only the line centred in the crop.

Notation, one token per numeral group, space separated:
- the number as written (e.g. 21, 236, 12). A long number may be a base plus a hooked vowel sign: write what you see; if the
  last stroke is a hook that looks like a 6, write 6.
- a vowel sign written right after the number: '+' (small cross/plus), '.' (dot), 'ρ' (a looped 'e'-like or 'p'-like tail),
  'σ' (a hook like a small 6 that is not clearly a digit), '⊣' (a u-like hook). Write it straight after the number: 21. 12+ 24ρ
- a mark ABOVE the number, written after any vowel sign with '@' and a shape name: @hat (^ circumflex), @bar (straight
  horizontal bar/macron), @acute (' short slanted stroke), @tilde (a wavy ~ stroke), @rmark (a small v- or r-shaped hooked mark, like a tiny letter r or v; if unsure between these two write @tilde?), @dots (two dots),
  @cross (a small + above), @other (any other shape). Several marks: write each, e.g. 23+@dots, 7ρ@hat
- an underline under the number: write '_' right after the number (35_)
- a word in ordinary letters (e.g. y, a, Bul, Rom, Lum, quam, nel, mil, cul): write it in braces {Bul}; the single letter
  y alone may be written y.
- the slash '/' as /. Clear Spanish handwriting (not cipher) at the start of a line: write it as one token {CLEAR:...}.
- unreadable: write your best guess followed by '?' (e.g. 23?), or '?' alone.
Output: a TSV, one row per line: LNN<TAB>tokens. First line a comment starting '# blind pass'. Nothing else.
Write the file to the path you are given, and reply only "done N lines".

Added for both passes of this page alike (N4-ES132B, after the 'Each crop' line): The paper shows faint mirror-image writing bleeding through from the other side: ignore it, transcribe only the dark ink. Small numerals or marks standing alone in the far right margin, outside the text block, are later marginal notes: leave them out. Output header and path given per pass.
