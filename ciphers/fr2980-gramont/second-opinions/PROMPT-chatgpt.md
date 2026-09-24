SECOND OPINION REQUEST, label SO-GRAMONT-F29R

We are an open cipher-research repository (github.com/NoAutopilot/cipher-lab). We have read a ciphered
letter and want you to try to prove that its text was already known before us, and to find mistakes in
our reading. Be adversarial: we would rather learn now that it is in print than claim it wrongly later.

THE ITEM
- Sender: Cardinal Gabriel de Gramont, bishop of Tarbes, French ambassador at Rome.
- Recipient: Jean Breton, seigneur de Villandry, secretary of Francis I.
- Place and date: Rome, 20 May 1530.
- Manuscript: Bibliothèque nationale de France, ms. français 2980, folio 29r (item 21 in the volume).
  Volume on Gallica: https://gallica.bnf.fr/ark:/12148/btv1b9059991d (find f.29 in the viewer).
- Cipher: a nomenclator; read with the Gramont 1530 key published by Satoshi Tomokiyo and George Lasry.
  569 cipher signs, of which we read 533 from the key, 30 uncertain, 5 unread.
- Our files: reading https://raw.githubusercontent.com/NoAutopilot/cipher-lab/main/ciphers/fr2980-gramont/reading.txt, transcription
  https://raw.githubusercontent.com/NoAutopilot/cipher-lab/main/ciphers/fr2980-gramont/ciphertext.txt, key https://raw.githubusercontent.com/NoAutopilot/cipher-lab/main/ciphers/fr2980-gramont/key.tsv, notes
  https://raw.githubusercontent.com/NoAutopilot/cipher-lab/main/ciphers/fr2980-gramont/NOTES.md, our own search log https://raw.githubusercontent.com/NoAutopilot/cipher-lab/main/ciphers/fr2980-gramont/AUDIT.md.
- Distinctive phrases of the deciphered French, useful for full-text search (old spelling, try variants):
  "il y baille a ce porteur"; "article que j'ay mis a part"; "l'adresse de dessus a vous combien que ce
  soit au roy"; "vous prie le luy demander car c'est le total"; "qui est cause que j'ay faict ledit article
  a part"; "pour vous donner cognoissance de tout".

WHERE WE HAVE NOT YET LOOKED PROPERLY (start here)
- Camusat, Meslanges historiques (1619), which prints Gramont letters of 1530: is this letter, or its
  substance, there? Gallica copy bpt6k5039434 (image only, no OCR for us).
- Champollion-Figeac, Captivité du roi François Ier (1847), and the Documents inédits series generally.
- Catalogue des actes de François Ier; Lettres de Marguerite d'Angoulême; Correspondance du cardinal Jean
  du Bellay (ed. Scheurer); Decrue, Anne de Montmorency; the Négociations diplomatiques entre la France
  et l'Autriche; Revue d'histoire diplomatique; Bibliothèque de l'École des chartes; any thesis on
  Gramont's Roman embassy 1529-1531.
- JSTOR and HathiTrust full text, which we cannot reach from our environment.

HOW TO REPORT (this part is the same for every label)
- Write your answer as one Markdown file in the repository github.com/NoAutopilot/cipher-lab at the path
  `ciphers/fr2980-gramont/second-opinions/chatgpt-2026-09-24.md`. Do not touch any other file. Do not commit to `main`:
  create a branch named `second-opinion/SO-GRAMONT-F29R` and open a pull request from it, titled exactly
  `[SO-GRAMONT-F29R] second opinion: Gramont to Villandry, 20 May 1530`.
- The first lines of the file must be this header, filled in:
      label: SO-GRAMONT-F29R
      model: <your model name and version>
      date: <UTC date you answered>
      prompt: PROMPT-chatgpt.md in this folder
  and then sections 1-5 in the order below.
- Every citation must be checkable from a desk: author, title, year, volume, page, and a URL to the page
  on Google Books, HathiTrust, Internet Archive, Gallica or the publisher. If you cannot give a page and a
  URL, mark the citation "unverified". Never invent a page number.
- Do not use the words "first", "new", "unpublished", "unread" or "never printed" about our reading. Our
  rule is that only a separate verifier may say that. Your job is to try to prove the opposite: that the
  text is already in print somewhere, or that our reading is wrong.

WHAT TO PUT IN THE FILE
1. Prior print: any edition, calendar, article or book that prints this letter, quotes it, summarises it,
   or prints its decipherment. Give the earliest you can find. If you find nothing, list exactly what you
   searched (catalogue, query, date) so we can tell a real gap from a shallow search.
2. Prior decipherment: anyone who has already read this cipher (the same key, the same folio), including
   blog posts, GitHub repositories, DECODE (de-crypt.org) records, theses, and conference papers.
3. Errors in our reading: any token, name, date or phrase you believe is misread, with your reason and
   the source that shows it.
4. Leads: archives, editions or scholars we should check, with a one-line reason each.
5. Confidence: one sentence on how sure you are that nothing prior exists, and what would change it.
