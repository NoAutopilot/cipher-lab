# How the September 2026 solvers work, and what to copy

Read from three public repositories on 19 September 2026:

| Repo | Owner | Commit | What it is |
|---|---|---|---|
| github.com/dbourdeau/cyphersolver | Daniel Bourdeau | shallow clone, 19 Sept 2026 | 99 target folders, about 45 items solved, read or partly read since 14 Sept 2026. Code MIT, text CC BY 4.0. |
| github.com/aaymeloglu/unsolved-ciphers | Andrew Aymeloglu | 837075e | 8 targets, a shared solver package (cipherkit), a catalogue sweep of DECODE, BNE and PARES. No licence file, so cite it, do not copy code from it. |
| github.com/robertpitt/forster-cipher | Robert Pitt | shallow clone | One target (Forster 1644), decoder plus tests. MIT. |

Both of the big repos say plainly that the work is done by Claude Fable 5.1 in Claude Code (Aymeloglu also uses Codex), with a person checking. Bourdeau calls his "an informal benchmark of a frontier AI on historically unsolved ciphers". That is the single most important fact about the current wave: the tooling is the same tooling we have. What separates a solve from a negative is target choice, archival legwork, and discipline about controls.

## 1. Almost nothing fell to pure cryptanalysis

Sorting Bourdeau's and Aymeloglu's finished items by what actually broke them:

