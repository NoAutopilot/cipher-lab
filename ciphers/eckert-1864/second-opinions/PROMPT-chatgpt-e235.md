SECOND OPINION REQUEST, label SO-ECKERT-E235

We are an open cipher-research repository (github.com/NoAutopilot/cipher-lab). We have read one American Civil War
cipher telegram and want you to try to prove that its text was already printed before us, and to find mistakes in our
reading. Be adversarial: we would rather learn now that it is in print than claim it wrongly later.

THE ITEM
- Source: Thomas T. Eckert Papers, Huntington Library, San Marino, mssEC 25 ("Ciphers Received and Sent", Fort Monroe) p.287 (digital pointer 5831), second entry on the page, continued on p.288 (pointer 5832), E235, headed "Ft Monroe Dec. 14 - 1864 / Maj Eckert Washington", https://hdl.huntington.org/digital/collection/p16003coll11/id/5831. Read with War Department Cipher No. 1 (Huntington mssEC 41).
- Reading: the Fort Monroe telegraph office (signed L. F. Sheldon, operator Geo. D. Sheldon) to Maj. T. T. Eckert, Washington, 14 Dec 1864: "Last Friday [Foster], who had landed between Tullifinny Creek and Coosawatchie just below Pocotaligo, made a [reconnoissance] in [force] to within [150] yards of [the railroad], during which he cut an opening through the woods so as to [command] the [railroad] with [siege] [guns]; then [fell back] about half a [mile] and held his own, although [attacked] by a large [force]; lost about [150] [killed] and [wounded]. [The enemy] suffered severely, being twice [repulsed]. He was then able to knock fits out of [the railroad] with [two] [30(-?)]-pound Parrotts. This accounts for the break of [communication] between [Charleston] and [Savannah]. We heard [heavy] firing in the direction of [Savannah] [River], west of [Savannah], on Thursday and Friday. [Steamer] United States with [990] exchanged prisoners left [Charleston] Monday morning, arrived here at [7] this morning and left immediately for Annapolis." Bracketed words are code words read from the period key; the numeral before "pound" is written "lamp plank" (30, 2), which may be "32" or a slip for the 30-pounders printed elsewhere.
- Context we already know: OR ser. I vol. 44 pp.665-666 (Foster to Halleck, 8 Dec 1864: position within three-quarters of a mile of the railroad between the Coosawhatchie and Tullifinny), p.708 (Foster to Sherman, 13 Dec: batteries command the railroad, within 1,200 yards), pp.749-750 (Sherman to Foster, 18 Dec: "let them whale away with their 30-pounder Parrotts"), and the reports of the 9 Dec action at the Tullifinny. These print the operations, not this telegram.
- Our files: reading https://raw.githubusercontent.com/NoAutopilot/cipher-lab/main/ciphers/eckert-1864/reading.md,
  key https://raw.githubusercontent.com/NoAutopilot/cipher-lab/main/ciphers/eckert-1864/key.md, search log
  https://raw.githubusercontent.com/NoAutopilot/cipher-lab/main/ciphers/eckert-1864/AUDIT.md (section "AUDIT (FV-FM5c)").

WHERE WE HAVE LOOKED: OR ser. I vol. 44 and ser. II vol. 7, ORN ser. I vols. 11 and 16 (full text); 174 cached Official Records and related volumes (phrase search); the Huntington's CONTENTdm full-text search (which found period clear copies of four sibling telegrams, but not of this one).

WHERE WE HAVE NOT YET LOOKED PROPERLY (start here)
- New York, Baltimore and Washington newspapers of 15-17 Dec 1864 (a Fort Monroe press despatch with these words, or the arrival of the steamer United States with exchanged prisoners at Annapolis); the Grant Papers vol. 13; regimental histories of the Tullifinny action (Hatch's Coast Division); exchange-of-prisoners literature for the Charleston/Savannah River exchange of Nov-Dec 1864; Google Books; HathiTrust; JSTOR.

HOW TO REPORT (this part is the same for every label)
- Write your answer as one Markdown file in the repository github.com/NoAutopilot/cipher-lab at the path
  `ciphers/eckert-1864/second-opinions/chatgpt-e235-<UTC date>.md`. Do not touch any other file. Do not commit to `main`:
  create a branch named `second-opinion/SO-ECKERT-E235` and open a pull request from it, titled exactly
  `[SO-ECKERT-E235] second opinion: Fort Monroe to Eckert, Foster at the Tullifinny and 990 exchanged prisoners, 14 Dec 1864`.
- The first lines of the file must be this header, filled in:
      label: SO-ECKERT-E235
      model: <your model name and version>
      date: <UTC date you answered>
      prompt: PROMPT-chatgpt-e235.md in this folder
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
