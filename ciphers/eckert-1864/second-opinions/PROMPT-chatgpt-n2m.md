SECOND OPINION REQUEST, label SO-ECKERT-N2M

We are an open cipher-research repository (github.com/NoAutopilot/cipher-lab). We have read one American Civil War
cipher telegram and want you to try to prove that its text was already printed before us, and to find mistakes in our
reading. Be adversarial: we would rather learn now that it is in print than claim it wrongly later.

THE ITEM
- Source: Thomas T. Eckert's telegraph ledger, Huntington Library, San Marino, mssEC 19 p.90 (digital pointer 8982,
  https://hdl.huntington.org/digital/collection/p16003coll11/id/8982), entry headed "Kimber Vicksburg  Washn June 11
  1864". Read with War Department Cipher No. 2 (the book is in the same collection, mssEC 47).
- Reading, 11 June 1864, 1 PM, Washington to Maj. Gen. E. R. S. Canby at Vicksburg, telegraph operator S. P. Kimber:
  "I can not find the gauge of the Vicksburg & Shreveport Rail-road. What is it?" signed with the code word the book
  gives for the Quartermaster-General (M. C. Meigs; the book's own entry carries a query mark). After the signature:
  "use Farmer Famish Mastiff for Can[by]", a service line naming the three code words for Canby.
- Our files: reading https://raw.githubusercontent.com/NoAutopilot/cipher-lab/main/ciphers/eckert-1864/reading-no2.md,
  key https://raw.githubusercontent.com/NoAutopilot/cipher-lab/main/ciphers/eckert-1864/key-no2.md, search log
  https://raw.githubusercontent.com/NoAutopilot/cipher-lab/main/ciphers/eckert-1864/AUDIT.md (section "AUDIT
  (propagation, AM-ECKV)").
- Context we found: Official Records ser. I vol. 34 pt 4 pp.424-425 prints Meigs to Canby, Washington, 17 June 1864,
  1.30 p.m., "I have telegraphed you twice to inform me of the gauge", and Canby's reply of 24 June. So this telegram is
  probably one of the two earlier ones, and copies may be in Meigs's letter books or the Quartermaster records.

WHERE WE HAVE LOOKED: Official Records ser. I vol. 34 pt 4 (full text, every 11 June 1864 item) and ser. III vol. 4;
Google Books phrase searches ("can not find the gauge", "gauge of the Vicksburg and Shreveport"); the Huntington's
catalogue record for the page.

WHERE WE HAVE NOT YET LOOKED PROPERLY (start here)
- Meigs's letter books and papers at the Library of Congress; NARA RG 92 (Quartermaster General) telegrams sent, and
  M504/M473 telegram series; any printed calendar of them.
- Canby papers and biographies (Heyman, Prudent Soldier, 1959); Miller, Second Only to Grant (2000).
- Histories of the Vicksburg, Shreveport and Texas Railroad and of the U.S. Military Railroads (McCallum's report).
- HathiTrust full text and JSTOR, which we cannot reach from our environment.

HOW TO REPORT (this part is the same for every label)
- Write your answer as one Markdown file in the repository github.com/NoAutopilot/cipher-lab at the path
  `ciphers/eckert-1864/second-opinions/chatgpt-n2m-<UTC date>.md`. Do not touch any other file. Do not commit to `main`:
  create a branch named `second-opinion/SO-ECKERT-N2M` and open a pull request from it, titled exactly
  `[SO-ECKERT-N2M] second opinion: QMG to Canby, 11 June 1864`.
- The first lines of the file must be this header, filled in:
      label: SO-ECKERT-N2M
      model: <your model name and version>
      date: <UTC date you answered>
      prompt: PROMPT-chatgpt-n2m.md in this folder
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
