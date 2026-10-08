SECOND OPINION REQUEST, label SO-ECKERT-E191

We are an open cipher-research repository (github.com/NoAutopilot/cipher-lab). We have read one American Civil War
cipher telegram and want you to try to prove that its text was already printed before us, and to find mistakes in our
reading. Be adversarial: we would rather learn now that it is in print than claim it wrongly later.

THE ITEM
- Source: Thomas T. Eckert Papers, Huntington Library, San Marino, mssEC 25 ("Ciphers Received and Sent", Fort Monroe) p.45 (digital pointer 5589), entry E191, headed "Ft. Monroe March 28 1864 / Geo W Baldwin Baltimore", https://hdl.huntington.org/digital/collection/p16003coll11/id/5589. Read with War Department Cipher No. 1 (Huntington mssEC 41).
- Reading: Maj. Gen. B. F. Butler (via Sheldon at Fort Monroe) to Maj. Gen. Lew Wallace, Baltimore, 28 Mar 1864: "I think you had better [arrest] at once [Colonel] William Chestnut, corner of South and Pratt streets, [Baltimore], and hold him safe. Please send me by [tomorrow] night's boat a confidential member of your staff of high intelligence. [Signed] [Butler] [12]".
- Context we already know: Wallace took command of the Middle Department (Baltimore) on 22 Mar 1864. Colonel William Chestnut is identified in the press: the Alexandria Gazette of 31 Mar 1864, p.1 (https://www.loc.gov/resource/sn85025007/1864-03-31/ed-1/?sp=1), reports that "Col. William Chestnut, grocer and commission merchant, and a prominent Union man, in Baltimore, was arrested yesterday morning ... at the request and by order of Gen. Butler", reportedly over contraband sales to Fortress Monroe or Norfolk. That prints the arrest, not this telegram.
- Our files: reading https://raw.githubusercontent.com/NoAutopilot/cipher-lab/main/ciphers/eckert-1864/reading.md,
  key https://raw.githubusercontent.com/NoAutopilot/cipher-lab/main/ciphers/eckert-1864/key.md, search log
  https://raw.githubusercontent.com/NoAutopilot/cipher-lab/main/ciphers/eckert-1864/AUDIT.md (sections "AUDIT (FV-FM3c)" and "AUDIT 2 (AUD2-LEDGER-7)").

WHERE WE HAVE LOOKED: OR ser. I vol. 33, ser. II vol. 6; Wallace's Autobiography (1906); Chronicling America (Alexandria Gazette, Evening Star, National Intelligencer hits); Butler's Private and Official Correspondence vols. III-IV (local text search); Internet Archive full text; the Huntington's CONTENTdm full-text search.

WHERE WE HAVE NOT YET LOOKED PROPERLY (start here)
- Baltimore newspapers (American, Sun, Clipper) of 29 Mar-10 Apr 1864, which may print the order or the charge; Lew Wallace's papers (Indiana Historical Society); Butler's Book (1892); Google Books; HathiTrust; JSTOR.

HOW TO REPORT (this part is the same for every label)
- Write your answer as one Markdown file in the repository github.com/NoAutopilot/cipher-lab at the path
  `ciphers/eckert-1864/second-opinions/chatgpt-e191-<UTC date>.md`. Do not touch any other file. Do not commit to `main`:
  create a branch named `second-opinion/SO-ECKERT-E191` and open a pull request from it, titled exactly
  `[SO-ECKERT-E191] second opinion: Butler to Lew Wallace, arrest Colonel William Chestnut, 28 Mar 1864`.
- The first lines of the file must be this header, filled in:
      label: SO-ECKERT-E191
      model: <your model name and version>
      date: <UTC date you answered>
      prompt: PROMPT-chatgpt-e191.md in this folder
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
