SECOND OPINION REQUEST, label SO-ES132-F89-F119

We are an open cipher-research repository (github.com/NoAutopilot/cipher-lab). We have applied a published key to two
ciphered letters of Philip II to his ambassador in Paris and want you to try to prove that their text was already printed
before us, and to find mistakes in our reading. Be adversarial: we would rather learn now that it is in print than claim
it wrongly later.

THE ITEMS
- Source: Bibliothèque nationale de France, Espagnol 132 (Gallica ark:/12148/btv1b10032556x), papers of Juan de Vargas
  Mexía (Mejía), Spanish ambassador in Paris. Letter A: f.89r-f.91r (canvases 86-88), Philip II to Vargas, Madrid,
  19 September 1578; a second ciphered copy of the same letter is at f.93-96. Letter B: f.119r-f.120r (canvases 116-117),
  Philip II to Vargas, Madrid, 15 October 1578.
- Cipher: Vargas Mexía's "Cipher 3" (Devos 1950 Cp.30; Alcocer 1921; key table published by S. Tomokiyo, cryptiana).
- What is already in print (we know): one paragraph of each letter (the Scotland paragraph: the Scottish ambassador,
  Antonio de Guaras, Bernardino de Mendoza; the 4,000 men) is printed by A. Teulet, Papiers d'état ... relatifs à
  l'histoire de l'Écosse, t. III (1860) pp.196-197 and 202-203, and Relations politiques ... avec l'Écosse t. V (1862),
  from the "Déchiffrement officiel", Archives nationales, Simancas fonds, liasse B 47 nos. 8 and 6.
- What we ask about: the OTHER paragraphs, which we read only uncertainly (syllable by syllable, graded M). Phrases as
  we read them: "arçobispo de Nazaret" (f.89r), "prohibir de veras y castigar con rigor", "tan injusta y de tan mal
  nombre", "el de Alanzon y el de Bearne" (f.90r), "las naos de Indias que se tomaron", "lo que toca a la navegacion de
  las Indias", "lo del trigo" (f.90v), "andamientos y pretension de ... Bearne", "don Sancho de Leyva" (f.91r),
  "se ha dado en esa villa a las predicas" (f.119r), "sobre lo de las piraterias" (f.120r).
- Our files: readings https://raw.githubusercontent.com/NoAutopilot/cipher-lab/main/ciphers/es132-vargas-mexia-1578/reading_f89r.txt
  (and reading_f89v, f90r, f90v, f91r, f119r, f119v, f120r in the same folder), key
  https://raw.githubusercontent.com/NoAutopilot/cipher-lab/main/ciphers/es132-vargas-mexia-1578/key.tsv, search log
  https://raw.githubusercontent.com/NoAutopilot/cipher-lab/main/ciphers/es132-vargas-mexia-1578/AUDIT.md (AUDIT 1 and AUDIT 2).

WHERE WE HAVE LOOKED: Teulet (both editions); Kervyn de Lettenhove, Relations politiques des Pays-Bas et de
l'Angleterre t. X-XI; Hume, Calendar of State Papers Spanish (Simancas) vol. 2 (1894: prints the king's letters of the
same days to Mendoza, not to Vargas); CODOIN vols. 6, 51 (Vargas's letters to Alonso de Curiel, 1578) and 112; Mignet,
Antonio Perez (1846); Gachard, La Bibliothèque nationale à Paris (1875); Les Sources inédites de l'histoire du Maroc;
Internet Archive and Google Books full text; OpenAlex; the cabinet-noir and other solver repositories; DECODE records
1980 and 1983.

WHERE WE HAVE NOT YET LOOKED PROPERLY (start here)
- J. Lefèvre, Correspondance de Philippe II sur les affaires des Pays-Bas, 2e partie, t. I (1577-1580), Brussels 1940.
- V. Vázquez de Prada, Felipe II y Francia (1559-1598) (2004), which works the AGS Estado K Vargas correspondence.
- AGS Estado K 1546-1548 (the king's minutes of 1578 to Vargas) and any calendar of them; BL Add MS 28421.
- Rubino, The Secrets of Antonio Pérez Decoded (Ohio State, 2012); García Hernán, Irlanda y el rey prudente (2000).
- HathiTrust full text and JSTOR.

HOW TO REPORT (this part is the same for every label)
- Write your answer as one Markdown file in the repository github.com/NoAutopilot/cipher-lab at the path
  `ciphers/es132-vargas-mexia-1578/second-opinions/chatgpt-<UTC date>.md`. Do not touch any other file. Do not commit to
  `main`: create a branch named `second-opinion/SO-ES132-F89-F119` and open a pull request from it, titled exactly
  `[SO-ES132-F89-F119] second opinion: Philip II to Vargas Mexia, 19 Sept and 15 Oct 1578, unprinted paragraphs`.
- The first lines of the file must be this header, filled in:
      label: SO-ES132-F89-F119
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
1. Prior print: any edition, calendar, article or book that prints these letters' other paragraphs, quotes them,
   summarises them, or prints their decipherment. Give the earliest you can find. If you find nothing, list exactly what
   you searched (catalogue, query, date) so we can tell a real gap from a shallow search.
2. Prior decipherment: anyone who has already read these two letters, including blog posts, GitHub repositories,
   DECODE (de-crypt.org) records, theses, and papers.
3. Errors in our reading: any word, name, date or phrase you believe is misread, with your reason and the source that
   shows it.
4. Leads: archives, editions or scholars we should check, with a one-line reason each.
5. Confidence: one sentence on how sure you are that nothing prior exists, and what would change it.
