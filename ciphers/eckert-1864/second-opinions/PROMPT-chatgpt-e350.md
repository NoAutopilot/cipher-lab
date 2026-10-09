SECOND OPINION REQUEST, label SO-ECKERT-E350

We are an open cipher-research repository (github.com/NoAutopilot/cipher-lab). We have read one American Civil War
cipher telegram and want you to try to prove that its text was already printed before us, and to find mistakes in our
reading. Be adversarial: we would rather learn now that it is in print than claim it wrongly later.

THE ITEM
- Source: Thomas T. Eckert Papers, Huntington Library, San Marino, mssEC 18 (War Department telegraph office, ciphers sent) p.229 (digital pointer 9895), the second entry on the page, E350, headed "Capt R C Clowry / Wash'n Nov. 10th 1864", signed Wm Redwood Price, https://hdl.huntington.org/digital/collection/p16003coll11/id/9895. Read with War Department Cipher No. 1 (Huntington mssEC 41).
- Reading: "[Washington] Nov [10] [9 PM] for [Colonel] A G Brackett, Special Inspector [Cavalry], Planters House, [St Louis]. [General-in-Chief] countermands the orders. Inform me Burnet House, [Cincinnati], Nov [12], when [General] Pleasonton's and Grierson's [commands] will be in [St Louis] and number of serviceable [horses] there for issue. Await orders. Will be in [Nashville] [15th] instant and [communicate]. [Signed] Wm Redwood Price, [Major] and so forth." Bracketed words are code words read from the period key; the rest is clear on the page (the Huntington transcription has "Tomama"; the page reads "Panama", the key word for Cavalry).
- Context we already know: Official Records ser. I vol. 45 pt 1: p.898 (Chambliss, Special Inspector Cavalry, Louisville 16 Nov 1864: "Major Price telegraphed me he would be here on the 14th"), p.952 (19 Nov: "Major Brackett, of the Cavalry Bureau"; Grierson's men at Saint Louis), p.1001 (Price, assistant inspector general of the Cavalry Bureau).
- Our files: reading https://raw.githubusercontent.com/NoAutopilot/cipher-lab/main/ciphers/eckert-1864/reading.md,
  key https://raw.githubusercontent.com/NoAutopilot/cipher-lab/main/ciphers/eckert-1864/key.md, search log
  https://raw.githubusercontent.com/NoAutopilot/cipher-lab/main/ciphers/eckert-1864/AUDIT.md (section "AUDIT (FV-MS18g)").

WHERE WE HAVE LOOKED: Official Records ser. I vols 41 pt 4 and 45 pt 1-2 (letters-only phrase grep and by name) and 166 other cached texts; Google Books (API); the Huntington's CONTENTdm full-text search.

WHERE WE HAVE NOT YET LOOKED PROPERLY (start here)
- Cavalry Bureau records (NARA RG 94/107/92); A. G. Brackett's papers and his History of the United States Cavalry (1865); St Louis and Cincinnati press of 10-15 Nov 1864; HathiTrust; JSTOR.

HOW TO REPORT (this part is the same for every label)
- Write your answer as one Markdown file in the repository github.com/NoAutopilot/cipher-lab at the path
  `ciphers/eckert-1864/second-opinions/chatgpt-e350-<UTC date>.md`. Do not touch any other file. Do not commit to `main`:
  create a branch named `second-opinion/SO-ECKERT-E350` and open a pull request from it, titled exactly
  `[SO-ECKERT-E350] second opinion: Price, Cavalry Bureau, to Brackett, St Louis: Pleasonton's and Grierson's commands and horses, 10 Nov 1864`.
- The first lines of the file must be this header, filled in:
      label: SO-ECKERT-E350
      model: <your model name and version>
      date: <UTC date you answered>
      prompt: PROMPT-chatgpt-e350.md in this folder
  and then sections 1-5 in the order below.
- Every citation must be checkable from a desk: author, title, year, volume, page, and a URL to the page
  on Google Books, HathiTrust, Internet Archive, Gallica or the publisher. If you cannot give a page and a
  URL, mark the citation "unverified". Never invent a page number.
- Do not use the words "first", "new", "unpublished", "unread" or "never printed" about our reading. Our
  rule is that only a separate verifier may say that. Your job is to try to prove the opposite: that the
  text is already in print somewhere, or that our reading is wrong.

WHAT TO PUT IN THE FILE
1. Prior print: any edition, calendar, article or book that prints this telegram, quotes it, summarises it,
   or prints its decipherment. Give the earliest you can find. If you find nothing, list exactly what you
   searched (catalogue, query, date) so we can tell a real gap from a shallow search.
2. Prior decipherment: anyone who has already read this cipher entry, including blog posts, GitHub
   repositories, the Decoding the Civil War project, DECODE (de-crypt.org) records, theses, and papers.
3. Errors in our reading: any token, name, date or phrase you believe is misread, with your reason and
   the source that shows it.
4. Leads: archives, editions or scholars we should check, with a one-line reason each.
5. Confidence: one sentence on how sure you are that nothing prior exists, and what would change it.
