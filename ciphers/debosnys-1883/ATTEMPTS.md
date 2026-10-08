# What has been tried on Henry Debosnys's four 1883 jail cryptograms

Status: open -- nothing has been read.
Written: 8 Oct 2026, by the cipher-lab agents (a project run by one person with AI agents).
Draft for the project owner's review; sources are the files in this folder (CAMPAIGN.md, HYPOTHESES.md, ITERATE.md, NOTES.md, swarm/DIGEST-1.md and DIGEST-2.md).

This is a plain-English record of every approach we have tried, what it assumed, how we checked that the test itself was fair, and what came out. The short version: we have not read a single word of the four cryptograms. We have ruled out a number of simple explanations, and we have found some real structure in the writing. The main obstacle is the quality of the images we worked from, and that is where the numbers point.

## A note on how the tests work

A negative result from a code-breaking program means nothing on its own, because the program may simply be unable to read anything that looks like this. So for every test we first built a **control**: a made-up cipher of the same size, the same number of distinct signs and the same design that the hypothesis describes, with a known answer, and with the same level of copying mistakes we measured in our own transcription. If the method could not read the control, a failure on the real cryptogram counted for nothing, and we logged the result as "could not decide". Only when the method read the control and then failed on the real text do we write "control-backed negative for that design at the current transcription". We never say "disproved": every negative below is about one design at the image quality we have.

## What we have to work with

- **The four cryptograms.** We worked from the public images of the four cryptograms, as published by Klaus Schmeh on his Cipherbrain blog, and from the published clear-text poems, including the 14-line French poem on the page of cryptogram 3. Cryptogram 2 is the longest; cryptogram 4 is a verse of 20 lines.
- **Size.** About 1,250 signs in total, drawn from about 160 distinct signs (1,251 signs over 160 sign types after a sign-by-sign labelling by eye).
- **Transcription quality.** Each page was read two or three times independently and the readings reconciled. They agree on roughly 80 to 90 per cent of signs (cryptogram 1: 81.6 per cent; cryptogram 2: 82.8 per cent; cryptograms 3 and 4 together: 90.0 per cent). Agreement is not accuracy. Measured against a synthetic page built from our own crops with known answers, two strong independent readers made 15.6 to 17.7 per cent errors, and a comparison against Daniel Bourdeau's independent reading of cryptogram 2 puts the error hiding inside our agreed signs at about the same size (16.5 to 17.7 per cent). So the sign error on the public images is about 15 to 18 per cent on cryptograms 1 and 2, and 8.5 to 10 per cent on the verse pages. We believe that is the limit of those images, not of the readers.
- **A museum note.** The Adirondack History Museum has shared scans of its original sheets for research use. They are held privately and are not part of anything described here.

## What we tried, by family

### 1. Transcription and the sign inventory

*Assumed:* nothing about the system; the aim was a clean list of the signs.
*Check:* the synthetic page with known answers, described above. We also tried folding together signs that two readers confuse, then re-reading; we trained a per-sign classifier for six groups of look-alike signs; and we tried a third and fourth reading by a stronger reader.
*Result:* the folds and the classifier did not carry over to a fresh page with known answers, and a further pass on the disputed signs alone would not bring cryptogram 2 inside the error range in which automatic solvers work, because a good share of the error sits in signs where both readers agreed.
*Ruled out / undecided:* better transcription from the public pixels is a dead end. Not a negative about the cipher.

### 2. Letter substitution (one sign per letter, several signs for common letters)

*Assumed:* each sign stands for a letter, in French, English, Portuguese, Spanish or Latin, with extra signs for frequent letters (a "homophonic" cipher).
*Check:* matched controls enciphered in each language with 15 per cent sign noise, read by the same solvers.
*Result:* French: the solver read 0 of 8 real runs against 5 of 8 on its control. English: the real text came out at the 8th percentile of 50 refits against 100 of 100 on the control. Portuguese: 0 of 24 against 4 of 4. Spanish and Latin: negative, but the controls only partly passed (control power 1 of 4 and 2 of 4), so these are "disfavoured", not excluded.
*Rules out:* a straightforward letter substitution in French, English or Portuguese at the current transcription (control-backed negative for that design). Also supported by the sheer number of distinct signs: about 160 is far more than a letter alphabet needs.

### 3. Syllable and mixed systems

*Assumed:* signs stand for syllables, or some letters and some syllables together. The couplet rhyme in section 8 points this way.
*Check:* controls with a syllable table of the same size, with and without noise.
*Result:* the mixed design (part letters, part syllables, plus some invented signs from reading mistakes) matched about 4 to 5 of 7 summary statistics on the pooled text; a homophonic version (2 to 4 signs per unit) matched 8 of 9 once the X sign is set aside as non-text; but the automatic solver for syllable systems could not read its own control once noise was added, so a solve could not be attempted.
*Verdict:* could not decide at this image quality. This is the family that the data most favour, and the one the images cannot yet test.

