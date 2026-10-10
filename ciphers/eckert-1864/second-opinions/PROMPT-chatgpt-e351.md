SECOND OPINION REQUEST, label SO-ECKERT-E351

We are an open cipher-research repository (github.com/NoAutopilot/cipher-lab). We have read one American Civil War-era
cipher telegram and want you to try to prove that its text was already printed before us, and to find mistakes in our
reading. Be adversarial: we would rather learn now that it is in print than claim it wrongly later.

THE ITEM
- Source: Thomas T. Eckert Papers, Huntington Library, San Marino, mssEC 18 (War Department telegraph office, ciphers sent) p.399 (digital pointer 10065), the second entry on the page, E351, headed "Bodle Balto / Wash Dec 2 1865", signed "Ed Town send asst Barton" (= Asst. Adjt. Gen. E. D. Townsend), https://hdl.huntington.org/digital/collection/p16003coll11/id/10065. Read with War Department Cipher No. 1 (Huntington mssEC 41).
- Reading: "[Washington] Dec [2] [2 PM] for [General] Hancock. Yours of this date recd. The [Secretary of War] says the habeas corpus in case of minors is not to be resisted. [Defend] the case as well as possible without counsel unless there is some peculiar point. [Report] the names of officers by whom minors discharged were illegally enlisted. Acknowledge receipt. [signed] Ed Townsend Asst [Adjt Genl]". Bracketed words are code words read from the period key; the rest is clear on the page.
- Context we already know: W. J. Bodle was Hancock's cipher operator at Baltimore in late 1865 (holder pointers 8012, 10060-10062). Hancock commanded the Middle Department. The telegram answers one of Hancock's of the same day, which we have not found.
- Our files: reading https://raw.githubusercontent.com/NoAutopilot/cipher-lab/main/ciphers/eckert-1864/reading.md,
  key https://raw.githubusercontent.com/NoAutopilot/cipher-lab/main/ciphers/eckert-1864/key.md, search log
  https://raw.githubusercontent.com/NoAutopilot/cipher-lab/main/ciphers/eckert-1864/AUDIT.md (section "AUDIT (FV-MS18j)").

WHERE WE HAVE LOOKED: Official Records ser. II vol. 8 and ser. III vol. 5 (a poor OCR copy), 164 cached edition texts; Google Books (API); Internet Archive full-text search; the Huntington's CONTENTdm full-text search.

WHERE WE HAVE NOT YET LOOKED PROPERLY (start here)
- Baltimore newspapers (Sun, American) of late Nov - early Dec 1865 for habeas corpus cases of enlisted minors before the federal or state courts; Hancock's Middle Department letters and telegrams (NARA RG 393), the Adjutant General's letters sent (NARA RG 94), the War Department telegrams sent (RG 107); OR ser. III vol. 5 in a readable text; HathiTrust; JSTOR.

HOW TO REPORT (this part is the same for every label)
- Write your answer as one Markdown file in the repository github.com/NoAutopilot/cipher-lab at the path
  `ciphers/eckert-1864/second-opinions/chatgpt-e351-<UTC date>.md`. Do not touch any other file. Do not commit to `main`:
  create a branch named `second-opinion/SO-ECKERT-E351` and open a pull request from it, titled exactly
  `[SO-ECKERT-E351] second opinion: Townsend for the Secretary of War to Hancock, Baltimore: habeas corpus for minors not to be resisted, 2 Dec 1865`.
- The first lines of the file must be this header, filled in:
      label: SO-ECKERT-E351
      model: <your model name and version>
      date: <UTC date you answered>
      prompt: PROMPT-chatgpt-e351.md in this folder
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
