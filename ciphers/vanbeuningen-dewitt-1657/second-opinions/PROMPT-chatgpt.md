SECOND OPINION REQUEST, label SO-VANBEUNINGEN-1657

We are an open cipher-research repository (github.com/NoAutopilot/cipher-lab). We have recovered a partial key
to a 1657 Dutch diplomatic cipher and want you to try to prove that this key, or a decipherment of this specific
cipher copy, was already known before us, and to find mistakes in our reading. Be adversarial: we would rather
learn now that it is in print than claim it wrongly later. The plaintext of the letter itself is NOT what we are
asking about -- it has been in print since 1919 (see below). What we are asking about is whether anyone has ever
actually deciphered the separate cipher COPY of this letter, or published the key/system it uses.

THE ITEM
- Sender: Coenraad van Beuningen, Dutch envoy at Copenhagen. Recipient: Johan de Witt, Grand Pensionary of
  Holland. Date: 19/29 September 1657 (Julian/Gregorian double-dated, as the letter itself gives it).
- Archive: Nationaal Archief, The Hague, archive 3.01.17 ("Archief van Johan de Witt, raadpensionaris van
  Holland"), inventory number 1538 (yearly bundle of Van Beuningen's 1657 despatches from Copenhagen), leaf-images
  ff.210-211 (`NL-HaNA_3.01.17_1538_0210.jpg`, `_0211.jpg`; digitised, public domain, no login,
  `service.archief.nl`). This is a SEPARATE physical copy, in a different and more cramped hand, of the same
  letter that survives in plain-text at ff.208-209 of the same bundle.
- The plaintext is already printed: R. Fruin / N. Japikse (ed.), *Brieven aan Johan de Witt*, Deel I (Werken
  uitgegeven door het Historisch Genootschap, 1919), pp.405-406, from the plain copy. The edition's own footnote
  1 to this letter states (our translation): "Not in Van Beuningen's own hand. The same letter also [survives]
  in unsolved cipher, in another hand" -- i.e. the 1919 editors already knew this cipher copy existed and
  explicitly say it was never deciphered by them. We are not claiming anything new about the letter's CONTENT;
  we are asking whether anyone since 1919 deciphered the CIPHER COPY itself, or published its key.

THE SYSTEM (recovered cryptanalytically from the cipher copy against the 1919 printed plaintext; no external key
sheet or table has been found for it)
The cipher copy interleaves two things: (1) plain, uncoded Dutch for function/connective words (de, van, met,
op, dat, sal, niet, daer, ...) copied through unchanged; (2) comma-separated, colon-terminated numeric groups of
1-3 digits, of two kinds -- a small closed NOMENCLATOR of about 9 distinct code-values (roughly in the range
100-225) each standing for a fixed multi-word phrase (Vereenichde Nederlanden, Haer Hoog Mog., Engelandt,
Sweden, Vranckrijk, Coningh van Denemarcken, Denemarcken, Elseneur, Londen), and a HOMOPHONIC LETTER ALPHABET
(roughly 21 letters recovered across 53 distinct code-values in the range 4-65) in which several different
numbers can stand for the same frequent letter (e.g. 'e' alone has at least five homophones: 50, 51, 52, 53, 54).
u/v and i/j are not distinguished, consistent with the period's Dutch orthography.

OUR READING (recovered by known-plaintext alignment against the 1919 print, not from any external key; grades
per our rule 4 -- C = fixed by 2+ independent word-contexts, M = a single context or a genuine unresolved
conflict)
- 862 cipher-copy tokens total: 345 plain Dutch (passed through unchanged) + 517 coded. Of the 517 coded
  tokens: 446 grade C, 70 grade M, 1 still unkeyed (code 106, one occurrence).
- Fully decoded example, no gaps: the 11-letter word "geobtineert" ("obtained") decodes completely from the
  recovered letter-alphabet alone: codes `57,50,12,44,25,61,10,50,51,21,25:` -> g-e-o-b-t-i-n-e-e-r-t.
- The 9-letter proper name "Rosewinge" (an envoy/courtier named in the printed plaintext) decodes completely:
  `21,12,23,50,32,61,10,57,51:` -> r-o-s-e-w-i-n-g-e, with the letter 'e' at positions 4 and 9 both getting the
  identical code 51.
- Nomenclator example: code `143:` recurs exactly where the print has "Vereenichde Nederlanden" (4 occurrences,
  each with matching adjacent plain-word context on both sides); code `144:` for "Haer Hoog Mog." (4
  occurrences); code `173:` for "Coningh van Denemarcken" (2 occurrences).
- Two codes remain genuine unresolved conflicts between two well-evidenced values rather than forced: code 40
  (14 supporting words vote 'd', 10 vote 'a'), code 11 (7 vote 'm', 5 vote 'n'). Both conflicts were
  independently reproduced in the same direction by a fresh-instance re-derivation working from the ciphertext
  and the 1919 print alone, which we take as evidence the ambiguity is real (a design feature of the cipher, or
  two homophone groups not yet disentangled) rather than an alignment artefact.
- Full files: reading
  https://raw.githubusercontent.com/NoAutopilot/cipher-lab/main/ciphers/vanbeuningen-dewitt-1657/reading.txt,
  key https://raw.githubusercontent.com/NoAutopilot/cipher-lab/main/ciphers/vanbeuningen-dewitt-1657/key.tsv,
  transcription
  https://raw.githubusercontent.com/NoAutopilot/cipher-lab/main/ciphers/vanbeuningen-dewitt-1657/ciphertext.tsv,
  the printed plaintext we aligned against
  https://raw.githubusercontent.com/NoAutopilot/cipher-lab/main/ciphers/vanbeuningen-dewitt-1657/plaintext_print.txt,
  notes https://raw.githubusercontent.com/NoAutopilot/cipher-lab/main/ciphers/vanbeuningen-dewitt-1657/NOTES.md,
  our own search log
  https://raw.githubusercontent.com/NoAutopilot/cipher-lab/main/ciphers/vanbeuningen-dewitt-1657/AUDIT.md.

WHAT WE HAVE ALREADY SEARCHED (do not just repeat these; see the four questions below for where to push further)
- Web search engine queries naming Van Beuningen, De Witt, "3.01.17", "onopgelost cijfer", and this letter's
  date: no hit connecting to a decipherment of the cipher copy.
- **M. Postma, *Johan de Witt en Coenraad van Beuningen: correspondentie tijdens de Noordse oorlog
  (1655-1660)*** (Utrecht doctoraalscriptie, 2006) -- the standard modern study of exactly this correspondence
  circle, cited repeatedly by a related student paper we did read. This is our largest gap: it could not be
  read directly across two sessions and two routes (Academia.edu 403s to us; the OpenAlex-listed DSpace handle
  is now stale/404; the university repository's own search API returned no matching record). A citing paper
  that quotes Postma about 20 times contains zero mentions of "cijfer"/"geheimschrift" in its own text, but that
  is evidence about the CITING paper only, not about whether Postma's own book discusses the cipher.
- **Karl de Leeuw**, *Cryptology and statecraft in the Dutch Republic* (PhD thesis, University of Amsterdam,
  2000; open access, read in full, 12,813 lines of extracted text grepped). This is the definitive scholarly
  source on Dutch Republic cryptology we could find. It discusses a DIFFERENT, later Van Beuningen cipher letter
  (1668, Van Beuningen by then ambassador in France, to Burgersdijk and Van der Togt, different code-value
  ranges) but never mentions this 1657 Copenhagen letter, its envoy, or its cipher. It does place the start of
  systematic Dutch diplomatic codebook-keeping at 1657/1658 (two specific administrative measures, 21 July 1657
  and 20 Sept/4 Oct 1658), which is consistent with -- but does not confirm -- our letter's small ad hoc
  9-entry nomenclator predating the later, larger standardised system.
- The Nationaal Archief's own full EAD finding aid for archive 3.01.17 (all ~41,000 lines, one fetch), grepped
  for "sleutel"/"cijfer"/"cypher"/"chiffre"/"geheimschrift"/"onopgelost": zero hits anywhere in the whole
  archive's catalogue description, including its own entry for inventory 1538.
- Internet Archive full-text (including lending-only items via the search-inside API), HathiTrust, Google Books
  (with an API key), OpenAlex, Semantic Scholar and CrossRef: searched for distinctive phrases from the
  plaintext ("Rijcxhoffmeester", "geobtineert op sijn versoeck", etc.) and for the correspondents' names. Every
  genuine hit traces back to the 1919 Japikse edition itself, which prints the PLAIN copy's text, not a
  decipherment of the cipher copy.
- Fresh shallow clones of both solver repositories, `dbourdeau/cyphersolver` and `aaymeloglu/unsolved-ciphers`:
  grepped for "beuningen", "3.01.17", "nieuwpoort" -- no hit for this target in either repository.
- DECODE (de-crypt.org)'s local catalogue snapshot, Cryptiana's Dutch-language page: no matching record.

FOUR QUESTIONS WE WANT YOU TO PUSH ON SPECIFICALLY
1. Has anyone -- an archivist, a Dutch historian, a cryptography-history scholar, a genealogy or diplomatic-
   history forum, a cipher-enthusiast site -- ever published a decipherment of the SEPARATE cipher copy at NA
   3.01.17 inv.1538 ff.210-211 specifically (as opposed to simply reading the already-printed plain copy at
   ff.208-209/Japikse I pp.405-406, which is not in question)?
2. Can you find, cite, or characterise M. Postma's 2006 dissertation *Johan de Witt en Coenraad van Beuningen:
   correspondentie tijdens de Noordse oorlog (1655-1660)* well enough to say whether it discusses this
   correspondence's use of cipher at all -- through a library catalogue record, a review, a citing work's
   detailed summary, or any copy you can access that we could not? Page numbers if you can get them.
3. Is there a published edition, catalogue, or cipher-history survey (Dutch, English, or otherwise) that
   describes the Dutch Republic's mid-1650s ad hoc diplomatic ciphers -- specifically a small (roughly 9-entry)
   nomenclator combined with a homophonic single-letter alphabet, predating the more elaborate post-1658
   codebook system Karl de Leeuw describes -- that might name or reproduce this exact key or a closely related
   one used by another envoy in the same years?
4. Do you see anything in our reading that looks wrong given what you can find about this correspondence or
   period Dutch diplomatic practice -- in particular, can you resolve either of our two open code conflicts
   (code 40 = 'd' or 'a'; code 11 = 'm' or 'n') from context, or suggest which of the two 1657 nomenclator
   phrases (Sweden vs Engelandt for codes 105/213) is more plausible on independent grounds?

HOW TO REPORT (this part is the same for every label)
- Write your answer as one Markdown file in the repository github.com/NoAutopilot/cipher-lab at the path
  `ciphers/vanbeuningen-dewitt-1657/second-opinions/chatgpt-<UTC date>.md`. Do not touch any other file. Do not
  commit to `main`: create a branch named `second-opinion/SO-VANBEUNINGEN-1657` and open a pull request from it,
  titled exactly `[SO-VANBEUNINGEN-1657] second opinion: Van Beuningen to De Witt cipher copy, 19/29 Sept 1657`.
- The first lines of the file must be this header, filled in:
      label: SO-VANBEUNINGEN-1657
      model: <your model name and version>
      date: <UTC date you answered>
      prompt: PROMPT-chatgpt.md in this folder
  and then sections 1-5 in the order below.
- Every citation must be checkable from a desk: author, title, year, volume, page, and a URL to the page on
  Google Books, HathiTrust, Internet Archive, the Nationaal Archief, DBNL, or the publisher. If you cannot give
  a page and a URL, mark the citation "unverified". Never invent a page number.
- Do not use the words "first", "new", "unpublished", "unread" or "never printed" about our reading. Our rule is
  that only a separate verifier may say that. Your job is to try to prove the opposite: that the key or a
  decipherment of this cipher copy is already in print somewhere, or that our reading is wrong.

WHAT TO PUT IN THE FILE
1. Prior print: any edition, calendar, article or book that prints a decipherment of the cipher copy itself, or
   its key, or discusses that a cipher copy (as opposed to the plain copy) of this letter exists. Give the
   earliest you can find. If you find nothing, list exactly what you searched (catalogue, query, date) so we can
   tell a real gap from a shallow search.
2. Prior decipherment or key identification: anyone who has already read this key or identified its system,
   including blog posts, GitHub repositories, DECODE (de-crypt.org) records, theses (above all Postma 2006), and
   conference papers.
3. Errors in our reading: any code, letter assignment, or nomenclator entry you believe is wrong, with your
   reason and the source that shows it. Address the four questions above explicitly.
4. Leads: archives, editions or scholars we should check, with a one-line reason each.
5. Confidence: one sentence on how sure you are that nothing prior exists, and what would change it.
