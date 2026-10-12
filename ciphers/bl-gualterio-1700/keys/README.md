# keys/ (bl-gualterio-1700)

`hmc6_gualterio.tsv`, `hmc6_sicily.tsv`: the Stuart court's cipher with Cardinal Gualterio (cant-name nomenclator plus
"Key to the figure cipher used with the above cipher", two numbers per letter) and with the King of Sicily (cant-name
nomenclator plus "Alphabet a double chiffres"), as printed in HMC, *Calendar of the Stuart Papers belonging to His Majesty
the King* vol. VI (1916), introduction pp. lxxvi-lxxxiii (archive.org `calendarofstuart06grea`, leaves n81-n88). Paired
by GUALT-HMC, 12 Oct 2026, from the item's djvu.xml word coordinates (`hmc6_rows_ocr.tsv`) with eye corrections on the
strip crops in `../images/hmc6/`; rebuild and check with `python3 build_hmc6_keys.py --check`. Columns: code (cant name or
figure), meaning, kind (letter/name/word; groups of people are `word`), grade (H: leaf image-checked, n81/n83/n86/n88;
M: leaf not image-checked, OCR only), leaf, page, note. Not tested against any ciphertext (none on disk). These are not the
Vernon-Gualterio key (Add MS 20582 f.74b).
