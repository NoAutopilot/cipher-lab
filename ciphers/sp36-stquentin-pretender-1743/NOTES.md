open
James Browne, *A History of the Highlands and of the Highland Clans* vol. 2 (archive.org `vol2historyofhig00brow`, djvu text grepped whole by GF4-BATCH10 (account-4), 3 Oct 2026), whose appendix prints Stuart Papers from Windsor for 1743 (nos. VIII-XXIII, pp. 440-452, Feb-Dec 1743), contains no letter from "St Quentin" (0 hits for "Quentin" in the volume) and no Mathews intercept; Browne vols 1 and 3 (`historyofhighla01brow`, `b29335206_0003`) and *Memorials of John Murray of Broughton* 1740-47 (SHS 1898, `memorialsofjohnm00murr`) also 0 hits for "Quentin".

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

## While waiting (27 Sept 2026, WAIT-PASS-B)

Waits on: a TNA page-copy order for SP 36/61/53 (REQUEST.md, since 24 Sept 2026).

- S: confirm digitisation status of SP 36/61 f.53 by record id -- not yet checked this pass, may already be online, before ordering -- tools/discovery_items.py.
- S: identify 'St Quentin' against the already-fetched Jacobite context (Coghlan, Bethune de Pologne, Flyn) via a targeted name search.
- S: cross-check the four neighbouring 1743 intercepts (f.18, 51, 117, 120) in the same piece for any reference to 'St Quentin', not yet compared against each other.

## Check-solved addendum (GF4-BATCH10 (account-4), 3 Oct 2026)

