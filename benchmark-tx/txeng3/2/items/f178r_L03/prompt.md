You are describing signs in a line of a 16th-century symbol-cipher letter (Italian hand). You read images only; you have no key and must not guess what any sign means. Do not open any file other than those listed here, and do not search the repository.

## Files
- Marked line crop(s) (the cipher line as the readers saw it; blue boxes with letter labels mark the positions to describe; the white strip at the top is padding added for the labels):
  - benchmark-tx/txeng3/2/items/f178r_L03/marked_f178r_L03_s2.png
  - benchmark-tx/txeng3/2/items/f178r_L03/marked_f178r_L03_s3.png
- Enlarged tile of each marked position (3x):
  - A: benchmark-tx/txeng3/2/items/f178r_L03/tile_A.png
  - B: benchmark-tx/txeng3/2/items/f178r_L03/tile_B.png
  - C: benchmark-tx/txeng3/2/items/f178r_L03/tile_C.png
  - D: benchmark-tx/txeng3/2/items/f178r_L03/tile_D.png
  - E: benchmark-tx/txeng3/2/items/f178r_L03/tile_E.png
  - F: benchmark-tx/txeng3/2/items/f178r_L03/tile_F.png
- Reference sheet of the cipher's signs with ID numbers T10-T98 (no meanings): ciphers/nevers-birago-fr3251-1572/harvest/sign_sheet_blind_1572.png
- Clear-text sheet crops (a contemporary clerk's handwritten plain text of the same letter; each sheet line is given as three overlapping crops s1, s2, s3 from left to right):
  - ciphers/nevers-birago-fr3251-1572/harvest/f179r_sheet/dec_L02_s1.jpg
  - ciphers/nevers-birago-fr3251-1572/harvest/f179r_sheet/dec_L02_s2.jpg
  - ciphers/nevers-birago-fr3251-1572/harvest/f179r_sheet/dec_L02_s3.jpg
  - ciphers/nevers-birago-fr3251-1572/harvest/f179r_sheet/dec_L03_s1.jpg
  - ciphers/nevers-birago-fr3251-1572/harvest/f179r_sheet/dec_L03_s2.jpg
  - ciphers/nevers-birago-fr3251-1572/harvest/f179r_sheet/dec_L03_s3.jpg

NOTE: on this line the boxes were placed by proportion along the line, not by exact segmentation, so a box may sit on a neighbouring sign; describe the sign nearest the box centre and say if the box is off.

## Positions to describe
For each label, the clerk's sheet line and its transcription are given with ONE word in [brackets] and a letter index inside that word (1 = first letter). That bracketed word is where the clerk's clear text corresponds to the marked cipher sign; the index is the letter the sign is believed to stand for. Find the word in the sheet crops and look at that letter.

- A: crop f178r_L03_s3.jpg; sheet line L03, letter 3 of the bracketed word: "et tolto [licencia] [struck word] da loro, altezze per incaminarsi, alla uolta, di guase"
- B: crop f178r_L03_s3.jpg; sheet line L03, letter 6 of the bracketed word: "et tolto [licencia] [struck word] da loro, altezze per incaminarsi, alla uolta, di guase"
- C: crop f178r_L03_s2.jpg; sheet line L02, letter 2 of the bracketed word: "ndea ch'auesse piu; a ritornare, a car.la ma solo, [andarsene] a, turino"
- D: crop f178r_L03_s2.jpg; sheet line L02, letter 4 of the bracketed word: "ndea ch'auesse piu; a ritornare, a car.la ma solo, [andarsene] a, turino"
- E: crop f178r_L03_s3.jpg; sheet line L03, letter 2 of the bracketed word: "[et] tolto licencia [struck word] da loro, altezze per incaminarsi, alla uolta, di guase"
- F: crop f178r_L03_s2.jpg; sheet line L02, letter 1 of the bracketed word: "ndea ch'auesse piu; a ritornare, a car.la ma solo, [andarsene] a, turino"

## Questions, answered per label from the images
Q1 box: does the blue box cover exactly one whole sign? Answer one of: whole | cut (only part of a sign is in the box, or the crop edge cuts the sign) | joined (the box holds more than one sign, or two signs are written touching) | unclear.
Q2 ink of that sign: clean | faint | damaged (blot, bleed-through, hole, smear) | struck-or-overwritten.
Q3 resemblance: the two reference-sheet IDs the sign most resembles, best first, each with a confidence 1-5 (5 = certain); then hard_pair: true if the two are hard to tell apart on THIS tile, false if the first is clearly it.
Q4 clerk text: the bracketed word as you actually read it in the sheet crop (letters only, as written, keep abbreviations); legible: true/false for the indexed letter; issue: one of none | abbreviation | ampersand | struck | correction | illegible | not-found (word not found in crops).
Q5 note: one short sentence, anything else you see at that position (e.g. a mark above, a different stroke weight, the box sits between two signs).

## Output
Write a JSON array to benchmark-tx/txeng3/2/items/f178r_L03/answer.json with one object per label: {"label","q1","q2","q3_top1","q3_conf1","q3_top2","q3_conf2","hard_pair","q4_word","q4_legible","q4_issue","q5"}. Then reply with just the JSON. Look at the tile AND the marked crop for every label; look at the reference sheet once; look at each sheet crop once.