open

# Z Ball to an unknown recipient, in cipher — TNA SP 36/74/1/60

QUEUE row: N62 (sources/solver-diffs/2026-09-23-non-decode-hits.tsv, "Candidates not on DECODE").

## Source

The National Archives, Kew, **SP 36/74/1/60** (State Papers Domestic, George II), folio 60, 1745 Nov. 19 (TNA
Discovery, fetched 24 Sept 2026, id C12771598; `digitised: false` confirmed by direct record fetch; no separate
`note` field). Scope content: "Folio 60. Z Ball to [unknown]. In cipher." 19 Nov. 1745 falls in the middle of the
Jacobite army's advance into England after crossing the border (the army took Carlisle 15 Nov, reached Preston
20 Nov, Manchester 28 Nov) — this piece is squarely intelligence/intercept material from the government side of
the '45 crisis, not Jacobite Rome-court correspondence (so HMC's *Calendar of the Stuart Papers* at Windsor,
which covers James Francis Edward Stuart's own court to Dec. 1718 only, does not apply here either).

## Check-solved sweep (24 September 2026)

1. **Editions.** The printed *Calendar of State Papers Domestic* series ends in Anne's reign (does not reach
   George II, 1745) — a hard exclusion by date, not a search failure, the same shape as sp36-stquentin's
   Stuart Papers exclusion and sp81-roe's Richardson 1740 exclusion. No other calendar or edition was located
   that covers SP 36 intercept material for Nov. 1745 specifically. "Z Ball" was not identified as a known
   historical figure by web search (`"Z Ball" OR "Zachary Ball" 1745 Jacobite intercepted letter cipher SP
   36`); results surfaced only general Jacobite-1745 research aids (jdb1745.net, TNA's own Jacobite Risings
   research guide) with no mention of this name or item.
2. **Sibling search (TNA Discovery).** `tools/discovery_items.py "SP 36" "SP 36/74" decipher` and `... Ball`
   return **only the target record itself** — no companion key or decipher elsewhere in the piece. A TNA-wide
   search (not piece-restricted) for the literal string `"Z Ball"` also returns only this one record.
   Government-side ciphers of this period were normally deciphered by the Deciphering Branch (Edward Willes)
   and often kept in **SP 106**; a targeted SP 106 search for this specific item was not run this pass (outside
   this run's search-term budget) — flagged as the next useful TNA query, not a clearance.
3. **Community lists.** WebSearch as above; local grep of `sources/cryptiana/` for "ball"/"SP 36/74": no
   relevant hits (matches, if any, are unrelated).
4. **DECODE.** No login attempted. `sources/decode/` greped for "Ball"/"SP 36/74"/"Z Ball": no hits.
5. **Solver repositories — a direct hit, corroborating rather than clearing.** Fresh shallow clone of
   `dbourdeau/cyphersolver` (24 Sept 2026, shared across this pass's four targets):
   `cyphersolver/oldest/scan_2026-09-23/hard_targets.md` — Bourdeau's own 23 Sept 2026 scan of "hard unsolved
   targets outside DECODE" — lists this **exact item** under "10. TNA intercepts flagged 'undeciphered'":
   > "Also: SP 78/111/93 (f. 212), a French letter 'entirely in cipher', 20/30 Sep 1642; SP 35/46/59
   > 'Undecyphered paper', c. 1723 (Atterbury plot); **SP 36/74/1/60 'Z Ball to [unknown]. In cipher', 19 Nov
   > 1745 (Jacobite rising).**"
   > "Images: State Papers Online (Gale, subscription) or TNA copy order; not free. Prior art: TNA catalogue
   > says undeciphered; nothing in print found."
   This is not a solve or a claim of novelty — it is Bourdeau's own team independently reaching the same
   verdict (unsolved, not free online, "nothing in print found") one day before this sweep, on their own
   search. `aaymeloglu/unsolved-ciphers`: zero matches for "Ball"/"SP 36/74."
6. **General web search.** As (1). No result ties a decipherment, key, or prior reading to SP 36/74/1/60
   specifically.

**Host requests this pass:** discovery.nationalarchives.gov.uk 4 (search x2, record detail x1, TNA-wide "Z
Ball" search x1, >=3s apart, shared budget with the other three targets this run), WebSearch 2, github.com 1
shallow clone each of both repos (grepped, shared across all four targets), sources/decode/ and
sources/cryptiana/ local greps (no network).

## Verdict

**Status: open.** No printed calendar reaches George II-era SP 36 (a hard date exclusion); "Z Ball" is
unidentified. No sibling key or decipher found under this piece's own search terms (an SP 106 Willes-branch
search was not run this pass and is the natural next step). No community list or DECODE record names this
item. dbourdeau/cyphersolver's own 23 Sept 2026 scan independently lists this exact shelfmark as unsolved and
not found in print, one day before this check — a second, independent negative search, not a clearance, and
not itself grounds for "never printed" wording (CLAUDE.md rule 10).

**Copy status:** no online image located; `digitised: false` confirmed by direct record fetch (id C12771598).
Bourdeau's scan separately notes the item is also on State Papers Online (Gale, subscription), not a free
route. **Copy-order.** See REQUEST.md.

**Recommended next steps (not run this pass):** (1) search TNA Discovery for an SP 106 (Deciphering Branch)
key or decipher tied to this correspondent or to Nov. 1745 Jacobite intercepts generally; (2) identify "Z Ball"
via Jacobite prosopography (jdb1745.net, the Jacobite Database of 1745, surfaced this pass but not queried
directly) or the government's own intercept-handling records; (3) once imaged, check whether the hand or cipher
matches other Nov. 1745 SP 36/74 intercepts in the same folder.
