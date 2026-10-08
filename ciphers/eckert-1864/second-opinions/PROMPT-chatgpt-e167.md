SECOND OPINION REQUEST, label SO-ECKERT-E167

We are an open cipher-research repository (github.com/NoAutopilot/cipher-lab). We have read one American Civil War
cipher telegram and want you to try to prove that its text was already printed before us, and to find mistakes in our
reading. Be adversarial: we would rather learn now that it is in print than claim it wrongly later.

THE ITEM
- Source: Thomas T. Eckert Papers, Huntington Library, San Marino, mssEC 25 ("Ciphers Received and Sent", Fort Monroe) p.274 (digital pointer 5818), entry E167, headed "New York Dec 6th 1864 / Geo D Sheldon Ft. Monroe", https://hdl.huntington.org/digital/collection/p16003coll11/id/5818. Read with War Department Cipher No. 1 (Huntington mssEC 41).
- Reading: Wm. Bradford (signed "Wm breeds ford"; John Horner, the military telegraph operator at New York, signs the transmission) to Maj. Gen. B. F. Butler via Sheldon at Fort Monroe, 6 Dec 1864: "[The steamer] Russia is in [New York]. Have examined her. Accommodations poor, for [horses] bad. River services bad, outside good. Draft not less than [7] and [1] half feet. Power good. Length [205] and depth [12] feet. Not more than [14] [miles] per hour speed. Mattawan not the craft for your services. Have not seen Sanborne yet. Particulars by letter. Yours, Wm. Bradford, address [37] Broad ..." ("Wesport raining here" not settled). Corrected 8 Oct 2026 by AUD2-LEDGER-4 (AUDIT.md "## AUDIT 2 (AUD2-LEDGER-4)"); most of the body is in clear in the Huntington's public transcription.
- Context we already know: The first Fort Fisher expedition was assembling; a transport Russia sailed with it (ORN ser. I vol. 11). Butler's dispatch boat Greyhound had burned in late Nov 1864, and Butler sent its master, Mr. Bradford, north "to select another boat for similar uses" (Butler, Private and Official Correspondence vol. V p.367, to George H. Powers).
- Our files: reading https://raw.githubusercontent.com/NoAutopilot/cipher-lab/main/ciphers/eckert-1864/reading.md,
  key https://raw.githubusercontent.com/NoAutopilot/cipher-lab/main/ciphers/eckert-1864/key.md, search log
  https://raw.githubusercontent.com/NoAutopilot/cipher-lab/main/ciphers/eckert-1864/AUDIT.md (section "AUDIT (FV-FM2)").

WHERE WE HAVE LOOKED: OR ser. I vol. 42 pt 3; ORN ser. I vols. 10-11; Butler's Private and Official Correspondence vols. IV-V (local text search); Internet Archive full text; the Huntington's CONTENTdm full-text search.

WHERE WE HAVE NOT YET LOOKED PROPERLY (start here)
- Butler's Book (1892); Butler's letterbooks (NARA RG 393); New York newspapers of Dec 1864 (shipping news for the Russia and the Mattawan); Google Books; HathiTrust; JSTOR.

HOW TO REPORT (this part is the same for every label)
- Write your answer as one Markdown file in the repository github.com/NoAutopilot/cipher-lab at the path
  `ciphers/eckert-1864/second-opinions/chatgpt-e167-<UTC date>.md`. Do not touch any other file. Do not commit to `main`:
  create a branch named `second-opinion/SO-ECKERT-E167` and open a pull request from it, titled exactly
  `[SO-ECKERT-E167] second opinion: Bradford to Butler, the steamer Russia, 6 Dec 1864`.
- The first lines of the file must be this header, filled in:
      label: SO-ECKERT-E167
      model: <your model name and version>
      date: <UTC date you answered>
      prompt: PROMPT-chatgpt-e167.md in this folder
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
