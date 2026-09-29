# PICTURES -- what each drawing and pictogram class shows, what it could mean, and a test (DEB-SWARM-E, 29 Sept 2026)

Public images only (PAGEMAP.md has the boxes). Candidate meanings are candidates: nothing here is a reading. Tests run
by `pict_tests.py` -> `pict_tests.json` (settled drafts, H31's punctuation filter, 10,000 within-line shuffles; each
statistic can move under the null, rule 3). Grades as PAGEMAP.md.

## Results first

| id | prediction | result | verdict |
|---|---|---|---|
| E1 | drawn vessels (BUCKET x3, PICT-JUG, BOX-M: cups and a jug, eye-checked) close lines | 5 of 5 line-final (band 0-1, p < 0.0001); class control: 2,000 random id sets of 5 tokens reach at most 3, none 5. E1b, PICT-JUG and BOX-M only (1 token each, so H33 could not have picked them): 2 of 2 (p 0.0009) | holds. A second picture class with an edge role: pictures open lines (H31), vessels close them |
| E2 | H31 survives the drawings the drafts miss | 12 of 56 lines picture-initial with the PAGEMAP corrections (band 0-7, p < 0.0001); picture line-final 4 (band 0-7) | holds; +1 line (c2a L04, a serpent/cord drawing coded `_`) |
| E3 | word-initial syllables written as pictures, with X as a word divider: X precedes interior pictures more than chance, follows them no more than chance | X before 3 (band 4-14, mean 8.7, p_le 0.016); X after 10 (band 4-14) | the divider version fails: X *avoids* the slot before a picture, as it avoids line starts and ends (H19). Either pictures are not word-initial, or X is not a divider; the second fits H39 (X non-text) |
| E4 | a repeated picture is a logogram inside recurring phrases: its neighbours repeat | 6 repeated (picture, neighbour) pairs (band 2-10, p 0.51); planted half-strength phrase gives 17 | no recurring phrase; the test could see one |
| E5 | the verse is a line-by-line rendering of the Greek on its verso (his label "Greek translation"): concrete images of a Greek line appear as pictures in the same cipher line | by eye, Schmeh's 1:1 line alignment: arrows are in Greek line 7 (ψυχῆς ὀϊστούς), cipher arrows in lines 10 and 16; lilies and roses in Greek 9, no plant sign in cipher 9 (leaf in 13); crowning in Greek 10, arrow in cipher 10; the only loose fit is a flying figure in cipher 11 beside "queen of the goddesses" (Greek 11) and Wisdom descending (12) | not supported (0 of 3 concrete Greek images in the same line). Qualitative, 13 pictures; not a control-backed negative |
| E6 | the digits 516 are a date: 16 May, his claimed birth day | his autobiography gives "May 16, 1836" (Sektu Part III quoting Farnsworth 2010); the No.9 page shows "516" in clear in L02 and a cube with 6, 1, 5 on three faces above L01 (6 and 1 adjacent, impossible on a real die) | consistent; one coincidence at about 1 in 365 for a random 3-digit month-day, higher since 516 is also a plausible cell, lodge or page number. Grade M; LIFE.md |

## Page drawings (not in-line)

