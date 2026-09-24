# AUDIT: Willem van Oranje to Günther van Schwarzburg, [Brussels, 2 May 1561] (WVO 8246)

Verifier V4 (Opus, for LANE V2), 24 Sept 2026, 09:48-09:55 UTC by `date -u`. Adversarial audit under CLAUDE.md rule 10.
No decoding done. The reading, key and ciphertext are unchanged.

Claim under audit (LANE R2 G1, 09:24 UTC, 24 Sept 2026): "WVO 8246 pp.1-2 read with a 79-sign homophonic German letter
cipher aligned from WVO 5109 against Japikse no.236 pp.232-233: 553 tokens C 491 M 24 U 38; p.3 not transcribed.
Japikse no.316 prints 8246 only to the clear opening." (F1 added p.3 at 09:43: pp.1-3 953 tokens, C 817 M 53 U 83.)

## 1. Verdict

| item | class | prior plaintext | prior decipherment of this item | evidence | confidence |
|---|---|---|---|---|---|
| 8246 cipher passage, pp.1-2 as read (and p.3, which is the same passage's continuation) | **N0** | **yes:** Japikse, *Correspondentie van Willem den Eerste* I (1934), no.316, pp.343-344 | **yes:** Japikse prints the whole cipher passage deciphered, in spaced type. That is his marking for text the Prince wrote in cipher, and the decipherment is credited to H. Koot (no.236, p.232 n.5) | strong: page images on disk (`images/japikse_p343.png`, `japikse_p344.png`, `japikse_p232.jpg`); the printed spaced text follows our reading word for word from its first word to its last | high |

**Safe sentence.** "The cipher passage of William of Orange's letter to Günther von Schwarzburg of [2 May] 1561 (WVO 8246)
is printed deciphered in Japikse, Correspondentie van Willem den Eerste I (1934), no.316, pp.343-344 (N0). Our key,
aligned from the sibling letter WVO 5109 and its printed plaintext, independently regenerates that text (pp.1-3: C 817,
M 53, U 83 of 953 signs)."

**Unsafe sentences.** "Japikse prints 8246 only to its clear opening." "The ciphered bulk of 8246 is unread / unprinted."
"We deciphered 8246 for the first time." "Previously unread cipher letter."

**Did we first-decipher? No.** Japikse printed the plaintext in 1934, and his footnotes name the solver: H. Koot of the
Dutch Foreign Ministry deciphered the Prince's cipher insertions. What this project adds is an explicit sign-by-sign key (79
signs, grade C) and a reproducible alignment. That is a re-decipherment and a key table, a contribution, not a new reading.

## 2. The evidence

- **Japikse p.343 (`images/japikse_p343.png`).** Heading "316. Aan Günther, graaf van Schwarzburg. 2 Mei (1561)". n.1:
  "S.A. Sondershausen. -- Uit Brussel. -- Zonder jaartal, dat echter niet dubieus is" (the same letter as our image, which
  carries the stamp "Staatsarchiv Rudolstadt, Kanzlei Sondershausen 693"). Five lines are in normal type, "Wolgeborner
  freundtlicher lieber Schwager und Bruder, Ich hab Pauln von Sahra ... angehen,". Everything from **"nemlich den heuradt
  zwichen Dennemarck undt Lothringen, hab ich nicht vonwegen sonder underthenigster dhiensten, damit ich Königliche Würden
  zuu Dennemarck geneigt, underlassen kunden E.L. in freundlichem vertrauen zu ermelden, dasz sich die alte hertzogin zu
  Lothringen vernemen lassen hat ..."** onward is in **spaced type**.
- **Japikse p.344 (`images/japikse_p344.png`).** The spaced type continues to **"... bin ich derselben, wesz mir wislich,
  idertzeit vertraulich mitzutheilem guttwillig."** Then comes normal type, "Und wust ich E.L. auch sunst ... alles guts zu
  wünschen", the letter's clear close.
- **Japikse p.232 (`images/japikse_p232.jpg`), no.236 = WVO 5109.** The spaced passage there carries n.5: "Het nu volgende
  ontbreekt in de minuut en is dus door den Prins zelf in cijferschrift ingelascht. De oplossing uit cijferschrift dank ik
  aan den heer H. Koot, ambtenaar aan Buitenlandsche Zaken alhier." So in this edition spaced type marks the cipher
  insertion, printed from Koot's solution. n.6 on the same page ("Renata (zie hierna, blz. 343)") points to no.316. The
  claim's own key rests on the same convention: G1 aligned 5109 against exactly this spaced passage.
