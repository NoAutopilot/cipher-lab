SECOND OPINION REQUEST, label SO-THURLOE-P4

We are an open cipher-research repository (github.com/NoAutopilot/cipher-lab). We have read the cipher passages of
one letter printed in Thurloe's State Papers without a decipherment. Try to prove that its cipher text was
already read or printed before us, and look for mistakes in our reading. Be adversarial. We would rather learn now that it is
in print than claim it wrongly later.

THE ITEM
- Letter of "W. S." (William Stamford, who signs his later letters in full), Calais, 13 March 1655 N.S. (Birch dates it "Callais,
  March 13, [1654. N.S.]"; the endorsement reads "13/3 March 1654/5"), to an unnamed correspondent. "Your friend" is the Protector. Macray's
  Rawlinson index has "Stamford, W., Calais. Letters to col. Kelsey; Mar. 1654/5, A. 24. 73".
- Print: Thomas Birch, A Collection of the State Papers of John Thurloe (1742), vol. 3 pp.187-189 (Internet Archive
  collectionofstat03thur; British History Online, thurloe-papers/vol3/pp185-195). The clear English is printed together with runs of cipher
  numerals (1-43 single letters, 62-189 words and names, and a sign for "the lord protector"). There is **no decipherment**. The endorsement
  summarises the letter: "His desire of a correspondence, and promise of performing some emminent service ... namely in
  discovering of the plott". Original: Bodleian MS Rawl. A. 24 (Birch's margin: "Vol. xxiv. p.73, 76").
- Key: rebuilt from Birch's printed decipherments of Stamford's later letters (vol. 3 pp.274-280 and 337-340). Tomokiyo
  (cryptiana.web.fc2.com/code/thurloe.htm, "William Stamford (1655)", image stamford.jpg) publishes the same letter table.
  Ours agrees with his on every value that occurs in this letter.
- Our reading of the cipher runs, normalised (the mechanical output has defects: "a plot hath been a hatching" is
  "apothhathaibeeneahtching", "irreconciliable with them as long as I live" is "irreconciiablk(w?)iththemaslongaailite";
  [England] (code 67) and "the cavaliers" (code 153) are each read from one occurrence only, grade M): "it is come to my knowledge by meere chance and without the
  least iniunction of secrecy, the person I got it from taking it for granted upon his meeting mee as hee thought
  stealing out of Whitehall [England] that I was not only perticularly informed of the mater but also employed in it";
  "the absolute breaking of a plot hath been a hatching by the whole partie of [143]"; "render my selfe irreconciliable
  with them as long as I live"; "the qualitie I am of ... amongst all the cavaliers"; "a more general rising ... in which more
  people are engaged then in any one of the former ones"; "a thousand armes". Eleven lines of p.188 remain partly
  incoherent.
- Our files: reading https://raw.githubusercontent.com/NoAutopilot/cipher-lab/main/ciphers/thurloe-printed/pool_1654/reading_P4.txt ; key https://raw.githubusercontent.com/NoAutopilot/cipher-lab/main/ciphers/thurloe-printed/pool_1654/key_stamford.tsv ;
  ciphertext https://raw.githubusercontent.com/NoAutopilot/cipher-lab/main/ciphers/thurloe-printed/P4/ciphertext.txt ; notes https://raw.githubusercontent.com/NoAutopilot/cipher-lab/main/ciphers/thurloe-printed/NOTES.md ; our search log https://raw.githubusercontent.com/NoAutopilot/cipher-lab/main/ciphers/thurloe-printed/AUDIT.md (sections "P4" and "Second audit
  (adversarial), P4").

WHERE WE HAVE LOOKED: Birch vol. 3 (text and index) and vol. 7 (general index); British History Online; CSPD 1655; Calendar
of the Clarendon State Papers vol. 3; Nicholas Papers vols 2-3; Clarke Papers vol. 3; Gardiner, Commonwealth and Protectorate
vol. 3; Abbott, Writings and Speeches of Cromwell vol. 3; Underdown, Royalist Conspiracy in England; Smith, Cavaliers in Exile;
Akkerman, Invisible Agents; Macray's Rawlinson catalogue; the Bodleian's online item catalogue (it has no item record for these folios);
Tomokiyo's pages; the GitHub repositories dbourdeau/cyphersolver and aaymeloglu/unsolved-ciphers; Internet Archive full text.

WHERE WE HAVE NOT YET LOOKED PROPERLY (start here)
- Timothy Noel Peacock, "Cromwell's 'spymaster'? John Thurloe and rethinking early modern intelligence", The Seventeenth
  Century 35:1 (2020) pp.3-30 (doi 10.1080/0268117X.2018.1524786); Alan Marshall, Intelligence and Espionage in the Reign of
  Charles II, and his 2023 chapter on Thurloe.
- Printed Clarendon State Papers vol. 3 (1786), March-April 1655; Firth, "Cromwell and the Insurrection of 1655", EHR 3 (1888)
  and 4 (1889); Woolrych, Penruddock's Rising 1655 (1955); Thurloe biographies; theses on Thurloe's intelligence network.
- Who William Stamford was (any biography, ODNB, History of Parliament, or Kelsey's papers), and whether any study quotes this letter's plot
  report.
- Any transcription or calendar of MS Rawl. A. 24 that notes a decipherment interlined or on a separate leaf.
- HathiTrust full text and JSTOR, which we cannot reach from our environment.

HOW TO REPORT (this part is the same for every label)
- Write your answer as one Markdown file in the repository github.com/NoAutopilot/cipher-lab at the path
  `ciphers/thurloe-printed/second-opinions/chatgpt-2026-09-24.md`. Do not touch any other file. Do not commit to `main`:
  create a branch named `second-opinion/SO-THURLOE-P4` and open a pull request from it, titled exactly
  `[SO-THURLOE-P4] second opinion: W. Stamford, Calais, 13 Mar 1655`.
- The first lines of the file must be this header, filled in:
      label: SO-THURLOE-P4
      model: <your model name and version>
      date: <UTC date you answered>
      prompt: PROMPT-chatgpt.md in this folder
  and then sections 1-5 in the order below.
- Every citation must be checkable from a desk: author, title, year, volume, page, and a URL to the page
  on Google Books, HathiTrust, Internet Archive, Gallica or the publisher. If you cannot give a page and a
  URL, mark the citation "unverified". Never invent a page number.
- Do not use the words "first", "new", "unpublished", "unread" or "never printed" about our reading. Our
  rule is that only a separate verifier may say that. Your job is to try to prove the opposite: that the
  text is already in print somewhere, or that our reading is wrong.

WHAT TO PUT IN THE FILE
1. Prior print: any edition, calendar, article or book that prints this letter, quotes it, summarises it,
   or prints its decipherment. Give the earliest you can find. If you find nothing, list exactly what you
   searched (catalogue, query, date) so we can tell a real gap from a shallow search.
2. Prior decipherment: anyone who has already read this cipher (the same key, the same folio), including
   blog posts, GitHub repositories, DECODE (de-crypt.org) records, theses, and conference papers.
3. Errors in our reading: any token, name, date or phrase you believe is misread, with your reason and
   the source that shows it.
4. Leads: archives, editions or scholars we should check, with a one-line reason each.
5. Confidence: one sentence on how sure you are that nothing prior exists, and what would change it.

<!-- Corrected 24 Sept 2026 by verifier V3a after SO-THURLOE-P4 (AUDIT.md): Peacock not Marshall; defects and M grades stated. -->
