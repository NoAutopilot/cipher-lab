SECOND OPINION REQUEST, label SO-ECKERT-N2-GF

We are an open cipher-research repository (github.com/NoAutopilot/cipher-lab). We have read one American Civil War-era
cipher telegram and want you to try to prove that its text was already printed before us, and to find mistakes in our
reading. Be adversarial: we would rather learn now that it is in print than claim it wrongly later.

THE ITEM
- Source: Thomas T. Eckert Papers, Huntington Library, San Marino, mssEC 18 (War Department telegraph office, ciphers sent) p.56 (digital pointer 9722), the second entry on the page, N2-GF, headed "Caldwell (no 2) / Hd Qrs A P / Wash. Apl 25 1864", https://hdl.huntington.org/digital/collection/p16003coll11/id/9722. Read with War Department Cipher No. 2.
- Reading: "[Meade] Moseby is collecting corn [horse]s &c [in the(?)] vicinity of Upperville Can you send a [regiment] of [cavalry] from Warrenton to meet a [command] I will send on [Wednesday] or [Thursday] next to break up this business & to take & [destroy] the supplies collected [?] [Augur] [3 PM]". Bracketed words are code words read from the period key; the rest is clear on the page.
- Context we already know: Meade's reply of the same day, 4 PM (Huntington pointer 4569): the regiment of cavalry can be sent but he would prefer not; Official Records ser. I vol. 33 p.985 (Tyler, 26 Apr: can start 'on Thursday as proposed') and p.315 (Lowell's scout toward Upperville, 28 Apr-1 May 1864).
- Our files: reading https://raw.githubusercontent.com/NoAutopilot/cipher-lab/main/ciphers/eckert-1864/reading-no2.md,
  key https://raw.githubusercontent.com/NoAutopilot/cipher-lab/main/ciphers/eckert-1864/key-no2.md, search log
  https://raw.githubusercontent.com/NoAutopilot/cipher-lab/main/ciphers/eckert-1864/AUDIT.md (section "AUDIT (FV-N2b)").

WHERE WE HAVE LOOKED: Official Records ser. I vols 32 pt 3 and 33 (24-26 Apr 1864); Papers of U. S. Grant vol. 10 (full-text search); Google Books phrase search; the Huntington's CONTENTdm full-text search.

WHERE WE HAVE NOT YET LOOKED PROPERLY (start here)
- Meade's and Augur's papers; histories of Mosby's command and of the 2nd Massachusetts Cavalry (Lowell); NARA RG 393 (Department of Washington, Army of the Potomac); the Washington press of 25 Apr-3 May 1864; HathiTrust; JSTOR.

HOW TO REPORT (this part is the same for every label)
- Write your answer as one Markdown file in the repository github.com/NoAutopilot/cipher-lab at the path
  `ciphers/eckert-1864/second-opinions/chatgpt-n2-gf-<UTC date>.md`. Do not touch any other file. Do not commit to `main`:
  create a branch named `second-opinion/SO-ECKERT-N2-GF` and open a pull request from it, titled exactly
  `[SO-ECKERT-N2-GF] second opinion: Augur to Meade: Mosby collecting corn and horses near Upperville, 25 Apr 1864`.
- The first lines of the file must be this header, filled in:
      label: SO-ECKERT-N2-GF
      model: <your model name and version>
      date: <UTC date you answered>
      prompt: PROMPT-chatgpt-n2-gf.md in this folder
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
