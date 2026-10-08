SECOND OPINION REQUEST, label SO-ECKERT-E49

We are an open cipher-research repository (github.com/NoAutopilot/cipher-lab). We have read one American Civil War
cipher telegram and want you to try to prove that its text was already printed before us, and to find mistakes in our
reading. Be adversarial: we would rather learn now that it is in print than claim it wrongly later.

THE ITEM
- Source: Thomas T. Eckert's telegraph ledger, Huntington Library, San Marino, mssEC 19 p.91 (digital pointer 8983),
  https://hdl.huntington.org/digital/collection/p16003coll11/id/8983, entry E49, headed "Sheldon, Washington 12 June 1864 4.10 PM, to Biggs, chief quartermaster, Fort Monroe". Read with War Department Cipher No. 1 (the book is in the same collection, mssEC 41).
- Reading: Meigs, Quartermaster General, to Biggs: an expedition sixteen thousand strong is to embark at White House tomorrow; send to that place immediately every vessel fitted to aid in this movement and in removing stores and wounded to a new base or hospital.
- Context we already know: The movement of 13 June 1864 from White House by water is well known; this telegram itself we have not found in print.
- Our files: reading https://raw.githubusercontent.com/NoAutopilot/cipher-lab/main/ciphers/eckert-1864/reading.md,
  key https://raw.githubusercontent.com/NoAutopilot/cipher-lab/main/ciphers/eckert-1864/key.md, search log
  https://raw.githubusercontent.com/NoAutopilot/cipher-lab/main/ciphers/eckert-1864/AUDIT.md (section "AUDIT (LS-V4)").

WHERE WE HAVE LOOKED: OR ser. I vol. 36 pt 3 and vol. 40 pt 2; OR ser. III vol. 4; Internet Archive full text; Google Books.

WHERE WE HAVE NOT YET LOOKED PROPERLY (start here)
- NARA RG 92 (Quartermaster General telegrams sent, June 1864); Meigs papers (Library of Congress); Ingalls/Biggs reports in the Quartermaster General annual report 1865.
- HathiTrust full text and JSTOR, which we cannot reach from our environment.

HOW TO REPORT (this part is the same for every label)
- Write your answer as one Markdown file in the repository github.com/NoAutopilot/cipher-lab at the path
  `ciphers/eckert-1864/second-opinions/chatgpt-e49-<UTC date>.md`. Do not touch any other file. Do not commit to `main`:
  create a branch named `second-opinion/SO-ECKERT-E49` and open a pull request from it, titled exactly
  `[SO-ECKERT-E49] second opinion: to Biggs, an expedition of 16,000 to embark at White House, 12 June 1864`.
- The first lines of the file must be this header, filled in:
      label: SO-ECKERT-E49
      model: <your model name and version>
      date: <UTC date you answered>
      prompt: PROMPT-chatgpt-e49.md in this folder
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
