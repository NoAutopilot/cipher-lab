open

# Newcastle to Carteret, ciphers around the Dettingen campaign — TNA SP 87/13/18, 76, 85 (1743)

QUEUE row: N14 (sources/solver-diffs/2026-09-23-non-decode-hits.tsv, "Candidates not on DECODE").

## Source

TNA, State Papers Foreign, Military Expeditions, **SP 87/13**, The National Archives, Kew. Catalogue text
quoted verbatim from the Discovery API (`discovery.nationalarchives.gov.uk/API/search/records`, fetched 24
September 2026):

> **SP 87/13/18** (1743 May 6, id C9188861): "Newcastle to Carteret: he encloses instructions for [a spy who
> is to go by the name of] Munchberg, and a cipher for his use. He has received £200. His correspondence
> with '101' [undeciphered]. Ascendancy of Nouailles at Versailles. **Marked 'most secret' and 'in
> cipher'.**"
> **SP 87/13/76** (1743 Jul 1, id C9188919): "Newcastle to Carteret (**original partially in cipher**): the
> battle [Dettingen] may lead to open war between Britain and France. ... PS. on 5 July on the insecurity of
> the passage and the probability of a second battle."
> **SP 87/13/85** (1743 Sept 2, id C9188928): "Newcastle to Carteret (private and particular, **original in
> cipher**), enclosing a letter to '101' [undeciphered]. Complicated state of affairs in the north."

Note: "'101' [undeciphered]" in these descriptions refers to the unidentified code-name of a spy/agent
whose identity the cataloguer could not establish — it does not mean a decipherment of the letter's cipher
text is missing or present; it is a separate fact from the "in cipher"/"partially in cipher" note on the
covering letters themselves.

## Check-solved sweep (23 September 2026)

1. **TNA Discovery, full-piece sweep for a sibling decipherment.** `tools/discovery_items.py` against
   series "SP 87" piece "SP 87/13" with terms cipher/decipher/undeciphered/duplicate (4 requests) returned
   8 items in the piece with a cipher-related match. Besides the three target items, the piece also holds
   **SP 87/13/29, 66, 78** (Newcastle to Carteret, all referencing the same undeciphered agent '101', none
   themselves marked in cipher) and **SP 87/13/95** (Hyndford to Stair, "original partially in cipher", a
   different correspondence pair, not part of this QUEUE row). None of the 8 items in the piece carries
   "deciphered" in its description. A class-wide phrase search for "deciphered" restricted to record series
   "SP 87" (1 request, 8 hits across the whole class covering 1704-1761) returned **zero** hits from piece
   13 (1743) — the nearest are SP 87/2/70 (1704) and SP 87/24/35 (1748, Newcastle to Cumberland, a later
   correspondent pair) — confirming no sibling decipherment exists anywhere in this piece. Item-details
   fetches (3 requests, ids C9188861/C9188919/C9188928) show `note: null` for all three (no separate note
   field beyond the search description) and **`digitised: false`** for all three.
2. **Print.** The QUEUE row's own suggestion, William Coxe's *Memoirs of the Administration of the Right
   Honourable Henry Pelham* (1829, 2 vols), is on archive.org and public-domain (`memoirsofadminis01coxeuoft`,
   `memoirsofadminis02coxe`); fetched both djvu texts (2 requests) and grepped for "Munchberg", "'101'",
   "Dettingen", and the exact covering dates (May 6, July 1/5, Sept 2, 1743). "Dettingen" appears often (the
   battle narrative itself), but **no hit for "Munchberg" or "101" in either volume**, and none of Coxe's
   dated letters from 1743 falls on May 6, July 1 or Sept 2 (nearest are May 31, July 13, Sept 4/8/16). Coxe
   does reproduce a private Carteret-to-Newcastle letter of that summer (Mentz, Aug. 16-27th, 1743)
   complaining explicitly that "the goodness of our cipher is nothing as to confidential letters, unless you
   are to suppose that I put my letters in cipher myself" — confirming the correspondents' own awareness of
   weak cipher security in this period, but that letter is a different, private channel from the official
   Secretary-of-State despatches in SP 87/13, and is not one of the three target items. Basil Williams,
   *Carteret and Newcastle* (1943; reprinted 1966), the standard modern monograph on this exact relationship
   and period, is on archive.org but **lending-only** (`access-restricted-item: true`,
   `carteretnewcastl0000will`) — not opened this sweep (brief: no logins). Flagged as the main unreached
   print gap.
3. **Community lists.** `sources/cryptiana/` grepped for "SP 87/13"/"Dettingen"/"Munchberg": no hit anywhere
   in the cached snapshot. No WebSearch hit for a dedicated Cryptiana/Cipherbrain post on this cluster
   either (searched "SP 87/13 cipher Newcastle Carteret 1743").
4. **DECODE.** `ay/catalogue/decode-catalog.csv` grepped for "SP 87/13"/"Dettingen"/"Munchberg": no record.
5. **Bourdeau.** `cs-recheck/CATALOGUE.md` and `SOLVED_CATALOGUE.md` grepped for the same terms: no hit.
6. **Aymeloglu.** `ay/CATALOGUE.md` grepped for the same terms: no hit.

Requests: discovery.nationalarchives.gov.uk 9 (4 term-searches on the piece, 3 item-details fetches, 1
class-level "deciphered" phrase search — the 8th request above was folded into the class search already
counted for N15, see that folder's notes for the shared search), archive.org 2 (djvu text, Coxe vols I-II).
WebSearch: 2 queries.

## Edition risk

**Partly realized, partly open.** Coxe's Pelham Administration covers this exact period and correspondents
in detail but, checked by full-text grep, does not print these three despatches or name "Munchberg" or the
agent "101" — it draws on the Newcastle/Pelham family's private letters, not the Secretary-of-State-to-envoy
official channel these items belong to. Basil Williams's *Carteret and Newcastle* (1943), the dedicated
modern study of this exact relationship, is the standing edition risk and was not checked (lending-only,
no login used this sweep).

## Verdict

**Open, stage 2 verified unsolved (conditional: Basil Williams's *Carteret and Newcastle* unread; HMC
Newcastle papers series (Add MS 32700 vicinity) not searched).** Three items, "in cipher"/"partially in
cipher" per the catalogue's own wording, none digitised, no sibling decipherment anywhere in piece SP 87/13
or the wider SP 87 class for 1743, not found by name/date in the one printed source checked (Coxe), no match
on DECODE, Bourdeau's or Aymeloglu's working lists, or Tomokiyo's cached pages. Not "new"; not
"unpublished" — a search result, not a discovery (rule 10).

## Next

TNA page-copy order for SP 87/13/18, 76 and 85 (all `digitised: false`, no cheaper route left besides the
one unread monograph). Before ordering, a single targeted check of Williams's *Carteret and Newcastle*
(borrow route, if login is fixed, or a library copy) for "Munchberg" or "101" would be the cheapest next
print check and should happen before any copy order, per rule 2 (image over transcription) and the access
playbook's edition-first instruction. Not batched into REQUEST.md this session (brief scope: record findings
and stage only).
