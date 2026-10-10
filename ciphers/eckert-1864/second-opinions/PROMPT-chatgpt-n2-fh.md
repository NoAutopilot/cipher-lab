SECOND OPINION REQUEST, label SO-ECKERT-N2-FH

We are an open cipher-research repository (github.com/NoAutopilot/cipher-lab). We have read one American Civil War-era
cipher telegram and want you to try to prove that its text was already printed before us, and to find mistakes in our
reading. Be adversarial: we would rather learn now that it is in print than claim it wrongly later.

THE ITEM
- Source: Thomas T. Eckert Papers, Huntington Library, San Marino, mssEC 18 (War Department telegraph office, ciphers sent) p.250 (digital pointer 9916), the third entry on the page, N2-FH, headed "J H Emerick / Washn Decr 17th 1864", https://hdl.huntington.org/digital/collection/p16003coll11/id/9916. Read with War Department Cipher No. 2.
- Reading: "[7 PM] [17] [Lieutenant] [Colonel] G W Bradley Chief [Quartermaster]: The [steam]er(s) Guide, Cossack, T. Collyer, Escort, Louise, Hero of Jersey, Manhattan & Crescent are ordered to [report] to [General Sherman] [.] Any [of the] above named vessels which are [in the] [James] [will be] ordered to [report] as directed at or [near] [Savannah] [?] chf [Quartermaster] at that [point] [signed] Rufus Ingalls Chf [Quartermaster] [Brigadier General]". Bracketed words are code words read from the period key; the rest is clear on the page; [?] is one unread group.
- Context we already know: the follow-up of 18 Dec 1864 to Bradley at City Point (Huntington pointer 9142, our N2-CJ): the orders about the transports for Sherman will be carried out; send the named boats in the James without delay.
- Our files: reading https://raw.githubusercontent.com/NoAutopilot/cipher-lab/main/ciphers/eckert-1864/reading-no2.md,
  key https://raw.githubusercontent.com/NoAutopilot/cipher-lab/main/ciphers/eckert-1864/key-no2.md, search log
  https://raw.githubusercontent.com/NoAutopilot/cipher-lab/main/ciphers/eckert-1864/AUDIT.md (section "AUDIT (FV-N2b)").

WHERE WE HAVE LOOKED: Official Records ser. I vols 41 pt 4, 42 pt 3, 44, 45 pt 2 (vessel names; 16-18 Dec 1864); Google Books phrase search; the Huntington's CONTENTdm full-text search.

WHERE WE HAVE NOT YET LOOKED PROPERLY (start here)
- Official Records ser. III vol. 4 and the Quartermaster General's annual report for 1865 (vessel lists); Official Records of the Union and Confederate Navies; the Meigs and Ingalls papers; NARA RG 92; the press of 17-24 Dec 1864; HathiTrust; JSTOR.

HOW TO REPORT (this part is the same for every label)
- Write your answer as one Markdown file in the repository github.com/NoAutopilot/cipher-lab at the path
  `ciphers/eckert-1864/second-opinions/chatgpt-n2-fh-<UTC date>.md`. Do not touch any other file. Do not commit to `main`:
  create a branch named `second-opinion/SO-ECKERT-N2-FH` and open a pull request from it, titled exactly
  `[SO-ECKERT-N2-FH] second opinion: Ingalls to Bradley: eight steamers ordered to report to Sherman at Savannah, 17 Dec 1864`.
- The first lines of the file must be this header, filled in:
      label: SO-ECKERT-N2-FH
      model: <your model name and version>
      date: <UTC date you answered>
      prompt: PROMPT-chatgpt-n2-fh.md in this folder
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
