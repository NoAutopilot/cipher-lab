SECOND OPINION REQUEST, label SO-ECKERT-N2-GA

We are an open cipher-research repository (github.com/NoAutopilot/cipher-lab). We have read one American Civil War-era
cipher telegram and want you to try to prove that its text was already printed before us, and to find mistakes in our
reading. Be adversarial: we would rather learn now that it is in print than claim it wrongly later.

THE ITEM
- Source: Thomas T. Eckert Papers, Huntington Library, San Marino, mssEC 18 (War Department telegraph office, ciphers sent) p.208 (digital pointer 9874), the second entry on the page (the ledger writes "No 2" above the page number), N2-GA, headed "RR McCaine  Wash'n Oct 22nd 64", https://hdl.huntington.org/digital/collection/p16003coll11/id/9874. Read with War Department Cipher No. 2.
- Reading: "[Washington] [October] [22] [11 AM] for [Colonel] J. W. Forsyth Chief of [Staff] [.] Pay mast hers [paymasters] will leave here [Monday] morning [24] inst with funds for pay ment [of the] [19] [Army] [Corps] and others [.] Please have sufficient east court [escort] at [Martinsburg] for their protection [signed] B W Brin [Brice] Acting Pray mestn [Paymaster] [General]". Bracketed words are code words read from the period key; the rest is clear on the page.
- Context we already know: Huntington pointer 9100 (mssEC 19 p.206), the same day 11.30 AM, Brice to Gen. Stevenson at Harpers Ferry in clear: paymasters with funds leave Monday morning for Sheridan's army, escort to Martinsburg; Official Records ser. I vol. 43 pt 2 pp.370-373 (14 Oct 1864: paymasters Moore and Ruggles captured with their funds on the B&O) and pp.471-472 (26 Oct 1864: a paymaster sent from Martinsburg with a strong escort).
- Our files: reading https://raw.githubusercontent.com/NoAutopilot/cipher-lab/main/ciphers/eckert-1864/reading-no2.md,
  key https://raw.githubusercontent.com/NoAutopilot/cipher-lab/main/ciphers/eckert-1864/key-no2.md, search log
  https://raw.githubusercontent.com/NoAutopilot/cipher-lab/main/ciphers/eckert-1864/AUDIT.md (section "AUDIT (FV-N2c)"; its section 5 lists corrections not yet applied to the reading file).

WHERE WE HAVE LOOKED: Official Records ser. I vol. 43 pt 2 (21-23 Oct 1864 by text and dated headings); Papers of U. S. Grant vol. 12 (full-text search); Google Books phrase search; Chronicling America (20-31 Oct 1864, hits not read page by page); the Huntington's CONTENTdm full-text search.

WHERE WE HAVE NOT YET LOOKED PROPERLY (start here)
- NARA RG 99 (Paymaster General, letters and telegrams sent) and RG 107; Sheridan's papers (Library of Congress); Official Records ser. III vols 4-5 and the Paymaster General's annual report of 1865; Mosby "Greenback Raid" literature; the Washington and Baltimore press of 22-28 Oct 1864; HathiTrust; JSTOR.

HOW TO REPORT (this part is the same for every label)
- Write your answer as one Markdown file in the repository github.com/NoAutopilot/cipher-lab at the path
  `ciphers/eckert-1864/second-opinions/chatgpt-n2-ga-<UTC date>.md`. Do not touch any other file. Do not commit to `main`:
  create a branch named `second-opinion/SO-ECKERT-N2-GA` and open a pull request from it, titled exactly
  `[SO-ECKERT-N2-GA] second opinion: Brice to Sheridan's chief of staff Forsyth: paymasters leave Monday the 24th for the 19th Corps, escort wanted at Martinsburg, 22 Oct 1864`.
- The first lines of the file must be this header, filled in:
      label: SO-ECKERT-N2-GA
      model: <your model name and version>
      date: <UTC date you answered>
      prompt: PROMPT-chatgpt-n2-ga.md in this folder
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
