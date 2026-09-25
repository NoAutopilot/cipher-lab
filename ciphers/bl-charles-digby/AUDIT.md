# AUDIT: King Charles I's cipher paper countersigned by Lord Digby, BL Add MS 6912

Verifier V6-DIGBY, session_01JDwd3SeAYKW1KbAKK6ViDs (Opus, for LANE V6, parent 7b), 25 Sept 2026, 15:43-15:55 UTC by
`date -u`. Adversarial audit under CLAUDE.md rule 10. No decoding done; no ciphertext, key or reading in the folder.

Claim under audit (NOTES.md, LANE CX / CX-STUART, 25 Sept 2026): BL Add MS 6912 is found-solved: it is the document
Wheatstone deciphered and printed in 1862 (Philobiblon Society), "Instructions pour le Sieur de Goffe" on the Orange
marriage; the match rests on physical description, date range and acquisition; no shelfmark in the pamphlet.

## 1. Verdict

| item | class | key | prior plaintext | prior decipherment of this item | identification | confidence in class |
|---|---|---|---|---|---|---|
| BL Add MS 6912, Charles I's instructions to Stephen Goffe for the Prince of Orange, [May] 1644, signed C.R., countersigned George Digby, seven pages of numerals | **N0** | `published` (Wheatstone 1862, credited) | **yes, in clear:** Groen van Prinsterer, *Archives ou correspondance inédite de la maison d'Orange-Nassau*, 2e série, tome IV (1642-1650), Utrecht 1859, no. DCCCXXa, pp.101-104, "Instructions pour le Sieur Goffe. Conditions du mariage du Prince de Galles", printed from the Orange archive's delivered copy, dated May 1644 | **yes:** Wheatstone, "Interpretation of an important historical document in cipher", *Memoirs/Miscellanies of the Philobiblon Society* 1862, reprinted in *The Scientific Papers of Sir Charles Wheatstone* (1879) pp.321-330, with his key to the literal cipher and the vocabulary | **confirmed** (very probable; see section 3 for the one residual gap) | high |

Key source: `published`. The key (about 90 homophones for letters plus a vocabulary of higher numbers, e.g. 320 les,
376 pour, 474 Angleterre, 495 le roi d'Angleterre) is Wheatstone's, printed at pp.324-325 of the 1879 reprint. Nothing
in this repository recovered or rebuilt it. `text: known`.

**Safe sentence.** "BL Add MS 6912 is the cipher of Charles I's instructions to Stephen Goffe for the Prince of Orange
(May 1644, countersigned by George Digby) that Charles Wheatstone deciphered and printed in 1862 (N0, key published);
the same instructions had already been printed in clear from the Orange archive by Groen van Prinsterer in 1859."

**Unsafe sentences.** "Unsolved Charles I cipher." "We identified / solved an unread royal cipher." "The 1641 marriage of
William of Orange and Princess Mary" (wrong marriage and wrong year: the text is the 1644 proposal to marry the Prince of
Wales to Louise Henriette, "Mademoiselle d'Orange"). "The plaintext was first printed by Wheatstone" (Groen 1859 is
earlier).

