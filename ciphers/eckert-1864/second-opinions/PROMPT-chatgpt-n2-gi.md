SECOND OPINION REQUEST, label SO-ECKERT-N2-GI

We are an open cipher-research repository (github.com/NoAutopilot/cipher-lab). We have read one American Civil War-era
cipher telegram and want you to try to prove that its text was already printed before us, and to find mistakes in our
reading. Be adversarial: we would rather learn now that it is in print than claim it wrongly later.

THE ITEM
- Source: Thomas T. Eckert Papers, Huntington Library, San Marino, mssEC 18 (War Department telegraph office, ciphers sent) p.248 (digital pointer 9914), the second entry on the page, labelled "No 2" and "3 Pm" above its header, N2-GI, headed "Caldwell Hdqrs AP  Wash DC Dec 14 1864", https://hdl.huntington.org/digital/collection/p16003coll11/id/9914. Read with War Department Cipher No. 2.
- Reading: "[Wednesday] [3 PM] [Meade G G] ---- In compliance with the Secys order of [2] inst I inform you that [2] Paymrs will leave [tomorrow] by [river] for [City Point] for the payment of [2] [regiment]s of [6] [Corps] unpaid to [31] of Aug [signed] B W Brice". Bracketed words are code words read from the period key; the rest is clear on the page.
- Context we already know: the same order of 2 December 1864 is cited in Brice's telegram to Sheridan of 10 Dec 1864 (our N2-GC, pointer 9913); the Sixth Corps returned from the Shenandoah Valley to Petersburg in early December 1864.
- Our files: reading https://raw.githubusercontent.com/NoAutopilot/cipher-lab/main/ciphers/eckert-1864/reading-no2.md,
  key https://raw.githubusercontent.com/NoAutopilot/cipher-lab/main/ciphers/eckert-1864/key-no2.md, search log
  https://raw.githubusercontent.com/NoAutopilot/cipher-lab/main/ciphers/eckert-1864/AUDIT.md (section "AUDIT (FV-N2c)"; its section 5 lists corrections not yet applied to the reading file).

WHERE WE HAVE LOOKED: Official Records ser. I vol. 42 pt 3 (13-15 Dec 1864; "paymaster", "Brice"); Papers of U. S. Grant vol. 13 (full-text search); Google Books phrase search; Chronicling America (12-24 Dec 1864, hits not read page by page); the Huntington's CONTENTdm full-text search.

WHERE WE HAVE NOT YET LOOKED PROPERLY (start here)
- the Secretary of War's order of 2 Dec 1864; NARA RG 99 (Paymaster General) and RG 107, RG 393 (Army of the Potomac, telegrams received); Meade's papers; Official Records ser. III vols 4-5 and the Paymaster General's 1865 report; Sixth Corps regimental histories; HathiTrust; JSTOR.

HOW TO REPORT (this part is the same for every label)
- Write your answer as one Markdown file in the repository github.com/NoAutopilot/cipher-lab at the path
  `ciphers/eckert-1864/second-opinions/chatgpt-n2-gi-<UTC date>.md`. Do not touch any other file. Do not commit to `main`:
  create a branch named `second-opinion/SO-ECKERT-N2-GI` and open a pull request from it, titled exactly
  `[SO-ECKERT-N2-GI] second opinion: Brice to Meade: two paymasters to City Point by river to pay two Sixth Corps regiments unpaid since 31 August, 14 Dec 1864`.
- The first lines of the file must be this header, filled in:
      label: SO-ECKERT-N2-GI
      model: <your model name and version>
      date: <UTC date you answered>
      prompt: PROMPT-chatgpt-n2-gi.md in this folder
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
