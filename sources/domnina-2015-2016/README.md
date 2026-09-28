# Domnina 2015 + 2016 (Spinelli brothers' private cipher) -- snapshot record

Fetched 28 Sept 2026, 05:57 UTC (campaign runner spinelli-beinecke-c1515, step H6, session_0189W7KLRRUSFLgi5iPbBYph)
from the Wayback Machine, not from the live host: the file's live URL
`https://istina.msu.ru/media/publications/article/a81/378/11992054/Domnina_Spinelli_cipher_EnglishRussian_-_kopiya.pdf`
(the one `sources/cryptiana/web/henryvii.htm` links as "updated pdf") answered 404 live on 27 Sept 2026 (INTAKE-SPINELLI)
and the CDX index's own last capture (16 Sept 2026) is a 404 too. Snapshot used:
`https://web.archive.org/web/20221111182436if_/<that URL>` (capture of 11 Nov 2022, 16,231,739 bytes as served,
sha256 e4e618d6a3b22da3f722f8cbf65b99c5f982d83d1986d0616ed9912dc49b3b32; two further full captures exist,
14 Mar 2024 12:51:22 and 12:51:25). The PDF itself (16 MB, ABBYY OCR layer, AES-encrypted for copying) is NOT
committed -- re-fetch it from that URL; the first attempt reset mid-transfer through the proxy, the single retry
with `--http1.1` completed. Kept here, unmodified: the OCR text layer as PyMuPDF extracts it (`domnina_pdf_ocr_text.txt`,
pages separated by form feeds; the Cyrillic-font OCR of the English pages is garbled in places) and the three
embedded page images that carry the cipher material (JPEG q88 of the PDF's own embedded scans).

The 27-page file is two items bound together:
- pp. 1-16: Ekaterina Domnina, "Ciphers in Early Tudor Diplomacy" (English), offprint from *Geheime Post. Kryptologie
  und Steganographie der diplomatischen Korrespondenz europaeischer Hoefe waehrend der Fruehen Neuzeit*, ed.
  Anne-Simone Rous and Martin Mulsow, Historische Forschungen 106, Duncker & Humblot, Berlin 2015 (printed pp. 179-194
  by the running heads). PDF p. 7 = printed p. 186: **Fig. 1, "The key to the private cipher of Tommaso Spinelli,
  1515-1522. A reconstruction (Ekaterina Domnina)"** (`p07_2015_fig1_key.jpg`, 2480x3507). PDF p. 10 = printed p. 189:
  Fig. 2, Tommaso Spinelli to his brother Leonardo, 2 July 1520, Antwerp, fol. 1r (Beinecke Gen MSS 109, box 126,
  folder 2583) (`p10_2015_fig2_letter_2jul1520.jpg`). PDF p. 16: the author's English note on how to cite the Russian
  version and what it adds.
- pp. 17-27: Domnina E. G., "Shifry v diplomatii rannikh Tyudorov: na materiale lichnoi perepiski Tommazo Spinelli.
  Prilozhenie" (Russian), in *Iskusstvo i kul'tura Evropy epokhi Vozrozhdeniya i rannego Novogo vremeni. Sbornik trudov
  v chest' Vsevoloda Matveevicha Volodarskogo*, Moscow-St Petersburg: Tsentr gumanitarnykh initsiativ, 2016, pp. 254-268
  + 1 colour plate (istina.msu.ru record 11992054, whose page answers HTTP 200 without a file link). PDF pp. 25-26 =
  printed pp. 266-268: the corrected transcription (Italian) and Russian translation of the **2 July 1520 letter**,
  the deciphered fragment in italics, "small changes" from the 2015 text because Leonardo's own decipherment of it was
  found after 2015. PDF p. 27 = the colour plate (`p27_2016_plate_key_letter_decipherment.jpg`, 3285x4808): **Ill. 1 the
  corrected key** (adds an FF cell and second forms to the 2015 table), **Ill. 2 the 1520 letter fol. 1r** (eight lines
  of cipher visible), **Ill. 3 Leonardo Spinelli's decipherment of the fragment** (Beinecke Gen MSS 109, box 127,
  folder 2611, fol. 2r; the author's p. 16 note says fol. 2r-v).

What the file does not contain, by a search of the OCR text on 28 Sept 2026 (pages 1-27, case-insensitive, for
1519, Barcel, gubern, Arbore, confess, Septem, Ispag, "folder 25xx/26xx", "fol."): no transcription, translation or
decipherment of the 7 Sept 1519 Barcelona letter (folder of the online item, Beinecke OID 10844890); the only letter
printed in full is 2 July 1520 (folder 2583), and the only other folder cited is 2571 (a 1509 quotation, p. 20). This is
a search result on an OCR layer of uneven quality, not a verdict (CLAUDE.md rule 10); a reader of the page images could
still find a passing quotation the OCR garbled.

Copyright: the article and figures are the author's and publishers'; the three page images are kept as research
reference copies of a key table and two manuscript reproductions, at the PDF's own resolution, and are not to be
republished from here.
