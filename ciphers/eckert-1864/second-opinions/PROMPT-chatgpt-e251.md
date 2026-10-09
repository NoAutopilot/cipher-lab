SECOND OPINION REQUEST, label SO-ECKERT-E251

We are an open cipher-research repository (github.com/NoAutopilot/cipher-lab). We have read one American Civil War
cipher telegram and want you to try to prove that its text was already printed before us, and to find mistakes in our
reading. Be adversarial: we would rather learn now that it is in print than claim it wrongly later.

THE ITEM
- Source: Thomas T. Eckert Papers, Huntington Library, San Marino, mssEC 25 ("Ciphers Received and Sent", Fort Monroe) p.272 (digital pointer 5816), entry E251, headed "Hd Qrs Army of James Dec 4 1250 PM / Geo D Sheldon Ft Monroe", https://hdl.huntington.org/digital/collection/p16003coll11/id/5816. Read with War Department Cipher No. 1 (Huntington mssEC 41).
- Reading: R. O'Brien for Maj. Gen. B. F. Butler, Hd Qrs Army of the James, to Fort Monroe, 4 Dec 1864: "[1 PM] For [Major] Carney, [Norfolk]. Tell [Colonel] Saunders [to] make a [report] to be sent me [by] tomorrow's boat of property found on him by any officers, captured at the time or taken from Stephen Barton of Bartonsville, [North Carolina]. Say nothing about this [telegram]. If [Colonel] Saunders is not able to make the [report] himself, get the facts and make the [report] yourself; also send me all the books and papers taken from Barton. Make and send these [report]s without attracting any observation. [Signed] [Butler]. R. O'Brien." Bracketed words are code words read from the period key.
- Context we already know: Butler's Private and Official Correspondence vol. V p.265: Butler to Shepley, Norfolk, 15 Oct 1864, Stephen Barton of Bartonsville, Hertford Co., arrested near South Mills with his property; send him up with all papers found upon him. Butler's Private and Official Correspondence vol. V p.11: Butler to Col. Saunders, 6 Aug 1864, assigning him to Norfolk as Provost Marshal; vol. V (Butler's later statement): Maj. Geo. C. Carney, Quartermaster's Department, Superintendent of Negro Affairs.
- Our files: reading https://raw.githubusercontent.com/NoAutopilot/cipher-lab/main/ciphers/eckert-1864/reading.md,
  key https://raw.githubusercontent.com/NoAutopilot/cipher-lab/main/ciphers/eckert-1864/key.md, search log
  https://raw.githubusercontent.com/NoAutopilot/cipher-lab/main/ciphers/eckert-1864/AUDIT.md (section "AUDIT (FV-FM7a)"; it corrects reading.md where they differ).

WHERE WE HAVE LOOKED: the Huntington's CONTENTdm full-text search across all pointers; OR ser. I vols. 35 pt 2, 40 pts 1-2, 42 pts 2-3, 43 pt 1 (full text); Butler's Private and Official Correspondence vols. IV-V; Plum, The Military Telegraph during the Civil War (1882) vols. I-II; the Grant Papers vols. 10-12 (Internet Archive full-text search, snippets only). Second audit (9 Oct 2026) added: the History of the 104th Pennsylvania Regiment (Davis, 1866) and a page-by-page read of OR ser. I vol. 35 pt 2 and vol. 40 pts 1-2 for the telegram's dates.

WHERE WE HAVE NOT YET LOOKED PROPERLY (start here)
- Norfolk provost-marshal records and the Department of Virginia and North Carolina letters of Dec 1864 (NARA RG 393); OR ser. I vol. 42 pt 3 page by page for 1-6 Dec 1864; North Carolina local histories of Hertford County (Bartonsville); Google Books; HathiTrust.

HOW TO REPORT (this part is the same for every label)
- Write your answer as one Markdown file in the repository github.com/NoAutopilot/cipher-lab at the path
  `ciphers/eckert-1864/second-opinions/chatgpt-e251-<UTC date>.md`. Do not touch any other file. Do not commit to `main`:
  create a branch named `second-opinion/SO-ECKERT-E251` and open a pull request from it, titled exactly
  `[SO-ECKERT-E251] second opinion: O'Brien for Butler to Maj. Carney, Norfolk: report on Stephen Barton's property, 4 Dec 1864`.
- The first lines of the file must be this header, filled in:
      label: SO-ECKERT-E251
      model: <your model name and version>
      date: <UTC date you answered>
      prompt: PROMPT-chatgpt-e251.md in this folder
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
