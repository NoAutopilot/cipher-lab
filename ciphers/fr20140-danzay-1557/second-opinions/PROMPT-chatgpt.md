SECOND OPINION REQUEST, label SO-DANZAY-F35

We are an open cipher-research repository (github.com/NoAutopilot/cipher-lab). We have read a ciphered
letter and want you to try to prove that its text was already known before us, and to find mistakes in
our reading. Be adversarial: we would rather learn now that it is in print than claim it wrongly later.

THE ITEM
- Sender: Charles de Danzay, French resident ambassador in Denmark.
- Recipient: Charles de Guise, Cardinal of Lorraine.
- Date: 27 January 1557 (as written; the letter is unfinished on f.35v and continues on f.36).
- Manuscript: Bibliothèque nationale de France, ms. français 20140, folio 35. Gallica volume:
  https://gallica.bnf.fr/ark:/12148/btv1b52521512h (alternate digitisation btv1b10782904z); find f.35.
- Cipher: read with the Danzay 1557 key published by Satoshi Tomokiyo (cryptiana.web.fc2.com). 638
  cipher tokens on f.35: 509 read from the key (61 of them nulls), 59 uncertain, 70 unread; continuous
  French on about 23 of 37 lines.
- Our files: reading https://raw.githubusercontent.com/NoAutopilot/cipher-lab/main/ciphers/fr20140-danzay-1557/reading.txt, transcription
  https://raw.githubusercontent.com/NoAutopilot/cipher-lab/main/ciphers/fr20140-danzay-1557/ciphertext.txt, key https://raw.githubusercontent.com/NoAutopilot/cipher-lab/main/ciphers/fr20140-danzay-1557/key.tsv, notes
  https://raw.githubusercontent.com/NoAutopilot/cipher-lab/main/ciphers/fr20140-danzay-1557/NOTES.md, our search log https://raw.githubusercontent.com/NoAutopilot/cipher-lab/main/ciphers/fr20140-danzay-1557/AUDIT.md.
- Distinctive phrases, clear hand (search with spelling variants): "le plus commodement qu'il me sera
  possible"; "ceste depesche affin que vous peussiez congnoistre l'estat des affaires de ce royaulme";
  "la promesse qui de long temps m'a esté faicte"; "attendant plus certain et expres commandement de ce
  que je doy entreprendre"; "il me semble qu'il seroyt bon de regarder". From the cipher: "chancelier",
  "Danoys", "marchans de Lion", "Augsbourg", "veulx tenyr", "je ne vous puys encores asseurer".

WHERE WE HAVE NOT YET LOOKED PROPERLY (start here)
- Delavaud, "Charles de Danzay" (Revue d'histoire diplomatique, 1911) and Cuisiat's edition of the
  Cardinal of Lorraine's correspondence (Lettres du cardinal Charles de Lorraine, 1998): does either print,
  quote or calendar a Danzay letter of January 1557?
- Daussy, Les huguenots et le roi (2002) and Daussy's other work on Danzay; Bricka's Danish edition of
  Danzay letters (1901); Danske Magazin; Handlinger rörande Skandinaviens historia; Rydberg, Sverges
  traktater; any Danish or Swedish edition of the French embassy correspondence 1548-1589.
- The Correspondance politique series of the Ministère des Affaires étrangères (Danemark); Ribier,
  Lettres et mémoires d'estat (1666); Teulet; the Négociations series; theses on Danzay.
- JSTOR, Persée, HathiTrust full text, which we cannot reach from our environment.

HOW TO REPORT (this part is the same for every label)
- Write your answer as one Markdown file in the repository github.com/NoAutopilot/cipher-lab at the path
  `ciphers/fr20140-danzay-1557/second-opinions/chatgpt-2026-09-24.md`. Do not touch any other file. Do not commit to `main`:
  create a branch named `second-opinion/SO-DANZAY-F35` and open a pull request from it, titled exactly
  `[SO-DANZAY-F35] second opinion: Danzay to the Cardinal of Lorraine, 27 Jan 1557`.
- The first lines of the file must be this header, filled in:
      label: SO-DANZAY-F35
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
