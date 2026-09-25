es16: period Spanish corpus for the character-level language model, 25 Sept 2026.

Don Quijote Part I (Cervantes, 1605) fetched from Project Gutenberg #2000 (plain UTF-8 text, MANIFEST.tsv
lists the source). Same publication year as ciphers/na-oldenbarnevelt-2442-1605's target letter (23 Dec 1605),
same Castilian written register. This is a modern-orthography transcription of the 1605 text, not a
period-spelling diplomatic edition, so it under-represents obsolete spellings (x for j, doubled consonants,
etc.); good enough for a letter n-gram model at the digit-recovery scale this target needs, not for anything
finer.

donquijote1605_pg2000_body.txt is donquijote1605_pg2000.txt with the Project Gutenberg licence boilerplate cut
(everything before "*** START OF..." at line 24 and from "*** END OF..." at line 37704 on, both in English and
not part of the work) -- use the _body file for any language model or held-out control; the raw file's tail is
English licence text, not Spanish, and a held-out slice drawn from the raw file's last 10% lands in it (caught
25 Sept 2026 when a first control run decoded as English).
