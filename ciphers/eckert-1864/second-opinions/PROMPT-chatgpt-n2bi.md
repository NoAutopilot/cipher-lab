SECOND OPINION REQUEST, label SO-ECKERT-N2BI

We are an open cipher-research repository (github.com/NoAutopilot/cipher-lab). We have read one American Civil War
cipher telegram and want you to try to prove that its text was already printed before us, and to find mistakes in our
reading. Be adversarial: we would rather learn now that it is in print than claim it wrongly later.

THE ITEM
- Source: Thomas T. Eckert's telegraph ledger, Huntington Library, San Marino, mssEC 19 p.119 (digital pointer 9011),
  https://hdl.huntington.org/digital/collection/p16003coll11/id/9011, entry N2-BI, 24 July 1864. Read with War Department Cipher No. 2 (mssEC 47); the book is in the same collection.
- Reading: Meigs to Ingalls 24 July 1864: about 1,000 cavalry horses on hand to be sent with artillery horses; depreciation of vouchers and certificates and short supply of money have checked deliveries; 3,962 cavalry horses issued since 1 July.
- Our files: reading https://raw.githubusercontent.com/NoAutopilot/cipher-lab/main/ciphers/eckert-1864/reading-no2.md,
  key https://raw.githubusercontent.com/NoAutopilot/cipher-lab/main/ciphers/eckert-1864/key-no2.md, search log
  https://raw.githubusercontent.com/NoAutopilot/cipher-lab/main/ciphers/eckert-1864/AUDIT.md (section "AUDIT (LS-V6)").

WHERE WE HAVE LOOKED: the Official Records by date and correspondent (ser. I and III); Chronicling America; Internet Archive full text; Google Books; OpenAlex, Semantic Scholar, CORE.

WHERE WE HAVE NOT YET LOOKED PROPERLY (start here)
- NARA RG 92 (Quartermaster General, telegrams sent, July 1864); Meigs's annual report for 1864 (OR ser. III vol. 4 and vol. 5).
- HathiTrust full text and JSTOR, which we cannot reach from our environment.

HOW TO REPORT (this part is the same for every label)
- Write your answer as one Markdown file in the repository github.com/NoAutopilot/cipher-lab at the path
  `ciphers/eckert-1864/second-opinions/chatgpt-n2bi-<UTC date>.md`. Do not touch any other file. Do not commit to `main`:
  create a branch named `second-opinion/SO-ECKERT-N2BI` and open a pull request from it, titled exactly
  `[SO-ECKERT-N2BI] second opinion: to Ingalls, City Point, on horses, 24 July 1864`.
- The first lines of the file must be this header, filled in:
      label: SO-ECKERT-N2BI
      model: <your model name and version>
      date: <UTC date you answered>
      prompt: PROMPT-chatgpt-n2bi.md in this folder
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
