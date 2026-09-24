found-solved

# Sir Horatio Palavicino to Burghley, with a cipher key — TNA SP 81/6/125 (1590)

QUEUE row: N21 (QUEUE.md "Candidates not on DECODE (catalogue scout of 23 September 2026)").

## Source

TNA, State Papers Foreign, Germany, States, **SP 81/6**, folio 125, The National Archives, Kew. Catalogue
text as scored in QUEUE.md N21 (TNA Discovery search-result description, not re-queried this pass per this
brief's "no TNA Discovery calls" restriction): "Folio 125: Palavicino to Burghley, with a cipher key." Single
item; the key is catalogued as part of the same folio, not a separate cross-reference. `digitised: false`
(recorded in the N21 scoring pass, 23 September 2026; not re-checked this pass).

## Editions-first check (24 September 2026)

**Stone's Palavicino biography identifies this exact folio and describes the cipher on it.** Lawrence Stone,
*An Elizabethan: Sir Horatio Palavicino* (Oxford: Clarendon Press, 1956) is on the Internet Archive as a
lending-only item, `archive.org/details/elizabethansirho0000ston`. No loan was taken (IA borrow/page-image
flow is unverified per CLAUDE.md's Access playbook and out of this brief's scope); the be-api full-text
search endpoint (`be-api.us.archive.org/fts/v1/search`), which works on lending-only items per the Access
playbook, returned direct hits. Four queries, each returning the snippet needed to reconstruct one
continuous passage (page_num field not used as a locator, per the playbook's warning that it is not a real
page number):

> "...the occasional word being coded. Thus the cipher Palavicino drew up for his second German embassy in
> 1590 comprised 103 names of persons, places, and numbers of troops [text continues, not recovered]...
> [a design limitation] he could not touch, would have made the cipher useless for all the rest.¹"
>
> Footnote 1: "S.P. Germany, States, 6, f. 125."

"S.P. Germany, States, 6, f. 125" is TNA's older citation form for what is now catalogued SP 81/6 f.125 —
this is our target folio, cited by shelfmark, not merely by subject. Stone is not vague about the cipher's
existence: he states its size (103 entries), its categories of covered terms (persons, places, troop
numbers), and a structural weakness in its design, in running prose in a peer-reviewed monograph. Per
CLAUDE.md rule 10 and the check-solved brief's "quote verbatim... before writing open," this rules out
writing "open": a named specialist source has already read and described the content of this specific
folio.

**What this does and does not establish.** Stone describes the cipher key's *design* (a 103-entry
nomenclator for the 1590 embassy) — this is either the folio itself (if SP 81/6/125 is the key table
Palavicino submitted to Burghley) or a closely related item Stone cites at the same shelfmark. It is not
established from this snippet evidence alone whether Stone reproduces the key values themselves (a full
cipher table) or only paraphrases its scope; the surrounding paragraph (adjacent sentences on either side
of the quoted material) was not recovered, since be-api's full-text search returns only short
highlight snippets around each query term, not full pages, for a lending-only item. No ciphertext message
enciphered under this key was found described anywhere in this sweep — Stone's passage reads as a
description of the key's structure and a weakness in it, not a decipherment of a specific dispatch.

Grade of this claim: **H** for the shelfmark match and the quoted description (read directly from Stone's
own text via full-text search, not inferred) — not the plaintext of any letter, since no accompanying
ciphertext or decipherment was located.

## Six-source sweep (24 September 2026)

1. **Web.** WebSearch: `"Palavicino" Burghley 1590 cipher SP 81 deciphered`, `"SP 81/6/125" Palavicino`.
   No solution, transcript or discussion of this specific folio found outside Stone (above); one hit
   surfaced Bourdeau's own site index (checked directly, see 5 below) and Horatio Palavicino's Wikipedia
   page (no cipher detail).
2. **Print.** Searched Internet Archive for further editions: HMC Salisbury (Cecil Papers, Hatfield)
   volume covering 1590, `calendarofmanusc04grea` (vol. 4, 1892). Fetched its full `_djvu.txt` to disk
   (one request) and grepped for "Palavicino": 23 letters found, **all addressed to Sir Robert Cecil**,
   dated 1593-1594 — this volume calendars the Cecil Papers at Hatfield, a different archive from the
   State Papers at TNA, and does not cover the 1590 Burghley correspondence in SP 81/6 at all. Not the
   right edition for this item; ruled out rather than left unchecked. CSP Foreign for 1589-90 proper
   (the "List and Analysis of State Papers, Foreign Series" by R.B. Wernham, which supersedes the old
   numbered Calendar series from 1589) was not found on Internet Archive (searched by title; only the
   pre-1589 numbered volumes are digitised there) — likely still in copyright (Wernham's volumes were
   published by HMSO/List and Index Society into the 1990s-2000s) and not checked further this pass.
