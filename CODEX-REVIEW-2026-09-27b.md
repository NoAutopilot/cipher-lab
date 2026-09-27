**Cipher-lab: five questions for making discoveries compound (follow-up to CODEX-REVIEW-2026-09-27.md)**

Prepared by ChatGPT/Codex · 27 September 2026 · pasted by the owner into the ytbiz parent session at about 14:30 UTC and filed here by parent 7m so both accounts can read it. The owner's question was "wdyt?"; the parent's answer is in STATUS.md's 14:3x line and in the chat. Nothing in this file is a decision.

---

Yes. My earlier answers focused too much on making the existing process more reliable. You're asking how to make it discover substantially more.

My strongest hypothesis is that the next major improvement will come from making discoveries compound across documents. Your Nassau work already hints at this: one useful relationship between letters can unlock more than another long attack on an isolated ciphertext.

I would organize the research around five questions.

1. Where could one discovery unlock twenty letters?

A difficult cipher and a valuable research target are not necessarily the same thing. For your stated goal, a moderately difficult key used across a neglected correspondence could be enormously valuable.

I would explicitly search for collections with shared cryptographic structure:

* Repeated symbol inventories across different letters.
* The same secretary or diplomatic office using related keys.
* Partly deciphered correspondence with unread siblings.
* Key books whose intended correspondence has not been identified.
* Collections where editions print cleartext but omit cipher passages.

Then prioritize the expected number of documents unlocked by resolving the shared obstacle.

Your existing crossmatcher is a start, but exact key reuse is only one relationship. The more ambitious problem is recognizing that two keys are related despite changed numbers, additions to the nomenclature, or a different handwritten symbol set. Those relationships need testing, not assuming.

What I can contribute: compare many candidate relationships, formulate specific transformation hypotheses, write the tests, and check whether the resulting mappings predict untouched passages. A successful connection becomes an asset for the entire collection.

2. Are the best targets even labelled as unsolved ciphers?

Searching catalogues for "cipher" inherits the cataloguer's knowledge and mistakes.

The Mary Stuart discovery is a useful precedent: researchers found and deciphered more than fifty previously unidentified letters in the BnF. Discovery and attribution were themselves major parts of the achievement.

I would test systematic reconnaissance of digitized volumes surrounding promising material, including correspondence catalogued under broad or uncertain descriptions. Look for cipher passages, attached keys, decipherments on facing pages, and repeated hands.

This should begin with a bounded experiment: inspect a few hundred neighboring pages, manually check a sample of pages the system rejected, and measure whether it finds worthwhile material missed by catalogue searches.

What I can contribute: inexpensive initial inspection, multilingual catalogue reconciliation, and connecting scattered clues. The opportunity is making a large amount of previously uneconomic archival searching practical. It still depends on accessible images and careful identification.

3. What missing document would make a hard cipher easy?

Before spending another large block of computation, I would ask what external evidence could collapse the problem:

* A recipient's deciphered copy.
* A sender's draft.
* A duplicate dispatch in another archive.
* An enclosure quoted in subsequent correspondence.
* A key filed under a secretary's name.
* A published translation whose original cipher was never identified.

This is broader than checking whether a translation already exists. A known plaintext can be the bridge to a key that unlocks genuinely unpublished siblings.

The ambitious version is to search for correspondence relationships across archives using dates, routes, aliases, diplomatic events, message structure, and partial textual matches. DECRYPT already supplies thousands of ciphertexts and keys, alongside historical language resources; there is substantial existing infrastructure to build upon.

What I can contribute: keep these different kinds of evidence in play together and turn a vague historical possibility into a ranked, testable search. Sometimes the highest-value next action will be obtaining one scan.

4. Can we solve the handwriting and the cipher together?

This is the technical bet I find most interesting.

A conventional sequence commits to a transcription and then solves it. But an ambiguous mark might be distinguishable only because one interpretation works consistently across several encrypted letters.

Imagine a glyph with three plausible visual readings. Each implies a different key constraint. Across thirty occurrences, two interpretations create contradictions; one predicts sensible text in a separate letter. That provides evidence for revisiting the glyph.

I would build an experiment that retains competing readings and jointly evaluates:

* Whether the symbols fit the images.
* Whether the proposed key behaves consistently.
* Whether the language fits the period.
* Whether the interpretation predicts unseen material.

The important safeguard is preserving the original visual evidence: a fluent sentence cannot simply authorize rewriting the transcription.

There is already research demonstrating learned decipherment from symbol recurrence patterns, including results on historical homophonic ciphers. That establishes a useful starting point, although it does not establish that the full joint system I'm proposing will work on your material.

What I can contribute: design and implement a small prototype, construct controlled examples, and compare it against your current process. This is a research hypothesis worth testing, not a capability I should pretend we already possess.

5. Are we searching over the right explanations?

A thousand attempts under the wrong cipher model can produce very little information.

For each stubborn target, I would maintain a small set of genuinely different explanations: mixed alphabet and nomenclature, variable-length groups, meaningful marks, changing keys, an unexpected language, or incorrect segmentation.

Each explanation should carry a prediction and a cheap experiment capable of weakening it.

For example, if a mark is cryptographically meaningful, separating marked and unmarked symbols should improve consistent decoding on withheld passages. If that never happens, we should reduce confidence in that explanation.

This is where I would take inspiration from the Navier-Stokes effort you mentioned: design the research so that intermediate discoveries change what gets tried next. The transferable idea is disciplined exploration and reuse of useful results. More attempts become valuable when they explore meaningfully different possibilities.

What is newly practical with me is the speed of that whole loop: historical research, explicit hypothesis, custom software, experiment, inspection, revised hypothesis. Those activities previously required considerable coordination between different specialties. I can help connect them, while specialists and original sources remain important where the evidence is difficult.

For the next month, I would make three concrete bets:

| Bet | Experiment | Evidence that it deserves expansion |
|---|---|---|
| Discover a productive collection | Search neighboring volumes around one strong existing family | Previously untracked cipher letters with credible shared structure |
| Make one solution propagate | Use a partly solved family to predict a sibling whose reading is withheld | Correct recovery beyond what the current process achieves |
| Recover information lost during transcription | Compare joint interpretation with fixed transcription on difficult passages | More independently confirmed symbols and plaintext without more false readings |

I would choose Nassau as a provisional starting point for the propagation experiment, because your own results already demonstrate useful relationships there. Salviati is a candidate for the joint-interpretation experiment, but I would first prove the method on material with known answers.

The ambition I would set is to make the next successful decipherment unlock a collection, and make that collection improve our ability to tackle the next one. Your project has pieces of this already. The missing demonstration is that they can produce that compounding effect.
