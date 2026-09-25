open
Coxe's *Memoirs of ... Henry Pelham* (1829, both vols., archive.org djvu read and grepped in full by this worker) shows no hit for "Munchberg" or "'101'" and no dated letter matching 6 May/1 Jul/2 Sept 1743, and a fresh Google Books full-text search (key+country=US, 25 Sept 2026) for "Munchberg" found only an unrelated 1759 place-name hit, so no printed source read by this worker names this cluster.

## Check-solved (LANE CX2, 25 Sept 2026)

Six-source sweep per .claude/briefs/check-solved.md, worker CX2-SP87A, re-run fresh:

1. **Web search.** `"SP 87/13" Newcastle Carteret 1743 cipher Munchberg solved` (1 query): no solve claim found; hits are TNA Discovery catalogue pages for SP 87/13/18 (confirming the same catalogue text already on file, plus a neighbouring item SP 87/13/64, "Munchberg reporting that he had been in Paris for three weeks... Holland, Lille, Douai and Valenciennes" — a fourth Munchberg-network item in the same piece, not previously logged, still an intelligence report *about* the agent, not a decipherment of the covering despatches) and `dbourdeau.github.io`'s index page only. No model-solve announcement.
2. **Standard edition/calendar, read by this worker.**
   a. TNA Discovery item-details re-fetched today for all three items (C9188861, C9188919, C9188928): `digitised: false` for all three, unchanged from 23 Sept 2026.
   b. Coxe, *Memoirs of the Administration of ... Henry Pelham* (1829, 2 vols, archive.org `memoirsofadminis01coxeuoft`/`memoirsofadminis02coxe`, public domain, no login needed) — re-confirmed the 23 Sept finding by re-reading the already-downloaded djvu text: no hit for "Munchberg" or "'101'" in either volume, and none of Coxe's dated 1743 letters falls on 6 May, 1 Jul or 2 Sept (nearest: 31 May, 13 Jul, 4/8/16 Sept).
   c. **New this pass:** Google Books full-text search (key+country=US) for `"Munchberg" Newcastle Carteret` returned only 2 hits, both *The London Chronicle* (1759, ids `lAjmKU5dL9IC`/`QzlSAAAAYAAJ`), an unrelated news item about the Bavarian town of Münchberg near Nuremberg during the Seven Years' War — not the 1743 spy codename, ruled out by date and context. A second query, `"Carteret and Newcastle" Basil Williams`, returned 300 results but none with a usable snippet for this book specifically (its own text is not indexed for full-text search on Google Books either) — Basil Williams's *Carteret and Newcastle* (1943), the dedicated modern monograph, remains genuinely unread: lending-only on archive.org (`carteretnewcastl0000will`) and not full-text searchable on Google Books. This is the one standing edition risk for this cluster, unchanged from 23 Sept 2026.
3. **Community lists.** `sources/cryptiana/` regrepped for "Munchberg", "Carteret Newcastle", "SP 87/13": zero hits anywhere in the cached snapshot (no change from 23 Sept).
4. **DECODE.** `sources/decode/` TSVs (fetched 24 Sept 2026) regrepped for "SP 87", "Munchberg", "Carteret", "Newcastle", "Dettingen": no record.
5. **Bourdeau.** Fresh shallow clone of `github.com/dbourdeau/cyphersolver` (25 Sept 2026) grepped for "SP 87", "Munchberg", "Carteret", "Newcastle", "Dettingen": no target folder or catalogue row matches; the only "Newcastle/Carteret" text found (`catalogue.json` id 78, BL Add MS 32305) is a verify-note suggestion pointing elsewhere ("Needs the key or a clear copy: Newcastle/Carteret papers, SP 107, SP 78") on a *different* item (Paris 1719 and Carré 1742-45 code letters, unrelated correspondents), not a hit on our cluster.
6. **Aymeloglu.** Fresh shallow clone of `github.com/aaymeloglu/unsolved-ciphers` (25 Sept 2026): 8 targets total, none matching this cluster's correspondents or shelfmark.

**Sibling decipherment re-check.** TNA Discovery class-wide phrase search for "deciphered" restricted to record series "SP 87" re-run today: 8 hits total (SP 87/2/70, 5/62, 40/121, 40/77, 24/35, 36/13, 32/45, 40/76), unchanged from 23 Sept 2026 and none in piece 13 (1743) — no sibling decipherment for this cluster. The full-piece cipher-term sweep from 23 Sept (8 items in piece 13, including the newly re-noted SP 87/13/64 Munchberg report) still shows none carrying "deciphered".

**Verdict: open, unchanged.** Coxe checked exhaustively and negative by name/date; no full-text route into Basil Williams's *Carteret and Newcastle* (1943), the standing edition risk, found this pass (lending-only, not Google-searchable); no community-list, DECODE, Bourdeau or Aymeloglu match; no model-solve announcement. Not "new"; not "unpublished" — a search result, not a discovery (rule 10).

**Requests today (25 Sept 2026):** discovery.nationalarchives.gov.uk 3 (item-details re-fetch, >=1.6s apart); archive.org 0 (Coxe djvu already on disk from 23 Sept, re-read not re-fetched); googleapis.com/books 2 (key+country=US); github.com 2 (git-protocol shallow clones). WebSearch: 1 query. No logins, no credentials printed.

---

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
