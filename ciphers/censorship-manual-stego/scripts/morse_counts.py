#!/usr/bin/env python3
"""Reference Morse element counts (dots, dashes, intra-word letter gaps, word gaps)
for the plaintext strings attested for the two censorship-manual mysteries.

International Morse Code is used as the REFERENCE alphabet only. The manual's own
caption for Illustration No. 11 (fashion drawing, p.14) explicitly says the drawing
uses "a system of Morse (not the usual dot and dash)" -- so these counts are a
baseline for comparing against a candidate carrier's element count, not a claim
that standard Morse was used. Run: python3 morse_counts.py
"""

MORSE = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
}

TEXTS = [
    ("mystery1a_en (manual p.14 caption, verbatim)",
     "HEAVY REINFORCEMENTS FOR THE ENEMY EXPECTED HOURLY"),
    ("mystery1a_de (Schmeh blog only -- NOT in the manual's own caption, see NOTES.md)",
     "MASSIVE FEINDVERSTAERKUNGEN WERDEN STUENDLICH ERWARTET"),
    ("mystery1b_en (manual p.14 caption, verbatim)",
     "BEFORE ARRAS"),
    ("mystery2_en (manual p.17 caption, verbatim, manual's own English translation)",
     "OIL HAS ARRIVED EVERYTHING IS READY GUSTAV AVAILABLE FOR THE APPOINTED DAY"),
    ("mystery2_de (Schmeh blog speculative back-translation only -- not in the manual)",
     "OEL IST ANGEKOMMEN ALLES IST FERTIG GUSTAV HAELT SICH AM VEREINBARTEN TAG BEREIT"),
]


def counts(text):
    words = text.upper().split()
    dots = dashes = letters = letter_gaps = 0
    for w in words:
        letters += len(w)
        letter_gaps += max(0, len(w) - 1)
        for ch in w:
            code = MORSE.get(ch)
            if code is None:
                continue
            dots += code.count('.')
            dashes += code.count('-')
    word_gaps = max(0, len(words) - 1)
    total_marks = dots + dashes
    return dict(letters=letters, dots=dots, dashes=dashes, total_marks=total_marks,
                letter_gaps=letter_gaps, word_gaps=word_gaps)


if __name__ == "__main__":
    for label, text in TEXTS:
        c = counts(text)
        print(f"{label}:")
        print(f"  text: {text}")
        print(f"  letters={c['letters']} dots={c['dots']} dashes={c['dashes']} "
              f"total_marks={c['total_marks']} letter_gaps={c['letter_gaps']} "
              f"word_gaps={c['word_gaps']}")
