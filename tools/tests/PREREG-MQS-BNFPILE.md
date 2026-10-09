# PREREG-MQS-BNFPILE (written 9 Oct 2026 before any control ran; `tools/bnf_findingaid.py --pile`)

Written before the scorer was run on the labelled sample, the planted pile or the null. The scorer's rules (bare item,
key sheet, neighbour trap, est_signs constant) were built on fr.2988 and on the saved notices of
`sources/bnf-findingaids/2026-10-07/` and `sources/bnf-aem/`; those notices are therefore the **development set** and
every number below is a regression/reproduction number there, not evidence of power on unseen volumes.

## C1 Reproduction (fr.2988 is the calibration item, not a known answer)
Expected: fr.2988 has bare = 26 (next saved notice at most 3), est_signs = 67,600, prior_work names the Bibliographie
citation, neighbour trap set, open_bare = 0 once volume-level prior work is applied, open_named = 2 (Ranzo f.2, f.9).
Gate: all of these exact. Why it can fail: change the bare rule or the prior-work parse and the numbers move. It shows
only that the code reproduces the prototype.

## C2 Hand-labelled sample (the real measure)
`tools/tests/data/bnf_pile_labels.tsv`: 54 cipher-bearing items, none from fr.2988, labelled by reading the item text
(bare / named / deciphered / key sheet) before the scorer ran on them. Stratum "random": 40 items drawn with
`random.Random(20261009)` from the 487 cipher-bearing items of the other saved notices (sorted by (title, no, text),
shuffled, first 40). The random stratum holds **no bare item and no key sheet**, so it cannot measure either; stratum
"stratum2" is the 14 cipher items that are short (<60 characters) or carry table/clef/alphabet/précédent words, and is
hand-labelled the same way (5 bare, 5 key sheet, the rest named). Stratum 2 was chosen by a loose filter that is not the
scorer, but I had seen the notices while building the scorer: its numbers are development-set numbers.
Label counts: bare 5, key sheet 5, deciphered 22, named 22.
Gates (precision AND recall): bare >= 0.80/0.80, key sheet >= 0.80/0.80, deciphered >= 0.95/0.95. Expected misses I
already know of, not hidden: `« Chiffre de 13043 »` (fr.3974-3995 no.32, a key sheet, has guillemets so reads as
named). Why it can fail differently from the reproduction: it scores items the rules were never tuned item-by-item
against, with labels that are mine, and a rule that only "knows" fr.2988 misses these.
A sample with 5 positives cannot license a power claim: report the counts, not a rate alone.

## C3 Held-out known pile
Look in `sources/decode/` and `sources/cryptiana/web/` for a volume listed as cipher letters catalogued without names
that is not fr.2988 and not a development notice, with its notice on disk. If none: log "no held-out pile; ranking
untested". Expected: none on disk.

## C4 Null whose pass is not guaranteed: planted pile
Plant a synthetic 10-item bare pile (item texts "Pièce en chiffre.", folios every 4, no names/dates/places) into the
fr.3251 notice (which has none), score the whole saved set + fr.2988 with prior work applied. Gate: the planted
volume ranks in the top 5 by open_bare. Why it can fail: the scorer ranks by count of open bare items after the
prior-work and neighbour rules; a planted pile covered by a spurious volume-level or portal prior hit, or classified
named by the place-name proxy, drops out. Not at ceiling: the control volume is a real notice, not a toy.
Sanity line only (cannot fail, rule 3): the old item-text shuffle across all notices. A within-volume shuffle of item
order does not change bare counts either; the within-fonds variant is reported beside it if cheap.

## C5 Shelf grade
`--pile` ships at most `weak` (one calibration point) until a second, independently found pile is scored, whatever
C2 returns. `PILE_MIN` = 5 open bare items for class `pile` is set here, before the sample ran.
