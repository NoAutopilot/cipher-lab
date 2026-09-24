# LANE G3 worker C: DC8 Baluze 156 f.157-158, letter-symbol half against Lasry's Sabran key (Opus, cap $5, disk + cryptiana only)

Target: ciphers/decode-2754-bnf-baluze156-1636. Read NOTES.md in full (numeral half: clean negative with control; letter-symbol half untested),
ciphertext_draft.tsv, key_sabran_1631.tsv, images/ (dc8_f157r/v, f158r).
Job (LANE G2 handoff priority 5): get the letter-symbol alphabet of George Lasry's published Sabran (1631) key from the Cryptiana pages the notes
cite (sources/cryptiana/web/GL.htm and louisxiii.htm; fetch the key image from cryptiana.web.fc2.com once if it is not on disk; at most 6 requests).
Transcribe it to key_sabran_1631_letters.tsv (grade M where the image is small). Match the DC8 symbols to it by shape, decode the letter-symbol
tokens, and score the result against a matched control (the same symbol-to-letter mapping shuffled, 1000 draws, French bigram/word score, and a
synthetic French text enciphered with the key at the same length). Report both numbers. If it reads: decode.json + tools/decode_key.py --check,
grades per token (H only where the key image is legible, S/M otherwise). If it does not: a negative with the control, and say what remains
untested. Also note whether the doubled-letter tokens (tt, ll, nn, ff) fit the key. No Gallica fetches. NOTES.md section
'Letter-symbol half (24 Sept 2026)'. Readings go for LANE V3.
