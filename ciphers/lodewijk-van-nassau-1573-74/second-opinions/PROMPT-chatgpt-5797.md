# Second-opinion prompt: WVO 5797 (Jan and Lodewijk van Nassau to Orange, 22 Oct 1573)

Paste everything below the line into the model. File the answer verbatim as `<model>-<date>.md` in this folder.

---

I am checking whether two specific words in a sixteenth-century cipher letter have ever been printed or
deciphered anywhere. Please answer only with exact citations: author, title, volume, year, and page or letter
number. Say plainly when you do not know. Do not guess.

The letter is from Jan and Lodewijk (Louis) of Nassau to their brother William of Orange, Dillenburg, 22 October
1573. It is numbered 5797 in the Huygens ING database "Briefwisseling van Willem van Oranje" (original: Koninklijk
Huisarchief, The Hague, A 3, 895/I, a minuut). It is mostly in clear German and French, with several short passages
in numeral cipher that Groen van Prinsterer printed as blanks in 1837:

Groen van Prinsterer, Archives ou correspondance inedite de la maison d'Orange-Nassau, 1re serie, tome IV
(1837), Lettre CDXLIV, pp.217-226.

Two of Groen's blanks are at:
- p.223-224: "Bey dem Herzog von Sachsen und [blank] ist willens ..." (the Duke of Saxony and the blank is
  willing to ...)
- p.225: "[blank] helt sich wol und thut in warheit viel" (the blank fares well and truly does much)

Already checked, and neither blank found filled in any of them: Groen's Archives, both series, every Internet
Archive copy (1re serie I-VIII plus Supplement, 2e serie I-V); Gachard, Correspondance de Guillaume le Taciturne
I-VI; Blok, Correspondentie van en betreffende Lodewijk van Nassau (Werken Historisch Genootschap n.s. 47, 1887,
checked page-by-page via HathiTrust Extracted Features for the words around each blank); Glawischnig, Niederlande,
Kalvinismus und Reichsgrafenstand (1973, full-text search inside the Internet Archive lending copy); Rachfahl,
Wilhelm von Oranien; the WVO catalogue record for 5797 itself (which names only Groen's edition and notes cipher
passages, no solution); Tomokiyo's Cryptiana pages; the solver repositories dbourdeau/cyphersolver and
aaymeloglu/unsolved-ciphers (grepped for Nassau/Lodewijk/Dillenburg/5797/Pfaltzgraf/Landgraf); Google Books,
OpenAlex, CrossRef and Semantic Scholar (name-phrase queries in German and French).

Questions:
1. Is either blank -- the one before "ist willens" (p.223-224) or the one before "helt sich wol" (p.225) -- ever
   filled in, quoted, or discussed as deciphered anywhere in print? Check especially any edition or study of the
   Nassau-Orange correspondence of 1573-1574, any study of the "Wetterauer Grafenverein"/Grafeneinigung of 1573,
   and G. Schmidt's Der Wetterauer Grafenverein (1989), which this search could not open inside.
2. Does a contemporary decipherment or interlinear gloss of 5797 itself (as opposed to a sibling letter) survive
   in another archive, for example the Nassau papers in Wiesbaden (HHStA Abt. 170/171) or elsewhere in the
   Koninklijk Huisarchief?
3. Has any study of this specific letter, or of the October 1573 negotiations it describes (the Palatine and the
   Landgrave of Hesse's support for the Nassau brothers), been published that would name these two code values?

---
Note (parent worker PR-LAND-4, 26 Sept 2026): this prompt is new, queued as SO-LODEWIJK-5797. The two blanks are
code 161 ("Landgraf") and code 153 ("Pfaltzgraf"), N4 after two audits (V8-NA5797, V8-NA5797-2/A2), key `period`
(the two name values, from the contemporary interlinear gloss on sibling letter WVO 5550) plus `ours` (the
surrounding letter table, our own cryptanalysis). The safe sentence quoted below is AUDIT.md's A2.5, confirming
V8.6 unchanged after the second adversarial audit -- **not** A4.3, which the queueing note named: A4.3 covers a
different spot in the same letter (p6_spot4, code 172, before "zeuget diesen morgen Kölln"), withdrawn from
classification entirely after a three-way value conflict (AUDIT.md A4), and is not part of this prompt's subject.

Quoted verbatim, AUDIT.md A2.5's safe sentence: "In WVO 5797 (Jan and Lodewijk van Nassau to Orange, 22 Oct
1573), printed by Groen van Prinsterer in 1837 with several passages left undeciphered, two of the blanks read
in part, 'the Palsgrave (Pfaltzgraf) holds well' and '... and the Landgrave ...', by locating them with a letter
table recovered by our own cryptanalysis and valuing the two name codes from a contemporary interlinear gloss on
the sibling letter WVO 5550; no prior decipherment of these blanks located (N4); the letter's other text is
Groen's." Unsafe: "we deciphered Lodewijk's 22 Oct 1573 letter", "the missing passages of Groen's CDXLIV are now
read", "first decipherment", "newly recovered names", or any sentence that calls the p5 blank fully read (two
further codes in the same blank, 136 and 146, sit unread) or calls the two name values ours (they are the 5550
gloss's, key `period`). Never use the words first, new, unpublished, unread or never printed about our reading
(rule 10).