Gate fix for the missing standard-edition citation. No printed calendar covers SP 36 for 1743 (the State Papers Domestic calendars
stop before George II's reign, the HMC *Stuart Papers* calendar ends Dec 1718, see the 24 Sept sweep), so this pass read the printed
selections of the Stuart Papers that do reach 1743, by full djvu-text grep (archive.org, no login): Browne, *History of the Highlands*
vols 1-3 (vol. 2 appendix nos. VIII-XXIII, pp. 440-452, prints the Chevalier's and his agents' letters of Feb-Dec 1743 -- Sempil,
O'Bryen, Lord John Drummond, Albano 12 June 1743 -- none from or naming "St Quentin", no Mathews intercept); and *Memorials of John
Murray of Broughton* (SHS 1898; 55 hits for "1743", appendix letters of 23 Dec 1743, p. 493): 0 hits for "Quentin" in all four
volumes; "Coghlan" and "Flyn" (the neighbouring f.18/f.120 correspondents) also 0. TNA Discovery record C7768193 re-fetched by id:
`digitised: false`, note "French. Part in cypher." (closes the 24 Sept "digitised not confirmed" caveat). Verdict: **open**,
unchanged -- a search result, not a discovery (rule 10). Still unread: the Windsor Stuart Papers themselves (uncalendared after 1718).

## Web and blog check (GF4-BATCH10 (account-4), 3 Oct 2026)

WebSearch, 3 Oct 2026: (1) `"St Quentin" Jacobite agent 1743 letter Pretender intercepted Admiral Mathews` -- Wikipedia pages
(Mathews, James Francis Edward Stuart, Dudley Bradstreet), Thomson's *Memoirs of the Jacobites* (Gutenberg), a freemasonry article;
none names St Quentin as a correspondent or this letter. (2) `"SP 36/61" cypher Pretender 1743` -- TNA catalogue pages for SP 36/62
items (C7768257, C7768333, C7768334: the Pretender's order to Waters, commission to Campbell, 23 Dec 1743 proclamation), not f.53;
no decipherment. (3) site-restricted to **Cipherbrain** (scienceblogs.de), the **Cryptiana blog** (cryptiana.blogspot.com) and
**Cipher Mysteries** (ciphermysteries.com), `Jacobite cipher 1743 Pretender intercepted letter` -- Cryptiana forum front page and
unrelated Cipher Mysteries posts (Milanese letters, La Buse, d'Agapeyeff); no post on this item, so no comment thread to read. (4)
the folder's title phrase `St. Quentin to the Pretender 1743 Austrian troops Queen of Hungary King of Sardinia Broglie Noailles` --
War of the Austrian Succession background only. No decipherment or clear text of SP 36/61/53 found on the open web.

## Premise check (GF4-BATCH10 (account-4), 3 Oct 2026)

(a) Folder's own mentions of a decipherment: **not found** -- NOTES.md and REQUEST.md mention none; "Part in cypher" is the only
cipher note. (b) Other solvers' working files: **not found** -- no SP 36/61 or St Quentin item in Bourdeau's or Aymeloglu's
repository (24 Sept clones, sweep item 5). (c) Physical neighbours: **unreachable as images** (`digitised: false`); by catalogue, the
24 Sept piece search found no key, decipher or decipherment in SP 36/61, and the neighbouring intercepts f.18, 51, 117, 120 carry no
cipher note. (d) Recipient's side: **not found** -- the recipient's (the Chevalier's) papers in print for 1743 (Browne vol. 2 appendix
pp. 440-452; Murray of Broughton's *Memorials*) carry no St Quentin letter; the original Windsor Stuart Papers are unread
(uncalendared after 1718). Item stays `open`.

## While waiting (3 Oct 2026, GF4-BATCH10)

Waits on: the TNA page copy of SP 36/61/53 (REQUEST.md). Digitisation now confirmed false by record id (3 Oct 2026), so the first
WAIT-PASS-B bullet above is done.

- S: be-api full-text search for "St. Quentin" with "Chevalier" across the Royal Archives' published Stuart-papers selections
  (Lang's *Pickle the Spy*, Mahon's *History* appendices) to identify the correspondent -- no login, tools/print_check.py.

Requests this pass (3 Oct 2026): discovery.nationalarchives.gov.uk 1; archive.org 7 (3 advancedsearch, 4 djvu text);
be-api.us.archive.org 2 (>=1.6 s apart). WebSearch 4.

Gate re-run (GF4-BATCH10, 3 Oct 2026): `sp36-stquentin-pretender-1743: open (line 1) -- edition/page or full-text-search citation found within 6 lines`, exit 0 (was exit 1: no standard-edition citation). `tools/next_steps.py --wait-only | grep sp36-stquentin`: no line.

## R9-SRCH (6 Oct 2026; worker session_014oHN8M2YCqbmoiEspiHbSg, Sonnet, LANE LANE-RUN9-account-4 -- committed by the lane orchestrator from the worker's own text, the worker's push being blocked)

Ran the folder's own free step ("While waiting", GF4-BATCH10 "S:"): "St. Quentin" with "Chevalier" in published Stuart Papers selections. Question: who is the St. Quentin of SP 36/61/53 (1743)?
Route: archive.org `_djvu.txt` whole-volume grep (`-L` needed, the bare download URL 302s) plus `be-api.us.archive.org/fts/v1/search?q=<term>&identifier=<id>`; no login.
Texts grepped: Lang, *Pickle the Spy* (`picklespy00lang`, 646,943 B): "Quentin" 5 raw hits, all OCR-adjacent false matches ("aquenting", "frequenting"), 0 for the name; "Chevalier" 28, none near a St. Quentin. Lang, *Companions of Pickle* (`companionsofpick00lang`, 563,631 B): Quentin 0, Chevalier 10. Mahon, *History of England* 1713-1783 vol. VI (`bub_gb_HyJTAAAAcAAJ`, 920,488 B): Quentin 0, Chevalier 1; (`bub_gb_4CFTAAAAcAAJ`, 892,695 B, volume not identified from its OCR header): Quentin 0, Chevalier 1; `bub_gb_WiRTAAAAcAAJ_2` returned 404 (not read).
be-api, items `picklespy00lang`, `companionsofpick00lang`, Browne `historyofhighla03brow`/`04brow`, HMC Stuart Papers `calendarofstuart07grea`, Taylor *Stuart Papers at Windsor* `stuartpapersatwi0000tayl`: "St. Quentin" 0, "St Quentin" 0 in all six; control "Chevalier" returns 1 in all six, but it is a per-item hit count, not a count of matches, so it shows the index answers, not that these OCRs are free of the name. HMC Stuart Papers vols stop at Dec 1718 (see 24 Sept sweep), so that item is a non-test for 1743.
Result: not found in these sources, searched by whole-volume grep and be-api full text on 6 Oct 2026. No correspondent identified. Mahon vol. covering 1743 (vol. III of the 7-vol. set) and Taylor's book not read in full (be-api only). Grades: no reading made. A search result, not a verdict.
Requests: archive.org 11 (incl. 4 advancedsearch, 1 404), be-api.us.archive.org 18, all >=1.7 s apart; no 429/403.
Verdict: open, unchanged; next step remains the TNA page copy (REQUEST.md).
(Same job, other three folders: sp78-doncaster-1621, sp87-chesterfield-1747 and sp87-newcastle-1743 had their named step already run by R7-DONC / R7-CHEST / R7-NEWC on 6 Oct 2026; not re-run, nothing added.)
