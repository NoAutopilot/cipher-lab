SECOND OPINION REQUEST, label SO-ECKERT-E321

We are an open cipher-research repository (github.com/NoAutopilot/cipher-lab). We have read one American Civil War
cipher telegram and want you to try to prove that its text was already printed before us, and to find mistakes in our
reading. Be adversarial: we would rather learn now that it is in print than claim it wrongly later.

THE ITEM
- Source: Thomas T. Eckert Papers, Huntington Library, San Marino, mssEC 25 ("Ciphers Received and Sent", Fort Monroe) p.238 (digital pointer 5782), first entry on the page, E321, headed "Head Qrs A. P. Sept 1/64 / Maj. Eckert Di - Sheldon F", signed Caldwell, https://hdl.huntington.org/digital/collection/p16003coll11/id/5782. Read with War Department Cipher No. 1 (Huntington mssEC 41). The same telegram is in the ledger a second time in its transposed (wire) order at the foot of p.237 (pointer 5781), and a received copy is at pointer 12319 (https://hdl.huntington.org/digital/collection/p16003coll11/id/12319).
- Reading: "I think cable should be laid on [north] side of [river] as it will take less cable and will be less danger of being dragged up by anchors and channel most of way is nearest [south] shore. D. Doren. Caldwell" Bracketed words are code words read from the period key; "cab bell" (cable) and "D do wren" (D. Doren) are the clerk's phonetic spellings. The telegram does not name the river; we have not supplied one.
- Context we already know: Plum, The Military Telegraph during the Civil War (1882) vol. II names A. H. Caldwell chief operator at Meade's headquarters and D. Doren superintendent of construction. We found no printed context for this cable. The telegram's text ends "D do wren" (D. Doren) and Caldwell's name stands below it; we have not established that Caldwell sent it, so read the sender as Army of the Potomac headquarters.
- Our files: reading https://raw.githubusercontent.com/NoAutopilot/cipher-lab/main/ciphers/eckert-1864/reading.md,
  key https://raw.githubusercontent.com/NoAutopilot/cipher-lab/main/ciphers/eckert-1864/key.md, search log
  https://raw.githubusercontent.com/NoAutopilot/cipher-lab/main/ciphers/eckert-1864/AUDIT.md (section "AUDIT (FV-FM10b)").

WHERE WE HAVE LOOKED: Official Records ser. I vol. 42 pt 2 (full text, by phrase and name), OR ser. I vols. 33, 36, 40, 43 and ORN by phrase; Plum, Military Telegraph I-II; Bates, Lincoln in the Telegraph Office; Papers of U. S. Grant vol. 12 (Internet Archive full-text snippets only); the Huntington's CONTENTdm full-text search across the whole Eckert collection.

WHERE WE HAVE NOT YET LOOKED PROPERLY (start here)
- Which river and which cable (James, Appomattox or another crossing near Petersburg, Aug-Sept 1864); Papers of U. S. Grant vol. 12 page by page; NARA RG 107 records; histories of the U. S. Military Telegraph Corps; Google Books; HathiTrust; JSTOR.

HOW TO REPORT (this part is the same for every label)
- Write your answer as one Markdown file in the repository github.com/NoAutopilot/cipher-lab at the path
  `ciphers/eckert-1864/second-opinions/chatgpt-e321-<UTC date>.md`. Do not touch any other file. Do not commit to `main`:
  create a branch named `second-opinion/SO-ECKERT-E321` and open a pull request from it, titled exactly
  `[SO-ECKERT-E321] second opinion: Head Qrs Army of the Potomac (signed Caldwell), to Maj. Eckert: lay the cable on the north side, 1 Sept 1864`.
- The first lines of the file must be this header, filled in:
      label: SO-ECKERT-E321
      model: <your model name and version>
      date: <UTC date you answered>
      prompt: PROMPT-chatgpt-e321.md in this folder
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
