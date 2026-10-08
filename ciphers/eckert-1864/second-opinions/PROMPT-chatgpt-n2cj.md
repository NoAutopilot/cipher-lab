SECOND OPINION REQUEST, label SO-ECKERT-N2CJ

We are an open cipher-research repository (github.com/NoAutopilot/cipher-lab). We have read one American Civil War
cipher telegram and want you to try to prove that its text was already printed before us, and to find mistakes in our
reading. Be adversarial: we would rather learn now that it is in print than claim it wrongly later.

THE ITEM
- Source: Thomas T. Eckert's telegraph ledgers, Huntington Library, San Marino, mssEC 19 p.248 (digital pointer 9142), entry N2-CJ, headed "J. H. Emerick City Point, Washington D. C. Dec. 18. '64", https://hdl.huntington.org/digital/collection/p16003coll11/id/9142. Read with War Department Cipher No. 2 (Huntington mssEC 47).
- Reading: to Col. Bradley, chief quartermaster, City Point, 18 Dec 1864 (signed with a group the reader takes as Ingalls, uncertain): the orders given at first in relation to the transports for Sherman will be carried out. Have such of the boats named as are in the James sent off as directed without delay to their destination.
- Context we already know: The frame is in clear in the Huntington's public transcription; "Sherman" and "the James" are code words.
- Our files: reading https://raw.githubusercontent.com/NoAutopilot/cipher-lab/main/ciphers/eckert-1864/reading-no2.md,
  key https://raw.githubusercontent.com/NoAutopilot/cipher-lab/main/ciphers/eckert-1864/key-no2.md, search log
  https://raw.githubusercontent.com/NoAutopilot/cipher-lab/main/ciphers/eckert-1864/AUDIT.md (section "AUDIT (FV-LS4-R2b)").

WHERE WE HAVE LOOKED: OR ser. I vols. 42 pt 3 and 44 (local text search); Internet Archive full text; Google Books.

WHERE WE HAVE NOT YET LOOKED PROPERLY (start here)
- The Papers of Ulysses S. Grant vol. 13, Quartermaster General's records (NARA RG 92), ORN ser. I vols. 11 and 16 (transports to Savannah), HathiTrust and JSTOR.

HOW TO REPORT (this part is the same for every label)
- Write your answer as one Markdown file in the repository github.com/NoAutopilot/cipher-lab at the path
  `ciphers/eckert-1864/second-opinions/chatgpt-n2cj-<UTC date>.md`. Do not touch any other file. Do not commit to `main`:
  create a branch named `second-opinion/SO-ECKERT-N2CJ` and open a pull request from it, titled exactly
  `[SO-ECKERT-N2CJ] second opinion: to Col. Bradley at City Point, boats in the James for Sherman's transports, 18 Dec 1864`.
- The first lines of the file must be this header, filled in:
      label: SO-ECKERT-N2CJ
      model: <your model name and version>
      date: <UTC date you answered>
      prompt: PROMPT-chatgpt-n2cj.md in this folder
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