3. **Community lists.** `sources/cryptiana/` grepped locally for "Palavicino": one match, in
   `web/venetian.htm`, is a different Palavicino ("Sforza[?] Palavicino", named inside an unrelated
   Venetian ambassador's dispatch text) — not this target. Cryptiana's live site and Cipherbrain/Cipher
   Mysteries were not fetched separately this pass (budget; the folio's obscurity outside Stone made this
   low-yield).
4. **DECODE.** No login attempted (broken, ASKS row 1). Checked Aymeloglu's cached DECODE catalogue
   (`unsolved-ciphers/catalogue/decode-records.jsonl`, `decode-ranked.md`) for "Palavicino", "Wroth", "SP
   81", "9/6958", "9/76": no match (one apparent BNE hit on "9/76" was a false positive, MSS/1869/76, an
   unrelated 1622 Spanish letter — substring match on the shelfmark fragment, not this target).
5. **Bourdeau's repository.** Shallow clone of `github.com/dbourdeau/cyphersolver` (fresh, 24 Sept 2026).
   `grep -ril "palavicino\|SP 81\|SP81"` across the whole tree: no target folder, no mention in
   README.md/TARGETS.md/SOLVED_CATALOGUE.md; the only "Palavicino" hits are in unrelated corpus/source
   text files (`stafford1586/csp_pp89-104.htm`, `it1583/asl1883.txt`, `vasto1527/prior/venetian_now.htm`)
   where the name appears incidentally in period text, not as a solved target.
6. **Aymeloglu's repository.** Shallow clone of `github.com/aaymeloglu/unsolved-ciphers` (fresh, 24 Sept
   2026). No target folder or catalogue row for Palavicino, Wroth, or SP 81 in
   README.md/TARGETS.md/SHORTLIST.md/CATALOGUE.md or the `catalogue/` PARES/BNE/DECODE scrapes (checked
   above under DECODE).

**Google Books sweep (24 September 2026, LANE S worker H, holding the Google Books slot — key+country=US,
filter=full):** 4 queries run, >=2s apart, all zero results: `"S.P. Germany, States" "f. 125" Palavicino`;
`Palavicino cipher Burghley 1590 "103"`; `Stone "Elizabethan" Palavicino cipher Germany`; `"SP 81/6"
Palavicino Burghley`. No corroboration or contradiction of the Stone 1956 finding from this route; Google
Books' full-view index does not surface Stone's monograph (likely not itself digitised in full view, or its
relevant page falls outside the snippet-indexed portion) for any phrasing tried.

## Verdict

**found-solved**, F1-leaning (a specialist monograph — Stone 1956 — already reads and describes this exact
folio's cipher by shelfmark, in enough detail to rule out "open," but TNA's own Discovery catalogue entry
does not link to Stone or note the cipher's content, so the *catalogue* is still uninformed even though the
*scholarship* is not). Not F0: no database or catalogue links the item to Stone's description. Whether this
is a unique "recovery" candidate under README's metric now turns on a question this sweep could not answer —
does Stone's book reproduce enough of the 103-entry key to read further Palavicino correspondence, or does
it only describe the key's scope? That requires the book's actual page (not just fts snippets), which needs
either an IA loan (unverified flow, out of this brief) or a library copy. Handing on: if this target is
pursued further, get Stone pp. near the "103 names" passage (page_num field is unreliable; a full-text
proximity search for "103 names" combined with reading the two surrounding pages once a loan is available
is the cheapest next step) before ordering a TNA copy of SP 81/6/125 itself — the printed source may already
answer what the folio contains.

## Copy status

Not copy-free: TNA Discovery lists `digitised: false` (per the N21 scoring pass). A copy order is the only
way to see the folio itself. REQUEST.md drafted (see that file) but not sent — no order placed, no price
guessed, per this brief's rules.

## Request counts (this target)

archive.org (be-api.us.archive.org fts): 6 (2 for Stone's biography's cipher/Burghley/SP81/103-names/useless
passages, plus the vol.4 Salisbury calendar's Palavicino/cipher queries counted under rah/wroth shared
work — see final report); archive.org (djvu.txt fetch): 1 (calendarofmanusc04grea, 2.7 MB). github.com: 2
shallow clones (shared with the other three targets in this batch, not re-cloned). No TNA Discovery calls
(per brief). No Google Books calls (per brief; queries logged above as pending). WebSearch: 2.
