open

# Chesterfield and Cumberland, ciphers on the Anglo-Dutch/Orange succession question — TNA SP 87/23/41, 51, 70 (1747)

QUEUE row: N15 (sources/solver-diffs/2026-09-23-non-decode-hits.tsv, "Candidates not on DECODE").

## Source

TNA, State Papers Foreign, Military Expeditions, **SP 87/23**, The National Archives, Kew. Catalogue text
quoted verbatim from the Discovery API (`discovery.nationalarchives.gov.uk/API/search/records`, fetched 24
September 2026):

> **SP 87/23/41** (21 July 1747, id C9040584): "**Chesterfield to Cumberland, partly in cipher**: the king's
> surprise that the prince of Orange has taken the command from Waldeck and given it to Cronstrom. Cumberland
> was correct not to show dissatisfaction. The king awaits a detailed peace proposal from the French court.
> His disappointment at the weakness of the Austrian contingent."
> **SP 87/23/51** (28 July 1747, id C9040876): "**Chesterfield to Cumberland, partly in cipher**: the king's
> decision on Saxe's letter will be delayed until the next post. A copy of the letter has been sent to
> Sandwich to show to the prince of Orange. Cumberland is not to release any French prisoners while M
> Seigneur continues to make difficulties."
> **SP 87/23/70** (14 August 1747, id C9046270): "**Cumberland to Chesterfield, partly in cipher**, enclosing
> a letter of his to the prince of Orange [SP 87/23/71] to demonstrate that he has not shown any offence at
> the Waldeck affair. He has ordered all officers to obey Cronstrom..."

## Check-solved sweep (24 September 2026)

1. **TNA Discovery, full-piece sweep for a sibling decipherment.** `tools/discovery_items.py` against
   series "SP 87" piece "SP 87/23" with terms cipher/decipher/undeciphered/duplicate (4 requests) returned
   exactly these 3 items — no other item in the piece is cipher-flagged. A class-wide phrase search for
   "deciphered" restricted to record series "SP 87" (1 request, 8 hits across the whole class, shared with
   the N14 sweep — see ciphers/sp87-newcastle-1743/NOTES.md) returned **zero** hits from piece 23 (1747):
   the nearest are SP 87/24/35 (1748, a different piece, Newcastle to Cumberland) and SP 87/32/45 (1758).
   No sibling decipherment exists in this piece. Item-details fetches (3 requests, ids
   C9040584/C9040876/C9046270; the first two needed one retry each after HTTP 202 "still processing"
   responses, both succeeded on retry, no further retries needed) confirm `note: null` (nothing beyond the
   search description) and **`digitised: false`** for all three.
2. **Print (the decisive finding for this cluster).** As the brief anticipated, Bonamy Dobrée's standard
   edition, *The Letters of Philip Dormer Stanhope, 4th Earl of Chesterfield* (1932, 6 vols), is **not** on
   archive.org in a directly matching edition search for "Letters of Lord Chesterfield" + Dobrée, but a
   broader search (creator:Dobree AND Chesterfield) found it under its full title: vols. 1-2 only
   (`lettersofphilipd0001bona`, `lettersofphilipd0002bona`), both **lending-only**
   (`access-restricted-item: true`) — not opened this sweep (brief: no logins). Vols. 3-6 not found on
   archive.org at all. Used the no-login full-text search API instead
   (`be-api.us.archive.org/fts/v1/search`, 4 requests: "Cronstrom", "Waldeck", "Cumberland", "\"Chesterfield
   to Cumberland\"" against vol. 2) per the access playbook's allowed no-login route. Result: **vol. 2 of
   Dobrée's edition discusses the exact same episode as SP 87/23/41 and /70** — the same names in the same
   context: "The Prince of Waldeck was put in command of the Dutch troops..."/"the appointing of the Prince
   of Waldeck to command in chief the Dutch..."/"General Cronstrom said beforehand that he would quit, but
   has since..."/"the English offered the Duke of Cumberland [command]... Cumberland was held to be in
   command with Königsegg ad latus" — and one highlighted snippet is explicitly sourced "**(S.P. Holland**"
   (State Papers Holland, SP 84, a different but related series), showing Dobrée's editorial apparatus cites
   official State Papers directly for this affair. No exact-phrase hit for "Chesterfield to Cumberland" (0
   results) — the fts phrase-search syntax may not be reliable, not evidence of absence. **The `page_num`
   field returned by this API (618) equals the item's own `imagecount` (618, confirmed via
   `archive.org/metadata`) for every hit** — the known finding recorded in CLAUDE.md (be-api's page_num is
   not a real locator) reproduces exactly here, so this cannot be cited as a page number, only as "the term
   is present somewhere in vol. 2." Whether Dobrée reproduces or merely narrates/footnotes the Waldeck-
   Cronstrom-Cumberland affair — and whether he draws on SP 87/23 specifically as opposed to SP 84 (Holland)
   or Cumberland's own Cabinet papers — cannot be determined from search snippets alone.