### 4. Order tests: does the text behave like a language?

*Assumed:* nothing about the key. Any text in a real language has sequential structure (certain signs tend to follow certain signs), and this survives most kinds of substitution.
*Check:* the same test on enciphered French, English, Portuguese, Latin and others at 15 and up to 25 per cent noise, and a no-language control.
*Result:* for every language control the test saw the language (scores 8.8 to 86 against a threshold of 4.3). Cryptograms 1 and 2 scored 0.39 to 0.91, level with the no-language control, and cryptogram 2 stayed there when we allowed for deleted and inserted signs. On a synthetic copy the test still separated language from non-language at 30 per cent noise (about 82 per cent), but only 66 to 73 per cent at 40 per cent noise, so the finding holds only if the true error on cryptogram 2 is below about 30 per cent. Our estimate is about 17 per cent on agreed signs, and possibly 20 to 30 per cent overall.
*Rules out:* any design that keeps the order of the text (letter or syllable) at the current transcription: a control-backed negative up to roughly 25 per cent noise. It does not exclude designs that scramble order or add filler (see sections 5, 6 and 11). For the shorter verse pages (about 370 signs) the test is too weak to decide.

### 5. Polyalphabetic (periodic), autokey and word codes

*Assumed:* a Vigenere-type shifting alphabet, a key that depends on the preceding text, or a table of about 60 whole words.
*Check:* controls built each way, read by the order tests.
*Result:* each control was read; the real text was not.
*Rules out:* these designs, as control-backed negatives. A running key (a long passage of text used as the key) and scrambling of letters inside words are not excluded; order tests cannot see them.

### 6. Transposition (reading the signs in columns)

*Assumed:* the signs are in the wrong order, for example written in columns.
*Check:* planted transpositions of known height.
*Result:* one possible lead (a column height of 34) appeared at a probability of 0.03 and vanished under a stricter rule for which marks count as signs. Our planted-transposition control failed twice (planted transpositions recovered in only 2-3 of 12, then 9-11 of 12 under a looser rule decided in advance, against a bar of 10 of 12).
*Verdict:* could not decide. We retired this scan as a tool; a different instrument or more text would be needed.

### 7. Masonic ciphers, pigpen and Copiale-type systems

*Assumed:* a lodge-style alphabet, or a Copiale-type system with word symbols.
*Check:* shape counts against pigpen controls and a neighbour test against a Copiale-like control.
*Result:* pigpen-shaped signs make up only 3.8 to 5.2 per cent of the tokens; the word-symbol neighbour test gave p 0.68 while the control passed 5 of 5; the number of distinct pictograms (23 in the 60 lines) is far above what a Copiale-type system uses (8 or fewer). The automatic Copiale solver fails its own control at 8 per cent noise or more.
*Rules out:* pigpen and Copiale-type word symbols for the pictograms (control-backed negative). The automatic solver could not decide.

### 8. X as a word space

*Assumed:* the very frequent X-like sign (about 14 to 16 per cent of the signs) separates words.
*Check:* controls with word spaces.
*Result:* p 0.25 and 0.36 for the real text against 0.000 for the control; the same result when X was removed from the text.
*Rules out:* X as a plain word divider (control-backed negative). The best-fitting model on record treats X as a non-text sign over a homophonic text (8 of 9 statistics without X, none with it); that is a working model, not a reading.

### 9. Cribs: guessing words that must be in the text

*Assumed:* the cipher text contains a known piece of writing.
- *The clear French poem on the cryptogram-3 page.* We tested it against every cryptogram as letters, syllables and words, at 160 sign types and at the coarser level: 0 of 24 combinations cleared. The control (the poem itself enciphered, with 0, 5 and 15 per cent noise) always cleared. Bourdeau's own isomorph test reached the same result with its own control.
- *The Greek poem and the English text on the reverse of cryptogram 4* (an altered copy of Thomas Moore's Anacreon ode, as identified by Sektu and others): 0 of 48 pairings for each of the two renderings (Gaffney's Greek and English), with the planted clear texts recovered at 15 per cent noise.
- *A pool of eight period poems for cryptogram 4*, as a straight copy: the real score was 0.815, which a couplet-shuffled null reaches 66.5 per cent of the time; the controls scored 0.85 to 0.99 and ranked first in 10 of 10 tests.
*Rules out:* the c3 poem, the verso texts and the eight pool poems as contiguous plaintext of any of the cryptograms, letter-level (control-backed negatives). A copy from an author outside the pool, or a patchwork copy, is untested.

### 10. Outside solvers, as recorded