| Route | Share | Examples |
|---|---|---|
| A printed key or table that nobody had applied to a printed ciphertext | large | Catinat 1691 (Bazeries' 1893 table on the 1819 Mémoires, 12,362 groups), Hesse 1603 (Rommel's own 1846 key on his 1840 figures), Gramont 1529, Sormano 1529, Pelissier 1592, Raince 1526, Norfolk 1570 (all Lasry or Tomokiyo keys published as images, never used) |
| The key was in the archive beside the letter | large | Yard 1699 (Manchester papers at Yale), Windischgrätz 1720 (DECODE R5017/R5018), Bordeaux 1653 (the English Deciphering Branch's own key sheet, DECODE R7537), Morosini 1588 (Meister 1906), Ottobon 1589 ("Ziffra prima", DECODE R1789), Starhemberg 1758 (1752 tables) |
| The plaintext was already in print and the lists were stale | common | Richelieu 1629 (Avenel 1858), Davison 1584 (CSP Scotland), Worcester 1526 (State Papers Henry VIII), du Bellay 1529 (Le Grand 1688), Adrian 1521 (Danvila 1899), Michell 1751, Matthias 1482, Barney 1863 (Reddit, Aug 2026) |
| A sibling letter with a contemporary decipherment, so the key is an alignment problem | common | Vich 1511, Sessa 1524, Soria 1523 key B, Balbases 1677, Affry 1757, Kauderbach 1754, Ferdinand 1635 (Aymeloglu), Lanssac 1573, Béthune 1601, Conti 1649 no. 43 |
| Genuine ciphertext-only break | about a dozen | Ségur 1585 (mod-5 test revealed an alphabetical syllabary), Lucca 1644 (polyphonic figures), Warsaw 1627 (alphabet in plain order), Richelieu 1629, Soglia 1848, Toledo 1565 (two clear-text cribs), Sun Yat-sen 1916 (brute force over 57,600 condenser keys), Lorraine 1592, Soria 1523 key A, Ormonde-Maltravers 1634, Forster 1644, Vande Perre 1653, Moray 1568 (partial) |

Every genuine break was a short homophonic or nomenclator system that had one of: visible word boundaries, cribs from surrounding clear text, or a structural regularity (alphabetical figure order, blocks of five, a separator digit). None was a large nomenclator attacked from a single letter.

Aymeloglu's shortlist states the same thing as a rule: "Pattern across every real solve 2015-2026: the break was identifying the system or finding the key or plaintext in an archive, with hill-climbing software to finish. Pure cryptanalysis of the ciphertext alone almost never did it."

## 2. The workflow, step by step

### Search before you solve
Both repos have a mandatory "is it really unsolved" step, and both got burned before adopting it. Aymeloglu's order: the cipher's name in a search engine, then the sender's printed Lettres or Correspondance on the Internet Archive, then the calendars and state-paper series, then the comment thread of the list post, then DECODE and the archive catalogue. Six of Bourdeau's first targets were already solved in the open. Tomokiyo's list lags weeks to years behind.

### Get the image, not the transcription
Transcription errors sank several ciphertext-only attacks and were only found on the page:
- Bordeaux 1653: 21 corrections; two different signs had been merged as "d". The solver was right about the design and still failed until the transcription was fixed.
- Birago 1571: Tomokiyo's inline "+" signs are superscript crosses over the following digits, a fourth diacritic class.
- Raince 1526: reading Tomokiyo's published key image by eye put l, m and n one column off. Re-measured by pixel position, it worked.
- Moray 1568: Tomokiyo's transcription conflates two glyphs under one label. Aymeloglu re-transcribed from the DECODE page image and measured the word gaps, which is what made the partial reading possible.

Practical access notes from their folders: Gallica IIIF serves full-resolution images if you send a browser User-Agent (`curl -A "Mozilla/5.0"`), with 1-2 s between fetches. PARES serves only about 915 px JPEGs, so crop and upscale. The British Library viewer has been offline since the 2023 cyber attack, so anything only in BL is blocked. DECODE (de-crypt.org) needs a free login for images; Bourdeau's organisation blocked account creation, so some of his items are parked on that alone.

### Look for the sibling
The most productive single move in both repos: find another letter in the same key that has a contemporary decipherment (interlinear, marginal, a minute in clear, a duplicate, a "copie du n° précédent"). Then the key is recovered by alignment, not search: anchor on repeated words, run an EM or hard-EM aligner, hold out one letter to check. Bourdeau's "sweep the whole volume" habit (Ségur: 440 canvases, one unlisted cipher leaf found; fr. 16127: 20 Mondoucet letters found) comes from this.

### Structure before search
Every ciphertext-only success started with a structural observation made by hand:
- Ségur: the upper figures fall into blocks of five (mod-5 residues 60/30/22/20/14), so the syllable table is ordered. The annealer was then designed around that constraint.
- Toledo 1565: figures 12-43 in plain alphabetical order. Two cribs fixed eleven letters and the order predicted the rest (f=21, x=41, y=42, z=43), each then confirmed on a word.
- Warsaw 1627: odd figures a-m, even figures n-z.
- Soglia 1848: 92 of 102 runs are even length, so 5 is a separator; 8 never in second place, so it is a 64-cell table plus an 8XXX code.
- Lucca 1644: one doubled pair in 231 letters of Italian, where ll tt ss run at 3-4%, so not a one-to-one substitution. It was polyphonic (17 = i or n, 19 = t or s).
- Kauderbach 1754: nulls found by phase statistics in an unseparated digit stream.
- Vatican 5: bias-corrected mutual information across a candidate digit shows 4 is a word separator.

Cheap tests to run first on any numeric cipher: digit-width histogram, index of coincidence per symbol class, doubled-pair rate against the language's expected rate, parity and position statistics per digit, frequency correlation between two letters suspected to share a key.

### The solver
Both repos converge on the same design: simulated annealing over a symbol-to-letter map, scored by a period-correct character 4- or 5-gram model, with a dictionary or segmentation bonus, frequency-ranked initialisation, several seeds, and a greedy climb to finish. Temperatures scale with text length. Nothing exotic.

Two things that mattered more than the algorithm:
- **Word boundaries.** Forster 1644 (207 tokens, 34 symbols): n-gram hill climbing produced vowel soup. A beam search over a lexicon, constrained only by same-symbol-same-letter and allowing long words to be skipped, gave most of the key in one run. Moray 1568 read only after the gaps were measured off the page and scored chunk by chunk.
- **A period-correct corpus.** French with u for v and i for j, and spellings like estoit, roy, luy, ie. Aymeloglu's cipherkit builds one corpus per language from Internet Archive documentary editions (Henri IV's Lettres missives, Avenel's Richelieu, Thurloe, Nicholas Papers) plus Gutenberg prose of the right century. Without the folding, controls pass and the target fails.

Bourdeau's Lorraine 1592 note has a warning worth keeping: an annealer that recovered only 37-56% of letters on known-key controls was replaced by steepest ascent that recovers 98-99%, and two traps were closed: unrestricted nulls let the search delete every hard position and beat real French, and selecting on raw score picks a degenerate all-e key.

### Controls, always
This is the discipline that separates these repos from hobbyist claims:
- **Matched control.** Before saying a target resists, encipher a synthetic text of the same length, alphabet size, symbol count, cipher design and language, and run the same solver. "Reads 5 of 6 matched 134-letter controls but not the target" is a result. "The annealer found nothing" is not.
- **Permutation tests.** Key-shuffle z (is this key better than a relabelling of the same glyphs?) and token-shuffle z (is the order of the text informative under this key?). They answer different questions and are not comparable.
- **Grades per token.** H read from a key source, C from known plaintext, S cryptanalytic with a control, M uncertain, I inferred or repaired. Every reading page gives the counts. A reading with no H or C is labelled a cryptanalytic result.
- **Null tests on the search itself.** Lorraine 1592: run the same search on shuffled ciphertexts with the same symbols and frequencies, score blind on distinct French words of six or more letters. The manuscript gave 33, five nulls gave 0-3.

### Verify against the world, not the model
The checks they trust are external: a spelled name that also stands in clear on the same page (Lorraine 1592, "chasteau" twice in cipher beside Chasteauvillain in clear); a decipherment that names a real person absent from the clear text (Toledo 1565, "Mosiur de Lenni" is Andrea Provana di Leinì); clause-by-clause agreement with a printed dispatch about the same events (Ormonde-Maltravers against Knowler 1739); alphabetical-rank consistency for code words in a one-part code (Soglia).

### Write it down
One folder per target. A NOTES.md with sources and links, what is established, what is inferred, the failure log, grade counts, and which corpus the model came from. Absolute dates, never "recently". A status vocabulary: solved, partial, open, closed-negative, found-solved, blocked. The ciphertext as transcribed is never silently repaired; proposed repairs live in their own file. A decode.py or verify.py that reproduces the reading from transcription plus key and exits non-zero if the committed reading is stale.

## 3. What the failures teach

Bourdeau's closed-negative and offline-only lists are as useful as his solves. The blockers fall into four kinds:

| Blocker | Items | What would move them |
|---|---|---|
| Below unicity distance | SP53/22 f.52 (84 tokens), Ormond-Arran 1678 (about 20 groups), Le Tellier 1657, du Croc 1567 (147 tokens, 40 symbols), Thurloe pieces b-d | Only a key or a sibling in the same key |
| Large nomenclator, one letter | d'Estaing 1779 (217 tokens of a 600-entry code), Chaulnes 1690 (300 groups, 116 distinct; the annealer recovers 4-12% of a matched control), Berthier 1812 (about 1,200 entries, 64% hapax), Stepney 1702 (24 groups), Maurice-Rupert 1645 (93 groups, max 398), Colbert 1674-75 (106 figures, probably a word nomenclator) | Archive copy of the decipherment or the key. All located; none online |
| Transcription-limited | Lorraine 1592 (a quarter of glyph identifications wrong), Sega 1593 (CNN reads 3 in 4 glyphs), Béthune 1601 (decoder already above the transcription's oracle bound), Esp. 318 no. 95 | Better images or human palaeography |
| Access blocked | Anything in BL (offline since 2023), DECODE images without a login, fr. 3633 (not digitised), Vilcoq 1969 (not digitised; sole source for Berthier and Marmont), Torcy and Villars 1710 (Tomokiyo's transcription links are dead) | A login, a reader's copy, an interlibrary loan, or an email to Tomokiyo |

Two specific results overturn entries in our own catalogue and are worth knowing cold:
- SP53/16 nos. 78 and 79 are symbol ciphers in Tomokiyo's glyph-label notation, not numeric ciphers. Bourdeau's third session built a solver that reads clean 507-token controls with 130 symbols, and no. 78 still shows no language basin in English, French, Latin, Italian or Spanish. The earlier claim that the two share a key was withdrawn. A design with 8% nulls plus word signs is not readable at this length, so that remains possible.
- Hyde's superscriptions are not a cipher. The 1724 editor of Barwick's Life says they were numbers "signifying nothing, only to puzzle the Enemy."

## 4. Tooling worth reusing

From Aymeloglu's cipherkit (read it for design, do not copy: no licence): normalize (folds before accent stripping), lm (CharLM, WordLM, backoff), segment (score a letter string by its best split into corpus words), anneal (with fixed values, bijective option, restarts), controls (matched_control, permutation_z, permutation_z_key, key_recovery), align (known plaintext to key, with conflicts reported), transcribe (deskew, line strips, gap detection, two-pass compare, consensus, review page), grades, corpora (per-language recipes with a versioned cleaner).

From Bourdeau (MIT): a shared `lang/` registry so no target grows its own lm.py; per-target decode scripts; `armstrong/pencil_score.py` for finding annotated microfilm frames; the Gallica IIIF fetch pattern; the catalogue harvest scripts for DECODE.

What we should adopt in cipher-lab now:
1. The H/C/S/M/I grades and the matched-control rule, as written policy in ciphers/README.md.
2. A per-language period corpus before any solver run. Aymeloglu lists the exact Internet Archive and Gutenberg sources per language.
3. A verify script per cipher folder once anything is claimed.
4. The status vocabulary and absolute dates in every NOTES.md.

## 23 September 2026: neighbouring records, and the pace of the competition

- Randolph to Sussex, July 1570 (Caligula C II f.277) went on the board as a cryptanalysis candidate with a printed paraphrase as crib. The contemporary decipherment was on the next leaf, f.278, a separate DECODE record (R4932) with status Decrypted. DECODE's own "key record" pointer (R4930) was wrong, which is why two passes missed it. Before any campaign: open every DECODE record with the same shelfmark, and read the calendar entry's source note (Boyd wrote "partly in cipher, deciphered").
- dbourdeau/cyphersolver read that item on 21 Sept, Charles I to Rupert 1645 on 21 Sept and most of Harley 287 on 21-22 Sept. A catalogue clone from 19 Sept was stale within two days. Re-clone both solver repositories immediately before promoting or solving anything, and again before a verifier writes an N-class.
- Same day: the Sforza-Maino 1446 pair, the one cryptanalysis candidate reachable with the network blocked, was attacked jointly with a matched control built first. The control read at 99%; the target did not move. That negative is worth having because both numbers exist (rule 3). The joint nomenclator annealer and the 15th-century Italian model are now in tools/ for the next Italian chancery target, and the cheapest reopening is an image, not more annealing.
- Same evening: the neighbour-record sweep of the cached DECODE catalogue looked like a lane that scales (202 pairs). Excluding by volume as well as by id, Bourdeau's repository already names 193 of them. A catalogue that a daily-active project also reads is not a lane; the differentiator is material that is not on DECODE (Gallica, BL, TNA, NRS, county and private archives) or the full catalogue behind the login, not the public scrape.
- 23 Sept 2026, TNA Discovery: the search-results description omits a separate item-detail note field; three of five SP 90/2 items carry 'Partly in cipher' only there. Every TNA sweep pulls item details for each hit, not only search results. And the non-DECODE catalogue lane worked: of the first fifteen scored rows, seven are verified unsolved at stage 2 with copy routes, against one of ten for the DECODE-neighbour lane.
- 23 Sept 2026, 19:25 UTC: the orchestrator's timestamps drifted from the real clock by up to eight hours and its briefs told workers the date was 23 September; forty files carried the wrong date until the commit log exposed it. Rule 6 now says read `date -u` first. Git commit times are the record when a timestamp is in doubt.

## 23 September 2026, evening: what produced results

- Two lanes produced stage-2 targets with the material in hand and no order: digitised manuscripts found by catalogue notes with the leaf viewed (Gallica: Dupuy 452, Dupuy 468), and printed ciphertext found by a numeral-run detector over Internet Archive full text (24 passages from 274 editions, one whose 1836 editor says he could not read it). Neither depends on a catalogue saying "cipher" in the way the solver projects search.
- Dupuy 468: the catalogue's bracketed attribution (Anhalt, 1515/16) was wrong, and the solver's edition search followed it. The verifier caught it from the decoded text ("ego filius ... Luneburg", "ego Joachimus"). Test the attribution against the plaintext before the edition search, and treat a catalogue's square brackets as a hypothesis.
- A decipherment on the leaf makes the reading a recovery and rules out "first" wording even at N3; the honest product is a transcription of the old decipherment plus what its key reads beyond it.
- Same night, Dupuy 468: verified N3, then found in print two hours later by an adversarial second audit, in the Reichstagsakten volume the first verifier had excluded after re-dating the letter to 1518/19 (it is 24 Jan 1520, and the senders it inferred were right). Two rules follow. A verifier's own re-dating or re-attribution widens the edition search to every volume within two years of every plausible date; it never narrows it. And nothing above N1 is called a result until a second, adversarial session has tried to find it in print, which is now gate 2 in CLAUDE.md's Outreach rule. Cost of the whole Dupuy 468 chain: about $65 for a contribution (the Latin cipher original identified for a printed letter, the catalogue's date and senders corrected).
