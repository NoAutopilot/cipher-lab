open (low confidence — see "report about a cipher" flag below)

# Waldegrave to Delafaye — TNA SP 78/205/95

QUEUE row: N55 (sources/solver-diffs/2026-09-23-non-decode-hits.tsv, "Candidates not on DECODE").

## Source

The National Archives, Kew, **SP 78/205/95** (State Papers Foreign, France), folio 146, 1734 July 21, Paris.
TNA Discovery full record (fetched 24 Sept 2026 via `tools/discovery_items.py "SP 78" "SP 78/205" cypher
decipher key`, id C7336977): "Folio 146: Waldegrave to Delafaye. **He managed to see a paper carelessly left
on a table by Fleury which was a copy of a letter in cypher from Newcastle to Comte de Marsay revealing
success of French espionage and knowledge of the cypher.**" James, 1st Earl Waldegrave, was British
ambassador in Paris 1730-40; Charles Delafaye was an Under-Secretary of State in London; Cardinal Fleury was
chief minister of France; "Comte de Marsay" is not otherwise identified this pass.

**Flag — likely a "report about a cipher," not ciphertext itself (24 Sept 2026).** The catalogue description
reads as Waldegrave reporting, in plain English, that he saw a French copy of an *English* cipher letter (the
Duke of Newcastle's, Secretary of State, to a "Comte de Marsay") that had fallen into French hands — evidence
that the French had penetrated the English Secretary of State's cipher, not a ciphertext passage inside
Waldegrave's own dispatch. This is the same "report about a cipher, not necessarily the cipher itself" pattern
flagged for N24, N38 and N65 in QUEUE.md (Andrew Stone to Newcastle, 1735, is N65 and reads almost identically:
a plain-English summary of someone else's ciphered letter). Nothing in the QUEUE row or the fuller Discovery
description states that f.146 itself carries untranscribed cipher symbols — the original QUEUE-row summary
("a paper of Cardinal Fleury's left on a table, copied and sent in cipher") is ambiguous on this point and the
fuller record above resolves the ambiguity toward "report," not "ciphertext." **Not resolved without a page
check**; flagged here rather than dropped, per this run's brief (four named targets, no re-scoring). If a
future worker confirms no cipher symbols appear on f.146, this row should be corrected off the board.

## Check-solved sweep (24 September 2026)

1. **Editions.** William Coxe, *Memoirs of the Life and Administration of Sir Robert Walpole ... With
   original correspondence and authentic papers* (3 vols, 1798) is the standard printed correspondence for
   this circle (Walpole, Newcastle, Delafaye, ambassadors including Waldegrave) and was checked by archive.org
   full-text search (`be-api.us.archive.org/fts/v1/search`, ids `bim_eighteenth-century_memoirs-of-the-life-
   and-_coxe-william_1798_{1,2,3}`, one query per volume, >=2s apart). "Marsay": **zero hits in all three
   volumes** — the Newcastle-to-Marsay letter Waldegrave describes is not named anywhere in Coxe. "Waldegrave":
   one hit each in vols 1-3 (index/table-of-contents lines: vol.1 "George Tilson to earl Waldegrave... 1747-8,
   Waldegrave Papers"; vol.2 "Mr. Delafaye to earl Waldegrave" (appendix listing, twice); vol.3 "the earl of
   Waldegrave... Sir Robert Walpole to the earl of Waldegrave"). "Delafaye" in vol.2: one hit, the same
   "Mr. Delafaye to earl Waldegrave" appendix-list line. All of these are letters **from** Delafaye/Walpole
   **to** Waldegrave (instructions sent out), the reverse direction from our target (Waldegrave to Delafaye,
   a report sent in). No hit reproduces or names a 21 July 1734 letter from Waldegrave. Per CLAUDE.md's
   caveat, the fts API's `page_num` field is not a real page locator and a single hit per volume is
   consistent with an index/appendix entry rather than the letter's own text — not an exhaustive read of
   either volume, a partial check.
2. **Sibling search (TNA Discovery, same piece).** The same query that found f.95 also returned its
   immediate neighbour f.94 (1734 July 17, a Paris Gazette newsletter enclosure with no cipher content) — no
   companion key, decipher, or decipherment note found elsewhere in SP 78/205 under cypher/decipher/key
   terms.
3. **Community lists.** Web search (`Waldegrave Delafaye 1734 Fleury cipher letter Hague`) returned only
   unrelated hits (a Royal Historical Society article on the 1729 Treaty of Seville, a Wikipedia
   disambiguation page for the unrelated mathematical "Waldegrave problem," Inria's Charles V cipher story,
   a papal-cipher paper) and four `beta.nationalarchives.gov.uk` catalogue-id links (not fetched — item-level
   Discovery ids, redundant with the direct query above) — nothing naming this letter or a prior
   solve/discussion. No Cryptiana or Cipherbrain hit; local grep of `sources/cryptiana/` for
   "waldegrave"/"delafaye"/"marsay" returned nothing.
4. **DECODE.** No login attempted. `sources/decode/` greped for "Waldegrave"/"Delafaye"/"Fleury"/"Marsay"/
   "SP 78/205": no hits.
5. **Solver repositories.** Both freshly shallow-cloned (24 Sept 2026, shared across this run's four
   targets). `dbourdeau/cyphersolver`: grep for "waldegrave|delafaye|marsay|SP 78/205" across
   `.md/.txt/.csv/.json` returns zero matches. `aaymeloglu/unsolved-ciphers`: zero matches for the same terms.
6. **General web search.** As (3). No result ties a cipher key, a decipherment, or a prior transcription
   to this specific item.

**Host requests this pass:** discovery.nationalarchives.gov.uk 3 (>=3s apart, shared across all four targets
this run), archive.org be-api fts 5 (>=2s apart), WebSearch 1, github.com 1 shallow clone each of both repos
(grepped, shared across all four targets), sources/decode/ and sources/cryptiana/ local greps (no network).

## Verdict

**Status: open, low confidence.** No printed edition (Coxe's Walpole *Memoirs*, the standard correspondence
collection for this exact circle) names or reproduces the Newcastle-to-Marsay letter or this Waldegrave
report; no sibling key found in the piece; no community list, DECODE record, or solver-repository entry
touches this item. But the fuller Discovery description read this pass makes it likely f.146 is Waldegrave
*describing*, in plain English, a French copy of someone else's cipher letter, not carrying ciphertext of
its own — the same failure mode already named for N24/N38/N65. **Do not treat as a nomination-ready
cryptanalysis or recovery target without a page check first** confirming cipher symbols are actually present
on f.146 (see REQUEST.md, which asks for exactly that confirmation alongside the copy).

**Copy status:** no online image located; **copy-order**. See REQUEST.md.