**Did we first-decipher? No.** Wheatstone deciphered it in about 1859-60 (his covering letter of 3 Feb 1862 says "two or
three years ago") at Sir Henry Ellis's request; the plaintext itself was in print in 1859 from the recipient's side. This
project's contribution is the identification (shelfmark to publication), which the BL's own record does not make.

## 2. The identification, point by point

**A. Ellis's letter (1 June 1858) in Wheatstone's paper** (read in full this session, archive.org
`the-scientific-papers-of-sir-charles-wheatstone`, `_djvu.txt`, pp.321-330): "A good many years ago the Trustees of the
British Museum purchased, at a large price, ... a very important document in cipher; occupying seven folio pages closely
filled with numerals; every page signed at top by King Charles the First, and countersigned below by Lord Digbye. I was
long ago in hope to have got it deciphered, and to have inserted it ... in my second series of original letters
illustrative of English history". The deciphered text ends "C. R. / GEORGE DIGBYE". So: a British Museum purchase,
before Ellis's *Original Letters* second series (1827).

**B. The BM's own index of acquisitions 1783-1835 lists exactly one such item, and it is 6912.** *Index to the Additional
Manuscripts, with those of the Egerton Collection, ... acquired in the years 1783-1835* (British Museum 1849; archive.org
`indextoadditiona00brituoft`, full text fetched once and grepped):
- under DIGBY (George), Lord Digby and Earl of Bristol: "Paper, in cypher, signed by Charles I., and countersigned by
  Lord Digby . . . 6912." (OCR "«912");
- under Charles I: "A paper, in cypher, signed by him . . . 6912."
- Only nine lines in the whole index contain "cypher/cipher"; none is another Charles I or Digby cipher paper. The
  Egerton collection is indexed in the same volume.
- Its preface: the manuscript catalogue runs "from No. 5017 ... to about No. 7084; subsequent to which the annual
  printed Lists ... from the year 1829". So Add MS 6912 was acquired before 1829 -- consistent with Ellis hoping to
  print it in his 1827 second series, and with "a good many years ago" in 1858. The number is plausible for the
  purchase Ellis describes.

**C. The BL's current record** (searcharchives.bl.uk 032-003442981, quoted by CX): "Long original paper in cypher,
signed by King Charles I, and countersigned by George, Lord Digby, on every page. It has originally been indorsed
'Instructions for Digbie'", 1640s, purchased. The endorsement "for Digbie" is the Secretary's docket, not the addressee;
the text is addressed to Goffe.

**D. Alternatives searched.** searcharchives.bl.uk, five queries ("countersigned Digby", "cypher Digby", "cipher
Goffe", "Goffe instructions", "Charles I cypher signed"): Add MS 6912 is the only item matching the Charles-I-signs,
Digby-countersigns, whole-paper-in-cipher description; the other hits are Rupert correspondence, Weckherlin's
cipher-keys and miscellanies. No Egerton or later Add MS candidate found. Groen prints a *second* set of Goffe
instructions, "de la part de la reine" (no. DCCCXXIXa, p.829 of the Index reference), which is the Queen's, not the
King's-with-Digby, and is not a candidate for a King-signed paper.

**E. Content and date.** Groen's clear text (1859) and Wheatstone's decipherment (1862) are the same document sentence
for sentence (read side by side this session: "l'estime qu'il faict de la persone et maison de S. A. ... Dans un temps
moins embrouillé que cellui-cy ...", the five articles, "l'affaire d'Amboin", "M' Jermyn a esté arresté et ce porteur
choysy"). Groen dates it May 1644, among Jermyn's letter of 30 May 1644 from Exeter and the Queen's letter carried by
Goff. Digby was Secretary of State from Sept 1643. The Prince is the Prince of Wales, the Princess Mademoiselle
d'Orange. BL's 1640s range fits; CX's "1641 marriage of William and Mary" does not.

**Residual gap (why "confirmed" and not "certain").** No source read names Add MS 6912 inside Wheatstone's paper, or
names Wheatstone in the BM index or the BL record. The link is: Ellis (Keeper, then Principal Librarian) says the BM
bought it; the BM's complete index for the only period Ellis's words allow lists a single matching paper, 6912. A
purchase after 1835 and before 1858 would escape that index, but Ellis's 1827 intention rules it out. A look at the
leaf (numerals with the Charles R. / George Digbye subscriptions, and "42. 50. 90. 93. 83..." opening as in
Wheatstone p.330) would make it certain; this was not attempted (BL images unavailable since 2023).

## 3. Searches (principal families)

| family | status | what | result |
|---|---|---|---|
| Wheatstone's paper | searched | archive.org `the-scientific-papers-of-sir-charles-wheatstone` djvu, pp.321-330 in full | decipherment, key, Ellis's provenance letter, cipher text opening; no shelfmark |
| BM acquisition index | searched | archive.org `indextoadditiona00brituoft` (1849), grep cypher/cipher/6912/Goffe/Digby | 6912 the only Charles I / Digby cipher paper 1783-1835; acquired pre-1829 |
| Holding archive catalogue | searched | searcharchives.bl.uk, 5 queries, JSON | only 6912 fits; BL record cites no decipherment |
| Recipient's printed papers | searched | Groen van Prinsterer, Archives 2e sér. IV (archive.org `archivesoucorres04unse`, 1859) and index vol. (`archivesoucorres05unse`) | **plaintext in clear, no. DCCCXXa pp.101-104, May 1644**; related Goffe/Jermyn/Queen letters pp.99-104 ff. |
| IA full text | searched | be-api fts: "Sieur de Goffe", "Sieur St. Goffe", "persone et maison de son altesse", "moins embrouillé", "6912" with Goffe/Wheatstone/Digby | 20 hits for "Sieur de Goffe": Groen (4 copies), Notes and Queries 1877, BM General Catalogue (dates Wheatstone's item "1644"), BnF Catalogue général, Kahn *The Codebreakers*, bibliographies; no "6912" link |
| Cipher literature | searched | Kahn, *The Codebreakers* (IA fts inside `codebreakersstor0000kahn_y0y0`) | Kahn describes Wheatstone's solution ("instructions in French for the Sieur de Goffe ... small one-part nomenclator"); his notes cite other Add MSS, not 6912 |
| Scholarship, open indexes | searched | OpenAlex (key) "Wheatstone cipher Charles Goffe": 0; Semantic Scholar (key) same query: no result returned | nothing |
| Solver repos, DECODE | searched earlier | CX/24 Sept sweeps (NOTES.md): no record for 6912 or Digby | not re-run |
| Google Books | not run | the identification was settled by IA full text; budget kept | -- |
| Philobiblon Miscellanies vol. 6/7 original | not located | the 1879 reprint states it is "From the Memoirs of the Philobiblon Society" and reprints the editor's note | reprint suffices for the text; original's flyleaf not seen |
| Clarendon State Papers, Thurloe, Gardiner | not searched | Groen's clear print made them unnecessary for the class | -- |
| JSTOR | queued | one row appended to JSTOR-QUEUE.tsv | never blocking |

Requests: archive.org 10 (advancedsearch 2, metadata 3, djvu downloads 5 of which one returned 500), be-api.us.archive.org 14, searcharchives.bl.uk 5, api.openalex.org 1,
api.semanticscholar.org 1, Google Books 0. No subagents, no logins, no images.

## 4. Postmortem

The CX identification was right, on weaker evidence than was available: it rested on matching Ellis's description to the
modern BL record, and it missed two things that are one grep away. (1) The BM's own 1849 index puts 6912 in the pre-1829
range and shows it is the only Charles I / Digby cipher paper acquired 1783-1835, which turns "strong circumstantial" into
"confirmed". (2) The plaintext is in print in clear from the recipient's archive (Groen 1859), three years before
Wheatstone; a recipient-side edition search (verifier.md: "search the recipient's printed family papers") would have
found it. CX also mis-dated and mis-identified the marriage (1641, William and Mary) from the phrase "le marriage du
prince et la princesse" without reading the text through to "prince de Galles" and "Henrietta d'Orange" in the key.
Corrected in NOTES.md.

Contribution to hand on (for the parent, not a novelty claim): the BL record for Add MS 6912 cites neither Wheatstone
1862 nor Groen 1859; a catalogue note is a correction the BL can check from its desk. Groen's clear text also settles
several words Wheatstone marked doubtful (his "(satisfaction)" is "syncérité", "(post)ure" is "procédure", "(preparé)s"
is "poursuivyes"; his unresolved 562 is "M' Jermyn", 484 is "Hollande", and the 522 of article 2 is "l'Empereur" in the
clear, while the 522 of the first sentence stands where Groen has "M' Jermyn", an OCR or transcription point to check), which is a key-level note on Wheatstone's
vocabulary, not a new reading.
