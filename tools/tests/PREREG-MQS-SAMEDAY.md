# PREREG-MQS-SAMEDAY (9 Oct 2026, LANE MQS next, account 4)

Written and pushed before any control is scored (CLAUDE.md rule 3). Tool: `tools/sameday.py` (added; no existing tool ranks
shared phrases between a partial reading and the sender's dated letters near a date -- research/MARY-STUART-TALK-2026-10-09.tsv
row M46). Idea: Lasry, Biermann and Tomokiyo 2023 (Cryptologia 47:2) p.125 (a letter dated by its overlap with a letter to
Beaton), p.136 n.97, p.137 n.100 ("striking thematic overlap and even some of the same wording").

## Input and statistic

A partial reading (words, `?` or `_` marks an unread word; unread words break phrases) and a letters TSV (id, date
YYYY-MM-DD, recipient, text). Phrases are word trigrams with all three words read, not made only of stopwords. Weight of a
trigram = log((N+1)/(df+1)), df = letters containing it. Window score W(d) = sum of weights of distinct reading trigrams
found in any letter dated within +-7 days of d (the item itself excluded).
- **Option A (dating evidence)**: rank of a date among all distinct letter dates by W(d).
- **Option B (crib candidates, graded I)**: for a shared trigram followed in the reading by an unread word, propose the
  word that follows the trigram in the window letters (most frequent).

## Known answer (same design, length and language as the intended use)

Corpus: Martin (ed.) 1836, *Despatches ... of the Marquess Wellesley* Vols 1-2, IA OCR already on disk
(`ciphers/mornington-1798/print/35304_djvu.txt`, `35315_djvu.txt`; clear print only, no reading or key of that target is
used or changed). Letters parsed by their "No. <roman>." heading; a letter is the sender's when its heading line names
"Mornington to" or "Wellesley to"; date from the first parseable date in the next three lines; body up to the next
heading. Kept: sender letters with >= 120 body words. Held-out items: every kept letter with at least one other kept
letter within +-7 days, at most 60 drawn by `random.Random(0)`. Partial reading: the first 300 body words, each kept
with p = 0.5 (`random.Random(1000 + i)`), the rest `?` -- a half-read letter of Mary-Stuart length, English.

## Gates (both computed, both gated; 20 shuffles each)

- **A**: share of held-out items whose true date ranks in the top 10% of candidate dates (average rank on ties).
  Null A: dates permuted among the corpus letters (`random.Random(s)`, s = 1..20); the item keeps its true date as the
  answer. Expected null about 0.10. Gate A: real >= 0.30 AND real > null p95.
  Why the null can differ: permuting dates changes which letters sit in the true date's window; the text is fixed, so
  W at the true date moves only if date proximity carries shared wording.
- **B**: precision = proposals equal to the hidden true word (case-folded) / proposals, true-date window. Null B: the
  same proposals from the window under each date shuffle. Gate B: real >= 0.30 AND real > null p95 AND >= 30 real
  proposals. Why the null can differ: proposals come from different letters under a shuffle; formulaic phrases
  ("I have the honour") will propose correctly in both, so the gate measures what the date window adds.
- Ceiling check: if null B >= 0.95 the control has no headroom and B is graded weak whatever the margin.

A gate missed ships the option `weak` with both numbers; nothing is run on a target from it.
