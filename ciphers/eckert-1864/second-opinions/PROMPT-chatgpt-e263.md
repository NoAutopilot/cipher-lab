SECOND OPINION REQUEST, label SO-ECKERT-E263

We are an open cipher-research repository (github.com/NoAutopilot/cipher-lab). We have read one American Civil War
cipher telegram and want you to try to prove that its text was already printed before us, and to find mistakes in our
reading. Be adversarial: we would rather learn now that it is in print than claim it wrongly later.

THE ITEM
- Source: Thomas T. Eckert Papers, Huntington Library, San Marino, mssEC 25 ("Ciphers Received and Sent", Fort Monroe) p.268 (digital pointer 5812), first entry on the page, E263, headed "Ft. Monroe Nov 29 1864 / Cipher Agent City Point", https://hdl.huntington.org/digital/collection/p16003coll11/id/5812. Read with War Department Cipher No. 1 (Huntington mssEC 41).
- Reading: Fort Monroe (Sheldon is the operator) to the Cipher Agent, City Point, 29 Nov 1864 [3.30 PM]: "For [Captain] William T. Howell, [Lieutenant General Grant]'s [headquarters], [City Point]. Tell [Colonel] Bradley to send all empty [steam]ers to [Washington] to bring down [troops]. Let them be sent as fast as they arrive and become [light]. See that estimates are prepared of material still required for buildings already in process of erection. [Signed] Rufus Ingalls, [Brigadier General], Chief [Quartermaster]." Bracketed words are code words read from the period key.
- Context we already know: Lt. Col. George W. Bradley was made depot quartermaster at City Point under Ingalls by Special Orders No. 120, City Point, 5 Nov 1864 (Official Records ser. I vol. 42 pt 3); Grant to Halleck, 28 Nov 1864, on sending the Sixth Corps infantry first. The next ledger entry the same day is Ingalls to Eckert for the Quartermaster General on steamers sent to Washington; its clear text is printed in Official Records ser. I vol. 42 pt 3 p. 739 (Ingalls to Meigs, Fortress Monroe, 29 Nov 1864 4 p.m.: "I have directed all steamers to be sent to Washington to be in readiness to bring back the Sixth Corps ..."). That is a different telegram from this one; we want to know whether THIS one (to Howell, for Col. Bradley, empty steamers, building estimates) is printed anywhere.
- Our files: reading https://raw.githubusercontent.com/NoAutopilot/cipher-lab/main/ciphers/eckert-1864/reading.md,
  key https://raw.githubusercontent.com/NoAutopilot/cipher-lab/main/ciphers/eckert-1864/key.md, search log
  https://raw.githubusercontent.com/NoAutopilot/cipher-lab/main/ciphers/eckert-1864/AUDIT.md (sections "AUDIT (FV-FM7b)" and "AUDIT 2 (AUD2-LEDGER-16)").

WHERE WE HAVE LOOKED: Official Records ser. I vols. 42 pt 3 (by phrase, and every letter of 28-30 Nov 1864) and 43 pt 2 (full text, by phrase); Grant Papers vols. 10-12 (snippet search); Butler's Private and Official Correspondence vols. IV-V; the Huntington's CONTENTdm full-text search.

WHERE WE HAVE NOT YET LOOKED PROPERLY (start here)
- Grant Papers vol. 13 (Nov 1864-Feb 1865); Quartermaster General's records (RG 92); Google Books; HathiTrust; JSTOR.


HOW TO REPORT (this part is the same for every label)
- Write your answer as one Markdown file in the repository github.com/NoAutopilot/cipher-lab at the path
  `ciphers/eckert-1864/second-opinions/chatgpt-e263-<UTC date>.md`. Do not touch any other file. Do not commit to `main`:
  create a branch named `second-opinion/SO-ECKERT-E263` and open a pull request from it, titled exactly
  `[SO-ECKERT-E263] second opinion: Ingalls to Capt. W. T. Howell: all empty steamers to Washington for troops, 29 Nov 1864`.
- The first lines of the file must be this header, filled in:
      label: SO-ECKERT-E263
      model: <your model name and version>
      date: <UTC date you answered>
      prompt: PROMPT-chatgpt-e263.md in this folder
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
