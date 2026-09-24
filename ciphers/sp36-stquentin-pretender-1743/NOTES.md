open

# St Quentin to "the Pretender" — TNA SP 36/61/53

QUEUE row: N54 (sources/solver-diffs/2026-09-23-non-decode-hits.tsv, "Candidates not on DECODE").

## Source

The National Archives, Kew, **SP 36/61/53** (State Papers Domestic, George II), folio 53, 1743 June 3.
TNA Discovery full record (fetched 24 Sept 2026 via `tools/discovery_items.py "SP 36" "SP 36/61" cypher
decipher key`, id C7768193): "Folio 53. St. Quentin to [the Pretender] with news of the general situation
concerning the Austrian troops; the Queen of Hungary, King of Sardinia, and the Marechals de Broglie and de
Noailles. Endorsed: **Intercepted by Admiral Mathews.**" Note field (QUEUE row, not re-fetched by id this
pass): "French. Part in cypher." `digitised` not confirmed this pass (Discovery record JSON did not surface
the field for this query shape; treat as undigitised per the playbook's general TNA rule until checked by id).

The Pretender here is James Francis Edward Stuart ("the Old Pretender"), in exile; this is one of a small
cluster of intercepted Jacobite correspondence in the same piece around early June 1743 (two years before the
'45): f.18 Coghlan to Strickland (Rome), f.51 Bethune de Pologne to the Pretender, f.117 "R" on fighting for
the Pretender, f.120 D. Flyn on delivering the Pretender's letters and books to Lord Derwentwater. Admiral
Thomas Mathews commanded in the Mediterranean in 1742-44 (Toulon fleet); "St Quentin" is not otherwise
identified in the catalogue snippet and was not resolved this pass — possibly a Jacobite code name or an
alias, given the company it keeps (Coghlan, Bethune de Pologne, Flyn are all minor agents, not named
principals).

## Check-solved sweep (24 September 2026)

1. **Editions.** WebSearch (`Calendar of the Stuart Papers Royal Archives HMC volumes coverage dates 1718`,
   24 Sept 2026) confirms the Royal Archives' published *Calendar of the Stuart Papers belonging to His
   Majesty the King* (HMC, 7 vols) runs vol.1 1579-Feb 1716 through vol.7 July-Dec 1718 (with an appendix to
   Dec 1717) — the whole printed calendar ends **December 1718**, a quarter-century before this item (June
   1743). It cannot calendar this letter by date alone; not fetched further, ruled out by date range, a
   caveat not a clearance (the later, uncalendared-in-print Stuart Papers at Windsor — per rct.uk's own
   "Stuart, Cumberland and Melbourne Papers" page, fetched by title only — are the ones that would actually
   hold a duplicate or an answer, and were not searched this pass; no online finding aid reachable under this
   run's hosts). No printed correspondence
   of "St Quentin" was found by search — the name is too thin to search on its own without an identification.
   WebSearch (`"St Quentin" letter "Pretender" 1743 cipher SP 36/61 National Archives`; a second, broader
   pass): no hit naming this letter, this shelfmark, or "St Quentin" as a Jacobite correspondent; returned
   only unrelated cipher scholarship (Cryptologia/tandfonline papal- and French-cipher articles), the TNA's
   own general Jacobite-cipher blog posts (none naming this item), and a Lyon & Turnbull auction lot for an
   unrelated 1715 Jacobite cryptographic key. One TNA Collection Blog post surfaced in this and other lanes'
   searches this week, "Secret diplomatic message deciphered after..." (about a different, 1650s item per
   other targets' NOTES) — not this letter.
2. **Sibling search (TNA Discovery, same piece).** `tools/discovery_items.py "SP 36" "SP 36/61" cypher
   decipher key` returns only f.53 itself — no companion key, decipher or decipherment note elsewhere in
   SP 36/61 under those terms. A second query for "Pretender" across the same piece surfaces the four
   neighbouring intercepts above (f.18, 51, 117, 120), none flagged as cipher or carrying a decipher note.
   No sibling key or decipherment found in the piece.
3. **Community lists.** Cryptiana/Cipherbrain: web search combining "St Quentin", "SP 36/61", "cipher",
   "Jacobite" found no post naming this item; local grep of `sources/cryptiana/` for "st quentin"/"SP 36/61"
   found nothing (the one "St Quentin" hit in the corpus, `sources/cryptiana/web/spanish3.htm`, is the 1557
   Battle of St Quentin, unrelated).
4. **DECODE.** No login attempted. `sources/decode/` (records-decrypted TSV, DC1-20 documents TSV, NOTES.md)
   greped for "St Quentin"/"SP 36/61"/"Pretender" 1743: no hits.
5. **Solver repositories.** Fresh shallow clones of both (24 Sept 2026, reused for all four targets this
   pass). `dbourdeau/cyphersolver`: grep for "st.?quentin|SP 36/61" across `.md/.txt/.csv/.json` returns
   only unrelated incidental matches (a napoleon-era source text, an unrelated key-search dump, a
   sessa1593 pieces file) — none reference this item, SP 36, the Pretender's 1743 correspondence, or St
   Quentin as a Jacobite name. `aaymeloglu/unsolved-ciphers`: zero matches for any of the search terms.
6. **General web search.** As above (1). No result identifies "St Quentin" as a specific historical person,
   nor connects this letter to any published edition, calendar, or prior solve attempt.

**Host requests this pass:** discovery.nationalarchives.gov.uk 3 (>=3s apart, shared across all four targets
this run), WebSearch 2, github.com 1 shallow clone each of both repos (grepped, shared across all four
targets), sources/decode/ and sources/cryptiana/ local greps (no network).

## Verdict

**Status: open.** No printed edition or calendar reaches 1743 for the Stuart Papers series (the only
published calendar of this correspondent's papers stops at 1718, a hard exclusion by date, not a search
failure); no sibling key or decipher found in the same TNA piece under a cipher/decipher/key term search; no
community list, DECODE record, or solver-repository entry names this item or "St Quentin." The correspondent's
identity is unresolved — "St Quentin" was not matched to a known Jacobite agent or code name this pass, which
would be the first useful step for any future editions check (a Stuart Papers finding aid or the Windsor
Royal Archives catalogue, both outside this run's hosts).

**Copy status:** no online image located; `digitised` field not directly confirmed by record id this pass
(treat as **copy-order**, consistent with every other item in this TNA series checked this week). See
REQUEST.md.

**Recommended next steps (not run this pass):** (1) identify "St Quentin" via the Windsor Royal Archives'
own online Stuart Papers finding aid or a Jacobite prosopography, since a name match would open a proper
editions search; (2) confirm digitisation status for f.53 directly by Discovery record id; (3) if a future
worker holds a Jacobite-studies journal index (the JSTOR/OpenAlex slot), search for "St Quentin" plus
"Pretender" plus 1743 — not run this pass, outside this lane's hosts.
