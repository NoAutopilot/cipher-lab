# Charles II to the Duke of Hamilton, August-September 1650

- **Status:** Open. Offline-only. The key is located in the archive and catalogued as open; nothing more can be
  done from published sources. This is the first target of the archive-request lane (see `REQUEST.md`).
- **Plaintext language:** English.
- **Source of ciphertext:** two printed witnesses, collated in `ciphertext.txt`. Gardiner (Camden Society 1880)
  printed the figures from the manuscripts and left them undeciphered; the 1766 *Account of the Preservation of
  King Charles II* printed them earlier. Where the two disagree (five places) both readings are kept and the
  microfilm of the originals will settle them.
- **Prior work:** Tomokiyo, charlesii.htm section 2, lists it and identifies 132 as Dunfermline. Bourdeau
  (cyphersolver/hamilton, 14-15 Sept 2026) collated the witnesses, established that the Camden volume cannot yield
  the key (Gardiner says the letters came "without any key being appended"), found the key's shelfmark in the NRS
  catalogue, and parked the item as offline-only. Aymeloglu's shortlist notes a second possible key location, John
  Wallis's papers at the Bodleian, which hold royalist letters he deciphered in 1650.
- **What is in the cipher:** 102 groups, 67 distinct, range 3-384. A small nomenclator. Groups under about 90 are
  probably letters and nulls, 100 and above words and names. 3 and 10 sit at the ends of runs three times each,
  so probably nulls or a terminal letter. Bare code words in clear: 163, 122, 223 (persons: agents or bearers),
  132 (the dateline). Repeated pairs across letters: 237 70, 192 ... 308 100, 308 290, 58 135 256 58 256.
- **Why it cannot be broken from the text:** 102 groups with almost no redundancy is far below what any solver
  reads. Bourdeau's judgement, and the matched-control discipline in LESSONS.md, both say stop here.
- **Historical frame, for checking the reading when the key comes:** Hamilton was confined to the Isle of Arran
  from the King's landing in June 1650 until January 1651. On 6 August the Kirk had just removed Charles from the
  army at Leith and was pressing the Dunfermline Declaration, signed 16 August; the "two things" are probably the
  declaration and the army. 31 August is three days before Dunbar. 27 September, "I have at last resolved that
  ... by the ...", is the decision that became the Start, Charles's flight from Perth to the Highland royalists on
  4 October; "preparing yourself ... to get you" is about getting Hamilton off Arran.
- **When the copies arrive:**
  1. Transcribe each of the five key sheets in GD406/1/2197 as `key-<item>.tsv` (number, value). Do not merge
     them; the 1650 key may be one sheet, or none of them.
  2. `python3 apply_key.py key-<item>.tsv` renders all four letters. A key that gives English in the runs and
     sensible names for 163, 122, 223 is the one. Grade every group H (read from the key sheet) and mark any
     group absent from the sheet M.
  3. If no sheet fits, order the microfilm frames of Red Book ii nos. 156-159 to check the printed figures,
     and try the Bodleian Wallis route.
  4. Send the result to Tomokiyo and to Bourdeau, who will record it.
