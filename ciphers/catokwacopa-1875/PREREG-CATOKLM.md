# PREREG-CATOKLM -- phrase-level LM search on the five unread lines (6 Oct 2026, worker R13-CATOKLM, account 2)

Committed and pushed before any control or target statistic below is computed. Script: `catoklm.py` (our own code; the
fit model and the positional prior are David Bourdeau's, cyphersolver targets/catokwacopa `search.py`, MIT, read not
copied; the trie/edge search is catok23.py's, imported unmodified). Step named by NOTES.md Verdict and QUEUE.md row 18.
Line numbers are Bourdeau's (pairs.tsv column 1): 9, 12, 23, 26, 29 = Ernst [9], [11], [22], [25], [28].

## Why a new instrument
R12-CATOK23 retired unigram exact-fit for these lines (control 0/100 unique; rule 3 third-attempt clause). This is a
different instrument: the scorer is a word-bigram LM plus a positional prior, so a reading is ranked as a phrase, not a
bag of words. Search space and fit model are unchanged so the only difference is the scorer.

## Corpus (era-matched; `en` not used)
`tools/data/en/README.md` records LANG_CORPORA["en"] (Holmes 1892 + Moby-Dick 1851, extended) as of unknown reliability
(per-fold spread 0.44-0.64), and it is a judge corpus, not a search LM. Used instead: the ten 1853-1875 Project Gutenberg
novels already on disk as catok23_stream.txt.gz (Tom Brown at Oxford, Verdant Green x2, Middlemarch, Bleak House,
Barchester Towers, Our Mutual Friend, The Way We Live Now, Great Expectations, A Tale of Two Cities) -- English prose of
the ads' own decades, with two Oxford-undergraduate novels matching the published readings' register (Conington, Jowett,
lectures). **Held out:** the last 10% of tokens of each novel are excluded from the LM and the vocabulary and are the only
source of control phrases (no leakage of planted phrases into the model).

## Instrument
- Candidate space: every word sequence over V (training words with count >= 3, plus 'a', 'i'; one-letter words otherwise
  out) that fits the line exactly under the published model: an order-preserving interleaving of A (8 May) and B (20 May)
  is a subsequence of the reading; <= 4 omitted letters per word, <= 12 per line. No misprints. No names list.
- Score: sum over words of [log P_bigram(w | previous word) + log prior(source of w's first letter) - 2.3 x omitted
  letters]. Bigram: absolute discounting D = 0.75 backed off to the unigram; first word unigram. Prior: Bourdeau's
  (consonant initial A .92 / B .04 / omitted .04; vowel initial A .35 / B .45 / omitted .20), scored as the best source
  available at the word's start position.
- Search: k-best beam over (i, j) stream positions, 80 partial readings per node, top 20 distinct word sequences kept.
- **Unique** iff score(top1) - score(top2) >= 3.0 nats (as R12-CATOK23).

## Synthetic control (matched; run first, per line)
Per target line, 20 synthetic lines (seed 1875 + line number): a window of consecutive words from a random position in
the held-out 10%, all words in V, letter count L+3..L+12 (L = |A|+|B| of that line). The design as the prior models it:
word-initial letters dropped at the prior's omitted rate, the remaining excess dropped uniformly from non-initial
letters; surviving word-initial letters go to A/B in the prior's ratio, other letters by a fair coin; rejection-sampled
until |A| equals the target line's |A| exactly (so |A|, |B| and L match the target line). These are real period phrases
of the same lengths under the same cipher design. Statistics: unique rate, correct-unique rate R_c (unique and top1 is
the planted word sequence), wrong-unique rate W_c, planted-in-top-20 rate, and (descriptive, no gate) mean top1 word
recovery (LCS of word sequences / planted words).

## Gate (stated recovery rate)
A line's control meets the gate iff **R_c >= 0.50 and W_c <= 0.10**. Only then is that target line scored:
unique -> grade S for its words (control-backed); not unique -> "control-backed: not forced by this instrument".
If the control is below the gate, the target line is **not scored** and is logged "CONTROL BELOW GATE: untestable by
this instrument at this N" (rule 3; not a negative). Thresholds are not tuned after seeing any result.

## Caveat registered in advance
The control assumes W.'s split follows Bourdeau's prior (fitted on seven undisputed lines); a split habit unlike it is
not represented. Bigram LMs trained on ~1.6M words are weak on rare phrases; a control failure says the instrument
cannot pick out a period phrase at these lengths, not that the lines have no reading.