| drawing | page | shows | candidate meanings | testable prediction | status |
|---|---|---|---|---|---|
| ink portrait | c1 | bearded man, bust | himself: Bauer (2017, fig. 5.1, credited to the museum) prints a "self-portrait ... (with cipher)", perhaps this leaf; his beard was shaved on 26 Apr 1883. Caution: four of his portraits of women are copies from *Peterson's Magazine* 1879 (Brown 2021), so a man's portrait may also be copied | if a self-portrait, the same face recurs across his papers; the c2b faint man is probably its show-through, not a second drawing | PAGEMAP: c2b show-through, M |
| bonnet portrait | c2a | figure in plumed bonnet, letters on the shoulder | copied: Brown (2021 plagiarism PDF on Cipherbrain, p.10) traces two head-and-shoulders women to *Peterson's Magazine* Nov 1879 "New style head-dresses, bonnets", one with "OLUMP" (or similar) on the shoulder, which the print does not carry -- our "oLvrip." is that word. So the picture is a copied fashion plate; only the added lettering is his | "OLUMP" is his device: it recurs in his other papers, or it spells something in his languages (Olympe? Olympus -- ΣΟΦΙΗ comes "from Olympus" in Greek line 12 of the verso) | lettering added to CRIBS.tsv; recurrence unchecked (Farnsworth not read) |
| cube 6/1/5, pitcher, tumbler | c2a | a still life above L01 | 516 = 16 May, his claimed birthday (E6); pitcher and tumbler: the same vessels that end lines (E1) | E6 above; the vessel link: cipher vessels end lines on pages with and without the still life (c2a, c2b, c3: yes, all three) | E6 consistent; E1 holds |
| couple walking | c3 | man in top hat, woman in long dress, arm in arm | marriage (8 June 1882); "Oh! mes amis" poem below | none sharper than E5-type content checks | -- |
| owl | c3 | owl on a branch | wisdom (Greek σοφία is the verse's theme word, ΣΟΦΙΗ, Greek line 12); night; jail | if the owl marks wisdom, it sits on the page carrying the verse's theme word: it does not (c3, not c4) | not supported, weak |
| dove with olive sprig | c2b L07 | a dove flying toward the sun | peace; the Noah dove; Odd Fellows dove ("hope and renewal", oddfellowsguide.com) | see the emblem-set row | -- |
| handshake + "L.M.F." | c2b foot | two clasped hands | Farnsworth: the Masonic grip "Boaz" (via Sektu 19 Jul 2017); a bond with a person "L.M.F." (Sektu); L.M.F. also in "H.D.D.L.M.F." (c2a L09): perhaps his initials H.D.D. joined to someone's L.M.F. | L.M.F. are initials of a person in LIFE.md: none of the names found (Wells, Desmarais, Judith, Jenkins, Olcott, Reddington, Patterson, Lemaire) fit L.M.F. | negative on the names at hand; daughters' and visitor's names not found |
| bird with key + banners | c4a | eagle/hawk holding a key (or cross) in its beak; "HENRY.D.DEBOSNYS" above and inverted below | a personal seal ("monographe"); the key = the key to the cipher, the jail key, or Odd Fellows keys; the bird = his name (none of FR aigle, EN eagle, PT águia maps to Debosnys) | the monogram is a rebus of the name: no syllable of Debosnys or Deletnack fits the bird's names | not supported |
| "W" monogram | c4a margin; c2a L16 in-line (PICT-CROWN) | two interlaced chevrons with a small circle below | a personal monogram (H.D.D.? W for Wells? M/W mirror of the "M" and "W" in the line-end cups); a square-and-compasses variant | if it is a signature mark, it sits at a start or end: in c2a L16 it is at position 4 of 32, mid-line; in c4a it is beside the title | mixed |
| church with tower and tree, fence caption | c2a L15 | building with tower beside a palm/willow | a church (marriage; Essex); Lisbon (Belem: Jerónimos tower, palms), his claimed birthplace | a birthplace rebus would sit near other Lisbon/Portugal words; untestable without a key | untested |
| three linked rings, trowel, hammer | c2b L01-L02 | tools and the three links drawn inline | Odd Fellows three links "Friendship, Love, Truth" (oddfellowsguide.com, 20 Jul 2017; en.wikipedia.org/wiki/Odd_Fellows); the trowel and a gavel/hammer are Masonic working tools | see emblem set | -- |

**The emblem set (observation, grade M).** Trowel, hammer, three linked rings, clasped hands, dove with olive sprig,
anchor, heart, sun with a face, stars, eagle, owl, bird with a key, a chevron monogram: most are fraternal emblems of
the time (the three links and the heart are Odd Fellows marks; the trowel and gavel Masonic; the dove, anchor and keys
also appear in Odd Fellows and Rebekah symbolism, oddfellowsguide.com and savethegraveseldorado.org). Farnsworth reads the
handshake as a Masonic grip. Group F owns the Masonic comparison; this is handed to them through the digest.
Prediction: if the in-line pictures are emblems used as emblems (a concept each), they behave as markers of units, not as
letters: rare, positionally marked, no fixed neighbours. That is what E1, E2 and E4 show. It does not say what they mean.

## In-line pictogram classes (H31's 23 ids, plus the ones PAGEMAP adds)

Counts are settled-draft tokens (h31_pictograms.json census). "initial/final" = line-initial/line-final tokens.

| class | n | init/final | shows (eye, pict_boxes.tsv) | FR / EN / PT words; rebus syllables | person or event (LIFE.md) | testable prediction | result |
|---|---|---|---|---|---|---|---|
| SUN | 9 | 3/0 (+1 after the dove, c2b L07) | sun with a face and rays | soleil (so-, sol-), sun (sun/son), sol (PT, Latin) | -- | if SUN = syllable so/sol/sun at word start, it opens lines and follows boundary signs | opens lines (H31/H33 p 0.009); X-before depleted (E3) |
| STAR | 10 | 0/1 | an asterisk "*" more than a drawn star | étoile, star, estrela; or a punctuation or null mark | -- | if STAR is punctuation, not a picture, dropping it from the class raises H31's effect size | not run (H31 already significant; it only dilutes) |
| PICT-TREE | 5 | 0/0 | small tree / bush | arbre, tree, árvore; acacia sprig (Masonic) | -- | a word-initial syllable would open some lines: 0 of 5 | against word-initial for this class |
| PICT-ARROW | 5 | 0/2 | arrow, "->", one ">" | flèche, arrow, seta; "see next" | the c3 page's "next page" arrow | if ARROW is a continuation mark, it ends lines or pages: 2 of 5 final, c2b L09 last sign of cryptogram 2 | partly |
| PICT-LEAF | 4 (one is the trowel) | 2/0 | leaf / sprig | feuille, leaf, folha; laurel | -- | -- | opener (H33 p 0.008) |
| PICT-FACE | 4 | 0/0 | small face or moon-like disc | visage, face, cara; moon; all-seeing eye | -- | -- | -- |
| PICT-ANCHOR | 2 (+1 MULTI) | 2/0 | anchor | ancre, anchor, âncora; hope (espérance) | his yacht; the Arctic | -- | opener |
| PICT-HORSE | 2 | 0/0 | horse (c1 with a standing figure) | cheval, horse, cavalo | the drive of 1 Aug 1882 (horse and wagon) | -- | -- |
| PICT-RUNNER | 2 | 1/0 | running or flying figure | coureur, runner; a flying spirit | escape | -- | opener once |
| PICT-HOUSE | 2 | 1/0 | house | maison, house, casa | her farm; the jail | -- | -- |
| RAM | 2 | 0/0 | a horned "ɤ" glyph like the zodiac sign of Aries | bélier, ram, carneiro; Aries (21 Mar - 19 Apr) | 16 May is Taurus, not Aries | if a zodiac sign marks his birth month it would be Taurus (♉): the glyph's horns fit either | undecided by eye |
| PICT-CROSSED | 2 | 0/0 | crossed sticks/tools | croix; crossed keys or hammers | -- | -- | -- |
| PICT-HEART | 1 | 1/0 | heart | coeur, heart, coração | the c3 poem "mon coeur" | -- | opener |
| PICT-EAGLE | 1 | 1/0 | spread eagle or sheaf | aigle, eagle | the monogram bird | -- | opener |
| vessels: BUCKET, PICT-JUG, BOX-M | 5 | 0/5 | cups (empty, with W, with M, with c/E), a jug | verre (FR, homophone of vers "verse, line"), coupe, cup, copo | the still life on c2a | E1 | holds (5/5) |
| singletons | 1 each | -- | bottle, barrel, fish, glass/cart, crown (= W monogram), bird, figure, D-arrow | -- | -- | too few for a test | -- |
| added by PAGEMAP | -- | -- | wavy serpent/cord (c2a L04 start), bird in flight (c2a L10), church (c2a L15), hammer and three rings (c2b L02), dove (c2b L07), anchor coded MULTI (c2a L17) | -- | -- | E2 | included |

## Signs that recur outside the cryptograms

- The anchor: in-line (c2a L15, c2a L17, verse line 14) and tattooed on his body, "an anchor with a coiled cable", with
  two crossed French tricolour flags and a sabre scar on the right knuckles (*A Garvey Family*, 1989, Google Books
  snippet, via this pass's writings search) -- the one cryptogram picture with a sourced occurrence outside the leaves.
- The "W" chevron monogram: c4a left margin beside the title (and its show-through on the verso) and in-line in c2a L16.
- The bird: monogram bird with key (c4a head); PICT-EAGLE (c2a L03), PICT-BIRD (c2a L17), the flying bird (c2a L10).
- Vessels: the pitcher and tumbler of the c2a still life; line-end cups on c2a, c2b, c3.
- "L.M.F.": clear capitals at c2a L09 (after H.D.D.) and beside the handshake on c2b.
- Digits: the cube's 6/1/5 and the clear "516" (c2a).
No public occurrence outside the leaves was found for the owl, dove, trowel, three links, bird-with-key or W monogram
(search result, not absence: Farnsworth's full reproductions were not read). WRITINGS.tsv lists what public print describes.

## The copying habit (context for every group, from WRITINGS.tsv)

Almost every clear English poem of his that Farnsworth printed is copied or patched from Thomas Moore, Stoddart,
Chivers or Colesworthy (Brown 2021); the Greek on the verso is Moore's; the Latin lines are Virgil and the Vulgate; the
women's portraits are *Peterson's* plates; autobiography passages come from *Boston Lyceum* 1827, the NY Times of 12 Feb
1882 and Julian Hawthorne. Two things do not come from print: his "Portuguese" (not readable as Portuguese, Sektu 2017)
and additions such as "OLUMP" and the dates on his poems. Prediction for the solving groups: the cipher's plaintext is
more likely a copied published text (Moore first) than his own composition -- Bourdeau's Moore and Delille tests were at
chance on his transcription, so the copy, if any, is from a source not yet tried. The clear French poem on c3 ("Oh! mes
amis ...") has no source found by Brown or by this pass.
