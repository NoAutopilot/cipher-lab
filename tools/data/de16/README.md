# de16: German (Early New High German) language-model text

`composed_enhg.txt` (S1, 24 Sept 2026): about 8.5 KB written for this repository by the model in 16th-century
chancery German (a Luther 1545 Genesis 1 passage from memory, then letter formulae and news-letter prose in the
style of the Saxony-Orange correspondence). It is NOT a historical source and must never be cited as one; it only
supplies n-gram statistics to `tools/homophonic_anneal.py`. Its topics overlap the 1561-64 letters (Spain, France,
Netherlands news), which helps a solver but also means a reading must be judged against a matched control whose
plaintext is NOT in the corpus (the controls use the 74 decipherment, align_74.txt, which is excluded).
