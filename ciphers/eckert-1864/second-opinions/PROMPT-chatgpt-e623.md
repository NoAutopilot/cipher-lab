SECOND OPINION REQUEST, label SO-ECKERT-E623

We are an open cipher-research repository (github.com/NoAutopilot/cipher-lab). We have read one American Civil War
cipher telegram and want you to try to prove that its text was already printed before us, and to find mistakes in our
reading. Be adversarial: we would rather learn now that it is in print than claim it wrongly later.

THE ITEM
- Source: Thomas T. Eckert Papers, Huntington Library, San Marino, mssEC 25 ("Ciphers Received and Sent", Fort Monroe) p.112 (digital pointer 5656), headed "May 5th 1864", E623, https://hdl.huntington.org/digital/collection/p16003coll11/id/5656. Read with War Department Cipher No. 1 (Huntington mssEC 41).
- Reading (code words in brackets, as corrected by our verifier, AUDIT (FV-L17c) s.3): "[Monroe] May fifth [12.30] for [Maj. Gen. Lew Wallace] [Baltimore] [.] W. W. Shore is in [Baltimore] somewhere he was some time ago ordered out of this Dept. [.] I want him caught and [Arrest]ed and sent to me under guard [.] Have the evidence against him [.] he is the Corresp't of the World from Balto as he was from here [.] the General [Telegraph]ed you three days ago to arrest him Since which we have heard nothing [.] I presume you did not get the dispatch [.] can send you if necessary a man who knows him [.] John I Davenport Lieut Office Bureau of [Information] very warm here today Yours Geo. D. Sheldon"
- Context we already know: Butler's telegram of 1 May 1864 to Lew Wallace ordering Shore's arrest (Huntington clear copy, pointer 10291: "Correspondant of the N. Y. World at Baltimore & also from Ft Monroe is WW Shore whom I sent away from this Dept ---- Please arrest him and send him to me ---- I have found in the Richmond papers that his articles are giving aid and comfort to the Enemy"). That is the earlier telegram, not this one.
- Our files: reading https://raw.githubusercontent.com/NoAutopilot/cipher-lab/main/ciphers/eckert-1864/reading.md,
  key https://raw.githubusercontent.com/NoAutopilot/cipher-lab/main/ciphers/eckert-1864/key.md, search log
  https://raw.githubusercontent.com/NoAutopilot/cipher-lab/main/ciphers/eckert-1864/AUDIT.md (section "AUDIT (FV-L17c)").

WHERE WE HAVE LOOKED: Official Records ser. I vols. 33, 36 pts 1-3 and 37, ser. II vol. 7 (full text, by phrase and by name); Butler's Private and Official Correspondence vol. IV; the Huntington's CONTENTdm full-text search across the whole Eckert collection (fresh words, 10 Oct 2026); Internet Archive full-text search (whole collection, by phrase).

WHERE WE HAVE NOT YET LOOKED PROPERLY (start here)
- The New York World and the Baltimore papers of May 1864 (Shore's arrest, his articles); Official Records ser. II vols. 6-7 by name; Lew Wallace's papers and autobiography; NARA RG 393 (Middle Department) and RG 109/110 (Turner-Baker papers, Bureau of Information); Google Books; HathiTrust; JSTOR.

HOW TO REPORT (this part is the same for every label)
- Write your answer as one Markdown file in the repository github.com/NoAutopilot/cipher-lab at the path
  `ciphers/eckert-1864/second-opinions/chatgpt-e623-<UTC date>.md`. Do not touch any other file. Do not commit to `main`:
  create a branch named `second-opinion/SO-ECKERT-E623` and open a pull request from it, titled exactly
  `[SO-ECKERT-E623] second opinion: Fort Monroe asks General Lew Wallace at Baltimore to arrest W. W. Shore, the New York World's correspondent, 5 May 1864`.
- The first lines of the file must be this header, filled in:
      label: SO-ECKERT-E623
      model: <your model name and version>
      date: <UTC date you answered>
      prompt: PROMPT-chatgpt-e623.md in this folder
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
