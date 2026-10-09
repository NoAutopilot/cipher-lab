SECOND OPINION REQUEST, label SO-ECKERT-E292

We are an open cipher-research repository (github.com/NoAutopilot/cipher-lab). We have read one American Civil War
cipher telegram and want you to try to prove that its text was already printed before us, and to find mistakes in our
reading. Be adversarial: we would rather learn now that it is in print than claim it wrongly later.

THE ITEM
- Source: Thomas T. Eckert Papers, Huntington Library, San Marino, mssEC 25 ("Ciphers Received and Sent", Fort Monroe) p.239 (digital pointer 5783), second entry on the page, E292, headed "Fort Monroe Sept 16/64 / G. J. Lawrence Harpers Ferry", signed Geo. D. Sheldon, https://hdl.huntington.org/digital/collection/p16003coll11/id/5783. Read with War Department Cipher No. 1 (Huntington mssEC 41).
- Reading: "[Head Quarters] A. P. [16]. For Lieut. [Colonel] Morgan, [Harpers Ferry]. The [enemy] made a raid on the cattle herd near Coggins Point & [captured] the entire herd, [2486] head. The lines are down and you will have to order by [telegraph] from [Monroe]. [Signed] Thomas Wilson Lieut [Colonel] and C. S. Add following from [Monroe] [6 PM]: The above telegram was received from Lieut [Colonel] Wilson. I will send [1200] head tomorrow. [Signed] M. P. Small Lieut Kernel and C. S." Bracketed words are code words read from the period key; "a Pea" (= A. P.) and "Kernel" (= Colonel) are the clerk's phonetic spellings.
- Context we already know: Official Records ser. I vol. 42 pt 2 prints Humphreys's order of 16 Sept 1864 naming "Colonel Wilson, chief commissary of subsistence", and Capt. D. D. Wiley to Lt Col M. R. Morgan, 18 Sept 1864, care of Lt Col M. P. Small at Fort Monroe: "The enemy got off with the whole herd at Coggins' Point, 2,486 head." The first entry on the same ledger page is Wilson's own telegram to Washington about the raid.
- Also known (second audit, 9 Oct 2026): Official Records ser. I vol. 42 pt 1 prints the 2,486 count in the reports of Capt. J. H. Woodward (addressed to Lt Col M. R. Morgan), Capt. N. A. Richardson and Wade Hampton, and the Papers of U. S. Grant vol. 12 puts Grant at Harpers Ferry on 16 Sept 1864; these are context, not a print of this telegram.
- Our files: reading https://raw.githubusercontent.com/NoAutopilot/cipher-lab/main/ciphers/eckert-1864/reading.md,
  key https://raw.githubusercontent.com/NoAutopilot/cipher-lab/main/ciphers/eckert-1864/key.md, search log
  https://raw.githubusercontent.com/NoAutopilot/cipher-lab/main/ciphers/eckert-1864/AUDIT.md (section "AUDIT (FV-FM9a)").

WHERE WE HAVE LOOKED: Official Records ser. I vol. 42 pts 1-3 (full text, by phrase and name); OR ser. I vols. 33, 36, 40, 43 and ORN by phrase; Papers of Ulysses S. Grant vol. 12 (Internet Archive full-text snippets only); Butler's Private and Official Correspondence vols. IV-V; the Huntington's CONTENTdm full-text search across the whole Eckert collection.

WHERE WE HAVE NOT YET LOOKED PROPERLY (start here)
- Commissary General of Subsistence records (NARA RG 192) and Wilson's or Small's letters; Papers of U. S. Grant vol. 12 page by page; histories of the 'Beefsteak Raid' (Hampton's cattle raid, 14-17 Sept 1864) that quote Union telegrams; newspapers of September 1864; Google Books; HathiTrust; JSTOR.

HOW TO REPORT (this part is the same for every label)
- Write your answer as one Markdown file in the repository github.com/NoAutopilot/cipher-lab at the path
  `ciphers/eckert-1864/second-opinions/chatgpt-e292-<UTC date>.md`. Do not touch any other file. Do not commit to `main`:
  create a branch named `second-opinion/SO-ECKERT-E292` and open a pull request from it, titled exactly
  `[SO-ECKERT-E292] second opinion: Fort Monroe to Lt Col M. R. Morgan, Harpers Ferry: the Coggins Point cattle raid, 16 Sept 1864`.
- The first lines of the file must be this header, filled in:
      label: SO-ECKERT-E292
      model: <your model name and version>
      date: <UTC date you answered>
      prompt: PROMPT-chatgpt-e292.md in this folder
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
