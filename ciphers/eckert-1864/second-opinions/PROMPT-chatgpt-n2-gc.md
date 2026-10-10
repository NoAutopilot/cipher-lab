SECOND OPINION REQUEST, label SO-ECKERT-N2-GC

We are an open cipher-research repository (github.com/NoAutopilot/cipher-lab). We have read one American Civil War-era
cipher telegram and want you to try to prove that its text was already printed before us, and to find mistakes in our
reading. Be adversarial: we would rather learn now that it is in print than claim it wrongly later.

THE ITEM
- Source: Thomas T. Eckert Papers, Huntington Library, San Marino, mssEC 18 (War Department telegraph office, ciphers sent) p.247 (digital pointer 9913), the first entry on the page, N2-GC, headed "R. R. McCaine  Washn Decr 10th 1864", https://hdl.huntington.org/digital/collection/p16003coll11/id/9913. Read with War Department Cipher No. 2.
- Reading: "[12 noon] [10] [Sheridan P H] [.] Pay masters ready togoto for pay ment of your [troops] unpaid to [August] [31] [.] Under the [Secretary of War]'s [order] of [December] [2] I mustache [unread code word] you for safe [guard] from Relay house [.] Please have me notified by [telegram] in [cipher] whenny [when] Pay masters maybe sent to Relay house [signed] B W Brice". Bracketed words are code words read from the period key; the rest is clear on the page.
- Context we already know: the same order of 2 December 1864 is cited in Brice's telegram to Meade of 14 Dec 1864 (our N2-GI, pointer 9914: "In compliance with the Secretary's order of the 2nd inst."); Brice was Acting Paymaster General (Army and Navy Official Gazette 1865, under 6 Dec 1864).
- Our files: reading https://raw.githubusercontent.com/NoAutopilot/cipher-lab/main/ciphers/eckert-1864/reading-no2.md,
  key https://raw.githubusercontent.com/NoAutopilot/cipher-lab/main/ciphers/eckert-1864/key-no2.md, search log
  https://raw.githubusercontent.com/NoAutopilot/cipher-lab/main/ciphers/eckert-1864/AUDIT.md (section "AUDIT (FV-N2c)"; its section 5 lists corrections not yet applied to the reading file).

WHERE WE HAVE LOOKED: Official Records ser. I vols 43 pt 2 and 45 pt 2 (9-11 Dec 1864 by text and dated headings; "Relay House"); Papers of U. S. Grant vol. 13 (full-text search); Google Books phrase search; Chronicling America (8-20 Dec 1864, hits not read page by page); the Huntington's CONTENTdm full-text search.

WHERE WE HAVE NOT YET LOOKED PROPERLY (start here)
- the Secretary of War's order of 2 Dec 1864 on paying troops (War Department general or special orders, Dec 1864); NARA RG 99 (Paymaster General) and RG 107; Sheridan's papers; Official Records ser. III vols 4-5 and the Paymaster General's 1865 report; the Washington and Baltimore press of 10-20 Dec 1864; HathiTrust; JSTOR.

HOW TO REPORT (this part is the same for every label)
- Write your answer as one Markdown file in the repository github.com/NoAutopilot/cipher-lab at the path
  `ciphers/eckert-1864/second-opinions/chatgpt-n2-gc-<UTC date>.md`. Do not touch any other file. Do not commit to `main`:
  create a branch named `second-opinion/SO-ECKERT-N2-GC` and open a pull request from it, titled exactly
  `[SO-ECKERT-N2-GC] second opinion: Brice to Sheridan: paymasters ready for troops unpaid since 31 August, to be sent to Relay House on word in cipher, 10 Dec 1864`.
- The first lines of the file must be this header, filled in:
      label: SO-ECKERT-N2-GC
      model: <your model name and version>
      date: <UTC date you answered>
      prompt: PROMPT-chatgpt-n2-gc.md in this folder
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