Daniel Bourdeau's cyphersolver repository carries an independent reading of the verse and of cryptogram 2 (MIT-licensed; we use it as a second witness, credited), and his tests against the clear poem. A. Aymeloglu's unsolved-ciphers repository lists the target as open after eleven rounds (cited only). Klaus Schmeh's Cipherbrain posts and Nick Pelling's Cipher Mysteries thread (90 comments) list the cryptograms as unsolved; Sektu (2017) rejected a one-sign-per-syllable French alexandrine and called the nasal-sound idea promising. We found no published reading, and this is a search result, not a statement about novelty.

### 11. Nulls: signs that mean nothing

*Assumed:* a third or more of the signs are meaningless padding, which no order test can see.
*H66:* looking for sign types that behave like padding in cryptogram 2. The control could not beat its own search noise in 0 of 10 runs at one padding share and 2 of 10 at another, so the attempt was a non-test.
*H67:* a more careful version (choose on half the lines, score on the other half). Before running it we checked the best a perfect padding-remover could do on our own synthetic text: it barely cleared a shuffle, so the test would not have been able to see anything.
*Verdict:* untestable at this length and noise. We stopped there rather than keep tuning the same instrument.

## What the data do show

These are the results that held up against their controls. None of them is a reading.

1. **One key across all four pages.** Sign usage correlates between all six pairs of cryptograms as it would for one shared key and not for independent keys; the verse uses the same signs as the prose.
2. **Rhyme at line ends of cryptogram 4.** The last signs of the two lines of a couplet match far more often within couplets than across them (4 to 5 of 9 to 10 couplets within, 0 of 9 across; p 0.0001 on our reading; Bourdeau's reading gives 9 of 10 within, 0 of 9 across). A sign therefore stands for a sound, which fits a syllable-sized unit.
3. **Pictures open lines.** Pictogram signs open lines far more often than chance (p 0.0002).
4. **X avoids line edges** while being spread evenly inside lines.
5. **Clear writing inside cryptogram 2.** The digits 516 and the capital letters H.D.D.L.M.F. appear in ordinary writing on the page. We checked them against the neighbouring signs and set them aside from the sign counts.
6. The 31 numeral-shaped signs inside the cipher scatter like ordinary signs rather than clustering, so they do not look like numbers written out in digits.

## What would move it

The automatic solvers for the likely designs (letter, syllable, Copiale-type) pass their own controls only when transcription error is below roughly 5 to 8 per cent; ours is 15 to 18 per cent on the two longest pages. Every hypothesis that depends on that threshold is waiting on it. Two things would change it. First, sharper images of the original sheets, so that the measured sign error could fall into that range, with our known-answer test rebuilt on those images first. Second, further clear writing in his hand, which would give a reference for letter forms and vocabulary. Until then the cryptograms remain open.

## Summary table

| Approach | Verdict | Deciding number |
|---|---|---|
| Better transcription from public images | Could not decide (images are the limit) | 15.6-17.7 per cent error on known-answer page |
| Letter substitution, French | Ruled out (control-backed negative, current transcription) | real 0 of 8 vs control 5 of 8 |
| Letter substitution, English | Ruled out (same) | real 8th percentile vs control 100 of 100 |
| Letter substitution, Portuguese | Ruled out (same) | real 0 of 24 vs control 4 of 4 |
| Letter substitution, Spanish / Latin | Could not decide (weak controls) | control power 1 of 4 and 2 of 4 |
| Syllable and mixed systems | Could not decide at this image quality | solver fails its own control with noise |
| Order-keeping design of any kind (cryptogram 2) | Ruled out up to about 25 per cent noise | real 0.27-2.56 vs threshold 5.1-5.6 |
| Periodic, autokey, 60-word code | Ruled out (control-backed) | each control read, real not |
| Column transposition | Could not decide | control 2-3, then 9-11 of 12 vs bar 10 |
| Pigpen / Copiale word symbols | Ruled out (control-backed) | pigpen 3.8-5.2 per cent; neighbour p 0.68 vs 5 of 5 |
| X as word space | Ruled out | p 0.25 / 0.36 vs 0.000 |
| Clear French poem as crib | Ruled out as contiguous plaintext | 0 of 24 |
| Greek / English verso texts as crib | Ruled out as contiguous plaintext | 0 of 48 each |
| Eight period poems, cryptogram 4 | Ruled out as contiguous copy | real 0.815; null reaches it 66.5 per cent |
| Nulls / padding (H66, H67) | Could not decide | control 0 of 10 and 2 of 10 |
| One key across the four pages | Positive | all 6 pairs in the shared-key band |
| Rhyme at line ends, cryptogram 4 | Positive | 4-5 of 9-10 within, 0 of 9 across, p 0.0001 |
| Pictures open lines | Positive | p 0.0002 |
