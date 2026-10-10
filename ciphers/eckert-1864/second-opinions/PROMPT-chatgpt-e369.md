SECOND OPINION REQUEST, label SO-ECKERT-E369

We are an open cipher-research repository (github.com/NoAutopilot/cipher-lab). We have read one American Civil War-era
cipher telegram and want you to try to prove that its text was already printed before us, and to find mistakes in our
reading. Be adversarial: we would rather learn now that it is in print than claim it wrongly later.

THE ITEM
- Source: Thomas T. Eckert Papers, Huntington Library, San Marino, mssEC 18 (War Department telegraph office, ciphers sent) p.354 (digital pointer 10020), the second entry on the page, E369, headed "H. F. Lines, No 1, Macon / Wash'n May 24th 1865", https://hdl.huntington.org/digital/collection/p16003coll11/id/10020. Read with War Department Cipher No. 1 (Huntington mssEC 41).
- Reading: "[Washington] [20] [14 -- read 24, see below] May [8.30 PM]. Officer [Command]ing [Augusta]. You will imm'y [arrest] Thomas J. [Camp]bell[,] who was confess skating [confiscating] officer for the [Rebel] [Government] at [Knoxville] [Tennessee][,] and send him under [guard] to [Nashville] to be delivered to [Major] [General] [Thomas]. [signed] [Secretary of War]. Forward by [rail road]". Bracketed words are code words read from the period key; the rest is clear on the page. The day words give 34; the header and the request below both say 24 May (we read a clerk's slip). "Chant" on the page is the key word Chart = Knoxville.
- Context we already know: the Huntington's received ledger (pointer 8756) holds Thomas's request in clear, Nashville 24 May 1865, 1 P.M., to the Secretary of War: "request that the Comdg officer at Augusta Ga be directed to arrest Thomas J. Campbell who was confiscating officer for the Rebel Government at Knoxville Tennessee ... send him to Nashville under guard". Civil War History (1963) mentions a Knoxville property sale by "Receiver T. J. Campbell" under the Confederate District Court; The Papers of Andrew Johnson identify a Thomas J. Campbell (1824-1885), McMinn County banker (snippets only).
- Our files: reading https://raw.githubusercontent.com/NoAutopilot/cipher-lab/main/ciphers/eckert-1864/reading.md,
  key https://raw.githubusercontent.com/NoAutopilot/cipher-lab/main/ciphers/eckert-1864/key.md, search log
  https://raw.githubusercontent.com/NoAutopilot/cipher-lab/main/ciphers/eckert-1864/AUDIT.md (section "AUDIT (FV-MS18l)").

WHERE WE HAVE LOOKED: Official Records ser. I vol. 49 pt 2 (24 May 1865 items, pp.888-906; pp.889 and 891 on page images; index), ser. II vol. 8 (index), 164 cached edition texts; Google Books (API); Internet Archive full-text search; the Huntington's CONTENTdm full-text search.

WHERE WE HAVE NOT YET LOOKED PROPERLY (start here)
- Thomas's and J. H. Wilson's papers and letter books; the Augusta and Knoxville press of May-June 1865; Confederate sequestration in East Tennessee (Campbell as receiver); The Papers of Andrew Johnson at the Campbell note; HathiTrust; JSTOR.

HOW TO REPORT (this part is the same for every label)
- Write your answer as one Markdown file in the repository github.com/NoAutopilot/cipher-lab at the path
  `ciphers/eckert-1864/second-opinions/chatgpt-e369-<UTC date>.md`. Do not touch any other file. Do not commit to `main`:
  create a branch named `second-opinion/SO-ECKERT-E369` and open a pull request from it, titled exactly
  `[SO-ECKERT-E369] second opinion: Secretary of War to the commander at Augusta: arrest Thomas J. Campbell, 24 May 1865`.
- The first lines of the file must be this header, filled in:
      label: SO-ECKERT-E369
      model: <your model name and version>
      date: <UTC date you answered>
      prompt: PROMPT-chatgpt-e369.md in this folder
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