- **Match with our reading.** `reading.txt` p1L01 begins "nemlichden heuradt zu[w]ischen [De]nnemarck undt Lothringen", and
  p3 ends "...wislich ider zeit vertrauli[.]h mit zu theilen". Those are the first and last words of Japikse's spaced text.
  The words between follow it: "alte Hertz[o]gin [z]u Lothringen vernemen lassen hat", "glaubwurdi[g]en leuthen vernommen",
  "umb bericht diesser sachen von hindan", "[.]eschriben wurde, wes", "gemudt", "sachen nicht mehr s[.]hrei[ben]". The
  clear close on MS p.3 ("und wunscht dich E.L. ...") is Japikse's normal-type "Und wust ich E.L. ...".
  The print also supplies the text at several of our U positions, for example "E.L. in" before "freundlichem", and "c" where
  F1 guessed that the looped `b` stands for c (s[b]hrei = schrei, i[b]h = ich).

## 3. Principal families

The class rests on the principal edition, the one that WVO's own record cites. Once that edition prints this very item
deciphered, further families cannot lower the class. They were not searched, and that is logged here, not hidden.

| family | searched / unreachable / not needed | what | result |
|---|---|---|---|
| Canonical edition named by WVO (Japikse 1934) | searched | pp.343-344 (no.316) and p.232 (no.236), page images already on disk and read by eye this session | **prints the cipher passage deciphered (N0)** |
| WVO record 8246 (Opmerkingen, Bron) | searched (from NOTES.md quotation) | "Grotendeels in cijfer ... ontleend aan Japikse" | no "oplossing" word, but its Bron is the edition that prints the solution |
| Groen van Prinsterer, Archives 1e sér. t.I and Supplément | not needed | -- | -- |
| Kluckhohn; Schwarzburg edition literature; Rachfahl; KHA / Rudolstadt / Sondershausen catalogues | not needed | -- | -- |
| Contemporary decipherment on the leaf (for N0 without print) | not needed | the MS images show no interlinear gloss, by eye on `08246_p1-3.jpg` at thumbnail scale | not relied on |
| Phrase search (Google Books, IA, DBNL, Delpher) | not needed | the print was located by page, not by phrase | -- |
| JSTOR | not needed | no row queued | -- |

Requests this audit: 0 network. Everything was read from images already on disk. No host was claimed, so
resources.huygens.knaw.nl was not touched and nothing needed posting for LANE N.

## 4. Postmortem

**Failure:** a misread of the edition's typography. The check-solved worker read Japikse no.316 and took the spaced type
on p.343 as clear text. C1 found the spaced-type convention on p.232 in the same volume and applied it to 5109 but not to
8246. G1 then built its key from that convention on 5109 and repeated "prints 8246 only to the clear opening." The
signal was also visible from the reading's side: the first decoded words, "nemlich den heuradt", are the words that
follow the last clear-type word on Japikse p.343. Nobody compared the reading with the print it cited.

**Lesson (for verifier.md and the solver brief):** after decoding, set the reading beside every printed text of the same
letter, including the one the search log says "stops before the cipher". Spaced type (*Sperrdruck*), italics or brackets
in an edition may be the editor's marking for a deciphered passage. Read the edition's footnotes on its first cipher letter
to learn its convention.

**Files and sentences corrected in place** (the originals are kept, struck through or with a dated correction note):
- `NOTES.md`: status word `partial` -> `found-solved`; "Critical finding: Japikse's printed text is the letter's clear
  opening only ...", the Verdict "Status: open ..." paragraph, check-solved item 1, and G1's search-log line.
- `QUEUE.md` WV3 row and harvest summary: "prints only the clear opening, stops before the ciphered majority".
- `status.json` results row: the line "Japikse's edition prints 8246 only up to its clear opening", and the grade.

## 5. Second opinions, JSTOR

None queued. The item is N0 on a located print, so SECOND-OPINIONS-QUEUE and JSTOR-QUEUE rows are not called for
(the brief asks for them only at N3 or higher).
