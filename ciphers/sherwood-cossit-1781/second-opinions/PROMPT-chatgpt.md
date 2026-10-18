SECOND OPINION REQUEST, label SO-SHERWOOD-COSSIT

We are an open cipher-research repository (github.com/NoAutopilot/cipher-lab). We have read a numeral cipher of February 1783 with a
dictionary as the code book and want you to try to prove that its text was already printed or deciphered before us, and to find
mistakes in our reading. Be adversarial: we would rather learn now that it is in print than claim it wrongly later.

THE ITEM
- Source: Haldimand Papers, British Library Add MS 21838 pp.345-347 (Library and Archives Canada transcript volume B.178, microfilm reel
  H-1737 frames 15-17, heritage.canadiana.ca, reel oocihm.lac_reel_h1737). Four numeral messages (No.1-No.4, groups of the form
  page-line, e.g. 364-32) brought in by Captain Benjamin Sumner (written "Summer" by Brymner) from the Rev. Ranna Cossit's circle,
  Claremont, New Hampshire; No.4 is dated February 1783. Justus Sherwood, Haldimand's secret-service officer, wrote a partial
  "sketch" of their sense (B.178 pp.84-85) and called the use of the cypher "blundering". Brymner, Report on Canadian Archives 1888,
  calendars them ("Cypher messages brought in by Summer 345 to 347") without the text.
- Key: John Entick, The New Spelling Dictionary (London, 1781), archive.org/details/11280377bsb: first number = page, second = printed
  line within a column, column not written (we choose it by context). Entick as a British code book is itself published (Friedman's
  lectures; Leighton and Matyas, "The History of Book Ciphers", CRYPTO '84, LNCS 196, 1985), but we have not found this cypher's
  book or text named anywhere.
- Reading (excerpt, No.4): "Wednesday last 500 [sleighs?] ... aid towards Os[wego] ... alarm them they expect ... was [destined?]
  towards the reduction of the new state Colonel Strong report[ed in] council myself hearing Windsor ... 500 men only ... February".
  No.1 mentions a member of the House of New H[ampshire], Boston, an army sailing to the West, Congress, Portsmouth, and damage by
  thunder to one of the thirteen ships. Many words are uninflected dictionary headwords.
- Our files: reading https://raw.githubusercontent.com/NoAutopilot/cipher-lab/main/ciphers/sherwood-cossit-1781/reading.txt,
  graded rows https://raw.githubusercontent.com/NoAutopilot/cipher-lab/main/ciphers/sherwood-cossit-1781/reading.tsv, ciphertext
  https://raw.githubusercontent.com/NoAutopilot/cipher-lab/main/ciphers/sherwood-cossit-1781/ciphertext.tsv, search log
  https://raw.githubusercontent.com/NoAutopilot/cipher-lab/main/ciphers/sherwood-cossit-1781/AUDIT.md
- Already searched (18 Oct 2026): Brymner 1888; Collections of the Vermont Historical Society I-II; Records of the Governor and Council
  of Vermont III; Fryer, Buckskin Pimpernel (1981); Pell, Ethan Allen (1929); Vermont History 48:2 (1980); New England Quarterly 3:4
  (1930); Google Books snippets of Leighton and Matyas 1985 (full chapter not read); OpenAlex, Semantic Scholar, CrossRef.

HOW TO ANSWER
- Write your answer as one markdown file at ciphers/sherwood-cossit-1781/second-opinions/SO-SHERWOOD-COSSIT.md in the repository
  github.com/NoAutopilot/cipher-lab, create a branch named `second-opinion/SO-SHERWOOD-COSSIT` and open a pull request from it, titled
  exactly `[SO-SHERWOOD-COSSIT] second opinion: Cossit/Sumner cypher messages, February 1783, Haldimand Papers B.178 pp.345-347`.
- The first lines of the file must be this header, filled in:
      label: SO-SHERWOOD-COSSIT
      model: <your model name and version>
      date: <UTC date you answered>
      prompt: PROMPT-chatgpt.md in this folder
  and then sections 1-5 in the order below.
- Every citation must be checkable from a desk: author, title, year, volume, page, and a URL to the page on Google Books, HathiTrust,
  Internet Archive or the publisher. If you cannot give a page and a URL, mark the citation "unverified". Never invent a page number.
- Do not use the words "first", "new", "unpublished", "unread" or "never printed" about our reading. Our rule is that only a separate
  verifier may say that. Your job is to try to prove the opposite.

WHAT TO PUT IN THE FILE
1. Prior print: any edition, calendar, article, thesis or book that prints these messages, quotes them, or prints a decipherment
   (in particular Leighton and Matyas 1985 and any work drawing on Albert C. Leighton's research files; Ian Pemberton's work on Justus
   Sherwood; writing on Ranna Cossit, Benjamin Sumner, Willett's Oswego expedition of February 1783). Give the earliest. If nothing,
   list exactly what you searched.
2. Prior decipherment: anyone who has already read these messages or identified their code book.
3. Errors in our reading: whether the line convention (page + printed line, column unwritten) is attested for other Haldimand-service
   dictionary messages; whether "Colonel Strong" at Windsor in February 1783 is attested; sources.
4. Leads: archives, editions or scholars we should check, with a one-line reason each.
5. Confidence: one sentence on how sure you are that nothing prior exists, and what would change it.
