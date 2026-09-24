SECOND OPINION REQUEST, label SO-GRAMONT-F30

We are an open cipher-research repository (github.com/NoAutopilot/cipher-lab). We have read a ciphered
letter and want you to try to prove that its text was already known before us, and to find mistakes in
our reading. Be adversarial: we would rather learn now that it is in print than claim it wrongly later.

THE ITEM
- Sender: Gabriel de Gramont, bishop of Tarbes (made cardinal in June 1530), French ambassador at Rome.
- Recipient: King Francis I (from the formulas "Sire" and "vostre commandement" in the text).
- Place and date: Rome, 20 May 1530.
- Manuscript: Bibliothèque nationale de France, ms. français 2980, folios 30r-30v (item 22 in the volume), written
  entirely in cipher, signed "De Gramont E. de Tarbe", dated "Faict à Rome, le XXme jour de may M.D.XXX".
  Volume on Gallica: https://gallica.bnf.fr/ark:/12148/btv1b9059991d (find f.30 in the viewer).
- Cipher: a nomenclator; read with the Gramont 1530 key published by Satoshi Tomokiyo and George Lasry.
  1973 cipher signs: 1502 read from the key, 158 more values proposed cryptanalytically with a control (grade S),
  254 uncertain, 59 unread.
- Our files: reading https://raw.githubusercontent.com/NoAutopilot/cipher-lab/main/ciphers/fr2980-gramont/reading_f30_extended.txt, transcription
  https://raw.githubusercontent.com/NoAutopilot/cipher-lab/main/ciphers/fr2980-gramont/ciphertext_f30.tsv, key https://raw.githubusercontent.com/NoAutopilot/cipher-lab/main/ciphers/fr2980-gramont/key.tsv, notes
  https://raw.githubusercontent.com/NoAutopilot/cipher-lab/main/ciphers/fr2980-gramont/NOTES.md, our own search log https://raw.githubusercontent.com/NoAutopilot/cipher-lab/main/ciphers/fr2980-gramont/AUDIT.md.
- Distinctive phrases of the deciphered French, useful for full-text search (old spelling, try variants):
  "la declaration de la liberte de Florence"; "la ville et la force entre vos mains"; "qu'il veult aller en
  Avignon"; "pour recouvrer ce que ses predecesseurs ont perdu"; "qu'il n'a aucune deliberation d'aller";
  "toutes choses qui vous touchent de si bon pied"; "l'ambassadeur et aultres ses ministres".

WHERE WE HAVE NOT YET LOOKED PROPERLY (start here)
- Camusat, Meslanges historiques (1619; Gallica bpt6k5039434 is the 1644 edition), which prints Gramont letters
  of 1530: is this letter, a summary, or its substance there?
- Imperial intercepts: CSP Spanish IV.1 p.603 says the governor of Asti intercepted Tarbes's letters in 1530 and
  that some were deciphered. Is a copy or decipherment of a 20 May 1530 letter to the king in Simancas (Estado),
  Vienna (HHStA), or printed in Lanz, Correspondenz des Kaisers Karl V, or the Nuntiaturberichte?
- Florentine sources for the siege of Florence in May 1530 (Varchi, Segni, Nardi; Florentine archives editions),
  since the letter discusses Florence's liberty.
- Catalogue des actes de François Ier; Decrue, Anne de Montmorency; Revue d'histoire diplomatique; Bibliothèque de
  l'École des chartes; any thesis on Gramont's Roman embassy 1529-1531.
- JSTOR and HathiTrust full text, which we cannot reach from our environment.

HOW TO REPORT (this part is the same for every label)
- Write your answer as one Markdown file in the repository github.com/NoAutopilot/cipher-lab at the path
  `ciphers/fr2980-gramont/second-opinions/chatgpt-f30-2026-09-24.md`. Do not touch any other file. Do not commit to `main`:
  create a branch named `second-opinion/SO-GRAMONT-F30` and open a pull request from it, titled exactly
  `[SO-GRAMONT-F30] second opinion: Gramont to Francis I, 20 May 1530 (f.30)`.
- The first lines of the file must be this header, filled in:
      label: SO-GRAMONT-F30
      model: <your model name and version>
      date: <UTC date you answered>
      prompt: PROMPT-chatgpt-f30.md in this folder
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
