# CHECK: SO-VANBEUNINGEN-1657 (PR 11, `chatgpt-2026-09-25.md`)

Citation check by V6-SOCHK (LANE V6), 25 Sept 2026, 16:55-17:10 UTC. Every citation in the answer was traced
to the source itself where it could be reached. Repository-file claims checked against `main` at a05e018.

| # | Claim in the answer | Result | What was read |
|---|---|---|---|
| 1 | Fruin/Japikse, *Brieven aan Johan de Witt* I (1919), pp.405-406, p.405 n.1: another copy in unresolved cipher | confirmed (repository transcription) | plaintext_print.txt line 40, transcribed by eye from the Huygens retroboeken page images (NOTES.md "Source"): "Dezelfde brief ook in onopgelost cijfer, van een andere hand"; page image not re-fetched this pass |
| 2 | Mirte Postma, *Johan de Witt en Coenraad van Beuningen: correspondentie tijdens de Noordse oorlog (1655-1660)*, Scriptio 2007, ISBN 9789087730079 | confirmed | Google Books API by ISBN: Mirte Postma, scriptio, 2007, 160 pp. |
| 3 | bookseller metadata (goedhartboeken.nl) gives 125 pp. | not confirmed | the cited URL now serves the shop's generic homepage (title "Welkom in onze boekhandel..."), no product record, no page count; Google Books and AUD2 both give 160 pp. Treat 125 as unverified |
| 4 | Stichting De Ruyter, *Rapport inzake de Jaarrekening 2022*, PDF p.25 of 34, item 144: Postma 2007 in the inventory | confirmed | institution's PDF, 34 pp., title page "Rapport inzake de Jaarrekening 2022"; PDF p.25: "144 / Johan de Witt en Coenraad van Beuningen / Postma, M. / 2007 / context / Correspondentie tijdens de Noordse oorlog 1655-1660" |
| 5 | Karl de Leeuw, *Cryptology and Statecraft in the Dutch Republic* (UvA thesis 2000), pure.uva.nl PDF | confirmed reachable | HTTP 200 application/pdf; its content was read by the first audit (AUDIT.md (d)); not re-read here |
| 6 | Fruin/Kernkamp, *Brieven van Johan de Witt* I (1906), IA `werken28nethgoog`, pp.440-441: Kernkamp deciphered Van Beuningen's cipher letters to the Amsterdam burgomasters, 28 Oct 1657, "omdat de sleutel van het geheimschrift voor in de portefeuille ligt" | confirmed | IA `_djvu.txt` (be-api fts answered 502 twice, so the OCR file was read instead), page 440-441 footnote read verbatim |
| 7 | same volume pp.71-72: 1653 key supplied to Van Beuningen | confirmed (location) | OCR pp.71-72 carries the passage on the cipher and its key ("De sleutel is een-..."); the value-by-value comparison is AUD2's, not repeated |
| 8 | Rosewinge: the prompt says both e's are 51, but the numerals it quotes are 50 then 51 | confirmed | PROMPT-chatgpt.md lines 43-45: codes `21,12,23,50,32,61,10,57,51` with "identical code 51" -- the prompt is wrong, the answer is right |
| 9 | reading.txt renders dominant choices: L09 "penningem", L30 "kenmen", L33 "dgent" where the print has penningen, kennen, agent | confirmed, one misquote | reading.txt L30 "k e n m e n", L33 "d g e n t" as stated; L09 actually reads "p e n m i n g e m" (penmingem), not "penningem"; the point (11 = m\|n and 40 = d\|a rendered by the dominant value) holds; print lines 10, 21, 23 read penningen, kennen, agent |
| 10 | web-index search log | not re-run | a search-engine silence, not a source |

Counts: 7 confirmed (1, 2, 4, 5, 6, 7, 8), 1 confirmed with a misquote (9), 1 not confirmed (3), 1 not re-run
(10). Nothing invented; the one unconfirmed item is a page count from a URL that no longer serves the record.

**Does any confirmed lead move the class?** No. Item 6 was already in AUDIT.md (AUD2 section): a decipherment of
three *other* letters (different recipient, different archive), not of ff.210-211. Item 4 is an access lead (a
physical copy of Postma 2007 in a named private institutional library), the most concrete route yet to the book
that holds item 2 at N3; it is not evidence either way. Item 1 N1 and item 2 N3 stand. No flag to the parent.

**Verdict: merge.** A faithful answer with its own unverified items marked; one page count unconfirmed, one
repository misquote (penningem for penmingem), listed in AUDIT.md.

Requests: archive.org 1 (djvu.txt), be-api.us.archive.org 2 (502 both), www.deruyter.org 1,
www.goedhartboeken.nl 1, pure.uva.nl 1 (HEAD), www.googleapis.com 1.
