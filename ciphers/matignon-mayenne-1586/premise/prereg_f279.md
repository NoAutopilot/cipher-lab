# Pre-registration: does fr.15572 ff.279-280 (period clear text) carry f.276's text? (A2P4-MATIG, 3 Oct 2026)

Written and pushed before any read of ff.279-280 beyond the one first line the Premise check (GF4-BATCH5) already
read at 1600 px. Brief: `.claude/briefs/runs/2026-10-03-acct2-a2p4-matig.md`. Script: `premise/match_f279.py`
(written after this file; implements exactly the rule below).

## Crib (target)
Tomokiyo, `sources/cryptiana/web/henryiii.htm` (Matignon's Cipher-3): f.276 "can be read as something like
'La Guiolle est en doubte du pu pour les amis de la Roussiere sont et grand nombre avec lu....'" -- a modern
paraphrase, grade M. Content words (M = 5, fixed now): **doubte, amis, roussiere, grand, nombre**.
"La Guiolle" is left out of the gate (it is the secondary question); "pu" is left out (uncertain in Tomokiyo).

## Text under test
Our transcription of ff.279-280 clear text (f.279r first; f.280r only if f.279r does not carry the match; plus
f.279v/f.280 rectos/versos that the manifest shows carry text, as far as the 4-vision-call budget reaches). Every
page actually read is listed in the result; a page not read is named as not read.

## Normalisation (both sides, one convention)
Lower case; accents stripped; u->v merged (u/v), j->i, y->i; non-letters dropped; doubled letters collapsed
(ss->s, ll->l); an apostrophe splits tokens. Unreadable tokens ([?]) are kept as a wildcard that matches nothing.

## Match rule
A crib word matches a text token when the normalised Levenshtein distance <= 1 for words of <= 5 letters, <= 2 for
longer words. Score = the largest number of the M crib words found **in crib order** inside any window of 60
consecutive text tokens (longest in-order subsequence, greedy over window starts, exact DP).
**Gate: score >= 4 of 5 = MATCH. Score <= 3 = NO MATCH.**

## Controls (must all score below the gate, i.e. <= 3, for a NO MATCH or MATCH to count)
- C1 crib-swap (same text, other cribs, same rule, 5 content words each, fixed now):
  - f.143 (Tomokiyo, Cipher-1): laisse, entendre, voulloit, partir, malcontant
  - f.111 (Tomokiyo): villeroi, verres, lettre, fais, roi
  - f.260 (Tomokiyo, St. Luc): arriva, hier, olleron, matin, venu
  If any C1 control reaches >= 4, the rule does not discriminate on this text: result NON-TEST, whatever the
  target scores.
- C2 text-swap (same f.276 crib, a clear passage known not to decipher f.276): Tomokiyo's f.282 margin
  transcription (an HTML comment in henryiii.htm, lines "l'arme sera emploie ... envo[i]e de deca", on disk).
  Must score <= 3.
- C3 positive control (the rule can fire): the f.276 crib string itself, respelled with one edit per word
  ("doute", "amys", "Rousiere", "grant", "nonbre"), embedded in the C2 text, must score 5.
The controls differ from the target on the statistic by construction-free means: a different crib or a
different text changes which tokens can match, so each can score anywhere 0-5.

## Secondary, descriptive only (no gate)
List every token of ff.279-280 within distance 2 of: guiolle, aiguillon, eguillon, roussiere, fontenai, poudre.
Report them with position; say whether "La Guiolle" plausibly = Aiguillon (interpretation, not a result).

## Vision budget
2 blind Sonnet reads of the f.279r line crops (one crop batch each) + 1 reconciliation + 1 spare; crops via
`tools/iiif_lines.py` (command pasted in NOTES.md before the first call); never a full leaf.
