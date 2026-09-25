# powers-1991 cheap test 1: print check + open-index scholarship pass

25 Sept 2026, LANE B2 worker bPOW (session_01XY737yPNqrjbduLQ7cCZNi).

## thefreelibrary.com (Thomas 2006 article, direct fetch)

`curl -A "cipher-lab research script (contact via repository)" https://www.thefreelibrary.com/Deciphering+the+code+in+Richard+Powers%27s+The+Gold+Bug+Variations.-a0159331538`
-> HTTP 403 (one attempt, per the good-citizen single-retry rule; not retried). ASKS/JSTOR-QUEUE row added below for an
owner-machine fetch of the full text.

## Open-index scholarship pass

**OpenAlex** (`Authorization: Bearer $OPENALEX_KEY`), 3 queries, >=1.5s apart:
- `Gold Bug Variations dedication cryptogram` -> 3 hits: J. T. Thomas 2006 "Deciphering the Code in Richard
  Powers's the Gold Bug Variations" (*Notes on Contemporary Literature*, OpenAlex W337305991); Shawn Rosenheim
  1997 *The Cryptographic Imagination* (book, not this article); Ottum 2005 on Poe.
- `Richard Powers Gold Bug Variations code` -> 576 hits, top relevant: the same Thomas 2006 record, plus Herman
  (1998) "Genetic Coding and Aesthetic Clues" (a different article from the Herman & Lernout piece Thomas cites).
- `Deciphering the code in Richard Powers` -> 7961 hits (mostly unrelated biomedical "deciphering" papers), same
  Thomas 2006 record at position 4.

**Full record pulled** (OpenAlex `works/W337305991`, no rate-limit issue, has an indexed abstract): Thomas, J. T.
(2006), "Deciphering the Code in Richard Powers's the Gold Bug Variations," *Notes on Contemporary Literature*
36:3. OpenAlex's abstract_inverted_index reconstructs to substantial running text (reproduced below, reflowed
from the inverted index, so word order past a certain point may show minor artifacts):

> As a preface to *The Gold Bug Variations*, this codon-like string of letters not only mirrors the genetic
> sequencing found throughout the narrative; it also troubles the unsuspecting reader... Is there a hidden,
> encoded message? If so, can it be deciphered using the coding techniques found throughout *Gold Bug*? Or is
> this cryptogram something else entirely? Although Luc Herman and Geert Lernout refer to these thirty-two
> letter groupings as a "motto" (*Mosaic* 31.4 [Dec. 1998]: 162), it seems more realistic to assume that these
> four lines function as an acknowledgements page... Herman and Lernout... suggest that the clue to this
> arrangement lies in the last two triplets, which represent the initials of Johann Sebastian Bach and of
> Bach's motto: Semper Dei Gloria. "The triplets do not contain coded information. Instead, the letters may
> well be the initials of sixty-three different names, of which Bach's is the last. The proliferation of P's in
> the final position may be explained by the presence, in the potential list of initials, of [several] of
> Richard Powers, and the question marks probably represent unknown middle [names]" (162). I am not exactly
> sure how Herman and Lernout arrived at the number sixty-three, instead of thirty-two... four of Powers's
> seven other novels... contain dedications to different personages (Marcel Proust, Anne Jardin, T. E.
> Lawrence, and Emily Dickinson...), suggesting Powers might have done the same with this text. Furthermore, a
> closer investigation into the family-members hypothesis proves fruitful. In his *Understanding Richard
> Powers*, Joseph Dewey names Powers's parents and explains that Powers was the fourth of five children, two
> older sisters and a brother and one younger brother, and that he spent... five "eye-opening" years in
> Thailand when his father accepted an appointment with the International School of Bangkok...

The abstract cuts off there (OpenAlex indexes abstracts, not full text). It does **not** give a full triplet-by-
triplet key or name list for all 32 groups -- it discusses the initials hypothesis, credits it to **Herman &
Lernout, "Genetic Randomness or Genetic Determinism? Moving Away from the Genome in Richard Powers's The Gold
Bug Variations," Mosaic 31.4 (Dec. 1998): p.162** (not Stefan Wagner's 2015 Cipherbrain comment, which is 17
years later and apparently re-derives the same idea independently), then extends it with a family-members
hypothesis (parents, four siblings) that it says "proves fruitful" but does not spell out beyond the abstract's
cutoff.

**Semantic Scholar** (`x-api-key: $S2_KEY`), 2 queries, >=1.5s apart:
- `Gold Bug Variations dedication cryptogram` -> 2 hits, same Thomas 2006 paper plus an unrelated 2017 Orfeo
  article.
- `Deciphering code Richard Powers Gold Bug Variations` -> 30 hits, same Thomas 2006 paper at top, rest are
  general Gold Bug Variations literary criticism (genome/DNA themes), none claiming a cryptogram solution.

**Crossref**, 1 query (`Deciphering the code in Richard Powers Gold Bug Variations`, 5 rows): 5 literary-
criticism articles on the novel's genome themes, none is the Thomas 2006 piece itself (Crossref does not appear
to have it indexed under that query) and none claims to solve the cryptogram.

## Verdict on this test

Not found-solved: no source read gives a full 32-triplet decipherment. What the pass establishes in print,
independent of thefreelibrary's inaccessible full text: the "initials" hypothesis has TWO known print sources,
not one -- Herman & Lernout, *Mosaic* 31.4 (Dec. 1998), p.162 (earliest found), and Thomas 2006, which extends
it with an unresolved "family members" sub-hypothesis (parents + 4 siblings) that the abstract says "proves
fruitful" without stating the result. Bruce Kallick's 2017 Cipherbrain comment already named Thomas 2006 (see
`sources/schmeh/posts/22-powers.txt` line 220) but not the earlier Herman & Lernout 1998 piece; the spec's
`hypothesis_on_record` field credits only Stefan Wagner's 2015 blog comment, which is now known to be neither
the earliest nor the only print source. This is a search result, not a novelty classification (rule 10); a
verifier should read the full Thomas 2006 and Herman & Lernout 1998 texts (both need the owner's machine or a
library gateway; see the queue row below) before any claim about what is or is not already worked out in print.

## Owner-machine queue row

Neither full text is reachable from the cloud. Added to `JSTOR-QUEUE.tsv`-style handling: see ASKS.md /
LOCAL-QUEUE.tsv entry for:
1. thefreelibrary.com Thomas 2006 full text (403 to the cloud).
2. Herman, Luc, and Geert Lernout. "Genetic Randomness or Genetic Determinism? Moving Away from the Genome in
   Richard Powers's The Gold Bug Variations." *Mosaic* 31.4 (Dec. 1998): 149-164. (JSTOR-hosted journal, not
   reachable from the cloud per the Access playbook.)

## Hosts / requests this test

thefreelibrary.com: 1 (403, not retried). api.openalex.org: 4 (3 search + 1 record fetch, key header, >=1.5s
apart). api.semanticscholar.org: 2 (key header, >=1.5s apart). api.crossref.org: 1. No Gallica, no Google
Books, no de-crypt.org. No subagents.
