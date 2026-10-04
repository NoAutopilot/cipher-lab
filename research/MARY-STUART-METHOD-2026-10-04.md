# The Mary Stuart method, read in full, and what it means for our work (research note, 4 Oct 2026)

Source: G. Lasry, N. Biermann and S. Tomokiyo, "Deciphering Mary Stuart's lost letters from 1578-1584", *Cryptologia*
47:2 (2023), pp. 101-202, doi 10.1080/01611194.2022.2160677, Open Access, CC BY-NC-ND. The owner supplied the PDF
on 4 Oct 2026, because the publisher answers 403 to the cloud. It is kept unmodified at
`sources/papers/lasry-biermann-tomokiyo-2023-mary-stuart.pdf`. Read in full by the account-3 orchestrator on
4 Oct 2026, about 14:40-15:00 UTC:
- sections 3 (Sources), 4.1-4.9 (Deciphering the letters) and 7 (Conclusion);
- Appendices A (codebreaking algorithm) and B (enciphering errors);
- the Acknowledgments.

Sections 5-6 (the letters' content) were skimmed only. Page numbers below are the journal's. Credit: every method
here is the authors' (CLAUDE.md rule 8). Tomokiyo is a co-author, and he recommended Armstrong 1808 to us
(CONTRIBUTIONS.md row 28).

## 1. What they actually did, step by step

The scale: more than 150,000 symbols in 57 letters, all in one cipher, 219 distinct symbol types (p. 110, 112).
Each step below is listed with where it is described.

| # | Step | What they did, in their words where it matters | Where |
|---|---|---|---|
| 1 | **Transcription by people, in a GUI, with arbitrary labels** | No OCR ("not applicable"). They used the CrypTool 2 transcription tool. Each symbol is boxed with the mouse and "assigned to specific symbol types (at this stage we did not know yet the meaning of those types, so we assigned them some arbitrary numbers)". Parts of the material were transcribed by the DECRYPT team (Tudor, Milioni, Megyesi). | p. 110, 112; Ack. p. 201 |
| 2 | **Variant marks are transcribed as separate types from the start** | "symbols with diacritics [captured] separately from the same symbols without them", because contemporary ciphers led them to expect the marks to change meaning. | p. 112 |
| 3 | **The transcription is revised by the decipherment** | At first they took `/` and `)` to be stand-alone symbols. "After progressing with codebreaking and decipherment ... we recognized them as diacritics as well and corrected our transcription database accordingly." | p. 112 n. 48 |
| 4 | **Iterative, not staged** | "We first transcribed a few documents, recovered some parts of the key, then transcribed additional documents, recovered more parts, and so on, rather than fully completing one step before starting the next one." | p. 110-111 |
| 5 | **Language by trial** | Italian, the language of the neighbouring documents, gave "no meaningful results". French gave a tentative decryption with recognisable words and fragments. | p. 112-115 |
| 6 | **Confirm fragments, then re-run on the rest** | They "marked those plausible fragments in the GUI tool, confirming the assignments of the homophone symbols that form those fragments, which now appear in capital letters". Then they "focus on the unconfirmed symbols". | p. 115 |
| 7 | **Special symbols found from context** | A repeat-previous symbol, from SVRLAR IVE PROCHAINE read as "sur l'arrivee prochaine". A delete-previous symbol, from MAV IS IR ERE read as MAUVISSIERE. Both were kept as hypotheses until other passages confirmed them. | p. 115 |
| 8 | **Structural partition before the solver** | They excluded every symbol with a diacritic from the homophone candidates, on the expectation that marked symbols are nomenclature. This gave "significantly fewer sequences that do not make sense". | p. 115-118 |
| 9 | **The machine does the alphabet only** | Simulated annealing recovers only which symbols stand for single letters. "Nomenclature symbols representing common words, parts of words, names, or places need to be recovered manually." | App. A p. 197 |
| 10 | **Nomenclature by "crossword" with an "avalanche effect"** | One symbol after L'ARRIVEE PROCHAINE is guessed as DE, then checked at every other occurrence (DECA etc.). Suffixes are read the same way (ANT, EST, ENT, ION, ON) from ADV_AGE, AVT_, R_ABLISSEM_. Each hypothesis is "tested ... and discard[ed]" in the GUI. | p. 118-122 |
| 11 | **Names from history** | One symbol is "my brother-in-law" whose arrival in England is expected, so it is the Duke of Anjou. This step only became possible "after we had made significant progress" and knew the writer. | p. 122 |
| 12 | **Plaintext copies from printed editions** | Several deciphered letters matched letters already printed (Labanoff 1844 and others). These copies confirmed names and common words. | p. 110, 122 n. 54, 124 |
| 13 | **Months by a deduction chain** | Six months came from plaintext copies. May came from "the anniversary of Mary's escape from Lochleven" (2 May). June, October, November and December came from letter cross-references and dated events. January came from a thematic match with a dated letter to Beaton. | p. 124-125 |
| 14 | **Comparison with sibling ciphers** | The reconstructed table resembles Mary's cipher with Chateauneuf (TNA SP 52/22/22) and a cipher in Castelnau's papers (BnF 500 Colbert 472 p. 347). The two share diacritics and nomenclature vocabulary. | p. 128-130 |
| 15 | **Enciphering errors explained, not tolerated** | Some letters had errors of "up to a few %", and "many of those errors were systematic". Most were *cross-cipher contamination*: the secretary, enciphering letters to Beaton with another key the same day, used the Beaton key's symbol for c, i, e or r. "Only after we understood this ... could numerous obscure passages ... be finally deciphered." The secretary's own on-page corrections (deletion symbol, crossing out, overwriting) are evidence for this. | App. B p. 198-200 |
| 16 | **Score function** | 5-grams from 16th-17th-century French Gutenberg texts, computed without spaces. The score is S = Σ N_g log F_g / Σ N_c²: the 5-gram log-likelihood divided by the sum of squared letter counts. The search is simulated annealing that swaps two symbols or reassigns one. | App. A p. 195-197 |
| 17 | **Known limits** | Some gaps come from "low quality of the scans"; physical inspection might fill them. | p. 191 |

**What the paper does NOT contain.** It reports no per-sign transcription error rate, no double keying or inter-reader
agreement, and no control or null in our rule-3 sense. Correctness rests on readable French, on plaintext copies in
print, and on internal consistency across about 57 letters. This settles the open question in
`research/TRANSCRIPTION-PRACTICE-2026-10-04.md`, "Not reached". Their transcription accuracy came from **people
labelling symbols and then correcting the labels through the decipherment**, not from a measured reading pipeline.

## 2. Set against our pipeline

| Their step | Ours | Gap |
|---|---|---|
| 1-2. People box symbols and give them arbitrary labels | Machine line reads. The owner's sign sorter is the human step (piles = arbitrary types) | **The sorter is their method.** On Birago 1572 the owner's piles beat the machines in 98 of 108 adjudicated disagreements (BIR-ADJ, 4 Oct). Our machine-side additions have now failed four times on the same eval item: TX-VIEWS FAIL, TX-AGREEAUDIT NON-TEST, TX-ALTS not adopted, TX-SHEET FAIL (0.077 vs 0.069, fixed 16 / broken 22). |
| 3-4. Decipherment corrects the transcription, iteratively | We transcribe blind to a measured error (TRANSCRIPTION.md), then decode. The key-constrained lattice decode exists but raised error at lam 1 | **The real difference.** We forbid the decode from touching labels, to keep the reading blind and testable. They let it, and accepted no error figure. A middle way: blind first; then a *declared* non-blind crossword pass that may change only M/U-graded signs and grades what it changes S or M (never H/C), with a held-out known-answer check (no.87) of how often it is right. |
| 6. Confirm fragments, re-run the rest | `homophonic.py` takes `fixed=`. RUN5-C1161RA ("M-sign re-anneal with C/S held") is this step | Tried once: its planted control recovered 0/3. Its own diagnosis was that the word-cover stage "drove all free signs to i". See the next row. |
| 16. Score with Σ N_c² in the denominator | Our scorers are add-k 4-gram log-likelihoods with no such term | **A concrete, cheap fix.** Dividing by Σ N_c² penalises a key that piles many symbols onto one letter: a degenerate key raises Σ N_c² sharply. That is the C1161RA failure ("all free signs to i"). It is a different instrument from C1161RA's own, so rule 3's third-attempt clause does not close it. |
| 8. Structural partition before the solver | Families model code+mark (`cm`) and nomenclator designs; marked or dotted signs are labelled separately | Check that every unkeyed homophonic run excludes marked or dotted symbols from the letter candidates when the design suggests it. Salviati (code+mark) and es132 (dot sign) are the obvious cases. |
| 12-13. Plaintext copies; dated-event deduction | Colbert copies (Pisany: 3 known-answer PASSes on 4 Oct); Gachard and Labanoff-type editions in check-solved | Already ours. Pisany is the closest case to theirs. |
| 14-15. Sibling ciphers; cross-cipher contamination | `key_crossmatch.py` matches whole ciphers. The code-by-code contamination check is named in LESSONS-LASRY.md section 3 item 8 for matignon-mayenne-1586 only | **Untried on the targets where it fits best** (section 3 below). |
| 1 (scale). One key, 150,000 symbols | The pools rule (CLAUDE.md pipeline 3, 25 Sept) | Same lesson. Their machine stage worked because it had about 57 letters in one key. |

## 3. What this means for specific targets

**Armstrong to Madison, 20 Feb 1808 (Tomokiyo's recommendation).** The paper's machine stage recovers only
single-letter homophones (App. A p. 197). Every word, name and syllable symbol was recovered by hand, *after*
enough text read to give context (p. 118-124). It was confirmed by plaintext copies found in print (p. 122 n. 54) and
by sibling tables (p. 128-130). Armstrong's letter is a pure word-and-syllable code: it has **no homophone stage at
all**. Every group is nomenclature in their sense. So on their own method the letter cannot be opened by a solver
from 369 groups. That is what our three solver attempts found (ARM-C1, H27, H73: "the objective, not the search, rules
out the reading at this N"). Their route for such symbols has three inputs:
- a plaintext copy of the letter (Armstrong's own letterbook or a Madison or State Department clear copy);
- more letters in the same code (volume);
- sibling tables for vocabulary and construction.

Those are the open owner-side and outreach items already on the board:
- ASKS 83: LOC Erving finding aid.
- ASKS 97: Monroe Papers catalogue.
- The NYHS and NYPL letters, waiting on address confirmation.
- The FDR Library, already sent.

*Interpretation:* on Armstrong, the paper's method points away from more cryptanalysis and toward finding the
material. The cheapest move there is the owner's two 5-minute browser look-ups.

**Birago 1572 (Nevers).** Birago's correspondence with Nevers ran through several keys in close succession:
- the Ceppo-Nevers key (1570-71);
- a numerical key (late 1571);
- the Nevers-Birago 1572 key.

Whether one clerk used two of them on the same day is not established. That is weaker than Mary Stuart's same-day
packets, so treat this as a hypothesis to test, not a likely cause. No.73 and no.85 carry 14 and 11 "off-sheet"
signs, which are not in the 1572 table. They also have two
conflicts: T95 l against T50 s, and the curled "Ce" (X_CE) that TX-SHEET found misread as T50. **Untried test:** for
each off-sheet or conflicting sign, look up the same glyph in the Ceppo-Nevers key and check whether *that* value
fits its context better than chance. Use a shuffled-glyph null, which can differ from the target on this statistic.
Script only, about $3.

**Pisany 1586-87.** RUN4/RUN5 logged a "T31 table-vs-page conflict": two shapes, one table cell. Run the same
contamination check against any other key of the Rome embassy on file (KEY-OFFICES.tsv).

**Vivonne 1572-73.** N7-VIV54Q found a key cell Tomokiyo's table has but our key.tsv omitted ("to z" = col-u row-3).
Run the same contamination check against the other Spanish-embassy keys of 1572-74 before calling any U-label
unreadable.

**Clairambault 1161.** Re-run the C/S-held re-anneal (step 6) with the Σ N_c² denominator, behind the same planted
control that C1161RA failed. That is a different instrument, not a fourth try of the same one.

## 4. Proposed actions, ranked (none run by this note)

1. **Owner, 10 minutes: ASKS 83 and 97** (Armstrong material). This is the paper's route for a pure code.
2. **BIR-CCE, about $3, script only:** the cross-cipher contamination test on Birago 1572's off-sheet and conflict
   signs against the Ceppo-Nevers key, pre-registered with a shuffled-glyph null.
3. **SCORE-NC2, about $3:** add a `--norm nc2` option to the homophonic scorer (Usage 8: option, help text, offline test).
   Re-run C1161RA's planted control with it. Run the target arm only if the control passes.
4. **TX-CROSSWORD, about $6:** the declared non-blind correction pass on no.87 (M/U signs only, graded S/M). Measure on the
   held-out known answer how often a decode-driven label change is right before it is used anywhere.
5. Rule change for the parent (not applied): add to TRANSCRIPTION.md that a person's sort is the field's own
   transcription method (this paper, p. 112). The sorter is the primary route on a symbol hand once machine
   additions have failed their benchmark.

Credit: Lasry, Biermann and Tomokiyo 2023. No reading in this repository changes because of this note, and nothing
here makes any claim about novelty (rule 10).
