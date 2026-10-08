SECOND OPINION REQUEST, label SO-ECKERT-O9AH

We are an open cipher-research repository (github.com/NoAutopilot/cipher-lab). We have read one American Civil War
cipher telegram and want you to try to prove that its text was already printed before us, and to find mistakes in our
reading. Be adversarial: we would rather learn now that it is in print than claim it wrongly later.

THE ITEM
- Source: Thomas T. Eckert's telegraph ledger, Huntington Library, San Marino, mssEC 19 p.45 (digital pointer 8937),
  https://hdl.huntington.org/digital/collection/p16003coll11/id/8937, entry O9-AH, 20 Apr 1864. Read with the War Department's older cipher vocabulary (mssEC 67); the book is in the same collection.
- Reading: to Capt. G. D. Wise, Astor House, New York, 20 Apr 1864: communicate with Maj. Van Vliet, who has chartered vessels for the expedition; all to reach Fort Monroe by the 24th and be coaled by the 25th; Butler desires to move 30,000 men, 2,000 horses, equipage of ten batteries and 100 wagons, with room for the men to lie down.
- Our files: reading https://raw.githubusercontent.com/NoAutopilot/cipher-lab/main/ciphers/eckert-1864/reading-no9.md,
  key https://raw.githubusercontent.com/NoAutopilot/cipher-lab/main/ciphers/eckert-1864/key-no9.md, search log
  https://raw.githubusercontent.com/NoAutopilot/cipher-lab/main/ciphers/eckert-1864/AUDIT.md (section "AUDIT (LS-V6)").

WHERE WE HAVE LOOKED: the Official Records by date and correspondent (ser. I and III); Chronicling America; Internet Archive full text; Google Books; OpenAlex, Semantic Scholar, CORE.

WHERE WE HAVE NOT YET LOOKED PROPERLY (start here)
- ORN ser. I vols 9-10 (Butler's James River expedition, transports); NARA RG 92 (Quartermaster General, April 1864); the New York press of 20-30 April 1864.
- HathiTrust full text and JSTOR, which we cannot reach from our environment.

HOW TO REPORT (this part is the same for every label)
- Write your answer as one Markdown file in the repository github.com/NoAutopilot/cipher-lab at the path
  `ciphers/eckert-1864/second-opinions/chatgpt-o9ah-<UTC date>.md`. Do not touch any other file. Do not commit to `main`:
  create a branch named `second-opinion/SO-ECKERT-O9AH` and open a pull request from it, titled exactly
  `[SO-ECKERT-O9AH] second opinion: to Wise on transports for Butler, 20 Apr 1864`.
- The first lines of the file must be this header, filled in:
      label: SO-ECKERT-O9AH
      model: <your model name and version>
      date: <UTC date you answered>
      prompt: PROMPT-chatgpt-o9ah.md in this folder
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
