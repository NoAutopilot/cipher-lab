SECOND OPINION REQUEST, label SO-ECKERT-N2BY

We are an open cipher-research repository (github.com/NoAutopilot/cipher-lab). We have read one American Civil War
cipher telegram and want you to try to prove that its text was already printed before us, and to find mistakes in our
reading. Be adversarial: we would rather learn now that it is in print than claim it wrongly later.

THE ITEM
- Source: Thomas T. Eckert's telegraph ledgers, Huntington Library, San Marino, mssEC 19 p.234 (digital pointer 9126), https://hdl.huntington.org/digital/collection/p16003coll11/id/9126, entry N2-BY, headed "A. H. Caldwell Mc  Wash'n Nov. 22nd 1864". Read with War Department Cipher No. 2 (key in our file key-no2.md, from mssEC 47 in the same collection).
- Ciphertext as written: "Hang Nancy Oliver Arnold to Palermo Rawl = lins / I will not beat Bridle until Yankee crowd".
- Reading: Washington, 8 PM, 22 [November 1864], to Brig. General Rawlins: I will not be at City Point until Thursday. [signed] Lieut. Gen. U. S. Grant.
- Context we already know: OR ser. I vol. 42 pt 3 prints Grant at Burlington, N. J., to Stanton, 18 Nov 1864, 8.30 p.m.: "I will be in Washington Tuesday morning. Will go to New York with my family and remain until Monday." The plain words of the entry (not the code words) are in the Huntington's own public transcription.
- Our files: reading https://raw.githubusercontent.com/NoAutopilot/cipher-lab/main/ciphers/eckert-1864/reading-no2.md,
  key https://raw.githubusercontent.com/NoAutopilot/cipher-lab/main/ciphers/eckert-1864/key-no2.md, search log
  https://raw.githubusercontent.com/NoAutopilot/cipher-lab/main/ciphers/eckert-1864/AUDIT.md (section "AUDIT (LS4-V2a)").

WHERE WE HAVE LOOKED: OR ser. I vol. 42 pt 3; Internet Archive full text (The Papers of Ulysses S. Grant vol. 13 is not on Internet Archive); Google Books (snippet search, which does reach Papers of U. S. Grant vol. 13); OpenAlex; the Huntington's own full-text search.

WHERE WE HAVE NOT YET LOOKED PROPERLY (start here)
- The Papers of Ulysses S. Grant, vol. 13 (Simon ed., 1985), pages for 18-24 Nov 1864 and their notes; the 1864 press of 22-26 Nov; NARA RG 107 (telegrams collected); HathiTrust full text and JSTOR.

HOW TO REPORT (this part is the same for every label)
- Write your answer as one Markdown file in the repository github.com/NoAutopilot/cipher-lab at the path
  `ciphers/eckert-1864/second-opinions/chatgpt-n2by-<UTC date>.md`. Do not touch any other file. Do not commit to `main`:
  create a branch named `second-opinion/SO-ECKERT-N2BY` and open a pull request from it, titled exactly
  `[SO-ECKERT-N2BY] second opinion: Grant to Rawlins, not at City Point until Thursday, 22 November 1864`.
- The first lines of the file must be this header, filled in:
      label: SO-ECKERT-N2BY
      model: <your model name and version>
      date: <UTC date you answered>
      prompt: PROMPT-chatgpt-n2by.md in this folder
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
