SECOND OPINION REQUEST, label SO-ECKERT-E594

We are an open cipher-research repository (github.com/NoAutopilot/cipher-lab). We have read one American Civil War
cipher telegram and want you to try to prove that its text was already printed before us, and to find mistakes in our
reading. Be adversarial: we would rather learn now that it is in print than claim it wrongly later.

THE ITEM
- Source: Thomas T. Eckert Papers, Huntington Library, San Marino, mssEC 25 ("Ciphers Received and Sent", Fort Monroe) p.397 (digital pointer 5941), headed "Ft Monroe Mar 27 / 65 / Maj. Eckert, Washington", sent 1.40 PM, E594, https://hdl.huntington.org/digital/collection/p16003coll11/id/5941. Read with War Department Cipher No. 1 (Huntington mssEC 41).
- Reading (code words in brackets, as corrected by our verifier, AUDIT (FV-L17b) s.4): "[Monroe] to Honorable John Shear man [= Sherman] [Washington] I am going tussey [= to see] [Maj Genl U.S. Grant] at [City Point] and expect toggo [= to go] back to [Goldsboro] [By the way of] [Newbern] from Old [Point] on Wednesday [Maj Gen W. T. Sherman] sent 1.40 PM Dealy Geo. D. Sheldon"
- Context we already know: Official Records ser. I vol. 47 pt 3 pp.32-33 print Sherman's two other telegrams from Old Point that day (to Grant: "All well at Goldsborough. I am coming up to see you ..."; to Stanton: "I am en route for City Point to see General Grant ...") and Stanton's 6.55 p.m. reply "Your brother, Senator Sherman, will start at 8 o'clock this evening to meet you at City Point"; The Papers of Ulysses S. Grant vol. 14 prints the telegram to Grant. None of these is this telegram to John Sherman.
- Our files: reading https://raw.githubusercontent.com/NoAutopilot/cipher-lab/main/ciphers/eckert-1864/reading.md,
  key https://raw.githubusercontent.com/NoAutopilot/cipher-lab/main/ciphers/eckert-1864/key.md, search log
  https://raw.githubusercontent.com/NoAutopilot/cipher-lab/main/ciphers/eckert-1864/AUDIT.md (section "AUDIT (FV-L17b)").

WHERE WE HAVE LOOKED: Official Records ser. I vols. 46 pts 1-3 and 47 pts 1-3 and ORN ser. I vols. 11-12 (full text, by phrase and by name); Butler's Private and Official Correspondence vols. IV-V; J. E. O'Brien, Telegraphing in Battle (1910); Plum, The Military Telegraph vol. II; the Huntington's CONTENTdm full-text search across the whole Eckert collection (fresh words, 10 Oct 2026); Internet Archive full-text search, whole collection and The Papers of Ulysses S. Grant vol. 14; The Sherman Letters (1894, correspondence between General and Senator Sherman).

WHERE WE HAVE NOT YET LOOKED PROPERLY (start here)
- John Sherman's Recollections of Forty Years (1895) vol. 1, the chapter on 1865; Sherman's Memoirs (1875, 1886), the March 1865 chapter; The Papers of Ulysses S. Grant vol. 14 page by page; NARA RG 107 telegrams received; newspapers of 28-31 March 1865; HathiTrust; JSTOR.

HOW TO REPORT (this part is the same for every label)
- Write your answer as one Markdown file in the repository github.com/NoAutopilot/cipher-lab at the path
  `ciphers/eckert-1864/second-opinions/chatgpt-e594-<UTC date>.md`. Do not touch any other file. Do not commit to `main`:
  create a branch named `second-opinion/SO-ECKERT-E594` and open a pull request from it, titled exactly
  `[SO-ECKERT-E594] second opinion: Sherman tells his brother he is going to see Grant at City Point and will return to Goldsboro from Old Point on Wednesday, 27 Mar 1865`.
- The first lines of the file must be this header, filled in:
      label: SO-ECKERT-E594
      model: <your model name and version>
      date: <UTC date you answered>
      prompt: PROMPT-chatgpt-e594.md in this folder
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
