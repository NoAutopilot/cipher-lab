# Reading instructions for the decipherment passes (N5-VIVK, 4 Oct 2026)
The page is a clerk's plain-French decipherment (1573, Spanish court news for the King of France), in a widely spaced
16th-century hand. Each page is cut into horizontal strips S01, S02, ... (no vertical overlap) and each strip into a
left half h1 and a right half h2 that share about 400 px in the middle (a word or two): for every text line, read the
h1 part, then continue with the h2 part, writing each word once.
Output: one output line per manuscript line, in order, the French exactly as written (old spelling, no modernising),
abbreviations as written with the suspension shown in brackets where you can expand it safely, e.g. "V[ost]re
Ma[jes]té", "led[ict]". A word you cannot read: <?>; a guess: the word followed by "?". Struck-through words: {del:...}.
Interlinear additions: {add:...}. Ignore later dockets, folio numbers and stamps.
