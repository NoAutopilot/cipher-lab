SECOND OPINION REQUEST, label SO-ECKERT-E103

We are an open cipher-research repository (github.com/NoAutopilot/cipher-lab). We have read one American Civil War
cipher telegram and want you to try to prove that its text was already printed before us, and to find mistakes in our
reading. Be adversarial: we would rather learn now that it is in print than claim it wrongly later.

THE ITEM
- Source: Thomas T. Eckert's telegraph ledgers, Huntington Library, San Marino, mssEC 19 p.237 (digital pointer 9129), entry E103, headed "J. C. Van Duzer Wash'n Nov 28th 1864 10.30 A. M.", https://hdl.huntington.org/digital/collection/p16003coll11/id/9129. Read with War Department Cipher No. 1 (Huntington mssEC 41).
- Reading: C. A. Dana (Assistant Secretary of War) to Brig. Gen. [J. D.?] Webster, 28 Nov 1864, 10.30 AM: "Orders have been given to transfer to [Baltimore] all mail matter in [?] dead for [Maj. Gen. Sherman's] [Army]. [C. A. Dana]" -- the words "feeble dead" are not understood.
- Context we already know: Related but not this telegram: the Army and Navy Journal of 31 Dec 1864 says mail for Sherman's army goes by way of New York; Sherman's own 1865 order routes it to Old Point via Baltimore.
- Our files: reading https://raw.githubusercontent.com/NoAutopilot/cipher-lab/main/ciphers/eckert-1864/reading.md,
  key https://raw.githubusercontent.com/NoAutopilot/cipher-lab/main/ciphers/eckert-1864/key.md, search log
  https://raw.githubusercontent.com/NoAutopilot/cipher-lab/main/ciphers/eckert-1864/AUDIT.md (section "AUDIT (FV-LS5-A)").

WHERE WE HAVE LOOKED: OR ser. I vols. 44 and 45 (local text search); Internet Archive full text; Google Books; the Huntington's CONTENTdm full-text search.

WHERE WE HAVE NOT YET LOOKED PROPERLY (start here)
- Dana's War Department telegrams of 28 Nov 1864 (NARA RG 107), Post Office Department records and the Postmaster General's report for 1865, the press of late Nov 1864, HathiTrust and JSTOR.

HOW TO REPORT (this part is the same for every label)
- Write your answer as one Markdown file in the repository github.com/NoAutopilot/cipher-lab at the path
  `ciphers/eckert-1864/second-opinions/chatgpt-e103-<UTC date>.md`. Do not touch any other file. Do not commit to `main`:
  create a branch named `second-opinion/SO-ECKERT-E103` and open a pull request from it, titled exactly
  `[SO-ECKERT-E103] second opinion: C. A. Dana to Webster, Sherman's army mail to Baltimore, 28 Nov 1864`.
- The first lines of the file must be this header, filled in:
      label: SO-ECKERT-E103
      model: <your model name and version>
      date: <UTC date you answered>
      prompt: PROMPT-chatgpt-e103.md in this folder
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
