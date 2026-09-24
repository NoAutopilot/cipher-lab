SECOND OPINION REQUEST, label SO-BLATHWAYT-1728

We are an open cipher-research repository (github.com/NoAutopilot/cipher-lab). We have partly read three short
French cipher passages of 1727-1729 in the Huntington Library and want you to try to prove that their text, or a
decipherment of them, was already printed or recorded before us, and to find mistakes in our reading. Be
adversarial: we would rather learn now that they are in print than claim it wrongly later.

THE ITEMS
- Source: Huntington Library, San Marino, William Blathwayt papers addenda (mssBLA 1-195), Box 3, "diplomatic
  correspondence and intelligence reports (1720-1734)"; finding aid https://oac.cdlib.org/findaid/ark:/13030/kt1199n4mx.
  The key was set out from contemporary French decipherments of other letters in the same box (mssBLA 179, 185,
  187-190, 194): one numeric code (groups numbered up to about 1,300; syllables, words, names), used 1725-1729; 395 groups are keyed.
- mssBLA 186, "Letter of intelligence", Madrid, 13 Sept 1728, in French, signed "N", describing Ripperda's escape
  from the castle of Segovia, with two lines in cipher. Its clear text is already printed in English extract:
  George Henry Rose (ed.), A Selection from the Papers of the Earls of Marchmont (1831), vol. 2 pp.414-415
  (archive.org/details/selectionfrompap02roseiala), as "The Abbe Paretti to Alexander Earl of Marchmont", dated there
  3 Sept 1728, with the p.1 cipher line shown only as "(Cypher.)"; the p.3 cipher line is outside the extract. The
  question is only the two cipher lines. Our partial reading: p.1 "l'ambassadeur [?] a été fort [?]
  [?] [?]te affaire"; p.3 "Monsieur de Patigno m'en a [?] ce soir" (Patiño). A slip in the folder by Christopher
  Storrs (26 Apr 2006) corrects the date from 1708 to 1728.
- mssBLA 191, enclosure (a): undated cipher letter from Port Ste Marie (El Puerto de Santa María), forwarded to
  the Duke of Newcastle from "Cesnok" (Cessnock, Ayrshire) on 8 Aug 1729. Partial reading (106 of 141 groups
  at grade C; the French below is our interpretation: "milord", "m'aime", "serai" and "ignorance" rest on joins,
  repairs and one inferred value, 585 = ig; the mechanical layer is reading.txt): the writer thanks "milord" for his letter, says that Monsieur Keene likes him but has no orders from
  [?] for him, that in "l'affaire passée" he did [?] service without being told what he could offer "pour le mieux
  à l'accommodement", "je serai inutile dans l'ignorance", "mandez-moi donc quelque ordre pour ma [?]".
- mssBLA 184, "Statement re M. Rottembourg", [1727-1728], French with seven code groups; only three syllables read.
- Our files: reading https://raw.githubusercontent.com/NoAutopilot/cipher-lab/main/ciphers/huntington-blathwayt-madrid-1728/reading.txt, graded tokens https://raw.githubusercontent.com/NoAutopilot/cipher-lab/main/ciphers/huntington-blathwayt-madrid-1728/reading_tokens.tsv, key https://raw.githubusercontent.com/NoAutopilot/cipher-lab/main/ciphers/huntington-blathwayt-madrid-1728/key.tsv,
  notes https://raw.githubusercontent.com/NoAutopilot/cipher-lab/main/ciphers/huntington-blathwayt-madrid-1728/NOTES.md, our search log https://raw.githubusercontent.com/NoAutopilot/cipher-lab/main/ciphers/huntington-blathwayt-madrid-1728/AUDIT.md.
- Page images: https://hdl.huntington.org/digital/collection/p15150coll7/id/61211 (BLA 186),
  https://hdl.huntington.org/digital/collection/p15150coll7/id/61008 (BLA 191),
  https://hdl.huntington.org/digital/collection/p15150coll7/id/60843 (BLA 184).

WHERE WE HAVE LOOKED: the whole Huntington collection (no duplicate or decipherment of these three); Coxe,
Memoirs of Walpole (1798) and of Horatio Walpole (1802), Memoirs of the Kings of Spain; HMC Townshend (1887); HMC
Polwarth vols I-III; Armstrong, Elisabeth Farnese (1892); Syveton on Ripperda (1896); Internet Archive full text;
TNA Discovery catalogue descriptions (SP 94, SP 89, SP 36, SP 78); CrossRef, HAL, Persée; GitHub cipher projects.

WHERE WE HAVE NOT YET LOOKED PROPERLY (start here)
- HMC, Report on the Manuscripts of Lord Polwarth, vols IV (1940) and V (1961): the Marchmont (Hume-Campbell)
  papers; BLA 191 was sent from Cessnock, the Hume-Campbell seat, and BLA 176-177 are addressed to Marchmont.
- Christopher Storrs, The Spanish Resurgence 1713-1748 (Yale 2016) and his articles: does he cite or quote BLA 186
  or the Port Ste Marie correspondent?
- TNA SP 94/98-100 (Keene, Seville and Port St Mary, 1728-29) and BL Add MSS Newcastle papers: any calendar,
  printed extract or decipherment of a Port St Mary intelligence letter of July-Aug 1729.
- Richard Lodge, "The Treaty of Seville (1729)", TRHS 1933, and Lodge's other Keene work; Goslinga (1915) on
  Soissons and Seville; the Montgon letters and memoirs; Spanish-language work on Patiño's agents and on Ripperda's
  escape; British Diplomatic Instructions if a Spain volume covers 1728-29.
- The identity of the Port Ste Marie correspondent (who wrote to "milord" in French, knew Keene and Patiño, and
  owed money) and of the Madrid writer signing "N": an identification in print would lead to the edition.
- HathiTrust full text, Google Books and JSTOR, which we cannot fully reach from our environment.

HOW TO REPORT (this part is the same for every label)
- Write your answer as one Markdown file in the repository github.com/NoAutopilot/cipher-lab at the path
  `ciphers/huntington-blathwayt-madrid-1728/second-opinions/chatgpt-2026-09-24.md`. Do not touch any other file. Do not commit to `main`:
  create a branch named `second-opinion/SO-BLATHWAYT-1728` and open a pull request from it, titled exactly
  `[SO-BLATHWAYT-1728] second opinion: Madrid and Port Ste Marie intelligence, 1728-29`.
- The first lines of the file must be this header, filled in:
      label: SO-BLATHWAYT-1728
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

<!-- Corrected 24 Sept 2026 by verifier V3a after SO-BLATHWAYT-1728 (AUDIT.md): Rose 1831 print stated; interpretive French marked. -->
