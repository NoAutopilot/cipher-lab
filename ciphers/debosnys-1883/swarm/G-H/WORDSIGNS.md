# Group H, task 3: signs for whole words

DEB-SWARM-H, 29 Sept 2026. Scripts: `logogram_test.py` (`logogram_copiale.json`), `neighbour_test.py`
(`neighbour_test.json`). Public copies only: the settled drafts c1, c2 and c3/c4.

## What the Copiale's word symbols look like (known answer)

In the Copiale the eight large symbols "appear to be logograms, standing for the names of (doubly secret) people and
organizations" ([K11] s.5; e.g. the lodge, the master, the apprentice grade). Measured on the whole public
transcription (1,771 lines, 455 logogram tokens):

| statistic | Copiale logograms | null / comparison |
|---|---|---|
| lines opened by a logogram | 21 | within-line shuffles: median 12, p99 20 (p 0.006) |
| lines closed by a logogram | 14 | median 12 (p 0.29) |
| neighbours that are word-space signs (before / after) | 0.74 / 0.72 | letter signs: 0.21 / 0.20 |

So the Copiale's own word symbols open lines only 1.75x chance. Their strong signature is that they **stand between
word spaces**, like a word.

## The blind test, controlled at Debosnys's size and event count

A blind version that needs no space class: G statistic of the neighbour tokens' sign types against the global sign
curve (a word symbol's neighbours pile up on the few space signs), null = the same number of anchor tokens at random
non-candidate positions, 2000 draws.

| text | anchors | G | null median | null p99 | p |
|---|---|---|---|---|---|
| Copiale, 5 windows each holding 60 logograms (5-14k tokens) | 60 | 285-332 | 81-85 | 110-115 | <0.0005 in 5/5 |
| Copiale, 5 windows of 1,184 tokens, logograms removed, 51-56 whole words replaced by word symbols on Debosnys's pictogram count curve (23 types) | 51-56 | 291-334 | ~80 | 101-110 | <0.0005 in 5/5 |
| **Debosnys, all four settled drafts (1,184 tokens), H31's pictogram class (PICT-*, SUN, STAR, HEART, RAM)** | 60 | **103.9** | 109.0 | 137.6 | **0.68** |

The test reads the Copiale design every time at Debosnys's size and event count. Debosnys's pictograms do not have
it: their neighbours are ordinary signs at ordinary rates (X flanks them 12 times against 13.0 expected; the most
over-represented flankers, CROSS-T 5 vs 1.5 and LOOP-STEM 5 vs 1.3, are single-digit counts). Grade S.

**Reading:** a Copiale-type design (word symbols set between word-space signs) is excluded for the pictograms,
with a control that passes. Not excluded: pictograms as word symbols in text **without** a space class, and
pictograms as rebus syllables (the runner's open idea), which this test cannot see. H31's line-initial excess (11 of 56
lines, p 0.0002, 3.7x chance) is much stronger than anything the Copiale's word symbols show (1.75x), so the
Copiale gives no precedent for it; a verse-initial or capital-letter role fits it better than a word role.

## Candidates to name (for group E and the merge; nothing here is read)

If the pictograms are words or rebus syllables, the testable ones are those that recur: STAR 10, SUN 9, PICT-TREE 5,
PICT-ARROW 5, PICT-FACE 4, PICT-LEAF 4, and the pairs HORSE, RUNNER, HOUSE, CROSSED, ANCHOR, RAM (2 each). Their
names in his languages (for example SUN: sol / soleil / sun; STAR: estrela / étoile / star; TREE: árvore / arbre /
tree; ANCHOR: âncora / ancre / anchor) give word-initial rebus syllables that group E's PICTURES.md can test
against the letter that follows each pictogram. A Copiale-style test of that needs a reading of the following
letters, which no group has yet.
