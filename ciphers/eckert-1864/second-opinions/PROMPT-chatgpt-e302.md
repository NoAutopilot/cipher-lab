SECOND OPINION REQUEST, label SO-ECKERT-E302

We are an open cipher-research repository (github.com/NoAutopilot/cipher-lab). We have read one American Civil War
cipher telegram and want you to try to prove that its text was already printed before us, and to find mistakes in our
reading. Be adversarial: we would rather learn now that it is in print than claim it wrongly later.

THE ITEM
- Source: Thomas T. Eckert Papers, Huntington Library, San Marino, mssEC 25 ("Ciphers Received and Sent", Fort Monroe) p.153 (digital pointer 5697), second entry on the page, E302, headed "Ft. Monroe May 27 1864 / Maj Eckert Di", signed Geo. D. Sheldon, https://hdl.huntington.org/digital/collection/p16003coll11/id/5697. Read with War Department Cipher No. 1 (Huntington mssEC 41).
- Reading: "If White House is made the base of supplies [West Point] will also be made a [depot] and an office there will be a great convenience. The old line was all [destroyed] last year, a new line must be built. If it is extended from [Williamsburg] up the Peninsula either to White House direct or [via] [West Point], the whole line [of the] Chickahominy must be [guarded] to protect it from raiders. Why not [cross] at [Yorktown] to Glow sister [Point] (Gloucester Point) thence by a direct [road] to the Mattie pony (Mattapony) and [cross] to [West Point]? Distance from G. [Point] to the Mattapony about [30] [miles], [road] is good and direct, from [West Point] to White House on [railroad] [12] [miles]. I think most [of the] [poles] on the [railroad] are standing, they are fine large chestnut poles and have not rotted down. The distance [via] G. [Point] is very little more than from [Williamsburg] up peninsula and by [Grant]'s [position] the route must be pretty secure, office at G. [Point] will also be convenience. Have asked O'Brien about material, think he must have considerable, I have very little wire on hand now. Geo D Sheldon." Bracketed words are code words read from the period key; "[poles]" is a word the writer left out; "Glow sister" and "Mattie pony" are the clerk's spellings.
- Context we already know: the question it answers is in clear on the page before (pointer 5696). Official Records ser. I vol. 36 pt 3 prints Eckert to R. O'Brien, 27 May 1864 ("Confer with Sheldon as to plans and route", p.262), Butler to Sheldon, 28 May ("across the York at Gloucester Point, thence up to West Point, thence across the Mattapony", p.262), and Sheldon to Butler and to Eckert, 28 May (pp.280-281).
- Our files: reading https://raw.githubusercontent.com/NoAutopilot/cipher-lab/main/ciphers/eckert-1864/reading.md,
  key https://raw.githubusercontent.com/NoAutopilot/cipher-lab/main/ciphers/eckert-1864/key.md, search log
  https://raw.githubusercontent.com/NoAutopilot/cipher-lab/main/ciphers/eckert-1864/AUDIT.md (section "AUDIT (FV-FM9b)").

WHERE WE HAVE LOOKED: Official Records ser. I vol. 36 pts 2-3 (full text, by phrase and name); OR ser. I vol. 33 and ORN vols. 9-10 by phrase; Papers of Ulysses S. Grant vol. 11 (Internet Archive full-text snippets only); Butler's Private and Official Correspondence vol. IV; the Huntington's CONTENTdm full-text search across the whole Eckert collection.

WHERE WE HAVE NOT YET LOOKED PROPERLY (start here)
- Records of the U.S. Military Telegraph (NARA RG 107, RG 92); W. R. Plum, The Military Telegraph during the Civil War (1882), on the York River / Gloucester Point line of May-June 1864; Papers of U. S. Grant vol. 11 page by page; Google Books; HathiTrust; JSTOR.

HOW TO REPORT (this part is the same for every label)
- Write your answer as one Markdown file in the repository github.com/NoAutopilot/cipher-lab at the path
  `ciphers/eckert-1864/second-opinions/chatgpt-e302-<UTC date>.md`. Do not touch any other file. Do not commit to `main`:
  create a branch named `second-opinion/SO-ECKERT-E302` and open a pull request from it, titled exactly
  `[SO-ECKERT-E302] second opinion: Sheldon to Eckert: a telegraph line to White House by Gloucester Point, 27 May 1864`.
- The first lines of the file must be this header, filled in:
      label: SO-ECKERT-E302
      model: <your model name and version>
      date: <UTC date you answered>
      prompt: PROMPT-chatgpt-e302.md in this folder
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
