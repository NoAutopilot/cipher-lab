SECOND OPINION REQUEST, label SO-ECKERT-E283

We are an open cipher-research repository (github.com/NoAutopilot/cipher-lab). We have read one American Civil War
cipher telegram and want you to try to prove that its text was already printed before us, and to find mistakes in our
reading. Be adversarial: we would rather learn now that it is in print than claim it wrongly later.

THE ITEM
- Source: Thomas T. Eckert Papers, Huntington Library, San Marino, mssEC 25 ("Ciphers Received and Sent", Fort Monroe) p.275 (digital pointer 5819), second entry on the page, E283, headed "Ft Monroe Dec 7 1864 / R OBrien HdQrs a of J", https://hdl.huntington.org/digital/collection/p16003coll11/id/5819. Read with War Department Cipher No. 1 (Huntington mssEC 41).
- Reading: Rear-Admiral D. D. Porter, Portsmouth [Gosport Navy Yard], via Fort Monroe and R. O'Brien at Butler's headquarters, to Commander W. A. Parker, U.S.S. Onondaga, Dutch [Gap], [James] River, 7 Dec 1864 {6 PM}: "Send at once [2] [gunboats] down to White Shoal [light] house, and to cruise between there and [Point] of Shoals night and day until further orders, and keep a good look out for [rebel] boats; they will not permit vessels to anchor [near] shore, and when they are obliged to do so will tow them off. [Capture] all boats found [in the] [river] by night or day and hold the persons in them as prisoners. Keep a good watch, ready for any [surprise], [steam] up and chain ready to slip [?]. Give [convoy] to vessels. [Signed] [D. D. Porter]." Bracketed words are code words read from the period key; braces are time words.
- Context we already know: Porter's written instructions to Parker of the same day (Official Records of the Union and Confederate Navies ser. I vol. 11 pp.153-154, Gosport Navy Yard, 7 Dec 1864) say "I telegraphed you to send two vessels there at once" and order care of the White Shoal and Point of Shoals light-houses; Parker's report of 11 Dec (p.188) found the Hunchback and Daylight "cruising between White Shoal light-house and Point of Shoals, as you had directed in a former telegram". Neither prints the telegram itself. We want to know whether its text is printed anywhere.
- Our files: reading https://raw.githubusercontent.com/NoAutopilot/cipher-lab/main/ciphers/eckert-1864/reading.md,
  key https://raw.githubusercontent.com/NoAutopilot/cipher-lab/main/ciphers/eckert-1864/key.md, search log
  https://raw.githubusercontent.com/NoAutopilot/cipher-lab/main/ciphers/eckert-1864/AUDIT.md (sections "AUDIT (FV-FM8b)" and "AUDIT 2 (AUD2-LEDGER-19)").

WHERE WE HAVE LOOKED: ORN ser. I vols. 9-11 (by phrase, and the 7-11 Dec pages of vol. 11); Official Records ser. I vol. 42 pt 3; Butler's Private and Official Correspondence vol. V; the Huntington's CONTENTdm full-text search.

WHERE WE HAVE NOT YET LOOKED PROPERLY (start here)
- Porter's letter-books and papers (Library of Congress); the Onondaga's log; Google Books; HathiTrust; JSTOR.


HOW TO REPORT (this part is the same for every label)
- Write your answer as one Markdown file in the repository github.com/NoAutopilot/cipher-lab at the path
  `ciphers/eckert-1864/second-opinions/chatgpt-e283-<UTC date>.md`. Do not touch any other file. Do not commit to `main`:
  create a branch named `second-opinion/SO-ECKERT-E283` and open a pull request from it, titled exactly
  `[SO-ECKERT-E283] second opinion: Porter to Commander Parker: two gunboats between White Shoal light and Point of Shoals, 7 Dec 1864`.
- The first lines of the file must be this header, filled in:
      label: SO-ECKERT-E283
      model: <your model name and version>
      date: <UTC date you answered>
      prompt: PROMPT-chatgpt-e283.md in this folder
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