3. **Community lists.** `sources/cryptiana/` grepped for "SP 87/23"/"Cronstrom"/"Chesterfield ...
   Cumberland": no hit anywhere in the cached snapshot.
4. **DECODE.** `ay/catalogue/decode-catalog.csv` grepped for "SP 87/23"/"Chesterfield"/"Cronstrom": no
   record.
5. **Bourdeau.** `cs-recheck/CATALOGUE.md` and `SOLVED_CATALOGUE.md` grepped for the same terms: no hit.
6. **Aymeloglu.** `ay/CATALOGUE.md` grepped for the same terms: no hit.

Requests: discovery.nationalarchives.gov.uk 9 (4 term-searches on the piece, 3 item-details fetches with 2
retries after HTTP 202, 1 class-level "deciphered" phrase search shared with N14), archive.org 2
(advancedsearch for the Dobrée edition, 2 queries counted as 1 request pair; metadata fetch for imagecount),
be-api.us.archive.org (fts) 4.

## Edition risk

**Real and unresolved, not moot.** Unlike N9/N10/N4/N5 in earlier sweeps, this is not a case of a scout
conflating two unrelated items: Dobrée's edition genuinely discusses the identical episode (Waldeck's
removal, Cronstrom's appointment, Cumberland's non-reaction) that SP 87/23/41 and /70 report, in the same
volume, with at least one State Papers citation nearby. Whether that amounts to *printing the cipher
letters themselves* (which would close this target) or *narrating the same events from other sources*
(which would leave it open) cannot be settled without reading vol. 2 around the Waldeck/Cronstrom passage —
blocked behind archive.org's lending restriction this session.

## Verdict

**Open, stage 2 verified unsolved (conditional: Dobrée vol. 2 pp. near the Waldeck/Cronstrom passage
unread, lending-restricted; vols. 3-6 of the same edition not located; HMC/Cumberland Cabinet papers not
searched).** Three items, "partly in cipher" per the catalogue's own wording for all three, none digitised,
no sibling decipherment in the piece or the wider SP 87 class for 1747, no match on DECODE, Bourdeau's or
Aymeloglu's working lists, or Tomokiyo's cached pages — but a live, specific print-edition lead not yet
closed. Not "new"; not "unpublished" — a search result, not a discovery (rule 10).

## Next

Before any TNA copy order: get inside Dobrée vol. 2 (archive.org loan, if IA credentials are fixed, or a
library copy) at the Waldeck/Cronstrom passage to determine whether it quotes SP 87/23/41 or /70 verbatim
or only narrates the same events from SP 84/other sources — the cheapest possible resolution of this
target, per rule 2 and the access playbook's edition-first instruction, and cheaper than a copy order for
all three items. If Dobrée turns out not to print the cipher text itself, then TNA page copies for all
three (`digitised: false`, no other route). Not batched into REQUEST.md this session (brief scope: record
findings and stage only).
